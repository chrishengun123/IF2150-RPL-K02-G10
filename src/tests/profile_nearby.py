"""Profiling fitur 'layanan terdekat' (UC02). Jalankan: python tests/profile_nearby.py [jumlah_data]"""
import cProfile
import os
import pstats
import sys
import tempfile
import time

os.environ["SAFESHE_DATA_DIR"] = tempfile.mkdtemp(prefix="safeshe_prof_")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from backend.db import conn, init_db
from backend.domain.layanan import ListLayanan, Peta
from backend.seed import seed_bulk

N = int(sys.argv[1]) if len(sys.argv) > 1 else 50000
init_db(); seed_bulk(N)
peta = Peta(); peta.lokasiSekitar((-6.9175, 107.6191))


def run(use_index, reps=30):
    t = time.perf_counter()
    for _ in range(reps):
        ListLayanan().ambilLayananTersedia(peta, 10, 20, use_index=use_index)
    return (time.perf_counter() - t) / reps * 1000


print(f"Data: {N} layanan")
print(f"Sebelum (full scan)   : {run(False):8.2f} ms/permintaan")
print(f"Sesudah (bounding box): {run(True):8.2f} ms/permintaan")
with conn() as c:
    print("EXPLAIN sebelum:", [r[3] for r in c.execute("EXPLAIN QUERY PLAN SELECT * FROM layanan")])
    print("EXPLAIN sesudah:", [r[3] for r in c.execute(
        "EXPLAIN QUERY PLAN SELECT * FROM layanan WHERE lat BETWEEN ? AND ? AND lon BETWEEN ? AND ?",
        (-7.0, -6.8, 107.5, 107.7))])
print("\ncProfile (full scan, 5 kali):")
pr = cProfile.Profile(); pr.enable()
for _ in range(5):
    ListLayanan().ambilLayananTersedia(peta, 10, 20, use_index=False)
pr.disable(); pstats.Stats(pr).sort_stats("cumulative").print_stats(6)

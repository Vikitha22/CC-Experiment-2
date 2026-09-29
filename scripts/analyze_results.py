import csv
import os
import statistics
import matplotlib.pyplot as plt

PROJECT = os.path.expanduser("~/vm-vs-container-performance")
RAW = os.path.join(PROJECT, "results/raw")
PROCESSED = os.path.join(PROJECT, "results/processed")
FIGURES = os.path.join(PROJECT, "results/figures")

os.makedirs(PROCESSED, exist_ok=True)
os.makedirs(FIGURES, exist_ok=True)

# ---------- API Performance ----------
api_file = os.path.join(RAW, "api_results.csv")

with open(api_file, newline="") as f:
    api_data = list(csv.DictReader(f))

api_vm = float(api_data[0]["real_time_seconds"])
api_container = float(api_data[1]["real_time_seconds"])

api_difference = ((api_container - api_vm) / api_vm) * 100

# ---------- Startup Performance ----------
startup_file = os.path.join(RAW, "startup_results.csv")

with open(startup_file, newline="") as f:
    startup_data = list(csv.DictReader(f))

startup_times = [
    float(row["real_time_seconds"])
    for row in startup_data
]

startup_mean = statistics.mean(startup_times)
startup_min = min(startup_times)
startup_max = max(startup_times)

# ---------- Scalability ----------
scale_file = os.path.join(RAW, "scalability_results.csv")

with open(scale_file, newline="") as f:
    scale_data = list(csv.DictReader(f))

requests = [
    int(row["concurrent_requests"])
    for row in scale_data
]

response_times = [
    float(row["real_time_seconds"])
    for row in scale_data
]

# ---------- Save Summary ----------
summary_file = os.path.join(PROCESSED, "analysis_summary.csv")

with open(summary_file, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["Metric", "Value"])

    writer.writerow([
        "API VM real time (seconds)",
        api_vm
    ])

    writer.writerow([
        "API Container real time (seconds)",
        api_container
    ])

    writer.writerow([
        "API difference (percent)",
        round(api_difference, 2)
    ])

    writer.writerow([
        "Startup mean (seconds)",
        round(startup_mean, 3)
    ])

    writer.writerow([
        "Startup minimum (seconds)",
        round(startup_min, 3)
    ])

    writer.writerow([
        "Startup maximum (seconds)",
        round(startup_max, 3)
    ])

# ---------- API Graph ----------
plt.figure()

plt.bar(
    ["VM", "Container"],
    [api_vm, api_container]
)

plt.ylabel("Real Time (seconds)")
plt.title("API Performance Comparison")

plt.savefig(
    os.path.join(FIGURES, "api_comparison.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ---------- Startup Graph ----------
plt.figure()

plt.plot(
    range(1, len(startup_times) + 1),
    startup_times,
    marker="o"
)

plt.xlabel("Run")
plt.ylabel("Startup Time (seconds)")
plt.title("Container Startup Time")

plt.savefig(
    os.path.join(FIGURES, "startup_time.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ---------- Scalability Graph ----------
plt.figure()

plt.plot(
    requests,
    response_times,
    marker="o"
)

plt.xlabel("Concurrent Requests")
plt.ylabel("Real Time (seconds)")
plt.title("Container Scalability")

plt.savefig(
    os.path.join(FIGURES, "scalability.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Analysis completed successfully.")
print()
print(f"API difference: {api_difference:.2f}%")
print(f"Average startup time: {startup_mean:.3f} seconds")
print(f"Minimum startup time: {startup_min:.3f} seconds")
print(f"Maximum startup time: {startup_max:.3f} seconds")
print()
print(f"Summary saved to: {summary_file}")
print(f"Graphs saved to: {FIGURES}")

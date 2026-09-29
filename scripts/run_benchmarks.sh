#!/bin/bash

PROJECT="$HOME/vm-vs-container-performance"
RAW="$PROJECT/results/raw"

echo "======================================"
echo " VM vs Container Benchmark Automation"
echo "======================================"

echo ""
echo "Running CPU benchmark..."
sysbench cpu --threads=4 --time=10 run \
  | grep -E "events per second|total time|total number of events" \
  > "$RAW/automation_cpu.txt"

echo "Running memory benchmark..."
sysbench memory --threads=4 --time=10 run \
  | grep -E "transferred|MiB/sec|total operations" \
  > "$RAW/automation_memory.txt"

echo ""
echo "Benchmark automation completed."
echo "Results saved in:"
echo "$RAW"

# Performance Analysis of Virtual Machines and Containers

## Overview

This experiment evaluates the performance of workloads running in a Virtual Machine (VM) and Docker Container environment.

The analysis covers CPU, memory, disk I/O, network throughput, application response time, container startup time, and application scalability.

The experiment was conducted using Ubuntu 24.04 running inside VMware Workstation with Docker installed for container-based benchmarking.

## Objectives

- Measure CPU performance
- Measure memory performance
- Measure disk I/O performance
- Measure network throughput
- Compare FastAPI application performance
- Measure container startup time
- Evaluate application scalability
- Automate benchmark execution
- Analyze and visualize the collected results

## Experimental Environment

| Component | Configuration |
|---|---|
| Host OS | Windows 11 Pro |
| Virtualization | VMware Workstation |
| VM OS | Ubuntu 24.04 |
| CPU | 4 vCPUs |
| Memory | 8 GB |
| Disk | 60 GB |
| Container Platform | Docker |
| CPU Benchmark | Sysbench 1.0.20 |
| Disk Benchmark | fio 3.36 |
| Network Benchmark | iperf3 3.16 |
| Programming Language | Python 3.12 |
| Application Framework | FastAPI |
| API Server | Uvicorn |

## Benchmark Methodology

The experiment was divided into system-level and application-level performance testing.

### System-Level Performance

- CPU
- Memory
- Disk I/O
- Network throughput

### Application-Level Performance

- FastAPI response time
- Container startup time
- Application scalability

All benchmark measurements were stored as raw results and analyzed using Python.

## CPU Performance

CPU performance was measured using Sysbench with four threads for ten seconds.

The benchmark records events per second, execution time, total events, and latency.

## Memory Performance

Memory throughput was measured using Sysbench with four threads for ten seconds.

The benchmark records memory transferred, throughput, and total operations.

## Disk I/O Performance

Disk performance was measured using fio with a 1 GB test file, 1 MB block size, direct I/O, and a 10-second read/write workload.

The benchmark records read bandwidth, write bandwidth, IOPS, and latency.

## Network Performance

Network throughput was measured using iperf3.

The measured throughput for the tested local container networking path was approximately:

**53.1 Gbits/sec**

This represents the tested local host/container networking path and not external Internet bandwidth.

# FastAPI Application Benchmark

A FastAPI application was developed for application-level performance testing.

The application contains two endpoints:

### `/`

Returns a simple JSON response.

### `/compute`

Performs a CPU-intensive calculation by computing the sum of squares for one million integers.

The `/compute` endpoint was tested in both the VM and Docker container environments.

# Performance Analysis

## FastAPI Response Time

| Environment | Real Time |
|---|---:|
| VM | 0.095 s |
| Container | 0.091 s |

The measured difference for this test was **-4.21%**.

### Performance Comparison

![Performance Analysis](./results/figures/performance_analysis.png)

The graph provides a visual comparison of the measured FastAPI response time between the VM and container environments.

## Container Startup Time

Container startup time was measured across three independent runs.

| Run | Real Time |
|---|---:|
| 1 | 0.699 s |
| 2 | 0.622 s |
| 3 | 0.621 s |

### Startup Statistics

| Metric | Time |
|---|---:|
| Average | 0.647 s |
| Minimum | 0.621 s |
| Maximum | 0.699 s |

![Startup Time](results/figures/startup_time.png)

## Scalability Analysis

The FastAPI application was tested with increasing numbers of concurrent requests.

| Concurrent Requests | Real Time |
|---:|---:|
| 10 | 0.787 s |
| 20 | 1.513 s |
| 50 | 3.867 s |

![Scalability](results/figures/scalability.png)

The results show how execution time changes as the number of concurrent requests increases.

# Results Summary

| Metric | Result |
|---|---:|
| VM API response time | 0.095 s |
| Container API response time | 0.091 s |
| API measured difference | -4.21% |
| Average startup time | 0.647 s |
| Minimum startup time | 0.621 s |
| Maximum startup time | 0.699 s |
| 10 concurrent requests | 0.787 s |
| 20 concurrent requests | 1.513 s |
| 50 concurrent requests | 3.867 s |
| Network throughput | 53.1 Gbits/sec |

# Automation

Benchmark execution was partially automated using:

scripts/run_benchmarks.sh

The script runs CPU and memory benchmarks and stores the extracted results.

The analysis was performed using:

scripts/analyze_results.py

The analysis generates summary statistics and performance graphs.

# Key Observations

- CPU, memory, disk, and network workloads were benchmarked.
- A FastAPI workload was used for application-level testing.
- VM and container API response times were measured using the same workload.
- Container startup time was measured over multiple runs.
- Application scalability was evaluated with increasing concurrent requests.
- Raw benchmark data was preserved for reproducibility.
- Performance graphs were generated from the collected measurements.

# Conclusion

This experiment provides a practical performance analysis of virtual machines and containers using both system-level and application-level workloads.

The study combines benchmark measurements with a FastAPI application to evaluate response time, startup behavior, and scalability.

The raw results, processed analysis, benchmark scripts, and performance visualizations provide a reproducible record of the experiment.

## Tools Used

- VMware Workstation
- Ubuntu 24.04
- Docker
- Sysbench
- fio
- iperf3
- Python
- FastAPI
- Uvicorn
- Matplotlib
- Git
- GitHub

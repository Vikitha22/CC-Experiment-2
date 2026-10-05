<div align="center">

# Performance Analysis of Virtual Machines and Containers

**An experimental comparison of a VMware Ubuntu virtual machine and a Docker container using system-level and application-level workloads**

![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-E95420?logo=ubuntu&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Uvicorn-009688?logo=fastapi&logoColor=white)
![VMware](https://img.shields.io/badge/VMware-Workstation-607078?logo=vmware&logoColor=white)

</div>

---

## Table of Contents

1. [Abstract](#abstract)
2. [Key Results](#key-results)
3. [Objectives](#objectives)
4. [Experimental Environment](#experimental-environment)
5. [Methodology](#methodology)
6. [FastAPI Application](#fastapi-application)
7. [Results and Analysis](#results-and-analysis)
8. [Discussion](#discussion)
9. [Limitations](#limitations)
10. [Automation](#automation)
11. [Project Structure](#project-structure)
12. [Conclusion](#conclusion)
13. [Tools Used](#tools-used)

---

## Abstract

This project evaluates the performance of workloads running in a **Virtual Machine (VM)** and in a **Docker container**. The study covers CPU, memory, disk I/O, network throughput, application response time, container startup time and application scalability.

The experiment was conducted on **Ubuntu 24.04 running inside VMware Workstation**, with Docker installed for container-based benchmarking. For the tested FastAPI `/compute` workload, the container responded in **0.091 s** compared with **0.095 s** in the VM. Container startup averaged **0.647 s**, and total execution time grew from **0.787 s** (10 concurrent requests) to **3.867 s** (50 concurrent requests). All measurements were stored as raw results and analyzed with Python.

## Key Results

| Metric | Result |
|---|---:|
| VM API response time (`/compute`) | **0.095 s** |
| Container API response time (`/compute`) | **0.091 s** |
| API measured difference | **-4.21 %** |
| Average container startup time | **0.647 s** |
| 10 concurrent requests | **0.787 s** |
| 20 concurrent requests | **1.513 s** |
| 50 concurrent requests | **3.867 s** |
| Network throughput (local path) | **53.1 Gbits/sec** |

## Objectives

- Measure CPU performance
- Measure memory performance
- Measure disk I/O performance
- Measure network throughput
- Compare FastAPI application performance in the VM and in a container
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

## Methodology

The experiment was divided into **system-level** and **application-level** performance testing.

| Level | Areas Tested |
|---|---|
| System-level | CPU, memory, disk I/O, network throughput |
| Application-level | FastAPI response time, container startup time, application scalability |

### System-Level Benchmarks

| Test | Tool | Configuration | Metrics Recorded |
|---|---|---|---|
| CPU | Sysbench | 4 threads, 10 seconds | Events per second, execution time, total events, latency |
| Memory | Sysbench | 4 threads, 10 seconds | Memory transferred, throughput, total operations |
| Disk I/O | fio | 1 GB test file, 1 MB block size, direct I/O, 10-second read/write | Read bandwidth, write bandwidth, IOPS, latency |
| Network | iperf3 | Local host/container networking path | Throughput |

### Network Throughput

The measured throughput for the tested local container networking path was approximately **53.1 Gbits/sec**.

> **Note:** This represents the tested local host/container networking path and **not** external Internet bandwidth.

## FastAPI Application

A FastAPI application was developed for application-level performance testing.

| Endpoint | Description |
|---|---|
| `/` | Returns a simple JSON response |
| `/compute` | CPU-intensive calculation: the sum of squares for one million integers |

The `/compute` endpoint was tested in both the VM and the Docker container environments.

## Results and Analysis

### 1. FastAPI Response Time

| Environment | Real Time |
|---|---:|
| VM | 0.095 s |
| Container | 0.091 s |

The measured difference for this test was **-4.21 %**, meaning the container's response time was 4.21 % lower than the VM's:

```
difference = (VM_time - Container_time) / VM_time x 100
           = (0.095 - 0.091) / 0.095 x 100
           = 4.21 %
```

<p align="center">
  <img src="https://raw.githubusercontent.com/Vikitha22/CC-Experiment-2/main/performance_analysis.png" alt="Performance Analysis - FastAPI Response Time" width="700">
  <br>
  <em>Figure 1. FastAPI <code>/compute</code> response time: VM vs container.</em>
</p>

### 2. Container Startup Time

Container startup time was measured across three independent runs.

| Run | Real Time |
|---|---:|
| 1 | 0.699 s |
| 2 | 0.622 s |
| 3 | 0.621 s |

| Statistic | Time |
|---|---:|
| Average | 0.647 s |
| Minimum | 0.621 s |
| Maximum | 0.699 s |

<p align="center">
  <img src="https://raw.githubusercontent.com/Vikitha22/CC-Experiment-2/main/results/figures/startup_time.png" alt="Container Startup Time" width="700">
  <br>
  <em>Figure 2. Container startup time across three runs.</em>
</p>

### 3. Scalability

The FastAPI application was tested with an increasing number of concurrent requests.

| Concurrent Requests | Real Time | Time per Request |
|---:|---:|---:|
| 10 | 0.787 s | 0.079 s |
| 20 | 1.513 s | 0.076 s |
| 50 | 3.867 s | 0.077 s |

<p align="center">
  <img src="https://raw.githubusercontent.com/Vikitha22/CC-Experiment-2/main/results/figures/scalability.png" alt="Application Scalability" width="700">
  <br>
  <em>Figure 3. Total execution time vs number of concurrent requests.</em>
</p>

### Results Summary

| Metric | Result |
|---|---:|
| VM API response time | 0.095 s |
| Container API response time | 0.091 s |
| API measured difference | -4.21 % |
| Average startup time | 0.647 s |
| Minimum startup time | 0.621 s |
| Maximum startup time | 0.699 s |
| 10 concurrent requests | 0.787 s |
| 20 concurrent requests | 1.513 s |
| 50 concurrent requests | 3.867 s |
| Network throughput | 53.1 Gbits/sec |

## Discussion

- **Response time:** The container completed the CPU-bound `/compute` request slightly faster than the VM (0.091 s vs 0.095 s). The gap is only about 4 ms, so it indicates comparable performance rather than a decisive advantage for either environment.
- **Startup time:** The container started in under one second on every run (average 0.647 s). Runs 2 and 3 were almost identical, and the first run was slightly slower.
- **Scalability:** Time per request stayed near 0.077 to 0.079 s from 10 to 50 requests, so total execution time grew approximately linearly with the number of requests for this CPU-bound workload.
- **Network:** The 53.1 Gbits/sec result reflects a local networking path and is not comparable to a physical network link.

## Limitations

- The API comparison is based on one measured value per environment, so the small difference may fall within normal run-to-run variation.
- Startup time was measured over only three runs.
- Scalability was evaluated at three load levels (10, 20 and 50 requests).
- The container was run on a single virtualized host (Ubuntu inside VMware), not on bare metal.
- Results are specific to this hardware and configuration.

## Automation

Benchmark execution was partially automated.

| Script | Purpose |
|---|---|
| `scripts/run_benchmarks.sh` | Runs the CPU and memory benchmarks and stores the extracted results |
| `scripts/analyze_results.py` | Generates summary statistics and performance graphs |

## Project Structure

```
CC-Experiment-2/
├── app/                    # FastAPI application
├── docker/                 # Docker configuration
├── docs/                   # System and environment documentation
├── scripts/
│   ├── run_benchmarks.sh   # Benchmark automation
│   └── analyze_results.py  # Analysis and graph generation
├── results/
│   └── figures/            # startup_time.png, scalability.png, ...
├── performance_analysis.png
├── .gitignore
└── README.md
```

## Conclusion

This experiment provides a practical performance analysis of virtual machines and containers using both system-level and application-level workloads.

The study combines benchmark measurements with a FastAPI application to evaluate response time, startup behavior and scalability. The container showed a slightly lower response time than the VM for the tested workload, started in about 0.65 s, and scaled roughly linearly with concurrent requests.

The raw results, processed analysis, benchmark scripts and performance visualizations provide a reproducible record of the experiment.

## Tools Used

| Category | Tools |
|---|---|
| Virtualization and containers | VMware Workstation, Ubuntu 24.04, Docker |
| Benchmarking | Sysbench, fio, iperf3 |
| Application | Python, FastAPI, Uvicorn |
| Analysis and visualization | Python, Matplotlib |
| Version control | Git, GitHub |

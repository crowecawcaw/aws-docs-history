

# AWS Glue worker types
<a name="worker-types"></a>

## Overview
<a name="worker-types-overview"></a>

AWS Glue provides multiple worker types to accommodate different workload requirements, from small streaming jobs to large-scale, memory-intensive data processing tasks. This section provides comprehensive information about all available worker types, their specifications, and usage recommendations.

### Worker type categories
<a name="worker-type-categories"></a>

AWS Glue offers two main categories of worker types:
+ **G Worker Types**: General-purpose compute workers optimized for standard ETL workloads
+ **R Worker Types**: Memory-optimized workers designed for memory-intensive Spark applications

### Data Processing Units (DPUs)
<a name="data-processing-units"></a>

The resources available on AWS Glue workers are measured in DPUs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.

**Memory-Optimized DPUs (M-DPUs)**: R type workers use M-DPUs, which provide double the memory allocation for a given size compared to standard DPUs. This means that while a standard DPU provides 16 GB of memory, an M-DPU in R type workers provides 32GB of memory optimized for memory-intensive Spark applications.

## Available worker types
<a name="available-worker-types"></a>

### G.1X
<a name="g1x-standard-worker"></a>
+ **DPU**: 1 DPU (4 vCPUs, 16 GB memory)
+ **Storage**: 94GB disk (approximately 44GB free)
+ **Use Case**: Data transforms, joins, and queries - scalable and cost-effective for most jobs

### G.2X
<a name="g2x-standard-worker"></a>
+ **DPU**: 2 DPU (8 vCPUs, 32 GB memory)
+ **Storage**: 138GB disk (approximately 78GB free)
+ **Use Case**: Data transforms, joins, and queries - scalable and cost-effective for most jobs

### G.4X
<a name="g4x-large-worker"></a>
+ **DPU**: 4 DPU (16 vCPUs, 64 GB memory)
+ **Storage**: 256GB disk (approximately 230GB free)
+ **Use Case**: Demanding transforms, aggregations, joins, and queries

### G.8X
<a name="g8x-extra-large-worker"></a>
+ **DPU**: 8 DPU (32 vCPUs, 128 GB memory)
+ **Storage**: 512GB disk (approximately 485GB free)
+ **Use Case**: Demanding transforms, aggregations, joins, and queries

### G.12X
<a name="g12x-very-large-worker"></a>
+ **DPU**: 12 DPU (48 vCPUs, 192 GB memory)
+ **Storage**: 768GB disk (approximately 741GB free)
+ **Use Case**: Very large and resource-intensive workloads requiring significant compute capacity

### G.16X
<a name="g16x-maximum-worker"></a>
+ **DPU**: 16 DPU (64 vCPUs, 256 GB memory)
+ **Storage**: 1024GB disk (approximately 996GB free)
+ **Use Case**: Largest and most resource-intensive workloads requiring maximum compute capacity

### R.1X - Memory-Optimized\*
<a name="r1x-memory-optimized-small"></a>
+ **DPU**: 1 M-DPU (4 vCPUs, 32 GB memory)
+ **Use Case**: Memory-intensive workloads with frequent out-of-memory errors or high memory-to-CPU ratio requirements

### R.2X - Memory-Optimized\*
<a name="r2x-memory-optimized-medium"></a>
+ **DPU**: 2 M-DPU (8 vCPUs, 64 GB memory)
+ **Use Case**: Memory-intensive workloads with frequent out-of-memory errors or high memory-to-CPU ratio requirements

### R.4X - Memory-Optimized\*
<a name="r4x-memory-optimized-large"></a>
+ **DPU**: 4 M-DPU (16 vCPUs, 128 GB memory)
+ **Use Case**: Large memory-intensive workloads with frequent out-of-memory errors or high memory-to-CPU ratio requirements

### R.8X - Memory-Optimized\*
<a name="r8x-memory-optimized-extra-large"></a>
+ **DPU**: 8 M-DPU (32 vCPUs, 256 GB memory)
+ **Use Case**: Very large memory-intensive workloads with frequent out-of-memory errors or high memory-to-CPU ratio requirements

**\*** You may encounter higher startup latency with these workers. To resolve the issue, try the following:
+ Wait a few minutes and then submit your job again.
+ Submit a new job with a reduced number of workers.
+ Submit a new job using a different worker type or size.

## Worker type specifications table
<a name="worker-type-specifications"></a>


**Worker Type Specifications**  

| Worker Type | DPU per Node | vCPU | Memory (GB) | Disk (GB) | Approximate Free Disk Space (GB) | Spark Executors per Node | 
| --- | --- | --- | --- | --- | --- | --- | 
| G.1X | 1 | 4 | 16 | 94 | 44 | 1 | 
| G.2X | 2 | 8 | 32 | 138 | 78 | 1 | 
| G.4X | 4 | 16 | 64 | 256 | 230 | 1 | 
| G.8X | 8 | 32 | 128 | 512 | 485 | 1 | 
| G.12X | 12 | 48 | 192 | 768 | 741 | 1 | 
| G.16X | 16 | 64 | 256 | 1024 | 996 | 1 | 
| R.1X | 1 | 4 | 32 | 94 | 44 | 1 | 
| R.2X | 2 | 8 | 64 | 138 | 78 | 1 | 
| R.4X | 4 | 16 | 128 | 256 | 230 | 1 | 
| R.8X | 8 | 32 | 256 | 512 | 485 | 1 | 

*Note*: R worker types have memory-optimized configurations with specifications optimized for memory-intensive workloads.

## Important considerations
<a name="important-considerations"></a>

### Startup latency
<a name="startup-latency"></a>

**Important**  
G.12X and G.16X worker types, as well as all R worker types (R.1X through R.8X), may encounter higher startup latency. To resolve the issue, try the following:  
Wait a few minutes and then submit your job again.
Submit a new job with a reduced number of workers.
Submit a new job using a different worker type and size.

## Choosing the right worker type
<a name="choosing-right-worker-type"></a>

### For standard ETL workloads
<a name="standard-etl-workloads"></a>
+ **G.1X or G.2X**: Most cost-effective for typical data transforms, joins, and queries
+ **G.4X or G.8X**: For more demanding workloads with larger datasets

### For large-scale workloads
<a name="large-scale-workloads"></a>
+ **G.12X**: Very large datasets requiring significant compute resources
+ **G.16X**: Maximum compute capacity for the most demanding workloads

### For memory-intensive workloads
<a name="memory-intensive-workloads"></a>
+ **R.1X or R.2X**: Small to medium memory-intensive jobs
+ **R.4X or R.8X**: Large memory-intensive workloads with frequent OOM errors

## Cost Optimization Considerations
<a name="cost-optimization-considerations"></a>
+ **Standard G workers**: Provide a balance of compute, memory and networking resources, and can be used for a variety of diverse workloads at lower cost
+ **R workers**: Specialized for memory-intensive tasks with fast performance for workloads that process large data sets in memory

## Best practices
<a name="best-practices"></a>

### Worker selection guidelines
<a name="worker-selection-guidelines"></a>

1. **Start with standard workers** (G.1X, G.2X) for most workloads

1. **Use R workers** when experiencing frequent out-of-memory errors or workloads with memory-intensive operations like caching, shuffling, and aggregating

1. **Consider G.12X/G.16X** for compute-intensive workloads requiring maximum resources

1. **Account for capacity constraints** when using new worker types in time-sensitive workflows

### Performance optimization
<a name="performance-optimization"></a>
+ Monitor CloudWatch metrics to understand resource utilization
+ Use appropriate worker counts based on data size and complexity
+ Consider data partitioning strategies to optimize worker efficiency
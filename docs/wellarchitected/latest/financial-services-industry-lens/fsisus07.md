# FSISUS07: How do you optimize batch processing components for sustainability?

Because batch processing is often found within many workloads across financial systems, verify that the minimum number of resources are consumed by batching transactions together while meeting your customer SLA and system requirements.

## FSISUS07-BP01 Optimize your batch processing systems

Because batch processing is often found within many workloads across financial
systems, verify that the minimum number of resources are consumed by batching
transactions together while meeting your customer SLA and system requirements.

**Prescriptive guidance**

- Queue up several requests together that don't require immediate processing.
- Increase serialization to flatten utilization across your pipeline.
- Modify the capacity of individual components to prevent idling resources
  waiting for input.
- Create buffers and establish rate limiting to smooth the consumption of
  external services.
- Use the most efficient available hardware and services to optimize your
  software.
- If possible, schedule jobs during times of day where carbon intensity for power
  is lowest.

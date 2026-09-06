

# Resilient training
<a name="sagemaker-hyperpod-ray-resilient-training"></a>

HyperPod resiliency runs beneath your Ray workloads. Health checks detect faulty nodes and recover them, host-level detection catches silent stalls, and tiered checkpointing shortens recovery after a failure. These capabilities apply to Ray without changes to your Ray code.

**Topics**
+ [Automatic node recovery with Ray](sagemaker-hyperpod-ray-node-recovery.md)
+ [Tiered checkpointing](sagemaker-hyperpod-ray-tiered-storage.md)
+ [Hung job detection](sagemaker-hyperpod-ray-hung-job-detection.md)
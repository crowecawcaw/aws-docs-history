# Allocating compute quota

in Amazon SageMaker HyperPod task governance

Cluster administrators can decide how the organization uses purchased compute. Doing so reduces waste and idle resources. You can allocate
compute quota such that teams can borrow unused resources from each other.
Compute quota allocation in HyperPod task governance lets administrators allocate resources at the
instance level and at a more granular resource level. This capability provides flexible and efficient resource management for teams by allowing granular
control over individual compute resources instead of requiring entire instance allocations. Allocating at a granular level eliminates inefficiencies of traditional instance-level
allocation. Through this approach, you can optimize resource utilization and reduce idle compute.

Compute quota allocation supports three types of resource allocation: accelerators, vCPU, and memory. Accelerators are components in accelerated computer
instances that that perform functions, such as floating point number calculations, graphics processing, or data pattern matching. Accelerators include GPUs,
Trainium accelerators, and neuron cores. For multi-team GPU sharing, different teams can receive specific GPU allocations from the same instance type, maximizing
utilization of accelerator hardware. For memory-intensive workloads that require additional RAM for data preprocessing or model caching scenarios, you can allocate memory
quota beyond the default GPU-to-memory ratio. For CPU-heavy preprocessing tasks that need substantial CPU resources alongside GPU training, you can allocate independent
CPU resource allocation.

Once you provide a value, HyperPod task governance calculates the ratio using the formula **allocated resource divided by the total amount of resources
available in the instance**. HyperPod task governance then uses this ratio to apply default allocations to other resources, but you can override
these defaults and customize them based on your use case. The following are sample scenarios of how
HyperPod task governance allocates resources based on your values:

- **Only accelerator specified** - HyperPod task governance applies the default ratio to vCPU and memory based on the accelerator values.
- **Only vCPU specified** - HyperPod task governance calculates the ratio and applies it to memory. Accelerators are set to 0.
- **Only memory specified** - HyperPod task governance calculates the ratio and applies it to vCPU because compute is required to run memory-specified workloads. Accelerators are set to 0.
  To programmatically control quota allocation, you can use the
  [ComputeQuotaResourceConfig](../APIReference/API_ComputeQuotaResourceConfig.md "../APIReference/API_ComputeQuotaResourceConfig.md") object and specify your allocations in integers.

```
{
    "ComputeQuotaConfig": {
        "ComputeQuotaResources": [{
            "InstanceType": "ml.g5.24xlarge",
            "Accelerators": "16",
            "vCpu": "200.0",
            "MemoryInGiB": "2.0"
        }]
    }
}
```

To see all of the allocated allocations, including the defaults, use the [DescribeComputeQuota](../APIReference/API_DescribeComputeQuota.md "../APIReference/API_DescribeComputeQuota.md") operation. To update your allocations, use the [UpdateComputeQuota](../APIReference/API_UpdateComputeQuota.md "../APIReference/API_UpdateComputeQuota.md") operation.

You can also use the HyperPod CLI to allocate compute quotas. For more information about the HyperPod CLI, see [Running jobs on SageMaker HyperPod clusters
orchestrated by Amazon EKS](sagemaker-hyperpod-eks-run-jobs.md "sagemaker-hyperpod-eks-run-jobs.md"). The following example demonstrates how to set compute quotas using the HyperPod CLI.

```
hyp create hyp-pytorch-job --version 1.1 --job-name sample-job \
--image 123456789012.dkr.ecr.us-west-2.amazonaws.com/ptjob:latest \
--pull-policy "Always" \
--tasks-per-node 1 \
--max-retry 1 \
--priority high-priority \
--namespace hyperpod-ns-`team-name` \
--queue-name hyperpod-ns-`team-name`-localqueue \
--instance-type `sample-instance-type` \
--accelerators 1 \
--vcpu 3 \
--memory 1 \
--accelerators-limit 1 \
--vcpu-limit 4 \
--memory-limit 2
```

To allocate quotas using the AWS console, follow these steps.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Under HyperPod clusters, choose **Cluster management**.
3. Under **Compute allocations**, choose **Create**.
4. If you don’t already have instances, choose **Add allocation** to add an instance.
5. Under **Allocations**, choose to allocate by instances
   or individual resources. If you allocate by individual resources, SageMaker AI automatically
   assigns allocations to other resources by the ratio that you chose.
   To override this ratio-based allocation, use the corresponding toggle to override that compute.
6. Repeat steps 4 and 5 to configure additional instances.
   After allocating compute quota, you can then
   submit jobs through the HyperPod CLI or `kubectl`. HyperPod
   efficiently schedules workloads based on available quota.

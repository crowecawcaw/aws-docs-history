#

Allocating GPU partition quota

You can extend compute quota allocation to support GPU partitioning, enabling fine-grained resource sharing at the GPU partition level. When GPU partitioning is enabled on supported GPUs in the cluster, each physical GPU can be partitioned into multiple isolated GPUs with defined compute, memory, and streaming multiprocessor allocations. For more information about GPU partitioning, see [Using GPU partitions in Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-gpu-partitioning.md "sagemaker-hyperpod-eks-gpu-partitioning.md"). You can allocate specific GPU partitions to teams, allowing multiple teams to share a single GPU while maintaining hardware-level isolation and predictable performance.

For example, an ml.p5.48xlarge instance with 8 H100 GPUs can be partitioned into GPU partitions, and you can allocate individual partitions to different teams based on their task requirements. When you specify GPU partition allocations, HyperPod task governance calculates proportional vCPU and memory quotas based on the GPU partition, similar to GPU-level allocation. This approach maximizes GPU utilization by eliminating idle capacity and enabling cost-effective resource sharing across multiple concurrent tasks on the same physical GPU.

## Creating Compute Quotas

```
aws sagemaker create-compute-quota \
  --name "fractional-gpu-quota" \
  --compute-quota-config '{
    "ComputeQuotaResources": [
      {
        "InstanceType": "ml.p4d.24xlarge",
        "AcceleratorPartition": {
            "Count": 4,
            "Type": "mig-1g.5gb"
        }
      }
    ],
    "ResourceSharingConfig": {
      "Strategy": "LendAndBorrow",
      "BorrowLimit": 100
    }
  }'
```

## Verifying Quota Resources

```
# Check ClusterQueue
kubectl get clusterqueues
kubectl describe clusterqueue `QUEUE_NAME`

# Check ResourceFlavors
kubectl get resourceflavor
kubectl describe resourceflavor `FLAVOR_NAME`
```

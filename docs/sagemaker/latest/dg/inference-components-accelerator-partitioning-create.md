

# Create an endpoint with GPU partitions
<a name="inference-components-accelerator-partitioning-create"></a>

To create a partitioned endpoint, you declare a partition layout on the production variant of an endpoint configuration, and then create an endpoint from that configuration. SageMaker AI partitions the accelerators while it launches the instances for the endpoint.

## Layout rules
<a name="accelerator-partitioning-layout-rules"></a>

You set the partition layout with the `AcceleratorPartitionLayouts` field on a production variant. The following rules apply to `AcceleratorPartitionLayouts`:
+ `AcceleratorPartitionLayouts` must contain exactly 1 entry. That entry describes how to divide one accelerator, and SageMaker AI applies it to every accelerator on every instance in the variant.
+ The requested partition types must fit on one accelerator. Otherwise, SageMaker AI returns a 400 error that states what the accelerator provides and what you requested. Each partition type is an NVIDIA MIG profile, and NVIDIA sets the number of compute and memory slices that it uses. For more information, see the [NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/) on the NVIDIA website.
+ To request multiple partitions of the same type, repeat the type. For example, `["mig-1g.5gb", "mig-1g.5gb", "mig-1g.5gb"]` requests three partitions per accelerator.
+ SageMaker AI doesn't support the following NVIDIA profile references:
  + `+me`: Includes at least one media engine (NVDEC, NVENC, NVJPG, or OFA).
  + `+gfx`: Adds support for graphics APIs (new in GB20X).
  + `+me.all`: Allocates all available media engines to this instance, without graphics support.
  + `-me`: Excludes all media engines, for pure compute workloads.

For the partition types that each instance family provides, see [GPU partition types](inference-components-accelerator-partitioning.md#accelerator-partitioning-types).

**Note**  
For more information about partition layouts, see [Supported MIG Profiles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html) in the NVIDIA Multi-Instance GPU User Guide on the NVIDIA website.

## Create the endpoint config
<a name="accelerator-partitioning-create-config"></a>

The following procedure creates a partitioned endpoint on an `ml.p4d.24xlarge` instance in US West (Oregon). An `ml.p4d.24xlarge` instance has 8 NVIDIA A100 accelerators, and each A100 has 7 compute slices. The endpoint divides each A100 into three partitions, one of each of the types `mig-4g.20gb`, `mig-2g.10gb`, and `mig-1g.5gb`. This layout uses all 7 compute slices. The endpoint provides 24 partitions in total, 8 of each type.

**Important**  
The `ml.p4d.24xlarge` instance incurs charges while the endpoint runs, whether or not inference components run on its partitions. To delete it, see [Delete a partitioned endpoint](inference-components-accelerator-partitioning-manage.md#accelerator-partitioning-delete). For pricing, see [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/ai/pricing/).

**To create the endpoint config (AWS CLI)**
+ Create an endpoint configuration that sets `AcceleratorPartitionLayouts` on the production variant. The following `create-endpoint-config` command creates the endpoint configuration `partition-demo-config`. Replace `{{111122223333}}` with your AWS account ID and `{{my-execution-role}}` with the name of an execution role that can pull the container image from Amazon ECR and write to Amazon CloudWatch Logs.

  ```
  aws sagemaker create-endpoint-config \
    --region us-west-2 \
    --endpoint-config-name partition-demo-config \
    --execution-role-arn arn:aws:iam::{{111122223333}}:role/{{my-execution-role}} \
    --production-variants '[
      {
        "VariantName": "AllTraffic",
        "InstanceType": "ml.p4d.24xlarge",
        "InitialInstanceCount": 1,
        "AcceleratorPartitionLayouts": [
          {
            "AcceleratorPartitionTypes": ["mig-4g.20gb", "mig-2g.10gb", "mig-1g.5gb"]
          }
        ]
      }
    ]'
  ```

  To confirm that SageMaker AI stored the layout, run the following `describe-endpoint-config` command:

  ```
  aws sagemaker describe-endpoint-config \
    --region us-west-2 \
    --endpoint-config-name partition-demo-config \
    --query 'ProductionVariants[0].AcceleratorPartitionLayouts'
  ```

  The output lists the partition types that you sent, in order. If the output is `null`, the endpoint won't be partitioned. For more information, see [Troubleshooting](inference-components-accelerator-partitioning-troubleshoot.md).

## Create the endpoint
<a name="accelerator-partitioning-create-endpoint"></a>

After you create the endpoint config, create the endpoint from it.

**To create a partitioned endpoint (AWS CLI)**

1. Create the endpoint, and wait for it to be in service. SageMaker AI partitions the accelerators while it launches the instances for the endpoint. Creating the endpoint can take some time. The following `create-endpoint` command creates the endpoint `partition-demo`, and the `wait endpoint-in-service` command waits until it's ready:

   ```
   aws sagemaker create-endpoint --region us-west-2 --endpoint-name partition-demo --endpoint-config-name partition-demo-config
   aws sagemaker wait endpoint-in-service --region us-west-2 --endpoint-name partition-demo
   ```

   If the waiter exits with an error, check the status in the next step instead of recreating the endpoint.

1. Describe the endpoint. The following `describe-endpoint` command returns the endpoint status, any failure reason, and the layout:

   ```
   aws sagemaker describe-endpoint \
     --region us-west-2 \
     --endpoint-name partition-demo \
     --query '[EndpointStatus,FailureReason,ProductionVariants[0].AcceleratorPartitionLayouts]'
   ```

   The layout appears in the output only after the status is `InService`. While the status is `Creating` or `Failed`, the layout is `null`, which is expected and doesn't mean that the endpoint isn't partitioned. If the status is `Failed`, the failure reason explains why.

   When the status is `InService`, the output echoes the layout that you sent, in order. Every accelerator is partitioned and the partitions are empty. An `InService` endpoint with no inference components is valid.

To place models on the partitions, see [Deploy models to GPU partitions with inference components](inference-components-accelerator-partitioning-deploy.md).
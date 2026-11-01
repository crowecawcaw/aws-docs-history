

# Deploy models to GPU partitions with inference components
<a name="inference-components-accelerator-partitioning-deploy"></a>

After your partitioned endpoint is `InService`, you deploy a model to it by creating an inference component that requests a partition type. Each copy of the inference component occupies one partition of that type. To create the endpoint, see [Create an endpoint with GPU partitions](inference-components-accelerator-partitioning-create.md).

## Inference component rules
<a name="accelerator-partitioning-ic-rules"></a>

The following rules apply to inference components on an endpoint with a partition layout:
+ `AcceleratorPartitionType` is required. If you omit it, SageMaker AI returns a 400 error.
+ The requested type must be one that the endpoint layout declares. Otherwise, SageMaker AI returns a 400 error that names the declared types.
+ `NumberOfAcceleratorDevicesRequired` must be 1. It refers to one partition.
+ `MinMemoryRequiredInMb` and `NumberOfCpuCoresRequired` describe host memory and CPU. The partition type sets the GPU memory.
+ Each copy uses one partition. Increase `CopyCount` to place more copies on free partitions of the same type.

## Create inference components
<a name="accelerator-partitioning-create-ic"></a>

The following procedure deploys a model to the endpoint `partition-demo` on a `mig-4g.20gb` partition. The inference component defines its model inline with a Hugging Face inference container that downloads the `gpt2` model from Hugging Face at startup, so you don't need to run `create-model`.

**To create inference components on partitions (AWS CLI)**

1. Create an inference component. Set `AcceleratorPartitionType` to select the partition type that the model runs on. The following `create-inference-component` command creates the inference component `demo-ic-4g` on a `mig-4g.20gb` partition:

   ```
   aws sagemaker create-inference-component \
     --region us-west-2 \
     --inference-component-name demo-ic-4g \
     --endpoint-name partition-demo \
     --variant-name AllTraffic \
     --specification '{
       "Container": {
         "Image": "763104351884.dkr.ecr.us-west-2.amazonaws.com/huggingface-pytorch-inference:1.10.2-transformers4.17.0-gpu-py38-cu113-ubuntu20.04",
         "Environment": {
           "HF_MODEL_ID": "gpt2",
           "HF_TASK": "text-generation"
         }
       },
       "ComputeResourceRequirements": {
         "AcceleratorPartitionType": "mig-4g.20gb",
         "NumberOfAcceleratorDevicesRequired": 1,
         "NumberOfCpuCoresRequired": 1,
         "MinMemoryRequiredInMb": 2048
       }
     }' \
     --runtime-config '{"CopyCount": 1}'
   ```

   To place a model on each partition type in the layout, repeat the command for each type with a different inference component name and `AcceleratorPartitionType`.

   The following list describes the fields in this example:
   + `AcceleratorPartitionType` must be one of the types in the endpoint layout.
   + `NumberOfAcceleratorDevicesRequired` must be 1. It refers to one partition.
   + `NumberOfCpuCoresRequired` and `MinMemoryRequiredInMb` describe host CPU and memory. The partition type sets the GPU memory.

1. Describe the inference component. It takes a few minutes to create. The following `describe-inference-component` command returns the name, status, and any failure reason of the inference component:

   ```
   aws sagemaker describe-inference-component --region us-west-2 --inference-component-name demo-ic-4g \
     --query '[InferenceComponentName,InferenceComponentStatus,FailureReason]' --output text
   ```

   An inference component is ready when its status is `InService`. If the status is `Failed`, the third column shows the failure reason. When the inference component is `InService`, the model runs on its own partition.

Partitioning doesn't affect invocation. Invoke the model as you would any inference component, by calling [InvokeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html) with the inference component name. For more information, see [Invoke models for real-time inference](realtime-endpoints-test-endpoints.md).
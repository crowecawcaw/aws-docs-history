

# Troubleshooting
<a name="inference-components-accelerator-partitioning-troubleshoot"></a>

Use the following information to resolve common problems with partitioned endpoints.

`DescribeEndpointConfig` returns `null` for the layout  
The `AcceleratorPartitionLayouts` field didn't reach the service, and an endpoint from this configuration won't be partitioned. Confirm that you call a supported AWS Region and that your AWS CLI or SDK version includes `AcceleratorPartitionLayouts`.

The endpoint configuration is rejected because the layout doesn't fit  
The partition types in the layout need more compute slices or memory slices than one accelerator provides. The error states what the accelerator provides and what you requested. Remove a partition or choose smaller types. For the types that each instance family provides, see [GPU partition types](inference-components-accelerator-partitioning.md#accelerator-partitioning-types). For more information about the partitions that each GPU supports, see [Supported MIG Profiles](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html) in the NVIDIA Multi-Instance GPU User Guide on the NVIDIA website.

A request is rejected with a 400 error that lists valid partition types  
The partition type isn't valid for the instance's GPU. Partition types don't carry from one instance family to another. Use one of the types that the error lists.

The endpoint configuration is rejected because of the number of layouts  
`AcceleratorPartitionLayouts` must contain exactly 1 entry. GPU partitioning also can't be combined with `ServerlessConfig` or instance pools on the same production variant.

The endpoint fails to partition the accelerators, and no error names a partition type  
Some partition types require a newer NVIDIA driver than the default image provides. On P4d instances, `mig-1g.10gb` requires a newer driver. Set `InferenceAmiVersion` to `al2023-ami-sagemaker-inference-gpu-4-1` on the production variant. For the driver version that each AMI version provides, see [Current versions and supported instance families](inference-gpu-drivers.md#inference-gpu-drivers-versions).

An inference component is rejected with a 400 error that names the declared partition types  
The partition type that you requested isn't in the endpoint layout. There is no fallback to a whole accelerator. Request one of the declared types, or create a new endpoint with a layout that includes the type that you need.

An inference component is rejected because of `AcceleratorPartitionType` or `NumberOfAcceleratorDevicesRequired`  
On an endpoint with a partition layout, every new inference component must set `AcceleratorPartitionType`, and `NumberOfAcceleratorDevicesRequired` must be 1. For the full list, see [Inference component rules](inference-components-accelerator-partitioning-deploy.md#accelerator-partitioning-ic-rules).

An inference component stays in `Failed` status  
Check the `FailureReason` field from `DescribeInferenceComponent`. A common cause is a model that needs more GPU memory than the partition type provides. Choose a larger partition type, which requires a new inference component and, if the type isn't in the layout, a new endpoint.
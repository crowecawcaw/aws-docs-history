

# Troubleshooting and best practices
<a name="training-sessions-troubleshooting"></a>

## Common errors and solutions
<a name="training-sessions-troubleshooting-errors"></a>

`ConcurrentAccessError`  
A session supports one `TrainingClient` at a time. You opened a second client on a session that already has one. Stop the first client, or scope each client to a `with` block.

`OperationError` on `forward_backward`  
A required `loss_fn_inputs` key is missing, or a tensor length does not match the model input. Provide full-sequence values with prompt positions zero-padded, and include every key your loss function requires. See [Training data](training-sessions-sdk.md#training-sessions-sdk-training-data).

`ValueError` from a restore factory  
You passed both `base_model` and `model_package_arn` and they name different base models, or you called `get_latest_model_package` without a `model_package_group_arn`. Pass matching values, or set the group on the client.

Rewards stop improving during RL  
You are sampling from stale weights. A `SamplingClient` is bound to the weights that existed when it was created. Rebind after every `optim_step` with `save_weights_and_get_sampling_client()`. See [On-policy sampling](training-sessions-sdk.md#training-sessions-sdk-on-policy).

Checkpoint operations fail with a Amazon VPC configuration  
S3 hostnames are not resolving to private IPs. Enable Private DNS on your S3 interface endpoint and enable DNS support and DNS hostnames on the Amazon VPC. See [Configure a VPC for SageMaker AI training sessions](training-sessions-vpc.md).

## Session inspection and diagnostics
<a name="training-sessions-troubleshooting-inspection"></a>
+ Use `svc.list_sessions(status_equals=...)` to find active or failed sessions, and `DescribeTrainingSession` for the status and failure reason of a specific session.
+ `future.result()` raises `OperationError` with the failure detail for an individual operation. Collect results as you pipeline so a failure surfaces at the step that caused it.

## Best practices
<a name="training-sessions-troubleshooting-best-practices"></a>
+ **Checkpoint periodically.** A session is compute and cannot be reattached by name. Call `save_state` on a fixed interval so you can resume from the latest checkpoint after a fault.
+ **Stop idle sessions.** An idle session holds the resources. Call `stop()` when you finish, or scope the client to a `with` block.
+ **Pipeline operations.** Submit successive training operations before collecting the earlier result, and keep many sampling calls in flight, to raise throughput.
+ **Use one model package group per experiment.** An unnamed group is shared across your account, which makes `get_latest_model_package` ambiguous. A dedicated group keeps resume exact.
+ **Clean up model packages.** Each saved package consumes Amazon S3 storage until you remove it. Use `delete_model_package(arn, delete_artifacts=True)` to remove both the package and its stored weights.
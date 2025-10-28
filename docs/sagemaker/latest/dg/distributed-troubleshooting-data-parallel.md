# Troubleshooting for distributed

training in Amazon SageMaker AI

If you have problems in running a training job when you use the library, use the following
list to try to troubleshoot. If you need further support, reach out to the SageMaker AI team through
[AWS Support Center](https://console.aws.amazon.com/support/ "https://console.aws.amazon.com/support/") or [AWS Developer Forums for
Amazon Amazon SageMaker AI](https://forums.aws.amazon.com/forum.jspa?forumID=285 "https://forums.aws.amazon.com/forum.jspa?forumID=285").

###### Topics

- [Using SageMaker AI distributed data
  parallel with Amazon SageMaker Debugger and checkpoints](#distributed-ts-data-parallel-debugger "#distributed-ts-data-parallel-debugger")
- [An unexpected prefix
  attached to model parameter keys](#distributed-ts-data-parallel-pytorch-prefix "#distributed-ts-data-parallel-pytorch-prefix")
- [SageMaker AI distributed training job
  stalling during initialization](#distributed-ts-data-parallel-efa-sg "#distributed-ts-data-parallel-efa-sg")
- [SageMaker AI distributed
  training job stalling at the end of training](#distributed-ts-data-parallel-stall-at-the-end "#distributed-ts-data-parallel-stall-at-the-end")
- [Observing scaling
  efficiency degradation due to Amazon FSx throughput bottlenecks](#distributed-ts-data-parallel-fxs-bottleneck "#distributed-ts-data-parallel-fxs-bottleneck")
- [SageMaker AI distributed
  training job with PyTorch returns deprecation warnings](#distributed-ts-data-parallel-deprecation-warnings "#distributed-ts-data-parallel-deprecation-warnings")

## Using SageMaker AI distributed data

parallel with Amazon SageMaker Debugger and checkpoints

To monitor system bottlenecks, profile framework operations, and debug model output
tensors for training jobs with SageMaker AI distributed data parallel, use Amazon SageMaker Debugger.

However, when you use SageMaker Debugger, SageMaker AI distributed data parallel, and SageMaker AI
checkpoints, you might see an error that looks like the following example.

```
SMDebug Does Not Currently Support Distributed Training Jobs With Checkpointing Enabled
```

This is due to an internal error between Debugger and checkpoints, which occurs when you
enable SageMaker AI distributed data parallel.

- If you enable all three features, SageMaker Python SDK automatically turns off
  Debugger by passing `debugger_hook_config=False`, which is equivalent
  to the following framework `estimator` example.

```
bucket=sagemaker.Session().default_bucket()
base_job_name="sagemaker-checkpoint-test"
checkpoint_in_bucket="checkpoints"

# The S3 URI to store the checkpoints
checkpoint_s3_bucket="s3://{}/{}/{}".format(bucket, base_job_name, checkpoint_in_bucket)

estimator = TensorFlow(
    ...

    distribution={"smdistributed": {"dataparallel": { "enabled": True }}},
    checkpoint_s3_uri=checkpoint_s3_bucket,
    checkpoint_local_path="/opt/ml/checkpoints",
    debugger_hook_config=False
)
```

- If you want to keep using both SageMaker AI distributed data parallel and SageMaker Debugger,
  a workaround is manually adding checkpointing functions to your training script
  instead of specifying the `checkpoint_s3_uri` and
  `checkpoint_local_path` parameters from the estimator. For more
  information about setting up manual checkpointing in a training script, see
  [Saving Checkpoints](distributed-troubleshooting-model-parallel.md#distributed-ts-model-parallel-checkpoints "distributed-troubleshooting-model-parallel.md#distributed-ts-model-parallel-checkpoints").

## An unexpected prefix

attached to model parameter keys

For PyTorch distributed training jobs, an unexpected prefix (`model` for
example) might be attached to `state_dict` keys (model parameters). The SageMaker AI
data parallel library does not directly alter or prepend any model parameter names when
PyTorch training jobs save model artifacts. The PyTorch's distributed training changes
the names in the `state_dict` to go over the network, prepending the prefix.
If you encounter any model failure problem due to different parameter names while you
are using the SageMaker AI data parallel library and checkpointing for PyTorch training, adapt
the following example code to remove the prefix at the step you load checkpoints in your
training script.

```
state_dict = {k.partition('`model.`')[2]:state_dict[k] for k in state_dict.keys()}
```

This takes each `state_dict` key as a string value, separates the string at
the first occurrence of `'model.'`, and takes the third list item (with index 2) of the partitioned string.

For more information about the prefix issue, see a discussion thread at [Prefix parameter names in saved model if trained by multi-GPU?](https://discuss.pytorch.org/t/prefix-parameter-names-in-saved-model-if-trained-by-multi-gpu/494 "https://discuss.pytorch.org/t/prefix-parameter-names-in-saved-model-if-trained-by-multi-gpu/494") in the
_PyTorch discussion forum_.

For more information about the PyTorch methods for saving and loading models, see
[Saving & Loading Model Across Devices](https://pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-model-across-devices "https://pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-model-across-devices") in the _PyTorch
documentation_.

## SageMaker AI distributed training job

stalling during initialization

If your SageMaker AI distributed data parallel training job stalls during initialization when
using EFA-enabled instances, this might be due to a misconfiguration in the security
group of the VPC subnet that's used for the training job. EFA requires a proper security
group configuration to enable traffic between the nodes.

###### To configure inbound and outbound rules for the security group

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. Choose **Security Groups** in the left navigation
   pane.
3. Select the security group that's tied to the VPC subnet you use for training.
4. In the **Details** section, copy the **Security group ID**.
5. On the **Inbound rules** tab, choose **Edit inbound rules**.
6. On the **Edit inbound rules** page, do the
   following:
   1. Choose **Add rule**.
   2. For **Type**, choose **All traffic**.
   3. For **Source**, choose **Custom**, paste the security group ID into the
      search box, and select the security group that pops up.

7. Choose **Save rules** to finish configuring the
   inbound rule for the security group.
8. On the **Outbound rules** tab, choose **Edit outbound rules**.
9. Repeat the step 6 and 7 to add the same rule as an outbound rule.

After you complete the preceding steps for configuring the security group with the
inbound and outbound rules, re-run the training job and verify if the stalling issue is
resolved.

For more information about configuring security groups for VPC and EFA, see [Security
groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") and [Elastic Fabric Adapter](../../../AWSEC2/latest/UserGuide/efa.md "../../../AWSEC2/latest/UserGuide/efa.md").

## SageMaker AI distributed

training job stalling at the end of training

One of the root causes of stalling issues at the end of training is a mismatch in the
number of batches that are processed per epoch across different ranks. All workers
(GPUs) synchronize their local gradients in the backward pass to ensure they all have
the same copy of the model at the end of the batch iteration. If the batch sizes are
unevenly assigned to different worker groups during the final epoch of training, the
training job stalls. For example, while a group of workers (group A) finishes processing
all batches and exits the training loop, another group of workers (group B) starts
processing another batch and still expects communication from group A to synchronize the
gradients. This causes group B to wait for group A, which already completed training and
does not have any gradients to synchronize.

Therefore, when setting up your training dataset, it is important that each worker
gets the same number of data samples so that each worker goes through the same number of
batches while training. Make sure each rank gets the same number of batches to avoid
this stalling issue.

## Observing scaling

efficiency degradation due to Amazon FSx throughput bottlenecks

One potential cause of lowered scaling efficiency is the FSx throughput limit. If you
observe a sudden drop in scaling efficiency when you switch to a larger training
cluster, try using a larger FSx for Lustre file system with a higher throughput limit. For
more information, see [Aggregate file
system performance](../../../fsx/latest/LustreGuide/performance.md#fsx-aggregate-perf "../../../fsx/latest/LustreGuide/performance.md#fsx-aggregate-perf") and [Managing storage and
throughput capacity](../../../fsx/latest/LustreGuide/managing-storage-capacity.md "../../../fsx/latest/LustreGuide/managing-storage-capacity.md") in the _Amazon FSx for Lustre User
Guide_.

## SageMaker AI distributed

training job with PyTorch returns deprecation warnings

Since v1.4.0, the SageMaker AI distributed data parallelism library works as a backend of
PyTorch distributed. Because of the breaking change of using the library with PyTorch,
you might encounter a warning message that the `smdistributed` APIs for the
PyTorch distributed package are deprecated. The warning message should be similar to the
following:

```
smdistributed.dataparallel.torch.dist is deprecated in the SageMaker AI distributed data parallel library v1.4.0+.
Please use torch.distributed and specify 'smddp' as a backend when initializing process group as follows:
torch.distributed.init_process_group(backend='smddp')
For more information, see the library's API documentation at
https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-modify-sdp-pt.html
```

In v1.4.0 and later, the library only needs to be imported once at the top of your
training script and set as the backend during the PyTorch distributed initialization.
With the single line of backend specification, you can keep your PyTorch training script
unchanged and directly use the PyTorch distributed modules. See [Use the SMDDP library in your PyTorch training
script](data-parallel-modify-sdp-pt.md "data-parallel-modify-sdp-pt.md")
to learn about the breaking changes and the new way to use the library with
PyTorch.

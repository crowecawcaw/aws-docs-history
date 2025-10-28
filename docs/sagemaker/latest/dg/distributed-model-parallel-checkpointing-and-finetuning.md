# Checkpointing and Fine-Tuning a Model

with Model Parallelism

The SageMaker model parallelism library provides checkpointing APIs to save the model state
and the optimizer state split by the various model parallelism strategies, and to
load checkpoints for continuous training from where you want to restart training and fine-tune.
The APIs also support options to save the model and optimizer states partially or fully.

###### Topics

- [Checkpointing a
  distributed model](#distributed-model-parallel-checkpoint "#distributed-model-parallel-checkpoint")
- [Fine-tuning a distributed model](#distributed-model-parallel-fine-tuning "#distributed-model-parallel-fine-tuning")

## Checkpointing a

distributed model

Choose one of the following topics depending on the framework between PyTorch and
TensorFlow and the version of the SageMaker model parallelism library you use.

###### Topics

- [Checkpointing
  a distributed PyTorch model (for the SageMaker model parallelism library v1.10.0
  and later)](#model-parallel-extended-features-pytorch-checkpoint "#model-parallel-extended-features-pytorch-checkpoint")
- [Checkpointing a distributed PyTorch model (for the SageMaker model parallelism
  library between v1.6.0 and v1.9.0)](#model-parallel-extended-features-pytorch-saving-loading-checkpoints "#model-parallel-extended-features-pytorch-saving-loading-checkpoints")
- [Checkpointing a
  distributed TensorFlow model](#distributed-model-parallel-checkpoint-tensorflow "#distributed-model-parallel-checkpoint-tensorflow")

### Checkpointing

a distributed PyTorch model (for the SageMaker model parallelism library v1.10.0
and later)

The SageMaker model parallelism library provides checkpoint APIs to save and load full
or partial checkpoints of the distributed model state and its optimizer
state.

###### Note

This checkpointing method is recommended if you use PyTorch and the SageMaker model
parallelism library v1.10.0 or later.

**Partial checkpointing**

To save checkpoints of a model trained with model parallelism, use the [`smdistributed.modelparallel.torch.save_checkpoint`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.save_checkpoint "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.save_checkpoint") API
with the partial checkpointing option set to true (`partial=True`). This
saves each model partition individually. In addition to the model and the optimizer
state, you can also save any additional custom data through the
`user_content` argument. The checkpointed model, optimizer, and user
content are saved as separate files. The `save_checkpoint` API call
creates checkpoint folders in the following structure.

```
- path
  - ${tag}_partial (folder for partial checkpoints)
    - model_rankinfo.pt
    - optimizer_rankinfo.pt
    - fp16_states_rankinfo.pt
    - user_content.pt
  - $tag (checkpoint file for full checkpoints)
  - user_content_$tag (user_content file for full checkpoints)
  - newest (a file that indicates the newest checkpoint)
```

To resume training from partial checkpoints, use the [`smdistributed.modelparallel.torch.resume_from_checkpoint`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.resume_from_checkpoint "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.resume_from_checkpoint")
API with `partial=True`, and specify the checkpoint directory and the tag
used while saving the partial checkpoints. Note that the actual loading of model
weights happens after model partitioning, during the first run of the
`smdistributed.modelparallel.torch.step`-decorated training step
function.

When saving a partial checkpoint, the library also saves the model partition decision
as files with `.pt` file extension. Conversely, when resuming from the
partial checkpoint, the library loads the partition decision files together. Once the
partition decision is loaded, you can't change the partition.

The following code snippet shows how to set the checkpoint APIs in a PyTorch
training script.

```
import smdistributed.modelparallel.torch as smp

model = ...
model = smp.DistributedModel(model)
optimizer = ...
optimizer = smp.DistributedOptimizer(optimizer)
user_content = ...     # additional custom data
checkpoint_path = "`/opt/ml/checkpoint/model_parallel`"

# Save a checkpoint.
smp.save_checkpoint(
    path=`checkpoint_path`,
    tag=f"`total_steps{total_steps}`",
    **partial=`True`**,
    model=`model`,
    optimizer=`optimizer`,
    user_content=`user_content`
    num_kept_partial_checkpoints=`5`
)

# Load a checkpoint.
# This automatically loads the most recently saved checkpoint.
smp_checkpoint = smp.resume_from_checkpoint(
    path=`checkpoint_path`,
    **partial=`True`**
)
```

**Full checkpointing**

To save the final model artifact for inference purposes, use the
`smdistributed.modelparallel.torch.save_checkpoint` API with
`partial=False`, which combines the model partitions to create a single
model artifact. Note that this does not combine the optimizer states.

To initialize training with particular weights, given a full model checkpoint, you can
use the `smdistributed.modelparallel.torch.resume_from_checkpoint` API with
`partial=False`. Note that this does not load optimizer states.

###### Note

With tensor parallelism, in general, the `state_dict` must be
translated between the original model implementation and the
`DistributedModel` implementation. Optionally, you can provide the
`state_dict` translation function as an argument to the
`smdistributed.modelparallel.torch.resume_from_checkpoint`. However,
for [Supported Models Out of the Box](model-parallel-extended-features-pytorch-hugging-face.md#model-parallel-extended-features-pytorch-hugging-face-out-of-the-box "model-parallel-extended-features-pytorch-hugging-face.md#model-parallel-extended-features-pytorch-hugging-face-out-of-the-box"), the library takes care of this translation automatically.

The following code shows an example of how to use the checkpoint APIs for fully
checkpointing a PyTorch model trained with model parallelism.

```
import smdistributed.modelparallel.torch as smp

model = ...
model = smp.DistributedModel(model)
optimizer = ...
optimizer = smp.DistributedOptimizer(optimizer)
user_content = ...     # additional custom data
checkpoint_path = "`/opt/ml/checkpoint/model_parallel`"

# Save a checkpoint.
smp.save_checkpoint(
    path=`checkpoint_path`,
    tag=f"`total_steps{total_steps}`",
    **partial=`False`**,
    model=`model`,
    optimizer=`optimizer`,
    user_content=`user_content`
    num_kept_partial_checkpoints=`5`
)

# Load a checkpoint.
# This automatically loads the most recently saved checkpoint.
smp_checkpoint = smp.resume_from_checkpoint(
    path=`checkpoint_path`,
    **partial=`False`**
)
```

### Checkpointing a distributed PyTorch model (for the SageMaker model parallelism

library between v1.6.0 and v1.9.0)

The SageMaker model parallelism library provides Python functions for saving partial or
full checkpoints for training jobs with tensor parallelism. The following procedure
shows how to use [`smp.save()`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.save "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.save") and [`smp.load()`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.load "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.load") to save and load a checkpoint when you use
tensor parallelism.

###### Note

This checkpointing method is recommended if you use PyTorch, [Tensor
Parallelism](model-parallel-extended-features-pytorch-tensor-parallelism.md "model-parallel-extended-features-pytorch-tensor-parallelism.md"), and
the SageMaker model parallelism library between v1.6.0 and v1.9.0.

1. Prepare a model object and wrap it with the library's wrapper function
   `smp.DistributedModel()`.

```
model = MyModel(...)
model = smp.DistributedModel(model)
```

2. Prepare an optimizer for the model. A set of model parameters is an
   iterable argument required by optimizer functions. To prepare a set of model
   parameters, you must process `model.parameters()` to assign
   unique IDs to individual model parameters.

If there are parameters with duplicated IDs in the model parameter
iterable, loading the checkpointed optimizer state fails. To create an
iterable of model parameters with unique IDs for your optimizer, see the
following:

```
unique_params = []
unique_params_set = set()
for p in model.parameters():
  if p not in unique_params_set:
    unique_params.append(p)
    unique_params_set.add(p)
del unique_params_set

optimizer = MyOpt(unique_params, ...)
```

3. Wrap the optimizer using the library's wrapper function
   `smp.DistributedOptimizer()`.

```
optimizer = smp.DistributedOptimizer(optimizer)
```

4.  Save the model and the optimizer state using [`smp.save()`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.save "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.save"). Depending on how you want to save
    checkpoints, choose one of the following two options:
    - **Option 1:** Save a partial model on
      each `mp_rank` for a single `MP_GROUP`.

    ```
    model_dict = model.local_state_dict() # save a partial model
    opt_dict = optimizer.local_state_dict() # save a partial optimizer state
    # Save the dictionaries at rdp_rank 0 as a checkpoint
    if smp.rdp_rank() == 0:
        smp.save(
            {"model_state_dict": model_dict, "optimizer_state_dict": opt_dict},
            f"/checkpoint.pt",
            partial=True,
        )
    ```

    With tensor parallelism, the library saves checkpointed files
    named in the following format:
    `checkpoint.pt_{pp_rank}_{tp_rank}`.

    ###### Note

    With tensor parallelism, make sure you set the if statement as
    `if smp.rdp_rank() == 0` instead of `if
 smp.dp_rank() == 0`. When the optimizer state is
    sharded with tensor parallelism, all reduced-data parallel ranks
    must save their own partition of the optimizer state. Using a
    wrong _if_ statement for
    checkpointing might result in a stalling training job. For more
    information about using `if smp.dp_rank() == 0`
    without tensor parallelism, see [General Instruction for Saving and Loading](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#general-instruction-for-saving-and-loading "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#general-instruction-for-saving-and-loading") in the
    _SageMaker Python SDK
    documentation_.
    - **Option 2:** Save the full
      model.

    ```
    if smp.rdp_rank() == 0:
        model_dict = model.state_dict(gather_to_rank0=True) # save the full model
        if smp.rank() == 0:
            smp.save(
                {"model_state_dict": model_dict},
                "/checkpoint.pt",
                partial=False,
            )
    ```

    ###### Note

    Consider the following for full checkpointing:

        + If you set `gather_to_rank0=True`, all
         ranks other than `0` return empty
         dictionaries.
        + For full checkpointing, you can only checkpoint the
         model. Full checkpointing of optimizer states is
         currently not supported.
        + The full model only needs to be saved at
         `smp.rank() == 0`.

5.  Load the checkpoints using [`smp.load()`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.load "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.load"). Depending on how you checkpointed
    in the previous step, choose one of the following two options:
    - **Option 1:** Load the partial
      checkpoints.

    ```
    checkpoint = smp.load("/checkpoint.pt", partial=True)
    model.load_state_dict(checkpoint["model_state_dict"], same_partition_load=False)
    optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
    ```

    You can set `same_partition_load=True` in
    `model.load_state_dict()` for a faster load, if you
    know that the partition will not change.
    - **Option 2:** Load the full
      checkpoints.

    ```
    if smp.rdp_rank() == 0:
        checkpoint = smp.load("/checkpoint.pt", partial=False)
        model.load_state_dict(checkpoint["model_state_dict"])
    ```

    The `if smp.rdp_rank() == 0` condition is not required,
    but it can help avoid redundant loading among different
    `MP_GROUP`s. Full checkpointing optimizer state dict
    is currently not supported with tensor parallelism.

### Checkpointing a

distributed TensorFlow model

To save a TensorFlow model while training with model parallelism, use the
following functions provided by the SageMaker model parallelism library.

- [`smdistributed.modelparallel.tensorflow.DistributedModel.save_model`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_tensorflow.html#smp.DistributedModel.save_model "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_tensorflow.html#smp.DistributedModel.save_model")
- [`smdistributed.modelparallel.tensorflow.CheckpointManager`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_tensorflow.html#smp.CheckpointManager "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_tensorflow.html#smp.CheckpointManager")

## Fine-tuning a distributed model

The fine-tuning needs to be configured in your training script. The following code
snippet shows an example structure of a training script using the [AutoModelForCausalLM](https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoModelForCausalLM "https://huggingface.co/docs/transformers/main/en/model_doc/auto#transformers.AutoModelForCausalLM") class of Hugging Face Transformers with modifications
for registering the `smdistributed.model.parallel.torch` modules and settings
for fine-tuning.

###### Note

Fine-tuning a distributed transformer (a Transformer model wrapped by
`smp.DistributedModel()`) with the [smp.delayed_param_initialization](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.delay_param_initialization "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed.modelparallel.torch.delay_param_initialization") function activated requires the
fine-tuning job to be configured with an FSx for Lustre file system. In cases where
you want to fine-tune a large-scale model with the delayed parameter initialization
option, you should set up an FSx for Lustre file system.

```
import argparse
from transformers import AutoModelForCausalLM
import smdistributed.modelparallel
import smdistributed.modelparallel.torch as smp

def parse_args():

    parser = argparse.ArgumentParser()

    # set an arg group for model
    model_grp = parser.add_argument_group(
        title="model", description="arguments to describe model configuration"
    )

    ... # set up numerous args to parse from the configuration dictionary to the script for training

    # add arg for activating fine-tuning
    model_grp.add_argument(
        "--fine_tune",
        type=int,
        default=0,
        help="Fine-tune model from checkpoint or pretrained model",
    )

def main():
    """Main function to train GPT."""
    args = parse_args()

    ... # parse numerous args

    if args.fine_tune > 0 and args.delayed_param > 0 and smp.rank() == 0:
        pretrained_model = AutoModelForCausalLM.from_pretrained(
            args.model_name or args.model_dir
        )
        model_state_dict = pretrained_model.state_dict()
        path = os.path.join(args.model_dir, "fullmodel.pt")
        torch.save(model_state_dict, path)

    # create a Transformer model and wrap by smp.model_creation()
    # with options to configure model parallelism parameters offered by SageMaker AI
    with smp.model_creation(
        tensor_parallelism=smp.tp_size() > 1 or args.use_distributed_transformer > 0,
        zero_init=args.use_distributed_transformer == 0,
        dtype=dtype,
        distribute_embedding=args.sharded_data_parallel_degree > 1 and smp.tp_size() > 1,
        use_alibi=args.alibi > 0,
        attention_in_fp32=args.attention_in_fp32 > 0,
        fp32_residual_addition=args.residual_addition_in_fp32 > 0,
        query_key_layer_scaling=args.query_key_layer_scaling > 0 and args.bf16 < 1,
        fused_softmax=args.fused_softmax > 0,
        fused_dropout=args.fused_dropout > 0,
        fused_bias_gelu=args.fused_bias_gelu > 0,
        flash_attention=args.flash_attention > 0,
    ):
        if args.fine_tune > 0 and args.delayed_param == 0:
            model = AutoModelForCausalLM.from_pretrained(
                args.model_name or args.model_dir
            )
        else:
            model = AutoModelForCausalLM.from_config(model_config)

    # wrap the model by smp.DistributedModel() to apply SageMaker model parallelism
    model = smp.DistributedModel(
        model, trace_device="gpu", backward_passes_per_step=args.gradient_accumulation
    )

    # wrap the optimizer by smp.DistributedOptimizer() to apply SageMaker model parallelism
    optimizer= ... # define an optimizer
    optimizer = smp.DistributedOptimizer(
        optimizer,
        static_loss_scale=None,
        dynamic_loss_scale=True,
        dynamic_loss_args={"scale_window": 1000, "min_scale": 1, "delayed_shift": 2},
    )

    # for fine-tuning, use smp.resume_from_checkpoint() to load a pre-trained model
    if args.fine_tune > 0 and args.delayed_param > 0:
        smp.resume_from_checkpoint(args.model_dir, tag="fullmodel.pt", partial=False)
```

For a complete example of training scripts and Jupyter notebooks, see the [GPT-2 examples for PyTorch](https://github.com/aws/amazon-sagemaker-examples/tree/main/training/distributed_training/pytorch/model_parallel/gpt2 "https://github.com/aws/amazon-sagemaker-examples/tree/main/training/distributed_training/pytorch/model_parallel/gpt2") in the _SageMaker AI Examples GitHub
repository_.

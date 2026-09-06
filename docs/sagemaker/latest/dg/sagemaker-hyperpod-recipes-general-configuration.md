

# General configuration
<a name="sagemaker-hyperpod-recipes-general-configuration"></a>

The config.yaml file specifies the training recipe and the cluster. It also includes runtime configurations such as environment variables for the training job.

```
defaults:
  - _self_
  - cluster: slurm 
  - recipes: training/llama/hf_llama3_8b_seq8192_gpu
instance_type: p5.48xlarge
git:
  repo_url_or_path: null
  branch: null
  commit: null
  entry_script: null
  token: null
env_vars:
  NCCL_DEBUG: WARN
```

You can modify the following parameters in `config.yaml`:

1. `defaults`: Specify your default settings, such as the default cluster or default recipes.

1. `instance_type`: Modify the Amazon EC2 instance type to match the instance type that you're using.

1. `git`: Specify the location of the SageMaker HyperPod recipe adapter repository for the training job.

1. `env_vars`: You can specify the environment variables to be passed into your runtime training job. For example, you can adjust the logging level of NCCL by specifying the NCCL\_DEBUG environment variable.

The recipe is the core configuration that defines your training job architecture. This file includes many important pieces of information for your training job, such as the following:
+ Whether to use model parallelism
+ The source of your datasets
+ Mixed precision training
+ Checkpointing-related configurations

You can use the recipes as-is. You can also use the following information to modify them.

## run
<a name="run"></a>

The following is the basic run information for running your training job.

```
run:
  name: llama-8b
  results_dir: ${base_results_dir}/${.name}
  time_limit: "6-00:00:00"
  model_type: hf
```

1. `name`: Specify the name for your training job in the configuration file.

1. `results_dir`: You can specify the directory where the results of your training job are stored.

1. `time_limit`: You can set a maximum training time for your training job to prevent it from occupying hardware resources for too long.

1. `model_type`: You can specify the type of model you are using. For example, you can specify `hf` if your model is from HuggingFace.

## exp\_manager
<a name="exp-manager"></a>

The exp\_manager configures the experiment. With the exp\_manager, you can specify fields such as the output directory or checkpoint settings. The following is an example of how you can configure the exp\_manager.

```
exp_manager:
  exp_dir: null
  name: experiment
  create_tensorboard_logger: True
```

1. `exp_dir`: The experiment directory includes the standard output and standard error files for your training job. By default, it uses your current directory.

1. `name`: The experiment name used to identify your experiment under the exp\_dir.

1. `create_tensorboard_logger`: Specify `True` or `False` to enable or disable the TensorBoard logger.

## Checkpointing
<a name="checkpointing"></a>

Here are three types of checkpointing we support:
+ Auto checkpointing
+ Manual checkpointing
+ Full checkpointing

### Auto checkpointing
<a name="auto-checkpointing"></a>

If you're saving or loading checkpoints that are automatically managed by the SageMaker HyperPod recipe adapter, you can enable `auto_checkpoint`. To enable `auto_checkpoint`, set `enabled` to `True`. You can use auto checkpointing for both training and fine-tuning. You can use auto checkpoinitng for both shared file systems and Amazon S3.

```
exp_manager
  checkpoint_dir: ${recipes.exp_manager.exp_dir}/checkpoints/
  auto_checkpoint:
    enabled: True
```

Auto checkpoint is saving the local\_state\_dict asynchronously with an automatically computed optimal saving interval.

**Note**  
Under this checkpointing mode, the auto saved checkpointing doesn't support re-sharding between training runs. To resume from the latest auto saved checkpoint, you must preserve the same shard degrees. You don't need to specify extra information to auto resume.

### Manual checkpointing
<a name="manual-checkpointing"></a>

You can modify `checkpoint_callback_params` to asynchronously save an intermediate checkpoint in shared\_state\_dict. For example, you can specify the following configuration to enable sharded checkpointing every 10 steps and keep the latest 3 checkpoints.

Sharded checkpointing allows you to change the shard degrees between training runs and load the checkpoint by setting `resume_from_checkpoint`.

**Note**  
If is a PEFT fine tuning, sharded checkpointing doesn't support Amazon S3.
Auto and manual checkpointing are mutually exclusive.
Only FSDP shard degrees and replication degrees changes are allowed.

```
exp_manager:
  checkpoint_callback_params:
    # Set save_top_k = 0 to disable sharded checkpointing
    save_top_k: 3
    every_n_train_steps: 10
    monitor: "step"
    mode: "max"
    save_last: False
  resume_from_checkpoint: ${recipes.exp_manager.exp_dir}/checkpoints/
```

To learn more about checkpointing, see [Checkpointing using SMP](model-parallel-core-features-v2-checkpoints.md).

### Full checkpointing
<a name="full-checkpointing"></a>

The exported full\_state\_dict checkpoint can be used for inference or fine tuning. You can load a full checkpoint through hf\_model\_name\_or\_path. Under this mode, only the model weights are saved.

To export the full\_state\_dict model, you can set the following parameters.

**Note**  
Currently, full checkpointing isn't supported for Amazon S3 checkpointing. You can't set the S3 path for `exp_manager.checkpoint_dir` if you're enabling full checkpointing. However, you can set `exp_manager.export_full_model.final_export_dir` to a specific directory on your local filesystem while setting `exp_manager.checkpoint_dir` to an Amazon S3 path.

```
exp_manager:
  export_full_model:
    # Set every_n_train_steps = 0 to disable full checkpointing
    every_n_train_steps: 0
    save_last: True
    final_export_dir : null
```

## model
<a name="model"></a>

Define various aspects of your model architecture and training process. This includes settings for model parallelism, precision, and data handling. Below are the key components you can configure within the model section:

### model parallelism
<a name="model-parallelism"></a>

After you've specified the recipe, you define the model that you're training. You can also define the model parallelism. For example, you can define tensor\_model\_parallel\_degree. You can enable other features like training with FP8 precision. For example, you can train a model with tensor parallelism and context parallelism:

```
model:
  model_type: llama_v3
  # Base configs
  train_batch_size: 4
  val_batch_size: 1
  seed: 12345
  grad_clip: 1.0

  # Model parallelism
  tensor_model_parallel_degree: 4
  expert_model_parallel_degree: 1
  context_parallel_degree: 2
```

To gain a better understanding of different types of model parallelism techniques, you can refer to the following approaches:

1. [Tensor parallelism](model-parallel-core-features-v2-tensor-parallelism.md)

1. [Expert parallelism](model-parallel-core-features-v2-expert-parallelism.md)

1. [Context parallelism](model-parallel-core-features-v2-context-parallelism.md)

1. [Hybrid sharded data parallelism](model-parallel-core-features-v2-sharded-data-parallelism.md)

### FP8
<a name="fp8"></a>

To enable FP8 (8-bit floating-point precision), you can specify the FP8-related configuration in the following example:

```
model:
  # FP8 config
  fp8: True
  fp8_amax_history_len: 1024
  fp8_amax_compute_algo: max
```

It's important to note that the FP8 data format is currently supported only on the P5 instance type. If you are using an older instance type, such as P4, disable the FP8 feature for your model training process. For more information about FP8, see [Mixed precision training](model-parallel-core-features-v2-mixed-precision.md).

### data
<a name="data"></a>

You can specify your custom datasets for your training job by adding the data paths under data. The data module in our system supports the following data formats:

1. JSON

1. JSONGZ (Compressed JSON)

1. ARROW

However, you are responsible for preparing your own pre-tokenized dataset. If you're an advanced user with specific requirements, there is also an option to implement and integrate a customized data module. For more information on HuggingFace datasets, see [Datasets](https://huggingface.co/docs/datasets/v3.1.0/en/index).

```
model:
  data:
    train_dir: /path/to/your/train/data
    val_dir: /path/to/your/val/data
    dataset_type: hf
    use_synthetic_data: False
```

You can specify how you're training the model. By default, the recipe uses pre-training instead of fine-tuning. The following example configures the recipe to run a fine-tuning job with LoRA (Low-Rank Adaptation).

```
model:
  # Fine tuning config
  do_finetune: True
  # The path to resume from, needs to be HF compatible
  hf_model_name_or_path: null
  hf_access_token: null
  # PEFT config
  peft:
    peft_type: lora
    rank: 32
    alpha: 16
    dropout: 0.1
```

For information about the recipes, see [SageMaker HyperPod recipes](https://github.com/aws/sagemaker-hyperpod-recipes).
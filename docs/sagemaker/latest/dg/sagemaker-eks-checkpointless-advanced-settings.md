# Advanced settings

HyperPod checkpointless training currently has getting started examples for two model architectures: GPT-OSS and Llama 3. To enable checkpointless training for your custom model, follow the integration guide, which involves modifying:

- Entry script, ie: the `main()` function
- Recipe
- Launch script
  **step 1.1: Modification - Entry script**

- Add the checkpointless training imports

```
# 1. add the imports
from hyperpod_checkpointless_training.nemo_plugins.megatron_strategy import CheckpointlessMegatronStrategy
from hyperpod_checkpointless_training.inprocess.health_check import CudaHealthCheck
from hyperpod_checkpointless_training.inprocess.wrap import HPCallWrapper, HPWrapper
from hyperpod_checkpointless_training.dataloader.mmap_data_module import MMAPDataModule
from hyperpod_checkpointless_training.dataloader.config import CacheResumeMMAPConfig
from hyperpod_checkpointless_training.dataloader.utils import CheckpointlessDataModule
from hyperpod_checkpointless_training.nemo_plugins.checkpoint_manager import PEFTCheckpointManager
from hyperpod_checkpointless_training.nemo_plugins.opt_patches import patch_megatron_optimizer
from hyperpod_checkpointless_training.nemo_plugins.checkpoint_connector import CheckpointlessCompatibleConnector
patch_megatron_optimizer()
from typing import Optional
from hyperpod_checkpointless_training.inprocess.train_utils import HPAgentK8sAPIFactory
from hyperpod_checkpointless_training.inprocess.abort import CheckpointlessFinalizeCleanup, CheckpointlessAbortManager
```

- Wrap the datamodule with MMAP

```
@property
def datamodule(self):
  # 2. add MMAP datamodule with checkpointless
  return CheckpointlessDataModule(
    cfg=self.cfg,
    data_module=MMAPDataModule(
      data_module=MYDataModule(...),
      mmap_config=CacheResumeMMAPConfig(
        cache_dir=self.cfg.mmap.cache_dir,
                 checkpoint_frequency=self.cfg.mmap.checkpoint_frequency),

      )
    )

@property
def strategy(self):
  # 2.2. Update the strategy.
  return CheckpointlessMegatronStrategy(
    **self.cfg.strategy,
    ddp=self.ddp)
```

- Wrap the main with checkpointless - this enables an in-process recovery to be triggered on fault

```
# 3.1 Wrap the main with checkpointless
@HPWrapper(
  health_check=CudaHealthCheck(),
  hp_api_factory=HPAgentK8sAPIFactory(),
  abort_timeout=60.0,
  checkpoint_manager=PEFTCheckpointManager(enable_offload=True),
  abort=CheckpointlessAbortManager.get_default_checkpointless_abort(),
  finalize=CheckpointlessFinalizeCleanup(),
)
def run_main(cfg, caller: Optional[HPCallWrapper] = None):
  ...
 resume = instantiate(cfg.resume)
  # 3.2 Checkpointless framework level changes.
  trainer.fresume = resume
  trainer._checkpoint_connector = CheckpointlessCompatibleConnector(trainer)
  trainer.wrapper = caller
```

**step 1.2: Modification - Model Config**

- Create another yaml config file with checkpointless training overrides.

```
defaults:
 - mymodel_config
 - _self_

callbacks:
 - _target_: nemo.utils.exp_manager.TimingCallback
 - _target_: nemo.lightning.pytorch.callbacks.GarbageCollectionCallback
  gc_interval_train: 5
  gc_interval_val: 5
 - _target_: nemo.lightning.pytorch.callbacks.megatron_comm_overlap.MegatronCommOverlapCallback
  tp_comm_overlap: False
 - _target_: hyperpod_checkpointless_training.nemo_plugins.fault_injection.HPFaultInjectionCallback
  test_fault_config:
   fault_type: "ipr"
   fault_prob_after_bwd: 0
   fault_prob_between_lock: 0
   fault_prob_during_fwd: 0
   fault_prob_during_bwd: 0
   fault_prob_random: 1
   fault_ranks: [8]
   steps_before_fault: 3
 - _target_: hyperpod_checkpointless_training.nemo_plugins.callbacks.CheckpointlessCallback # Checkpointless changes.
  enable_inprocess: true
  enable_checkpointless: true
  enable_checksum: false
  clean_tensor_hook : true
 - _target_: hyperpod_checkpointless_training.nemo_plugins.datamodule_epoch_callback.DataModuleEpochCallback


resume:
 _target_: hyperpod_checkpointless_training.nemo_plugins.resume.CheckpointlessAutoResume # Checkpointless changes.
 restore_config:
  _target_: nemo.lightning.RestoreConfig
  path: ""
  load_artifacts: false
 resume_from_directory: ${logger.ckpt.dirpath}
 resume_if_exists: true
 resume_past_end: true
 resume_ignore_no_checkpoint: true

strategy:
 num_distributed_optimizer_instances: 2 # Checkpointless changes.
```

**step 1.3: Modification - Job Config**

Modify the job config yaml to

- turn on Rootless by exposing the environment variables and,
- add the `inprocess-restart` flag to the hyperpodrun command

```
# Enable Rootless features
  export HPCT_USE_ROOTLESS=1 && \
  sysctl -w net.ipv4.ip_local_port_range="20000 65535" && \

  hyperpodrun --nproc_per_node=8 \
                    ...
                    --inprocess-restart \
                    ...
```

**step 1.4: launch the job with kubectl**

```
kubectl apply -f your_job_config.yaml
```

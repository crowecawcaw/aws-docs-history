

# Use the PyTorch framework estimators in the SageMaker Python SDK
<a name="data-parallel-framework-estimator"></a>

You can launch distributed training by adding the `distribution` argument to the SageMaker AI [`PyTorch`](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) framework estimator. The SageMaker AI distributed data parallelism (SMDDP) library supports PyTorch distributed training.

**Note**  
SMDDP discontinued TensorFlow support after v2.11.0. For distributed training with TensorFlow, use alternative distribution strategies.

The following launcher options are available for launching PyTorch distributed training.
+ `pytorchddp` – This option runs `mpirun` and sets up environment variables needed for running PyTorch distributed training on SageMaker AI. To use this option, pass the following dictionary to the `distribution` parameter.

  ```
  { "pytorchddp": { "enabled": True } }
  ```
+ `torch_distributed` – This option runs `torchrun` and sets up environment variables needed for running PyTorch distributed training on SageMaker AI. To use this option, pass the following dictionary to the `distribution` parameter.

  ```
  { "torch_distributed": { "enabled": True } }
  ```
+ `smdistributed` – This option also runs `mpirun` but with `smddprun` that sets up environment variables needed for running PyTorch distributed training on SageMaker AI.

  ```
  { "smdistributed": { "dataparallel": { "enabled": True } } }
  ```

If you chose to replace NCCL `AllGather` to SMDDP `AllGather`, you can use all three options. Choose one option that fits with your use case.

If you chose to replace NCCL `AllReduce` with SMDDP `AllReduce`, you should choose one of the `mpirun`-based options: `smdistributed` or `pytorchddp`. You can also add additional MPI options as follows.

```
{ 
    "pytorchddp": {
        "enabled": True, 
        "custom_mpi_options": "-verbose -x NCCL_DEBUG=VERSION"
    }
}
```

```
{ 
    "smdistributed": { 
        "dataparallel": {
            "enabled": True, 
            "custom_mpi_options": "-verbose -x NCCL_DEBUG=VERSION"
        }
    }
}
```

The following code sample shows the basic structure of a ModelTrainer with distributed training options.

```
from sagemaker.train import ModelTrainer
from sagemaker.train.configs import SourceCode, Compute, InputData
from sagemaker.core import image_uris

# Retrieve the training image for the desired PyTorch version
training_image = image_uris.retrieve(
    framework="pytorch",
    region="{{us-west-2}}",
    version="{{2.0.1}}",
    py_version="{{py310}}",
    instance_type="{{ml.p4d.24xlarge}}",
    image_scope="training"
)

source_code = SourceCode(
    source_dir="{{subdirectory-to-your-code}}",
    entry_script="{{adapted-training-script.py}}"
)

compute = Compute(
    # For running a multi-node distributed training job, specify a value greater than 1
    # Example: 2,3,4,..8
    instance_count={{2}},

    # Instance types supported by the SageMaker AI data parallel library: 
    # ml.p4d.24xlarge, ml.p4de.24xlarge
    instance_type="{{ml.p4d.24xlarge}}"
)

pt_model_trainer = ModelTrainer(
    training_image=training_image,
    base_job_name="{{training_job_name_prefix}}",
    source_code=source_code,
    role="{{SageMakerRole}}",
    compute=compute,

    # Activate distributed training with SMDDP
    distribution={ "pytorchddp": { "enabled": True } }  # mpirun, activates SMDDP AllReduce OR AllGather
    # distribution={ "torch_distributed": { "enabled": True } }  # torchrun, activates SMDDP AllGather
    # distribution={ "smdistributed": { "dataparallel": { "enabled": True } } }  # mpirun, activates SMDDP AllReduce OR AllGather
)

pt_model_trainer.train(input_data_config=[
    InputData(channel_name="training", data_source="{{s3://bucket/path/to/training/data}}")
])
```

**Note**  
PyTorch Lightning and its utility libraries such as Lightning Bolts are not preinstalled in the SageMaker AI PyTorch DLCs. Create the following `requirements.txt` file and save in the source directory where you save the training script.  

```
# requirements.txt
pytorch-lightning
lightning-bolts
```
For example, the tree-structured directory should look like the following.  

```
├── pytorch_training_launcher_jupyter_notebook.ipynb
└── sub-folder-for-your-code
    ├──  adapted-training-script.py
    └──  requirements.txt
```
For more information about specifying the source directory to place the `requirements.txt` file along with your training script and a job submission, see [Using third-party libraries](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) in the *Amazon SageMaker AI Python SDK documentation*.

**Considerations for activating SMDDP collective operations and using the right distributed training launcher options**
+ SMDDP `AllReduce` and SMDDP `AllGather` are not mutually compatible at present.
+ SMDDP `AllReduce` is activated by default when using `smdistributed` or `pytorchddp`, which are `mpirun`-based launchers, and NCCL `AllGather` is used.
+ SMDDP `AllGather` is activated by default when using `torch_distributed` launcher, and `AllReduce` falls back to NCCL.
+ SMDDP `AllGather` can also be activated when using the `mpirun`-based launchers with an additional environment variable set as follows.

  ```
  export SMDATAPARALLEL_OPTIMIZE_SDP=true
  ```
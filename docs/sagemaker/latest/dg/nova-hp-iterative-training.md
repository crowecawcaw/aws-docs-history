# Iterative training

Iterative training enables the development of sophisticated training pipelines for Amazon
Nova models by chaining multiple training techniques in sequence. This approach allows you to
layer different customization methods to achieve precisely tailored models.

The process begins by training an Amazon Nova model using one of the standard techniques
(such as SFT, PEFT, or DPO). After completion, you'll find a `manifest.json` file in your
specified S3 output location. This file contains a `checkpoint_s3_bucket` value that indicates
where the trained model is stored.

You can then use this checkpoint location as the `model_name_or_path` parameter in
subsequent training runs, effectively building upon your previous customization work. This
creates a chain of progressive improvements, with each training stage refining the model
further based on your specific requirements.

Iterative training allows you to develop more sophisticated training pipelines to tune
Amazon Nova models. By chaining training modules, you're able to layer training techniques to
customize your models exactly to your needs.

You start by training Amazon Nova using one of the techniques described in [Amazon Nova customization on Amazon SageMaker HyperPod](nova-hp.md "nova-hp.md"). In the output S3 location defined during training, locate the
`manifest.json` file. This file contains the value
`checkpoint_s3_bucket` that indicates where the output model is defined.
You can utilize this output location as the `model_name_or_path` value in
future training runs.

###### Example

The following example steps through a workflow that defines supervised fine-tuning
(SFT) > SFT > direct preference optimization (DPO) iterative training runs for an
Amazon Nova Lite model. First, you must define the run recipe for the initial SFT training of
the foundation model.

```
## Run config
run:
  name: "my-fullrank-run-sft"             # A descriptive name for your training job
  model_type: "amazon.nova-lite-v1:0:300k"  # Model variant specification, do not change
  model_name_or_path: "nova-lite/prod"      # Base model path, do not change
  replicas: 4                               # Number of compute instances for training, allowed values are 4, 8, 16
  data_s3_path: "s3://`Path to training data`"          # Your training data path
  output_s3_path: "s3://`Path to output data location`" # Output artifact path
```

This training job will produce a `manifest.json` file in the path defined at
`output_s3_path` that resembles the following:

`{"checkpoint_s3_bucket":"s3://<escrow bucket>/<job id>/outputs/checkpoints"}`

This checkpoint path can be used in the next iterative training step as the
`model_name_or_path`. Doing so directs the training to use the previous
checkpoint as the base model for the next training method instead of the base foundation
model.

The following step in the example defines a SFT training run on a different set of data,
which can be used to train a model across various sets of interactions.

```
## Run config
run:
  name: "my-fullrank-run-sft-2"             # A descriptive name for your training job
  model_type: "amazon.nova-lite-v1:0:300k"  # Model variant specification, do not change
  model_name_or_path: "s3://`customer-escrow-bucket-unique_id/my-fullrank-run-sft-unique id`/outputs/checkpoints"      # Model checkpoint after 1st SFT run
  replicas: 4                               # Number of compute instances for training, allowed values are 4, 8, 16
  data_s3_path: "s3://`Path to training data #2`"       # Customer data path
  output_s3_path: "s3://`Path to output data location`" # Output artifact path
```

Like the first training set, this will output a similar `manifest.json` file in
the output location:

`{"checkpoint_s3_bucket":"s3://<escrow bucket>/<job id>/outputs/checkpoints"}`

This can then be used as the final input to the last iterative training run using
DPO:

```
## Run config
run:
  name: "my-fullrank-run-dpo"             # A descriptive name for your training job
  model_type: "amazon.nova-lite-v1:0:300k"  # Model variant specification, do not change
  model_name_or_path: "s3://`customer-escrow-bucket-unique_id/my-fullrank-run-sft-2-unique id`/outputs/checkpoints"      # Model checkpoint after 2nd SFT run
  replicas: 4                               # Number of compute instances for training, allowed values are 4, 8, 16
  data_s3_path: "s3://`Path to training data #2`"       # Your training data path
  output_s3_path: "s3://`Path to output data location`" # Output artifact path
```

The output at any step of this iterative training pipeline can be used for either
inference or evaluation as well to check the progress of the model along the way to ensure
it is converging to the desired output.

###### Limitations

Iterative training can be run with any of the available training methods in any
order, for as many iterations you need to achieve your desired outcome. When
iteratively training, both the model and the technique (that is full-rank compared with LoRA
PEFT) must stay consistent. For example, if you attempt to iteratively train with
full-rank fine-tuning after a LoRA PEFT training, the training job will throw an
error. Similarly, if you want to define a Amazon Nova Lite training job on top of a
Amazon Nova Micro checkpoint, you will receive an error.

# Iterative training

Iterative training allows you to develop more sophisticated training pipelines to tune
Amazon Nova models. By chaining training modules, you're able to layer training techniques to
customize your models exactly to your needs.

To begin, you start by training Amazon Nova using one of the techniques described in [SageMaker AI HyperPod training](customize-fine-tune-hyperpod.md "customize-fine-tune-hyperpod.md").
In the output S3 location defined during training, locate the `manifest.json`
file. This file contains the value `checkpoint_s3_bucket` that indicates where
the output model is defined. You can utilize this output location as the
`model_name_or_path` value in future training runs.

For detailed instructions about using iterative training with Amazon Nova model customization, see the [Iterative training](../../../sagemaker/latest/dg/nova-hp-iterative-training.md "../../../sagemaker/latest/dg/nova-hp-iterative-training.md") section from SageMakeruser guide.

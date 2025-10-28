# Use the Debugger APIs to run your own

custom rules

The following code sample shows how to configure a custom rule with the
[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"). This example assumes that the custom rule script you created in the previous step
is located at '_path/to/my_custom_rule.py_'.

```
from sagemaker.debugger import Rule, CollectionConfig

**custom\_rule** = Rule.custom(
    name='MyCustomRule',
    image_uri='759209512951.dkr.ecr.us-west-2.amazonaws.com/sagemaker-debugger-rule-evaluator:latest',
    instance_type='ml.t3.medium',
    source='path/to/my_custom_rule.py',
    rule_to_invoke='CustomGradientRule',
    collections_to_save=[CollectionConfig("gradients")],
    rule_parameters={"threshold": "20.0"}
)
```

The following list explains the Debugger `Rule.custom` API arguments.

- `name` (str): Specify a custom rule name as you want.
- `image_uri` (str): This is the image of the container that has the
  logic of understanding your custom rule. It sources and evaluates the specified
  tensor collections you save in the training job. You can find the list of open
  source SageMaker AI rule evaluator images from [Amazon SageMaker Debugger image URIs for custom rule
  evaluators](debugger-reference.md#debuger-custom-rule-registry-ids "debugger-reference.md#debuger-custom-rule-registry-ids").
- `instance_type` (str): You need to specify an instance to build a
  rule docker container. This spins up the instance in parallel with a training
  container.
- `source` (str): This is the local path or the Amazon S3 URI to your
  custom rule script.
- `rule_to_invoke` (str): This specifies the particular Rule class
  implementation in your custom rule script. SageMaker AI supports only one rule to
  be evaluated at a time in a rule job.
- `collections_to_save` (str): This specifies which tensor
  collections you will save for the rule to run.
- `rule_parameters` (dictionary): This accepts parameter inputs in a
  dictionary format. You can adjust the parameters that you configured in the
  custom rule script.
  After you set up the `custom_rule` object, you can use it for building a SageMaker AI estimator for any training jobs.
  Specify the `entry_point` to your training script. You do not need to make any change of your training script.

```
from sagemaker.tensorflow import TensorFlow

estimator = TensorFlow(
                role=sagemaker.get_execution_role(),
                base_job_name='smdebug-custom-rule-demo-tf-keras',
                entry_point='path/to/your_training_script.py'
                train_instance_type='ml.p2.xlarge'
                ...

                # debugger-specific arguments below
                rules = [**custom\_rule**]
)

estimator.fit()
```

For more variations and advanced examples of using Debugger custom rules, see the following example notebooks.

- [Monitor your training job with Amazon SageMaker Debugger custom rules](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/tensorflow_keras_custom_rule/tf-keras-custom-rule.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/tensorflow_keras_custom_rule/tf-keras-custom-rule.html")
- [PyTorch iterative model pruning of ResNet and AlexNet](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-debugger/pytorch_iterative_model_pruning "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-debugger/pytorch_iterative_model_pruning")
- [Trigger Amazon CloudWatch Events using Debugger Rules to Take an Action Based on Training
  Status with TensorFlow](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-debugger/tensorflow_action_on_rule "https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-debugger/tensorflow_action_on_rule")

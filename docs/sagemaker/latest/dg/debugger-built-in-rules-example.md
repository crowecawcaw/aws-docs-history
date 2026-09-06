

# Example notebooks and code samples to configure Debugger rules
<a name="debugger-built-in-rules-example"></a>

**Note**  
Amazon SageMaker Debugger is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Debugger, but we do not plan to introduce new features. For more information, see [Debugger availability change](debugger-availability-change.md). 

In the following sections, notebooks and code samples of how to use Debugger rules to monitor SageMaker training jobs are provided.

**Topics**
+ [Debugger built-in rules example notebooks](#debugger-built-in-rules-notebook-example)
+ [Debugger built-in rules example code](#debugger-deploy-built-in-rules)
+ [Use Debugger built-in rules with parameter modifications](#debugger-deploy-modified-built-in-rules)

## Debugger built-in rules example notebooks
<a name="debugger-built-in-rules-notebook-example"></a>

The following example notebooks show how to use Debugger built-in rules when running training jobs with Amazon SageMaker AI: 
+ [Using a SageMaker Debugger built-in rule with TensorFlow](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-debugger/tensorflow_builtin_rule)
+ [Using a SageMaker Debugger built-in rule with Managed Spot Training and MXNet](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-debugger/mxnet_spot_training)
+ [Using a SageMaker Debugger built-in rule with parameter modifications for a real-time training job analysis with XGBoost](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker-debugger/xgboost_realtime_analysis)

While running the example notebooks in SageMaker Studio, you can find the training job trial created on the **Studio Experiment List** tab. For example, as shown in the following screenshot, you can find and open a **Describe Trial Component** window of your current training job. On the Debugger tab, you can check if the Debugger rules, `vanishing_gradient()` and `loss_not_decreasing()`, are monitoring the training session in parallel. For a full instruction of how to find your training job trial components in the Studio UI, see [SageMaker Studio - View Experiments, Trials, and Trial Components](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks.html#studio-tasks-experiments).

![An image of running a training job with Debugger built-in rules activated in SageMaker Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/debugger/debugger-built-in-rule-studio.png)


There are two ways of using the Debugger built-in rules in the SageMaker AI environment: deploy the built-in rules as it is prepared or adjust their parameters as you want. The following topics show you how to use the built-in rules with example codes.

## Debugger built-in rules example code
<a name="debugger-deploy-built-in-rules"></a>

The following code sample shows how to set the Debugger built-in rules using the `Rule.sagemaker` method. To specify built-in rules that you want to run, use the `rules_configs` API operation to call the built-in rules. To find a full list of Debugger built-in rules and default parameter values, see [List of Debugger built-in rules](debugger-built-in-rules.md).

```
import boto3
import sagemaker
from sagemaker.train import ModelTrainer
from sagemaker.core.debugger import Rule, CollectionConfig, rule_configs
from sagemaker.core.helper.session_helper import get_execution_role
built_in_rules=[ 
            Rule.sagemaker(rule_configs.vanishing_gradient()),
            Rule.sagemaker(rule_configs.loss_not_decreasing())
]

from sagemaker.core import image_uris
from sagemaker.train.configs import SourceCode, Compute

training_image = image_uris.retrieve(
    framework="tensorflow",
    region=boto3.Session().region_name,
    version="{{2.9.0}}",
    py_version="{{py39}}",
    instance_type="{{ml.p3.2xlarge}}",
    image_scope="training"
)

# construct a SageMaker AI ModelTrainer with the Debugger built-in rules
sagemaker_model_trainer=ModelTrainer(
    training_image=training_image,
    source_code=SourceCode(entry_script='directory/to/your_training_script.py'),
    role=get_execution_role(),
    base_job_name='debugger-built-in-rules-demo',
    compute=Compute(instance_type="{{ml.p3.2xlarge}}", instance_count=1),

    # debugger-specific arguments below
    rules=built_in_rules
)
sagemaker_model_trainer.train()
```

**Note**  
The Debugger built-in rules run in parallel with your training job. The maximum number of built-in rule containers for a training job is 20. 

For more information about the Debugger rule class, methods, and parameters, see the [SageMaker Debugger Rule class](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html) in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable). 

To find an example of how to adjust the Debugger rule parameters, see the following [Use Debugger built-in rules with parameter modifications](#debugger-deploy-modified-built-in-rules) section.

## Use Debugger built-in rules with parameter modifications
<a name="debugger-deploy-modified-built-in-rules"></a>

The following code example shows the structure of built-in rules to adjust parameters. In this example, the `stalled_training_rule` collects the `losses` tensor collection from a training job at every 50 steps and an evaluation stage at every 10 steps. If the training process starts stalling and not collecting tensor outputs for 120 seconds, the `stalled_training_rule` stops the training job. 

```
import boto3
import time
import sagemaker
from sagemaker.train import ModelTrainer
from sagemaker.core.debugger import Rule, CollectionConfig, rule_configs
from sagemaker.core.helper.session_helper import get_execution_role

# call the built-in rules and modify the CollectionConfig parameters

base_job_name_prefix= 'smdebug-stalled-demo-' + str(int(time.time()))

built_in_rules_modified=[
    Rule.sagemaker(
        base_config=rule_configs.stalled_training_rule(),
        rule_parameters={
                'threshold': '120',
                'training_job_name_prefix': base_job_name_prefix,
                'stop_training_on_fire' : 'True'
        },
        collections_to_save=[ 
            CollectionConfig(
                name="losses", 
                parameters={
                      "train.save_interval": "50",
                      "eval.save_interval": "10"
                } 
            )
        ]
    )
]

from sagemaker.core import image_uris
from sagemaker.train.configs import SourceCode, Compute

training_image = image_uris.retrieve(
    framework="tensorflow",
    region=boto3.Session().region_name,
    version="{{2.9.0}}",
    py_version="{{py39}}",
    instance_type="{{ml.p3.2xlarge}}",
    image_scope="training"
)

# construct a SageMaker AI ModelTrainer with the modified Debugger built-in rule
sagemaker_model_trainer=ModelTrainer(
    training_image=training_image,
    source_code=SourceCode(entry_script='directory/to/your_training_script.py'),
    role=get_execution_role(),
    base_job_name=base_job_name_prefix,
    compute=Compute(instance_type="{{ml.p3.2xlarge}}", instance_count=1),

    # debugger-specific arguments below
    rules=built_in_rules_modified
)
sagemaker_model_trainer.train()
```
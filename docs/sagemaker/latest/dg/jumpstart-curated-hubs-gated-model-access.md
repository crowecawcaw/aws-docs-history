# Restrict access to JumpStart gated models

Amazon SageMaker JumpStart provides access to both publicly available and proprietary foundation models.
There are certain gated models in private Amazon S3 buckets that require you to have accepted the model's
EULA (end user license agreement) in order to access them. For more information, see
[EULA
acceptance with the SageMaker Python SDK](jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula-python-sdk "jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula-python-sdk").

The current default behavior is that if a user accepts a model's EULA, then the user can
access the model and create [fine-tuning training jobs](jumpstart-foundation-models-use-python-sdk-estimator-class.md "jumpstart-foundation-models-use-python-sdk-estimator-class.md"). However, if you're an administrator
and would like to restrict fine-tuning access to these gated models, you can set a policy that
denies permissions to use the `CreateTrainingJob` action whenever the request
is to a gated model.

The following is an example AWS Identity and Access Management (IAM) policy that an administrator can add to a
user's IAM role:

```
{
    "Effect": "Deny",
    "Action": "sagemaker:CreateTrainingJob",
    "Resource": "*",
    "Condition": {
        "Bool": {
            "sagemaker:DirectGatedModelAccess": "true"
        }
    }
}
```

If you want to grant users access to specific models without providing unrestricted
access to the gated models, set up a curated hub and add the specific models to the hub.
For more information, see [Private curated hubs for foundation model access control in JumpStart](jumpstart-curated-hubs.md "jumpstart-curated-hubs.md").

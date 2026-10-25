

# Setting up the access role
<a name="functions-prerequisites-access-role"></a>

A function that invokes a model runs the invocation in your account. Elemental Inference makes the call by assuming the IAM role in the feed's `accessRoleArn` field. This is the same access role that a smart crop output uses to read graphics-compositing templates from Amazon S3. A feed has one access role, shared by every output on that feed, so if the feed already has one, add the Amazon Bedrock permissions to the existing role rather than creating a second role.

**Important**  
Set the access role on the feed at the same time as you add the function output. Elemental Inference rejects a feed that carries a function output with a model target and no access role.

**Note**  
Elemental Inference invokes Amazon Bedrock as the access role in your account, so your account's Amazon Bedrock settings in the feed's Region govern how Amazon Bedrock handles the content that a function sends, including whether prompts and responses are retained. Elemental Inference doesn't send function content to any other AI service. For more information, see [Data retention](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html) in the *Amazon Bedrock User Guide*.

## Permissions policy
<a name="functions-prerequisites-permissions-policy"></a>

Attach a policy that allows `bedrock:InvokeModel` on exactly the models that your functions target.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowInferenceFunctionModelInvocation",
      "Effect": "Allow",
      "Action": "bedrock:InvokeModel",
      "Resource": [
        "arn:aws:bedrock:{{region}}::foundation-model/{{model-id}}",
        "arn:aws:bedrock:{{region}}:{{111122223333}}:inference-profile/{{profile-id}}"
      ]
    }
  ]
}
```

**Note**  
If a function targets a cross-Region inference profile, grant both the inference-profile ARN and the foundation-model ARNs in each of the Regions that the profile spans. This is an Amazon Bedrock requirement. For more information, see [Set up an inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html) in the *Amazon Bedrock User Guide*.

## Trust policy
<a name="functions-prerequisites-trust-policy"></a>

The role must trust the Elemental Inference service principal. Elemental Inference assumes the role with an external ID and with the confused-deputy condition keys set from the feed, so we recommend that you require all three, as follows.


| Condition key | Value that Elemental Inference sends | 
| --- | --- | 
| sts:ExternalId | The fixed string ElementalInference. | 
| aws:SourceAccount | The ID of the account that owns the feed. | 
| aws:SourceArn | The ARN of the feed whose function is running. | 

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "elemental-inference.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "ElementalInference",
          "aws:SourceAccount": "{{111122223333}}"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:elemental-inference:{{region}}:{{111122223333}}:feed/*"
        }
      }
    }
  ]
}
```

To restrict the role to one feed, replace the wildcard in `aws:SourceArn` with the full feed ARN. These condition keys protect against the cross-service confused deputy problem. For more information, see [Cross-service confused deputy prevention](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*.
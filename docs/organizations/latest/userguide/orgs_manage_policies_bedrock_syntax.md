

# Amazon Bedrock policy syntax and examples
<a name="orgs_manage_policies_bedrock_syntax"></a>

An Amazon Bedrock policy is a plaintext file that is structured according to the rules of JSON. The syntax for Amazon Bedrock policies follows the syntax for all declarative policy types. For more information, see [Policy syntax and inheritance for declarative policy types](orgs_manage_policies_inheritance_mgmt.md). This topic focuses on applying that general syntax to the specific requirements of the Amazon Bedrock policy type.

The following Amazon Bedrock policy example shows the basic Amazon Bedrock policy syntax:

```
{
    "bedrock": {
        "guardrail_inference": {
            "us-east-1": {
                "config_1": {
                    "identifier": {
                        "@@assign": "arn:aws:bedrock:us-east-1:123456789012:guardrail/hu1dlsv9wy1d:1"
                    },
                    "selective_content_guarding": {
                        "system": {
                            "@@assign": "selective"
                        },
                        "messages": {
                            "@@assign": "comprehensive"
                        }
                    },
                    "model_enforcement": {
                        "included_models": {
                            "@@assign": ["ALL"]
                        },
                        "excluded_models": {
                            "@@assign": ["amazon.titan-embed-text-v2:0", "cohere.embed-english-v3"]
                        }
                    }
                }
            }
        }
    }
}
```

## The Amazon Bedrock policy syntax includes the following elements
<a name="bedrock-policy-components"></a>

`"bedrock"`  
The top-level key for Amazon Bedrock policy documents.

`"guardrail_inference"`  
Defines guardrail enforcement configuration.

`<region>`  
The region where the policy will be enforced. For example, `"us-east-1"`.

`"config_1"`  
Configuration identifier for the guardrail settings.

`"identifier"` (Required)  
Guardrail ARN, followed by `:version`, the Guardrail version.  
+ The Guardrail must be owned by the Management account. You cannot create a policy using a Guardrail from another account.
+ The Guardrail must have a version, and that version cannot be DRAFT. To create a version of your guardrail, see [Create a version of a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-versions-create.html) in the Amazon Bedrock user guide.
+ The Guardrail must have a Resource Based Policy that allows organization members to call `ApplyGuardrail`.
+ The Guardrail must be created and used in the specified region.

`"selective_content_guarding"` (Optional)  
Amazon Bedrock APIs allow marking specific content within the input that the caller wants guardrails to process. These settings let enforcers control whether or not to respect content tagging decisions made by the caller. When specified, one of `"system"` or `"messages"` is required.

`"system"` (Optional)  
Choose how system prompts will be processed by guardrails. Defaults to `comprehensive` when not specified.  
+ `"comprehensive"`: Evaluate all content regardless of guard content tags.
+ `"selective"`: Only evaluate content within guard content tags. Does not evaluate any content when no tags are specified.

`"messages"` (Optional)  
Choose how message content with user and assistant conversation will be processed by guardrails. Defaults to `comprehensive` when not specified.  
+ `"comprehensive"`: Evaluate all content regardless of guard content tags.
+ `"selective"`: Only evaluate content within guard content tags. Evaluates all content within messages when no tags are specified.

`"model_enforcement"` (Optional)  
Model-specific information for the enforced guardrail configuration. If not present, the configuration is enforced on all models.

`"included_models"` (Required)  
List of models to enforce the guardrail on. When empty, applies enforcement to all models. Also accepts the keyword “ALL” to explicitly include all models.

`"excluded_models"` (Required)  
Models to exclude from enforcement of the guardrail. When empty, does not exclude any models from enforcement. If a model is present in both the included and excluded models lists, it is excluded.
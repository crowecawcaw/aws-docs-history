# Amazon Bedrock policy syntax and

examples

An Amazon Bedrock policy is a plaintext file that is structured according to the rules of JSON. The syntax for Amazon Bedrock policies follows the syntax for all management policy types. For more information, see [Policy syntax and inheritance for management policy types](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md"). This topic focuses on applying that general syntax to the specific requirements of the Amazon Bedrock policy type.

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
                    "input_tags": {
                        "@@assign": "honor"
                    }
                }
            }
        }
    }
}
```

## The Amazon Bedrock policy syntax includes the following elements

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

- The Guardrail must be owned by the Management account. You cannot create a policy using a Guardrail from another account.
- The Guardrail must have a version, and that version cannot be DRAFT. To create a version of your guardrail, see "Creating a Guardrail Version" in the Amazon Bedrock user guide.
- The Guardrail must have a Resource Based Policy that allows organization members to call `ApplyGuardrail`.
- The Guardrail must be created and used in the specified region.

`"input_tags"` (Required)

Specifies how guardrails handle tagged content:

- `"honor"`: If a request contains guardrails-tagged content (see "Content for Guardrails" in the Amazon Bedrock user guide), only guard against content within the input tags.
- `"ignore"`: Guard against all content in the request, even if there are guardrail input tags.

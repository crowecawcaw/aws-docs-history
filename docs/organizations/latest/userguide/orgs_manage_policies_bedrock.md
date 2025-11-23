# Amazon Bedrock policies

Amazon Bedrock policies allow you to enforce safeguards configured in Amazon Bedrock Guardrails automatically across any
element in your organization structure for all model inference calls to Amazon Bedrock. This eliminates the need to configure an individual guardail for each account. Amazon Bedrock Guardrails provides
configurable safeguards to help safely build generative AI applications at scale, with a standard approach for a wide range of foundation models including: models supported in Amazon Bedrock, fine-tuned models, and models hosted outside of Amazon Bedrock.

Amazon Bedrock policies in AWS Organizations allow you to reference a guardrail created in your management account
in a JSON format. You can attach any policy into the required element of your organization structure, such as
the root, organizational units (OUs), and individual accounts. AWS Organizations applies inheritance rules to
combine the policies, which results in an effective policy for each account that dictates how safeguards are enforced for your generative AI application.

This capability is currently
available in preview.

## How it works

Amazon Bedrock policies give you control over automatic enforcement of safeguards within guardrails across
multiple accounts for all model inference calls to Amazon Bedrock. You need to reference a specific version of
the appropriate guardrail within your policy, adhering to your
organization's responsible AI requirements. This is specific to the AWS region where your guardrail
exists, and you need to have different guardrails for each AWS region where you want the enforcement of
safety controls. You can then attach this policy to any node of the organization, and accounts beneath that node will then automatically inherit those safeguards
and apply them for every model invocation to Amazon Bedrock.

Amazon Bedrock policies help you ensure consistent safety controls throughout your organization, and provide a centralized approach to safely build generative AI applications at scale.

# AWS Config Managed Rules

AWS Config provides _AWS managed rules_, which are predefined, customizable
rules that AWS Config uses to evaluate whether your AWS resources comply with common best
practices. For example, you could use a managed rule to quickly start assessing whether
your Amazon Elastic Block Store (Amazon EBS) volumes are encrypted or
whether specific tags are applied to your resources.

The AWS Config console guides you through the process
of configuring and activating a managed rule. You can also use the AWS Command Line Interface or AWS Config API to
pass the JSON code that defines your configuration of a managed rule.

You can customize the behavior of a managed rule to suit your needs. For example, you can
define the rule's scope to constrain which resources trigger an evaluation for the rule,
such as EC2 instances or volumes.

You can customize the rule's parameters to define
attributes that your resources must have to comply with the rule. For example, you can
customize a parameter to specify that your security group should block incoming traffic to a
specific port number.

Before using managed rules, see [Considerations](evaluate-config.md#evaluate-config-considerations "evaluate-config.md#evaluate-config-considerations").

###### Topics

- [List of Managed Rules](managed-rules-by-aws-config.md "managed-rules-by-aws-config.md")
- [List of Managed Rules by Evaluation Mode](managed-rules-by-evaluation-mode.md "managed-rules-by-evaluation-mode.md")
- [List of Managed Rules by Trigger Type](managed-rules-by-trigger-type.md "managed-rules-by-trigger-type.md")
- [List of Managed Rules by Region Availability](managing-rules-by-region-availability.md "managing-rules-by-region-availability.md")
- [Creating Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md")

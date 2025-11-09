# AWS Config Custom Rules

AWS Config Custom Rules are rules that you create from scratch. There are two ways to create
AWS Config custom rules: with Lambda functions ([AWS Lambda Developer Guide](../../../lambda/latest/dg/gettingstarted-concepts.md#gettingstarted-concepts-function "../../../lambda/latest/dg/gettingstarted-concepts.md#gettingstarted-concepts-function")) and with Guard ([Guard GitHub
Repository](https://github.com/aws-cloudformation/cloudformation-guard "https://github.com/aws-cloudformation/cloudformation-guard")), a policy-as-code language.

AWS Config custom rules created with Lambda are called _AWS Config Custom Lambda
Rules_ and AWS Config custom rules created with Guard are called
_AWS Config Custom Policy Rules_.

Before using custom rules, see [Considerations](evaluate-config.md#evaluate-config-considerations "evaluate-config.md#evaluate-config-considerations").

## AWS Config Custom Policy Rules

Rules written using Guard can be created from the AWS Config console or by using
the AWS Config rule APIs. AWS Config Custom Policy rules allow you to create AWS Config Custom rules
without needing to use Java or Python to develop Lambda functions to manage your custom
rules. AWS Config Custom Policy rules are initiated by configuration changes. For more
information about Guard, see the [Guard GitHub
Repository](https://github.com/aws-cloudformation/cloudformation-guard "https://github.com/aws-cloudformation/cloudformation-guard").

## AWS Config Custom Lambda Rules

Custom Lambda rules provide you with the option to use Java or Python to create a
Lambda function for a AWS Config Custom rule. A _Lambda function_ is
custom code that you upload to AWS Lambda, and it is invoked by events that are published
to it by an event source. If the Lambda function is associated with an AWS Config rule, AWS Config
invokes it when the rule is initiated. The Lambda function then evaluates the
configuration information that is sent by AWS Config, and it returns the evaluation results.
For more information about Lambda functions, see [Function and Event Sources](../../../lambda/latest/dg/intro-core-components.md "../../../lambda/latest/dg/intro-core-components.md") in
the _AWS Lambda Developer Guide_.

## Format differences for AWS Config Custom Rules

The following table displays the format differences in the fields for the [ConfigurationItem](../APIReference/API_ConfigurationItem.md "../APIReference/API_ConfigurationItem.md") data type and for AWS Config Custom Rules.

| ConfigurationItem          | AWS Config Custom Rule      |
| -------------------------- | --------------------------- |
| `version`                  | `configurationItemVersion`  |
| `accountId`                | `awsAccountId`              |
| `arn`                      | `ARN`                       |
| `configurationItemMD5Hash` | `configurationStateMd5Hash` |

###### Topics

- [Creating Custom Policy Rules](evaluate-config_develop-rules_cfn-guard.md "evaluate-config_develop-rules_cfn-guard.md")
- [Creating Custom Lambda Rules](evaluate-config_develop-rules_lambda-functions.md "evaluate-config_develop-rules_lambda-functions.md")
- [Managing Deleted Resources for Custom Lambda Rules](evaluate-config_develop-rules-delete.md "evaluate-config_develop-rules-delete.md")

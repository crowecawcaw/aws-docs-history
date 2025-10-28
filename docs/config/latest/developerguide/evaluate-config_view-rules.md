# Viewing Details and Compliance Information for your AWS Config Rules

###### Important

For accurate reporting on the compliance status, you must record the `AWS::Config::ResourceCompliance` resource type.
For more information, see [Recording AWS Resources](select-resources.md "select-resources.md").

You can use the AWS Config console or the AWS SDKs to view your
rules.

###### Topics

- [Using the console](#evaluate-config_view-rules-console "#evaluate-config_view-rules-console")
- [Using the AWS SDKs](#evaluate-config_view-rules-cli "#evaluate-config_view-rules-cli")

## Viewing Rules (Console)

The **Rules** page shows your rules and their current compliance
results in a table. The result for each rule is **Evaluating...**
until AWS Config finishes evaluating your resources against the rule. You can update the
results with the refresh button. When AWS Config finishes evaluations, you can see the
rules and resource types that are compliant or noncompliant. For more information,
see [Viewing Compliance Information and Evaluation Results for your AWS Resources with AWS Config](evaluate-config_view-compliance.md "evaluate-config_view-compliance.md").

###### Note

AWS Config evaluates only the resource types that it is recording. For example, if you add
the **cloudtrail-enabled** rule but don't record the CloudTrail trail
resource type, AWS Config can't evaluate whether the trails in your account are compliant or
noncompliant. For more information, see [Recording AWS Resources with AWS Config](select-resources.md "select-resources.md").

###### To view your rules

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. In the AWS Management Console menu, verify that the region selector is set to a region that
   supports AWS Config rules. For the list of supported regions, see [AWS Config Regions and Endpoints](../../../general/latest/gr/rande.md#awsconfig_region "../../../general/latest/gr/rande.md#awsconfig_region")
   in the _Amazon Web Services General Reference_.
3. In the left navigation, choose **Rules**.
4. The **Rules** page shows
   all the rule that are currently in your AWS account. It lists the name,
   associated remediation action, and compliance status of each rule.
   - Choose **Add rule** to get started with creating a
     rule.
   - Choose a rule to see its settings, or choose a rule and **View
     details**.
   - See the compliance status of the rule when it evaluates your
     resources.
   - Choose a rule and **Edit rule** to change the
     configuration settings of the rule and set a remediation action for a
     noncompliant rule.

## Viewing Rules

(AWS SDKs)

The following code examples show how to use `DescribeConfigRules`.

CLI

**AWS CLI**

**To get details for an AWS Config rule**

The following command returns details for an AWS Config rule named `InstanceTypesAreT2micro`:

```
`aws configservice describe-config-rules --config-rule-names `InstanceTypesAreT2micro``

```

Output:

```
{
    "ConfigRules": [
        {
            "ConfigRuleState": "ACTIVE",
            "Description": "Evaluates whether EC2 instances are the t2.micro type.",
            "ConfigRuleName": "InstanceTypesAreT2micro",
            "ConfigRuleArn": "arn:aws:config:us-east-1:123456789012:config-rule/config-rule-abcdef",
            "Source": {
                "Owner": "CUSTOM_LAMBDA",
                "SourceIdentifier": "arn:aws:lambda:us-east-1:123456789012:function:InstanceTypeCheck",
                "SourceDetails": [
                    {
                        "EventSource": "aws.config",
                        "MessageType": "ConfigurationItemChangeNotification"
                    }
                ]
            },
            "InputParameters": "{\"desiredInstanceType\":\"t2.micro\"}",
            "Scope": {
                "ComplianceResourceTypes": [
                    "AWS::EC2::Instance"
                ]
            },
            "ConfigRuleId": "config-rule-abcdef"
        }
    ]
}
```

- For API details, see
  [DescribeConfigRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-config-rules.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-config-rules.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This sample lists config rules for the account, with selected properties.**

```
Get-CFGConfigRule | Select-Object ConfigRuleName, ConfigRuleId, ConfigRuleArn, ConfigRuleState

```

**Output:**

```
ConfigRuleName                                    ConfigRuleId       ConfigRuleArn                                                        ConfigRuleState
--------------                                    ------------       -------------                                                        ---------------
ALB_REDIRECTION_CHECK                             config-rule-12iyn3 arn:aws:config-service:eu-west-1:123456789012:config-rule/config-rule-12iyn3 ACTIVE
access-keys-rotated                               config-rule-aospfr arn:aws:config-service:eu-west-1:123456789012:config-rule/config-rule-aospfr ACTIVE
autoscaling-group-elb-healthcheck-required        config-rule-cn1f2x arn:aws:config-service:eu-west-1:123456789012:config-rule/config-rule-cn1f2x ACTIVE
```

- For API details, see
  [DescribeConfigRules](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This sample lists config rules for the account, with selected properties.**

```
Get-CFGConfigRule | Select-Object ConfigRuleName, ConfigRuleId, ConfigRuleArn, ConfigRuleState

```

**Output:**

```
ConfigRuleName                                    ConfigRuleId       ConfigRuleArn                                                        ConfigRuleState
--------------                                    ------------       -------------                                                        ---------------
ALB_REDIRECTION_CHECK                             config-rule-12iyn3 arn:aws:config-service:eu-west-1:123456789012:config-rule/config-rule-12iyn3 ACTIVE
access-keys-rotated                               config-rule-aospfr arn:aws:config-service:eu-west-1:123456789012:config-rule/config-rule-aospfr ACTIVE
autoscaling-group-elb-healthcheck-required        config-rule-cn1f2x arn:aws:config-service:eu-west-1:123456789012:config-rule/config-rule-cn1f2x ACTIVE
```

- For API details, see
  [DescribeConfigRules](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/config#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/config#code-examples").

```
class ConfigWrapper:
    """
    Encapsulates AWS Config functions.
    """

    def __init__(self, config_client):
        """
        :param config_client: A Boto3 AWS Config client.
        """
        self.config_client = config_client


    def describe_config_rule(self, rule_name):
        """
        Gets data for the specified rule.

        :param rule_name: The name of the rule to retrieve.
        :return: The rule data.
        """
        try:
            response = self.config_client.describe_config_rules(
                ConfigRuleNames=[rule_name]
            )
            rule = response["ConfigRules"]
            logger.info("Got data for rule %s.", rule_name)
        except ClientError:
            logger.exception("Couldn't get data for rule %s.", rule_name)
            raise
        else:
            return rule



```

- For API details, see
  [DescribeConfigRules](../../../goto/boto3/config-2014-11-12/DescribeConfigRules.md "../../../goto/boto3/config-2014-11-12/DescribeConfigRules.md")
  in _AWS SDK for Python (Boto3) API Reference_.

The following code examples show how to use `DescribeComplianceByConfigRule`.

CLI

**AWS CLI**

**To get compliance information for your AWS Config rules**

The following command returns compliance information for each AWS Config rule that is violated by one or more AWS resources:

```
`aws configservice describe-compliance-by-config-rule --compliance-types `NON_COMPLIANT``

```

In the output, the value for each `CappedCount` attribute indicates how many resources do not comply with the related rule. For example, the following output indicates that 3 resources do not comply with the rule named `InstanceTypesAreT2micro`.

Output:

```
{
    "ComplianceByConfigRules": [
        {
            "Compliance": {
                "ComplianceContributorCount": {
                    "CappedCount": 3,
                    "CapExceeded": false
                },
                "ComplianceType": "NON_COMPLIANT"
            },
            "ConfigRuleName": "InstanceTypesAreT2micro"
        },
        {
            "Compliance": {
                "ComplianceContributorCount": {
                    "CappedCount": 10,
                    "CapExceeded": false
                },
                "ComplianceType": "NON_COMPLIANT"
            },
            "ConfigRuleName": "RequiredTagsForVolumes"
        }
    ]
}
```

- For API details, see
  [DescribeComplianceByConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-compliance-by-config-rule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-compliance-by-config-rule.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example retrieves compliances details for the rule ebs-optimized-instance, for which there is no current evaluation results for the rule, hence it returns INSUFFICIENT_DATA**

```
(Get-CFGComplianceByConfigRule -ConfigRuleName ebs-optimized-instance).Compliance

```

**Output:**

```
ComplianceContributorCount ComplianceType
-------------------------- --------------
                           INSUFFICIENT_DATA
```

**Example 2: This example returns the number of non-compliant resources for the rule ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK.**

```
(Get-CFGComplianceByConfigRule -ConfigRuleName ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK -ComplianceType NON_COMPLIANT).Compliance.ComplianceContributorCount

```

**Output:**

```
CapExceeded CappedCount
----------- -----------
False       2
```

- For API details, see
  [DescribeComplianceByConfigRule](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example retrieves compliances details for the rule ebs-optimized-instance, for which there is no current evaluation results for the rule, hence it returns INSUFFICIENT_DATA**

```
(Get-CFGComplianceByConfigRule -ConfigRuleName ebs-optimized-instance).Compliance

```

**Output:**

```
ComplianceContributorCount ComplianceType
-------------------------- --------------
                           INSUFFICIENT_DATA
```

**Example 2: This example returns the number of non-compliant resources for the rule ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK.**

```
(Get-CFGComplianceByConfigRule -ConfigRuleName ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK -ComplianceType NON_COMPLIANT).Compliance.ComplianceContributorCount

```

**Output:**

```
CapExceeded CappedCount
----------- -----------
False       2
```

- For API details, see
  [DescribeComplianceByConfigRule](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

The following code examples show how to use `GetComplianceSummaryByConfigRule`.

CLI

**AWS CLI**

**To get the compliance summary for your AWS Config rules**

The following command returns the number of rules that are compliant and the number that are noncompliant:

```
`aws configservice get-compliance-summary-by-config-rule`

```

In the output, the value for each `CappedCount` attribute indicates how many rules are compliant or noncompliant.

Output:

```
{
    "ComplianceSummary": {
        "NonCompliantResourceCount": {
            "CappedCount": 3,
            "CapExceeded": false
        },
        "ComplianceSummaryTimestamp": 1452204131.493,
        "CompliantResourceCount": {
            "CappedCount": 2,
            "CapExceeded": false
        }
    }
}
```

- For API details, see
  [GetComplianceSummaryByConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-summary-by-config-rule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-summary-by-config-rule.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This sample returns the number of Config rules that are non-compliant.**

```
Get-CFGComplianceSummaryByConfigRule -Select ComplianceSummary.NonCompliantResourceCount

```

**Output:**

```
CapExceeded CappedCount
----------- -----------
False       9
```

- For API details, see
  [GetComplianceSummaryByConfigRule](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This sample returns the number of Config rules that are non-compliant.**

```
Get-CFGComplianceSummaryByConfigRule -Select ComplianceSummary.NonCompliantResourceCount

```

**Output:**

```
CapExceeded CappedCount
----------- -----------
False       9
```

- For API details, see
  [GetComplianceSummaryByConfigRule](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

The following code examples show how to use `GetComplianceDetailsByConfigRule`.

CLI

**AWS CLI**

**To get the evaluation results for an AWS Config rule**

The following command returns the evaluation results for all of the resources that don't comply with an AWS Config rule named `InstanceTypesAreT2micro`:

```
`aws configservice get-compliance-details-by-config-rule --config-rule-name `InstanceTypesAreT2micro` --compliance-types `NON_COMPLIANT``

```

Output:

```
{
    "EvaluationResults": [
        {
            "EvaluationResultIdentifier": {
                "OrderingTimestamp": 1450314635.065,
                "EvaluationResultQualifier": {
                    "ResourceType": "AWS::EC2::Instance",
                    "ResourceId": "i-1a2b3c4d",
                    "ConfigRuleName": "InstanceTypesAreT2micro"
                }
            },
            "ResultRecordedTime": 1450314645.261,
            "ConfigRuleInvokedTime": 1450314642.948,
            "ComplianceType": "NON_COMPLIANT"
        },
        {
            "EvaluationResultIdentifier": {
                "OrderingTimestamp": 1450314635.065,
                "EvaluationResultQualifier": {
                    "ResourceType": "AWS::EC2::Instance",
                    "ResourceId": "i-2a2b3c4d",
                    "ConfigRuleName": "InstanceTypesAreT2micro"
                }
            },
            "ResultRecordedTime": 1450314645.18,
            "ConfigRuleInvokedTime": 1450314642.902,
            "ComplianceType": "NON_COMPLIANT"
        },
        {
            "EvaluationResultIdentifier": {
                "OrderingTimestamp": 1450314635.065,
                "EvaluationResultQualifier": {
                    "ResourceType": "AWS::EC2::Instance",
                    "ResourceId": "i-3a2b3c4d",
                    "ConfigRuleName": "InstanceTypesAreT2micro"
                }
            },
            "ResultRecordedTime": 1450314643.346,
            "ConfigRuleInvokedTime": 1450314643.124,
            "ComplianceType": "NON_COMPLIANT"
        }
    ]
}
```

- For API details, see
  [GetComplianceDetailsByConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-details-by-config-rule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-details-by-config-rule.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example obtains the evaluation results for the rule access-keys-rotated and returns the output grouped by compliance-type**

```
Get-CFGComplianceDetailsByConfigRule -ConfigRuleName access-keys-rotated | Group-Object ComplianceType

```

**Output:**

```
Count Name                      Group
----- ----                      -----
    2 COMPLIANT                 {Amazon.ConfigService.Model.EvaluationResult, Amazon.ConfigService.Model.EvaluationResult}
    5 NON_COMPLIANT             {Amazon.ConfigService.Model.EvaluationResult, Amazon.ConfigService.Model.EvaluationResult, Amazon.ConfigService.Model.EvaluationRes...
```

**Example 2: This example queries compliance details for the rule access-keys-rotated for COMPLIANT resources.**

```
Get-CFGComplianceDetailsByConfigRule -ConfigRuleName access-keys-rotated -ComplianceType COMPLIANT | ForEach-Object {$_.EvaluationResultIdentifier.EvaluationResultQualifier}

```

**Output:**

```
ConfigRuleName      ResourceId            ResourceType
--------------      ----------            ------------
access-keys-rotated BCAB1CDJ2LITAPVEW3JAH AWS::IAM::User
access-keys-rotated BCAB1CDJ2LITL3EHREM4Q AWS::IAM::User
```

- For API details, see
  [GetComplianceDetailsByConfigRule](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example obtains the evaluation results for the rule access-keys-rotated and returns the output grouped by compliance-type**

```
Get-CFGComplianceDetailsByConfigRule -ConfigRuleName access-keys-rotated | Group-Object ComplianceType

```

**Output:**

```
Count Name                      Group
----- ----                      -----
    2 COMPLIANT                 {Amazon.ConfigService.Model.EvaluationResult, Amazon.ConfigService.Model.EvaluationResult}
    5 NON_COMPLIANT             {Amazon.ConfigService.Model.EvaluationResult, Amazon.ConfigService.Model.EvaluationResult, Amazon.ConfigService.Model.EvaluationRes...
```

**Example 2: This example queries compliance details for the rule access-keys-rotated for COMPLIANT resources.**

```
Get-CFGComplianceDetailsByConfigRule -ConfigRuleName access-keys-rotated -ComplianceType COMPLIANT | ForEach-Object {$_.EvaluationResultIdentifier.EvaluationResultQualifier}

```

**Output:**

```
ConfigRuleName      ResourceId            ResourceType
--------------      ----------            ------------
access-keys-rotated BCAB1CDJ2LITAPVEW3JAH AWS::IAM::User
access-keys-rotated BCAB1CDJ2LITL3EHREM4Q AWS::IAM::User
```

- For API details, see
  [GetComplianceDetailsByConfigRule](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

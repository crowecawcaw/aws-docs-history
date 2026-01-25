# Use `DescribeConfigRules` with an AWS SDK or CLI

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

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cfs#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cfs#code-examples").

```
    DATA(lo_result) = lo_cfs->describeconfigrules(
      it_configrulenames = VALUE /aws1/cl_cfsconfigrulenames_w=>tt_configrulenames(
        ( NEW /aws1/cl_cfsconfigrulenames_w( iv_rule_name ) )
      )
    ).
    ot_cfg_rules = lo_result->get_configrules( ).
    MESSAGE 'Retrieved AWS Config rule data.' TYPE 'I'.


```

- For API details, see
  [DescribeConfigRules](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Config with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

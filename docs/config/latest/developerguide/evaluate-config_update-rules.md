# Updating AWS Config Rules

You can use the AWS Config console or the AWS SDKs to update your
rules.

###### Topics

- [Using the console](#evaluate-config_update-rules-console "#evaluate-config_update-rules-console")
- [Using the AWS SDKs](#evaluate-config_update-rules-cli "#evaluate-config_update-rules-cli")

## Updating Rules (Console)

The **Rules** page shows your rules and their current compliance
results in a table. The result for each rule is **Evaluating...**
until AWS Config finishes evaluating your resources against the rule. You can update the
results with the refresh button. When AWS Config finishes evaluations, you can see the
rules and resource types that are compliant or noncompliant. For more information,
see [Viewing Compliance Information and Evaluation Results for your AWS Resources with AWS Config](evaluate-config_view-compliance.md "evaluate-config_view-compliance.md").

###### To update a rule

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. In the AWS Management Console menu, verify that the region selector is set to a region that
   supports AWS Config rules. For the list of supported regions, see [AWS Config Regions and Endpoints](../../../general/latest/gr/rande.md#awsconfig_region "../../../general/latest/gr/rande.md#awsconfig_region")
   in the _Amazon Web Services General Reference_.
3. In the left navigation, choose **Rules**.
4. Choose a rule and **Edit rule** for the rule that you want to
   update.
5. Modify the settings on the **Edit rule** page to change your
   rule as needed.
6. Choose **Save**.

## Updating Rules

(AWS SDKs)

If you are updating a rule that you added previously,
you can specify the rule by `ConfigRuleName`,
`ConfigRuleId`, or `ConfigRuleArn` in the `ConfigRule` data type that you use in this request.
You use the same `PutConfigRule` command that you use when adding a rule.

The following code examples show how to use `PutConfigRule`.

CLI

**AWS CLI**

**To add an AWS managed Config rule**

The following command provides JSON code to add an AWS managed Config rule:

```
`aws configservice put-config-rule --config-rule `file://RequiredTagsForEC2Instances.json``

```

`RequiredTagsForEC2Instances.json` is a JSON file that contains the rule configuration:

```
{
  "ConfigRuleName": "RequiredTagsForEC2Instances",
  "Description": "Checks whether the CostCenter and Owner tags are applied to EC2 instances.",
  "Scope": {
    "ComplianceResourceTypes": [
      "AWS::EC2::Instance"
    ]
  },
  "Source": {
    "Owner": "AWS",
    "SourceIdentifier": "REQUIRED_TAGS"
  },
  "InputParameters": "{\"tag1Key\":\"CostCenter\",\"tag2Key\":\"Owner\"}"
}
```

For the `ComplianceResourceTypes` attribute, this JSON code limits the scope to resources of the `AWS::EC2::Instance` type, so AWS Config will evaluate only EC2 instances against the rule. Because the rule is a managed rule, the `Owner` attribute is set to `AWS`, and the `SourceIdentifier` attribute is set to the rule identifier, `REQUIRED_TAGS`. For the `InputParameters` attribute, the tag keys that the rule requires, `CostCenter` and `Owner`, are specified.

If the command succeeds, AWS Config returns no output. To verify the rule configuration, run the describe-config-rules command, and specify the rule name.

**To add a customer managed Config rule**

The following command provides JSON code to add a customer managed Config rule:

```
`aws configservice put-config-rule --config-rule `file://InstanceTypesAreT2micro.json``

```

`InstanceTypesAreT2micro.json` is a JSON file that contains the rule configuration:

```
{
  "ConfigRuleName": "InstanceTypesAreT2micro",
  "Description": "Evaluates whether EC2 instances are the t2.micro type.",
  "Scope": {
    "ComplianceResourceTypes": [
      "AWS::EC2::Instance"
    ]
  },
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
  "InputParameters": "{\"desiredInstanceType\":\"t2.micro\"}"
}
```

For the `ComplianceResourceTypes` attribute, this JSON code limits the scope to resources of the `AWS::EC2::Instance` type, so AWS Config will evaluate only EC2 instances against the rule. Because this rule is a customer managed rule, the `Owner` attribute is set to `CUSTOM_LAMBDA`, and the `SourceIdentifier` attribute is set to the ARN of the AWS Lambda function. The `SourceDetails` object is required. The parameters that are specified for the `InputParameters` attribute are passed to the AWS Lambda function when AWS Config invokes it to evaluate resources against the rule.

If the command succeeds, AWS Config returns no output. To verify the rule configuration, run the describe-config-rules command, and specify the rule name.

- For API details, see
  [PutConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-config-rule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-config-rule.html")
  in _AWS CLI Command Reference_.

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


    def put_config_rule(self, rule_name):
        """
        Sets a configuration rule that prohibits making Amazon S3 buckets publicly
        readable.

        :param rule_name: The name to give the rule.
        """
        try:
            self.config_client.put_config_rule(
                ConfigRule={
                    "ConfigRuleName": rule_name,
                    "Description": "S3 Public Read Prohibited Bucket Rule",
                    "Scope": {
                        "ComplianceResourceTypes": [
                            "AWS::S3::Bucket",
                        ],
                    },
                    "Source": {
                        "Owner": "AWS",
                        "SourceIdentifier": "S3_BUCKET_PUBLIC_READ_PROHIBITED",
                    },
                    "InputParameters": "{}",
                    "ConfigRuleState": "ACTIVE",
                }
            )
            logger.info("Created configuration rule %s.", rule_name)
        except ClientError:
            logger.exception("Couldn't create configuration rule %s.", rule_name)
            raise



```

- For API details, see
  [PutConfigRule](../../../goto/boto3/config-2014-11-12/PutConfigRule.md "../../../goto/boto3/config-2014-11-12/PutConfigRule.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cfs#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cfs#code-examples").

```
    " Create a config rule for S3 bucket public read prohibition
    lo_cfs->putconfigrule(
      io_configrule = NEW /aws1/cl_cfsconfigrule(
        iv_configrulename = iv_rule_name
        iv_description = |S3 Public Read Prohibited Bucket Rule|
        io_scope = NEW /aws1/cl_cfsscope(
          it_complianceresourcetypes = VALUE /aws1/cl_cfscplncresrctypes_w=>tt_complianceresourcetypes(
            ( NEW /aws1/cl_cfscplncresrctypes_w( |AWS::S3::Bucket| ) )
          )
        )
        io_source = NEW /aws1/cl_cfssource(
          iv_owner = |AWS|
          iv_sourceidentifier = |S3_BUCKET_PUBLIC_READ_PROHIBITED|
        )
        iv_inputparameters = '{}'
        iv_configrulestate = |ACTIVE|
      )
    ).
    MESSAGE 'Created AWS Config rule.' TYPE 'I'.


```

- For API details, see
  [PutConfigRule](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

# Deleting AWS Config Rules

You can use the AWS Config console or the AWS SDKs to delete your
rules.

###### Topics

- [Considerations](#evaluate-config_delete-rules-considerations "#evaluate-config_delete-rules-considerations")
- [Using the console](#evaluate-config_delete-rules-console "#evaluate-config_delete-rules-console")
- [Using the AWS SDKs](#evaluate-config_delete-rules-cli "#evaluate-config_delete-rules-cli")

## Considerations

**Recommendation: Consider excluding the `AWS::Config::ResourceCompliance` resource type from recording before deleting rules**

Deleting rules creates configuration items (CIs) for `AWS::Config::ResourceCompliance`
that can affect your costs for the configuration recorder. If you are deleting rules which evaluate a large number of resource types,
this can lead to a spike in the number of CIs recorded.

To avoid the associated costs, you can opt to disable recording
for the `AWS::Config::ResourceCompliance` resource type before deleting rules, and re-enable recording after the rules have been deleted.

However, since deleting rules is an asynchronous process, it might take an hour or more to complete. During the time
when recording is disabled for `AWS::Config::ResourceCompliance`, rule evaluations will not be recorded in the associated resource’s history.

## Deleting Rules (Console)

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

###### To delete a rule

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. In the AWS Management Console menu, verify that the region selector is set to a region that
   supports AWS Config rules. For the list of supported regions, see [AWS Config Regions and Endpoints](../../../general/latest/gr/rande.md#awsconfig_region "../../../general/latest/gr/rande.md#awsconfig_region")
   in the _Amazon Web Services General Reference_.
3. In the left navigation, choose **Rules**.
4. Choose a rule from the table that you want to delete.
5. From the **Actions** dropdown list, choose **Delete
   rule**.
6. When prompted, type "Delete" (case-sensitive) and then choose
   **Delete**.

## Deleting Rules

(AWS SDKs)

The following code examples show how to use `DeleteConfigRule`.

CLI

**AWS CLI**

**To delete an AWS Config rule**

The following command deletes an AWS Config rule named `MyConfigRule`:

```
`aws configservice delete-config-rule --config-rule-name `MyConfigRule``

```

- For API details, see
  [DeleteConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-config-rule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-config-rule.html")
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


    def delete_config_rule(self, rule_name):
        """
        Delete the specified rule.

        :param rule_name: The name of the rule to delete.
        """
        try:
            self.config_client.delete_config_rule(ConfigRuleName=rule_name)
            logger.info("Deleted rule %s.", rule_name)
        except ClientError:
            logger.exception("Couldn't delete rule %s.", rule_name)
            raise




```

- For API details, see
  [DeleteConfigRule](../../../goto/boto3/config-2014-11-12/DeleteConfigRule.md "../../../goto/boto3/config-2014-11-12/DeleteConfigRule.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cfs#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/cfs#code-examples").

```
    lo_cfs->deleteconfigrule( iv_rule_name ).
    MESSAGE 'Deleted AWS Config rule.' TYPE 'I'.


```

- For API details, see
  [DeleteConfigRule](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

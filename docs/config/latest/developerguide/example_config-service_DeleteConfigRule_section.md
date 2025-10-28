# Use `DeleteConfigRule` with an AWS SDK or CLI

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

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Config with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

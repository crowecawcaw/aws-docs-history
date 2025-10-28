# Use `RetireGrant` with an AWS SDK or CLI

The following code examples show how to use `RetireGrant`.

CLI

**AWS CLI**

**To retire a grant on a customer master key**

The following `retire-grant` example deletes a grant from a KMS key.

The following example command specifies the `grant-id` and the `key-id` parameters. The value of the `key-id` parameter must be the key ARN of the KMS key.

```
`aws kms retire-grant \
 --grant-id `1234a2345b8a4e350500d432bccf8ecd6506710e1391880c4f7f7140160c9af3` \
 --key-id `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

```

This command produces no output. To confirm that the grant was retired, use the `list-grants` command.

For more information, see [Retiring and revoking grants](grant-manage.md#grant-delete "grant-manage.md#grant-delete") in the _AWS Key Management Service Developer Guide_.

- For API details, see
  [RetireGrant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/retire-grant.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/retire-grant.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kms#code-examples").

```
class GrantManager:
    def __init__(self, kms_client):
        self.kms_client = kms_client

    @classmethod
    def from_client(cls) -> "GrantManager":
        """
        Creates a GrantManager instance with a default KMS client.

        :return: An instance of GrantManager initialized with the default KMS client.
        """
        kms_client = boto3.client("kms")
        return cls(kms_client)


    def retire_grant(self, grant):
        """
        Retires a grant so that it can no longer be used.

        :param grant: The grant to retire.
        """
        try:
            self.kms_client.retire_grant(GrantToken=grant["GrantToken"])
        except ClientError as err:
            logger.error(
                "Couldn't retire grant %s. Here's why: %s",
                grant["GrantId"],
                err.response["Error"]["Message"],
            )
        else:
            print(f"Grant {grant['GrantId']} retired.")



```

- For API details, see
  [RetireGrant](../../../goto/boto3/kms-2014-11-01/RetireGrant.md "../../../goto/boto3/kms-2014-11-01/RetireGrant.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

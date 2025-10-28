# Use `EnableKeyRotation` with an AWS SDK or CLI

The following code examples show how to use `EnableKeyRotation`.

CLI

**AWS CLI**

**To enable automatic rotation of a KMS key**

The following `enable-key-rotation` example enables automatic rotation of a customer managed KMS key with a rotation period of 180 days. The KMS key will be rotated one year (approximate 365 days) from the date that this command completes and every year thereafter.

The `--key-id` parameter identifies the KMS key. This example uses a key ARN value, but you can use either the key ID or the ARN of the KMS key.The `--rotation-period-in-days` parameter specifies the number of days between each rotation date. Specify a value between 90 and 2560 days. If no value is specified, the default value is 365 days.

```
`aws kms enable-key-rotation \
 --key-id `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab` \
 --rotation-period-in-days `180``

```

This command produces no output. To verify that the KMS key is enabled, use the `get-key-rotation-status` command.

For more information, see [Rotating keys](rotate-keys.md "rotate-keys.md") in the _AWS Key Management Service Developer Guide_.

- For API details, see
  [EnableKeyRotation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/enable-key-rotation.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/enable-key-rotation.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kms#code-examples").

```
class KeyManager:
    def __init__(self, kms_client):
        self.kms_client = kms_client
        self.created_keys = []

    @classmethod
    def from_client(cls) -> "KeyManager":
        """
        Creates a KeyManager instance with a default KMS client.

        :return: An instance of KeyManager initialized with the default KMS client.
        """
        kms_client = boto3.client("kms")
        return cls(kms_client)


    def enable_key_rotation(self, key_id: str) -> None:
        """
        Enables rotation for a key.

        :param key_id: The ARN or ID of the key to enable rotation for.
        """
        try:
            self.kms_client.enable_key_rotation(KeyId=key_id)
        except ClientError as err:
            logging.error(
                "Couldn't enable rotation for key '%s'. Here's why: %s",
                key_id,
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [EnableKeyRotation](../../../goto/boto3/kms-2014-11-01/EnableKeyRotation.md "../../../goto/boto3/kms-2014-11-01/EnableKeyRotation.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

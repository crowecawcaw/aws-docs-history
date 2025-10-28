# Use `GetKeyPolicy` with an AWS SDK or CLI

The following code examples show how to use `GetKeyPolicy`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](example_kms_Scenario_Basics_section.md "example_kms_Scenario_Basics_section.md")

CLI

**AWS CLI**

**To copy a key policy from one KMS key to another KMS key**

The following `get-key-policy` example gets the key policy from one KMS key and saves it in a text file. Then, it replaces the policy of a different KMS key using the text file as the policy input.

Because the `--policy` parameter of `put-key-policy` requires a string, you must use the `--output text` option to return the output as a text string instead of JSON.

```
`aws kms get-key-policy \
 --policy-name `default` \
 --key-id `1234abcd-12ab-34cd-56ef-1234567890ab` \
 --query `Policy` \
 --output `text` `>` `policy.txt`

`aws` `kms` `put-key-policy` \
 --policy-name `default` \
 --key-id `0987dcba-09fe-87dc-65ba-ab0987654321` \
 --policy `file://policy.txt``

```

This command produces no output.

For more information, see [PutKeyPolicy](../APIReference/API_PutKeyPolicy.md "../APIReference/API_PutKeyPolicy.md") in the _AWS KMS API Reference_.

- For API details, see
  [GetKeyPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-key-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-key-policy.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kms#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kms#code-examples").

```
class KeyPolicy:
    def __init__(self, kms_client):
        self.kms_client = kms_client

    @classmethod
    def from_client(cls) -> "KeyPolicy":
        """
        Creates a KeyPolicy instance with a default KMS client.

        :return: An instance of KeyPolicy initialized with the default KMS client.
        """
        kms_client = boto3.client("kms")
        return cls(kms_client)


    def get_policy(self, key_id: str) -> dict[str, str]:
        """
        Gets the policy of a key.

        :param key_id: The ARN or ID of the key to query.
        :return: The key policy as a dict.
        """
        if key_id != "":
            try:
                response = self.kms_client.get_key_policy(
                    KeyId=key_id,
                )
                policy = json.loads(response["Policy"])
            except ClientError as err:
                logger.error(
                    "Couldn't get policy for key %s. Here's why: %s",
                    key_id,
                    err.response["Error"]["Message"],
                )
                raise
            else:
                pprint(policy)
                return policy
        else:
            print("Skipping get policy demo.")



```

- For API details, see
  [GetKeyPolicy](../../../goto/boto3/kms-2014-11-01/GetKeyPolicy.md "../../../goto/boto3/kms-2014-11-01/GetKeyPolicy.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

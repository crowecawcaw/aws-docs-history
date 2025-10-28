# Use `UntagResource` with an AWS SDK or CLI

The following code examples show how to use `UntagResource`.

CLI

**AWS CLI**

**To remove tags from a data store.**

The following `untag-resource` example shows how to remove tags from a data store.

```
`aws healthlake untag-resource \
 --resource-arn `"arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/b91723d65c6fdeb1d26543a49d2ed1fa"` \
 --tag-keys '`["key1"]`'`

```

This command produces no output.

- For API details, see
  [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/untag-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/untag-resource.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)


    def untag_resource(self, resource_arn: str, tag_keys: list[str]) -> None:
        """
        Untags a HealthLake resource.
        :param resource_arn: The resource ARN.
        :param tag_keys: The tag keys to remove from the resource.
        """
        try:
            self.health_lake_client.untag_resource(
                ResourceARN=resource_arn, TagKeys=tag_keys
            )
        except ClientError as err:
            logger.exception(
                "Couldn't untag resource %s. Here's why %s",
                resource_arn,
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [UntagResource](../../../goto/boto3/healthlake-2017-07-01/UntagResource.md "../../../goto/boto3/healthlake-2017-07-01/UntagResource.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples").

For a complete list of AWS SDK developer guides and code examples, see
[Using HealthLake with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

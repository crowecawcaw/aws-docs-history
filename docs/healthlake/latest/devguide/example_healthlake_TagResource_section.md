# Use `TagResource` with an AWS SDK or CLI

The following code examples show how to use `TagResource`.

CLI

**AWS CLI**

**To add a tag to data store**

The following `tag-resource` example shows how to add a tag to a data store.

```
`aws healthlake tag-resource \
 --resource-arn `"arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/0725c83f4307f263e16fd56b6d8ebdbe"` \
 --tags '`[{"Key": "key1", "Value": "value1"}]`'`

```

This command produces no output.

- For API details, see
  [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/tag-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/tag-resource.html")
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


    def tag_resource(self, resource_arn: str, tags: list[dict[str, str]]) -> None:
        """
        Tags a HealthLake resource.
        :param resource_arn: The resource ARN.
        :param tags: The tags to add to the resource.
        """
        try:
            self.health_lake_client.tag_resource(ResourceARN=resource_arn, Tags=tags)
        except ClientError as err:
            logger.exception(
                "Couldn't tag resource %s. Here's why %s",
                resource_arn,
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [TagResource](../../../goto/boto3/healthlake-2017-07-01/TagResource.md "../../../goto/boto3/healthlake-2017-07-01/TagResource.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples").

For a complete list of AWS SDK developer guides and code examples, see
[Using HealthLake with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

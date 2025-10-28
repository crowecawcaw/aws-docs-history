# Tagging HealthLake data stores

You can assign metadata to HealthLake data stores in the form of tags. Each tag is a label
consisting of a user-defined key and value. Tags help you manage, identify, organize, search
for, and filter data stores.

###### Important

Do not store protected health information (PHI), personally identifiable information (PII), or other confidential or sensitive information in tags.
Tags are not intended to be used for private or sensitive data.

The following topics describe how to use HealthLake tagging operations using the AWS Management Console,
AWS CLI, and AWS SDKs. For more information, see [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") in the
_AWS General Reference Guide_.

###### Topics

- [Tagging a HealthLake data store](#tagresource "#tagresource")
- [Listing tags for a HealthLake data
  store](#listtagsforresource "#listtagsforresource")
- [Untagging a HealthLake data
  store](#untagresource "#untagresource")

## Tagging a HealthLake data store

Use `TagResource` to tag a HealthLake data store. The following menus provide a
procedure for the AWS Management Console and code examples for the AWS CLI and AWS SDKs. For more
information, see [`TagResource`](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") in the _AWS HealthLake API Reference_.

###### To tag a HealthLake data store

Choose a menu based on your access preference to AWS HealthLake.

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

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.

1. Sign in to the [Data stores](https://console.aws.amazon.com/healthlake/home#/list-datastores "https://console.aws.amazon.com/healthlake/home#/list-datastores") page on the HealthLake Console.
2. Choose a data store.

The **Data store details** page opens. 3. Under the **Tags** section, choose **Manage
tags**.

The **Manage tags** page opens. 4. Choose **Add new tag**. 5. Enter a **Key** and **Value** (optional). 6. Choose **Save**.

## Listing tags for a HealthLake data

store

Use `ListTagsForResource` to list tags for a HealthLake data store. The following
menus provide a procedure for the AWS Management Console and code examples for the AWS CLI and AWS SDKs.
For more information, see [`ListTagsForResource`](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") in the _AWS HealthLake API
Reference_.

###### To list tags for a HealthLake data store

Choose a menu based on your access preference to AWS HealthLake.

CLI

**AWS CLI**

**To list tags for a data store**

The following `list-tags-for-resource` example lists the tags associated with the specified data store.:

```
`aws healthlake list-tags-for-resource \
 --resource-arn `"arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/0725c83f4307f263e16fd56b6d8ebdbe"``

```

Output:

```
{
    "tags": {
        "key": "value",
        "key1": "value1"
    }
}
```

- For API details, see
  [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/list-tags-for-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/list-tags-for-resource.html")
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


    def list_tags_for_resource(self, resource_arn: str) -> dict[str, str]:
        """
        Lists the tags for a HealthLake resource.
        :param resource_arn: The resource ARN.
        :return: The tags for the resource.
        """
        try:
            response = self.health_lake_client.list_tags_for_resource(
                ResourceARN=resource_arn
            )
            return response["Tags"]
        except ClientError as err:
            logger.exception(
                "Couldn't list tags for resource %s. Here's why %s",
                resource_arn,
                err.response["Error"]["Message"],
            )
            raise



```

- For API details, see
  [ListTagsForResource](../../../goto/boto3/healthlake-2017-07-01/ListTagsForResource.md "../../../goto/boto3/healthlake-2017-07-01/ListTagsForResource.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples").

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.

1. Sign in to the [Data stores](https://console.aws.amazon.com/healthlake/home#/list-datastores "https://console.aws.amazon.com/healthlake/home#/list-datastores") page on the HealthLake Console.
2. Choose a data store.

The **Data store details** page opens. Under the
**Tags** section, all data store tags are listed.

## Untagging a HealthLake data

store

Use `UntagResource` to remove a tag from a HealthLake data store. The following
menus provide a procedure for the AWS Management Console and code examples for the AWS CLI and AWS SDKs.
For more information, see [`UntagResource`](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") in the _AWS HealthLake API
Reference_.

###### To untag a HealthLake data store

Choose a menu based on your access preference to AWS HealthLake.

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

###### Example availability

Can't find what you need? Request a code example using the **Provide
feedback** link on the right sidebar of this page.

1. Sign in to the [Data stores](https://console.aws.amazon.com/healthlake/home#/list-datastores "https://console.aws.amazon.com/healthlake/home#/list-datastores") page on the HealthLake Console.
2. Choose a data store.

The **Data store details** page opens. 3. Under the **Tags** section, choose **Manage tags**.

The **Manage tags** page opens. 4. Choose **Remove** next to the tag you want to remove. 5. Choose **Save**.

# Tagging a model

You can identify, organize, search for, and filter your Amazon Rekognition models by using
tags. Each tag is a label consisting of a user-defined key and value. For example, to
help determine billing for your models, tag your models with a `Cost center`
key and add the appropriate cost center number as a value. For more information, see
[Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md").

Use tags to:

- Track billing for a model by using cost allocation tags. For more information,
  see [Using Cost Allocation
  Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md").
- Control access to a model by using Identity and Access Management (IAM). For
  more information, see [Controlling access to AWS
  resources using resource tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").
- Automate model management. For example, you can run automated start or stop
  scripts that turn off development models during non-business hours to reduce
  costs. For more information, see [Running a trained Amazon Rekognition Custom Labels model](running-model.md "running-model.md").
  You can tag models by using the Amazon Rekognition console or by using the AWS SDKs.

###### Topics

- [Tagging models (console)](#tm-tagging-model-console "#tm-tagging-model-console")
- [Viewing model tags](#tm-tagging-model-viewing-console "#tm-tagging-model-viewing-console")
- [Tagging models (SDK)](#tm-tagging-model-sdk "#tm-tagging-model-sdk")

## Tagging models (console)

You can use the Rekognition console to add tags to models, view the tags attached to a
model, and remove tags.

### Adding or removing

tags

This procedure explains how to add tags to, or remove tags from, an existing
model. You can also add tags to a new model when it is trained. For more
information, see [Training an Amazon Rekognition Custom Labels model](training-model.md "training-model.md").

###### To add tags to, or remove tags from, an existing model using the

console

1. Open the Amazon Rekognition console at [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ " https://console.aws.amazon.com/rekognition/").
2. Choose **Get started**.
3. In the navigation pane, choose **Projects**.
4. On the **Projects** resources page, choose the
   project that contains the model that you want to tag.
5. In the navigation pane, under the project you previously chose, choose
   **Models**.
6. In the **Models** section, choose the model that you
   want to add a tag to.
7. On the model's details page, choose the **Tags** tab.
8. In the **Tags** section, choose **Manage
   tags**.
9. On the **Manage tags** page, choose **Add new
   tag**.
10. Enter a key and a value.
    1. For **Key**, enter a name for the key.
    2. For **Value**, enter a value.

11. To add more tags, repeat steps 9 and 10.
12. (Optional) To remove a tag, choose **Remove** next to
    the tag that you want to remove. If you are removing a previously saved
    tag, it is removed when you save your changes.
13. Choose **Save changes** to save your changes.

## Viewing model tags

You can use the Amazon Rekognition console to view the tags attached to a model.

To view the tags attached to _all models within a
project_, you must use the AWS SDK. For more information, see [Listing model tags](#listing-model-tags-sdk "#listing-model-tags-sdk").

###### To view the tags attached to a model

1. Open the Amazon Rekognition console at [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ " https://console.aws.amazon.com/rekognition/").
2. Choose **Get started**.
3. In the navigation pane, choose **Projects**.
4. On the **Projects** resources page, choose the project
   that contains the model whose tag you want to view.
5. In the navigation pane, under the project you previously chose, choose
   **Models**.
6. In the **Models** section, choose the model whose tag you
   want to view.
7. On the model's details page, choose the **Tags** tab. The
   tags are shown in **Tags** section.

## Tagging models (SDK)

You can use the AWS SDK to:

- Add tags to a new model
- Add tags to an existing model
- List the tags attached to a model
- Remove tags from a model

The tags in the following AWS CLI examples are in the following format.

```
--tags '{"`key1`":"`value1`","`key2`":"`value2`"}'

```

Alternatively, you can use this format.

```
--tags `key1`=`value1`,`key2`=`value2`
```

If you haven't installed the AWS CLI, see [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").

### Adding tags to a new model

You can add tags to a model when you create it using the [CreateProjectVersion](../APIReference/API_CreateProjectVersion.md "../APIReference/API_CreateProjectVersion.md") operation. Specify one or more tags in the
`Tags` array input parameter.

```
aws rekognition create-project-version --project-arn `project arn` \
  --version-name `version_name` \
  --output-config '{ "S3Location": { "Bucket": "`output bucket`", "Prefix":  "`output folder`" } }' \
  --tags '{"`key1`":"`value1`","`key2`":"`value2`"}' \
  --profile custom-labels-access
```

For information about creating and training a model, see [Training a model (SDK)](training-model.md#tm-sdk "training-model.md#tm-sdk").

### Adding tags to an existing model

To add one or more tags to an existing model, use the [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") operation. Specify the model's Amazon Resource Name
(ARN) (`ResourceArn`) and the tags (`Tags`) that you want
to add. The following example shows how to add two tags.

```
aws rekognition tag-resource --resource-arn `resource-arn` \
  --tags '{"`key1`":"`value1`","`key2`":"`value2`"}' \
  --profile custom-labels-access
```

You can get the ARN for a model by calling [CreateProjectVersion](../APIReference/API_CreateProjectVersion.md "../APIReference/API_CreateProjectVersion.md").

### Listing model tags

To list the tags attached to a model, use the [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") operation and specify the ARN of the model
(`ResourceArn`). The response is a map of tag keys and values
that are attached to the specified model.

```
aws rekognition list-tags-for-resource --resource-arn `resource-arn` \
  --profile custom-labels-access
```

The output displays a list of the tags attached to the model.

```
{
    "Tags": {
        "Dept": "Engineering",
        "Name": "Ana Silva Carolina",
        "Role": "Developer"
    }
}
```

To see which models in a project have a specific tag, call
`DescribeProjectVersions` to get a list of models. Then call
`ListTagsForResource` for each model in the response from
`DescribeProjectVersions`. Inspect the response from
`ListTagsForResource` to see if the required tag is present.

The following Python 3 example shows you how search all your projects for a
specific tag key and value. The output includes the project ARN and the model
ARN where a matching key is found.

###### To search for a tag value

1. Save the following code to a file named
   `find_tag.py`.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Purpose
Shows how to find a tag value that's associated with models within
your Amazon Rekognition Custom Labels projects.
"""
import logging
import argparse
import boto3

from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)


def find_tag_in_projects(rekognition_client, key, value):
    """
    Finds Amazon Rekognition Custom Label models tagged with the supplied key and key value.
    :param rekognition_client: An Amazon Rekognition boto3 client.
    :param key: The tag key to find.
    :param value: The value of the tag that you want to find.
    return: A list of matching model versions (and model projects) that were found.
    """
    try:

        found_tags = []
        found = False

        projects = rekognition_client.describe_projects()
        # Iterate through each project and models within a project.
        for project in projects["ProjectDescriptions"]:
            logger.info("Searching project: %s ...", project["ProjectArn"])

            models = rekognition_client.describe_project_versions(
                ProjectArn=(project["ProjectArn"])
            )

            for model in models["ProjectVersionDescriptions"]:
                logger.info("Searching model %s", model["ProjectVersionArn"])

                tags = rekognition_client.list_tags_for_resource(
                    ResourceArn=model["ProjectVersionArn"]
                )

                logger.info(
                    "\tSearching model: %s for tag: %s value: %s.",
                    model["ProjectVersionArn"],
                    key,
                    value,
                )
                # Check if tag exists.

                if key in tags["Tags"]:
                    if tags["Tags"][key] == value:
                        found = True
                        logger.info(
                            "\t\tMATCH: Project: %s: model version %s",
                            project["ProjectArn"],
                            model["ProjectVersionArn"],
                        )
                        found_tags.append(
                            {
                                "Project": project["ProjectArn"],
                                "ModelVersion": model["ProjectVersionArn"],
                            }
                        )

        if found is False:
            logger.info("No match for Tag %s with value %s.", key, value)
        return found_tags
    except ClientError as err:
        logger.info("Problem finding tags: %s. ", format(err))
        raise


def main():
    """
    Entry point for example.
    """
    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    # Set up command line arguments.
    parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)

    parser.add_argument("tag", help="The tag that you want to find.")
    parser.add_argument("value", help="The tag value that you want to find.")

    args = parser.parse_args()
    key = args.tag
    value = args.value

    print(f"Searching your models for tag: {key} with value: {value}.")


    session = boto3.Session(profile_name='custom-labels-access')
    rekognition_client = session.client("rekognition")

    # Get tagged models for all projects.
    tagged_models = find_tag_in_projects(rekognition_client, key, value)

    print("Matched models\n--------------")
    if len(tagged_models) > 0:
        for model in tagged_models:
            print(
                "Project: {project}\nModel version: {version}\n".format(
                    project=model["Project"], version=model["ModelVersion"]
                )
            )

    else:
        print("No matches found.")

    print("Done.")


if __name__ == "__main__":
    main()

```

2. At the command prompt, enter the following. Replace
   `key` and `value`
   with the key name and the key value that you want to find.

```
python find_tag.py `key` `value`
```

### Deleting tags from a model

To remove one or more tags from a model, use the [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") operation. Specify the ARN of the model
(`ResourceArn`) and the tag keys (`Tag-Keys`) that you
want to remove.

```
aws rekognition untag-resource --resource-arn `resource-arn` \
  --tag-keys '["`key1`","`key2`"]' \
  --profile custom-labels-access
```

Alternatively, you can specify `tag-keys` in this format.

```
--tag-keys `key1`,`key2`
```

# Configuring Amazon SNS topic tags

This topic explains how to configure tags for an [Amazon SNS
topic](sns-tags.md "sns-tags.md") using the AWS Management Console, an AWS SDK, or the AWS CLI.

###### Important

Do not add personally identifiable information (PII) or other confidential or
sensitive information in tags. Tags are accessible to other Amazon Web Services, including
billing. Tags are not intended to be used for private or sensitive data.

## Listing, adding, and

removing tags for an Amazon SNS topic using the AWS Management Console

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. On the navigation panel, choose **Topics**.
3. On the **Topics** page, choose a topic and then choose
   **Edit**.
4. Expand the **Tags** section.

The tags added to the topic are listed. 5. Modify topic tags:

    * To add a tag, choose **Add tag** and enter a
     **Key** and **Value**
     (optional).
    * To remove a tag, choose **Remove tag** next to a
     key-value pair.

6. Choose **Save changes**.

## Adding tags to a topic using an AWS

SDK

To use an AWS SDK, you must configure it with your credentials. For more
information, see [The shared config and credentials
files](../../../sdkref/latest/guide/creds-config-files.md "../../../sdkref/latest/guide/creds-config-files.md") in the _AWS SDKs and Tools Reference Guide_.

The following code examples show how to use `TagResource`.

CLI

**AWS CLI**

**To add a tag to a topic**

The following `tag-resource` example adds a metadata tag to the specified Amazon SNS topic.

```
`aws sns tag-resource \
 --resource-arn `arn:aws:sns:us-west-2:123456789012:MyTopic` \
 --tags `Key=Team,Value=Alpha``

```

This command produces no output.

- For API details, see
  [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/tag-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/tag-resource.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.SnsException;
import software.amazon.awssdk.services.sns.model.Tag;
import software.amazon.awssdk.services.sns.model.TagResourceRequest;
import java.util.ArrayList;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class AddTags {
    public static void main(String[] args) {
        final String usage = """

                Usage:    <topicArn>

                Where:
                   topicArn - The ARN of the topic to which tags are added.

                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String topicArn = args[0];
        SnsClient snsClient = SnsClient.builder()
                .region(Region.US_EAST_1)
                .build();

        addTopicTags(snsClient, topicArn);
        snsClient.close();
    }

    public static void addTopicTags(SnsClient snsClient, String topicArn) {
        try {
            Tag tag = Tag.builder()
                    .key("Team")
                    .value("Development")
                    .build();

            Tag tag2 = Tag.builder()
                    .key("Environment")
                    .value("Gamma")
                    .build();

            List<Tag> tagList = new ArrayList<>();
            tagList.add(tag);
            tagList.add(tag2);

            TagResourceRequest tagResourceRequest = TagResourceRequest.builder()
                    .resourceArn(topicArn)
                    .tags(tagList)
                    .build();

            snsClient.tagResource(tagResourceRequest);
            System.out.println("Tags have been added to " + topicArn);

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [TagResource](../../../goto/SdkForJavaV2/sns-2010-03-31/TagResource.md "../../../goto/SdkForJavaV2/sns-2010-03-31/TagResource.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples").

```
suspend fun addTopicTags(topicArn: String) {
    val tag =
        Tag {
            key = "Team"
            value = "Development"
        }

    val tag2 =
        Tag {
            key = "Environment"
            value = "Gamma"
        }

    val tagList = mutableListOf<Tag>()
    tagList.add(tag)
    tagList.add(tag2)

    val request =
        TagResourceRequest {
            resourceArn = topicArn
            tags = tagList
        }

    SnsClient.fromEnvironment { region = "us-east-1" }.use { snsClient ->
        snsClient.tagResource(request)
        println("Tags have been added to $topicArn")
    }
}


```

- For API details, see
  [TagResource](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

## Managing tags with Amazon SNS API

actions

To manage tags using the Amazon SNS API, use the following API actions:

- [`ListTagsForResource`](../api/API_ListTagsForResource.md "../api/API_ListTagsForResource.md")
- [`TagResource`](../api/API_TagResource.md "../api/API_TagResource.md")
- [`UntagResource`](../api/API_UntagResource.md "../api/API_UntagResource.md")

## API actions that support ABAC

The following is a list of API actions that support attribute-based access control
(ABAC). For more details about ABAC, see [What is
ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

- [`AddPermission`](../api/API_AddPermission.md "../api/API_AddPermission.md")
- [`ConfirmSubscription`](../api/API_ConfirmSubscription.md "../api/API_ConfirmSubscription.md")
- [`DeleteTopic`](../api/API_DeleteTopic.md "../api/API_DeleteTopic.md")
- [`GetDataProtectionPolicy`](../api/API_GetDataProtectionPolicy.md "../api/API_GetDataProtectionPolicy.md")
- [`GetSubscriptionAttributes`](../api/API_GetSubscriptionAttributes.md "../api/API_GetSubscriptionAttributes.md")
- [`GetTopicAttributes`](../api/API_GetTopicAttributes.md "../api/API_GetTopicAttributes.md")
- [`ListSubscriptionsByTopic`](../api/API_ListSubscriptionsByTopic.md "../api/API_ListSubscriptionsByTopic.md")
- [`ListTagsForResource`](../api/API_ListTagsForResource.md "../api/API_ListTagsForResource.md")
- [`Publish`](../api/API_Publish.md "../api/API_Publish.md")
- [`PublishBatch`](../api/API_PublishBatch.md "../api/API_PublishBatch.md")
- [`PutDataProtectionPolicy`](../api/API_PutDataProtectionPolicy.md "../api/API_PutDataProtectionPolicy.md")
- [`RemovePermission`](../api/API_RemovePermission.md "../api/API_RemovePermission.md")
- [`SetSubscriptionAttributes`](../api/API_SetSubscriptionAttributes.md "../api/API_SetSubscriptionAttributes.md")
- [`SetTopicAttributes`](../api/API_SetTopicAttributes.md "../api/API_SetTopicAttributes.md")
- [`Subscribe`](../api/API_Subscribe.md "../api/API_Subscribe.md")
- [`TagResource`](../api/API_TagResource.md "../api/API_TagResource.md")
- [`Unsubscribe`](../api/API_Unsubscribe.md "../api/API_Unsubscribe.md")
- [`UntagResource`](../api/API_UntagResource.md "../api/API_UntagResource.md")

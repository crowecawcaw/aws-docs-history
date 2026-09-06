

# Configuring Amazon SNS topic tags
<a name="sns-tags-configuring"></a>

This topic explains how to configure tags for an [Amazon SNS topic](sns-tags.md) using the AWS Management Console, an AWS SDK, or the AWS CLI.

**Important**  
Do not add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to other Amazon Web Services, including billing. Tags are not intended to be used for private or sensitive data.

## Listing, adding, and removing tags for an Amazon SNS topic using the AWS Management Console
<a name="list-add-update-remove-tags-for-topic-aws-console"></a>

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home).

1. On the navigation panel, choose **Topics**.

1. On the **Topics** page, choose a topic and then choose **Edit**.

1. Expand the **Tags** section.

   The tags added to the topic are listed.

1. Modify topic tags:
   + To add a tag, choose **Add tag** and enter a **Key** and **Value** (optional).
   + To remove a tag, choose **Remove tag** next to a key-value pair.

1. Choose **Save changes**.

## Adding tags to a topic using an AWS SDK
<a name="tag-resource-aws-sdks"></a>

To use an AWS SDK, you must configure it with your credentials. For more information, see [The shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/creds-config-files.html) in the *AWS SDKs and Tools Reference Guide*.

The following code examples show how to use `TagResource`.

------
#### [ CLI ]

**AWS CLI**  
**To add a tag to a topic**  
The following `tag-resource` example adds a metadata tag to the specified Amazon SNS topic.  

```
aws sns tag-resource \
    --resource-arn {{arn:aws:sns:us-west-2:123456789012:MyTopic}} \
    --tags {{Key=Team,Value=Alpha}}
```
This command produces no output.  
+  For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/tag-resource.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#code-examples). 

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
+  For API details, see [TagResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/TagResource) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples). 

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
+  For API details, see [TagResource](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------

## Managing tags with Amazon SNS API actions
<a name="manage-tags-with-sns-api-actions"></a>

To manage tags using the Amazon SNS API, use the following API actions:
+ [`ListTagsForResource`](https://docs.aws.amazon.com/sns/latest/api/API_ListTagsForResource.html)
+ [`TagResource`](https://docs.aws.amazon.com/sns/latest/api/API_TagResource.html)
+ [`UntagResource`](https://docs.aws.amazon.com/sns/latest/api/API_UntagResource.html)

## API actions that support ABAC
<a name="api-actions-that-support-abac"></a>

The following is a list of API actions that support attribute-based access control (ABAC). For more details about ABAC, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.
+ [`AddPermission`](https://docs.aws.amazon.com/sns/latest/api/API_AddPermission.html)
+ [`ConfirmSubscription`](https://docs.aws.amazon.com/sns/latest/api/API_ConfirmSubscription.html)
+ [`DeleteTopic`](https://docs.aws.amazon.com/sns/latest/api/API_DeleteTopic.html)
+ [`GetDataProtectionPolicy`](https://docs.aws.amazon.com/sns/latest/api/API_GetDataProtectionPolicy.html)
+ [`GetSubscriptionAttributes`](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)
+ [`GetTopicAttributes`](https://docs.aws.amazon.com/sns/latest/api/API_GetTopicAttributes.html)
+ [`ListSubscriptionsByTopic`](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptionsByTopic.html)
+ [`ListTagsForResource`](https://docs.aws.amazon.com/sns/latest/api/API_ListTagsForResource.html)
+ [`Publish`](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html)
+ [`PublishBatch`](https://docs.aws.amazon.com/sns/latest/api/API_PublishBatch.html)
+ [`PutDataProtectionPolicy`](https://docs.aws.amazon.com/sns/latest/api/API_PutDataProtectionPolicy.html)
+ [`RemovePermission`](https://docs.aws.amazon.com/sns/latest/api/API_RemovePermission.html)
+ [`SetSubscriptionAttributes`](https://docs.aws.amazon.com/sns/latest/api/API_SetSubscriptionAttributes.html)
+ [`SetTopicAttributes`](https://docs.aws.amazon.com/sns/latest/api/API_SetTopicAttributes.html)
+ [`Subscribe`](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)
+ [`TagResource`](https://docs.aws.amazon.com/sns/latest/api/API_TagResource.html)
+ [`Unsubscribe`](https://docs.aws.amazon.com/sns/latest/api/API_Unsubscribe.html)
+ [`UntagResource`](https://docs.aws.amazon.com/sns/latest/api/API_UntagResource.html)
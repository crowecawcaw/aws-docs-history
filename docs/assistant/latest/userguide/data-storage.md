

# Data storage in the AWS assistant
<a name="data-storage"></a>

The AWS assistant stores your questions, its responses, and additional context, such as console metadata, to generate responses to your questions and requests. For information about how data is encrypted, see [Data protection in the AWS assistant](data-protection.md). For information about how AWS may use some questions that you ask the AWS assistant and its responses to improve our services, see [Service improvement for the AWS assistant](service-improvement.md).

## AWS Regions where content is processed and stored
<a name="aws-regions-processing-storage"></a>

If you're an AWS IAM Identity Center workforce user, at the Amazon Q Developer Pro tier, your content is stored in the AWS Region where your Amazon Q Developer profile was created only for the following features:
+ Chatting with the AWS assistant in the AWS Management Console
+ Diagnosing console errors with the AWS assistant

When you use any other feature at the Amazon Q Developer Pro tier, your content may be stored and processed in a US Region. If you are using a Q Developer profile in a non-US Region, you can create a service control policy (SCP) to block access to features that store content and perform inference in the US. For an example SCP, see [Example SCP: Deny access outside the Europe (Frankfurt) Region](security-iam-examples.md#scp-example-deny-outside-eu).

For other AWS assistant features, and when using the AWS assistant Free tier, your content is stored in a Region in the US. Data processed during diagnosing console error sessions is stored in US West (Oregon). All other data is stored in US East (N. Virginia). Note the following features that store data differently.

**Note**  
When you use visualizations, your visualizations-related content is stored in a US Region.  
When you create an investigation with Amazon CloudWatch investigations, your content may be stored and processed in other Regions. For more information, see [Security in CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#cross-region-inference) in the *Amazon CloudWatch User Guide*.

With cross-Region inference, your requests to the AWS assistant may be processed in a different Region within the geography where your content is stored. For more information, see [Cross-Region inference](cross-region-processing.md#cross-region-inference).
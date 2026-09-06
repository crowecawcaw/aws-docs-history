

# Setup scheduled assessments and drift notification
<a name="scheduled-assessment"></a>

AWS Resilience Hub allows you to setup scheduled assessments and drift notification for assessing your application daily and getting notified when a drift is detected.

**To setup drift notification**

1. To assess your application daily, turn on **Automatically assess daily**.

   If this option is turned on, the daily assessment schedule begins only after the following:
   + The application is manually assessed successfully for the first time.
   + The application is configured with an appropriate IAM role.
   + If your application is configured with current IAM user permissions, you must create the `AWSResilienceHubAsssessmentExecutionPolicy`

      role using the appropriate procedure in [How AWS Resilience Hub works with IAM](security_iam_service-with-iam.md).

1. To get notified when AWS Resilience Hub detects any drifts from the resiliency policies, or when its resources have drifted, turn on **Get notified when the application drifts**.

   If this option is turned on, to receive drift notifications, you must specify an Amazon Simple Notification Service (Amazon SNS) topic. To provide Amazon SNS topic, in **Provide an SNS Topic** section, select **Choose an SNS topic** option and select an Amazon SNS topic from the **Choose an SNS topic** dropdown list.
**Note**  
To enable AWS Resilience Hub to publish notifications to your Amazon SNS topics, your Amazon SNS topic must be configured with appropriate permissions. For more information about configuring permissions, see [Enabling AWS Resilience Hub to publish to your Amazon Simple Notification Service topics](enabling-sns-in-arh.md).
Daily assessments can have an impact on your quota for runs. For more information about quotas, see [AWS Resilience Hub endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/resiliencehub.html) in the *AWS General Reference*.

   To use Amazon SNS topics that are in a different AWS account or different Region, or both, select **Enter SNS topic ARN** and enter the Amazon Resource Name (ARN) of the Amazon SNS topic in the **Provide an SNS topic** box. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*.

## Next
<a name="scheduled-assessment-next"></a>

 [Setup permissions](setup-permissions.md) 
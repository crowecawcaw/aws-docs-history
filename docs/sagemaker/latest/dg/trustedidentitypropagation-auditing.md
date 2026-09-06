

# Monitoring and auditing with CloudTrail
<a name="trustedidentitypropagation-auditing"></a>

With trusted identity propagation enabled, AWS CloudTrail logs include the identity information of the specific user who performed an action, rather than just the IAM role. This provides enhanced auditing capabilities for compliance and security.

To view identity information in CloudTrail logs:
+ Open the [CloudTrail console](https://console.aws.amazon.com/cloudtrail).
+ Choose **Event history** from the left navigation pane.
+ Choose events from SageMaker AI and related services.
+ Under the **Event record** find `onBehalfOf` key. This contains the `userId` key and other user identification information that can be mapped to a specific IAM Identity Center user.

  See [CloudTrail use cases for IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/sso-cloudtrail-use-cases.html) for more information.
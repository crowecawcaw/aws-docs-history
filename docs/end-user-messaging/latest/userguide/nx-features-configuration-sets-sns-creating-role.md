

# Amazon SNS access policy
<a name="nx-features-configuration-sets-sns-creating-role"></a>

Access to an Amazon SNS topic is controlled by a *resource policy* attached to the Amazon SNS topic, this is also called an *access policy*. For more information about Amazon SNS *access polices*, see [Identity and access management](https://docs.aws.amazon.com/sns/latest/dg/security-iam.html) in the *Amazon SNS Developer Guide*. 

**Note**  
If your Amazon SNS topic has server-side encryption enabled with AWS Key Management Service then also add the policy to the associated [symmetric encryption customer](#nx-features-configuration-sets-sns-creating-role-encrypted) managed key.

Update the *access policy* with the following statement to permit AWS End User Messaging to publish to the Amazon SNS topic.
+ Replace {{111122223333}} with the unique ID for your AWS account.
+ Replace {{TopicName}} with the name of the Amazon SNS topic.
+ Replace {{Region}} with the AWS Region that contains the Amazon SNS topic and configuration set.
+ Replace {{ConfigSetName}} with the name of the configuration set.

**Note**  
Use the AWS End User Messaging console to generate the example IAM policy for this event destination.

## Access policy for encrypted Amazon SNS topics
<a name="nx-features-configuration-sets-sns-creating-role-encrypted"></a>

If your Amazon SNS topic has server-side encryption enabled with AWS Key Management Service, add the following policy to the associated symmetric encryption customer managed key. You must add the policy to a customer managed key because you cannot modify the AWS managed key for Amazon SNS. 

**Note**  
Use the AWS End User Messaging console to generate the example IAM policy for this event destination.
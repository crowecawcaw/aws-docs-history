

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Security best practices for Amazon Pinpoint
<a name="security-best-practices"></a>

Use AWS Identity and Access Management (IAM) accounts to control access to Amazon Pinpoint API operations, especially operations that create, modify, or delete Amazon Pinpoint resources. For the Amazon Pinpoint API, such resources include projects, campaigns and journeys. For the Amazon Pinpoint SMS and Voice API, such resources include phone numbers, pools and configuration sets. 
+ Create an individual user for each person who manages Amazon Pinpoint resources, including yourself. Don't use AWS root credentials to manage Amazon Pinpoint resources.
+ Grant each user the minimum set of permissions required to perform his or her duties.
+ Use IAM groups to effectively manage permissions for multiple users.
+ Rotate your IAM credentials regularly.

For more information about Amazon Pinpoint security, see [Security in Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security_iam_service-with-iam.html). For more information about IAM, see [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html). For information on IAM best practices, see [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html). 
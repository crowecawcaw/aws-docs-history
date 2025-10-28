# Identity and access management in the RFDK

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

Access controls in AWS are governed by the [AWS Identity & Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") service. In IAM, you can
create and manage identities, roles, and policies to determine what entities are able to access or modify which resources. CDK’s AWS Construct Library provides several constructs,
interfaces and classes for working with IAM in your CDK applications. For an overview of working with IAM in CDK, see the
[CDK Permissions documentation](../../../cdk/latest/guide/permissions.md "../../../cdk/latest/guide/permissions.md").

The RFDK uses CDK’s IAM concepts to grant access that is required from principals (e.g. EC2 instance profiles, ECS task definitions roles, etc…​) that require access to resources.
Some examples include:

- The Deadline Render Queue’s IAM role is granted read access to the Secrets Manager Secret that stores the credentials to the database
- The Deadline Worker Fleet’s IAM role is granted access to stream logs to the CloudWatch log group that it is configured to use
  When building a CDK application, it is important to take care when working with IAM resources. As a general rule, it is best to subscribe to the principle of least-privilege and
  only grant access as minimally required. In the CDK, this is done by scoping IAM policies to minimally required resources and principals. Please refer to
  [Security Best Practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") for more details.

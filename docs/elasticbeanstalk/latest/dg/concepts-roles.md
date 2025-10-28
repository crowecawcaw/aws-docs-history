# Elastic Beanstalk Service roles, instance profiles, and user

policies

Roles are an entities that you create with AWS Identity and Access Management (IAM) to apply permissions. There are
required roles for your Elastic Beanstalk environment to function properly. You also have the option to
create your own custom policies and roles that you can assign to users or groups.

## Required roles for your Elastic Beanstalk environment

When you create an environment, AWS Elastic Beanstalk prompts you to provide the following AWS Identity and Access Management
(IAM) roles:

- [Service role](concepts-roles-service.md "concepts-roles-service.md"): Elastic Beanstalk assumes a service role
  to use other AWS services on your behalf.
- [Instance profile](concepts-roles-instance.md "concepts-roles-instance.md") Elastic Beanstalk applies an instance
  profile to the Amazon EC2 instances in your environment. This action allows them to perform
  required tasks, such as retrieving information from Amazon Simple Storage Service (Amazon S3) and uploading logs to
  S3.

###### Create the service role and EC2 instance profile role

If your AWS account doesn’t have an EC2 instance profile or a service role, you must
create one of each using the IAM service. You can then assign the EC2 instance profile and
service role to new environments that you create. The **Create
environment** wizard guides you to the IAM service, so that you can create
these roles with the required permissions.

## Optional polices and roles to manage your Elastic Beanstalk

environment

You can optionally create [user policies](concepts-roles-user.md "concepts-roles-user.md") and
apply them to IAM users and groups in your account. Doing so allows the users to create and
manage Elastic Beanstalk applications and environments. You can also assign Elastic Beanstalk [managed policies](AWSHowTo.iam.md "AWSHowTo.iam.md") for full access and
read-only access to users or groups. For more information about these policies, see [Managing Elastic Beanstalk user policies](AWSHowTo.iam.md "AWSHowTo.iam.md").

You can create your own instance profiles and user policies for advanced scenarios. If
your instances need to access services that aren't included in the default policies, you can
create a new policy or add additional policies to the default one. If the managed policy is
too permissive for your needs, you can also create more restrictive user policies. For more
information about AWS permissions, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

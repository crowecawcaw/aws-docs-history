# Create a service-linked role for

AWS IoT SiteWise

AWS IoT SiteWise requires a service-linked role to perform certain actions and to access resources on your behalf. A service-linked role is a unique type of AWS Identity and Access Management (IAM) role that is linked directly to AWS IoT SiteWise. By creating this role, you grant AWS IoT SiteWise the necessary permissions to access other AWS services and resources required for its operation, such as Amazon S3 for data storage or AWS IoT for device communication.

You don't need to manually create a service-linked role. When you perform the following
operations in the AWS IoT SiteWise console, AWS IoT SiteWise creates the service-linked role for you.

- Create a Greengrass V1 gateway.
- Configure the logging option.
- Choosing the opt-in button in the execute query banner.
  If you delete this service-linked role, and then need to create it again, you can use the
  same process to recreate the role in your account. When you perform any operation in the
  AWS IoT SiteWise console, AWS IoT SiteWise creates the service-linked role for you again.

You can also use the IAM console or API to create a service-linked role for
AWS IoT SiteWise.

- To do so in the IAM console, create a role with the **AWSServiceRoleForIoTSiteWise**
  policy and a trust relationship with `iotsitewise.amazonaws.com`.
- To do so using the AWS CLI or IAM API, create a role with the
  `arn:aws:iam::aws:policy/aws-service-role/AWSServiceRoleForIoTSiteWise`
  policy and a trust relationship with `iotsitewise.amazonaws.com`.
  For more information, see [Create a service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#create-service-linked-role "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#create-service-linked-role") in the _IAM User Guide_.

If you delete this service-linked role, you can use this same process to create the role
again.

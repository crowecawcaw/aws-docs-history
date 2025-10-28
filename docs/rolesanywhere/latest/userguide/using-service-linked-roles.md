# Using service-linked roles for IAM Roles Anywhere

AWS Identity and Access Management Roles Anywhere uses IAM[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to IAM Roles Anywhere. Service-linked roles are predefined by IAM Roles Anywhere and
include all the permissions that the service requires to publish CloudWatch metrics
and ensure the private certificate authorities you use as trust anchors can be accessed as part
of authenticating with IAM Roles Anywhere. They also ensure that you receive auditing information
regarding IAM Roles Anywhere. Service-linked roles are different from the roles that you configure for
the service and obtain temporary credentials for.

A service-linked role makes setting up IAM Roles Anywhere easier because you don’t have to
manually add the necessary permissions. IAM Roles Anywhere defines the permissions of its
service-linked roles. Unless defined otherwise, only IAM Roles Anywhere can assume its service-linked
roles. The defined permissions include the trust policy and the permissions policy. The
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This
protects your IAM Roles Anywhere resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles**
column. Choose a **Yes** with a link to view the service-linked
role documentation for that service.

## Service-linked role permissions for

IAM Roles Anywhere

IAM Roles Anywhere uses the service-linked role named **AWSServiceRoleForRolesAnywhere**
which allows IAM Roles Anywhere to publish CloudWatch metrics and check the configuration of AWS Private CA
in your account. This service-linked role has an IAM policy attached to it named
[AWSRolesAnywhereServicePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceRoleForRolesAnywhere "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceRoleForRolesAnywhere").

The AWSServiceRoleForRolesAnywhere service-linked role trusts the following services to assume the role:

- `rolesanywhere.amazonaws.com`

The role permissions policy named AWSRolesAnywhereServicePolicy allows IAM Roles Anywhere to complete the following actions on the
specified resources:

- Actions on CloudWatch:
  - `cloudwatch:PutMetricData` – Allows IAM Roles Anywhere to publish metric
    data points to the `AWS/RolesAnywhere` and `AWS/Usage` namespaces.

- Actions on AWS Private CA:
  - `acm-pca:GetCertificateAuthorityCertificate` – Allows IAM Roles Anywhere to retrieve the certificate and
    certificate chain for your private certificate authority.
  - `acm-pca:DescribeCertificateAuthority` – Allows IAM Roles Anywhere to list information about your
    private certificate authority.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": [
 "AWS/RolesAnywhere",
 "AWS/Usage"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "acm-pca:GetCertificateAuthorityCertificate",
 "acm-pca:DescribeCertificateAuthority"
 ],
 "Resource": "arn:aws:acm-pca:*:*:*"
 }
 ]
 }`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": [
 "AWS/RolesAnywhere",
 "AWS/Usage"
 ]
 }
 }
 }
 ]
 }`

```

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for

IAM Roles Anywhere

You don't need to manually create a service-linked role. When you
create your first trust anchor in the AWS Management Console, the AWS CLI, or the AWS API, IAM Roles Anywhere
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. Note that credentials will still be issued, but metrics will not be reported.

You can also use the IAM console to create a service-linked role when you have trust
anchors in your account but no service-linked role. In the AWS CLI or the AWS API, create a
service-linked role with the `rolesanywhere.amazonaws.com` service name. For more
information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for

IAM Roles Anywhere

IAM Roles Anywhere does not allow you to edit the AWSServiceRoleForRolesAnywhere service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for

IAM Roles Anywhere

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If IAM Roles Anywhere is using the role when you try to delete the resources, then the
deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To delete IAM Roles Anywhere resources used by the AWSServiceRoleForRolesAnywhere

- Delete all trust anchors in your account in all Regions that contain them.

###### To manually delete the service-linked role using

IAM

- For information about using the IAM console, the AWS CLI, or the AWS API to delete the
  AWSServiceRoleForRolesAnywhere service-linked role, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
  _IAM User Guide_.

## Supported regions for

IAM Roles Anywhere service-linked roles

IAM Roles Anywhere supports using service-linked roles in all of the regions where the service
is available. For more information, see [AWS regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

| Region name                | Region identity | Support in IAM Roles Anywhere |
| -------------------------- | --------------- | ----------------------------- |
| US East (N. Virginia)      | us-east-1       | Yes                           |
| US East (Ohio)             | us-east-2       | Yes                           |
| US West (N. California)    | us-west-1       | Yes                           |
| US West (Oregon)           | us-west-2       | Yes                           |
| Asia Pacific (Mumbai)      | ap-south-1      | Yes                           |
| Asia Pacific (Osaka)       | ap-northeast-3  | Yes                           |
| Asia Pacific (Seoul)       | ap-northeast-2  | Yes                           |
| Asia Pacific (Singapore)   | ap-southeast-1  | Yes                           |
| Asia Pacific (Sydney)      | ap-southeast-2  | Yes                           |
| Asia Pacific (Tokyo)       | ap-northeast-1  | Yes                           |
| Asia Pacific (Hong Kong)   | ap-east-1       | Yes                           |
| Asia Pacific (Jakarta)     | ap-southeast-3  | Yes                           |
| Canada (Central)           | ca-central-1    | Yes                           |
| Europe (Frankfurt)         | eu-central-1    | Yes                           |
| Europe (Ireland)           | eu-west-1       | Yes                           |
| Europe (London)            | eu-west-2       | Yes                           |
| Europe (Paris)             | eu-west-3       | Yes                           |
| Europe (Milan)             | eu-south-1      | Yes                           |
| Europe (Stockholm)         | eu-north-1      | Yes                           |
| Africa (Cape Town)         | af-south-1      | Yes                           |
| South America (São Paulo)  | sa-east-1       | Yes                           |
| Middle East (Bahrain)      | me-south-1      | Yes                           |
| Asia Pacific (Hyderabad)   | ap-south-2      | Yes                           |
| Europe (Zurich)            | eu-central-2    | Yes                           |
| Europe (Spain)             | eu-south-2      | Yes                           |
| Middle East (UAE)          | me-central-1    | Yes                           |
| Asia Pacific (Melbourne)   | ap-southeast-4  | Yes                           |
| Israel (Tel Aviv)          | il-central-1    | Yes                           |
| Canada West (Calgary)      | ca-west-1       | Yes                           |
| Asia Pacific (Thailand)    | ap-southeast-7  | Yes                           |
| Asia Pacific (Malaysia)    | ap-southeast-5  | Yes                           |
| Mexico (Central)           | mx-central-1    | Yes                           |
| Asia Pacific (Taipei)      | ap-east-2       | Yes                           |
| Asia Pacific (New Zealand) | ap-southeast-6  | Yes                           |
| AWS GovCloud (US-West)     | us-gov-west-1   | Yes                           |
| AWS GovCloud (US-East)     | us-gov-east-1   | Yes                           |

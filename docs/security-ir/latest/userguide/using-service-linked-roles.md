# Using service-linked roles

**Service-linked
roles for AWS Security Incident Response**

###### Contents

- [AWS SLR: AWSServiceRoleForSecurityIncidentResponse](#AWSServiceRoleForSecurityIncidentResponse "#AWSServiceRoleForSecurityIncidentResponse")
- [AWS SLR: AWSServiceRoleForSecurityIncidentResponse_Triage](#AWSServiceRoleForSecurityIncidentResponse_Triage "#AWSServiceRoleForSecurityIncidentResponse_Triage")
- [Supported regions for AWS Security Incident Response service-linked roles](#sir-slr-regions "#sir-slr-regions")

**Supports service-linked
roles:** Yes

A service-linked role is a type of service role that is linked
to an AWS service. The service can assume the role to perform an
action on your behalf. Service-linked roles appear in your AWS
account and are owned by the service. An IAM administrator can
view, but not edit the permissions for service-linked roles.

A service-linked role makes setting up AWS Security Incident Response easier because
you don’t have to manually add the necessary permissions. AWS Security Incident Response
defines the permissions of its service-linked roles, and unless defined
otherwise, only AWS Security Incident Response can assume its roles. The defined permissions
include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles,
see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have
**Yes**
in the Service-linked roles column. Choose a Yes with a link to view the
service-linked role documentation for that service.

## AWS SLR: AWSServiceRoleForSecurityIncidentResponse

AWS Security Incident Response uses the service-linked role (SLR) named AWSServiceRoleForSecurityIncidentResponse
– AWS Security Incident Response policy to identify accounts subscribed, create cases, and tag related resources.

### Permissions

The AWSServiceRoleForSecurityIncidentResponse service-linked role trusts the following service
to assume the role:

- `triage.security-ir.amazonaws.com`

Attached to this role is the
AWS managed policy named [AWSSecurityIncidentResponseServiceRolePolicy](aws-managed-policies.md#AWSSecurityIncidentResponseServiceRolePolicy "aws-managed-policies.md#AWSSecurityIncidentResponseServiceRolePolicy").
The service uses the role to perform actions on the following resources:

- _AWS Organizations:_ Allows the service to lookup membership accounts for use with the service.
- _CreateCase:_ Allows the service create service cases on behalf of membership accounts.
- _TagResource:_ Allows the service tag resources configured as part of the service.

### Managing the role

You don't need to manually create a service-linked role. When you onboard to to AWS Security Incident Response in the AWS Management Console, the AWS CLI,
or the AWS API, the service creates the service-linked role for you.

###### Note

If you created a membership using a delegated administrator account, then
service-linked roles need to be manually created in AWS Organizations Management accounts.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the
role in your account. When you onboard to the service it creates the service-linked role for you again.

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see
[Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## AWS SLR: AWSServiceRoleForSecurityIncidentResponse_Triage

AWS Security Incident Response uses the service-linked role (SLR) named AWSServiceRoleForSecurityIncidentResponse_Triage
– AWS Security Incident Response policy to continuously monitor your environment for security threats,
tune security services to reduce alert noise, and gather information to investigate potential incidents.

### Permissions

The AWSServiceRoleForSecurityIncidentResponse_Triage service-linked role trusts the following service
to assume the role:

- `triage.security-ir.amazonaws.com`

Attached to this role is the
AWS managed policy [AWSSecurityIncidentResponseTriageServiceRolePolicy](aws-managed-policies.md#AWSSecurityIncidentResponseTriageServiceRolePolicy "aws-managed-policies.md#AWSSecurityIncidentResponseTriageServiceRolePolicy").
The service uses the role to perform actions on the following resources:

- _Events:_ Allows the service to create an Amazon EventBridge managed rule.
  This rule is the infrastructure required in your AWS account to deliver events from your account to the service.
  This action is performed on any AWS resource managed by `triage.security-ir.amazonaws.com`.
- _Amazon GuardDuty:_ Allows the service to tune security services to reduce alert noise and gather
  information to investigate potential incidents. This action is performed on any AWS resource.
- _AWS Security Hub:_ Allows the service to tune security services to reduce alert noise and gather
  information to investigate potential incidents. This action is performed on any AWS resource.

### Managing the role

You don't need to manually create a service-linked role. When you onboard to to AWS Security Incident Response in the AWS Management Console, the AWS CLI,
or the AWS API, the service creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the
role in your account. When you onboard to the service it creates the service-linked role for you again.

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see
[Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Supported regions for AWS Security Incident Response service-linked roles

AWS Security Incident Response supports using service-linked roles in all of the regions where the service is available.

- US East (Ohio)
- US West (Oregon)
- US East (Virginia)
- EU (Frankfurt)
- EU (Ireland)
- EU (London)
- EU (Paris)
- EU (Stockholm)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- South America (São Paulo)

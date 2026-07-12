# Service-linked role permissions for Amazon Inspector multi-cloud scans

Amazon Inspector multi-cloud scanning uses the service-linked role named `AWSServiceRoleForAmazonInspector2ThirdParty`. This SLR allows Amazon Inspector to perform actions on your behalf for multi-cloud resource scanning, including managing cloud connectors, configuration recorders, and vulnerability assessments of resources in external cloud environments. This
service-linked role trusts the `thirdparty.inspector2.amazonaws.com` service to assume the
role.

The permissions policy for the role, which is named `AmazonInspector2ThirdPartyServiceRolePolicy`, allows
Amazon Inspector to perform tasks such as:

- Use actions to discover multi-cloud resources through Inspector-owned service views.
- Use AWS Systems Manager actions to manage associations, automation executions, and cloud connectors for multi-cloud VM scanning.
- Use the IAM `PassRole` action to pass Amazon Inspector roles to AWS Systems Manager for automation execution, scoped to roles with names starting with `Inspector2SSM` or `Inspector2VmScanner`.
- Use the IAM `GetRole` action to verify that Amazon Inspector roles exist before passing them.
- Use the IAM `CreateServiceLinkedRole` action to create the AWS Systems Manager service-linked role when required by association creation.
- Use actions to manage service-linked configuration recorders and connectors for multi-cloud resource discovery.
- Use CloudWatch actions to retrieve health metrics for multi-cloud connectors.
- Use AWS STS `GetWebIdentityToken` action for OIDC federation into external cloud environments, scoped to the Azure AD token audience.
  For the permissions in this policy, see [AmazonInspector2ThirdPartyServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonInspector2ThirdPartyServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonInspector2ThirdPartyServiceRolePolicy.md") in the _AWS Managed Policy Reference Guide_.

# IAM roles created by the Systems Manager console

When you create a Cloud Connector in the Systems Manager AWS Management Console, Systems Manager creates and
configures three IAM roles in your AWS account on your behalf. It also
assigns a managed instance role to the Azure virtual machines registered through
the connector. The roles establish the trust chain between Systems Manager, State Manager,
Automation, and Azure through OpenID Connect (OIDC) federation. This trust chain
lets Systems Manager run Automation runbooks against your Azure virtual machines without
long-lived secrets.

Each role name uses the pattern
`SSM-Azure`Type`-`connector-name`-`id8``,
where `connector-name` is the display name you provided
(sanitized to alphanumeric characters, dashes, and underscores, then truncated
to fit IAM's 64-character role-name limit) and `id8`
is the first eight characters of a UUID. The roles are created in the
`/service-role/` IAM path.

The console creates the roles in this order:

1. Azure federation role, with a trust policy that initially names only
   the Systems Manager service principal as a trusted entity.
2. Automation assume role and automation dispatch role.
3. The console then updates the Azure federation role's trust policy to
   add the automation assume role and the automation dispatch role as
   trusted principals. After this update, the trust policy is the one shown
   in [Azure federation role](cloud-connector-azure-federation-role.md "cloud-connector-azure-federation-role.md").

###### Note

The Systems Manager console creates these roles only during the Cloud Connector setup
wizard. If you create a Cloud Connector with the AWS CLI (as described in [Step 2: Create an Systems Manager Cloud Connector](cloud-connector-create-ssm-connector.md "cloud-connector-create-ssm-connector.md")), you must create the
roles yourself. The trust and permissions policies in this section show the
JSON you can use to recreate them. If you recreate the roles, do the
following:

- Create all three roles (Azure federation, automation assume, and
  automation dispatch) in the `/service-role/` IAM path.
  The permissions policies and the Azure federation role's trust policy
  reference the roles by ARNs that include this path.
- Tag the automation assume role and the automation dispatch role
  with the principal tag `caller=SSM`. The Azure federation
  role's trust policy requires this tag.
  All API calls that these roles make are logged to AWS CloudTrail (CloudTrail). For
  information about Systems Manager logging in CloudTrail, see [Logging AWS Systems Manager API calls with AWS CloudTrail](monitoring-cloudtrail-logs.md "monitoring-cloudtrail-logs.md").

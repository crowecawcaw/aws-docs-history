# IAM condition keys for organizational

governance

AWS Transfer Family provides IAM condition keys that allow you to restrict resource configurations in
any IAM policy. These condition keys can be used in identity-based policies attached to
users or roles, or Service Control Policies (SCPs) for organizational governance.

Service Control Policies are IAM policies that apply to an entire AWS organization,
providing preventative guardrails across multiple accounts. When used in SCPs, these
condition keys help enforce security and compliance requirements organization-wide.

See also

- [Actions, resources, and condition keys for Transfer Family](../../../service-authorization/latest/reference/list_awstransferfamily.md "../../../service-authorization/latest/reference/list_awstransferfamily.md")
- [Service
  control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md")
- Video describing how to enforce preventive
  guardrails using service control policies

## Available condition keys

AWS Transfer Family supports the following condition keys for use in IAM policies:

`transfer:RequestServerEndpointType`

Restricts server creation and updates based on endpoint type (PUBLIC, VPC,
VPC_ENDPOINT). Commonly used to prevent public-facing endpoints.

`transfer:RequestServerProtocols`

Restricts server creation and updates based on supported protocols (SFTP,
FTPS, FTP, AS2).

`transfer:RequestServerDomain`

Restricts server creation based on domain type (S3, EFS).

`transfer:RequestConnectorProtocol`

Restricts connector creation based on protocol (AS2, SFTP).

## Supported actions

The condition keys can be applied to the following AWS Transfer Family actions:

- `CreateServer`: Supports `RequestServerEndpointType`,
  `RequestServerProtocols`, and `RequestServerDomain`
  condition keys
- `UpdateServer`: Supports `RequestServerEndpointType` and
  `RequestServerProtocols` condition keys
- `CreateConnector`: Supports `RequestConnectorProtocol`
  condition key

## Example SCP policy

The following example SCP prevents the creation of public AWS Transfer Family servers across your
organization:

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "DenyPublicTransferServers",
 "Effect": "Deny",
 "Action": ["transfer:CreateServer", "transfer:UpdateServer"],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "transfer:RequestServerEndpointType": "PUBLIC"
 }
 }
 }]
}`

```

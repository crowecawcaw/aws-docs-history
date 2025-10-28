#

Considerations and limitations for AWS Glue ETL Trusted Identity Propagation integration

###### Important

By default sessions are not private which means one IdC user can access another IdC user's session. You can use
[tagOnCreate](glue-is-security.md#glue-is-tagoncreate "glue-is-security.md#glue-is-tagoncreate") to make your
sessions private. For example, the session can be tagged with an owner tag and the value of it as IDC User Id and then on the policy, you can
use a global condition key like
[`identitystore:UserId`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-identity-store-user-id "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-identity-store-user-id") to validate against the owner tag in the client principal/runtime role
policy for all session API operations to ensure that one IdC User isn't able to access another IdC user's session.

Consider the following points when you use IAM Identity Center Trusted Identity Propagation with AWS Glue Application:

- Trusted Identity Propagation through Identity Center is supported on AWS Glue 5.0 and higher, and only with AWS Glue interactive
  sessions.
- AWS Glue data catalog is covered under Lake Formation identity center integration.
- Trusted Identity Propagation is limited to interactive sessions in AWS Glue, excluding other data processing entities like jobs,
  triggers, workflows, and ML tasks. All AWS Glue APIs, however, record user identities in AWS CloudTrail for auditing.
- AWS Glue currently supports integration with IAM Identity Center exclusively through API and CLI interfaces, not via the console.
- Once an application is enabled on AWS Glue side, make sure to create 5.0 sessions with IdC Credentials but don't create a 4.0
  session with IdC credentials.
- Trusted Identity Propagation with AWS Glue is supported in the following AWS Regions:
  - af-south-1 – Africa (Cape Town)
  - ap-east-1 – Asia Pacific (Hong Kong)
  - ap-northeast-1 – Asia Pacific (Tokyo)
  - ap-northeast-2 – Asia Pacific (Seoul)
  - ap-northeast-3 – Asia Pacific (Osaka)
  - ap-south-1 – Asia Pacific (Mumbai)
  - ap-southeast-1 – Asia Pacific (Singapore)
  - ap-southeast-2 – Asia Pacific (Sydney)
  - ap-southeast-3 – Asia Pacific (Jakarta)
  - ca-central-1 – Canada (Central)
  - eu-central-1 – Europe (Frankfurt)
  - eu-north-1 – Europe (Stockholm)
  - eu-south-1 – Europe (Milan)
  - eu-west-1 – Europe (Ireland)
  - eu-west-2 – Europe (London)
  - eu-west-3 – Europe (Paris)
  - me-south-1 – Middle East (Bahrain)
  - sa-east-1 – South America (São Paulo)
  - us-east-1 – US East (N. Virginia)
  - us-east-2 – US East (Ohio)
  - us-west-1 – US West (N. California)
  - us-west-2 – US West (Oregon)

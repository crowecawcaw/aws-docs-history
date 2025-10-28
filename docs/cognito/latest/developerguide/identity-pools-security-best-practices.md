# Security best practices for Amazon Cognito

identity pools

Amazon Cognito identity pools provide temporary AWS credentials for your application.
AWS accounts often contain both the resources that your application users need, and
private back-end resources. The IAM roles and policies that make up AWS credentials can
grant access to any of these resources.

The primary best practice of identity pool configuration is to ensure that your
application can get the job done without excess or unintended privilege. To guard against
security misconfiguration, review these recommendations before the launch of each
application that you want to release to production.

###### Topics

- [IAM configuration best
  practices](#identity-pools-security-best-practices-iam "#identity-pools-security-best-practices-iam")
- [Identity pool configuration
  best practices](#identity-pools-security-best-practices-cib "#identity-pools-security-best-practices-cib")

## IAM configuration best

practices

When a guest or authenticated user initiates a session in your application that
requires identity pool credentials, your application retrieves temporary AWS
credentials for an IAM role. The credentials might be for a default role, a role
chosen by rules in your identity pool configuration, or for a custom role chosen by your
app. With the permissions assigned to each role, your user gains access to your AWS
resources.

For more information about general IAM best practices, see [IAM best
practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the AWS Identity and Access Management User Guide.

### Use trust

policy conditions in IAM roles

IAM requires that roles for identity pools have at least one trust policy
condition. This condition can, for example, set the role’s scope to authenticated
users only. AWS STS also requires that cross-account basic authentication requests
have two specific conditions: `cognito-identity.amazonaws.com:aud` and
`cognito-identity.amazonaws.com:amr`. As a best practice, apply both
of these conditions in all IAM roles that trust the identity pools service
principal `cognito-identity.amazonaws.com`.

- `cognito-identity.amazonaws.com:aud`: The _aud_ claim in the identity pool token must match
  a trusted identity pool ID.
- `cognito-identity.amazonaws.com:amr`: The _amr_ claim in the identity pool token must be
  either _authenticated_ or _unauthenticated_. With this condition, you can
  reserve access to a role only to unauthenticated guests, or only to
  authenticated users. You can further refine the value of this condition to
  restrict the role to users from a specific provider, for example
  `graph.facebook.com`.

The following example role trust policy grants access to a role under the
following conditions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Federated": "cognito-identity.amazonaws.com"
 },
 "Action": "sts:AssumeRoleWithWebIdentity",
 "Condition": {
 "StringEquals": {
 "cognito-identity.amazonaws.com:aud": "us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
 },
 "ForAnyValue:StringLike": {
 "cognito-identity.amazonaws.com:amr": "authenticated"
 }
 }
 }
 ]
}`

```

###### Elements that relate to identity pools

- `"Federated": "cognito-identity.amazonaws.com"`: Users must
  come from an identity pool.
- `"cognito-identity.amazonaws.com:aud":
"us-east-1:a1b2c3d4-5678-90ab-cdef-example11111"`: Users must come
  from the specific identity pool
  `us-east-1:a1b2c3d4-5678-90ab-cdef-example11111`.
- `"cognito-identity.amazonaws.com:amr": "authenticated"`: Users
  must be authenticated. Guest users can’t assume the role.

### Apply

least privilege permissions

When you set permissions with IAM policies for authenticated access or guest
access, grant only the specific permissions required to perform specific tasks, or
_least privilege_ permissions. The following
example IAM policy, when applied to a role, grants read-only access to a single
image file in an Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject"
 ],
 "Effect": "Allow",
 "Resource": ["arn:aws:s3:::mybucket/assets/my_picture.jpg"]
 }
 ]
}`

```

## Identity pool configuration

best practices

Identity pools have flexible options for the generation of AWS credentials. Don’t
take design shortcuts when your application can work with the most secure
methods.

### Understand the

effects of guest access

Unauthenticated guest access permits users to retrieve data from your
AWS account before they sign in. Anyone who knows your identity pool ID can
request unauthenticated credentials. Your identity pool ID isn’t confidential
information. When you activate guest access, the AWS permissions that you grant to
unauthenticated sessions are available to everyone.

As a best practice, leave guest access deactivated and fetch required resources
only after users authenticate. If your application requires access to resources
before sign-in, take the following precautions.

- Familiarize yourself with the [automatic limitations
  placed on unauthenticated roles](iam-roles.md#access-policies-scope-down-services "iam-roles.md#access-policies-scope-down-services").
- Monitor and adjust the permissions of your unauthenticated IAM roles to
  match the specific needs of your application.
- Grant access to specific resources.
- Secure the trust policy of your default unauthenticated IAM role.
- Activate guest access only when you are confident that you would grant the
  permissions in your IAM role to anyone on the internet.

### Use enhanced

authentication by default

With basic (classic) authentication, Amazon Cognito delegates selection of the IAM role
to your app. In contrast, the enhanced flow uses the centralized logic in your
identity pool to determine the IAM role. It also provides additional security for
unauthenticated identities with a [scope-down policy](iam-roles.md#access-policies-scope-down-services "iam-roles.md#access-policies-scope-down-services") that sets
an upper limit on IAM permissions. The enhanced flow is the most secure choice
with the lowest level of developer effort. To learn more about these options, see
[Identity pools authentication flow](authentication-flow.md "authentication-flow.md")
.

The basic flow can expose the client-side logic that goes into role selection and
assembly of the AWS STS API request for credentials. The enhanced flow hides both
the logic and the assume-role request behind identity pool automation.

When you configure basic authentication, apply [IAM best practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") to
your IAM roles and their permissions.

### Use developer

providers securely

Developer authenticated identities are a feature of identity pools for server-side
applications. The only evidence of authentication that identity pools require for
developer authentication are the AWS credentials of an identity pool developer.
Identity pools don’t enforce any restrictions on the validity of the
developer-provider identifiers that you present in this authentication flow.

As a best practice, only implement developer providers under the following
conditions:

- To create accountability for the use of developer-authenticated
  credentials, design your developer provider name and identifiers to indicate
  the authentication source. For example: `"Logins" : {"MyCorp provider"
: "`[provider application ID]`"}`.
- Avoid long-lived user credentials. Configure your server-side client to
  request identities with service-linked roles like [EC2 instance profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md") and [Lambda execution
  roles](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md").
- Avoid mixing internal and external sources of trust in the same identity
  pool. Add your developer provider and your single sign-on (SSO) providers in
  separate identity pools.

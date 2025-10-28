# Dynamic permission management

approaches

## Understanding Transfer Family permission

architecture

AWS Transfer Family supports dynamic permission management through session policies, which allow
you to restrict the effective permissions of IAM roles at runtime. This approach works
for both service-managed users and custom identity provider users, but is only supported
when transferring files to or from Amazon S3 (not Amazon EFS).

Every AWS Transfer Family user operates with a permission model that consists of:

1. _Base IAM role_ - Defines the foundational permissions for
   the user
2. _Optional session policy_ - Restricts (scopes down) the
   base permissions at runtime

The effective permissions are the intersection of the base role permissions and the
session policy permissions. Session policies can only restrict permissions; they cannot
grant additional permissions beyond what the base role allows.

This architecture applies to both user types:

- _Service-managed users_ - Session policies can be
  configured directly in the user settings
- _Custom identity provider users_ - Session policies can be
  returned as part of the authentication response or stored in AWS Secrets Manager

## Two approaches to permission

management

When designing permissions for Transfer Family users who need unique access patterns, you can
choose between two main approaches:

One role per user

Create a separate IAM role for each Transfer Family user with specific permissions
tailored to that user's needs. Use this approach when:

- Each user requires very different permissions
- Permission administration is handled by different people in your
  organization
- You need fine-grained control over individual user access

Shared role with session policies

Use a single IAM role with broad permissions (such as access to an entire
Amazon S3 bucket containing multiple user home directories) and apply session
policies to restrict each user to their specific area. This approach
significantly reduces administrative overhead compared to managing separate
roles for each user. Use this approach when:

- Users need similar types of access but to different resources (for
  example, all users need read/write access, but each only to their
  own folder)
- You want to simplify role management and avoid creating dozens or
  hundreds of individual roles
- Users should only access their designated home directories within
  a shared bucket
- Permission administration is centralized within your
  organization

For example, instead of creating separate roles for users "alice", "bob",
and "charlie", you can create one role with access to the entire
`s3://company-transfers/` bucket, then use session policies
to restrict alice to `s3://company-transfers/alice/`, bob to
`s3://company-transfers/bob/`, and so on.

## Implementing session policies

Session policies work by restricting the effective permissions of the base IAM role
assigned to a user. The final permissions are the intersection of the role's permissions
and the session policy's permissions.

You can implement dynamic session policies in two ways:

Variable substitution

Use Transfer Family policy variables such as `${transfer:Username}`,
`${transfer:HomeDirectory}`, and
`${transfer:HomeBucket}` in your session policies. These
variables are automatically replaced with the actual values at runtime. For
more information about these variables, see [Creating a session policy for an Amazon S3
bucket](users-policies-session.md "users-policies-session.md").

Dynamic generation

For custom identity providers, generate session policies on-the-fly as
part of the authentication response from your Lambda function or API Gateway
method. This approach allows you to create highly customized policies based
on user attributes, group memberships, or external data sources at
authentication time.

You can also store pre-generated session policies in AWS Secrets Manager by
including a key named `Policy` with the session policy JSON as
the value. This allows you to use the same broad IAM role across multiple
users while maintaining user-specific access controls.

###### Note

Session policies are only supported for file transfers to and from Amazon S3. They do
not apply to Amazon EFS file systems. For Amazon EFS, permissions are governed by UID/GID and
permission bits applied within the filesystem itself.

## Implementation by user type

Service-managed users

For service-managed users, you can specify session policies directly in
the user configuration through the AWS Transfer Family console, API, or CLI. For more
information, see [Working with service-managed users](service-managed-users.md "service-managed-users.md").

Custom identity provider users

For custom identity provider users, you can provide session policies in
two ways:

- Through AWS Secrets Manager by including a key named `Policy`
  with the session policy as the value
- Directly in the Lambda function response or API Gateway response as
  part of the authentication result

For more information, see [Custom identity provider solution](custom-idp-toolkit.md "custom-idp-toolkit.md").

## Example: Simplifying role management with

session policies

This example demonstrates how dynamic permission management can significantly reduce
administrative overhead while maintaining security.

### Scenario

Your organization has 50 users who need SFTP access to transfer files. Each user
should only access their own folder within a shared Amazon S3 bucket called
`company-transfers`. Without session policies, you would need to
create 50 separate IAM roles.

Traditional approach (without session policies)

- Create 50 IAM roles: `TransferRole-Alice`,
  `TransferRole-Bob`,
  `TransferRole-Charlie`, etc.
- Each role has specific permissions to only that user's
  folder
- Managing permissions requires updating individual roles
- Adding new users requires creating new roles

Dynamic approach (with session policies)

- Create 1 IAM role: `TransferRole-Shared` with broad
  permissions to the entire bucket
- Use session policies to restrict each user to their specific
  folder at runtime
- Managing permissions requires updating one role or session
  policy template
- Adding new users requires no new roles, just user
  configuration

### Implementation

Here's how you would implement the dynamic approach (using the
`company-transfers` bucket as an example to be replaced with your
actual Amazon S3 bucket):

###### To implement dynamic permission management

1. Create one shared IAM role with broad Amazon S3 permissions:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": "arn:aws:s3:::company-transfers/*"
 },
 {
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::company-transfers"
 }
 ]
}`

```

2. Create a session policy template that restricts access to the user's
   folder:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": "arn:aws:s3:::company-transfers/${transfer:Username}/*"
 },
 {
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::company-transfers",
 "Condition": {
 "StringLike": {
 "s3:prefix": "${transfer:Username}*"
 }
 }
 }
 ]
}`

```

3. Configure each user with:
   - The shared IAM role
   - The session policy applied as follows:
     - _Service-managed users_: Use the API or
       CLI to apply the JSON via the Policy parameter when creating
       or modifying users (the console only offers predefined
       policy options)
     - _Custom identity provider users_:
       Either return it as part of the Lambda function response
       during authentication, or store it in AWS Secrets Manager as a key
       named "Policy" alongside the user's credentials

   - Home directory:
     `/company-transfers/${transfer:Username}/`

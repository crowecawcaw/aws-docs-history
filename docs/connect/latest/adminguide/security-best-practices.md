# Security Best Practices for Amazon Connect

Amazon Connect provides a number of security features to consider as you develop and implement your
own security policies. The following best practices are general guidelines and don't
represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

###### Contents

- [Amazon Connect preventative security best
  practices](#bp-security-profiles "#bp-security-profiles")
- [Amazon Connect detective security best practices](#bp-security-detective "#bp-security-detective")
- [Amazon Connect Chat security best practices](#bp-security-chat "#bp-security-chat")
- [Amazon Connect WebRTC security best practices](#bp-webrtc-security "#bp-webrtc-security")

## Amazon Connect preventative security best

practices

- Ensure that all profile permissions are as restrictive as possible. Allow
  access to only those resources absolutely required for the user's role. For
  example, don't give agents permissions to create, read, or update users in
  Amazon Connect.
- Ensure that multi-factor authentication (MFA) is set up through your SAML 2.0
  identity provider, or Radius server, if that's more applicable for your use
  case. After MFA is set up, a third text box becomes visible on the Amazon Connect login
  page to provide the second factor.
- If you use an existing directory through Directory Service or SAML-based authentication
  for identity management, ensure that you follow all security requirements
  appropriate for your use case.
- Use the **Log in for emergency access** URL on the instance
  page of the AWS console only in emergency situations, not for daily use. For
  more information, see [Emergency login to the Amazon Connect admin
  website](emergency-admin-login.md "emergency-admin-login.md").

### Use service control policies (SCPs)

Service control policies (SCPs) are a type of organization policy that you can use
to manage permissions in your organization. An SCP defines a guardrail, or sets
limits, on the actions that the account's administrator can delegate to users and
roles in the affected accounts. You can use SCPs to protect critical resources
associated with your Amazon Connect workload.

#### Set a Service Control Policy to prevent the deletion

critical resources

If you’re using SAML 2.0-based authentication and delete the AWS IAM Role
that is used for authenticating Amazon Connect users, users won't be able to log in to
the Amazon Connect instance. You will need to delete and recreate users to be associated
with a new Role. This results in the deletion of all data associated with those
users.

To prevent the accidental deletion of critical resources and to protect the
availability of your Amazon Connect instance, you can set a [Service Control
Policy](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") (SCP) as an additional control.

Following is an example SCP that can be applied at the AWS Account,
Organizational Unit, or Organizational Root to prevent the deletion of the Amazon Connect
instance and associated Role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonConnectRoleDenyDeletion",
 "Effect": "Deny",
 "Action": [
 "iam:DeleteRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/`ConnectUserRole`"
 ]
 },
 {
 "Sid": "AmazonConnectInstanceDenyDeletion",
 "Effect": "Deny",
 "Action": [
 "connect:DeleteInstance"
 ],
 "Resource": [
 "arn:aws:connect:`us-east-1`:`111122223333`:instance/`InstanceId`"
 ]
 }
 ]
}`

```

## Amazon Connect detective security best practices

Logging and monitoring are important for the availability, reliability and,
performance of contact center. You should [log relevant
information from Amazon Connect flows to CloudWatch](contact-flow-logs.md "contact-flow-logs.md") and [build alerts and notifications](contact-flow-log-alerts.md "contact-flow-log-alerts.md") based on the
same.

Define log retention requirements and lifecycle policies early on, and plan to move
log files to cost-efficient storage locations as soon as practical. Amazon Connect public APIs
log to CloudTrail; for more information, see [Log Amazon Connect API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md"). Review and automate actions based on
CloudTrail logs.

We recommend Amazon S3 for long-term retention and archiving of log data, especially for
organizations with compliance programs that require log data to be auditable in its
native format. After log data is in an Amazon S3 bucket, define lifecycle rules to
automatically enforce retention policies and move these objects to other, cost-effective
storage classes, such as Amazon S3 Standard - Infrequent Access (Standard - IA) or
Amazon Glacier.

The AWS Cloud provides flexible infrastructure and tools to support both
sophisticated partner offerings and self-managed centralized-logging solutions. This
includes solutions such as Amazon OpenSearch Service and Amazon CloudWatch Logs.

You can implement fraud detection and prevention for incoming contacts by customizing
Amazon Connect flows per your requirements. For example, you can check incoming contacts against
previous contact activity in Dynamo DB and then take actions such as disconnecting a
contact who is on a deny list.

## Amazon Connect Chat security best practices

When you integrate with the Amazon Connect Participant Service directly (or use the Amazon Connect Chat
Java Script library) and use WebSocket or streaming endpoints to receive messages for
your frontend applications or websites, you must protect your application from DOM-based
XSS (cross-site scripting) attacks.

The following security recommendations can help safeguard against XSS attacks:

- Implement proper output encoding to help prevent malicious scripts from
  executing.
- Do not mutate DOM directly. For example, don't use `innerHTML` to
  render chat response contents. It might contain malicious Javascript code that
  can lead to an XSS attack. Use frontend libraries like React to escape and
  sanitize any executable code included in the chat response.
- Implement a Content Security Policy (CSP) to restrict the sources from which
  your application can load scripts, styles, and other resources. This adds an
  extra layer of protection.

## Amazon Connect WebRTC security best practices

For both WebRTC and chat contacts, participants are issued a Participant Token, which
is a bearer token that uniquely identifies them within a contact session. Because
possession of this token grants access, its exposure can lead to impersonation attacks.
Therefore, protecting this token is critical.

The following security recommendations can help safeguard against impersonation attacks:

- **Authenticate users before token issuance**. Ensure that robust authentication and authorization checks are performed before vending a participant token to any client or external service.
- **Minimize token exposure**. Do not log participant tokens or embed them in URLs. Use secure transport (HTTPS/TLS) for all token exchanges..
- **Respond to token leaks quickly**. If a token leak is detected, immediately terminate or stop the associated contact to prevent unauthorized access.
- **Use least privilege principles**. Limit token lifespan wherever possible, ensuring tokens are valid only for the duration necessary.
- **Monitor and audit**. Track token usage and access patterns to detect anomalies or potential abuse.

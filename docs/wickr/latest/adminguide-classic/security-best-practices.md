This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Security best practices for AWS Wickr

Wickr provides a number of security features to consider as you develop and implement
your own security policies. The following best practices are general guidelines and don’t
represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

To prevent potential security events associated with your use of Wickr, follow these
best practices:

- Implement least privilege access and create specific roles to be used for
  Wickr actions. Use IAM templates to create a
  role. For more information, see [AWS managed policies for AWS Wickr](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
- Access the AWS Management Console for Wickr by authenticating to the AWS Management Console first. Don't
  share your personal console credentials. Anyone on the internet can browse to the
  console, but they can't sign in or start a session unless they have valid
  credentials to the console.

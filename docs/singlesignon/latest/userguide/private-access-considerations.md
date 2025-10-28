# Considerations for AWS Management Console Private

Access

If your organization uses the AWS Management Console Private Access feature, you should consider how
your users will sign-in to IAM Identity Center.

A VPC endpoint policy restricts sign-in to the management
console, which prevents your users from signing in to AWS accounts they are not authorized
to access. For more information, see [AWS Management Console Private
Access](../../../awsconsolehelpdocs/latest/gsg/console-private-access.md "../../../awsconsolehelpdocs/latest/gsg/console-private-access.md") in the _AWS Management Console Getting Started Guide_.

**VPC endpoints block sign-in to the IAM Identity Center**

It's important to note that using VPC endpoints will block sign-in to the IAM Identity Center. This
happens when a user is already logged into the management console through the VPC endpoint. To
ensure your users can continue to sign-in to IAM Identity Center, they must use the public endpoint for
AWS sign-in, rather than the VPC endpoint.

# Overview of AWS Management Console Private

Access security controls

## Account restrictions on the AWS Management Console

from your network

AWS Management Console Private Access is useful in scenarios when you want to limit access to the
AWS Management Console from your network only to a specified set of known AWS accounts in your
organization. By doing so, you can prevent users from signing in to unexpected
AWS accounts from within your network. You can implement these controls using the
AWS Management Console VPC endpoint policy. For more information, see [Implementing service control
policies and VPC endpoint policies](implementing-console-private-access-policies.md "implementing-console-private-access-policies.md").

## Connectivity from your network to the

internet

Internet connectivity from your network is still required to access assets used by the
AWS Management Console, such as static content (JavaScript, CSS, images), and all AWS services not
enabled by [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md"). For a list of the top-level domains used by the AWS Management Console, see
[Troubleshooting](troubleshooting.md "troubleshooting.md").

###### Note

Currently, AWS Management Console Private Access doesn't support endpoints such as
`status.aws.amazon.com`, `health.aws.amazon.com`, and
`docs.aws.amazon.com`. You will need to route these domains to the public
internet.

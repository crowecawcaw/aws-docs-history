# Resource-based policy

examples for AWS Elemental MediaTailor

To learn how to attach a resource-based policy to a channel, see **[Create a channel using the MediaTailor console](channel-assembly-creating-channels.md "channel-assembly-creating-channels.md")**.

###### Topics

- [Anonymous
  access](#security_iam_resource-based-policy-examples-anonymous-access "#security_iam_resource-based-policy-examples-anonymous-access")
- [Cross-account access](#security_iam_resource-based-policy-examples-cross-account-access "#security_iam_resource-based-policy-examples-cross-account-access")

## Anonymous

access

Consider the following `Allow` policy. With this policy in effect, MediaTailor
allows anonymous access to the `mediatailor:GetManifest` action on the
channel resource in the policy. This occurs where `region` is
the AWS Region, `accountID` is your AWS account ID, and
`channelName` is the name of the channel resource.

## Cross-account access

Consider the following `Allow` policy. With this policy in effect, MediaTailor
allows the `mediatailor:GetManifest` action on the channel resource in the
policy, across accounts. This occurs where `region` is the
AWS Region, `accountID` is your AWS account ID, and
`channelName` is the name of the channel resource.

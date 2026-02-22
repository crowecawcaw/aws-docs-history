# Troubleshooting

Consult this section to find solutions to common problems with the AWS Management Console.

You can also diagnose and troubleshoot common errors for some AWS services using Amazon Q Developer. For more information,
see [Diagnose common errors in the console with Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/diagnose-console-errors.md "../../../amazonq/latest/qdeveloper-ug/diagnose-console-errors.md") in the _Amazon Q Developer User Guide_.

###### Topics

- [The page isn't loading properly](#page-not-loading "#page-not-loading")
- [My browser displays an 'access denied' error when connecting to
  the AWS Management Console](#access-denied-error "#access-denied-error")
- [My browser displays timeout errors when connecting to
  the AWS Management Console](#regional-outage "#regional-outage")
- [I want to change the language of the AWS Management Console
  but I can't find the language selection menu at the bottom of the page](#change-my-language "#change-my-language")

## The page isn't loading properly

- If this problem only occurs occasionally, check your internet connection.
  Try to connect through a different network, or with or without a VPN, or try using a different web browser.
- If all impacted users are from the same team, it may be a privacy browser extension or security firewall issue. Privacy browser extensions and security firewalls
  can block access to the domains used by the AWS Management Console. Try turning off these
  extensions or adjusting firewall settings. To verify issues with your
  connection, open your browser developer tools ([Chrome](https://developer.chrome.com/docs/devtools/open/ "https://developer.chrome.com/docs/devtools/open/"),
  [Firefox](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/index.html "https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/index.html")) and inspect the errors in the
  **Console** tab. The AWS Management Console uses domains' suffixes
  including the
  following list. This list is not exhaustive and can change with time. These domains' suffixes aren't used exclusively by AWS.
  - .a2z.com
  - .amazon.com
  - .amazonaws.com
  - .aws
  - .aws.com
  - .aws.dev
  - .awscloud.com
  - .awsplayer.com
  - .awsstatic.com
  - .cloudfront.net
  - .live-video.net

###### Warning

Since July 31, 2022, AWS no longer supports Internet Explorer 11. We recommend that you use the AWS Management Console with other supported
browsers. For more information, see [AWS News Blog](https://aws.amazon.com/jp/blogs/aws/heads-up-aws-support-for-internet-explorer-11-is-ending/ "https://aws.amazon.com/jp/blogs/aws/heads-up-aws-support-for-internet-explorer-11-is-ending/").

## My browser displays an 'access denied' error when connecting to

the AWS Management Console

Recent changes made to the console might affect your access if all of the following conditions are met:

- You access AWS Management Console from a network that is configured to reach AWS service endpoints through VPC endpoints.
- You restrict access to AWS services by either using `aws:SourceIp` or `aws:SourceVpc` global condition key in your IAM policies.

We recommend you review the IAM policies that contain the `aws:SourceIp` or `aws:SourceVpc` global condition key. Apply both `aws:SourceIp` and `aws:SourceVpc` where applicable.

Some AWS Management Console features use dual-stack domains that support both IPv4 and IPv6 connections. If your IAM policy restricts access using `aws:SourceIp` with only IPv4 CIDR blocks, requests might fail when your operating system prefers IPv6 connections (or vice versa). To avoid this, include both IPv4 and IPv6 CIDR blocks in your `aws:SourceIp` condition. For more information, see [aws:SourceIp](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip") in the _AWS Identity and Access Management User Guide_.

You can also onboard to the AWS Management Console Private Access feature to access the AWS Management Console through a VPC endpoint and use `aws:SourceVpc` conditions in your policies. For more information, see the following:

- [AWS Management Console Private Access](console-private-access.md "console-private-access.md")
- [How AWS Management Console Private Access works with
  aws:SourceVpc](identity-other-policy-types.md#location-identity "identity-other-policy-types.md#location-identity")
- [Supported AWS global condition context
  keys](identity-other-policy-types.md#supported-global-condition-keys "identity-other-policy-types.md#supported-global-condition-keys")

## My browser displays timeout errors when connecting to

the AWS Management Console

If there's a service outage in your default AWS Region, your browser might display a
**`504 Gateway Timeout`** error when trying to connect to the
AWS Management Console. To log in to the AWS Management Console from a different Region, specify an alternate
Regional
endpoint in the URL. For example, if there's an outage in the `us-west-1` (N.
California)
Region,
to access the `us-west-2` (Oregon) Region use the following template:

```
https://`region`.console.aws.amazon.com
```

For more information, see [AWS Management Console service endpoints](../../../general/latest/gr/mgmt-console.md "../../../general/latest/gr/mgmt-console.md") in
the _AWS General Reference_.

To view the status of all AWS services, including the AWS Management Console, see [AWS Health Dashboard](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status").

## I want to change the language of the AWS Management Console

but I can't find the language selection menu at the bottom of the page

The language selection menu has moved to the new Unified Settings page. To
change the language of the AWS Management Console, [navigate to the Unified Settings page](unified-settings.md "unified-settings.md"),
and then choose the language for the console.

For more information, see [Changing the language of the
AWS Management Console](change-language.md "change-language.md").

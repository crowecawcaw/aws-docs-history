# Chatting about your network security

|                                                                             |
| --------------------------------------------------------------------------- |
| Chatting about network security is in preview,<br>and is subject to change. |

Amazon Q can help you analyze your network security configurations, identify missing or
misconfigured AWS network security services, and provide recommendations for a stronger
network security posture. This helps you understand network security findings, implement
remediation steps, and follow security best practices without interrupting your
workflow.

When you ask Amazon Q about your network security, its responses include specific
information about your resources, related security findings, and detailed remediation
instructions as well as links to learn more in the AWS Management Console.

For more information about network security analysis with Amazon Q, see [Get insights with Amazon Q
Developer](../../../waf/latest/developerguide/nsd-security-insights.md "../../../waf/latest/developerguide/nsd-security-insights.md") in the _AWS Shield network security director Developer Guide_.

## Prerequisites

You can chat about your AWS network security in the AWS Management Console and in [configured chat applications](q-in-chat-applications.md "q-in-chat-applications.md").

For Amazon Q to answer questions about your network security, the following
prerequisites must be met.

### Add permissions

To chat about your network security, your IAM identity must have permissions to
chat with Amazon Q. For an IAM policy that grants the required
permissions, see [Allow users to chat with Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-chat "id-based-policy-examples-users.md#id-based-policy-examples-allow-chat").

### Enable AWS Shield network security director

To chat about your network security with Amazon Q, you must enable AWS Shield
network security director in your AWS account. To enable AWS Shield
network security director:

1. Open the AWS Shield network security director console at [https://console.aws.amazon.com/nsd/](https://console.aws.amazon.com/nsd/ "https://console.aws.amazon.com/nsd/").
2. Follow the setup instructions to enable the service.
3. Run a scan to collect security information about your resources.

## Example questions

Following are example questions about network security that you can ask Amazon Q:

- Identify my top network security findings
- Summarize the network security of my environment
- Are my systems at risk of DDoS attacks?
- How can I improve my network security?
- Do I have any resources without WAF protection?
- Which resources are not protected from common web vulnerabilities?
- What are the common network security issues on my EC2 instances?
- Do I have any WAF WebACLs that aren’t protecting anything?

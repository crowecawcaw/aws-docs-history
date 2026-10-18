

# Chatting about your network security
<a name="chat-network-security"></a>

**Note**  
The public preview of this capability has now ended and is no longer accessible. For more information about this capability, contact [AWS Support](https://aws.amazon.com/premiumsupport) or an [AWS Sales Representative](https://aws.amazon.com/contact-us/sales-support/).

Amazon Q can help you analyze your network security configurations, identify missing or misconfigured AWS network security services, and provide recommendations for a stronger network security posture. This helps you understand network security findings, implement remediation steps, and follow security best practices without interrupting your workflow.

When you ask Amazon Q about your network security, its responses include specific information about your resources, related security findings, and detailed remediation instructions as well as links to learn more in the AWS Management Console.

## Prerequisites
<a name="chat-network-security-prereqs"></a>

You can chat about your AWS network security in the AWS Management Console and in [configured chat applications](q-in-chat-applications.md).

For Amazon Q to answer questions about your network security, the following prerequisites must be met.

### Add permissions
<a name="add-permissions-chat-network-security"></a>

To chat about your network security, your IAM identity must have permissions to chat with Amazon Q. For an IAM policy that grants the required permissions, see [Allow users to chat with Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-chat).

## Example questions
<a name="example-questions-network-security"></a>

Following are example questions about network security that you can ask Amazon Q:
+ Identify my top network security findings
+ Summarize the network security of my environment
+ Are my systems at risk of DDoS attacks?
+ How can I improve my network security?
+ Do I have any resources without WAF protection?
+ Which resources are not protected from common web vulnerabilities?
+ What are the common network security issues on my EC2 instances?
+ Do I have any WAF WebACLs that aren’t protecting anything?
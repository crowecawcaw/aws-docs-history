

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Troubleshooting and support for AWS Wickr
<a name="troubleshoot"></a>

The following procedures and tips can help you troubleshoot issues with AWS Wickr. If you cannot resolve the issue using the steps in this guide, open a support case in the [AWS Support Center](https://console.aws.amazon.com/support/home).

**Topics**
+ [Support responsibilities](#support-model)
+ [Troubleshoot general issues for AWS Wickr](troubleshoot-general.md)
+ [Troubleshoot login and registration issues](troubleshoot-enduser.md)
+ [Troubleshoot SSO and authentication issues](troubleshoot-sso.md)
+ [Troubleshoot identity and access issues](troubleshoot-iam.md)
+ [Troubleshoot network and connectivity issues](troubleshoot-network.md)

## Support responsibilities
<a name="support-model"></a>

AWS Wickr follows a shared-responsibility support model. As a network administrator, you own first-line support for your end users; AWS supports the underlying service.


**AWS Wickr support responsibilities**  

| Support level | Owner | Responsibilities | 
| --- | --- | --- | 
| Self-service | End users | For troubleshooting steps, see the [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/troubleshoot.html), also available from the Support option in the client. Escalate unresolved issues to the network administrator. | 
| First-line support | Network administrators | Own initial triage and day-to-day support for your end users, including user management, network configuration, security group configuration, and bot management. Plan a support team and an internal help channel sized to your deployment before rollout. | 
| Service support | AWS Support | Handles service issues. Open a case in the [AWS Support Center](https://console.aws.amazon.com/support/home) when an issue can't be resolved through administrator troubleshooting. | 

### Best practices for supporting your end users
<a name="support-best-practices"></a>

Use the following best practices to stand up first-line support for your Wickr deployment.
+ **Designate administrators and a support team** – Size your team to your deployment. As a planning starting point, plan for roughly one support contact per 15,000–20,000 end users, adjusted for your ticket volume and onboarding peaks. Plan for administration at scale. Grant the AWS Identity and Access Management (IAM) permissions required to access the AWS Support Center to the administrators and support staff you designate, so they can open and manage cases. For more information, see [Getting started with AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html).
+ **Track issues in a ticketing system** – Use a ticketing or IT service management (ITSM) system, such as Jira, ServiceNow, or Zendesk, to capture and route end-user issues.
+ **Automate support with a Wickr bot** – Connect a bot to your ticketing system with the AWS Wickr Bot API so that end users can open requests without leaving Wickr. For more information, see the [AWS Wickr Bots and Integrations Guide](https://docs.aws.amazon.com/wickr/latest/wickrio/bot-overview.html).
+ **Give end users one place to get help** – Provide a dedicated help channel or support email address, and publicize it so that end users know where to go before contacting AWS.
+ **Send a welcome communication** – When you invite end users, send a welcome email that explains how to sign in, where to find help, and who to contact.
+ **Build a network of power users** – Identify champions across teams to provide peer-to-peer support and drive adoption.
+ **Point end users to self-service first** – Direct end users to the troubleshooting topics in the [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/troubleshoot.html) before they escalate. The **Support** option in the client links to the same topics.
+ **Escalate unresolved issues to AWS** – When first-line support can't resolve a service- or platform-level issue, open a case in the [AWS Support Center](https://console.aws.amazon.com/support/home).
+ **Get expert help deploying at scale** – For hands-on help planning, deploying, and supporting Wickr across a large organization, engage [AWS Professional Services](https://aws.amazon.com/professional-services/).
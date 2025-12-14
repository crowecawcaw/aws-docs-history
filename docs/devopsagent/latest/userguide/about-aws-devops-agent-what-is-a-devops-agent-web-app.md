# What is a DevOps Agent Web App?

AWS DevOps Agent uses a dual-console architecture that separates administrative functions from day-to-day operational activities. This design enables administrators to configure the service while operations teams focus on incident response and prevention.

## Consoles

AWS DevOps Agent provides two distinct interfaces:

- **AWS Management Console** – Administrators use the AWS Management Console to set up and manage AWS DevOps Agent. In this console, you can [Creating an Agent Space](getting-started-with-aws-devops-agent-creating-an-agent-space.md "getting-started-with-aws-devops-agent-creating-an-agent-space.md") connect AWS services and third-party tools, and manage access permissions for your organization.
- **DevOps Agent web app -** Operations teams use DevOps Agent Space web apps for daily incident response activities. This standalone application provides an interface where on-call engineers can launch investigations, interact with the agent through natural language chat, view application topologies, and review incident prevention recommendations.

## Web app capabilities

The DevOps Agent web app provides the following primary capabilities:

- **Incident Response –** The page is where you create and track incident investigations as well as generate mitigation plans to resolve incidents.
- **Incident Prevention –** Found in the Prevention tab, this is where you will find recommendations to improve your observability posture, delivery processes, and infrastructure architecture to prevent future incidents.
- **DevOps Center –** The DevOps Center tab provides an interactive visual representation of the account resources and their relationships across all of the resources in the connected accounts. You can view the topology with different levels of detail.
- **Runbooks** – Natural language explanations of your company’s in-house processes, high-level application architectures, and desired agent behaviors

## Authentication

AWS DevOps Agent supports flexible authentication methods to accommodate different organizational requirements:

- **IAM Identity Center integration (User access)** – Organizations can use AWS Identity Center (IAM Identity Center) to centrally manage user access to the DevOps Agent Space web apps. IAM Identity Center can federate with external identity providers through standard OIDC and SAML protocols, including providers like Okta, Ping Identity, and Microsoft Entra ID. This method supports multi-factor authentication from your identity provider.
- **IAM authentication link (Admin access)** – An alternative method provides direct access to the web app from the AWS Management Console using your existing console session. This option is useful This option is useful before implementing full Identity Center integration, but sessions are limited to 10 minutes.

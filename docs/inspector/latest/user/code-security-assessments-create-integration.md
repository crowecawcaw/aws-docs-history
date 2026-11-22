

# Creating an integration between Amazon Inspector your code repository

 This section includes topics that describe how to create an integration between Amazon Inspector and your code repository. When you create an integration, all code repositories are listed as projects in the Amazon Inspector console on the **Code Security** page. Other topics in this section describe how to access your integrations and projects. 

 Code Security only imports up to 100,000 projects, and only the default branch for each repository is monitored. A project can be associated with a maximum of three default scan configurations. 

 Code Security only supports a maximum of 100 integrations per account. Code Security integrations have no concept of the delegated administrator account/member account relationship. 

 To avoid encountering restrictions, we recommend not using the same host for an integration more than once. 

 Integrations with GitHub SaaS require public internet access. GitHub Enterprise Server and GitLab Self-Managed support both public internet access and private network connectivity through VPC configurations or AWS CodeConnections. For configuration details, see [Creating an integration between Amazon Inspector and GitHub Enterprise Server](code-security-assessments-connect-github-enterprise-server.md) and [Creating an integration between Amazon Inspector and GitLab Self-Managed](code-security-assessments-connect-gitlab.md). 

**Important**  
 Third-party integrations might be temporarily or permanently disabled without prior notice for any reason, such as to address security concerns. 
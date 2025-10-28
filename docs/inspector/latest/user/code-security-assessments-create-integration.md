# Creating an integration between Amazon Inspector your code repository

This section includes topics that describe how to create an integration between Amazon Inspector and your code repository.
When you create an integration, all code repositories are listed as projects in the Amazon Inspector console on the **Code Security** page.
Other topics in this section describe how to access your integrations and projects.

Code Security only imports up to 100,000 projects, and only the default branch for each repository is monitored.
A project can be associated with a maximum of three default scan configurations.

Code Security only supports a maximum of 100 integrations per account.
Code Security integrations have no concept of the delegated administrator account/member account relationship.

To avoid encountering restrictions, we recommend not using the same host for an integration more than once.

Integrations with GitHub SaaS, GitHub Enterprise Cloud, and GitHub Enterprise Server require public internet access.

###### Important

Third-party integrations might be temporarily or permanently disabled without prior notice for any reason, such as to address security concerns.

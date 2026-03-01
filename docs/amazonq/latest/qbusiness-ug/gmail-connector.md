# Connecting Gmail to Amazon Q Business

With Amazon Q Business, you can connect your Gmail enterprise email
system to unlock valuable organizational knowledge stored in email communications. When you
connect Gmail to Amazon Q Business, your users can search and get
answers from email content and conversations directly through the Amazon Q web
experience.

You can connect your Gmail instance to Amazon Q Business using either the AWS Management Console or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API. This connection enables your organization to leverage email-based knowledge for improved decision-making and faster information discovery.

###### Topics

- [Gmail connector versions](gmail-versions.md "gmail-versions.md")
- [Gmail connector overview](gmail-overview.md "gmail-overview.md")
- [Prerequisites for connecting Amazon Q Business to Gmail](gmail-prereqs.md "gmail-prereqs.md")
- [Connecting Amazon Q Business to Gmail using the latest connector (Console)](gmail-console-new.md "gmail-console-new.md")
- [Connecting Amazon Q Business to Gmail using the legacy connector (Console)](gmail-console-original.md "gmail-console-original.md")
- [Connecting Amazon Q Business to Gmail using the new connector (API)](gmail-new-api.md "gmail-new-api.md")
- [Connecting Amazon Q Business to Gmail using the original connector (API)](gmail-original-api.md "gmail-original-api.md")
- [How Amazon Q Business connector crawls Gmail ACLs](gmail-user-management.md "gmail-user-management.md")
- [Gmail data source connector field mappings](gmail-field-mappings.md "gmail-field-mappings.md")
- [IAM role for Amazon Q Business Gmail connector](gmail-iam-role.md "gmail-iam-role.md")
- [Understand error codes in the Amazon Q Business Gmail connector](gmail-error-codes.md "gmail-error-codes.md")

**Learn more**

- For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](create-application.md "create-application.md").
- For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](create-application-iam.md "create-application-iam.md").
- For an overview of connector features, see [Data source connector concepts](connector-concepts.md "connector-concepts.md").
- For information about connector configuration best practices, see [Connector configuration best practices](connector-best-practices.md "connector-best-practices.md").

###### Note

**ACL behavior by connector version:**

- **New connector:** ACL and identity crawling is automatically enabled and cannot be disabled. No manual configuration is required.
- **Original connector:** ACL and identity crawling can be manually configured during setup.

###### Note

**Original connector only:** Field mappings are only available when using the original Gmail connector. The new connector uses optimized default field mappings that cannot be customized.

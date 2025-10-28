# Using Lake Formation application integration

Lake Formation allows third-party services to integrate with Lake Formation and get temporary access to Amazon S3
data on behalf of their users by using [GetTemporaryGlueTableCredentials](../APIReference/API_GetTemporaryGlueTableCredentials.md "../APIReference/API_GetTemporaryGlueTableCredentials.md") and [GetTemporaryGluePartitionCredentials](../APIReference/API_GetTemporaryGluePartitionCredentials.md "../APIReference/API_GetTemporaryGluePartitionCredentials.md") operations. This allows third-party services
to use the same authorization and credential vending feature that the rest of AWS analytics
services use. This section describes how to use these API operations to integrate a
third-party query engine with Lake Formation.

These API operations are disabled by default. There are two options to authorize Lake Formation to
integrate applications:

- Configure IAM session tags that are validated every time the application integration API
  operations are called

For more information, see [Enabling permissions for a third-party query
engine to call application integration API operations](permitting-third-party-call.md "permitting-third-party-call.md").

- Enable the option that **Allows external engines to access data in Amazon S3 locations with full table access**

This option allows query engines and applications to get credentials without IAM
session tags if the user has full table access. It provides query engines and applications
performance benefits as well as simplifies data access. Amazon EMR on Amazon EC2 is able to
leverage this setting.

For more information, see [Application integration for full table
access](full-table-credential-vending.md "full-table-credential-vending.md") .

###### Topics

- [How Lake Formation application integration works](how-vending-works.md "how-vending-works.md")
- [Roles and responsibilities in Lake Formation application
  integration](roles-and-responsibilities.md "roles-and-responsibilities.md")
- [Lake Formation workflow for application integration API
  operations](api-overview.md "api-overview.md")
- [Registering a third-party query engine](register-query-engine.md "register-query-engine.md")
- [Enabling permissions for a third-party query
  engine to call application integration API operations](permitting-third-party-call.md "permitting-third-party-call.md")
- [Application integration for full table
  access](full-table-credential-vending.md "full-table-credential-vending.md")

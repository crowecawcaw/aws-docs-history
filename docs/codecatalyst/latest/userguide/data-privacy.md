Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Data privacy in Amazon CodeCatalyst

CodeCatalyst collects aggregate information in IAM Identity Center. CodeCatalyst uses this aggregate data to provide
access to spaces and projects in CodeCatalyst. The following aggregate information is
collected:

- User's full name
- User's email
- User's user name
  CodeCatalyst data is automatically encrypted at rest. No customer action is required. When a user,
  identity center, or space is deleted, CodeCatalyst deletes customer data within 24 hours.

CodeCatalyst uses AWS-owned AWS KMS keys. CodeCatalyst does not support encryption at rest using
customer managed KMS keys for the identity attributes retrieved from IAM Identity Center.

For more information about AWS KMS keys, see the user documentation at [AWS KMS keys](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md").

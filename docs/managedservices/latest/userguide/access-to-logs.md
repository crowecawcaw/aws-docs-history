# Accessing your logs

To access your logs, ensure that you have one of the required IAM roles and are in your AMS account. Then navigate to the directory shown.

Multi-Account Landing Zone (MALZ)
Provides five default IAM roles, each of which allow access to all logs
within your account (all are prefaced with `AWSManagedServices`):

- `AdminRole`
- `CaseRole`
- `ChangeManagementRole`
- `ReadOnlyRole`
- `SecurityOpsRole`

Access to these roles is configured via federation, with each role being mapped to a group within your Active Directory domain.

To learn more about these roles, see [IAM user role in AMS](defaults-user-role.md "defaults-user-role.md") .

Single-Account Landing Zone (SALZ)
The default `Customer_ReadOnly_Role` for AMS single-account landing zone allows your
access to all logs within your account. Access to the logs is controlled using AWS Identity and Access
Management (IAM) roles mapped to Active Directory groups.

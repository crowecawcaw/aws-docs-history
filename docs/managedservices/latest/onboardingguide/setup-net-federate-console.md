# Configuring federation to the AMS console (MALZ)

The IAM roles and SAML identity provider (Trusted Entity) detailed in the following table have been provisioned as part of
the AMS infrastructure. These roles allow you to audit and view the AMS core accounts.

| Role                                   | Permissions                                                                                                      |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| AWSManagedServicesReadOnlyRole         | Allows you to view the AMS infrastructure in the core accounts.                                                  |
| AWSManagedServicesCaseRole             | Allows you to view the resources in your new application account and file AMS incidents and service requests.    |
| AWSManagedServicesChangeManagementRole | Allows you to view the AMS infrastructure in the core accounts, file AWS Support tickets, and request some RFCs. |

For the full list of the roles available under different accounts see
[IAM user role in AMS](defaults-user-role.md "defaults-user-role.md") .

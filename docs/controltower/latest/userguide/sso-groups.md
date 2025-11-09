# IAM Identity Center Groups for AWS Control Tower

AWS Control Tower offers preconfigured groups to organize users that perform specific tasks in
your accounts. You can add users and assign them to these groups directly in IAM Identity Center.
Doing so matches permission sets to users in groups within your accounts. For the latest
guidance and best practices on configuring your groups, see [Best practices](../../../singlesignon/latest/userguide/delegated-admin.md#delegated-admin-best-practices "../../../singlesignon/latest/userguide/delegated-admin.md#delegated-admin-best-practices") in the _IAM Identity Center User Guide_.

The following groups are created when you set up your landing zone.

| AWSAccountFactory  | Account                        | Permission sets                                                                             | Description |
| ------------------ | ------------------------------ | ------------------------------------------------------------------------------------------- | ----------- |
| Management account | AWSServiceCatalogEndUserAccess | This group is only used in this account to provision new accounts<br>using Account Factory. |

| AWSServiceCatalogAdmins | Account                          | Permission sets                                                                                                                                                                                              | Description |
| ----------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| Management account      | AWSServiceCatalogAdminFullAccess | This group is only used in this account to make administrative<br>changes to Account Factory. Users in this group can't provision new accounts<br>unless they're also in the **AWSAccountFactory**<br>group. |

| AWSControlTowerAdmins | Account                    | Permission sets                                                                                             | Description |
| --------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| Management account    | AWSAdministratorAccess     | Users of this group in this account are the only ones that have<br>access to the AWS Control Tower console. |
| Log archive account   | AWSAdministratorAccess     | Users have administrator access in this account.                                                            |
| Audit account         | AWSAdministratorAccess     | Users have administrator access in this account.                                                            |
| Member accounts       | AWSOrganizationsFullAccess | Users have full access to Organizations in this account.                                                    |

| AWSSecurityAuditPowerUsers | Account            | Permission sets                                                                                                                                           | Description |
| -------------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Management account         | AWSPowerUserAccess | Users can perform application development tasks and can create and<br>configure resources and services that support AWS aware application<br>development. |
| Log archive account        | AWSPowerUserAccess | Users can perform application development tasks and can create and<br>configure resources and services that support AWS aware application<br>development. |
| Audit account              | AWSPowerUserAccess | Users can perform application development tasks and can create and<br>configure resources and services that support AWS aware application<br>development. |
| Member accounts            | AWSPowerUserAccess | Users can perform application development tasks and can create and<br>configure resources and services that support AWS aware application<br>development. |

| AWSSecurityAuditors | Account           | Permission sets                                                                   | Description |
| ------------------- | ----------------- | --------------------------------------------------------------------------------- | ----------- |
| Management account  | AWSReadOnlyAccess | Users have read-only access to all AWS services and resources in<br>this account. |
| Log archive account | AWSReadOnlyAccess | Users have read-only access to all AWS services and resources in<br>this account. |
| Audit account       | AWSReadOnlyAccess | Users have read-only access to all AWS services and resources in<br>this account. |
| Member accounts     | AWSReadOnlyAccess | Users have read-only access to all AWS services and resources in<br>this account. |

| AWSLogArchiveAdmins | Account                | Permission sets                                  | Description |
| ------------------- | ---------------------- | ------------------------------------------------ | ----------- |
| Log archive account | AWSAdministratorAccess | Users have administrator access in this account. |

| AWSLogArchiveViewers | Account           | Permission sets                                                                   | Description |
| -------------------- | ----------------- | --------------------------------------------------------------------------------- | ----------- |
| Log archive account  | AWSReadOnlyAccess | Users have read-only access to all AWS services and resources in<br>this account. |

| AWSAuditAccountAdmins | Account                | Permission sets                                  | Description |
| --------------------- | ---------------------- | ------------------------------------------------ | ----------- |
| Audit account         | AWSAdministratorAccess | Users have administrator access in this account. |

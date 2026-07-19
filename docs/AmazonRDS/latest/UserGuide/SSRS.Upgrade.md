# Upgrading from SSRS to PBIRS

When you upgrade an existing RDS DB instance running SSRS to SQL Server 2025, SSRS is
replaced by Power BI Report Server (PBIRS). To complete the transition, you must add the `PBIRS`
option to a SQL Server 2025 option group — either a new one or an existing one — and
associate it with your DB instance. For more information, see
[Turning on SSRS or PBIRS](SSRS.Enabling.md "SSRS.Enabling.md"). This transition
doesn't impact your existing reports. Your paginated reports (.rdl) and report
data sources are preserved and remain accessible through the PBIRS web portal after
the upgrade completes. The web portal endpoint remains the same after the upgrade.
Existing bookmarks and application integrations that reference the reporting URL
continue to work without modification.

After the upgrade, if you have any automation that uses the `rds_msbi_task`
stored procedure with SSRS task types such as `SSRS_GRANT_PORTAL_PERMISSION`
or `SSRS_REVOKE_PORTAL_PERMISSION` and the `@ssrs_group_or_username`
parameter, you must update it to use the equivalent PBIRS task types
`PBIRS_GRANT_PORTAL_PERMISSION` and `PBIRS_REVOKE_PORTAL_PERMISSION`
with the `@pbirs_group_or_username` parameter.

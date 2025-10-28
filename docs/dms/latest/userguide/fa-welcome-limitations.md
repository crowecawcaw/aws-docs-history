# Understanding DMS Fleet Advisor limitations

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service Fleet
Advisor. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet
Advisor console or AWS DMS Fleet Advisor resources. For more information, see [AWS DMS Fleet
Advisor end of support](dms_fleet.md "dms_fleet.md").

Limitations when using the DMS Fleet Advisor include the following:

- DMS Fleet Advisor generates one-to-one recommendations. For each source database,
  DMS Fleet Advisor determines a single target engine. DMS Fleet Advisor doesn't handle multitenant
  servers and doesn't provide recommendations for running several databases on a
  single target DB instance.
- DMS Fleet Advisor doesn't provide recommendations about available database version
  upgrades.
- DMS Fleet Advisor generates recommendations for up to 100 databases at one time.
- If you install DMS data collector, which is a Windows application, make sure
  that you also install .NET Framework 4.8 and PowerShell 6.0 and higher. For the
  hardware requirements, see [Installing a data
  collector](fa-data-collectors-install.md "fa-data-collectors-install.md").
- The DMS data collector requires permissions to run requests using LDAP protocol on your
  domain server.
- The DMS data collector requires the sudo SSH script running in Linux.
- The DMS data collector requires permissions to run remote PowerShell, Windows Management
  Instrumentation (WMI), WMI Query Language (WQL), and registry scripts in
  Windows.
- For MySQL and PostgreSQL, DMS Fleet Advisor can't collect performance metrics from your
  database. Instead, DMS Fleet Advisor collects the OS server metrics. Therefore, you can't
  generate recommendations based on utilization metrics for MySQL and PostgreSQL
  databases that run on Amazon RDS and Aurora.

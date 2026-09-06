

# SSRS and PBIRS log files
<a name="SSRS.Logs"></a>

You can list, view, and download SSRS and PBIRS log files. Log files follow a naming convention of ReportServerService\_{{timestamp}}.log and are located in the `D:\rdsdbdata\Log\SSRS` directory. (The `D:\rdsdbdata\Log` directory is also the parent directory for error logs and SQL Server Agent logs.)

For existing SSRS or PBIRS instances, you might need to restart the service to access report server logs. You can restart the SSRS service by updating the `SSRS` option, or the PBIRS service by updating the `PBIRS` option.

For more information, see [Working with Amazon RDS for Microsoft SQL Server logs](Appendix.SQLServer.CommonDBATasks.Logs.md).
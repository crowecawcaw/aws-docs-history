# Troubleshooting data collection issues related to SSL in AWS DMS

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service
Fleet Advisor. After May 20, 2026, you will no longer be able to access the
AWS DMS Fleet Advisor console or AWS DMS Fleet Advisor resources. For more
information, see [AWS DMS Fleet
Advisor end of support](dms_fleet.md "dms_fleet.md").

If you run into issues related to SSL with the DMS data collector, try the following actions.

**SSL errors**
Your database requires a secure SSL connection, and you have not turned on the
**Verify CA** and **Use SSL** options for the connection.
Turn on these options and ensure that your local OS has the Certificate Authority installed
that your database uses. For more information, see [Setting up SSL](fa-using-ssl.md#fa-using-ssl-setup "fa-using-ssl.md#fa-using-ssl-setup").

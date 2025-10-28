# Troublehsooting data collection issues

related to Windows webpage composer

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service
Fleet Advisor. After May 20, 2026, you will no longer be able to access the
AWS DMS Fleet Advisor console or AWS DMS Fleet Advisor resources. For more
information, see [AWS DMS Fleet
Advisor end of support](dms_fleet.md "dms_fleet.md").

If you run into issues related to Windows webpage composer with the DMS data collector, try the following actions.

**WPC: The network path was not found**

Turn on the inbound firewall rule "File and Printer Sharing
(SMB–In)". For example:

`* Inbound TCP/IP at local port 445`.

Also, start the Remote Registry service and set its start-up type to
Automatic.

**WPC: Access is denied**

Add the DMS data collector user to the
Performance Monitor Users or Administrators group.

**WPC: Category does not exist**

Run `loader /r` to rebuild the performance counter cache, then
restart your computer.

###### Note

For information about troubleshooting issues when migrating data using AWS Database Migration Service (AWS DMS), see
[Troubleshooting and diagnostic support](CHAP_Troubleshooting.md "CHAP_Troubleshooting.md").

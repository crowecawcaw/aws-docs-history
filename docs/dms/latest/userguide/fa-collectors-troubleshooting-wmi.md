# Troubleshooting data collection issues related to

Windows Management Instrumentation in AWS DMS

###### Important

End of support notice: On May 20, 2026, AWS will end support for AWS Database Migration Service
Fleet Advisor. After May 20, 2026, you will no longer be able to access the
AWS DMS Fleet Advisor console or AWS DMS Fleet Advisor resources. For more
information, see [AWS DMS Fleet
Advisor end of support](dms_fleet.md "dms_fleet.md").

If you run into issues related to Windows Management Instrumentation with the DMS data collector, try the following actions.

**WMI: The RPC server is unavailable. (Exception from HRESULT: 0x800706BA)**

Turn on the inbound firewall rule "Windows Management Instrumentation
(DCOM–In)". For example:

`* Inbound TCP/IP at local port 135`.

Also, turn on the inbound firewall rule "Windows Management
Instrumentation (WMI–In)". For example:

`* Inbound TCP/IP at local port 49152 – 65535`
for Windows Server 2008 and higher versions.

`* Inbound TCP/IP at local port 1025 – 5000` for Windows Server 2003 and lower versions.

**WMI: Access is denied. (Exception from HRESULT: 0x80070005 (E_ACCESSDENIED))**

Try the following:

- Add the DMS data collector user to the Windows group,
  Distributed COM Users or Administrators.
- Start the Windows Management Instrumentation service and set its
  start-up type to Automatic.
- Make sure that your DMS data collector user name is in the
  `\` format.

**WMI: Access denied**

Add Remote Enable permission to the DMS data collector user on
the root WMI namespace.

Use Advanced settings and make sure that permissions apply to "This
namespace and subnamespaces."

**WMI: The call was canceled by the message filter. (Exception from HRESULT: 0x80010002...)**

Restart the Windows Management Instrumentation service.

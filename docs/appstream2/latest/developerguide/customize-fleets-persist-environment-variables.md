# Persist Environment Variables in Amazon WorkSpaces Applications

Environment variables enable you to dynamically pass settings across applications. For
example, many engineering applications rely on environment variables to specify the IP
address or host name of a license server to locate and check out a license from that
server.

Follow the steps in these procedures to make environment variables available across
your fleet instances.

###### Note

The following instructions apply to Windows fleets only.

###### Contents

- [Change System Environment Variables](customize-fleets-system-environment-variables.md "customize-fleets-system-environment-variables.md")
- [Change User Environment Variables](customize-fleets-user-environment-variables.md "customize-fleets-user-environment-variables.md")
- [Create an Environment Variable That is Limited in Scope](customize-fleets-environment-variable-limited-scope.md "customize-fleets-environment-variable-limited-scope.md")

###### Note

If you are using Active Directory and Group Policy with WorkSpaces Applications, keep in mind that
streaming instances must be joined to an Active Directory domain to use Group Policy
for environment variables. For information about how to configure the Group Policy
**Environment Variable** preference item, see [Configure an Environment Variable Item](<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc772047(v=ws.11)> "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc772047(v=ws.11)") in the Microsoft
documentation.



This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Infrastructure 6.32 release
<a name="infra-release-notes-6.32"></a>

The following release notes include information for infrastructure release 6.32. For information on the release timeline, see [Change log](#infra-release-notes-6.32-change-log).

**Platform version**


|  |  | 
| --- | --- | 
| Infrastructure | 6.32.1 (1024) | 

**New features**:
+ Administrators can now toggle private IP restrictions at the superadmin level. Toggling the restrictions off facilitates ADFS and other SSO integration over private connections.
+  The downloaded config filename now matches the name in the admin dashboard.

**Improvements**:
+ Added a new port allowlist (TCP 8443). This port allowlist is needed for the new CALLING\_BASE\_URL environment variable in the Switchboard container, which facilitates internal communication between the messaging and calling servers.
+ Redirected the base URL to /admin
+  Added a “Removed” banner for former Wickr Me users
+ Updated ServerAPI to Node18
+ Proactively retry to reconnect web sockets in federation gateway on disconnect

## Change log
<a name="infra-release-notes-6.32-change-log"></a>

**Change log for 6.32 release and release notes**


| Change | Description | Date | 
| --- | --- | --- | 
| Final release | Final notes with Replicated build number Replicated build numbers are dependent on deployment model, KOTS (1024) or Native Scheduler (1882).  | February 12, 2024 | 
| Infrastructure update | Updates to address vulnerability scan results, new features, and patching | February 8, 2024 | 
| Initial release | Initial release of February release notes | February 5, 2024 | 
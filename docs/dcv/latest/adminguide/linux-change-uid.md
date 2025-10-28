# Linux Sessions fail to start after UID change

On a Linux host, changing the user ID (UID) of an user or using a different Active Directory
configuration that modifies the UID of an user, could cause failures in starting Amazon DCV sessions on
the host.

The issue is caused by the fact that the processes of the DCV session, which run with the new UID,
are not authorized to access files and folders that still retain the previous UID. In particular:

- The [log files](troubleshooting-logs.md "troubleshooting-logs.md") in the Amazon DCV log directory
- The home folder of the user
  The issue affects both console and virtual sessions.

To resolve this problem, ensure that the home folder of the user and the files it contains
have the correct UID and remove old [Amazon DCV log files](troubleshooting-logs.md "troubleshooting-logs.md")
that have the previous UID.

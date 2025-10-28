# Automatically update PBIS on Linux instances

AMS uses the Power Broker Identity Service (PBIS) module to join Linux instances into AMS-managed Active Directory.

AMS automatically updates PBIS on Linux instances.

**FAQ:**

When will AMS update PBIS?
AMS turns on PBIS update at reboot. If there is a new PBIS version available, then AMS attempts to install the new
version during the next instance reboot.

Can PBIS update be turned off?
You can turn off PBIS update at the instance or account levels:

- **Account level:** Create a parameter in the SSM parameter store: Name: `/ams/skip-pbis-update`, Value: `true` (any case).

###### Note

The instance profile must have permissions to read SSM parameters. If the flag is missing, then the default behavior is to run the update.

- **Instance level:**
  - Tag-based: Add the following tag to the instance: Key: `skip_pbis_update`, Value: `true` (any case).
  - Config file: Add the following flag to the `/opt/aws/ams/etc/ams.conf.d/state.ini` file: `skip_pbis_update = true.`

###### Note

Tag has a higher priority than the SSM parameter. You can turn off the PBIS update at the account level through the parameter, but
turn it it for a single (or multiple) instance(s) by adding a tag `Key:skip_pbis_update`, `Value: false`.

To configure any of the described options, follow the standard change management process in your AMS environment.

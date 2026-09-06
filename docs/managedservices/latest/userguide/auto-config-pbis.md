

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Automatically update PBIS on Linux instances
<a name="auto-config-pbis"></a>

AMS uses the Power Broker Identity Service (PBIS) module to join Linux instances into AMS-managed Active Directory.

AMS automatically updates PBIS on Linux instances.

**FAQ:**

When will AMS update PBIS?  
AMS turns on PBIS update at reboot. If there is a new PBIS version available, then AMS attempts to install the new version during the next instance reboot.

Can PBIS update be turned off?  
You can turn off PBIS update at the instance or account levels:  
+ **Account level:** Create a parameter in the SSM parameter store: Name: `/ams/skip-pbis-update`, Value: `true` (any case).
The instance profile must have permissions to read SSM parameters. If the flag is missing, then the default behavior is to run the update.
+ **Instance level:**
  + Tag-based: Add the following tag to the instance: Key: `skip_pbis_update`, Value: `true` (any case).
  + Config file: Add the following flag to the `/opt/aws/ams/etc/ams.conf.d/state.ini` file: `skip_pbis_update = true.`

**Note**  
Tag has a higher priority than the SSM parameter. You can turn off the PBIS update at the account level through the parameter, but turn it it for a single (or multiple) instance(s) by adding a tag `Key:skip_pbis_update`, `Value: false`.

To configure any of the described options, follow the standard change management process in your AMS environment.
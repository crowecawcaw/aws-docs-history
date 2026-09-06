

# Upgrading the DRSFA Client
<a name="upgrading-drsfa"></a>

Most DRSFA components upgrade automatically on execution. If the client displays a message requiring a manual upgrade, complete these steps:

1. Navigate to the directory where the original installation took place.

1. Download the DRSFA installer:

   ```
   wget https://drsfa-us-west-2.s3.us-west-2.amazonaws.com/drs_failback_automation_installer.sh
   ```
**Note**  
Verify the installer hash: `https://drsfa-hashes-us-west-2.s3.us-west-2.amazonaws.com/drs_failback_automation_installer.sh.sha512`

1. Run the installer:

   ```
   bash drs_failback_automation_installer.sh
   ```

1. Remove the installer:

   ```
   rm drs_failback_automation_installer.sh
   ```
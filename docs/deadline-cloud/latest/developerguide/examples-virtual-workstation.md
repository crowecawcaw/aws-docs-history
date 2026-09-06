

# Set up a virtual workstation for Deadline Cloud with a script
<a name="examples-virtual-workstation"></a>

The [virtual\_workstation](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/utility_scripts/virtual_workstation) scripts on the GitHub website turn a fresh Linux or Windows workstation into a Deadline Cloud submission machine. An artist who logs in finds Blender and the Deadline Cloud submitter installed, alongside Deadline Cloud monitor with a profile already configured. The only remaining step is signing in.

Each script takes the monitor URL as its argument and runs five steps. It validates the URL, installs Blender from the official archive, and installs the submitter with its silent installer. It then enables the submitter's Blender add-on, which the silent installer alone doesn't do. Finally, it installs the monitor and creates the profile non-interactively with `deadline-cloud-monitor create-profile`. Every download is verified against a published SHA-256 checksum. Blender stands in for whichever DCC you run; the README describes adapting the scripts to another DCC.

Run the Linux script as root on Ubuntu 22.04 with a desktop environment present:

```
sudo ./setup_workstation_linux.sh https://{{mystudio.us-west-2}}.deadlinecloud.amazonaws.com/
```

On Windows, run the PowerShell script in an elevated session as the artist's own account, because the monitor profile and Blender add-on preferences are stored for each user. The README covers running the scripts from EC2 user data or an image bake, the Ubuntu and browser requirements for monitor sign-in, and splitting the Windows script for studios where artists are standard users.

For scripts that configure the workers instead of workstations, see [Host configuration script examples for Deadline Cloud](examples-host-config.md).
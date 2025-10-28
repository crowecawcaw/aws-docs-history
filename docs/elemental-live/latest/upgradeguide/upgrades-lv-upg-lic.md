# Step F: Upgrade the license

The new version of the software might include a feature that is in an add-on package. Such
a feature requires a license. Therefore, you must obtain a new license and install it.

If you didn't purchase any add-on packages, skip this step.

###### To obtain the license for an Elemental Live appliance

- Contact your AWS Elemental sales person and provide the following information:
  - The names of the add-on packages you want. For a list of add-on packages, see
    [Purchasing an add-on
    package](../ug/ref-licenses-purchase.md "../ug/ref-licenses-purchase.md") in Elemental Live User Guide.
  - The hardware serial number or the MAC address of the node.

###### To obtain the license for qualified hardware or a VM

1.  Contact your AWS Elemental sales person and provide the following information:
    - The names of the add-on packages you want. For a list of add-on packages, see
      [Purchasing an add-on
      package](../ug/ref-licenses-purchase.md "../ug/ref-licenses-purchase.md") in Elemental Live User Guide.
    - The key file that you generated when you initially installed the software. The
      file name has this syntax:

    `activation_<hostname of the
 system>`.key``

    You can find this key in either of these places:

        + In the home directory of the hardware unit or VM
        + On your workstation. If you followed the recommendation that we gave in the
         installation procedure, this folder has a name such as
         `elemental_live_license_keys`.

2.  AWS Elemental provides you with a new license. The license has the following syntax:

`lic-download-<hostname>.tgz`

###### To install the license

You must unzip the license file, copy the unzipped file to the node that it applies to,
and restart the elemental service. Following are detailed instructions.

1. AWS Elemental provides you with a new version of the license. You receive this license in one
   of these ways:
   - Via email
   - Via your Salesforce account

2. Download the license file to your workstation. Then follow the procedure that applies
   to your browser to open the folder that contains the downloaded license files. Make a note
   of the folder where the license files are located.
3. Use a method such as SCP to move the license file (the .tgz file) from your
   workstation to the location on the Elemental Live hardware unit where your licenses are
   stored. This folder might have a name like `elemental_licenses`.

The new license will replace the current license because the two files have the same
name.

Make sure that you put the correct license on each hardware unit. The license only
works on a specific hardware unit. 4. Using an SSH client such as PuTTY, log in to the hardware unit with the elemental user
credentials.

You are logged in at the home directory (`/home/elemental`). 5. Navigate to the directory that contains the license file, and extract the
`.lic` files from the `.tgz` file. Place the
`.lic` files in these folders:

`/home/elemental`

`/opt/elemental_se`

The new license will replace the current license because the two files have the same
name. 6. Enter the following command to restart the Elemental Live service:

```
[elemental@hostname ~]$ sudo service elemental_se restart
```

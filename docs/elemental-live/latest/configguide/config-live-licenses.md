# Configuring licenses

Each Elemental Live node requires its own license. Without the license,
the service won't start.

There is one license (license file) for Elemental Live. The license
gives access to features of the product:

- Core features.
- Additional features that you have opted for by purchasing an
  add-on package.
  The procedure for deploying the license depends on your
  situation.

###### Topics

- [Licensing a new
  appliance](#config-live-lic-app "#config-live-lic-app")
- [Licensing qualified hardware or
  a VM](#config-live-lic-vm "#config-live-lic-vm")
- [Upgrading and licensing an
  add-on package](#config-live-lic-upgrade "#config-live-lic-upgrade")
- [Licensing an add-on package without
  upgrading](#config-live-lic-existing "#config-live-lic-existing")

## Licensing a new

appliance

You might be deploying a newly purchased AWS Elemental Live appliance.

There is nothing for you to do because the software is already
installed, along with the license (which covers the core features
and all add-on packages that your purchased). There are no licensing
steps to follow.

## Licensing qualified hardware or

a VM

You might be performing the initial deployment of AWS Elemental Live on
qualified hardware or a VM.

AWS Elemental sends you an email that contains an activation code for
each node. You must generate and activate a license (which covers
the core features and all add-on packages) as part of the procedure
to install the software. See [Set up licenses](../installguide/install-lv-ig-licensing.md "../installguide/install-lv-ig-licensing.md") (for qualified hardware) or [Set up licenses](../installguide/install-vm-lv-ig-licensing.md "../installguide/install-vm-lv-ig-licensing.md") (for a VM) in AWS Elemental Live Install Guide.

## Upgrading and licensing an

add-on package

You might want to upgrade the software in an existing deployment,
and enable an add-on package as part of the upgrade. AWS Elemental sends
you an email that includes a link to an upgraded version of the
license. You must download and activate the license as part of the
procedure to upgrade the software.

See [Upgrade the license](../upgradeguide/upgrades-lv-upg-lic.md "../upgradeguide/upgrades-lv-upg-lic.md") in the AWS Elemental Live Upgrade Guide.

## Licensing an add-on package without

upgrading

You might want to enable an add-on package in an existing
deployment, without needing to upgrade the AWS Elemental Live software.

###### To obtain the license for an Elemental Live appliance

1. Contact your AWS Elemental sales person and provide the
   following information:
   - The names of the add-on packages you want. For a
     list of add-on packages, see [Purchasing an add-on package](../ug/ref-licenses.md "../ug/ref-licenses.md") in Elemental Live
     User Guide.
   - The hardware serial number or the MAC address of
     the node.

2. AWS Elemental provides you with a new license. The license has
   the following syntax:

`lic-download-<hostname>.tgz`

###### To obtain the license for qualified hardware or a VM

1.  Contact your AWS Elemental sales person and provide the
    following information:
    - The names of the add-on packages you want. For a
      list of add-on packages, see [Purchasing an add-on package](../ug/ref-licenses.md "../ug/ref-licenses.md") in Elemental Live
      User Guide.
    - The key file that you generated when you initially
      installed the software. The file name has this
      syntax:

    `activation_<hostname of the
 system>`.key``

    You can find this key in either of these
    places:

        + In the home directory of the hardware unit
         or VM
        + On your workstation. If you followed the
         recommendation that we gave in the
         installation procedure, this folder has a
         name such as
         `elemental_live_license_keys`.

2.  AWS Elemental provides you with a new license. The license has
    the following syntax:

`lic-download-<hostname>.tgz`

###### To install the license

You must unzip the license file, copy the unzipped file to the
node that it applies to, and restart the elemental service.
Following are detailed instructions.

1. AWS Elemental provides you with a new version of the license. You
   receive this license in one of these ways:
   - Via email
   - Via your Salesforce account

2. Download the license file to your workstation. Then follow
   the procedure that applies to your browser to open the
   folder that contains the downloaded license files. Make a
   note of the folder where the license files are located.
3. Use a method such as SCP to move the license file (the
   .tgz file) from your workstation to the location on the
   Elemental Live hardware unit where your licenses are stored.
   This folder might have a name like
   `elemental_licenses`.

The new license will replace the current license because
the two files have the same name.

Make sure that you put the correct license on each
hardware unit. The license only works on a specific hardware
unit. 4. Using an SSH client such as PuTTY, log in to the hardware
unit with the elemental user credentials.

You are logged in at the home directory
(`/home/elemental`). 5. Navigate to the directory that contains the license file,
and extract the `.lic` files from the
`.tgz` file. Place the
`.lic` files in these folders:

`/home/elemental`

`/opt/elemental_se`

The new license will replace the current license because
the two files have the same name. 6. Enter the following command to restart the Elemental Live
service:

```
[elemental@hostname ~]$ sudo service elemental_se restart
```

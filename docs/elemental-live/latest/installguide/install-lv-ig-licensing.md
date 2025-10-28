# Step D: Set up

licenses

At this point, the software is installed but it is not yet
enabled.

You must now generate and install the license file on each
node.

The license generation procedure works as follows:

- You receive an email with activation codes, one for each
  instance of the product (Elemental Live) that you purchased.
  At each Elemental Live hardware unit, you use one activation
  code to generate a key file. The key file incorporates the
  specific activation code and the specific hostname of the
  hardware unit. The key file works only with this activation
  code's product (Elemental Live) and with this hardware unit.
- You copy the key file from the node to your workstation.
  At your workstation, you open the AWS Elemental Support Center
  console and generate a license using each key file. Like the
  key file used to generate it, the license file is valid only
  for this product (Elemental Live) and this specific hardware
  unit.
- After you generate the license file, you copy it to the
  hardware unit that it belongs to, and use the CLI to install
  the license.

###### Topics

- [Organize your
  activation codes](#install-live-license-retrieve "#install-live-license-retrieve")
- [Generate a key
  file](#install-live-license-generate "#install-live-license-generate")
- [Generate a
  license](#install-live-license-download "#install-live-license-download")
- [Install the
  license files](#install-live-license-install "#install-live-license-install")

## Organize your

activation codes

###### To organize the activation codes:

1. Locate the email you received from AWS Elemental. This email
   contains an activation code or codes, one for each
   Elemental Live software instance that you have purchased.
   The activation code looks like this:

`LVE-111-222-333`

If you didn't receive this email or have lost it,
contact AWS Elemental Support through the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter"). 2. If you have more than one activation code, each activation code specifies
the hardware configuration that the code applies to. For example, it
specifies that the code is for hardware that is comparable to an L820
appliance.

Identify the hardware unit that applies for each access code. For example,
identify the hardware unit (and its hostname) that is comparable to the L820
appliance. Make a note of the assignments. For example, you might assign as
follows:

`LVE-111-222-333` with the hardware unit that has the
hostname `SystemA`.

`LVE-111-222-444` with the hardware unit that has the
hostname `SystemB`.

## Generate a key

file

You must generate a key file using a utility that always
exists on the operating system of the hardware unit.

###### To generate a key file

Perform this step at each Elemental Live hardware
unit.

1. Using an SSH client such as PuTTY, log in to the
   hardware unit with the _elemental_
   user credentials.

You are logged in at the home directory
(`/elemental`). 2. Enter this command:

```
[elemental@hostname ~] **./keygen**
```

3. At the prompt, enter the activation code that belongs
   to this hardware unit. The following _key file_ is created in the
   home directory: `activation_<hostname of the
system>`.key``.

For example,
`activation_SystemA.key` 4. Copy the key file from the hardware unit to your workstation. We recommend
that you copy all the key files to a specific folder on your workstation.
Give the folder a suitable name such as
`elemental_live_license_keys`. Make a note of the
path because you will need it in the next step. 5. Repeat these steps for each Elemental Live hardware
unit. Make sure that you use a different activation code
on each hardware unit.

## Generate a

license

You must log on to the AWS Elemental Appliances & Software
console, and use the key file to generate a license.

###### Note

This procedure assumes that an administrator in your
organization has set you up as an AWS IAM user, with the
permissions that you need to generate licenses. For more
information, see [AWS Elemental
Appliances and Software Service Getting Started
Guide](https://amzn.to/AWSElementalSerGSG "https://amzn.to/AWSElementalSerGSG").

It also assumes that you have your IAM credentials (user
name and password). If you don't have these credentials,
speak to an administrator in your organization. AWS Elemental can't
provide you with these credentials.

###### To generate a license

Perform this step at your workstation.

1. Open the AWS Elemental Appliances & Software console at
   [https://console.aws.amazon.com/elemental-appliances-software/](https://console.aws.amazon.com/elemental-appliances-software/ "https://console.aws.amazon.com/elemental-appliances-software/").
2. On the navigation pane of the AWS Elemental Appliances &
   Software home page, choose
   **Activations**. The
   **Activations List** page appears.
   Choose the **Ready to license**
   tab.

The **Ready to license** tab shows
one entry for each product that you purchased. Each
product is identified by a product name and a unique
activation code. The activation code is the code that
you [received in the email](#install-live-license-retrieve "#install-live-license-retrieve"). Following from our
example, you might see two lines:

`LxxxPNL LVE-111-222-333 Live product
 2021-11-01`

`LxxxPNL LVE-111-222-444 Live product
 2021-11-01` 3. Choose the **Generate license**
button (at the top-right corner of the tab). The
**Generate new license** page
appears. 4. On the **Generate new license** page, choose the
**Choose files** button, and navigate to the folder
that you [copied the key files
to](#install-live-license-generate "#install-live-license-generate"). For example,
`/elemental_live_license_keys`.

In the dialog box that appears, select all the key
files that you generated, then choose
**Open**.

On the **Generate new license** page,
one entry appears for each key file. For example:

```
activation_systemA.key
15.39 KB
11/04/2021, 2:02:01 PM

activation_systemB.key
15.39 KB
11/04/2021, 2:32:22 PM
```

5. Choose **Generate license**. A
   license is generated for each entry. After the
   **License generated** message
   appears, the product for each license moves to the
   **Activations** tab.

###### Download the license files

1. On the **Activations** tab, choose
   one of the entries you want to set up. The
   **Product details** page appears
   for this product.
2. Choose the **Software** tab and look for the
   **License file** link.
3. Choose the **License file** link and follow the prompts
   to download the file.
4. Repeat these steps to download all the license files that you
   generated.
5. Follow the procedure that applies to your browser to open the folder that
   contains the downloaded license files. Make a note of the folder where the
   license files are located.

**About the License
Files**

Each license file is named as follows:
`lic-download-<hostname>.tgz`

For example:
`lic-download-systemA.tgz`

Each `tgz` license file contains the main
license for Elemental Live and licenses for all the add-on packs
that you purchased.

The licenses work only with the specific product and the
specific hardware unit.

## Install the

license files

When you [downloaded the license files](#install-live-license-download "#install-live-license-download"), you should have made a
note of the folder where these files were downloaded to on your
workstation. You must now transfer each file to its hardware
unit and install it.

###### To transfer the license to the hardware unit

- Use a method such as SCP to move the license file (the
  `.tgz` file) from your
  workstation to a location on the Elemental Live hardware
  unit. We recommend that you copy the file to a folder
  with a name like
  `elemental_licenses`.

Make sure that you put the correct license on each
hardware unit. The license only works on a specific
hardware unit.

###### To install the license on the hardware unit

On each hardware unit, you must set up Elemental Live to
use the license file.

1. Using an SSH client such as PuTTY, log in to the
   hardware unit with the _elemental_
   user credentials.

You are logged in at the home directory
(`/home/elemental`). 2. Navigate to the directory that contains the license
file, and extract the `.lic` files
from the `.tgz` file. Place the
`.lic` files in these
folders:

`/home/elemental`

`/opt/elemental_se` 3. Enter the following command to restart the
Elemental Live service:

`[elemental@hostname ~]$ sudo service
 elemental_se restart`

# Step A: Prepare hardware and

download files

## Prepare hardware and

network

To prepare your hardware and network, make sure the following steps are
complete:

- You have physically installed (racked) the hardware unit.
- You have set up the unit as a node on your organization's network.
- You have configured network cards and ensured that they're able to reach
  other machines on the network.
- You have set up a method, such as SCP, for transferring files between your
  workstation and the node.

## Note your activation

code

You should have received an email with your activation code. You need this number
for the installation.

If you're installing Elemental Live software on more than one
hardware unit, you received an activation code for each
instance. Decide which activation code you will use for each
unit, and make a note. The codes are not tied ahead of time to
any specific hardware unit, but you cannot use the same code on
more than one.

## Download installation

files

Download the installation files for Elemental Live.

###### To download installation files

1. Log in to [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations"). For detailed steps to
   download installation files, see [Downloading Elemental Live software](detailed-dl-lv-ig.md "detailed-dl-lv-ig.md").
2. Download your files.

You need the following files for Elemental Live:

    * A kickstart file (`.iso`)
     file for creating a USB boot drive. For example,
     `centos-20161028T12270-production-usb.iso`.


    You use this file to put a preconfigured
     installation of your operating system on your
     physical hardware unit. If you're downloading
     the kickstart file for several products, make a
     note of which file belongs to which product.
     Files are not interchangeable across
     products.
    * An installation (`.run`)
     file for the Elemental Live software itself. For
     example:



    `elemental_production_live_2.25.4.12345.run`.

## Create bootable

kickstart

At your workstation, use a third-party utility (such as
PowerISO or ISO2USB) to create a bootable USB drive from the
`.iso` file. For help, see
[this knowledge base article](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X").

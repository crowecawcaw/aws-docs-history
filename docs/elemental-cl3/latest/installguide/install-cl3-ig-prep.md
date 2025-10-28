# Step A: Prepare the hardware and download

files

## Prepare the hardware and network

To prepare your hardware and network, make sure you have done the
following:

- Physically installed the appliance.
- Set up the unit as a node on your network.
- Configured network cards and ensured that they're able to reach other
  machines on the network.
- Set up a method, such as SCP, for transferring files from your workstation
  to the node.

## Note your activation code

You should have received an email with your activation code.
You need this number for the installation.

If you're installing Conductor Live software on more than one appliance, you received
an activation code for each instance. Decide which activation code you will use for
each unit, and make a note. The codes are not tied ahead of time to any specific
appliance, but you cannot use the same code on more than one.

## Download files

Download the installation files for Conductor Live.

###### To download installation files

1. Log in to [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations"). For detailed steps to download installation
   files, see [Downloading AWS Elemental Conductor Live software](detailed-dl-cl3-ig.md "detailed-dl-cl3-ig.md").
2. Download your files.

You need the following files for Conductor Live:

    * A kickstart file (`.iso`) file for creating a
     USB boot drive. For example,
     `centos-20161028T12270-production-usb.iso`.


    You use this file to put a preconfigured installation of your
     operating system on your physical appliance.If you're
     downloading the kickstart file for several products, make a note of
     which file belongs to which AWS Elementalproduct. Files are not
     interchangeable across products.
    * An installation (`.run`) file for the Conductor Live
     software itself. For example:



    `elemental_production_conductor_live_3.25.5.12345.run`.

## Create bootable kickstart

At your workstation, use a third-party utility (such as PowerISO or ISO2USB) to
create a bootable USB drive from the `.iso` file. For help, see
the knowledge base article [Creating Bootable Recovery
(kickstart) Media](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X").

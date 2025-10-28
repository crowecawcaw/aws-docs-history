# Step A: Prepare hardware and

download files

## Prepare hardware and

network

To prepare your hardware and network, make sure you have done
the following:

- Physically installed the hardware unit.
- Set up the unit as a node on your network.
- Configured network cards and ensured that they're
  able to reach other machines on the network.
- Set up a method, such as SCP, for transferring files
  from your workstation to the VM guest.

## Note your activation

code

You should have received an email with your activation code.
You need this number for the installation.

If you're installing AWS Elemental software on more than one
system, you received an activation code for each system. Decide
and note which activation code you will use for each unit. The
codes are not tied ahead of time to any specific system, but you
cannot use the same code on more than one.

## Download installation

files

Download the installation files for each unique AWS Elemental product
that you're using.

###### To download installation files

1. Log in to [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations"). For detailed steps to
   download installation files, see [Downloading Elemental Live software](detailed-dl-lv-ig.md "detailed-dl-lv-ig.md").
2. Download your files.

You need the following files for Elemental Live.

    * A kickstart (`.ova`) file
     for creating a VM instance. For example,
     `centos-20161028T12270-production-usb.ova`.


    You will use this file to put a preconfigured
     installation of your operating system on your
     VM.
    * An installation (`.run`)
     file for the Elemental Live software itself. For
     example:


    `elemental_production_live_2.25.4.12345.run`


    Make sure that you download the right version
     of software for the processing architecture that
     you need, either CPU-only or GPU-enabled.

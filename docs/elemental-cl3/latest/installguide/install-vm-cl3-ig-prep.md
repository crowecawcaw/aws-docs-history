# Step A: Prepare the hardware and download

files

## Install the hardware

units

Install the Hypervisors according to the procedures for your organization.

###### Important

All the hypervisor hardware for one Conductor Live cluster must be installed in
the same physical location. This means that the hardware that hosts the Conductor Live
VM guest or guests, and that hosts the AWS Elemental Live guests must all be in the same
physical location.

## Prepare the hardware and network

To prepare your hardware and network, make sure you have done the following:

- Physically installed the appliance.
- Set up the unit as a node on your network.
- Configured network cards and ensured that they're able to reach other machines on the network.
- Set up a method, such as SCP, for transferring files from your workstation to the
  VM guest.

## Note Your Activation Code

You should have received an email with your activation code. You need this number for the installation.

If you're installing AWS Elemental software on more than one system, you received an activation code for each system. Decide and note which activation code you will use for each unit.
The codes are not tied ahead of time to any specific system, but you cannot use the same code on more than one.

## Download Files

Download the installation files for each unique AWS Elemental product that you're using.

###### To download installation files

1. Log in to [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations").
   For detailed steps to download installation files, see
   [Downloading AWS Elemental Conductor Live software](detailed-dl-cl3-ig.md "detailed-dl-cl3-ig.md").
2. Download your files.

You need the following files for each unique piece of AWS Elemental software that you're installing.

    * A kickstart (`.ova`) file for creating a VM instance.
     For example, `centos-20161028T12270-production-usb.ova`.


    You will use this file to put a preconfigured installation of your operating system on your VM.
    * An installation (`.run`) file for the AWS Elemental software itself. For example,
     `elemental_production_conductor_live247_3.25.5.12345.run`.

For example, if you're installing Conductor Live on two systems and AWS Elemental Live on five systems,
you need to download two `.iso` files and two `.run` files.

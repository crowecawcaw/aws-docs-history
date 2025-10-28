This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step A: Prepare Hardware and Download

Files

## Prepare Hardware and Network

To prepare your hardware and network, make sure you have done the following:

- Physically installed the hardware unit.
- Set up the unit as a node on your network.
- Configured network cards and ensured that they're able to reach other machines on the network.
- Set up a method, such as SCP, for transferring files from your workstation to the
  node.

## Note Your Activation Code

You should have received an email with your activation code. You need this number for the installation.

If you're installing AWS Elemental software on more than one system, you received an activation code for each system. Decide and note which activation code you will use for each unit.
The codes are not tied ahead of time to any specific system, but you cannot use the same code on more than one.

## Download Files

Download the installation files for each unique AWS Elemental product that you're using.

###### To download installation files

1. Log in to [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations").
   For detailed steps to download installation files, see [Downloading AWS Elemental Server Software](detailed-dl-srvr-ig.md "detailed-dl-srvr-ig.md").
2. Download your files.

You need the following files for each unique piece of AWS Elemental software that you're installing.

    * A kickstart (`.iso`) file for creating a USB boot drive.
     For example, `centos-20161028T12270-production-usb.iso`.


    You use this file to put a preconfigured installation of your operating system
     on your physical machine.
    * An installation (`.run`) file for the AWS Elemental software itself.
     For example, `elemental_production_server_2.18.3.44452.run`.


    Make sure that you download the right version of software for the processing architecture that you need, either CPU-only or GPU-enabled.

For example, if you're installing AWS Elemental Conductor File on two systems and AWS Elemental Server on five systems,
you need to download two `.iso` files and two `.run` files.

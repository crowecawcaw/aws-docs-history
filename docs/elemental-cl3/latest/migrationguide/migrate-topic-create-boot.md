# Create a boot USB drive

Only Dell servers support the ability to install RHEL 9 from a boot USB drive.
SuperMicro servers don't support this ability.

1. Obtain the RHEL 9 `.iso` file from [AWS Elemental Software Download page](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/softwaredownloads "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/softwaredownloads").

Find the AWS Elemental product and version they are planning to use. The appropriate
ISO file appears beside that version. 2. At your workstation, use a third-party utility (such as PowerISO or ISO2USB)
to create a bootable USB drive from your `.iso` file. For
help, read the Knowledge article [Creating Bootable
Recovery (kickstart) Media](https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X "https://us-east-1.console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/viewknowledge/How-to-create-bootable-recovery-kickstart-media-Windows-and-Apple-OS-X").

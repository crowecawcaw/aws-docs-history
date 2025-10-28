Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Troubleshooting `unlock-device` command problems with Snowball Edge

If the `unlock-device` command returns `connection refused`, you may have mistyped the command syntax or the configuration of your computer or network may be preventing the command from reaching the Snow device. Take these actions to resolve the situation:

1. Ensure the command was entered correctly.
   1. Use the LCD screen on the device to verify the IP addressed used in the command is correct.
   2. Ensure that the path to the manifest file used in the command is correct, including the file name.
   3. Use the [AWS Snowball Edge Management Console](https://console.aws.amazon.com/importexport/home?region=us-west-2 "https://console.aws.amazon.com/importexport/home?region=us-west-2") to verify the unlock code used in the command is correct.

2. Ensure the computer you are using is on the same network and subnet as the Snow device.
3. Ensure the computer you are using and the network are configured to allow access to the Snow device. Use the `ping` command for your operating system to determine if the computer can reach the Snow device over the network. Check the configurations of antivirus software, firewall configuration, virtual private network (VPN), or other configurations of your computer and network.

## Troubleshooting manifest file

problems with Snowball Edge

Each job has a specific manifest file associated with it. If you create
multiple jobs, track which manifest is for which job.

If you lose a manifest file or if a manifest file is corrupted, you can
download the manifest file for a specific job again. You do so using the console, AWS CLI, or
one of the AWS APIs.

If you run an update on the Snowball Edge, then a new manifest file needs to be downloaded and used for the job. For information about downloading a manifest file, see [Getting credentials to access a Snowball Edge](getting-started.md#get-credentials "getting-started.md#get-credentials").

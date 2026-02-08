# Prerequisites for listener mode

Before you create SRT outputs in listener mode, you must complete the following prerequisites:

1. **Create or identify a channel security group (Public delivery method only)**: For channels using the Public delivery method, you must attach a channel security group to the channel. The channel security group controls which downstream systems (SRT callers) are allowed to connect to the MediaLive listener endpoints. For information about channel security groups, see [Using channel security groups](feature-channel-security-groups.md "feature-channel-security-groups.md").

For channels using VPC delivery or MediaLive Anywhere channels, the channel security group is not required. Instead, you must configure your network to allow SRT connections from the caller destination to reach the listener endpoints. 2. **Coordinate with downstream systems**: Discuss the following with the operator of each downstream system:

    * The IP addresses that the downstream systems will connect from. You need these addresses to create or update the input security group that the channel security group references.
    * The encryption algorithm: AES 128, AES 192, or AES 256.
    * The passphrase for encryption. The passphrase can be 10 to 79 Unicode characters.
    * The preferred latency (in milliseconds) for packet loss and recovery. The valid range is 120 to 15000 milliseconds.
    * The stream ID, if the downstream system uses this identifier. The stream ID is optional.

3. **Store the passphrase in Secrets Manager**: Follow the steps in [Set up the passphrase in AWS Secrets Manager](srt-output-encryption-asm.md "srt-output-encryption-asm.md") to store the passphrase in AWS Secrets Manager.

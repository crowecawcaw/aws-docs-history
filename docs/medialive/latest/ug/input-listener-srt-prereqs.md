# Get ready

1. Discuss the following information with the operator of the upstream
   system:
   - The IP address that the upstream system will push from. You need this
     address to create an input security group that allows traffic from this
     address. For more information about input security groups, see [Working with input security groups](working-with-input-security-groups.md "working-with-input-security-groups.md").
   - The encryption algorithm that the upstream system will use: AES 128,
     AES 192, or AES 256. Encryption is required for SRT Listener inputs.

   Agree on a passphrase with the operator of the upstream system. The
   passphrase is used to generate the key for encrypting and decrypting the
   source content.
   - The stream ID, if the upstream system uses this identifier. The
     stream ID is an optional free-form string that the upstream system
     can send during the connection handshake. MediaLive accepts all connections
     regardless of the stream ID value. MediaLive logs the stream ID for
     monitoring and troubleshooting purposes only.
   - The preferred latency (in milliseconds) for implementing packet
     loss and recovery. Packet recovery is a key feature of SRT. The valid
     range is 120 to 15000 milliseconds.

2. You must store the passphrase that you agreed on with the operator. Someone
   in your organization must store the passphrase in a secret in AWS Secrets Manager. For
   more information, see [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md"). Create a secret of type
   **Other type of secret**. The result of creating the
   secret is an ARN that looks like this:

`arn:aws:secretsmanager:`region`:123456789012:secret:`Sample-abcdef``

###### Important

Store SRT passphrases in Secrets Manager as plaintext (for example, `secretpassword123`). Do not use the key/value option or JSON format when creating the Secret, as this may cause interoperability issues with other services. Store the passphrase as plaintext only.

Ensure your passphrase is between 10 and 79 characters. 3. Create or identify an input security group that includes the IP address of
the upstream system. For information about creating input security groups, see
[Creating an input security group](create-input-security-groups.md "create-input-security-groups.md").

# How delivery from Elemental Live to MediaConnect works at runtime

Here is the data that AWS Elemental Live has: The flow ARN. The Access key ID and Secret access key. Here is the data that MediaConnect has: The flow ARN. The destination IPs and protocol details. The encryption type and algorithm. The role ARN (for obtaining the secret - the encryption key). The secret ARN. When the event starts, Elemental Live authenticates with AWS using the AWS access key ID and AWS secret access key. It then sends the flow ARN to MediaConnect. MediaConnect accepts the request because Elemental Live has permission to make requests to MediaConnect. MediaConnect looks up the flow and determines if the flow is set up for encryption.

- If the flow is set up for encryption, MediaConnect sends the encryption type and algorithm information, and the secret ARN to Elemental Live. Elemental Live uses the secret ARN to get the secret (the encryption key) from Secrets Manager. Secrets Manager accepts the request from Elemental Live because Elemental Live has permission to get this secret.

Elemental Live uses the encryption key to encrypt the video and sends the encrypted video to MediaConnect.

MediaConnect in its turn uses the secret ARN to get the secret (the encryption key) from the Secrets Manager. Secrets Manager accepts the request from MediaConnect because MediaConnect has permission to get this secret; it has permission because it has been set up as a trusted entity with Secrets Manager. MediaConnect uses the encryption key to decrypt the video.

- If the flow is not set up for encryption, MediaConnect instructs Elemental Live to deliver the video unencrypted. Secrets Manager is not involved.

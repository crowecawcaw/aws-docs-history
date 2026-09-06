

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Register server credentials
<a name="connector-register-server-credentials"></a>

Once you have the MGN connector set up and ready to use, you can register source servers to the MGN connector. To do so click on the MGN connector name, then click "Register servers".

The servers list contains the source servers that were imported via the import feature or discovered by the agentless replication process.

Select the source servers you want to register to the MGN connector. Click the "Register servers with the MGN connector" button.

To perform actions on your source server, you must provide source server credentials. Server credentials are stored in AWS Secrets Manager. You can use an existing secret from AWS Secrets Manager or create a new one. You can create the credentials in the MGN console by choosing **Register server credentials** from the **Actions** menu.
+ Use existing secret
  + Using AWS Secrets Manager, MGN can use the stored source server credentials to connect to the source machine and perform actions on it. You must specify the secret that stores the source server credentials.
  + You may designate the same secret for multiple source servers if they share the same credentials.
  + Be sure to add the `AWSApplicationMigrationServiceManaged` tag to the secret with the value set to `True`.
+ Create new secret
  + **Secret name** - Enter a name for your new secret. The name you specify will be saved in AWS Secrets Manager.
  + **Encryption key** - To encrypt, either use the KMS key provided by Secrets Manager or create your own customer managed KMS key.
  + **For Windows servers:**
    + **Communication protocol** - This is the WinRM connection protocol between the MGN Connector and source servers used to install the agents. Specify either HTTP or HTTPS. We recommend HTTPS for secure and encrypted communication. Default is HTTPS.
    + **UserName** - A user that is authorized to install the agent and perform actions on the source server.
    + **Password** - The specific source server's password.
    + **CertificateAuthority** (Required if WinCaValidation is true) - The CA public certificate in PEM format, base64-encoded. Must be omitted or empty if WinCaValidation is false.
  + **For Linux servers:**
    + **UserName** - A user that is authorized to install the agent and perform actions on the source server.
    + **Credentials** - Provide one of the following:
      + **PrivateKey** - The source server's RSA private key in PEM format, base64-encoded. (The connector uses RSA keys only.)
      + **Password** - The specific source server's password (alternative to PrivateKey).
    + **HostKey** (Required if LinuxHostKeyValidation is true) - The source server's public host key in the format: `algorithm_name base64_public_key` (e.g., `ssh-ed25519 AAAA...`). This is the full base64 public key blob from ssh-keyscan output, not a fingerprint. Must be omitted if LinuxHostKeyValidation is false.
  + **Tags** - Secret key-value pairs will be assigned to the new secret. Note that `AWSApplicationMigrationServiceManaged` tag will also be added with the value set to `True`.
  + Here is the structure of the secrets manager entry:

    ```
    {
      "WinConnectionProtocol": "HTTPS",
      "WinUserName": "windows_username",
      "WinPassword": "windows_password",
      "WinCertificateAuthority": "<base64-encoded CA public certificate (PEM)>",
      "WinCaValidation": true,
      "LinuxUserName": "linux_username",
      "LinuxPrivateKey": "<base64-encoded RSA private key (PEM)>",
      "LinuxPassword": "<alternative to LinuxPrivateKey>",
      "LinuxHostKey": "ssh-ed25519 <base64 public host key>",
      "LinuxHostKeyValidation": true
    }
    ```
  + **Important notes on secret format:**
    + **Base64 encoding:** `LinuxPrivateKey` and `WinCertificateAuthority` must be base64-encoded PEM values. If you create the secret in the MGN console, encoding is performed automatically. If you create the secret manually in AWS Secrets Manager, you must encode these values yourself. Raw PEM text will cause connection failures.
    + **Private key format:** `LinuxPrivateKey` must be an RSA private key. Other key types are not supported.
    + **Validation flags:** `WinCaValidation` and `LinuxHostKeyValidation` are required fields and must always be present in the secret.
    + **Validation constraints:** `WinCertificateAuthority` is required only when `WinCaValidation` is true. `LinuxHostKey` is required only when `LinuxHostKeyValidation` is true. When their validation flag is false, these fields should be omitted or empty.
    + **HTTP protocol constraint:** `WinCaValidation` must be false when `WinConnectionProtocol` is set to HTTP.
    + **HostKey format:** The `LinuxHostKey` value is the full base64 public key blob from ssh-keyscan output (the second field), in the format `algorithm_name base64_key`. It is NOT a fingerprint or thumbprint.
+ 
**Note**  
The CA/HostKey validation is controlled by the validation flags (`WinCaValidation` and `LinuxHostKeyValidation`). When a validation flag is set to true, you must provide the corresponding CA or HostKey value. When set to false, the CA or HostKey fields should be omitted or left empty. If you do not provide the required value when validation is enabled, credential validation will fail with a "mandatory field not found" error.
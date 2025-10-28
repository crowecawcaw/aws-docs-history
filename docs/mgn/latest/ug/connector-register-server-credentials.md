NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Register server credentials

Once you have the MGN connector set up and ready to use, you can register source servers to the MGN connector. To do so click on the MGN connector name, then click “Register servers“.

The servers list contain the source servers that were imported via the import feature or discovered by the agentless replication process.

Select the source servers you want to register to the MGN connector. Click the "Register servers with the MGN connector" button.

In order to perform actions on your source server, you must provide source server credentials. Server credentials are stored in AWS Secrets Manager. You can use an existing secret from the AWS Secrets Manager or create a new one.

- Use existing secret
  - Using AWS Secrets Manager AWS MGN can use the stored source server credentials and API keys in order to connect to the source machine and perform actions on it. You must specify the secret that stores the source server credentials, using an existing secret.
  - You may designate the same secret for multiple source servers, if they share the same credentials.
  - Be sure to add the AWSApplicationMigrationServiceManaged tag to the secret. The value is ignored, and may be left empty.

- Create new secret
  - **Secret name** - Enter a name for your new secret. The name you specify will be saved in AWS Secret Manager.
  - **Encryption key** - To encrypt, either use the KMS key provided by Secret Manager or create your own customer managed KMS key.
  - **For Windows servers:**
    - **Communication protocol** –
      this is the WinRM connection protocol between the MGN Connector and Source Servers used to install the agents.

    ###### Note

    Though you can use HTTP, we
    recommend that you use HTTPS to ensure secure and encrypted
    communication between the MGN connector and the source
    servers.

    Specify either:

        * **HTTP**
        * **HTTPS**

    - **UserName** – A user that is authorized to install the agent and perform actions on the source server.
    - **Password** – The specific source server's password.
    - **CertificateAuthority**
      (Optional) - Include the source server IPs in the
      certificate's SAN field to enable communication.

  - **For Linux servers:**
    - **UserName** – A user that is authorized to install the agent and perform actions on the source server.
    - **Provide one of the following:**
      - **Password** – The specific source server's password.
      - **PrivateKey** – The source server’s private key.

    - **HostKey** (Optional) – include the host key to validate it during SSH connection.

  - **Tags** - Secret key-value pairs will be assigned to the new secret. Note that AWSApplicationMigrationServiceManaged tag will also be added.
  - Here is the structure of the secrets manager entry:

  ```

      {
      "WinConnectionProtocol":"HTTPS",
      "WinUserName":"*windows\_username*",
      "WinPassword":"*windows\_password*",
      "WinCertificateAuthority":"",
      "WinCaValidation":false,
      "LinuxUserName":"*linux\_username*",
      "LinuxPrivateKey":"*linux\_private\_key*",
      "LinuxHostKey":"*linux\_host\_key*",
      "LinuxHostKeyValidation":false
      }

  ```

- ###### Note

The CA/HostKey validation is turned on by default, indicated by the validation flag being set to true. Provide the CA or HostKey in the json for validation. If you don’t provide it, you must explicitly disable validation by setting the validation flag to false. The key algorithm in HostKey, must be provided in the following format:

```
"HostKey": "algorithm_name thumbprint"
```

List of supported algorithms: "ssh-ed25519", "ecdsa-sha2-nistp256", "ecdsa-sha2-nistp384", "ecdsa-sha2-nistp521", "rsa-sha2-512", "rsa-sha2-256", "ssh-rsa", "ssh-dss"

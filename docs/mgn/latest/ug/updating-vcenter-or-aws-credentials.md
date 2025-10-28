NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Updating the vCenter or AWS

Credentials

Users who want to change the vCenter or AWS credentials used by the Application Migration Service appliance
should follow these steps. This change requires root privileges on the appliance:

1. In the command prompt, navigate to the aws-vcenter-client directory:

`cd /var/lib/aws-vcenter-client/1.1.8/` 2. Run the vCenter configuration update tool with this command:

`sudo ./vcenter_configuration_update` 3. When running the vCenter configuration update tool, you are prompted to provide the
necessary credentials. Follow these steps to update the credentials. Provide the required info
in each field and then press Enter:

    * New vCenter username (--new-vcenter-username)
    * New vCenter password (--new-vcenter-password)
    * New AWS Secret Key ID (--new-aws-access-key-id)
    * New AWS Secret Access Key (--new-aws-secret-access-key)
    * New path to the CA (optional) (--new-ca-path)

4. If you do not provide the `--new-ca-path` flag, the tool first asks if you want to
   update the CA path. If you answer yes, it prompts you for the new CA path. If you answer
   no, the tool uses the CA path from the previous configuration. The tool verifies the
   new vCenter and AWS credentials by attempting to connect to vCenter and Application Migration Service using them.
5. Upon successful connection to vCenter and Application Migration Service, the tool saves the new credentials
   and restart the necessary services.
6. In case of failure to connect to vCenter or Application Migration Service, the new credentials are not stored,
   and the previous configuration is retained. This error message is
   displayed: `Failed to connect to the vCenter endpoint or MGN using the new connection
details. The configuration changes will not be applied.`

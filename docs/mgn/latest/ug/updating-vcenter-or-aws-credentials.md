

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Updating the vCenter or AWS Credentials
<a name="updating-vcenter-or-aws-credentials"></a>

Users who want to change the vCenter or AWS credentials used by the MGN appliance should follow these steps. This change requires root privileges on the appliance:

1.  In the command prompt, navigate to the aws-vcenter-client directory:

   `cd /var/lib/aws-vcenter-client/1.1.8/`

1.  Run the vCenter configuration update tool with this command:

    `sudo ./vcenter_configuration_update` 

1.  When running the vCenter configuration update tool, you are prompted to provide the necessary credentials. Follow these steps to update the credentials. Provide the required info in each field and then press Enter: 
   +  New vCenter username (--new-vcenter-username) 
   +  New vCenter password (--new-vcenter-password) 
   +  New AWS Access Key ID (--new-aws-access-key-id) 
   +  New AWS Secret Access Key (--new-aws-secret-access-key) 
   +  New path to the CA (optional) (--new-ca-path) 

1.  If you do not provide the `--new-ca-path` flag, the tool first asks if you want to update the CA path. If you answer yes, it prompts you for the new CA path. If you answer no, the tool uses the CA path from the previous configuration. The tool verifies the new vCenter and AWS credentials by attempting to connect to vCenter and MGN using them. 

1.  Upon successful connection to vCenter and MGN, the tool saves the new credentials and restarts the necessary services. 

1.  In case of failure to connect to vCenter or MGN, the new credentials are not stored, and the previous configuration is retained. This error message is displayed: `Failed to connect to the vCenter endpoint or MGN using the new connection details. The configuration changes will not be applied.` 
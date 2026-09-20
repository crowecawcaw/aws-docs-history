

# Create external resources
<a name="create-external-resources"></a>

This CloudFormation stack creates networking, storage, active directory, and domain certificates (if a PortalDomainName is provided). You must have these external resources available to deploy the product.

You may [ download the recipes template](https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/res/res_demo_env/assets/bi.yaml) before deployment.

**Time to deploy:** Approximately 40-90 minutes 

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).
**Note**  
Make sure you are in your administrator account.

1. Launch [ the template](https://console.aws.amazon.com/cloudformation/home#/stacks/quickcreate?templateURL=https%3A%2F%2Fs3.amazonaws.com%2Faws-hpc-recipes%2Fmain%2Frecipes%2Fres%2Fres_demo_env%2Fassets%2Fbi.yaml) in the console.

   If you are deploying in an AWS GovCloud Region, launch the template in your GovCloud partition account (for example, [ here](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/res/res_demo_env/assets/bi.yaml) for the AWS GovCloud (US-West) Region).

1. Enter the template parameters:
**Important**  
Use different values for `AdminPassword` and `ServiceAccountPassword` to maintain proper security boundaries between these accounts.


<table>
<thead>
  <tr><th>Parameter </th><th>Default </th><th>Description </th></tr>
</thead>
<tbody>
  <tr><td>DomainName </td><td><code>corp.res.com</code></td><td>Domain used for the active directory. The default value is supplied in the <code>LDIF</code> file which sets up bootstrap users. If you would like to use the default users, leave the value as default. To change the value, update and provide a separate <code>LDIF</code> file. This does not need to match the domain used for active directory.</td></tr>
  <tr><td>SubDomain (GovCloud only)</td><td></td><td><b>This parameter is optional for commercial regions, but required for GovCloud regions.</b><br /> If you provide a SubDomain, the parameter will be prefixed to the DomainName provided. The provided Active Directory domain name will become a subdomain.</td></tr>
  <tr><td>AdminPassword</td><td></td><td>The password for the active directory administrator (username <code>Admin</code>). This user is created in the active directory for the initial bootstrapping phase and is not used after.<br /><b>Important:</b> the format of this field can either be (1) a plain text password or (2) the ARN of an AWS Secret formatted as a key/value pair <code>{"password":"somepassword"}</code>.<br /><b>Note:</b> The password for this user must meet the <a href="https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements"> password complexity requirements for active directory</a>.</td></tr>
  <tr><td>ServiceAccountPassword</td><td></td><td>Password used to create a service account (<code>ReadOnlyUser</code>). This account is used for synchronization.<br /><b>Important:</b> the format of this field can either be (1) a plain text password or (2) the ARN of an AWS Secret formatted as a key/value pair <code>{"password":"somepassword"}</code>.<br /><b>Note:</b> The password for this user must meet the <a href="https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements"> password complexity requirements for active directory</a>.</td></tr>
  <tr><td>Keypair</td><td></td><td>Connects the administrative instances using an SSH client. <br /><b>Note: </b>AWS Systems Manager Session Manager can also be used to connect to instances.</td></tr>
  <tr><td>LDIFS3Path</td><td><code>aws-hpc-recipes/main/recipes/res/res_demo_env/assets/res.ldif</code></td><td>The Amazon S3 path to an LDIF file imported during the bootstrapping phase of active directory setup. For more information, see <a href="https://github.com/aws-samples/aws-hpc-recipes/blob/main/recipes/dir/demo_managed_ad/README.md#ldif-support"> LDIF Support</a>. The parameter pre-populates with a file that creates a number of users in the active directory.To view the file, see the <a href="https://github.com/aws-samples/aws-hpc-recipes/blob/main/recipes/res/res_demo_env/assets/res.ldif"> res.ldif file</a> available in GitHub.</td></tr>
  <tr><td>ClientIpCidr</td><td></td><td>The IP address from which you will access the site. For example, you can select your IP address and use <code>[IPADDRESS]/32</code> to only allow access from your host. You can update this post-deployment.</td></tr>
  <tr><td>ClientPrefixList</td><td></td><td>Enter a prefix list to provide access to the active directory management nodes. For information on creating a managed prefix list, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/working-with-managed-prefix-lists.html">Work with customer-managed prefix lists</a>.</td></tr>
  <tr><td>EnvironmentName</td><td><code>res-[environment name]</code></td><td>If the <code>PortalDomainName</code> is provided, this parameter is used to add tags to the secrets generated so that they can be used within the environment. This will need to match the <code>EnvironmentName</code> parameter used when creating the RES stack. If you are deploying multiple environments in your account, this will need to be unique.</td></tr>
  <tr><td>PortalDomainName</td><td></td><td><b>For GovCloud deployments, do not enter this parameter. The certificates and secrets were manually created during the prerequisites.</b>The domain name in Amazon Route 53 for the account. If this is provided, then a public certificate and key file will be generated and uploaded to AWS Secrets Manager. If you have your own domain and certificates, this parameter and <code>EnvironmentName</code> can be left blank.</td></tr>
</tbody>
</table>


1.  Acknowledge all checkboxes in **Capabilities**, and choose **Create stack**. 


# Step 1: Launch the product
<a name="launch-the-product"></a>

Follow the step-by-step instructions in this section to configure and deploy the product into your account.

**Time to deploy:** Approximately 60 minutes 

You can [ download the CloudFormation template](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/latest/ResearchAndEngineeringStudio.template.json) for this product before deploying it. 

If you are deploying in AWS GovCloud (US-West), use this [ template](https://research-engineering-studio-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/releases/latest/ResearchAndEngineeringStudio.template.json).

**res-stack** - Use this template to launch the product and all associated components. The default configuration deploys the RES main stack and authentication, frontend, and backend resources. 

**Note**  
AWS CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) (AWS CDK) constructs. 

The AWS CloudFormation template deploys Research and Engineering Studio on AWS in the AWS Cloud. You must meet the [prerequisites](prerequisites.md) before launching the stack. 

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. Launch the [ template ](https://console.aws.amazon.com/cloudformation/home#/stacks/quickcreate?templateURL=https%3A%2F%2Fresearch-engineering-studio-us-east-1.s3.amazonaws.com%2Freleases%2Flatest%2FResearchAndEngineeringStudio.template.json).

   To deploy in AWS GovCloud (US-West), launch this [ template](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/quickcreate?templateURL=https://research-engineering-studio-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/releases/latest/ResearchAndEngineeringStudio.template.json).

1. The template launches in the US East (N. Virginia) Region by default. To launch the product in a different AWS Region, use the Region selector in the console navigation bar.
**Note**  
This product uses the Amazon Cognito service, which is not currently available in all AWS Regions. You must launch this product in an AWS Region where Amazon Cognito is available. For the most current availability by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). 

1. Under **Parameters**, review the parameters for this product template and modify them as necessary. If you deployed the automated external resources, you can find these parameters in the **Outputs** tab of the external resources stack. 


<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>EnvironmentName</td><td>{{&lt;<i>res-demo</i>&gt;}}</td><td>A unique name given to your RES environment starting with res-, no longer than 11 characters, and no capital letters.</td></tr>
  <tr><td>AdministratorEmail</td><td></td><td>The email address for the user completing setup of the product. This user additionally functions as a break-glass (emergency access) user if there is an Active Directory single sign-on integration failure.</td></tr>
  <tr><td>InfrastructureHostAMI</td><td>ami-{{[numbers or letters only]}}</td><td><i>(Optional)</i> You can provide a custom AMI ID to use for all the infrastructure hosts. The current supported OSes are Amazon Linux 2, Amazon Linux 2023, RHEL8, RHEL9, Windows Server 2019 and 2022 (x86), and Windows 10 and 11. For more information, see <a href="prerequisites.md#prep-ami">Prepare Amazon Machine Images (AMIs)</a>.</td></tr>
  <tr><td>SSHKeyPair</td><td></td><td>The key pair used to connect to infrastructure hosts.</td></tr>
  <tr><td>ClientIP</td><td>{{x.x.x}}.0/24 or {{x.x.x}}.0/32</td><td>IP address filter that limits connections to the system. You can update the ClientIpCidr after deployment.</td></tr>
  <tr><td>ClientPrefixList</td><td></td><td><i>(Optional)</i> Provide a managed prefix list for IPs allowed to directly access the web UI and SSH into the bastion host.</td></tr>
  <tr><td>IAMPermissionBoundary</td><td></td><td><i>(Optional)</i> You can provide a managed policy ARN that will be attached as a permission boundary to all roles created in RES. For more information, see <a href="permission-boundaries.md">Setting custom permission boundaries</a>. </td></tr>
  <tr><td>IAMResourcePrefix</td><td></td><td><i>(Optional)</i> A prefix applied to your IAM resources deployed by the RES environment ending with <code>-</code>, no longer than 12 characters.</td></tr>
  <tr><td>IAMResourcePath</td><td><code>/</code></td><td><i>(Optional)</i> A path applied to your IAM resources deployed by the RES environment that starts and ends with <code>/</code>.</td></tr>
  <tr><td>VpcId</td><td></td><td>ID for the VPC where instances will launch.</td></tr>
  <tr><td>IsLoadBalancerInternetFacing</td><td></td><td>Select true to deploy internet facing load balancer (Requires public subnets for load balancer). For deployments that need restricted internet access, select false.</td></tr>
  <tr><td>LoadBalancerSubnets</td><td></td><td>Select at least two subnets in different Availability Zones where load balancers will launch. For deployments that need restricted internet access, select private subnets. For deployments that need internet access, select public subnets. If more than two were created by the external networking stack, select all that were created.</td></tr>
  <tr><td>InfrastructureHostSubnets</td><td></td><td>Select at least two private subnets in different Availability Zones where infrastructure hosts will launch. If more than two were created by the external networking stack, select all that were created.</td></tr>
  <tr><td>VdiSubnets</td><td></td><td>Select at least two private subnets in different Availability Zones where VDI instances will launch. If more than two were created by the external networking stack, select all that were created.</td></tr>
  <tr><td>ActiveDirectoryName</td><td><code>corp.res.com</code></td><td>Domain for the Active Directory. It does not need to match the portal domain name.</td></tr>
  <tr><td>ADShortName</td><td><code>corp</code></td><td>The short name for the Active Directory. This is also called the NetBIOS name.</td></tr>
  <tr><td>LDAP Base</td><td><b>{{DC=corp,DC=res,DC=com}}</b></td><td>An LDAP path to the base within the LDAP hierarchy.</td></tr>
  <tr><td>LDAPConnectionURI</td><td></td><td>A single ldap:// path that points to the Active Directory host server. If you deployed the automated external resources with the default AD domain, you can use ldap://corp.res.com.</td></tr>
  <tr><td>ServiceAccountCredentialsSecretArn</td><td></td><td>Provide a Secret ARN which contains the username and password for the Active Directory service account user, formatted as a username:password key/value pair.</td></tr>
  <tr><td>UsersOU</td><td></td><td>Organizational unit within AD for users that will sync.</td></tr>
  <tr><td>GroupsOU</td><td></td><td>Organizational unit within AD for groups that will sync.</td></tr>
  <tr><td>SudoersGroupName</td><td>RESAdministrators</td><td>Group name that contains all users with sudo access on instances at install and administrator access on RES. </td></tr>
  <tr><td>ComputersOU</td><td></td><td>Organizational unit within AD that instances will join.</td></tr>
  <tr><td>DomainTLSCertificateSecretARN</td><td></td><td> <i>(Required for LDAPS)</i> Provide a domain TLS certificate secret ARN to enable TLS communication to AD. Leave empty if not using LDAPS. </td></tr>
  <tr><td>EnableLdapIDMapping</td><td></td><td>Determines if UID and GID numbers are generated by SSSD or if the numbers provided by the AD are used. Set to True to use SSSD generated UID and GID, or False to use UID and GID provided by the AD. For most cases this parameter should be set to True.</td></tr>
  <tr><td>DisableADJoin</td><td>False</td><td>To prevent Linux hosts from joining the directory domain, change to True. Otherwise, leave in the default setting of False. </td></tr>
  <tr><td>ServiceAccountUserDN </td><td></td><td>Provide the distinguished name (DN) of the service account user in Directory.</td></tr>
  <tr><td>SharedHomeFilesystemID</td><td></td><td>An EFS ID to use for the shared home filesystem for Linux VDI hosts.</td></tr>
  <tr><td>CustomDomainNameforWebApp</td><td></td><td><i>(Optional)</i> Subdomain used by the web portal to provide links for the web portion of the system.</td></tr>
  <tr><td>CustomDomainNameforVDI</td><td></td><td><i>(Optional)</i> Subdomain used by the web portal to provide links for the VDI portion of the system.</td></tr>
  <tr><td>ACMCertificateARNforWebApp</td><td></td><td><i>(Optional)</i> When using the default configuration, the product hosts the web application under the domain amazonaws.com. You can host the product services under your domain. If you deployed the automated external resources, this was generated for you and the information can be found in the Outputs of the res-bi stack. If you need to generate a certificate for your web application, see <a href="configuration-guide.md">Configuration guide</a>.</td></tr>
  <tr><td>CertificateSecretARNforVDI</td><td></td><td><i>(Optional)</i> This ARN secret stores the public certificate for your web portal's public certificate. If you set a portal domain name for your automated external resources, you can find this value under the Outputs tab of the res-bi stack.</td></tr>
  <tr><td>PrivateKeySecretARNforVDI</td><td></td><td><i>(Optional)</i> This ARN secret stores the private key for your web portal's certificate. If you set a portal domain name for your automated external resources, you can find this value under the Outputs tab of the res-bi stack.</td></tr>
  <tr><td>CognitoUserPoolId</td><td></td><td>Cognito user pool for user and client authentication. RES will create one by default if no Cognito user pool is specified.</td></tr>
  <tr><td>CognitoUserPoolDomainUrl </td><td></td><td>Cognito user pool domain for managed login. This parameter must be provided when the <code>CognitoUserPoolId</code> is specified.</td></tr>
</tbody>
</table>


1. Under **Configure stack options → Tags - *optional***, add the tags (key-value pairs) you want to apply to RES deployed resources. Tag key `Name` and `res:*` are preserved by RES and cannot be used as tag keys.

1. Choose **Create stack** to deploy the stack. 

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You receive a CREATE\_COMPLETE status in approximately 60 minutes. 

**Important**  
You are responsible for patching your infrastructure/VDI hosts after deployment.
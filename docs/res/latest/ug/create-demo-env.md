# Create a demo environment

Follow the steps in this section to try out Research and Engineering Studio on AWS. This demo deploys a non-production
environment with a minimal set of parameters using the [Research and Engineering Studio on AWS demo environment stack template](https://github.com/aws-samples/aws-hpc-recipes/blob/main/recipes/res/res_demo_env/assets/res-demo-stack.yaml "https://github.com/aws-samples/aws-hpc-recipes/blob/main/recipes/res/res_demo_env/assets/res-demo-stack.yaml"). It uses a
Keycloak server for SSO.

Note that after you deploy the stack, you must follow the
[Post deployment steps](#create-demo-env-post-deployment "#create-demo-env-post-deployment")
below to set up users in the environment before you login.

## Create a one-click demo stack

This AWS CloudFormation stack creates all the components required by Research and Engineering Studio.

**Time to deploy**: ~90 minutes

### Prerequisites

###### Topics

- [Create an AWS account with an administrative
  user](#create-demo-env-aws-account "#create-demo-env-aws-account")
- [Create an Amazon EC2 SSH key pair](#create-demo-env-ssh-key-pair "#create-demo-env-ssh-key-pair")
- [Increase service quotas](#create-demo-env-increase-service-quotas "#create-demo-env-increase-service-quotas")

#### Create an AWS account with an administrative

user

You must have an AWS account with an administrative user:

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

#### Create an Amazon EC2 SSH key pair

If you do not have Amazon EC2 SSH key pair, you will need to create one. For more information,
see [Create
a key pair using Amazon EC2](../../../AWSEC2/latest/UserGuide/create-key-pairs.md "../../../AWSEC2/latest/UserGuide/create-key-pairs.md") in the _Amazon EC2 User Guide_.

#### Increase service quotas

We recommend [increasing the service quotas](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") for:

- [Amazon VPC](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md")
  - Increase the Elastic IP address quota per NAT gateway from five to eight
  - Increase the NAT gateways per Availability Zone from five to ten

- [Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md")
  - Increase the EC2-VPC Elastic IPs from five to ten

Your AWS account has default quotas, formerly referred to as limits, for each AWS service.
Unless otherwise noted, each quota is Region-specific. You can request increases for some
quotas, and other quotas cannot be increased. For more information,
see [Quotas for AWS services in
this product](plan-your-deployment.md#quotas-for-aws-services-in-this-product "plan-your-deployment.md#quotas-for-aws-services-in-this-product").

### Create resources and input parameters

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").

###### Note

Make sure you are in your administrator account. 2. Launch [the template](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/res/res_demo_env/assets/res-demo-stack.yaml "https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/res/res_demo_env/assets/res-demo-stack.yaml") in the console. 3. Under **Parameters**, review the parameters for this
product template and modify them as necessary.

| Parameter          | Default        | Description                                                                                                                                                                                |
| ------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EnvironmentName    | `<*res-demo*>` | A unique name given to your RES environment starting with res-, no longer than 11 characters, and no capital letters.                                                                      |
| AdministratorEmail |                | The email address for the user completing setup of the product. This user additionally functions as a break-glass user if there is an Active Directory single sign on integration failure. |
| KeyPair            |                | The key pair used to connect to infrastructure hosts.                                                                                                                                      |
| ClientIPCidr       | <0.0.0.0/0>    | IP address filter which limits connection to the system. You can update the ClientIpCidr after deployment.                                                                                 |
| InboundPrefixList  |                | _(Optional)_ Provide a managed prefix list for IPs allowed to directly access the web UI and SSH into the bastion host.                                                                    | 4. Choose **Create stack**. ## Post deployment steps 1. You can now log in to the demo environment using the clusteradmin user and the temporary password sent to the administrator email you entered during setup. You are prompted to create a new password on your first log in. 2. If you want to use the "Sign in with organization SSO" feature, you must first reset the passwords for each user you would like to log in as. You can reset user passwords from the AWS Directory Service. The demo stack creates four users with usernames which you can use: admin1, user1, admin2, and user2. 1. Go to the Directory Service console. 2. Select the Directory Id for your environment. You can get the Directory Id from the output of the `<StackName>*DirectoryService*` stack. 3. From the top right **Action** dropdown menu, select **Reset user password**. 4. For all the users you want to use, enter the username, type in the new password you want and then choose **Reset Password**. 3. Once you have reset the user passwords, proceed to the single sign in log in page to access the environment. Your deployment is now ready. Use the EnvironmentUrl you received in your email to access the UI, or you can also get the same URL from the output of the deployed stack. You may now login to the Research and Engineering Studio environment with the user and password that you reset the password for in Active Directory. |

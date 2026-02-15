# Create a ROSA with HCP cluster using the ROSA CLI

The following sections describe how to get started with ROSA with hosted control planes (ROSA with HCP) using AWS STS and the ROSA CLI.
For steps to create a ROSA with HCP cluster using Terraform, see [the Red Hat documentation](https://docs.openshift.com/rosa/rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.html "https://docs.openshift.com/rosa/rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.html"). To learn more about the Terraform provider for creating ROSA clusters, see [the Terraform documentation](https://registry.terraform.io/providers/terraform-redhat/rhcs/latest/docs "https://registry.terraform.io/providers/terraform-redhat/rhcs/latest/docs").

The ROSA CLI uses `auto` mode or `manual` mode to create the IAM resources and OpenID Connect (OIDC) configuration required to create a ROSA
cluster.
`auto` mode automatically creates the required IAM roles and policies and OIDC provider.
`manual` mode outputs the AWS CLI commands that are needed to create the IAM resources manually.
By using `manual` mode, you can review the generated AWS CLI commands before running them manually.
With `manual` mode, you can also pass the commands to another administrator or group in your organization so they can create the resources.

The procedures in this document use the `auto` mode of the ROSA CLI to create the required IAM resources and OIDC configuration for ROSA with HCP.
For more options to get started, see [Get started with ROSA](getting-started.md "getting-started.md").

###### Topics

- [Prerequisites](#getting-started-hcp-prereqs "#getting-started-hcp-prereqs")
- [Create Amazon VPC architecture](#create-vpc-hcp "#create-vpc-hcp")
- [Create the required IAM roles and OpenID Connect configuration](#create-iam-roles-oidc-hcp "#create-iam-roles-oidc-hcp")
- [Create a ROSA with HCP cluster using the ROSA CLI and AWS STS](#create-hcp-cluster-cli "#create-hcp-cluster-cli")
- [Configure an identity provider and grant cluster access](#configure-oidc-hcp-cli "#configure-oidc-hcp-cli")
- [Grant user access to a cluster](#grant-user-access-hcp-cli "#grant-user-access-hcp-cli")
- [Configure cluster-admin permissions](#configure-cluster-admin-hcp "#configure-cluster-admin-hcp")
- [Configure dedicated-admin permissions](#configure-dedicated-admin-hcp "#configure-dedicated-admin-hcp")
- [Access a cluster through the Red Hat Hybrid Cloud Console](#console-access-hcp-cli "#console-access-hcp-cli")
- [Deploy an application from the Developer Catalog](#deploy-app-hcp-cli "#deploy-app-hcp-cli")
- [Revoke cluster-admin permissions from a user](#revoke-cluster-admin-hcp-cli "#revoke-cluster-admin-hcp-cli")
- [Revoke dedicated-admin permissions from a user](#revoke-dedicated-admin-hcp-cli "#revoke-dedicated-admin-hcp-cli")
- [Revoke user access to a cluster](#revoke-user-hcp-cli "#revoke-user-hcp-cli")
- [Delete a cluster and AWS STS resources](#delete-cluster-hcp-cli "#delete-cluster-hcp-cli")

## Prerequisites

Complete the prerequisite actions listed in [Set up to use ROSA](set-up.md "set-up.md").

## Create Amazon VPC architecture

The following procedure creates Amazon VPC architecture that can be used to host a cluster.
All cluster resources are hosted in the private subnet.
The public subnet routes outbound traffic from the private subnet through a NAT gateway to the public internet.
This example uses the CIDR block `10.0.0.0/16` for the Amazon VPC.
However, you can choose a different CIDR block.
For more information, see [VPC sizing](../../../vpc/latest/userguide/configure-your-vpc.md#vpc-sizing "../../../vpc/latest/userguide/configure-your-vpc.md#vpc-sizing").

###### Important

If Amazon VPC requirements are not met, cluster creation fails.

###### Example

Terraform

1. Install the Terraform CLI.
   For more information, see the [install instructions in the Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli "https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli").
2. Open a terminal session and clone the Terraform VPC repository.

```
git clone https://github.com/openshift-cs/terraform-vpc-example
```

3. Navigate to the created directory.

```
cd terraform-vpc-example
```

4. Initiate the Terraform file.

```
terraform init
```

Once complete, the CLI returns a message that Terraform has been successfully initialized. 5. To build a Terraform plan based on the existing template, run the following command.
The AWS Region must be specified.
Optionally, you can choose to specify a cluster name.

```
terraform plan -out rosa.tfplan -var region=<region>
```

Once the command has run, a `rosa.tfplan` file is added to the `hypershift-tf` directory.
For more detailed options, see [the Terraform VPC repository’s README file](https://github.com/openshift-cs/terraform-vpc-example/blob/main/README.md "https://github.com/openshift-cs/terraform-vpc-example/blob/main/README.md"). 6. Apply the plan file to build the VPC.

```
terraform apply rosa.tfplan
```

Once complete, the CLI returned a success message that verifies the added resources.

    1. (Optional) Create environment variables for the Terraform-provisioned private, public, and machinepool subnet IDs to use when creating your ROSA with HCP cluster.



    ```
    export SUBNET_IDS=$(terraform output -raw cluster-subnets-string)
    ```
    2. (Optional) Verify that the environment variables were correctly set.



    ```
    echo $SUBNET_IDS
    ```

Amazon VPC console

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").
2. On the VPC dashboard, choose **Create VPC**.
3. For **Resources to create**, choose **VPC and more**.
4. Keep **Name tag auto-generation** selected to create Name tags for the VPC resources, or clear it to provide your own Name tags for the VPC resources.
5. For **IPv4 CIDR block**, enter an IPv4 address range for the VPC. A VPC must have an IPv4 address range.
6. (Optional) To support IPv6 traffic, choose **IPv6 CIDR block, Amazon-provided IPv6 CIDR block**.
7. Leave **Tenancy** as `Default`.
8. For **Number of Availability Zones (AZs)**, choose the number that you require.
   For Multi-AZ deployments, ROSA requires three Availability Zones.
   To choose the AZs for your subnets, expand **Customize AZs**.

###### Note

Some ROSA instance types are only available in select Availability Zones.
You can use the ROSA CLI command `rosa list instance-types` command to list all ROSA instance types available.
To check if an instance type is available for a given Availability Zone, use the AWS CLI command
`aws ec2 describe-instance-type-offerings --location-type availability-zone --filters Name=location,Values=<availability_zone> --region <region> --output text | egrep "<instance_type>"`. 9. To configure your subnets, choose values for **Number of public subnets** and **Number of private subnets**.
To choose the IP address ranges for your subnets, expand **Customize subnets CIDR blocks**.

###### Note

ROSA with HCP requires that customers configure at least one public and private subnet per Availability Zone used to create clusters. 10. To grant resources in the private subnet access to the public internet over IPv4, for **NAT gateways**, choose the number of AZs in which to create NAT gateways.
In production, we recommend that you deploy a NAT gateway in each AZ with resources that need access to the public internet. 11. (Optional) If you need to access Amazon S3 directly from your VPC, choose **VPC endpoints, S3 Gateway**. 12. Leave the default DNS options selected.
ROSA requires DNS hostname support on the VPC. 13. Expand **Additional tags**, choose **Add new tag**, and add the following tag keys.
ROSA uses automated preflight checks that verify that these tags are used.

    * **Key**: `kubernetes.io/role/elb`
    * **Key**: `kubernetes.io/role/internal-elb`

14. Choose **Create VPC**.

AWS CLI

1. Create a VPC with a `10.0.0.0/16` CIDR block.

```
 aws ec2 create-vpc \
     --cidr-block 10.0.0.0/16 \
     --query Vpc.VpcId \
     --output text
```

The preceding command returns the VPC ID.
The following is an example output.

```
vpc-1234567890abcdef0
```

2. Store the VPC ID in an environment variable.

```
export VPC_ID=vpc-1234567890abcdef0
```

3. Create a `Name` tag for the VPC, using the `VPC_ID` environment variable.

```
aws ec2 create-tags --resources $VPC_ID --tags Key=Name,Value=MyVPC
```

4. Enable DNS hostname support on the VPC.

```
aws ec2 modify-vpc-attribute \
    --vpc-id $VPC_ID \
    --enable-dns-hostnames
```

5. Create a public and private subnet in the VPC, specifying the Availability Zones where the resources should be created.

###### Important

ROSA with HCP requires that customers configure at least one public and private subnet per Availability Zone used to create clusters.
For Multi-AZ deployments, three Availability Zones are required.
If these requirements are not met, cluster creation fails.

###### Note

Some ROSA instance types are only available in select Availability Zones.
You can use the ROSA CLI command `rosa list instance-types` command to list all ROSA instance types available.
To check if an instance type is available for a given Availability Zone, use the AWS CLI command
`aws ec2 describe-instance-type-offerings --location-type availability-zone --filters Name=location,Values=<availability_zone> --region <region> --output text | egrep "<instance_type>"`.

```
aws ec2 create-subnet \
    --vpc-id $VPC_ID \
    --cidr-block 10.0.1.0/24 \
    --availability-zone us-east-1a \
    --query Subnet.SubnetId \
    --output text
aws ec2 create-subnet \
    --vpc-id $VPC_ID \
    --cidr-block 10.0.0.0/24 \
    --availability-zone us-east-1a \
    --query Subnet.SubnetId \
    --output text
```

6. Store the public and private subnet IDs in environment variables.

```
export PUBLIC_SUB=subnet-1234567890abcdef0
export PRIVATE_SUB=subnet-0987654321fedcba0
```

7. Create the following tags for your VPC subnets.
   ROSA uses automated preflight checks that verify that these tags are used.

###### Note

You must tag at least one private subnet and, if applicable, one public subnet.

```
aws ec2 create-tags --resources $PUBLIC_SUB --tags Key=kubernetes.io/role/elb,Value=1
aws ec2 create-tags --resources $PRIVATE_SUB --tags Key=kubernetes.io/role/internal-elb,Value=1
```

8. Create an internet gateway and a route table for outbound traffic.
   Create a route table and elastic IP address for private traffic.

```
aws ec2 create-internet-gateway \
    --query InternetGateway.InternetGatewayId \
    --output text
aws ec2 create-route-table \
    --vpc-id $VPC_ID \
    --query RouteTable.RouteTableId \
    --output text
aws ec2 allocate-address \
    --domain vpc \
    --query AllocationId \
    --output text
aws ec2 create-route-table \
    --vpc-id $VPC_ID \
    --query RouteTable.RouteTableId \
    --output text
```

9. Store the IDs in environment variables.

```
export IGW=igw-1234567890abcdef0
export PUBLIC_RT=rtb-0987654321fedcba0
export EIP=eipalloc-0be6ecac95EXAMPLE
export PRIVATE_RT=rtb-1234567890abcdef0
```

10. Attach the internet gateway to the VPC.

```
aws ec2 attach-internet-gateway \
    --vpc-id $VPC_ID \
    --internet-gateway-id $IGW
```

11. Associate the public route table to the public subnet, and configure traffic to route to the internet gateway.

```
aws ec2 associate-route-table \
    --subnet-id $PUBLIC_SUB \
    --route-table-id $PUBLIC_RT
aws ec2 create-route \
    --route-table-id $PUBLIC_RT \
    --destination-cidr-block 0.0.0.0/0 \
    --gateway-id $IGW
```

12. Create the NAT gateway and associate it with the elastic IP address to enable traffic to the private subnet.

```
aws ec2 create-nat-gateway \
    --subnet-id $PUBLIC_SUB \
    --allocation-id $EIP \
    --query NatGateway.NatGatewayId \
    --output text
```

13. Associate the private route table to the private subnet, and configure traffic to route to the NAT gateway.

```
aws ec2 associate-route-table \
    --subnet-id $PRIVATE_SUB \
    --route-table-id $PRIVATE_RT
aws ec2 create-route \
    --route-table-id $PRIVATE_RT \
    --destination-cidr-block 0.0.0.0/0 \
    --gateway-id $NATGW
```

14. (Optional) For multi-AZ deployments, repeat the above steps to configure two more Availability Zones with public and private subnets.

## Create the required IAM roles and OpenID Connect configuration

Before creating a ROSA with HCP cluster, you must create the necessary IAM roles and policies and the OpenID Connect (OIDC) configuration.
For more information about IAM roles and policies for ROSA with HCP, see [AWS managed policies for ROSA](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

This procedure uses the `auto` mode of the ROSA CLI to automatically create the OIDC configuration necessary to create a ROSA with HCP cluster.

1. Create the required IAM account roles and policies. The `--force-policy-creation` parameter updates any existing roles and policies that are present.
   If no roles and policies are present, the command creates these resources instead.

```
rosa create account-roles --force-policy-creation
```

###### Note

If your offline access token has expired, the ROSA CLI outputs an error message stating that your authorization token needs updated.
For steps to troubleshoot, see [Troubleshoot ROSA CLI expired offline access tokens](troubleshooting-rosa.md#rosa-cli-expired-token "troubleshooting-rosa.md#rosa-cli-expired-token"). 2. Create the OpenID Connect (OIDC) configuration that enables user authentication to the cluster.
This configuration is registered to be used with OpenShift Cluster Manager (OCM).

```
rosa create oidc-config --mode=auto
```

3. Copy the OIDC config ID provided in the ROSA CLI output.
   The OIDC config ID needs to be provided later to create the ROSA with HCP cluster.
4. To verify the OIDC configurations available for clusters associated with your user organization, run the following command.

```
rosa list oidc-config
```

5. Create the required IAM operator roles, replacing `<OIDC_CONFIG_ID>` with the OIDC config ID copied previously.

###### Example

###### Important

You must supply a prefix in `<PREFIX_NAME>` when creating the Operator roles. Failing to do so produces an error.

```
rosa create operator-roles --prefix <PREFIX_NAME> --oidc-config-id <OIDC_CONFIG_ID> --hosted-cp
```

6. To verify the IAM operator roles were created, run the following command:

```
rosa list operator-roles
```

## Create a ROSA with HCP cluster using the ROSA CLI and AWS STS

You can create a ROSA with HCP cluster using AWS Security Token Service (AWS STS) and the `auto` mode that’s provided in the ROSA CLI.
You have the option to create a cluster with a public API and Ingress or a private API and Ingress.

You can create a cluster with a single Availability Zone (Single-AZ) or multiple Availability Zones (Multi-AZ).
In either case, your machine’s CIDR value must match your VPC’s CIDR value.

The following procedure uses the `rosa create cluster --hosted-cp` command to create a Single-AZ ROSA with HCP cluster.
To create a Multi-AZ cluster, specify `multi-az` in the command and the private subnet IDs for each private subnet you want you to deploy to.

1. Create a ROSA with HCP cluster with one of the following commands.
   - Create a ROSA with HCP cluster with a public API and Ingress, specifying the cluster name, operator role prefix, OIDC config ID, and public and private subnet IDs.

   ```
   rosa create cluster --cluster-name=<CLUSTER_NAME> --sts --mode=auto --hosted-cp --operator-roles-prefix <OPERATOR_ROLE_PREFIX> --oidc-config-id <OIDC_CONFIG_ID> --subnet-ids=<PUBLIC_SUBNET_ID>,<PRIVATE_SUBNET_ID>
   ```

   - Create a ROSA with HCP cluster with a private API and Ingress, specifying the cluster name, operator role prefix, OIDC config ID, and private subnet IDs.

   ```
   rosa create cluster --private --cluster-name=<CLUSTER_NAME> --sts --mode=auto --hosted-cp --subnet-ids=<PRIVATE_SUBNET_ID>
   ```

2. Check the status of your cluster.

```
rosa describe cluster -c <CLUSTER_NAME>
```

###### Note

If the creation process fails or the `State` field doesn’t change to a ready status after 10 minutes, see [Troubleshooting](troubleshooting-rosa.md "troubleshooting-rosa.md").

To contact Support or Red Hat support for assistance, see [Getting ROSA support](rosa-support.md "rosa-support.md"). 3. Track the progress of the cluster creation by watching the OpenShift installer logs.

```
rosa logs install -c <CLUSTER_NAME> --watch
```

## Configure an identity provider and grant cluster access

ROSA includes a built-in OAuth server.
After your cluster is created, you must configure OAuth to use an identity provider.
You can then add users to your configured identity provider to grant them access to your cluster.
You can grant these users `cluster-admin` or `dedicated-admin` permissions as required.

You can configure different identity provider types for your ROSA
cluster.
Supported types include GitHub, GitHub Enterprise, GitLab, Google, LDAP, OpenID Connect, and HTPasswd identity providers.

###### Important

The HTPasswd identity provider is included only to enable a single, static administrator user to be created.
HTPasswd isn’t supported as a general-use identity provider for ROSA.

The following procedure configures a GitHub identity provider as an example.
For instructions on how to configure each of the supported identity provider types, see [Configuring identity providers for AWS STS](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/install_rosa_classic_clusters/rosa-sts-config-identity-providers "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/install_rosa_classic_clusters/rosa-sts-config-identity-providers").

1. Navigate to [github.com](https://github.com/ "https://github.com/") and log in to your GitHub account.
2. If you don’t have a GitHub organization to use for identity provisioning for your cluster, create one.
   For more information, see [the steps in the GitHub documentation](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch "https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch").
3. Using the ROSA CLI’s interactive mode, configure an identity provider for your cluster.

```
rosa create idp --cluster=<CLUSTER_NAME> --interactive
```

4. Follow the configuration prompts in the output to restrict cluster access to members of your GitHub organization.

```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Type of identity provider: github
? Identity provider name: github-1
? Restrict to members of: organizations
? GitHub organizations: <GITHUB_ORG_NAME>
? To use GitHub as an identity provider, you must first register the application:
  - Open the following URL:
    https://github.com/organizations/<GITHUB_ORG_NAME>/settings/applications/new?oauth_application%5Bcallback_url%5D=https%3A%2F%2Foauth-openshift.apps.<CLUSTER_NAME>/<RANDOM_STRING>.p1.openshiftapps.com%2Foauth2callback%2Fgithub-1&oauth_application%5Bname%5D=<CLUSTER_NAME>&oauth_application%5Burl%5D=https%3A%2F%2Fconsole-openshift-console.apps.<CLUSTER_NAME>/<RANDOM_STRING>.p1.openshiftapps.com
  - Click on 'Register application'
...
```

5. Open the URL in the output, replacing `<GITHUB_ORG_NAME>` with the name of your GitHub organization.
6. On the GitHub web page, choose **Register application** to register a new OAuth application in your GitHub organization.
7. Use the information from the GitHub OAuth page to populate the remaining `rosa create idp` interactive prompts by running the following command.
   Replace `<GITHUB_CLIENT_ID>` and `<GITHUB_CLIENT_SECRET>` with the credentials from your GitHub OAuth application.

```
...
? Client ID: <GITHUB_CLIENT_ID>
? Client Secret: [? for help] <GITHUB_CLIENT_SECRET>
? GitHub Enterprise Hostname (optional):
? Mapping method: claim
I: Configuring IDP for cluster '<CLUSTER_NAME>'
I: Identity Provider 'github-1' has been created.
   It will take up to 1 minute for this configuration to be enabled.
   To add cluster administrators, see 'rosa grant user --help'.
   To login into the console, open https://console-openshift-console.apps.<CLUSTER_NAME>.<RANDOM_STRING>.p1.openshiftapps.com and click on github-1.
```

###### Note

It might take approximately two minutes for the identity provider configuration to become active.
If you configured a `cluster-admin` user, you can run `oc get pods -n openshift-authentication --watch` to watch the OAuth pods redeploy with the updated configuration. 8. Verify that the identity provider is configured correctly.

```
rosa list idps --cluster=<CLUSTER_NAME>
```

## Grant user access to a cluster

You can grant a user access to your cluster by adding them to the configured identity provider.

The following procedure adds a user to a GitHub organization that’s configured for identity provisioning to the cluster.

1. Navigate to [github.com](https://github.com/ "https://github.com/") and log in to your GitHub account.
2. Invite users that require cluster access to your GitHub organization.
   For more information, see [Inviting users to join your organization](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization "https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization") in the GitHub documentation.

## Configure `cluster-admin` permissions

1. Grant the `cluster-admin` permissions by running the following command.
   Replace `<IDP_USER_NAME>` and `<CLUSTER_NAME>` with your user and cluster name.

```
rosa grant user cluster-admin --user=<IDP_USER_NAME> --cluster=<CLUSTER_NAME>
```

2. Verify that the user is listed as a member of the `cluster-admins` group.

```
rosa list users --cluster=<CLUSTER_NAME>
```

## Configure `dedicated-admin` permissions

1. Grant the `dedicated-admin` permissions by using the following command. Replace `<IDP_USER_NAME>` and `<CLUSTER_NAME>` with your user and cluster name by running the following command.

```
rosa grant user dedicated-admin --user=<IDP_USER_NAME> --cluster=<CLUSTER_NAME>
```

2. Verify that the user is listed as a member of the `cluster-admins` group.

```
rosa list users --cluster=<CLUSTER_NAME>
```

## Access a cluster through the Red Hat Hybrid Cloud Console

Log in to your cluster through the Red Hat Hybrid Cloud Console.

1. Obtain the console URL for your cluster using the following command.
   Replace `<CLUSTER_NAME>` with the name of your cluster.

```
rosa describe cluster -c <CLUSTER_NAME> | grep Console
```

2. Navigate to the console URL in the output and log in.

In the **Log in with…​** dialog, choose the identity provider name and complete any authorization requests presented by your provider.

## Deploy an application from the Developer Catalog

From the Red Hat Hybrid Cloud Console, you can deploy a Developer Catalog test application and expose it with a route.

1. Navigate to [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift "https://console.redhat.com/openshift") and choose the cluster you want to deploy the app into.
2. On the cluster’s page, choose **Open console**.
3. In the **Administrator** perspective, choose **Home** > **Projects** > **Create Project**.
4. Enter a name for your project and optionally add a **Display Name** and **Description**.
5. Choose **Create** to create the project.
6. Switch to the **Developer** perspective and choose **+Add**.
   Make sure that the selected project is the one that was just created.
7. In the **Developer Catalog** dialog, choose **All services**.
8. In the **Developer Catalog** page, choose **Languages** > **JavaScript** from the menu.
9. Choose **Node.js**, and then choose **Create Application** to open the **Create Source-to-Image Application** page.

###### Note

You might need to choose **Clear All Filters** to display the **Node.js** option. 10. In the **Git** section, choose **Try Sample**. 11. In the **Name** field, add a unique name. 12. Choose **Create**.

###### Note

The new application takes several minutes to deploy. 13. When the deployment is complete, choose the route URL for the application.

A new tab in the browser opens with a message that’s similar to the following.

```
Welcome to your Node.js application on OpenShift
```

14. (Optional) Delete the application and clean up resources:
    1.  In the **Administrator** perspective, choose **Home** > **Projects**.
    2.  Open the action menu for your project and choose **Delete Project**.

## Revoke `cluster-admin` permissions from a user

1. Revoke the `cluster-admin` permissions using the following command. Replace `<IDP_USER_NAME>` and `<CLUSTER_NAME>` with your user and cluster name.

```
rosa revoke user cluster-admin --user=<IDP_USER_NAME> --cluster=<CLUSTER_NAME>
```

2. Verify that the user isn’t listed as a member of the `cluster-admins` group.

```
rosa list users --cluster=<CLUSTER_NAME>
```

## Revoke `dedicated-admin` permissions from a user

1. Revoke the `dedicated-admin` permissions by using the following command. Replace `<IDP_USER_NAME>` and `<CLUSTER_NAME>` with your user and cluster name.

```
rosa revoke user dedicated-admin --user=<IDP_USER_NAME> --cluster=<CLUSTER_NAME>
```

2. Verify that the user isn’t listed as a member of the `dedicated-admins` group.

```
rosa list users --cluster=<CLUSTER_NAME>
```

## Revoke user access to a cluster

You can revoke cluster access for an identity provider user by removing them from the configured identity provider.

You can configure different types of identity providers for your cluster. The following procedure revokes cluster access for a member of a GitHub organization.

1. Navigate to [github.com](https://github.com/ "https://github.com/") and log in to your GitHub account.
2. Remove the user from your GitHub organization. For more information, see [Removing a member from your organization](https://docs.github.com/en/organizations/managing-membership-in-your-organization/removing-a-member-from-your-organization "https://docs.github.com/en/organizations/managing-membership-in-your-organization/removing-a-member-from-your-organization") in the GitHub documentation.

## Delete a cluster and AWS STS resources

You can use the ROSA CLI to delete a cluster that uses AWS Security Token Service (AWS STS).
You can also use the ROSA CLI to delete the IAM roles and OIDC provider created by ROSA.
To delete the IAM policies created by ROSA, you can use the IAM console.

###### Note

IAM roles and policies created by ROSA might be used by other ROSA clusters in the same account.

1. Delete the cluster and watch the logs. Replace `<CLUSTER_NAME>` with the name or ID of your cluster.

```
rosa delete cluster --cluster=<CLUSTER_NAME> --watch
```

###### Important

You must wait for the cluster to delete completely before you remove the IAM roles, policies, and OIDC provider.
The account IAM roles are required to delete the resources created by the installer.
The operator IAM roles are required to clean up the resources created by the OpenShift operators.
The operators use the OIDC provider to authenticate. 2. Delete the OIDC provider that the cluster operators use to authenticate by running the following command.

```
rosa delete oidc-provider -c <CLUSTER_ID> --mode auto
```

3. Delete the cluster-specific operator IAM roles.

```
rosa delete operator-roles -c <CLUSTER_ID> --mode auto
```

4. Delete the account IAM roles using the following command.
   Replace `<PREFIX>` with the prefix of the account IAM roles to delete.
   If you specified a custom prefix when creating the account IAM roles, specify the default `ManagedOpenShift` prefix.

```
rosa delete account-roles --prefix <PREFIX> --mode auto
```

5. Delete the IAM policies created by ROSA.
   1. Log in to the [IAM console](https://console.aws.amazon.com/iamv2/home#/home "https://console.aws.amazon.com/iamv2/home#/home").
   2. On the left menu under **Access management**, choose **Policies**.
   3. Select the policy that you want to delete and choose **Actions** > **Delete**.
   4. Enter the policy name and choose **Delete**.
   5. Repeat this step to delete each of the IAM policies for the cluster.

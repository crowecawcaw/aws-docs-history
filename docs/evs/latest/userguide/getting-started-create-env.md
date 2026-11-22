

# Create an environment

This page applies to EVS-deployed environments (VCF 5.2.x). For Self-deployed environments that run VCF 9.x, see [Deploy in Self-deployed mode](getting-started-self-deployed.md).

Create an Amazon Elastic VMware Service environment in EVS-deployed mode with the Amazon EVS console or the AWS CLI. In this mode, environment creation adds the hosts and deploys VMware Cloud Foundation (VCF) on them. In Self-deployed mode, you add hosts and install VCF after you create the environment.

**Important**  
You can configure an environment only when you create it. You can’t change the environment settings after you create it. You can’t add VLAN subnets or change their CIDR blocks after you create the environment. For an overview of all environment settings, see the [Amazon EVS API Reference Guide](https://docs.aws.amazon.com/evs/latest/APIReference/Welcome.html).

## Before you begin
<a name="create-env-evs-deployed-before-you-begin"></a>

Complete the following tasks before you create the environment.
+ Check that you meet the Amazon EVS service requirements. Environment deployment fails if they aren’t met. For more information, see [Prepare your AWS account](setting-up.md).
+ Build the network foundation in the same Region and Availability Zone where you create the environment. This includes the VPC, the service access subnet, DNS and NTP, a route server in Amazon VPC Route Server with two endpoints and two peers, and a network ACL. For more information, see [Build the network foundation](network-foundation.md).
+ Size the Amazon EVS VLAN subnets. You can’t add VLAN subnets or change their CIDR blocks after you create the environment. For more information, see [Plan your VPC and VLAN subnets](plan-network-sizing.md) and [VLAN subnets, VLAN IDs, and IP addresses](vlan-subnet-reference.md).
+ If you plan to use HCX over the internet, create a custom network ACL for the HCX VLAN. We recommend a dedicated network ACL so that you can control HCX internet traffic separately. For more information, see [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md).
+ If you plan to use HCX over the internet, create the IPAM, the Elastic IP addresses, and the public CIDR block in your VPC. For the steps, see Part 1 of [Configure HCX public internet connectivity](evs-env-hcx-internet-access.md).
+ Have your Broadcom Site ID, a VCF solution key (VMware vSphere 8 Enterprise Plus for VCF), and a vSAN license key. For the license requirements, see [License key requirements](#license-keys-evs-deployed).
+ Create a DNS A record in a forward lookup zone and a PTR record in a reverse lookup zone for each host and each VCF management appliance. For the list of records, see [Deployment prerequisite checklist](evs-deployment-prereq-checklist.md).
+ Create an Amazon EC2 key pair for SSH access to the hosts.

### License key requirements
<a name="license-keys-evs-deployed"></a>

Your license keys must meet the following requirements.
+ The VCF solution key must have sufficient cores, and the vSAN license key must have sufficient vSAN capacity. The thresholds depend on the instance type. For more information, see [VCF licensing](vcf-license-mgmt.md).
+ Neither key can be in use by an existing Amazon EVS environment.
+ Amazon EVS doesn’t validate license keys. To validate them, go to [Broadcom support](https://support.broadcom.com/web/ecx).
+ You must keep a valid VCF solution key and vSAN license key in SDDC Manager for the service to function. If you manage the keys in the vSphere Client after deployment, make sure that they also appear on the licensing screen of SDDC Manager.
+ Your VCF subscription and your environment ID are available to Amazon EVS across all AWS Regions for license compliance.

## Create the environment
<a name="create-env-evs-deployed-procedure"></a>

Environment creation can take several hours.

**Important**  
The hosts that Amazon EVS deploys in your account incur charges. For prices, see [Amazon EVS pricing](https://aws.amazon.com/evs/pricing). To stop the charges, delete the environment as described in [Delete an EVS-deployed environment](getting-started-cleanup-env-hosts.md).

You can create the environment by using the Amazon EVS console or the AWS CLI.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs). Check that the AWS Region in the upper right of the console is the Region where you want to create the environment. To change it, choose the Region name and choose another Region.

1. In the navigation pane, choose **Environments**.

1. Choose **Create environment**.

1. On the **Validate Amazon EVS requirements** page, check that the service requirements are met, and then do the following.

   1. (Optional) For **Name**, enter an environment name.

   1. For **Environment version**, choose your VCF version. For the versions that Amazon EVS provides, see [Supported VCF versions and instance types](versions-provided.md). The list also includes a **Self-deployed** option. If you choose it, the wizard follows the Self-deployed flow instead of these steps. For more information, see [Deploy in Self-deployed mode](getting-started-self-deployed.md).

   1. For **Site ID**, enter your Broadcom Site ID.

   1. For **VCF Solution key**, enter a VCF solution key (VMware vSphere 8 Enterprise Plus for VCF).

   1. For **vSAN license key**, enter a vSAN license key.

   1. For **VCF license terms**, select the check box. You confirm that you have purchased, and will continue to maintain, VCF software licenses that cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS is shared with Broadcom to verify license compliance.

   1. Choose **Next**.

1. On the **Specify host details** page, add the four hosts that Amazon EVS requires for initial deployment. For each host, do the following.

   1. Choose **Add host details**.

   1. For **DNS hostname**, enter the host name for the host.

   1. For **instance type**, choose the Amazon EC2 instance type.

   1. For **ESX host version**, Amazon EVS uses the default ESX version for the VCF version that you chose. For more information, see [Supported VCF versions and instance types](versions-provided.md).

   1. For **SSH key pair**, choose an SSH key pair for SSH access to the host.

   1. Choose **Add host**.

1. On the **Configure networks and connectivity** page, do the following.

   1. For **HCX connectivity requirements**, choose whether to use HCX with private connectivity or over the internet. For help with the choice, see [Plan HCX connectivity](plan-hcx-connectivity.md).

   1. For **VPC**, choose the VPC that you created.

   1. (HCX internet connectivity only) For **HCX network ACL**, choose the network ACL to associate with the HCX VLAN.

   1. For **Service access subnet**, choose the private subnet that you created with the VPC.

   1. (Optional) For **Security group**, choose up to two security groups that control communication between the Amazon EVS control plane and the VPC. If you choose none, Amazon EVS uses the default security group. The security groups must allow connectivity to your DNS servers and the Amazon EVS VLAN subnets.

   1. Under **Management connectivity**, enter the CIDR blocks for the Amazon EVS VLAN subnets. For a public HCX VLAN, the netmask length must be exactly /28. For a private HCX VLAN and all other VLAN subnets, the netmask length must be /28 to /24. You can’t add VLAN subnets or change their CIDR blocks after you create the environment.

   1. Under **Expansion VLANs**, enter the CIDR blocks for additional Amazon EVS VLAN subnets. You can use them to expand VCF capabilities, such as NSX Federation.

   1. Under **Workload/VCF connectivity**, enter the CIDR block for the NSX uplink VLAN. Then choose the two route server peer IDs that peer with the route server endpoints over the NSX uplink. For more information, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md).

   1. Choose **Next**.

1. On the **Specify Management DNS hostnames** page, do the following.

   1. Under **Management appliance DNS hostnames**, enter the DNS host names for the virtual machines that host the VCF management appliances. If you use Route 53 for DNS, also choose the hosted zone that contains your DNS records.

   1. Under **Credentials**, choose the AWS managed KMS key for Secrets Manager or a customer managed KMS key that you provide. The key encrypts the VCF credentials for SDDC Manager, NSX Manager, and vCenter. Customer managed KMS keys have usage costs. For more information, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing).

   1. Choose **Next**.

1. (Optional) On the **Add tags** page, add tags for the environment and choose **Next**.

1. On the **Review and create** page, review your configuration and choose **Create environment**.

1. Open a terminal session.

1. Run the `aws evs create-environment` command. Specify the following parameters.
   + For `--vpc-id`, specify the VPC that you created, with a minimum IPv4 CIDR range of /22.
   + For `--service-access-subnet-id`, specify the ID of the private subnet that you created with the VPC.
   + For `--vcf-version`, specify the VCF version. For the versions that Amazon EVS provides, see [Supported VCF versions and instance types](versions-provided.md).
   + With `--terms-accepted`, you confirm that you have purchased, and will continue to maintain, VCF software licenses that cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS is shared with Broadcom to verify license compliance.
   + For `--license-info`, specify your VCF solution key (VMware vSphere 8 Enterprise Plus for VCF) and your vSAN license key.
   + For `--initial-vlans`, specify the CIDR blocks for the Amazon EVS VLAN subnets that Amazon EVS creates for you. The VCF management appliances are deployed on these VLAN subnets. For a public HCX VLAN, the netmask length must be exactly /28. For a private HCX VLAN and all other VLAN subnets, the netmask length must be /28 to /24. You can’t add VLAN subnets or change their CIDR blocks after you create the environment.
   + Use `hcxNetworkAclId` in `--initial-vlans` only for HCX internet connectivity. Specify the custom network ACL for the public HCX VLAN.
   + For `--hosts`, specify the four hosts that Amazon EVS requires for environment deployment. For each host, include the DNS host name, the EC2 SSH key name, and the EC2 instance type. The dedicated host ID is optional.
   + For `--connectivity-info`, specify the two route server peer IDs that you created. For more information, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md).
   + For `--vcf-hostnames`, specify the DNS host names for the virtual machines that host the VCF management appliances.
   + For `--site-id`, specify your Broadcom Site ID. Broadcom gives you this ID at the close of your software contract or contract renewal.
   + (Optional) For `--region`, specify the Region for the environment. If you don’t specify it, your default Region is used.

     The following is a sample request. Replace the example IDs, names, and CIDR blocks with your own values. Each VLAN CIDR block must be inside a CIDR block of your VPC. The sample uses a private HCX VLAN subnet. For HCX over the internet, use a public /28 CIDR block from your IPAM pool for `hcx`, set `isHcxPublic` to `true`, and set `hcxNetworkAclId` to the ID of your network ACL (it starts with `acl-`). For the steps, see [Configure HCX public internet connectivity](evs-env-hcx-internet-access.md). Replace `<region-code>` with the Region where you want to create the environment.

     ```bash
     aws evs create-environment \
     --environment-name testEnv \
     --vpc-id vpc-1234567890abcdef0 \
     --service-access-subnet-id subnet-01234a1b2cde1234f \
     --vcf-version VCF-5.2.2 \
     --terms-accepted \
     --license-info "{
           \"solutionKey\": \"00000-00000-00000-abcde-11111\",
           \"vsanKey\": \"00000-00000-00000-abcde-22222\"
         }" \
        --initial-vlans "{
           \"vmkManagement\": {
             \"cidr\": \"10.10.0.0/24\"
           },
           \"vmManagement\": {
             \"cidr\": \"10.10.1.0/24\"
           },
           \"vMotion\": {
             \"cidr\": \"10.10.2.0/24\"
           },
           \"vSan\": {
             \"cidr\": \"10.10.3.0/24\"
           },
           \"vTep\": {
             \"cidr\": \"10.10.4.0/24\"
           },
           \"edgeVTep\": {
             \"cidr\": \"10.10.5.0/24\"
           },
           \"nsxUplink\": {
             \"cidr\": \"10.10.6.0/24\"
           },
           \"hcx\": {
             \"cidr\": \"10.10.7.0/24\"
           },
           \"expansionVlan1\": {
             \"cidr\": \"10.10.8.0/24\"
           },
           \"expansionVlan2\": {
               \"cidr\": \"10.10.9.0/24\"
           }
         }" \
     --hosts "[
         {
           \"hostName\": \"esx01\",
           \"keyName\": \"sshKey-04-05-45\",
           \"instanceType\": \"i4i.metal\",
           \"dedicatedHostId\": \"h-07879acf49EXAMPLE\"
         },
         {
           \"hostName\": \"esx02\",
           \"keyName\": \"sshKey-04-05-45\",
           \"instanceType\": \"i4i.metal\",
           \"dedicatedHostId\": \"h-07878bde50EXAMPLE\"
         },
         {
           \"hostName\": \"esx03\",
           \"keyName\": \"sshKey-04-05-45\",
           \"instanceType\": \"i4i.metal\",
           \"dedicatedHostId\": \"h-07877eio51EXAMPLE\"
         },
         {
           \"hostName\": \"esx04\",
           \"keyName\": \"sshKey-04-05-45\",
           \"instanceType\": \"i4i.metal\",
           \"dedicatedHostId\": \"h-07863ghi52EXAMPLE\"
         }
       ]" \
     --connectivity-info "{
         \"privateRouteServerPeerings\": [\"rsp-1234567890abcdef0\",\"rsp-abcdef01234567890\"]
       }" \
       --vcf-hostnames "{
         \"vCenter\": \"vcf-vc01\",
         \"nsx\": \"vcf-nsx\",
         \"nsxManager1\": \"vcf-nsxm01\",
         \"nsxManager2\": \"vcf-nsxm02\",
         \"nsxManager3\": \"vcf-nsxm03\",
         \"nsxEdge1\": \"vcf-edge01\",
         \"nsxEdge2\": \"vcf-edge02\",
         \"sddcManager\": \"vcf-sddcm01\",
         \"cloudBuilder\": \"vcf-cb01\"
       }" \
     --site-id my-site-id \
     --region <region-code>
     ```

     The following is a sample response.

     ```json
     {
         "environment": {
             "environmentId": "env-abcde12345",
             "environmentState": "CREATING",
             "stateDetails": "The environment is being initialized, this operation may take some time to complete.",
             "createdAt": "2025-04-13T12:03:39.718000+00:00",
             "modifiedAt": "2025-04-13T12:03:39.718000+00:00",
             "environmentArn": "arn:aws:evs:us-east-2:111122223333:environment/env-abcde12345",
             "environmentName": "testEnv",
             "vpcId": "vpc-1234567890abcdef0",
             "serviceAccessSubnetId": "subnet-01234a1b2cde1234f",
             "vcfVersion": "VCF-5.2.2",
             "termsAccepted": true,
             "licenseInfo": [
                 {
                     "solutionKey": "00000-00000-00000-abcde-11111",
                     "vsanKey": "00000-00000-00000-abcde-22222"
                 }
             ],
             "siteId": "my-site-id",
             "connectivityInfo": {
                 "privateRouteServerPeerings": [
                     "rsp-1234567890abcdef0",
                     "rsp-abcdef01234567890"
                 ]
             },
             "vcfHostnames": {
                 "vCenter": "vcf-vc01",
                 "nsx": "vcf-nsx",
                 "nsxManager1": "vcf-nsxm01",
                 "nsxManager2": "vcf-nsxm02",
                 "nsxManager3": "vcf-nsxm03",
                 "nsxEdge1": "vcf-edge01",
                 "nsxEdge2": "vcf-edge02",
                 "sddcManager": "vcf-sddcm01",
                 "cloudBuilder": "vcf-cb01"
             }
         }
     }
     ```

     The ARN in the sample uses the `aws` partition. In other partitions, the ARN starts with that partition name.

You have started the creation of an Amazon EVS environment.

## What happens during creation
<a name="create-env-evs-deployed-after"></a>

The following happens when you create the environment.
+ Amazon EVS creates the Amazon EVS VLAN subnets and implicitly associates them with the main route table of the VPC. After deployment completes, you must explicitly associate the VLAN subnets with a route table for NSX connectivity. For more information, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md).
+ Hosts that are created with the environment receive the tag `DoNotDelete-EVS-[<environmentId>]-[<hostname>]`.
+ Tags that you add to the environment don’t propagate to the underlying AWS resources, such as EC2 instances. You can tag those resources with the console of the respective service or the AWS CLI.

**Warning**  
Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. To create, replace, or delete a host, use the Amazon EVS console, the AWS CLI, or the Amazon EVS API.

**Note**  
Amazon EVS deploys a recent bundled version of VCF that might not include individual product updates (async patches).

After deployment completes, we recommend that you review and update the individual products so that they include the latest fixes. You can use the Broadcom Async Patch Tool (AP Tool) or the SDDC Manager in-product lifecycle management (LCM) automation. For more information, see [Update and upgrade](evs-lifecycle-mgmt.md).

**Important**  
You must upgrade NSX outside of SDDC Manager.

## Next step
<a name="create-env-evs-deployed-next"></a>

 [Verify environment creation](verify-env-creation.md) 
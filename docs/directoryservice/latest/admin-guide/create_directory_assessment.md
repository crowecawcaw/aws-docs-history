# Creating directory assessments

You can create a directory assessment as part of creating a hybrid directory, or you can create one
manually. To create an assessment manually, open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/"). On the
**Directories** page, under the **Directory assessments** section,
choose **Create assessment**.

###### To create a directory assessment

1. On the **Create directory assessment** page, for **Directory DNS
   name**, enter your self-managed Active Directory DNS name.
2. For **DNS IP Addresses**, enter two DNS IP addresses for your
   self-managed AD.
3. Hybrid directory requires a Amazon VPC with at least two subnets. If you don't already
   have these, you can create them. In the **Networking** section,
   provide the following:
   1. For **VPC**, choose your VPC identifier.
   2. For **Subnets**, choose the identifier for each of
      the two subnets. Each subnet must be in different Availability Zones.
      For more information, see [Amazon VPC network requirements](create_hybrid_directory_prereqs.md#hybrid-dir-prereqs-vpc "create_hybrid_directory_prereqs.md#hybrid-dir-prereqs-vpc").
   3. For **Security group**, choose the security group
      identifier. By default, AWS attaches a security group to allow network
      access to the AWS Secrets Manager managed nodes in your Amazon VPC. You can optionally
      supply your own security group that allows network traffic to and from
      your self-managed domain controllers outside of your Amazon VPC.

4. In the **AWS Systems Manager nodes** section, choose two Systems Manager nodes or
   instances based on the following requirements:
   - If your Active Directory is **self-managed outside of the
     AWS Cloud**, you will need two Systems Manager node
     for a hybrid and multicloud environment. For more
     information on how to provision these nodes, see [Setting up Systems Manager for hybrid and multicloud
     environments](../../../systems-manager/latest/userguide/systems-manager-hybrid-multicloud.md "../../../systems-manager/latest/userguide/systems-manager-hybrid-multicloud.md").
   - If your Active Directory is **self-managed within the AWS Cloud**,
     you will need two Systems Manager managed EC2 instances. For more
     information on how to provision these instances, see [Managing EC2 instances with Systems Manager](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md").

5. Choose **Next** to open the **Review and create
   directory assessment** page.
6. On the **Review and create directory assessment** page, review the directory assessment
   information and make any necessary changes. When the information is correct,
   choose **Create assessment**. Creating the directory assessment takes around 30
   minutes. You're returned to the Directories details page. A green banner appears
   when the directory assessment succeeds.

###### Warning

To create a hybrid directory, the directory assessment must enter a
**`SUCCESS`** state. You can't create a hybrid directory
without first successfully passing a directory assessment.

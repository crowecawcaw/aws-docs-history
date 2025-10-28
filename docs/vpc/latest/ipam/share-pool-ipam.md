# Share an IPAM pool using AWS RAM

Follow the steps in this section to share an IPAM pool using AWS Resource Access Manager
(RAM). When you share an IPAM pool with RAM, “principals” can allocate CIDRs from the pool
to AWS resources, such as VPCs, from their respective accounts. A principal is a concept
in RAM that means any AWS account, IAM role or organizational unit in AWS Organizations.
For more information, see [Sharing
your AWS resources](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md") in the _AWS RAM User
Guide_.

###### Note

- You can only share an IPAM pool with AWS RAM if you've integrated IPAM with AWS Organizations. For
  more information, see [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md "enable-integ-ipam.md"). You cannot share an
  IPAM pool with AWS RAM if you are a single account IPAM user.
- You must enable resource sharing with AWS Organizations in AWS RAM. For
  more information, see [Enable resource sharing within AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS RAM User Guide_.
- RAM sharing is only available in the home AWS Region of your IPAM. You must create the share in
  the AWS Region that the IPAM is in, not in the Region of the IPAM pool.
- The account that creates and deletes IPAM pool resource shares must have the
  following permissions in the IAM policy attached to their IAM role:
  - `ec2:PutResourcePolicy`
  - `ec2:DeleteResourcePolicy`

- You can add multiple IPAM pools to a RAM share.
- While you can share IPAM pools with any AWS account outside an AWS Organization, IPAM will only monitor the IP addresses in accounts outside the Organization if the account owner has gone through the process of sharing their resource discovery with the delegated IPAM admin as described in [Integrate IPAM with accounts outside of your organization](enable-integ-ipam-outside-org.md "enable-integ-ipam-outside-org.md").

AWS Management Console

###### To share an IPAM pool using RAM

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. By default, the default private scope is selected. If you don’t want to use the default
   private scope, from the dropdown menu at the top of the content pane, choose the scope you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. In the content pane, choose the pool you want to share and choose **Actions** > **View details**.
5. Under **Resource sharing**, choose **Create resource share**. As a result, the AWS RAM console opens. You'll create the shared pool in AWS RAM.
6. Choose **Create a resource share**.
7. Add a **Name** for the shared resource.
8. Under **Select resource type**, select IPAM pools and choose
   one or more IPAM pools.
9. Choose **Next**.
10. Choose one of the permissions for the resource share:
    - **AWSRAMDefaultPermissionsIpamPool**: Choose this permission to
      allow principals to view the CIDRs and allocations in the shared
      IPAM pool and allocate/release CIDRs in the pool.
    - **AWSRAMPermissionIpamPoolByoipCidrImport**: Choose this
      permission to allow principals to import BYOIP CIDRs into the shared IPAM pool. You will
      need this permission only if you have existing BYOIP CIDRs and you want to import them to IPAM and
      share them with principals. For additional information on BYOIP CIDRs to IPAM,
      see [Tutorial: Transfer a BYOIP IPv4 CIDR to IPAM](tutorials-byoip-ipam-transfer-ipv4.md "tutorials-byoip-ipam-transfer-ipv4.md").

11. Choose the principals that are allowed to access this resource. If principals will be importing existing BYOIP CIDRs
    to this shared IPAM pool, add the BYOIP CIDR owner account as principal.
12. Review the resource share options and the principals you’ll be sharing with and choose **Create**.

Command line
The command(s) in this section link to the _AWS CLI Command Reference_. There you’ll find detailed descriptions
of the options you can use when you run the command(s).

Use the following AWS CLI commands to share an IPAM pool using RAM:

1. Get the ARN of the IPAM: [describe-ipam-pools](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md")
2. Create the resource share: [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md")
3. View the resource share: [get-resource-shares](../../../cli/latest/reference/ram/get-resource-shares.md "../../../cli/latest/reference/ram/get-resource-shares.md")

As a result of creating the resource share in RAM, other principals can now allocate CIDRs
to resources using the IPAM pool. For information on monitoring resources
created by principals, see [Monitor CIDR usage by resource](monitor-cidr-compliance-ipam.md "monitor-cidr-compliance-ipam.md"). For more information
on how to create a VPC and allocate a CIDR from a shared IPAM pool, see [Create a VPC](../userguide/create-vpc.md "../userguide/create-vpc.md") in the _Amazon VPC User Guide_.

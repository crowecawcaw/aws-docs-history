

# Using the Neptune-Export service to export Neptune data
<a name="export-service"></a>

You can use the following steps to export data from your Neptune DB cluster to Amazon S3 using the Neptune-Export service:

## Installing the Neptune-Export service
<a name="export-service-install"></a>

Use an AWS CloudFormation template to create the stack:

**To install the Neptune-Export service**

1. Launch the CloudFormation stack on the CloudFormation console by choosing one of the **Launch Stack** buttons in the following table:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/neptune/latest/userguide/export-service.html)

1.  On the **Select Template** page, choose **Next**.

1. On the **Specify Details** page, the template, set the following parameters:
   + **`VPC`**   –   The easiest way to set up the Neptune-Export service is to install it in the same Amazon VPC as your Neptune database. If you want to install it in a separate VPC you can use [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) to establish connectivity between the Neptune DB cluster's VPC and the Neptune-Export service VPC.
   + **`Subnet1`**   –   The Neptune-Export service must be installed in a subnet in your VPC that allows outbound IPv4 HTTPS traffic from the subnet to the internet. This is so that the Neptune-Export service can call the [AWS Batch API](https://aws.amazon.com/premiumsupport/knowledge-center/batch-job-stuck-runnable-status/) to create and run an export job.

     If you created your Neptune cluster using the CloudFormation template on the [Create Neptune cluster](get-started-create-cluster.md) page in the Neptune documentation, you can use the `PrivateSubnet1` and `PrivateSubnet2` outputs from that stack to populate this and the next parameter.
   + **`Subnet2`**   –   A second subnet in the VPC that allows outbound IPv4 HTTPS traffic from the subnet to the internet.
   + **`EnableIAM`**   –   Set this to `true` to secure the Neptune-Endpoint API using AWS Identity and Access Management (IAM). We recommend that you do so.

     If you do enable IAM authentication, you must `Sigv4` sign all HTTPS requests to the endpoint. You can use a tool such as [awscurl](https://github.com/okigan/awscurl) to sign requests on your behalf.
   + **`VPCOnly`**   –   Setting this to `true` makes the export endpoint VPC-only, so that you can only access it from within the VPC where the Neptune-Export service is installed. This restricts the Neptune-Export API to being used only from within that VPC.

     We recommend that you set `VPCOnly` to `true`.
   + **`NumOfFilesULimit `**   –   Specify a value between 10,000 and 1,000,000 for `nofile` in the `ulimits` container property. The default is 10,000, and we recommend keeping the default unless your graph contains a large number of unique labels.
   + **`PrivateDnsEnabled `** (Boolean)   –   Indicates whether to associate a private hosted zone with the specified VPC or not. The default value is `true`.

     When a VPC endpoint is created with this flag enabled, all API Gateway traffic is routed through the VPC endpoint, and public API Gateway endpoint calls becomes disabled. If you set `PrivateDnsEnabled` to `false`, the public API Gateway endpoint is enabled, but the Neptune export service cannot be connected through the private DNS endpoint. You can then use a public DNS endpoint for the VPC endpoint to call the export service, as detailed [here](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-api-test-invoke-url.html#apigateway-private-api-public-dns).
   +  **`NeptuneExportVersion`**   –   Specify the version of the Neptune Export Utility to be used. All versions greater than or equal to `v1.1.11` are supported. A version of `v2.latest` may be used to automatically receive minor updates. The full list of available versions, as well as patch notes can be found in the open source [GitHub releases](https://github.com/aws/neptune-export/releases). 

1. Choose **Next**.

1. On the **Options** page, choose **Next**.

1. On the **Review** page, select the first check box to acknowledge that CloudFormation will create IAM resources. Select the second check box to acknowledge `CAPABILITY_AUTO_EXPAND` for the new stack. 
**Note**  
`CAPABILITY_AUTO_EXPAND` explicitly acknowledges that macros will be expanded when creating the stack, without prior review. Users often create a change set from a processed template so that the changes made by macros can be reviewed before actually creating the stack. For more information, see the CloudFormation [CreateStack](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html) API.

   Then choose **Create**.

## Enable access to Neptune from Neptune-Export
<a name="export-service-access-to-neptune"></a>

After the Neptune-Export installation has completed, update your [Neptune VPC security group](get-started-vpc.md#security-vpc-security-group) to allow access from Neptune-Export. When the Neptune-Export CloudFormation stack has been created, the **Outputs** tab includes a `NeptuneExportSecurityGroup` ID. Update your Neptune VPC security group to allow access from this Neptune-Export security group.

## Enable access to the Neptune-Export endpoint from a VPC-based EC2 instance
<a name="export-service-access-to-service"></a>

If you make your Neptune-Export endpoint VPC-only, you can only access it from within the VPC in which the Neptune-Export service is installed. To allow connectivity from an Amazon EC2 instance in the VPC from which you can make Neptune-Export API calls, attach the `NeptuneExportSecurityGroup` created by the CloudFormation stack to that Amazon EC2 instance.
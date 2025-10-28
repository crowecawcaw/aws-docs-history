# Manage costs for EC2 Fast Launch underlying resources

There is no service charge to configure Windows AMIs for EC2 Fast Launch. However,
when you enable EC2 Fast Launch for an Amazon EC2 Windows AMI, standard pricing
applies for underlying AWS resources that Amazon EC2 uses to prepare and store the
pre-provisioned snapshots. You can configure cost allocation tags to help you
track and manage the costs that are associated with EC2 Fast Launch resources.
For more information about how to configure cost allocation tags, see
[Track EC2 Fast Launch costs on your bill](#win-track-fast-launch-costs "#win-track-fast-launch-costs").

The following example demonstrates how the costs associated with EC2 Fast Launch
snapshots costs might be allocated.

**Example scenario:** The AtoZ Example company has a Windows AMI
with a 50 GiB EBS root volume. They enable EC2 Fast Launch for their AMI, and set the
target resource count to five. Over the course of a month, using EC2 Fast Launch
for their AMI costs them around $5.00, and the cost breakdown is as follows:

1. When AtoZ Example enables EC2 Fast Launch, Amazon EC2 launches five small instances.
   Each instance runs through the Sysprep and OOBE Windows launch steps, rebooting as
   required. This takes several minutes for each instance (time can vary, based on how
   busy that Region or Availability Zone (AZ) is, and on the size of the AMI).

###### Costs

    * Instance runtime costs (or minimum runtime, if applicable): five
     instances
    * Volume costs: five EBS root volumes

2. When the pre-provisioning process completes, Amazon EC2 takes a snapshot of the instance, which
   it stores in Amazon S3. Snapshots are typically stored for 4–8 hours before they
   are consumed by a launch. In this case, the cost is roughly $0.02 to $0.05 per
   snapshot.

###### Costs

    * Snapshot storage (Amazon S3): five snapshots

3. After Amazon EC2 takes the snapshot, it stops the instance. At that point, the instance
   is no longer accruing costs. However EBS volume costs continue to accrue.

###### Costs

    * EBS volumes: costs continue for the associated EBS root volumes.

###### Note

The costs shown here are for demonstration purposes only. Your costs will vary,
depending on your AMI configuration and pricing plan.

## Track EC2 Fast Launch costs on your bill

Cost allocation tags can help you organize your AWS bill to reflect the costs
associated with EC2 Fast Launch. You can use the following tag that Amazon EC2
adds to the resources it creates when it prepares and stores pre-provisioned snapshots
for EC2 Fast Launch:

**Tag key:** `CreatedBy`, **Value:** `EC2 Fast Launch`

After you activate the tag in the Billing and Cost Management console, and set up your detailed billing
report, the `user:CreatedBy` column appears on the report. The column
includes values from all services. However, if you download the CSV file, you can
import the data into a spreadsheet, and filter for `EC2 Fast Launch` in
the value. This information also appears in the AWS Cost and Usage Report when the tag is activated.

###### Step 1: Activate user-defined cost allocation tags

To include resource tags in your cost reports, you must first activate the tag
in the Billing and Cost Management console. For more information, see
[Activating User-Defined Cost
Allocation Tags](../../../awsaccountbilling/latest/aboutv2/activating-tags.md "../../../awsaccountbilling/latest/aboutv2/activating-tags.md") in the _AWS Billing and Cost Management User Guide_.

###### Note

Activation can take up to 24 hours.

###### Step 2: Set up a cost report

If you already have a cost report set up, a column for your tag appears the next
time the report runs after activation is complete. To set up cost reports for the
first time, choose one of the following.

- See [Setting
  up a monthly cost allocation report](../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md#allocation-report "../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md#allocation-report") in the _AWS Billing and Cost Management User Guide_.
- See [Creating Cost
  and Usage Reports](../../../cur/latest/userguide/cur-create.md "../../../cur/latest/userguide/cur-create.md") in the _AWS Cost and Usage Report User Guide_.

###### Note

It can take up to 24 hours for AWS to start delivering reports to your S3 bucket.

You can configure EC2 Fast Launch for Windows AMIs that you own, or AMIs
that are shared with you from the Amazon EC2 console, API, SDKs, [CloudFormation](../../../AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.md"), or **ec2** commands in the AWS CLI. The
following sections cover configuration steps for the Amazon EC2 console and AWS CLI.

You can also create custom Windows AMIs that are configured for EC2 Fast Launch with
EC2 Image Builder. For more information, see [Create
distribution settings for a Windows AMI with EC2 Fast Launch enabled (AWS CLI)](../../../imagebuilder/latest/userguide/cr-upd-ami-distribution-settings.md#cli-create-ami-dist-config-win-fast-launch "../../../imagebuilder/latest/userguide/cr-upd-ami-distribution-settings.md#cli-create-ami-dist-config-win-fast-launch").

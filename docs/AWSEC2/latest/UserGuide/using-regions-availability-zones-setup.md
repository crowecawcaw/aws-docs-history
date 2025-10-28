# Select a Region for your Amazon EC2

resources

Amazon EC2 resources are specific to the AWS Region or zone in which they reside. When
you create an Amazon EC2 resource, you select the Region for the resource.

###### Considerations

- Some AWS resources might not be available in all Regions. Ensure that you
  can create all the AWS resources that you need in a Region before you start
  creating resources in a Region.
- Some Regions are disabled by default. You must enable these Regions before you
  can use them. For more information , see [AWS
  Regions](../../../global-infrastructure/latest/regions/aws-regions.md "../../../global-infrastructure/latest/regions/aws-regions.md").

###### To select a Region for a resource using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation bar, choose the **Regions** selector and
   then choose the Region.

![View your Regions](images/EC2_select_region.png) 3. The Regions selector includes all resources that are available for use in your
AWS account. Choose the underlined text near the bottom of the list to view
the Regions that are not enabled for your account.

###### To select a Region for a resource using the AWS CLI

You can configure the AWS CLI to use a default Region. If you don't specify a Region
in the command, the default Region is used. To use a different Region for a specific
command, add the following option.

```
--region `us-east-1`
```

###### To select a Region for a resource using the Tools for PowerShell

You can configure the Tools for Windows PowerShell to use a default Region. If you don't specify a Region
in a command, the default Region is used. To use a different Region for a specific
command, add the following parameter.

```
-Region `us-east-1`
```

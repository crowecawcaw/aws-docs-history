

# Scanning Windows EC2 instances with Amazon Inspector
<a name="windows-scanning"></a>

**Note**  
This page applies to customers that have not opted in to Enhanced EC2 Scanning.

 Amazon Inspector automatically discovers all supported Windows instances and includes them in continuous scanning without any extra actions. For information about which instances are supported, see [Operating systems and programming languages supported by Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/supported.html). Amazon Inspector runs Windows scans at regular intervals. Windows instances are scanned at discovery and then every 6 hours. However, you can [adjust the default scan interval](https://docs.aws.amazon.com/inspector/latest/user/windows-scanning.html#windows-scan-schedule) after the first scan. 

 When Amazon EC2 scanning is activated, Amazon Inspector creates the following SSM associations for your Windows resources: `InspectorDistributor-do-not-delete`, `InspectorInventoryCollection-do-not-delete`, and `InvokeInspectorSsmPlugin-do-not-delete`. To install the Amazon Inspector SSM plugin on your Windows instances, the `InspectorDistributor-do-not-delete` SSM association uses the [`AWS-ConfigureAWSPackage` SSM document](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html) and the [`AmazonInspector2-InspectorSsmPlugin` SSM Distributor package](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html). For more information, see [The Amazon Inspector SSM plugin for Windows](https://docs.aws.amazon.com/inspector/latest/user/deep-inspection.html#inspector/latest/user/deep-inspection.html). To collect instance data and generate Amazon Inspector findings, the `InvokeInspectorSsmPlugin-do-not-delete` SSM association runs the Amazon Inspector SSM plugin at 6-hour intervals. However, you can [customize this setting using a cron or rate expression](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html). 

**Note**  
 Amazon Inspector stages updated Open Vulnerability and Assessment Language (OVAL) definition files to the S3 bucket `inspector2-oval-prod-{{your-AWS-Region}}`. The Amazon S3 bucket contains OVAL definitions used in scans. These OVAL definitions shouldn't be modified. Otherwise, Amazon Inspector won't scan for new CVEs when they release. 

## Amazon Inspector scan requirements for Windows instances
<a name="windows-requirements"></a>

To scan a Windows instance, Amazon Inspector requires the instance to meet the following criteria:
+ The instance is an SSM managed instance. For instructions about setting up your instance for scanning, see [Configuring the SSM Agent](scanning-ec2.md#configure-ssm).
+ The instance operating system is one of the supported Windows operating systems. For a complete list of supported operating systems, see [Amazon EC2 instances status values](supported.md#supported-os-ec2).
+ The instance has the Amazon Inspector SSM plugin installed. Amazon Inspector automatically installs the Amazon Inspector SSM plugin for managed instances upon discovery. See the next topic for details about the plugin.

**Note**  
If your host is running in an Amazon VPC without outgoing internet access, Windows scanning requires your host to be able to access Regional Amazon S3 endpoints. To learn how to configure an Amazon S3 Amazon VPC endpoint, see [Create a gateway endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#create-gateway-endpoint-s3) in the *Amazon Virtual Private Cloud User Guide*. If your Amazon VPC endpoint policy is restricting access to external S3 buckets, you must specifically allow access to the bucket maintained by Amazon Inspector in your AWS Region that stores the OVAL definitions used to evaluate your instance. This bucket has the following the format: `inspector2-oval-prod-{{REGION}}`. 

## Setting custom schedules for Windows instance scans
<a name="windows-scan-schedule"></a>

You can customize the time between your Windows Amazon EC2 instance scans by setting a cron expression or rate expression for the `InvokeInspectorSsmPlugin-do-not-delete` association using SSM. For more information, see [Reference: Cron and rate expressions for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html) in the *AWS Systems Manager User Guide* or use the following instructions. 

Select from the following code examples to change the scan cadence for Windows instances from the default 6 hours to 12 hours using either a rate expression or a cron expression.

The following examples require you to use the **AssociationId** for the association named `InvokeInspectorSsmPlugin-do-not-delete`. You can retrieve your **AssociationId** by running the following AWS CLI command:

```
$ aws ssm list-associations --association-filter-list "key=AssociationName,value=InvokeInspectorSsmPlugin-do-not-delete" --region {{us-east-1}}
```

**Note**  
The **AssociationId** is Regional, so you need to first retrieve a unique ID for each AWS Region. You can then run the command to change the scan cadence in each Region where you want to set a custom scan schedule for Windows instances.

------
#### [ Example rate expression ]

```
$ aws ssm update-association \
--association-id "{{YourAssociationId}}" \
--association-name "InvokeInspectorSsmPlugin-do-not-delete" \
--schedule-expression "rate(12 hours)"
```

------
#### [ Example cron expression ]

```
$ aws ssm update-association \
--association-id "{{YourAssociationId}}" \
--association-name "InvokeInspectorSsmPlugin-do-not-delete" \
--schedule-expression "cron(0 0/12 * * ? *)"
```

------


# Deactivating a scan type in Amazon Inspector
<a name="deactivate-scans"></a>

When you deactivate a scan type, you lose access to any findings the scan type produced. If you [reactivate the scan type](https://docs.aws.amazon.com/inspector/latest/user/activate-scans.html), Amazon Inspector scans all eligible resources to generate new findings. If you want to keep a record of your findings, you can export them to an Amazon Simple Storage Service (Amazon S3) bucket as a findings report. For more information, see [Exporting Amazon Inspector findings reports](findings-managing-exporting-reports.md). When you deactivate a scan type, you might encounter the following changes in the AWS account where you deactivated the scan type: 

**[Amazon EC2 scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-ec2.html)**  
 When you deactivate Amazon Inspector Amazon EC2 scanning for an account, the following SSM associations are deleted: 
+ `InspectorDistributor-do-not-delete`
+ `InspectorInventoryCollection-do-not-delete`
+ `InspectorLinuxDistributor-do-not-delete`
+ `InvokeInspectorLinuxSsmPlugin-do-not-delete`
+ `InvokeInspectorSsmPlugin-do-not-delete`.

 Additionally, the Amazon Inspector SSM plugin is removed from all Windows hosts. For more information, see [Scanning Windows EC2 instance](windows-scanning.md). 

**[Amazon ECR scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html)**  
 When you deactivate Amazon ECR scanning for an account, the Amazon ECR scan type account changes from **Enhanced scanning** with Amazon Inspector to **Basic scanning** with Amazon ECR. 

**[Lambda standard scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html#lambda-standard-scans)**  
 When you deactivate Lambda standard scanning for an account, you deactivate Lambda code scanning if the scan type was actived. You also delete the CloudTrail service-linked channel that Amazon Inspector create when you activate Lambda standard scanning. 

**[Amazon Inspector Code Security](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html#lambda-standard-scans)**  
 When you deactivate Code Security for your account, you delete all integrations, projects, and scan configurations associated with it. If your account is the delegated administrator for an organization, you only deactivate Code Security for your account, and memeber accounts become standalone accounts. 

## Deactivating scans
<a name="deatctivate-scans-proc"></a>

Deactivating all scan types for an account deactivates Amazon Inspector for that account in that AWS Region. For more information, see [Deactivating Amazon Inspector](deactivating-best-practices.md).

To complete this procedure for a multi-account environment, follow these steps while signed in as the Amazon Inspector delegated administrator.

------
#### [ Console ]

**To deactivate scans**

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home).

1. By using the AWS Region selector in the upper-right corner of the page, select the Region where you want to deactivate scans.

1. In the navigation pane, choose **Account management**.

1. Choose the **Accounts** tab to show the scanning status of an account.

1. Select the check box of each account for which you want to deactivate scans.

1. Choose **Actions**, and, from the **Deactivate** options, select the scan type you wish to deactivate.

1. (Recommended) Repeat these steps in each AWS Region for which you want to deactivate that scan type.

------
#### [ API ]

Run the [Disable](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Disable.html) API operation. In the request, provide the account IDs you are deactivating scans for, and for `resourceTypes` provide one or more of `EC2`, `ECR`, `LAMBDA`, or `LAMBDA_CODE` to deactivate scans.

------
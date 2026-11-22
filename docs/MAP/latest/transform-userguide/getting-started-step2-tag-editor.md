

# AWS Tag Editor

You can use the AWS Resource Groups and Tag Editor to tag your migrated resources.





**Note**  
The AWS Tag Editor only works for resources running in the account.

**To get started**

1. Open the AWS Management Console.

1. Go to the **Resource Groups & Tag Editor, Tagging, Tag Editor** page.

1. Specify the Region(s) your resources are located. **Example**: us-east-1.

1. Choose the type of resources you want to bulk tag. **Example**: EC2, Lambda, and S3.

1. Choose **Search resources** to view the resources that meet the conditions you have selected.

1. Select all or a few of the listed resources you want to tag.

1. Choose **Manage tags** of selected resources.

1. Enter `aws-apn-id` in the Tag Key field.
**Note**  
The Migration Acceleration Program requires that you tag resources with the `aws-apn-id` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 

1. Enter and replace your **PRM ID** with the tag value you want to apply to the migrated workloads.

   **Example**: 
   + If your PRM ID is {{ra-abcdefg123456}}, use the value {{migra-abcdefg123456}}.

1. Choose **Review**.

1. Choose **Apply tag** changes.

Depending on your migrated resource and PRM ID, the tag value can be any of the following:
+ `mig{{PRM ID}}`
+ `sap{{PRM ID}}`
+ `oracle{{PRM ID}}`

**Note**  
Use lowercase letters for the `mig`, `sap`, and `oracle` prefixes. For more information about what tag values you should use, see [Tagging key combinations](setting-up.md). For more information about your PRM ID, see [PRM ID length](mpe-length.md).
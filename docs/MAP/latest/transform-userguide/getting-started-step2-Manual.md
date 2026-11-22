

# Manual tagging

You can manually tag your migrated resources using the AWS Management Console.



**To get started**

1. Go to your AWS Management Console. 

1. Go to the migrated resources. **Example**: Amazon RDS.

1. Choose **Add tags**.

1. Enter `aws-apn-id` as the Tag key.
**Note**  
The Migration Acceleration Program requires that you tag resources with the `aws-apn-id` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 

1. Enter and replace your **PRM ID** with the tag value you want to apply to the migrated workloads.

   **Example**: 
   + If your PRM ID is {{ra-abcdefg123456}}, use the value {{migra-abcdefg123456}}.

1. Choose **Save**.

Depending on your migrated resource and PRM ID, the tag value can be any of the following:
+ `mig{{PRM ID}}`
+ `sap{{PRM ID}}`
+ `oracle{{PRM ID}}`

**Note**  
Use lowercase letters for the `mig`, `sap`, and `oracle` prefixes. For more information about what tag values you should use, see [Tagging key combinations](setting-up.md). For more information about your PRM ID, see [PRM ID length](mpe-length.md).



Repeat the steps above for all associated resources such as Snapshots. For more information about tagging resources, see the [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon Elastic Compute Cloud user guide for Linux instances*.
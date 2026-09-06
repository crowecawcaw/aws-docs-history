

# Manual tagging
<a name="getting-started-step2-Manual"></a>

You can manually tag your migrated resources using the AWS Management Console.



**To get started**

1. Go to your AWS Management Console. 

1. Go to the migrated resources. **Example**: Amazon RDS.

1. Choose **Add tags**.

1. Enter `map-migrated` as the Tag key.
**Note**  
The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 

1. Enter and replace your **MPE ID** with the tag value you want to apply to the migrated workloads.

   **Example**: 
   + If your MPE ID is {{12345}}, use the value {{mig12345}}.
   + If your MPE ID is {{ABCDE12345}}, use the value {{migABCDE12345}}.

1. Choose **Save**.

Depending on your migrated resource and MPE ID, the tag value can be any of the following:

## Short MPE IDs
<a name="manual-short-ids"></a>
+ `mig{{5-digit MPE ID}}`
+ `sap{{5-digit MPE ID}}`
+ `oracle{{5-digit MPE ID}}`

## Long MPE IDs
<a name="manual-long-ids"></a>
+ `mig{{10 alphanumeric characters MPE ID}}`
+ `sap{{10 alphanumeric characters MPE ID}}`
+ `oracle{{10 alphanumeric characters MPE ID}}`

**Note**  
Use lowercase letters for the `mig`, `sap`, and `oracle` prefixes and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about what tag values you should use, see [Tagging key combinations](setting-up.md). For more information about your MPE ID, see [MPE ID length](mpe-length.md).



Repeat the steps above for all associated resources such as Snapshots. For more information about tagging resources, see the [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon Elastic Compute Cloud user guide for Linux instances*.
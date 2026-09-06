

# Tagging Resources
<a name="getting-started-step2"></a>

You can begin tagging your migrated resources in order for them to be included in your MAP 2.0 incentive calculations. Tagging your migrated workloads with the `map-migrated` tag gives you the following benefits:


+ You can track the migration inventory scope as it is migrated over time from your existing environment to AWS.
+ You can identify specific AWS resources used in place of existing pre-migration resources.
+ You can collect the cost and usage data of the migrated resources for you to report TCO and other financial data.



These tags are applied by the workload owners who are migrating their workloads and this process is repeated as workloads are moved across until the entire MAP migration scope has been migrated. While we encourage you to automate as much as possible, you have the ability to tag your migrated workloads using automated and manual tagging methods.



You can add a tag line to your templates if you are using an Infrastructure-As-Code tool such as AWS CloudFormation or Terraform to create your migrated resource on AWS. However, you can tag resources individually or bulk tag them using the AWS Tag Editor if you are creating resources directly from the AWS Management Console. For more information about tagging values, see [Tagging key combinations](setting-up.md).

**Note**  
The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 

**Topics**
+ [MAP tag](tag-key.md)
+ [Automated tagging](getting-started-step2-Automation.md)
+ [Manual tagging](getting-started-step2-Manual.md)
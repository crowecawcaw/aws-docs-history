

# Frequently Asked Questions (FAQs)
<a name="FAQs"></a>

Below you'll find answers to the most common questions you may have on MAP 2.0.

**Topics**
+ [How can I create Amazon Bedrock inference profiles to use supported foundation models?](#bedrock-inference-profiles)
+ [What are the supported foundation models in Amazon Bedrock?](#bedrock-supported-foundation-models)
+ [Why is tagging required for MAP 2.0?](#why-is-tagging-required)
+ [Should I activate the Cost Allocation Tag?](#account-activation)
+ [Should migrations occur under the management (payer) account?](#migration-account)
+ [Where do I find my MPE ID?](#mpe-number)
+ [How do I tag my migrated resources in AWS with `map-migrated` tag?](#map-tag)
+ [I’ve already onboarded to MAP 2.0 and have been following the tagging process that required CUR and a Server ID from Migration Hub. How should I proceed going forward?](#onboarding)
+ [What is the process for baseline AWS services that cannot be tagged but may also be included in MAP (which can include VMware Cloud on AWS, Amazon Connect or AWS Managed Services)?](#other-services)
+ [Will I receive MAP incentives if I tag an existing AWS resource?](#existing-resource)
+ [Can I use an Amazon S3 bucket that existed before the MAP agreement as destination for my migration?](#s3-buckets)
+ [What services are in scope for MAP 2.0?](#scope-services)
+ [Are tags case sensitive?](#tags)
+ [Can I use Amazon EC2 Dedicated Hosts as part of MAP 2.0?](#ec2-hosts)
+ [What should I do if I don't see the `map-migrated` tag in the Cost allocation tags screen?](#map-migrated-tag)

## How can I create Amazon Bedrock inference profiles to use supported foundation models?
<a name="bedrock-inference-profiles"></a>

See [Track, allocate, and manage your generative AI cost and usage with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/track-allocate-and-manage-your-generative-ai-cost-and-usage-with-amazon-bedrock/). You must tag the inference profile as described in [Tagging Resources](getting-started-step2.md).

## What are the supported foundation models in Amazon Bedrock?
<a name="bedrock-supported-foundation-models"></a>

For a list of supported foundation models that are eligible for MAP credits, see [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html). To gain access to these supported foundation models and purchase any provisioned throughput, you must use the Amazon Bedrock Console or API.

## Why is tagging required for MAP 2.0?
<a name="why-is-tagging-required"></a>

Tagging is a way to assign a label to an AWS resource. Tags enable you to categorize your AWS resources in different ways. For example, you can categorize by purpose, owner, department,or environment. Each tag consists of a key and an optional value (for example, Department: Finance), both of which you define. For the purposes of MAP, you must tag migrated workloads with the `map-migrated` tag to enable the following:


+  Tracking of the migration inventory scope, as it is migrated over time from your existing environment to AWS.
+ Identification of the specific AWS resources being used in place of existing pre-migration resources.

**Important**  
You must use the tag key `map-migrated` exactly as it appears here. You cannot introduce spaces, change the case of any of the letters, or alter the key in any way.

The tagging exercise is done when the workload is migrated to AWS. Typically, tags are applied by the workload owners who will be migrating their workloads. This process is repeated as workloads are moved across until the entire MAP migration scope has been migrated. Tagging your AWS resources is a best practice even outside of MAP. For more information, see the [Tagging Best Practices Whitepaper](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf).



**Note**  
The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 

## Should I activate the Cost Allocation Tag?
<a name="account-activation"></a>

The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost allocation tag in the management (payer) account that is mentioned in the MAP project plan. For the MAP 2.0 terms signed between November 01, 2022 and November 18, 2024, the cost-allocation tag setup is not automatically activated. See [Verify and Fix map-migrated cost-allocation tag](troubleshooting.md#getting-started-manual).



## Should migrations occur under the management (payer) account?
<a name="migration-account"></a>

Migrations must occur under the management (payer) account and any accounts linked to the management (payer) account. All migrated resources that are part of the migration plan must be tagged with `map-migrated` as defined in this guide.

**Important**  
You must use the tag key `map-migrated` exactly as it appears here. You cannot introduce spaces, change the case of any of the letters, or alter the key in any way.



**Note**  
The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 

## Where do I find my MPE ID?
<a name="mpe-number"></a>

Your project number found within your migration plan is also known as your MPE ID. For more information about your MPE ID, see [MPE ID length](mpe-length.md).



## How do I tag my migrated resources in AWS with `map-migrated` tag?
<a name="map-tag"></a>

While we encourage you to automate tagging your resources, you can tag your resources in AWS in the following ways:
+ If you are rehosting servers, use AWS Application Migration Service (MGN) for your migration.
+ MGN supported MAP auto-tagging.
+ You can go to each resource in AWS console and create tags.
+ You can write custom scripts to bulk tag your resources during or after the creation.

**Important**  
You must use the tag key `map-migrated` exactly as it appears here. You cannot introduce spaces, change the case of any of the letters, or alter the key in any way.

**Note**  
The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 



## I’ve already onboarded to MAP 2.0 and have been following the tagging process that required CUR and a Server ID from Migration Hub. How should I proceed going forward?
<a name="onboarding"></a>

For the previously existing MAP 2.0 projects, keep tagging as it was defined at the time the MAP 2.0 term was signed. For the MAP 2.0 terms signed after November 01, 2022, the related workloads should follow this tagging guide.



## What is the process for baseline AWS services that cannot be tagged but may also be included in MAP (which can include VMware Cloud on AWS, Amazon Connect or AWS Managed Services)?
<a name="other-services"></a>

The process is automated for Amazon Connect, VMware Cloud on AWS, and AWS Managed Services (AMS).



## Will I receive MAP incentives if I tag an existing AWS resource?
<a name="existing-resource"></a>

The Program Terms clearly state that only MAP resources that are launched after the agreement acceptance date are eligible for MAP incentives.



## Can I use an Amazon S3 bucket that existed before the MAP agreement as destination for my migration?
<a name="s3-buckets"></a>

You are recommended to use new S3 buckets for migration workloads. If, for any reason you have to use existing S3 buckets for migration workloads, you need to provide to your account team with the ARNs for each of the existing S3 buckets be used for migration and each bucket’s current baseline spend. This information is added to the MAP agreement. You will then need to tag these buckets during migration. For more information on how to baseline the existing S3 buckets, see the [How do I find the cost of my Amazon S3 buckets](https://aws.amazon.com/premiumsupport/knowledge-center/s3-find-bucket-cost/#:~:text=To%20see%20where%20requests%20to,contain%20Amazon%20S3%20request%20details) guide.



## What services are in scope for MAP 2.0?
<a name="scope-services"></a>

You can find all eligible services for MAP in the Included Services list: **https://s3-us-west-2.amazonaws.com/map-2.0-customer-documentation/included-services/MAP\_Included\_Services\_List.pdf**. Certain Specialized Services may also be included in your Migration Plan or MAP Migration Tracking and Incentive Guide. Eligible services for MAP for SAP are provided in the MAP for SAP Migration Tracking and Incentive Guide.



## Are tags case sensitive?
<a name="tags"></a>

Yes. See [MAP tag](tag-key.md).



## Can I use Amazon EC2 Dedicated Hosts as part of MAP 2.0?
<a name="ec2-hosts"></a>

Yes, it is possible for you to use Amazon EC2 Dedicated Hosts as part of MAP 2.0.



## What should I do if I don't see the `map-migrated` tag in the Cost allocation tags screen?
<a name="map-migrated-tag"></a>

The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost-allocation tag in the management (payer) account that is mentioned in the MAP project plan. For the MAP 2.0 terms signed between November 01, 2022 and November 18, 2024, the cost-allocation tag setup is not automatically activated. See [Verify and Fix map-migrated cost-allocation tag](troubleshooting.md#getting-started-manual).



**Note**  
The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 
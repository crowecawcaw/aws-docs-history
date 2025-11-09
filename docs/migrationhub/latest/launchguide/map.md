AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Migration Acceleration Program (MAP)

The [AWS Migration Acceleration Program (MAP)](https://aws.amazon.com/migration-acceleration-program/ "https://aws.amazon.com/migration-acceleration-program/") is a program to support customers as they
migrate to the cloud. MAP is based on AWS's experience migrating thousands of global customers
to the cloud.

Watch the **Introduction to MAP** video in any of the following
languages: [[English]](https://d2cwqplnsdeec3.cloudfront.net/EN-Video1-WelcomeMAP2.mp4 "https://d2cwqplnsdeec3.cloudfront.net/EN-Video1-WelcomeMAP2.mp4")
[[French]](https://d2cwqplnsdeec3.cloudfront.net/FR-Video1-WelcomeMAP2.mp4 "https://d2cwqplnsdeec3.cloudfront.net/FR-Video1-WelcomeMAP2.mp4")
[[Italian]](https://d2cwqplnsdeec3.cloudfront.net/IT-Video1-WelcomeMAP2.mp4 "https://d2cwqplnsdeec3.cloudfront.net/IT-Video1-WelcomeMAP2.mp4")
[[Spanish]](https://d2cwqplnsdeec3.cloudfront.net/ES-Video1-WelcomeMAP2.mp4 "https://d2cwqplnsdeec3.cloudfront.net/ES-Video1-WelcomeMAP2.mp4")

###### Getting started

If you are getting started with AWS Migration Acceleration Program 2.0, the following
are the required steps to start generating MAP credits:

1. **MAP tagging setup:** Activate the tag key that is
   required for MAP 2.0 in **AWS Billing > Cost Allocation
   Tags**. For more information, see [AWS account setup](https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/html/AWSMapDocs/getting-started-step1.html "https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/html/AWSMapDocs/getting-started-step1.html") in the AWS Migration Acceleration
   Program 2.0 Tagging Guide and [Using AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the AWS Billing User
   Guide.
2. **Tag selection:** Choose the appropriate MAP 2.0 tag
   key/value combination. For more information, see [Tagging key combinations](https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/html/AWSMapDocs/setting-up.html "https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/html/AWSMapDocs/setting-up.html") in the AWS Migration Acceleration
   Program 2.0 Tagging Guide.
3. **Tagging migrated workloads:** See the [list of MAP 2.0 eligible services](https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/included-services/MAP_Included_Services_List.pdf "https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/included-services/MAP_Included_Services_List.pdf") and [MAP tagging best practices](#map-tagging-best-practices "#map-tagging-best-practices").

## What is tagging for MAP?

A tag is a key-value pair that you apply to an AWS resource to hold metadata about that
resource. Tagging makes it possible for organizations to categorize and manage their cloud
infrastructure easily at scale. You can also use tagging to create new resource constructs for
visibility or control. For example, you can use tagging to group together resources that make
up a workload. To obtain the full benefits of MAP, you must tag the migrated workloads. For
more information, see [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") and [Guidance
for Tagging on AWS](https://aws.amazon.com/solutions/guidance/tagging-on-aws/ "https://aws.amazon.com/solutions/guidance/tagging-on-aws/").

If you are a new MAP customer, see [AWS Migration Acceleration Program 2.0 Tagging Guide](https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/html/AWSMapDocs/what-is-service.html "https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/html/AWSMapDocs/what-is-service.html"). For a
list of MAP-credit-eligible services, see [What services are in scope for MAP 2.0?](https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/html/AWSMapDocs/FAQs.html#scope-services "https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/html/AWSMapDocs/FAQs.html#scope-services") in the AWS Migration
Acceleration Program 2.0 Tagging Guide.

Watch the **Tagging for MAP** video in any of the following
languages: [[English]](https://d2cwqplnsdeec3.cloudfront.net/EN-Video2-CostAllocationTagsMAP2.mp4 "https://d2cwqplnsdeec3.cloudfront.net/EN-Video2-CostAllocationTagsMAP2.mp4") [[French]](https://d2cwqplnsdeec3.cloudfront.net/FR-Video2-CostAllocationTagsMAP2.mp4 "https://d2cwqplnsdeec3.cloudfront.net/FR-Video2-CostAllocationTagsMAP2.mp4")
[[Italian]](https://d2cwqplnsdeec3.cloudfront.net/IT-Video2-CostAllocationTagsMAP2.mp4 "https://d2cwqplnsdeec3.cloudfront.net/IT-Video2-CostAllocationTagsMAP2.mp4")
[[Spanish]](https://d2cwqplnsdeec3.cloudfront.net/ES-Video2-CostAllocationTagsMAP2.mp4 "https://d2cwqplnsdeec3.cloudfront.net/ES-Video2-CostAllocationTagsMAP2.mp4")

## General best practices for tagging resources

on AWS

AWS Documentation: [Tagging AWS Resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") .

Blog Post: [Maximizing resource tagging at scale and across teams for your migration
to AWS](https://aws.amazon.com/blogs/mt/maximizing-resource-tagging-at-scale-and-across-teams-for-your-migration-to-aws/ "https://aws.amazon.com/blogs/mt/maximizing-resource-tagging-at-scale-and-across-teams-for-your-migration-to-aws/").

The following training video explains how to tag resources in AWS.

Vea el vídeo [Etiquetado de
recursos en AWS para mejorar operaciones en la nube](https://youtu.be/cVGf81f9-n8 "https://youtu.be/cVGf81f9-n8") en español.

## MAP tagging best practices

- **Tagging with AWS CloudFormation:**
  - You can use CloudFormation Linter to enforce tags. You can create rules to enforce
    certain tag keys, and include linting steps in pipelines. For more information, see
    [AWS CloudFormation Linter](https://github.com/aws-cloudformation/cfn-lint "https://github.com/aws-cloudformation/cfn-lint") on GitHub.
  - When you create or update an AWS CFN stack, set tags in the AWS Management
    Console or by using the AWS CLI. AWS CloudFormation propagates these tags to all the AWS resources
    that you create in the stack. For more information, see [create-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack.html") and [update-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack.html") in the AWS CLI command reference.

- **Tagging with AWS Config:**
  - To identify and tag MAP 2.0 eligible resources that were created after the MAP
    agreement was signed, use the [AWS Config Conformance Pack](https://github.com/aws-samples/map20-tag-conformance-pack "https://github.com/aws-samples/map20-tag-conformance-pack") . For more information, see [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/").

- **Tagging with AWS Application Migration Service (Application Migration Service):**
  - With Application Migration Service, you can enable MAP tagging to automatically tag your launched
    instances. To enable MAP tagging, go to the Application Migration Service console and choose **Add
    MAP tag to Launched Instances**, then specify the MAP tag value that you
    want to use. Application Migration Service will automatically tag your launched instances with the key
    `map-migrated` and the value required for the MAP program. Application Migration Service only
    tags Amazon EC2 instances and Amazon EBS volumes. For more information, see the Application Migration Service [MAP program tagging](../../../mgn/latest/ug/map-program-tagging.md "../../../mgn/latest/ug/map-program-tagging.md") topic and the MAP tagging guide
    provided by your MAP team.

- **AWS remediation options:**
  - Use AWS Config to create rules that check resources for required tags and to
    continuously monitor your resources against those rules. Use it with [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") to trigger automated responses to missing tag values. For example, you can
    set it to send an email through Amazon SNS. For more information, see [Using Amazon EventBridge Scheduler with Amazon SNS](../../../sns/latest/dg/using-eventbridge-scheduler.md "../../../sns/latest/dg/using-eventbridge-scheduler.md") in
    the Amazon SNS Developer Guide.

- **Additional resources:**
  - [Service control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md")
  - [Enforcing tagging on resource creation](../../../organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.md")
  - [Tag Policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md")
  - [Restricting allowed tag key/values](https://aws.amazon.com/blogs/aws/new-use-tag-policies-to-manage-tags-across-multiple-aws-accounts/ "https://aws.amazon.com/blogs/aws/new-use-tag-policies-to-manage-tags-across-multiple-aws-accounts/")

## MAP 2.0 customer-facing dashboard

The **MAP 2.0 Dashboard** is a self-serve mechanism for
eligible MAP 2.0 customers to track the progress of their MAP migrations. This dashboard is
available in the billing console for payer accounts that are part of MAP 2.0 agreements signed
after November 2022. This dashboard is only available for customers that have received their
first tranche of credits. For more information, and to learn how to access the dashboard, see
the [MAP 2.0 Dashboard User Guide](https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/forms/MAP_Dashboard_Guide.pdf "https://s3.us-west-2.amazonaws.com/map-2.0-customer-documentation/forms/MAP_Dashboard_Guide.pdf").

## Monitor untagged services eligible for MAP credits

After you tag the target AWS resources, check to see how much these resources are used
for each management account in your migration. You can use Cost Explorer to see the
approximate amount of the target AWS resources. You can also use it to create a report on
AWS services that are eligible for MAP credits but have not been tagged. To do so, select
the filters below.

| **Report parameters** | **Filter**               | **Setting**                                                                                                                                                            |
| --------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Time                  | Date range               | Specify a date range                                                                                                                                                   |
| Time                  | Granularity              | Specify a granularity                                                                                                                                                  |
| Group by              | Dimension                | Select Service, Linked account or Tag, as appropriate                                                                                                                  |
| Filters               | Service                  | Exclude non-MAP-2.0-eligible services                                                                                                                                  |
| Filters               | Usage type               | Exclude all "DataTransfer" values                                                                                                                                      |
| Filters               | Usage type group         | Exclude all "Data Transfer" values                                                                                                                                     |
| Filters               | Tag                      | Choose to view either tagged spend or untagged spend. You can also leave it<br>blank and then use the 'Dimension' to show the split of tagged versus untagged<br>spend |
| Advanced options      | Aggregate costs by       | Amortized costs                                                                                                                                                        |
| Advanced options      | Additional data settings | Untick all                                                                                                                                                             |

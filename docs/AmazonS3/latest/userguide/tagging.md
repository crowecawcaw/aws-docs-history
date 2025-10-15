# Tagging for cost allocation or attribute-based access control (ABAC)

An AWS tag is a key-value pair that holds metadata. You attach the tags to your Amazon S3 resources, such as buckets. You can tag resources when you create them or manage tags on existing resources. There is no additional charge for using tags beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").


## How tags work


Amazon S3 support two types of tags:



* **AWS-generated tags:** 
 AWS automatically applies these tags, and you cannot modify them or remove them. To learn more about AWS-generated tags, see [Using AWS-generated tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html").
* **User-defined tags:** 
 You apply these tags to your S3 resources and manage them.

### User-defined tags


A user-defined tag is a tag key-value pair that you use to label your resources. User-defined tags consist of a required key and an optional value. These are the main components of a user-defined tag:


#### The tag key


The tag key is the required name of the tag. For example, `project` is the tag key in the following tag key-value pair:




| Key | Value |
| --- | --- |
| `project` | `Trinity` |


The tag key is a case-sensitive string that must contain between 1 and 128 Unicode characters. Keys can only contain Unicode letters or numbers, white space, and the following symbols:



* `_` - underscore
* `.` - period
* `:` - colon
* `/` - forward slash
* `=` - equal sign
* `+` - plus sign
* `@` - at sign
* `-` - dash

#### The tag value


The tag value is an optional string. For example, `Trinity` is the tag value in this tag key-value pair:




| Key | Value |
| --- | --- |
| `project` | `Trinity` |


The tag value is a case-sensitive string that can contain between 0 and 256 Unicode characters. Values can only contain Unicode letters or numbers, white space, and the following symbols:



* `_` - underscore
* `.` - period
* `:` - colon
* `/` - forward slash
* `=` - equal sign
* `+` - plus sign
* `@` - at sign
* `-` - dash

For details on the characters allowed in user-defined tags and other restrictions, see [User-Defined Tag Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html#allocation-tag-restrictions "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html#allocation-tag-restrictions") in the *AWS Billing and Cost Management User Guide*.


#### The tag set


Each S3 resource has one *tag set* that contains all of the tag key and value pairs that are assigned to that bucket. A tag set can be empty, or it can contain as many as 50 user-defined tags, except in the case of tagging objects. Objects can have up to 10 tags only.


While each key must be unique in a tag set, you can use the same value multiple times. For example, you can have the same value, `Trinity`, for following two tag keys:




| Key | Value |
| --- | --- |
| `project` | `Trinity` |
| `cost-center` | `Trinity` |


When you add a tag that has the same key as an existing tag, the new value overwrites the old value.


AWS doesn't apply any semantic meaning to your tags. We interpret tags strictly as character strings.


To add, list, modify, or delete tags, you can use the Amazon S3 console, the AWS Command Line Interface (AWS CLI), or the Amazon S3 API. 


## Common ways to use tags


Use tags on your S3 resources for:



1. **Cost allocation** – Track storage costs by bucket tag in AWS Billing and Cost Management.
2. **Attribute-based access control (ABAC)** – Scale access permissions and grant access to S3 resources based on their tags.

###### Note

You can use the same tags for both cost allocation and access control.


### Using tags for cost allocation


Track your Amazon S3 storage costs by applying tags to S3 resources and activating these tags for cost allocation.


To start tracking costs:



1. Add tags to your S3 resources or use existing tags. For example, you can label buckets with a tag that identifies a project or a group of projects.
2. Activate the tags for cost allocation in the AWS Billing and Cost Management console. See [Activating user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html") in the *AWS Billing and Cost Management User Guide*. You can activate user-defined or AWS-generated tags. For more information, see [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html").

AWS uses the activated tags to organize your resource costs in various billing and cost management tools, such as: 



* **Cost allocation report**

Provides a high-level view of costs organized by your activated tags. For more information, see [Using the monthly cost allocation report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html") in the *AWS Billing
User Guide*.
* **Cost and Usage Report (CUR)**


Provides the most detailed set of AWS cost and usage data, including tag-based cost breakdowns. For more information, see [What are AWS Cost and Usage Reports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html "https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html") in the *AWS Data Export User Guide*.

###### Amazon S3 resources that support tracking costs with tags


The following Amazon S3 resources support storage cost tracking using tags. 



* **Directory buckets**


For more information, see [Managing tags for directory buckets](directory-buckets-tagging.md#working-with-tags "directory-buckets-tagging.md#working-with-tags").
* **General purpose buckets**


For more information, see [Managing tags for general purpose buckets](CostAllocTagging.md#working-with-tags-gpb "CostAllocTagging.md#working-with-tags-gpb").

### Using tags for attribute-based access control (ABAC)


Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes, i.e., tags. You can attach tags to AWS Identity and Access Management (IAM) entities (users or roles) and to AWS resources, such as Amazon S3 Access Points and directory buckets. Then, you control permissions to these resources using tag-based conditions in access control policies to allow or deny operations when these conditions are met. 


With ABAC, you use tag-based condition keys in your AWS organizations, IAM, and S3 resource policies. For enterprises, ABAC in Amazon S3 supports authorization across multiple AWS accounts. 


In your IAM policies, you can control access to S3 resources based on the bucket's tags by using [condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys").


###### Supported condition keys


You can use the following AWS condition keys for all Amazon S3 resources that support ABAC. 



* `aws:ResourceTag/key-name`
* `aws:RequestTag/key-name`
* `aws:TagKeys`

Some resources support additional Amazon S3 condition keys. For a complete list of condition keys that can be used for ABAC and example policies, see the following tagging topics for the resource. 


###### Amazon S3 resources that support ABAC


The following Amazon S3 resources support attribute-based access control (ABAC) using tags. 



* **Access points**


For more information, see [Using tags with S3 Access Points for general purpose buckets](access-points-tagging.md "access-points-tagging.md") and [Using tags with S3 Access Points for directory buckets](access-points-db-tagging.md "access-points-db-tagging.md").
* **Batch operation jobs**


For more information, see [Controlling access and labeling jobs using tags](batch-ops-job-tags.md "batch-ops-job-tags.md").
* **Directory buckets**


For more information, see [Using tags with S3 directory buckets](directory-buckets-tagging.md "directory-buckets-tagging.md").
* **Objects**


For more information, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md").
* **S3 Access Grants**


For more information, see [Managing tags for S3 Access Grants](access-grants-tagging.md "access-grants-tagging.md").
* **S3 Storage Lens Groups**


For more information, see [Managing AWS resource tags with Storage
 Lens groups](storage-lens-groups-manage-tags.md "storage-lens-groups-manage-tags.md").

## Planning your tagging strategy


We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add. For more information about how to implement an effective resource tagging strategy, see the [Tagging Best Practices AWS Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html "https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html").


###### Best practices for tagging Amazon S3 resources


When you use tags, we recommend that you adhere to the following best practices:




* Document conventions for tag use that are followed by all teams in your organization. In particular, ensure the names are both descriptive and consistent. For example, standardize on the format `environment:prod` rather than tagging some resources with `env:production`.


###### Important

Do not store personally identifiable information (PII) or other confidential or sensitive information in tags.
* Automate tagging to ensure consistency. For example, you can include tags in an AWS CloudFormation template. When you create resources with the template, the resources are tagged automatically.
* Use tags only when necessary. Avoid unnecessary tag proliferation and complexity.
* Review tags periodically for relevance and accuracy. Remove or modify outdated tags as needed.
* Consider creating tags with the AWS Tag Editor in the AWS Management Console. You can use the Tag Editor to add tags to multiple supported AWS resources, including Amazon S3 resources, at the same time. For more information, see [Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/tag-editor.html "https://docs.aws.amazon.com/ARG/latest/userguide/tag-editor.html") in the *AWS Resource Groups User Guide*.

## Managing tags for Amazon S3 resources


For more information on how to manage tags for Amazon S3 resources, see the following:



* [Managing tags for Access Points for general purpose buckets](access-points-tagging.md#working-with-tags-access-points "access-points-tagging.md#working-with-tags-access-points")
* [Managing tags for Access Points for directory buckets](access-points-db-tagging.md#working-with-tags-access-points-db "access-points-db-tagging.md#working-with-tags-access-points-db")
* [Controlling access and labeling jobs using tags](batch-ops-job-tags.md "batch-ops-job-tags.md")
* [Managing tags for directory buckets](directory-buckets-tagging.md#working-with-tags "directory-buckets-tagging.md#working-with-tags")
* [Managing tags for general purpose buckets](CostAllocTagging.md#working-with-tags-gpb "CostAllocTagging.md#working-with-tags-gpb")
* [Categorizing your objects using tags](object-tagging.md "object-tagging.md")
* [Managing tags for S3 Access Grants](access-grants-tagging.md "access-grants-tagging.md")
* [Managing AWS resource tags with Storage
 Lens groups](storage-lens-groups-manage-tags.md "storage-lens-groups-manage-tags.md")

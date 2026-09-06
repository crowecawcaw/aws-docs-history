

# Tagging Amazon Aurora andAmazon RDS resources
<a name="USER_Tagging"></a><a name="tagging"></a>

An Amazon RDS tag is a name-value pair that you define and associate with an Amazon RDS resource such as a DB instance or DB snapshot. The name is referred to as the key. Optionally, you can supply a value for the key.

You can use the AWS Management Console, the AWS CLI, or the Amazon RDS API to add, list, and delete tags on Amazon RDS resources. When using the CLI or API, make sure to provide the Amazon Resource Name (ARN) for the RDS resource to work with. For more information about constructing an ARN, see [Constructing an ARN for Amazon RDS](USER_Tagging.ARN.Constructing.md).

You can use tags to add metadata to your Aurora and Amazon RDS resources. You can use the tags to add your own notations about database instances, snapshots, Aurora clusters, and so on. Doing so can help you to document your Aurora and Amazon RDS resources. You can also use the tags with automated maintenance procedures. 

 In particular, you can use these tags with IAM policies. You can use them to manage access to Aurora and Amazon RDS resources and to control what actions can be applied to those resources. You can also use these tags to track costs by grouping expenses for similarly tagged resources. 

You can tag the following Aurora and Amazon RDS resources:
+ DB instances
+ DB clusters
+ Aurora global clusters
+ DB cluster endpoints
+ Read replicas
+ DB snapshots
+ DB cluster snapshots
+ Reserved DB instances
+ Event subscriptions
+ DB option groups
+ DB parameter groups
+ DB cluster parameter groups
+ DB subnet groups
+ RDS Proxies
+ RDS Proxy endpoints
+ Blue/green deployments
+ Zero-ETL integrations
+ Automated backups
+ Cluster automated backups

**Note**  
When you tag a DB instance, Aurora automatically applies those tags to the associated Performance Insights resources. Currently, you can't tag RDS Proxies and RDS Proxy endpoints by using the AWS Management Console.

**Topics**
+ [Why use Amazon RDS resource tags?](#Tagging.Purpose)
+ [How Amazon RDS resource tags work](#Overview.Tagging)
+ [Best practices for tagging Amazon RDS resources](#Tagging.best-practices)
+ [Copying tags to DB cluster snapshots](#USER_Tagging.CopyTagsCluster)
+ [Tagging automated backup resources](#USER_Tagging.AutomatedBackups)
+ [Adding and deleting tags in Amazon RDS](#Tagging.HowTo)
+ [Tutorial: Use tags to specify which Aurora DB clusters to stop](Tagging.Aurora.Autostop.md)

## Why use Amazon RDS resource tags?
<a name="Tagging.Purpose"></a>

You can use tags to do the following:
+ Categorize your RDS resources by application, project, department, environment, and so on. For example, you could use a tag key to define a category, where the tag value is an item in this category. You might create the tag `environment=prod`. Or you might define a tag key of `project` and a tag value of `Salix`, which indicates that an Amazon RDS resource is assigned to the Salix project.
+ Automate resource management tasks. For example, you could create a maintenance window for instances tagged `environment=prod` that differs from the window for instances tagged `environment=test`. You could also configure automatic DB snapshots for instances tagged `environment=prod`.
+ Control access to RDS resources within an IAM policy. You can do this by using the global `aws:ResourceTag/{{tag-key}}` condition key. For example, a policy might allow only users in the `DBAdmin` group to modify DB instances tagged with `environment=prod`. For information about managing access to tagged resources with IAM policies, see [Identity and access management for Amazon Aurora](UsingWithRDS.IAM.md) and [Controlling access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html#access_tags_control-resources) in the *AWS Identity and Access Management User Guide*. 
+ Monitor resources based on a tag. For example, you can create an Amazon CloudWatch dashboard for DB instances tagged with `environment=prod`.
+ Track costs by grouping expenses for similarly tagged resources. For example, if you tag RDS resources associated with the Salix project with `project=Salix`, you can generate cost reports for and allocate expenses to this project. For more information, see [How AWS billing works with tags in Amazon RDS](#Tagging.Billing).

## How Amazon RDS resource tags work
<a name="Overview.Tagging"></a>

AWS doesn't apply any semantic meaning to your tags. Tags are interpreted strictly as character strings. 

**Topics**
+ [Tag sets in Amazon RDS](#Overview.Tagging.Sets)
+ [Tag structure in Amazon RDS](#Overview.Tagging.Structure)
+ [Amazon RDS resources eligible for tagging](#Overview.Tagging.Resources)
+ [How AWS billing works with tags in Amazon RDS](#Tagging.Billing)

### Tag sets in Amazon RDS
<a name="Overview.Tagging.Sets"></a>

Every Amazon RDS resource has a container called a tag set. The container includes all the tags that are assigned to the resource. A resource has exactly one tag set. 

A tag set contains 0—50 tags. If you add a tag to an RDS resource with the same key as an existing resource tag, the new value overwrites the old.

### Tag structure in Amazon RDS
<a name="Overview.Tagging.Structure"></a>

The structure of an RDS tag is as follows:

**Tag key**  
The key is the required name of the tag. The string value must be 1—128 Unicode characters in length and cannot be prefixed with `aws:` or `rds:`. The string can contain only the set of Unicode letters, digits, whitespace, `_`, `.`, `:`, `/`, `=`, `+`, `-`, and `@`. The Java regex is `"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"`. Tag keys are case-sensitive. Thus, the keys `project` and `Project` are distinct.  
A key is unique to a tag set. For example, you cannot have a key-pair in a tag set with the key the same but with different values, such as `project=Trinity` and `project=Xanadu`.

**Tag value**  
The value is an optional string value of the tag. The string value must be 1—256 Unicode characters in length. The string can contain only the set of Unicode letters, digits, whitespace, `_`, `.`, `:`, `/`, `=`, `+`, `-`, and `@`. The Java regex is `"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"`. Tag values are case-sensitive. Thus, the values `prod` and `Prod` are distinct.  
Values don't need to be unique in a tag set and can be null. For example, you can have a key-value pair in a tag set of `project=Trinity` and `cost-center=Trinity`. 

### Amazon RDS resources eligible for tagging
<a name="Overview.Tagging.Resources"></a>

You can tag the following Amazon RDS resources:
+ DB instances
+ DB clusters
+ DB cluster endpoints
+ Read replicas
+ DB snapshots
+ DB cluster snapshots
+ Reserved DB instances
+ Event subscriptions
+ DB option groups
+ DB parameter groups
+ DB cluster parameter groups
+ DB subnet groups
+ RDS Proxies
+ RDS Proxy endpoints
**Note**  
Currently, you can't tag RDS Proxies and RDS Proxy endpoints by using the AWS Management Console.
+ Blue/green deployments
+ Zero-ETL integrations (preview)
+ Automated backups
+ Cluster automated backups

### How AWS billing works with tags in Amazon RDS
<a name="Tagging.Billing"></a>

Use tags to organize your AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill with tag key values included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.

#### How cost allocation tags work with DB clustersnapshots
<a name="Tagging.Billing.Snapshots"></a>

You can add a tag to a DB cluster snapshot. However, your bill won't reflect this grouping. For cost allocation tags to apply to DB cluster snapshots, the following conditions must be met:
+ The tags must be attached to the parent DB instance.
+ The parent DB instance must exist in the same AWS account as the DB cluster snapshot.
+ The parent DB instance must exist in the same AWS Region as the DB cluster snapshot.

DB cluster snapshots are considered orphaned if they don't exist in the same Region as the parent DB instance, or if the parent DB instance is deleted. Orphaned DB snapshots don't support cost allocation tags. Costs for orphaned snapshots are aggregated in a single untagged line item. Cross-account DB cluster snapshots aren't considered orphaned when the following conditions are met:
+ They exist in the same Region as the parent DB instance.
+ The parent DB instance is owned by the source account.
**Note**  
If the parent DB instance is owned by a different account, cost allocation tags don't apply to cross-account snapshots in the destination account.

## Best practices for tagging Amazon RDS resources
<a name="Tagging.best-practices"></a>

When you use tags, we recommend that you adhere to the following best practices:
+ Document conventions for tag use that are followed by all teams in your organization. In particular, ensure the names are both descriptive and consistent. For example, standardize on the format `environment:prod` rather than tagging some resources with `env:production`.
**Important**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags.
+ Automate tagging to ensure consistency. For example, you can use the following techniques:
  + Include tags in an CloudFormation template. When you create resources with the template, the resources are tagged automatically.
  + Define and apply tags using AWS Lambda functions.
  + Create an SSM document that includes steps to add tags to your RDS resources.
+ Use tags only when necessary. You can add up to 50 tags for a single RDS resource, but a best practice is to avoid unnecessary tag proliferation and complexity.
+ Review tags periodically for relevance and accuracy. Remove or modify outdated tags as needed.
+ Consider creating tags with the AWS Tag Editor in the AWS Management Console. You can use the Tag Editor to add tags to multiple supported AWS resources, including RDS resources, at the same time. For more information, see [Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/tag-editor.html) in the *AWS Resource Groups User Guide*.

## Copying tags to DB cluster snapshots
<a name="USER_Tagging.CopyTagsCluster"></a>

When you create or restore a DB cluster, you can specify that the tags from the cluster are copied to snapshots of the DB cluster. Copying tags ensures that the metadata for the DB snapshots matches that of the source DB cluster. It also ensures any access policies for the DB snapshot also match those of the source DB cluster. Tags are not copied by default. 

You can specify that tags are copied to DB snapshots for the following actions: 
+ Creating a DB cluster
+ Restoring a DB cluster
+ Creating a read replica
+ Copying a DB cluster snapshot

**Note**  
In some cases, you might include a value for the `--tags` parameter of the [create-db-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-snapshot.html) AWS CLI command. Or you might supply at least one tag to the [CreateDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBSnapshot.html) API operation. In these cases, RDS doesn't copy tags from the source DB instance to the new DB snapshot. This functionality applies even if the source DB instance has the `--copy-tags-to-snapshot` (`CopyTagsToSnapshot`) option turned on.   
If you take this approach, you can create a copy of a DB instance from a DB snapshot. This approach avoids adding tags that don't apply to the new DB instance. You create your DB snapshot using the AWS CLI `create-db-snapshot` command (or the `CreateDBSnapshot` RDS API operation). After you create your DB snapshot, you can add tags as described later in this topic.

## Tagging automated backup resources
<a name="USER_Tagging.AutomatedBackups"></a>

Automated backup resources are created when you set backup retention period value from 0 to greater than 0. You can tag instance or cluster automated backup resources during creation using the `--tag-specifications` parameter.

### Tag-Specifications Parameter
<a name="USER_Tagging.AutomatedBackups.TagSpecifications"></a>

APIs that support the `--tag-specifications` request parameter (like [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html), [restore-db-instance-from-db-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-db-snapshot.html), [create-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster.html), etc.) can tag automated backups (Resource Type: `auto-backup` or `cluster-auto-backup`) during creation.

#### Tagging cluster automated backups
<a name="USER_Tagging.AutomatedBackups.TagSpecifications.Cluster"></a>

Use `--tag-specifications` with `ResourceType=cluster-auto-backup` when creating DB clusters that have automated backups enabled.

**Note**  
Automated backup tags are independent of source DB instance tags, DB cluster tags, or DB snapshot tags.

## Adding and deleting tags in Amazon RDS
<a name="Tagging.HowTo"></a>

You can do the following:
+ Create tags when you create a resource, for example, when you run the AWS CLI command `create-db-instance`.
+ Add tags to an existing resource using the command `add-tags-to-resource`.
+ List tags associated with a specific resource using the command `list-tags-for-resource`.
+ Update tags using the command `add-tags-to-resource`.
+ Remove tags from a resource using the command `remove-tags-from-resource`.

The following procedures show how you can perform typical tagging operations on resources related to DB instances and Aurora DB clusters. Note that tags are cached for authorization purposes. For this reason, when you add or update tags on Amazon RDS resources, several minutes can pass before the modifications are available. 

### Console
<a name="USER_Tagging.CON"></a>

The process to tag an Amazon RDS resource is similar for all resources. The following procedure shows how to tag an Amazon RDS DB instance. 

**To add a tag to a DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.
**Note**  
To filter the list of DB instances in the **Databases** pane, enter a text string for **Filter databases**. Only DB instances that contain the string appear.

1. Choose the name of the DB instance that you want to tag to show its details. 

1. In the details section, scroll down to the **Tags** section. 

1. Choose **Add**. The **Add tags** window appears.   
![Add tags window.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/RDSConsoleTagging5.png)

1. Enter a value for **Tag key** and **Value**.

1. To add another tag, you can choose **Add another Tag** and enter a value for its **Tag key** and **Value**. 

   Repeat this step as many times as necessary.

1. Choose **Add**. 

**To delete a tag from a DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.
**Note**  
To filter the list of DB instances in the **Databases** pane, enter a text string in the **Filter databases** box. Only DB instances that contain the string appear.

1. Choose the name of the DB instance to show its details. 

1. In the details section, scroll down to the **Tags** section. 

1. Choose the tag you want to delete.  
![Tags section.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/RDSConsoleTagging6.png)

1. Choose **Delete**, and then choose **Delete** in the **Delete tags** window. 

### AWS CLI
<a name="USER_Tagging.CLI"></a>

You can add, list, or remove tags for a DB instance using the AWS CLI.
+ To add one or more tags to an Amazon RDS resource, use the AWS CLI command [`add-tags-to-resource`](https://docs.aws.amazon.com/cli/latest/reference/rds/add-tags-to-resource.html).
+ To list the tags on an Amazon RDS resource, use the AWS CLI command [`list-tags-for-resource`](https://docs.aws.amazon.com/cli/latest/reference/rds/list-tags-for-resource.html).
+ To remove one or more tags from an Amazon RDS resource, use the AWS CLI command [`remove-tags-from-resource`](https://docs.aws.amazon.com/cli/latest/reference/rds/remove-tags-from-resource.html).

To learn more about how to construct the required ARN, see [Constructing an ARN for Amazon RDS](USER_Tagging.ARN.Constructing.md).

### RDS API
<a name="USER_Tagging.API"></a>

You can add, list, or remove tags for a DB instance using the Amazon RDS API.
+ To add a tag to an Amazon RDS resource, use the [`AddTagsToResource`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddTagsToResource.html) operation.
+ To list tags that are assigned to an Amazon RDS resource, use the [`ListTagsForResource`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ListTagsForResource.html).
+ To remove tags from an Amazon RDS resource, use the [`RemoveTagsFromResource`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RemoveTagsFromResource.html) operation.

To learn more about how to construct the required ARN, see [Constructing an ARN for Amazon RDS](USER_Tagging.ARN.Constructing.md).

When working with XML using the Amazon RDS API, tags use the following schema:

```
 1. <Tagging>
 2.       <TagSet>
 3.           <Tag>
 4.               <Key>Project</Key>
 5.               <Value>Trinity</Value>
 6.           </Tag>
 7.           <Tag>
 8.               <Key>User</Key>
 9.               <Value>Jones</Value>
10.           </Tag>
11.       </TagSet>
12.   </Tagging>
```

The following table provides a list of the allowed XML tags and their characteristics. Values for `Key` and `Value` are case-sensitive. For example, `project=Trinity` and `PROJECT=Trinity` are distinct tags. 



| Tagging element | Description | 
| --- | --- | 
| TagSet | A tag set is a container for all tags assigned to an Amazon RDS resource. There can be only one tag set per resource. You work with a TagSet only through the Amazon RDS API. | 
| Tag | A tag is a user-defined key-value pair. There can be from 1 to 50 tags in a tag set. | 
| Key | A key is the required name of the tag. For restrictions, see [Tag structure in Amazon RDS](#Overview.Tagging.Structure).<br />The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with `aws:` or `rds:`. The string can only contain only the set of Unicode letters, digits, white space, '\_', '.', '/', '=', '\+', '-' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").<br />Keys must be unique to a tag set. For example, you cannot have a key-pair in a tag set with the key the same but with different values, such as project/Trinity and project/Xanadu.  | 
| Value | A value is the optional value of the tag. For restrictions, see [Tag structure in Amazon RDS](#Overview.Tagging.Structure).<br />The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with `aws:` or `rds:`. The string can only contain only the set of Unicode letters, digits, white space, '\_', '.', '/', '=', '\+', '-' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").<br />Values do not have to be unique in a tag set and can be null. For example, you can have a key-value pair in a tag set of project/Trinity and cost-center/Trinity. | 
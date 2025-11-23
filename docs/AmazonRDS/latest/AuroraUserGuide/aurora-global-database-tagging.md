# Tagging Amazon Aurora Global Database resources

With the Aurora Global Database feature, you can apply RDS tags to resources at different levels within a global
database. If you aren't familiar with how tags are used with AWS or Aurora resources, see
[Tagging Amazon Aurora and Amazon RDS resources](USER_Tagging.md "USER_Tagging.md") before applying tags within your global database.

###### Note

Because AWS processes tag data as part of its cost-reporting mechanisms, don't include any sensitive
data or personally identifiable information (PII) in the tag names or values.

You can apply tags to the following kinds of resources within a global database:

- The container object for your entire global database. This resource is known as the global cluster.

After you create the global cluster by performing an **Add AWS Region** operation in the
console, you can add tags by using the details page for the global cluster. On the **Tags**
tab within the global cluster details page, you can add, remove, or modify tags and their associated values
by choosing **Manage tags**.

With the AWS CLI and RDS API, you can add tags to the global cluster at the same time you create it. You can
also add, remove, or modify tags for an existing global cluster.

- The primary cluster. You use the same procedures for working with tags here as for standalone Aurora
  clusters. You can set up the tags before turning the original Aurora cluster into a global database. You can
  also add, remove, or modify tags and their associated values by choosing **Manage tags** on
  the **Tags** tab within the DB cluster details page.
- Any secondary clusters. You use the same procedures for working with tags here as for standalone Aurora
  clusters. You can set up the tags at the same time as you create a secondary Aurora cluster by using the
  **Add AWS Region** action in the console. You can also add, remove, or modify tags and
  their associated values by choosing **Manage tags** on the **Tags** tab
  within the DB cluster details page.
- Individual DB instances within the primary or secondary clusters. You use the same procedures for working
  with tags here as for Aurora or RDS DB instances. You can set up the tags at the same time as you add a new
  DB instance to the Aurora cluster by using the **Add reader** action in the console. You can
  also add, remove, or modify tags and their associated values by choosing **Manage tags** on
  the **Tags** tab within the DB instance details page.

Here are some examples of the kinds of tags you might assign within a global database:

- You might add tags to the global cluster to record overall information about your application, such as
  anonymized identifiers representing owners and contacts within your organization. You might use tags to
  represent properties of the application that uses the global database.
- You might add tags to the primary cluster and secondary clusters to track costs for your application at the
  AWS Region level. For details about that procedure, see
  [How AWS billing works with tags in Amazon RDS](USER_Tagging.md#Tagging.Billing "USER_Tagging.md#Tagging.Billing").
- You might add tags to specific DB instances with the Aurora clusters to indicate their special purpose. For
  example, within the primary cluster, you might have a reader instance with a low failover priority that is
  used exclusively for report generation. A tag can distinguish this special-purpose DB instance from other
  instances that are dedicated to high availability within the primary cluster.
- You might use tags at all levels of your global database resources to control access through IAM policies.
  For more information, see
  [Controlling
  access to AWS resources](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources") in the _AWS Identity and Access Management User
  Guide_.

###### Tip

In the AWS Management Console, you add tags to the global cluster container as a separate step after you create it. If
you want to avoid any time interval when the global cluster exists without access control tags, you can
apply the tags during the `CreateGlobalCluster` operation by creating that resource through
AWS CLI, RDS API, or a CloudFormation template.

- You might use tags at the cluster level, or for the global cluster, to record information about quality
  assurance and testing of your application. For example, you might specify a tag on a DB cluster to record
  the last time you performed a switchover to that cluster. You might specify a tag on the global cluster to
  record the time of the last disaster recovery drill for the entire application.

## AWS CLI examples of tagging for global databases

The following AWS CLI examples show how you can specify and examine tags for all the types of Aurora resources in
your global database.

You can specify tags for the global cluster container with the `create-global-cluster` command. The
following example creates a global cluster and assigns two tags to it. The tags have keys `tag1`
and `tag2`.

```
`$`  aws rds create-global-cluster --global-cluster-identifier `my_global_cluster_id` \
  --engine aurora-mysql --tags Key=tag1,Value=val1 Key=tag2,Value=val2

```

You can list the tags on the global cluster container with the `describe-global-clusters` command.
When working with tags, you typically run this command first to retrieve the Amazon Resource Name (ARN) of the
global cluster. You use the ARN as a parameter in subsequent commands for working with tags. The following
command displays the tag information in the `TagList` attribute. It also shows the ARN, which is
used as a parameter in the later examples.

```
`$`  aws rds describe-global-clusters --global-cluster-identifier `my_global_cluster_id`
`{
 "GlobalClusters": [
 {
 "Status": "available",
 "Engine": "aurora-mysql",
 "GlobalClusterArn": "`my_global_cluster_arn`",
 ...
 "TagList": [
 {
 "Value": "val1",
 "Key": "tag1"
 },
 {
 "Value": "val2",
 "Key": "tag2"
 }
 ]
 }
 ]
}`

```

You can add new tags with the `add-tags-to-resource` command. With this command, you specify the
Amazon Resource Name (ARN) of the global cluster instead of its identifier. Adding a tag with the same name as
an existing tag overwrites the value of that tag. If you include spaces or special characters in the tag
values, quote the values as appropriate for your operating system or command shell. The following example
modifies the tags of the global cluster from the previous example. Originally, the cluster had tags with keys
`tag1` and `tag2`. After the command finishes, the global cluster has a new tag with key
`tag3`, and the tag with key `tag1` has a different value.

```
`$`  aws rds add-tags-to-resource --resource-name `my_global_cluster_arn` \
  --tags Key=tag1,Value="new value for tag1" Key=tag3,Value="entirely new tag"

`$`  aws rds describe-global-clusters --global-cluster-identifier `my_global_cluster_id`
`{
 "GlobalClusters": [
 {
 "Status": "available",
 "Engine": "aurora-mysql",
 ...
 "TagList": [
 {
 "Value": "new value for tag1",
 "Key": "tag1"
 },
 {
 "Value": "val2",
 "Key": "tag2"
 },
 {
 "Value": "entirely new tag",
 "Key": "tag3"
 }
 ]
 }
 ]
}`

```

You can delete a tag from the global cluster with the `remove-tags-from-resource` command. With
this command, you specify only a set of tag keys, without any tag values. The following example modifies the
tags of the global cluster from the previous example. Originally, the cluster had tags with keys
`tag1`, `tag2`, and `tag3`. After the command finishes, only the tag with key
`tag1` remains.

```
`$`  aws rds remove-tags-from-resource --resource-name `my_global_cluster_arn` --tag-keys tag2 tag3

`$`  aws rds describe-global-clusters --global-cluster-identifier `my_global_cluster_id`
`{
 "GlobalClusters": [
 {
 "Status": "available",
 "Engine": "aurora-mysql",
 ...
 "TagList": [
 {
 "Value": "new value for tag1",
 "Key": "tag1"
 }
 ]
 }
 ]
}`

```

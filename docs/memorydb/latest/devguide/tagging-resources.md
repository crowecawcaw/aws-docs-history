# Tagging your MemoryDB resources

To help you manage your clusters and other MemoryDB resources, you can assign your own metadata to each resource in the form of tags. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This is useful when you have many resources of the same type—you can quickly identify a specific resource based on the tags that you've assigned to it. This topic describes tags and shows you how to create them.

###### Warning

As a best practice, we recommend that you do not include sensitive data in your tags.

A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value, both of which you define.

Tags enable you to categorize your AWS resources in different ways, for example, by purpose or owner. For example, you could define a set of tags for your account's MemoryDB clusters that helps you track each cluster's owner and user group.

We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources.
You can search and filter the resources based on the tags you add. For more information about how to implement an effective
resource tagging strategy, see the [AWS whitepaper Tagging Best Practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf").

Tags don't have any semantic meaning to MemoryDB and are interpreted strictly as a string of characters.
Also, tags are not automatically assigned to your resources. You can edit tag keys and values, and you can remove tags from a resource at any time.
You can set the value of a tag to `null`. If you add a tag that has the same key as an existing tag on that resource, the new value overwrites the old value.
If you delete a resource, any tags for the resource are also deleted.

You can work with tags using the AWS Management Console, the AWS CLI, and the MemoryDB API.

If you're using IAM, you can control which users in your AWS account have permission to create, edit, or delete tags.
For more information, see [Resource-level permissions](iam.md "iam.md").

You can tag most MemoryDB resources that already exist in your account. The table below lists the resources that support tagging.

If you're using the AWS Management Console, you can apply tags to resources by using the [Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md"). Some resource screens enable you to specify tags for a resource when you create the resource; for example, a tag with a key of Name and a value that you specify. In most cases, the console applies the tags immediately after the resource is created (rather than during resource creation). The console may organize resources according to the **Name** tag, but this tag doesn't have any semantic meaning to the MemoryDB service.

Additionally, some resource-creating actions enable you to specify tags for a resource when the resource is created. If tags cannot be applied during resource creation, we roll back the resource creation process. This ensures that resources are either created with tags or not created at all, and that no resources are left untagged at any time. By tagging resources at the time of creation, you can eliminate the need to run custom tagging scripts after resource creation.

If you're using the Amazon MemoryDB API, the AWS CLI, or an AWS SDK, you can use the `Tags` parameter on the relevant MemoryDB API action to apply tags. They are:

- `CreateCluster`
- `CopySnapshot`
- `CreateParameterGroup`
- `CreateSubnetGroup`
- `CreateSnapshot`
- `CreateACL`
- `CreateUser`
- `CreateMultiRegionCluster`
  The following table describes the MemoryDB resources that can be tagged, and the resources that can be tagged on creation using the MemoryDB API, the AWS CLI, or an AWS SDK.

| Tagging support for MemoryDB resources | Resource | Supports tags | Supports tagging on creation |
| -------------------------------------- | -------- | ------------- | ---------------------------- |
| parametergroup                         | Yes      | Yes           |
| subnetgroup                            | Yes      | Yes           |
| cluster                                | Yes      | Yes           |
| snapshot                               | Yes      | Yes           |
| user                                   | Yes      | Yes           |
| acl                                    | Yes      | Yes           |
| multiregioncluster                     | Yes      | Yes           |

You can apply tag-based resource-level permissions in your IAM policies to the MemoryDB API actions that support tagging on creation to implement granular control over the users and groups that can tag resources on creation.
Your resources are properly secured from creation—tags that are applied immediately to your resources. Therefore any tag-based resource-level permissions controlling the use of resources are immediately effective.
Your resources can be tracked and reported on more accurately. You can enforce the use of tagging on new resources, and control which tag keys and values are set on your resources.

For more information, see [Tagging resources examples](#tagging-your-resources-example "#tagging-your-resources-example").

For more information about tagging your resources for billing, see [Monitoring costs with cost allocation tags](tagging.md "tagging.md").

The following rules apply to tagging as part of request operations:

- **CreateCluster** :
  - If the `--cluster-name` is supplied:

  If tags are included in the request, the cluster will be tagged.
  - If the `--snapshot-name` is supplied:

  If tags are included in the request, the cluster will be tagged only with those tags. If no tags are included in the request,
  the snapshot tags will be added to the cluster.

- **CreateSnapshot** :
  - If the `--cluster-name` is supplied:

  If tags are included in the request, only the request tags will be added to the snapshot. If no tags are included in the request,
  the cluster tags will be added to the snapshot.
  - For automatic snapshots:

  Tags will propagate from the cluster tags.

- **CopySnapshot** :

If tags are included in the request, only the request tags will be added to the snapshot.
If no tags are included in the request,
the source snapshot tags will be added to the copied snapshot.

- **TagResource** and **UntagResource** :

Tags will be added/removed from the resource.
MemoryDB multi megion clusters are a global resource. As such, tags can be specified, modified or listed on multi region clusters by invoking the relevant APIs in any given region where MemoryDB Multi-Region is supported. For more information on region support, see [Prerequisites and limitations](multi-region.md "multi-region.md").

Tags on multi region clusters are independent from tags on regional clusters. You can specify different sets of tags on a multi region cluster and it’s contained regional clusters. There is no hierarchical connection between these tags and they are not copied through the hierarchy between these resource types.

When you add or remove tags through the `TagResource` and `UntagResource` APIs, you might not immediately see the latest effective tags in the ListTags API response, due to the tags being eventually consistent specifically for Multi Region clusters.

The following basic restrictions apply to tags:

- Maximum number of tags per resource – 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length – 128 Unicode characters in UTF-8.
- Maximum value length – 256 Unicode characters in UTF-8.
- Although MemoryDB allows for any character in its tags, other services can be restrictive. The allowed characters across services are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . \_ : / @
- Tag keys and values are case-sensitive.
- The `aws:` prefix is reserved for AWS use. If a tag has a tag key with this prefix, then you can't edit or delete the tag's key or value. Tags with the `aws:` prefix do not count against your tags per resource limit.
  You can't terminate, stop, or delete a resource based solely on its tags; you must specify the resource identifier. For example, to delete snapshots that you tagged with a tag key called `DeleteMe`,
  you must use the `DeleteSnapshot` action with the resource identifiers of the snapshots, such as `snap-1234567890abcdef0`.

For more information on MemoryDB resources you can tag, see [Resources you can tag](#tagging-your-resources "#tagging-your-resources").

- Adding tags to a cluster.

```
aws memorydb tag-resource \
--resource-arn arn:aws:memorydb:us-east-1:`111111222233`:cluster/my-cluster \
--tags Key="project",Value="XYZ" Key="memorydb",Value="Service"
```

- Creating a cluster using tags.

```
aws memorydb create-cluster \
--cluster-name testing-tags \
--description cluster-test \
--subnet-group-name test \
--node-type db.r6g.large \
--acl-name open-access \
--tags Key="project",Value="XYZ" Key="memorydb",Value="Service"


```

- Creating a Snapshot with tags.

For this case, if you add tags on request, even if the cluster contains tags, the snapshot will receive only the request tags.

```
aws memorydb create-snapshot \
--cluster-name testing-tags \
--snapshot-name bkp-testing-tags-mycluster \
--tags Key="work",Value="foo"
```

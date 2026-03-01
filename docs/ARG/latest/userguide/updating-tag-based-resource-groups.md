# Update tag-based query groups

The following procedures show you how to update a tag-based query group.

Console
Update a tag-based group by changing the resource types or tags in the
query on which the group is based. You can also add or change the group's
description.

1. Sign in to the [AWS Resource Groups console](https://console.aws.amazon.com/resource-groups "https://console.aws.amazon.com/resource-groups").
2. In the navigation pane, under **[Saved Resource
   Groups](https://console.aws.amazon.com/resource-groups/groups "https://console.aws.amazon.com/resource-groups/groups")**, choose the name of the group, and
   then choose **Edit**.

###### Note

You can update only resource groups that you own. The
**Owner** column shows account ownership
for each resource group. Any groups with an account owner other
than the one you're signed in to were created in AWS License Manager. For
more information, see [Host
resource groups in AWS License Manager](../../../license-manager/latest/userguide/host-resource-groups.md "../../../license-manager/latest/userguide/host-resource-groups.md") in the
_License Manager User Guide_. 3. On the **Edit group** page, under
**Grouping criteria**, add or remove resource
types. You can have a maximum of 20 resource types in a query. To
remove a resource type, choose **X** on the
resource type's label. Choose **View group
resources** to see how the changes affect your group's
resource members. In this walkthrough, we add the resource type
**AWS::RDS::DBInstance** to the query. 4. Still under **Grouping criteria**, edit the tags
as needed. In this example, we filter for resources that have a tag
key of **Stage** and add a tag value of
**Test**. The tag value is optional, but
narrows the results of the query further. To remove a tag, choose
**X** on the tag's label. 5. In **Additional information**, you can edit the
group description. You cannot edit a group's name after the group
has been created. 6. (Optional) In **Group tags**, you can add or
remove tags. Group tags are metadata about your resource group. They
do not affect member resources. To change the resources that are
returned by the resource group's query, edit the tags found under
**Grouping criteria**.

Group tags are useful if you plan to make this group a member of a
larger group. Specifying at least a tag key is required to create a
group. Therefore, be sure to add at least a tag key in
**Group tags** to groups that you plan to nest
into larger groups. 7. Choose **Preview group resources** to retrieve
the updated list of EC2 instances, S3 buckets, and Amazon RDS database
instances in your account that match the specified tag keys. If you
do not see resources in the list that you expect, be sure that the
resources are tagged with tags that you specified
in**Grouping criteria**. 8. When you are finished, choose **Save
changes**.

AWS CLI & AWS SDKs
In the AWS CLI, you update a group's query and update a resource group's
description by using two different commands. You cannot edit an existing
group's name. In the AWS CLI, you can change a tag-based group to a
CloudFormation stack-based group, or vice versa.

1. If you do not want to change the description of your group, skip
   this step and go on to the next. In an AWS CLI session, type the
   following, and then press **Enter**, replacing the
   values for group name and description with your own.

```
`$` `aws resource-groups update-group \
 --group-name `resource-group-name` \
 --description "`description_text`"`
```

The following command is an example.

```
`$` `aws resource-groups update-group \
 --group-name my-resource-group \
 --description "EC2 instances, S3 buckets, and RDS DBs that we are using for the test stage."`
```

The command returns a full, updated description of the
group. 2. To update the query and tags of a group, type the following
command. Replace the values for group name, resource types, tag
keys, and tag values with your own. Then pres
**Enter**. You can have a maximum of 20
resource types in a query.

```
`$` `aws resource-groups update-group-query \
 --group-name `resource-group-name` \
 --resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"`resource_type1`\",\"`resource_type2`\"],\"TagFilters\":[{\"Key\":\"`Key1`\",\"Values\":[\"`Value1`\",\"`Value2`\"]},{\"Key\":\"`Key2`\",\"Values\":[\"`Value1`\",\"`Value2`\"]}]}"}'`
```

The following command is an example.

```
`$` `aws resource-groups update-group-query \
 --group-name my-resource-group \
 --resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\",\"AWS::S3::Bucket\",\"AWS::RDS::DBInstance\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'`
```

The command returns the updated query as a result.

# Update an CloudFormation stack-based

group

The following procedures show you how to update a CloudFormation stack-based group.

Console
You cannot change an CloudFormation stack-based group to a tag-based group in the
AWS Management Console. However, you can change the stack on which the group is based, or
change the stack resource types that you want to include in the group. You
can also add or change the group's description.

1. Sign in to the [AWS Resource Groups console](https://console.aws.amazon.com/resource-groups "https://console.aws.amazon.com/resource-groups").
2. In the navigation pane, under **[Saved resource
   groups](https://console.aws.amazon.com/resource-groups/groups "https://console.aws.amazon.com/resource-groups/groups")**, choose the name of the group, and
   then choose **Edit**.
3. ###### Note

You can update only resource groups that you own. The
**Owner** column shows account ownership
for each resource group. Any groups with an account owner other
than the one you're signed in to were created in AWS License Manager. For
more information, see [Host
resource groups in AWS License Manager](../../../license-manager/latest/userguide/host-resource-groups.md "../../../license-manager/latest/userguide/host-resource-groups.md") in the
_License Manager User Guide_. 4. On the **Edit group** page, under
**Grouping criteria**, to change the stack on
which your group is based, choose the stack from the drop-down list.
A resource group can be based on only one stack. To filter the list
of stacks, start typing the name of the stack. Only stacks with
supported statuses appear in the list. For a list of supported
statuses, see [Creating query-based groups in AWS Resource Groups](gettingstarted-query.md "gettingstarted-query.md") in this guide. 5. Add or remove resource types. Only resource types that are
available in the stack are shown in the drop-down list. The default
is **All supported resource types**. You can have a
maximum of 20 resource types in a query. To remove a resource type,
choose **X** on the resource type's label. For more
information about which resource types are supported and can be in
the group, see [Resource types you can use with AWS Resource Groups and
Tag Editor](supported-resources.md "supported-resources.md"). 6. Choose **Preview group resources** to retrieve
the list of resources in the CloudFormation stack that match your selected
resource types. 7. In **Additional information**, you can edit the
group description. You cannot edit a group's name after the group
has been created. 8. In **Group tags**, add or remove tags. Group tags
are metadata about your resource group. They do not affect member
resources. To change the resources that are returned by the resource
group's query, edit tags in **Grouping
criteria**.

Group tags are useful if you plan to make this group a member of a
larger group. Specifying at least a tag key is required to create a
group. Therefore, be sure to add at least a tag key in
**Group tags** to groups that you plan to nest
into larger groups. 9. When you are finished, choose **Save
changes**.

AWS CLI & AWS SDKs
In the AWS CLI, you update a group's query and update a resource group's
description by using two different commands. You cannot edit an existing
group's name. In the AWS CLI, you can change a tag-based group to a
CloudFormation stack-based group, or vice versa.

1. If you do not want to change the description of your group, skip
   this step and go on to the next. Run the following command,
   replacing the values for group name and description with your
   own.

```
`$` `aws resource-groups update-group \
 --group-name "`resource-group-name`" \
 --description "`description_text`"`
```

The following command is an example.

```
`$` `aws resource-groups update-group \
 --group-name "My-CFN-stack-group" \
 --description "EC2 instances, S3 buckets, and RDS DBs that we are using for the test stage."`
```

The command returns a full, updated description of the
group. 2. To update the query and tags of a group, run the following
command. Replace the values for group name, stack identifier, and
resource types with your own. To add resource types, provide the
full list of resource types in the command, not only resource types
you are adding. You can have a maximum of 20 resource types in a
query.

The `stack_identifier` is the stack ARN,
as shown in the example command.

```
`$` `aws resource-groups update-group-query \
 --group-name `resource-group-name` \
 --description "`description`" \
 --resource-query '{"Type":"CLOUDFORMATION_STACK_1_0","Query":"{\"StackIdentifier\":\"`stack_identifier`\",\"ResourceTypeFilters\":[\"`resource_type1`\",\"`resource_type2`\"]}"}'`
```

The following command is an example.

```
`$` `aws resource-groups update-group-query \
 --group-name "my-resource-group" \
 --description "Updated CloudFormation stack-based group" \
 --resource-query '{"Type":"CLOUDFORMATION_STACK_1_0","Query":"{\"StackIdentifier\":\"arn:aws:cloudformation:us-west-2:810000000000:stack\/AWStestuseraccount\/fb0d5000-aba8-00e8-aa9e-50d5cEXAMPLE\",\"ResourceTypeFilters\":[\"AWS::EC2::Instance\",\"AWS::S3::Bucket\"]}"}'`
```

The command returns the updated query as a result.

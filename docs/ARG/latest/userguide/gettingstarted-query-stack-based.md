# Create an AWS CloudFormation stack-based

group

The following procedures show you how to build a stack-based query and use it to
create a resource group.

Console

1. Sign in to the [AWS Resource Groups console](https://console.aws.amazon.com/resource-groups "https://console.aws.amazon.com/resource-groups").
2. In the navigation pane, choose **[Create Resource
   Group](https://console.aws.amazon.com/resource-groups/groups/new "https://console.aws.amazon.com/resource-groups/groups/new")**.
3. On **Create query-based group**, under
   **Group type**, choose the
   **CloudFormation stack based** group
   type.
4. Choose the stack that you want to be the basis of your group. A
   resource group can be based on only one stack. To filter the list of
   stacks, start typing the name of the stack. Only stacks with
   supported statuses appear in the list.
5. Choose resource types in the stack that you want to include in the
   group. For this walkthrough, keep the default, **All
   supported resource types**. For more information about
   which resource types are supported and can be in the group, see
   [Resource types you can use with AWS Resource Groups and
   Tag Editor](supported-resources.md "supported-resources.md").
6. Choose **View group resources** to return the
   list of resources in the AWS CloudFormation stack that match your selected
   resource types.
7. After you have the results that you want, create a group based on
   this query.
   1. Under **Group details**, for
      **Group name**, type a name for your
      resource group.

   A resource group name can have a maximum of 128
   characters, including letters, numbers, hyphens, periods,
   and underscores. The name cannot start with `AWS`
   or `aws`. These are reserved. A resource group
   name must be unique in the current Region in your
   account. 2. (Optional) In **Group description**,
   enter a description of your group. 3. (Optional) In **Group tags**, add tag key
   and value pairs that apply only to the resource group, not
   the member resources in the group.

   Group tags are useful if you plan to make this group a
   member of a larger group. Because specifying at least a tag
   key is required to create a group, be sure to add at least a
   tag key in **Group tags** to groups that
   you plan to nest into larger groups.

8. When you're finished, choose **Create
   group**.

AWS CLI & AWS SDKs
An AWS CloudFormation stack-based group is based on a query of type
`CLOUDFORMATION_STACK_1_0`.

1. Run the following command, replacing the values for group name,
   description, stack identifier, and resource types with your own.
   Descriptions can have a maximum of 512 characters, including
   letters, numbers, hyphens, underscores, punctuation, and
   spaces.

If you do not specify resource types, Resource Groups includes all supported
resource types in the stack. You can have a maximum of 20 resource
types in a query. A resource group name can have a maximum of 128
characters, including letters, numbers, hyphens, periods, and
underscores. The name cannot start with `AWS` or
`aws`. These are reserved. A resource group name must
be unique in your account.

The `stack_identifier` is the stack ARN,
as shown in the example command.

```
`$` `aws resource-groups create-group \
 --name `group_name` \
 --description "`description`" \
 --resource-query '{"Type":"CLOUDFORMATION_STACK_1_0","Query":"{\"StackIdentifier\":\"`stack_identifier`\",\"ResourceTypeFilters\":[\"`resource_type1`\",\"`resource_type2`\"]}"}'`
```

The following command is an example.

```
`$` `aws resource-groups create-group \
 --name My-CFN-stack-group \
 --description "My first CloudFormation stack-based group" \
 --resource-query '{"Type":"CLOUDFORMATION_STACK_1_0","Query":"{\"StackIdentifier\":\"arn:aws:cloudformation:us-west-2:123456789012:stack\/`AWStestuseraccount`\/fb0d5000-aba8-00e8-aa9e-50d5cEXAMPLE\",\"ResourceTypeFilters\":[\"AWS::EC2::Instance\",\"AWS::S3::Bucket\"]}"}'`
```

2. The following are returned in the response to the command.
   - A full description of the group you have created.
   - The resource query that you used to create the
     group.

# Build a tag-based query and create a group

The following procedures show you how to build a tag-based query and use it to create
a resource group.

Console

1. Sign in to the [AWS Resource Groups console](https://console.aws.amazon.com/resource-groups "https://console.aws.amazon.com/resource-groups").
2. In the navigation pane, choose **[Create Resource
   Group](https://console.aws.amazon.com/resource-groups/groups/new "https://console.aws.amazon.com/resource-groups/groups/new")**.
3. On the **Create query-based group** page, under
   **Group type**, choose the **Tag
   based** group type.
4. Under **Grouping criteria**, choose the resource
   types that you want to be in your resource group. You can have a
   maximum of 20 resource types in a query. For this walkthrough,
   choose **AWS::EC2::Instance** and
   **AWS::S3::Bucket**.
5. Still under **Grouping criteria**, for
   **Tags**, specify a tag key, or a tag key and
   value pair, to limit the matching resources to include only those
   that are tagged with your specified values. Choose
   **Add** or press **Enter**
   when you've finished your tag. In this example, filter for resources
   that have a tag key of **Stage**. The tag value is
   optional, but narrows the results of the query further. You can add
   multiple values for a tag key by adding an `OR` operator
   between tag values. To add more tags, choose
   **Add**. Queries assign an `AND`
   operator to tags, so any resource that matches the specified
   resource types and all specified tags is returned by the
   query.
6. Still under **Grouping criteria**, choose
   **Preview group resources** to return the list
   of EC2 instances and S3 buckets in your account that match the
   specified tag key or keys.
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
A tag-based group is based on a query of type
`TAG_FILTERS_1_0`.

1. In an AWS CLI session, type the following, and then press
   **Enter**, replacing the values for group name,
   description, resource types, tag keys, and tag values with your own.
   Descriptions can have a maximum of 512 characters, including
   letters, numbers, hyphens, underscores, punctuation, and spaces. You
   can have a maximum of 20 resource types in a query. A resource group
   name can have a maximum of 128 characters, including letters,
   numbers, hyphens, periods, and underscores. The name cannot start
   with `AWS` or `aws`. These are reserved. A
   resource group name must be unique in your account.

At least one value for `ResourceTypeFilters` is
required. To specify all resource types, use
`AWS::AllSupported` as the
`ResourceTypeFilters` value.

```
`$` `aws resource-groups create-group \
 --name `resource-group-name` \
 --resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"`resource_type1`\",\"`resource_type2`\"],\"TagFilters\":[{\"Key\":\"`Key1`\",\"Values\":[\"`Value1`\",\"`Value2`\"]},{\"Key\":\"`Key2`\",\"Values\":[\"`Value1`\",\"`Value2`\"]}]}"}'`
```

The following command is an example.

```
`$` `aws resource-groups create-group \
 --name my-resource-group \
 --resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'`
```

The following command is an example that includes all supported
resource types.

```
`$` `aws resource-groups create-group \
 --name my-resource-group \
 --resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'`
```

2. The following are returned in the response to the command.
   - A full description of the group you have created.
   - The resource query that you used to create the
     group.
   - The tags that are associated with the group.

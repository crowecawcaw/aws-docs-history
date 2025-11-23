# Creating query-based groups in AWS Resource Groups

## Types of resource group queries

In AWS Resource Groups, a _query_ is the foundation of a query-based group.
You can base a resource group on one of two types of queries.

**Tag-based**

Tag-based queries include lists of resource types that are specified in
the following format
`AWS::`service`::`resource``,
and tags. _Tags_ are keys that help identify and sort
your resources in your organization. Optionally, tags include values for
keys.

For a tag-based query, you also specify the tags that are shared by the
resources that you want to be members of the group. For example, if you want
to create a resource group that has all of the Amazon EC2 instances and Amazon S3
buckets that you are using to run the testing stage of an application, and
you have instances and buckets that are tagged this way, choose the
`AWS::EC2::Instance` and `AWS::S3::Bucket`
resource types from the drop-down list, and then specify the tag key
`Stage`, with a tag value of
`Test`.

The syntax of the `ResourceQuery` parameter of a tag-based
resource group contains the following elements:

- `Type`

This element indicates which kind of query defines this resource
group. To create a tag-based resource group, specify the value
`TAG_FILTERS_1_0`, as follows:

```
"Type": "TAG_FILTERS_1_0"
```

- `Query`

This element defines the actual query used to match against
resources. It contains a string representation of a JSON structure
with the following elements:

    + `ResourceTypeFilters`



    This element limits the results to only those resource
     types that match the filter. You can specify the following
     values:




    	- `"AWS::AllSupported"` – to
    	 specify that the results can include resources of
    	 any type that match the query and that are currently
    	 supported by the Resource Groups service.
    	- `"AWS::`service-id`::`resource-type``
    	 – a comma separated list of resource-type
    	 specification strings with this format: , such as
    	 `"AWS::EC2::Instance"`.
    + `TagFilters`



    This element specifies key/value string pairs that are
     compared to the tags attached to your resources. Those with
     a tag key and value that match the filter are included in
     the group. Each filter consists of these elements:




    	- `"Key"` – a string with a key
    	 name. Only resources that have tags with a matching
    	 key name match the filter and are members of the
    	 group.
    	- `"Values"` – a string with a
    	 comma separated list of values for the specified
    	 key. Only resources with a matching tag key and a
    	 value that matches one in this list are members of
    	 the group.

All of these JSON elements must be combined into a single-line string
representation of the JSON structure. For example, consider a
`Query` with the following example JSON structure. This query
is meant to match only Amazon EC2 instances that have a tag "Stage" with a value
"Test".

```
{
    "ResourceTypeFilters": [ "AWS::EC2::Instance" ],
    "TagFilters": [
        {
            "Key": "Stage",
            "Values": [ "Test" ]
        }
    ]
}
```

That JSON can be represented as the following single-line string, and used
as the value of the `Query` element. Because the value of a JSON
structure must be a double-quoted string, you must escape any embedded
double-quote characters or forward slash characters by preceding each with a
backslash as shown here:

```
"Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"
```

The complete `ResourceQuery` string is then represented as
shown here, as a CLI command parameter:

```
--resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'
```

**CloudFormation stack-based**

In an CloudFormation stack-based query, you choose an CloudFormation stack in your account
in the current region, and then choose resource types in the stack that you
want to be in the group. You can base your query on only one CloudFormation stack.

###### Note

An CloudFormation stack can contain other CloudFormation "child" stacks. However, a
resource group based on a "parent" stack doesn't get all of the child
stacks' resources as group members. Resource groups adds the child
stacks to the parent stack's resource group as single group members and
doesn't expand them.

Resource Groups supports queries based on CloudFormation stacks that have one of the
following statuses.

- `CREATE_COMPLETE`
- `CREATE_IN_PROGRESS`
- `DELETE_FAILED`
- `DELETE_IN_PROGRESS`
- `REVIEW_IN_PROGRESS`

###### Important

Only resources that are directly created as part of the stack in the
query are included in the resource group. Resources created later by
members of the CloudFormation stack do not become members of the group. For
example, if an auto-scaling group is created by CloudFormation as part of the
stack, then that auto-scaling group **_is_** a member of the group.
However, an Amazon EC2 instance created by that auto-scaling group as part of
its operation **_is
not_** a member of the CloudFormation stack-based
resource group.

If you create a group based on an CloudFormation stack, and the stack's status
changes to one that is no longer supported as a basis for a group query,
such as `DELETE_COMPLETE`, the resource group still exists, but
it has no member resources.

After you create a resource group, you can perform tasks on the resources in the
group.

The syntax of the `ResourceQuery` parameter of a CloudFormation stack-based
resource group contains the following elements:

- `Type`

This element indicates which kind of query defines this resource group.

To create a CloudFormation stack-based resource group, specify the value
`CLOUDFORMATION_STACK_1_0`, as follows:

```
"Type": "CLOUDFORMATION_STACK_1_0"
```

- `Query`

This element defines the actual query used to match against resources. It
contains a string representation of a JSON structure with the following
elements:

    + `ResourceTypeFilters`



    This element limits the results to only those resource types that
     match the filter. You can specify the following values:




    	- `"AWS::AllSupported"` – to specify that the
    	 results can include resources of any type that match the
    	 query.
    	- `"AWS::`service-id`::`resource-type``
    	 – a comma separated list of resource-type specification
    	 strings with this format: , such as
    	 `"AWS::EC2::Instance"`.
    + `StackIdentifier`



    This element specifies the Amazon Resource Name (ARN) of the CloudFormation
     stack whose resources you want to include in the group.

All of these JSON elements must be combined into a single-line string representation
of the JSON structure. For example, consider a `Query` with the following
example JSON structure. This query is meant to match only Amazon S3 buckets that are part of
the specified CloudFormation stack.

```
{
    "ResourceTypeFilters": [ "AWS::S3::Bucket" ],
    "StackIdentifier": "arn:aws:cloudformation:us-west-2:123456789012:stack/`MyCloudFormationStackName`/fb0d5000-aba8-00e8-aa9e-50d5cEXAMPLE"
}
```

That JSON can be represented as the following single-line string, and used as the
value of the `Query` element. Because the value of a JSON structure must be a
double-quoted string, you must escape any embedded double-quote characters or forward
slash characters by preceding each with a backslash as shown here:

```
"Query":"{\"ResourceTypeFilters\":[\"AWS::S3::Bucket\"],\"StackIdentifier\":\"arn:aws:cloudformation:us-west-2:123456789012:stack\/`MyCloudFormationStackName`\/fb0d5000-aba8-00e8-aa9e-50d5cEXAMPLE\"
```

The complete `ResourceQuery` string is then represented as shown here, as a
CLI command parameter:

```
--resource-query '{"Type":"CLOUDFORMATION_STACK_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::S3::Bucket\"],\"StackIdentifier\":\"arn:aws:cloudformation:us-west-2:123456789012:stack\/`MyCloudFormationStackName`\/fb0d5000-aba8-00e8-aa9e-50d5cEXAMPLE\"}'
```

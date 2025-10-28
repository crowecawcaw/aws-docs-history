AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Example Resource Explorer search queries

The following examples show the syntax for common types of queries that you can use in
AWS Resource Explorer.

###### Important

If you use the AWS CLI `search` command and your `--query-string`
parameter value has the `-` operator as the first character, you must
separate the parameter name from its value with an equal sign character (`=`)
instead of the usual space character. If you use the space character, the CLI
misinterprets the string. For example, the following query fails.

```
aws resource-explorer-2 search --query-string "-tag:none region:us-east-1"
```

The following corrected query, with an `=` replacing the space, works as
expected.

```
aws resource-explorer-2 search --query-string`=`"-tag:none region:us-east-1"
```

If you change the order of the filters in the query string so that the `-`
isn't the first character in the parameter value, you can use the standard space
character. The following query works.

```
aws resource-explorer-2 search --query-string "region:us-east-1 -tag:none"
```

## Search for untagged resources

If you want to use [attribute-based access control
(ABAC)](https://aws.amazon.com/identity/attribute-based-access-control/ "https://aws.amazon.com/identity/attribute-based-access-control/") in your account, use [cost-based
allocation](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md"), or perform tag-based automation against your resources, you need
to know which resources in your account might be missing tags. The following example
query uses the special case filter [tag: none](using-search-query-syntax.md#query-syntax-filters "using-search-query-syntax.md#query-syntax-filters")
to return all resources that are missing user-generated tags.

The `tag:none` filter applies to only tags that are _created by the user_. Tags that are generated and maintained by AWS are
exempt from this filter and still appear in the results.

```
tag:none
```

To also exclude all AWS created system tags, add a second filter as shown in the
following example. The first element in the query string duplicates the previous example
by filtering out all user-created tags. AWS created system tags _always_ begin with the letters `aws`. Therefore,
you can use the [logical NOT operator ( - )](using-search-query-syntax.md#query-syntax-operators "using-search-query-syntax.md#query-syntax-operators")
with the [tag.key filter](using-search-query-syntax.md#query-syntax-filters "using-search-query-syntax.md#query-syntax-filters") to also exclude any
resources that have a tag with a key name that begins with `aws`.

```
tag:none -tag.key:aws*
```

## Search for tagged resources

To find all resources that have a tag of any type, you can use the [logical NOT operator ( - )](using-search-query-syntax.md#query-syntax-operators "using-search-query-syntax.md#query-syntax-operators") with the special
case [tag: none](using-search-query-syntax.md#query-syntax-filters "using-search-query-syntax.md#query-syntax-filters") filter as follows.

```
-tag:none
```

## Search for resources that are missing a specific tag

Also related to ABAC, you might want to search for all resources that don't have a tag
with a specified key. The following example uses the [logical NOT operator -](using-search-query-syntax.md#query-syntax-operators "using-search-query-syntax.md#query-syntax-operators") to
return all resources that are missing a tag with the key name
`Department`.

```
-tag.key:Department
```

## Search for resources that have invalid tag values

For compliance reasons, you might want to search for all resources that have missing
or misspelled tag values on important tags. The following example returns all resources
that have a tag with the key name `environment`. However, the query filters
out any resource that has one of the valid values `prod`, `integ`,
or `dev`. Any results that appear from this query have some other value that
you should investigate and correct.

###### Important

Resource Explorer searches are **_not_** case sensitive and can't distinguish between key
names and values that differ only by how they're capitalized. For example, the
values in the following example match `PROD`, `prod`,
`PrOd`, or any variation. However, some applications use tags in
case-sensitive ways. We recommend that you standardize on a capitalization strategy
for your organization, such as using only lower-case tag key names and values. A
consistent approach can help avoid the confusion that can be caused by having tags
that differ only by how they're capitalized.

```
tag.key:environment -tag:environment=prod -tag:environment=integ -tag:environment=dev
```

## Search for resources in a subset of AWS Regions

Use the ['\*' wildcard
operator](using-search-query-syntax.md#query-syntax-operators "using-search-query-syntax.md#query-syntax-operators") to match all Regions in a certain area of the world. The following
example returns all resources that are in Regions in Europe (EU).

```
region:eu-*
```

## Search for global resources

Use the special case `global` value for the `region:` filter to
find your resources that are considered to be global and not associated with an
individual Region.

```
region:global
```

## Search for resources of a certain type that are located in a

specific Region

When you use multiple filters, Resource Explorer evaluates the expression by combining the
prefixes with implicit logical `AND` operators. The following example returns
all resources that are in the Asia Pacific (Hong Kong) Region `AND` are Amazon EC2
instances.

```
region:ap-east-1 resourcetype:ec2:instance
```

###### Note

Because of the implicit `AND`, you can successfully use only one filter
for an attribute that can have only one value associated with the resource. For
example, a resource can be part of only one AWS Region. Therefore, the following
query returns no results.

```
region:us-east-1 region:us-west-1
```

This limitation does **_not_** apply to the filters for attributes that can have
multiple values at the same time, such as `tag:`, `tag.key:`,
and `tag.value:`.

## Search for resources that have a multi-word term

Surround a multi-word term with [double
quotation marks (")](using-search-query-syntax.md#query-syntax-operators "using-search-query-syntax.md#query-syntax-operators") to return only results that have the entire
term in the specified order. Without double quotation marks, Resource Explorer returns resources
that match any individual words that make up the term. For example, the following query
uses the double quotation marks to return only resources that match the term `"west
 wing"`. The query does **_not_** match resources in the `us-west-2`
AWS Region (or any other Region that includes `west` in its code) or
resources that match the word "wing" without the word "west".

```
"west wing"
```

## Search for resources that are part of a specified CloudFormation

stack

When you create a resource as part of an AWS CloudFormation stack, they are all tagged with the
stack's name _automatically_. The following example
returns all resources that were created as part of the specified stack.

```
tag:aws:cloudformation:stack-name=`my-stack-name`
```

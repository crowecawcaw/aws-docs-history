AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Search query syntax reference for Resource Explorer

AWS Resource Explorer helps you to find individual AWS resources in your AWS accounts. To help
you find the exact resources you're looking for, Resource Explorer accepts search query strings that
support the syntax described in this topic. For example queries that demonstrate how to use
the features described here, see [Example Resource Explorer search queries](using-search-query-examples.md "using-search-query-examples.md").

###### Note

At this time, tags attached to AWS Identity and Access Management (IAM) resources, such as roles or users,
are not indexed.

## How queries work in Resource Explorer

Search queries always use a view. If you don't explicitly specify one, Resource Explorer uses
the view designated as the default for the AWS Region that you're working in.

Views determine which resources are available for you to query. You can create
different views that each return a different set of resources.

For example, you could create a view that includes only those resources that are
tagged with the key `Environment` and the value `Production`.
Then, you could choose to grant access for that view to only those users who have a
business reason to view those resources. A separate view that includes the
`Alpha` or `Beta` environment resources could be accessed by
different users who need to view those resources. For information about controlling who
gets access to which views, see [Granting access to Resource Explorer views for
search](configure-views-grant-access.md "configure-views-grant-access.md").

## Query string syntax

This section provides information about basic aspects of query syntax, filters, and
filter operators.

### Search query string

A `QueryString` is a set of free-form text keywords that Resource Explorer
implicitly joins using `OR` operator logic. You seperate each keyword
from the others by using a space, as shown in the following example:

`ec2 billing test gamma`

Resource Explorer evaluates this list of keywords to mean:

`ec2 **OR** billing **OR** test **OR** gamma`

The search results for this example are based on the following behavior:

- Resource Explorer sorts results by relevance and gives higher preference to resources
  that match a greater number of the search terms. Resources that match more
  of the terms are pushed higher in the search results.
- Resources that do not match one or more of the terms aren't excluded from
  the results, but Resource Explorer considers them of lower relevance. Resources that
  don't match the terms are pushed further down in the search results.

If you specify an empty string for the `QueryString` parameter, your
query returns the first 1,000 resources that are available through the view
used for the operation. The maximum number of resources that can be returned by any
query is 1,000.

###### Note

AWS reserves the right to update the matching logic and relevance algorithms
for evaluating free-form text keywords so that we can provide customers with the
most relevant results. Therefore, results returned for the same queries using
free-form text keywords might change over time. Where you require more
deterministic results, we recommend that you use filters. Filter matching logic
does not change over time.

### Filters

You can limit the results of your query more strictly by including **_filters_**.

If you use more than one filter in the search query, Resource Explorer joins the filters
using the `AND` operator. If a filter contains multiple values, Resource Explorer
uses the `OR` operator between each value.

For example, consider the following query that consists of two free-form keywords
and two specified filters:

`test instance service:EC2 region:us-west-2`

Resource Explorer evaluates the query as follows:

`( test **OR** instance ) **AND** service:EC2 **AND**
 region:us-west-2`

The query string `test instance` follows the logical `OR`
syntax of a keyword query string while the specified `service:` and
`region:` filters follow the implicit `AND` syntax. This
example query's results include any resources that are associated with Amazon EC2, and
are in the US West (Oregon) AWS Region, and have at least one of the keywords
attached in some way.

###### Note

Because of the implicit `AND` operator, you can successfully use
only one filter for an attribute that can have only one value associated with
the resource. For example, a resource can be part of only one AWS Region.
Therefore, the following query returns no results.

`region:us-east-1 region:us-west-1`

This limitation does not apply to the filters for attributes that can have
multiple values at the same time, such as `tag:`,
`tag.key:`, and `tag.value:`.

**Specifying multiple filter values**

Resource Explorer allows you to specify multiple values for each filter, which Resource Explorer joins
with the `OR` operator. You can use this operator to scope down results
to multiple resource types, accounts, tags, and more with a simple syntax. When
specifying multiple values in the same filter, separate each value with a
comma.

For example, consider the following query that consists of two filters, where one
filter includes multiple possible values separated by a comma:

`service:EC2 region:us-west-2,us-east-1`

Given the comma-separated syntax of the `region:` filter, Resource Explorer
evaluates the query as follows:

`(service:EC2) **AND** (region:us-west-2
 **OR** region:us-east-1)`

Resource Explorer applies the `OR` operator to the comma-separated
`region:` filter values.

This example query's results include any resources that are associated with Amazon EC2
and are in the US West (Oregon) or US East (N. Virginia) AWS Region.

###### Note

You can escape or quote the commas used to specify the `OR`
operator like other special characters. For example,
`tag.key:comma\,literal` or `tag.key:"comma,literal"`.

The following table lists the available filter names that you can use
in a Resource Explorer search query.

| Filter name              | Description and example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `accountid:`             | The AWS account that owns the resource. Resource Explorer includes in<br>the results only the resources that are owned by the specified<br>account.<br>`accountid:123456789012`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `application:`           | This filter enables you to search for resources with an<br>`awsApplication` tag key and a resource group<br>value. You can search by application name or the application<br>resource group ARN.<br>`application:MyApplicationName`<br>`application:arn:aws:resource-groups:us-east-1:123456789012:group/MyApplicationName/123456789abced`<br>`arn:aws:resource-groups:us-east-1:123456789012:group/MyApplicationName/123456789abced`<br>NoteTo use this filter, your view must have access to tagging<br>data.                                                                                                                |
| `id:`                    | The identifier of an individual resource, expressed as an<br>[Amazon resource name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").<br>`id:arn:aws:license-manager:us-east-1:123456789012:license-configuration:lic-ecbd5574fd92cb0d312baea26EXAMPLE`                                                                                                                                                                                                                                                                                                   |
| `region:`                | The AWS Region where the resource is located. Resource Explorer<br>includes in the results only the resources that reside in the<br>specified AWS Region.<br>`region:us-east-1`<br>NoteTyping only the Region code (without a filter, such as<br>`us-east-1`) doesn't return the same<br>results as `region:us-east-1`. This outcome<br>is because, as a free-form text keyword that isn't a filter,<br>the Region code is broken down into its individual pieces.<br>For example, `us-east-1` is searched as<br>`us`, `east`, and `1`.<br>This breakdown into components doesn't occur when you use<br>the `region:` prefix. |
| `region:global`          | A special case for the `region:` filter that you<br>can use to find resources that are not associated with an<br>individual AWS Region but are considered to be global in<br>scope.<br>`region:global`<br>NoteTyping only the keyword `global` doesn't return<br>the same results as `region:global` because the<br>literal word "global" is not attached to global resources.<br>Typing `global` as a keyword returns only those<br>resources that have that literal string associated with the<br>resource.                                                                                                                 |
| `resourcetype:`          | The resource type in<br>``service`:`type``<br>notation. Resource Explorer includes in the results only the resources of<br>the specified type.<br>`resourcetype:ec2:instance`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `resourcetype.supports:` | This filter enables you to search for resources that support<br>tags. `tags` is the only supported value. Resource Explorer<br>includes in the results only the resources that are taggable.<br>`resourcetype.supports:tags`                                                                                                                                                                                                                                                                                                                                                                                                  |
| `service:`               | The AWS service that is associated with the type of the<br>resource. Resource Explorer includes in the results only the resources that<br>are created and managed by the specified service.<br>`service:ec2`                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `tag:`                   | A tag key/value pair expressed as<br>`<key>=<value>`. Resource Explorer includes in<br>the results only the resources that have a tag with both a<br>matching key and the specified value.<br>`tag:environment=production`<br>To use this filter, your view must have an<br>`IncludeProperty` with the \*_Name_<br>• parameter specified as `tags`.<br>This configuration displays the `tag` property and<br>value in resource search results.                                                                                                                                                                                |
| `tag:all`                | A special case of the `tag:` filter that enables<br>you to search for resources that have one or more user-created<br>tags attached, even if the resource type is not supported in<br>Resource Explorer.<br>To use this filter, your view must have an<br>`IncludeProperty` with the \*_Name_<br>• parameter specified as `tags`.<br>This configuration displays the `tag` property and<br>value in resource search results.<br>NoteResources with \*AWS<br>service-created<br>• tags still appear in results<br>for this filter.                                                                                             |
| `tag:none`               | A special case of the `tag:` filter that enables<br>you to search for any resources that don't have any user-created<br>tags attached.<br>To use this filter, your view must have an<br>`IncludeProperty` with the \*_Name_<br>• parameter specified as `tags`.<br>This configuration displays the `tag` property and<br>value in resource search results.<br>NoteResources with \*AWS<br>service-created<br>• tags still appear in results<br>for this filter.                                                                                                                                                               |
| `tag.key:`               | A tag key. Resource Explorer includes in the results only the resources<br>that have a tag with a matching key, regardless of value.<br>`tag.key:environment`<br>To use this filter, your view must have an<br>`IncludeProperty` with the \*_Name_<br>• parameter specified as `tags`.<br>This configuration displays the `tag` property and<br>value in resource search results.                                                                                                                                                                                                                                             |
| `tag.value:`             | A tag value. Resource Explorer includes in the results only the resources<br>that have a tag with a matching value, regardless of the key<br>name.<br>`tag.value:production`<br>To use this filter, your view must have an<br>`IncludeProperty` with the \*_Name_<br>• parameter specified as `tags`.<br>This configuration displays the `tag` property and<br>value in resource search results.                                                                                                                                                                                                                              |

### Filter operators

You can modify your keywords and filters by including one of the operators shown
in the following table as part of the string.

| Operator                                                     | Description and example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"`multiple word<br>phrase`"`<br>or<br>"`hyphenated-phrase`" | Surround a multi-word phrase that should be treated as a<br>single keyword with double quotation marks characters (`"<br>"`). Resource Explorer includes only those resources that match<br>the entire phrase, with all words together, and in the specified<br>order.<br>If you don't use the double quotation marks, Resource Explorer breaks up<br>the phrase into its components by spaces or hyphens, and<br>includes resources that match the individual components, even if<br>they're not together or in a different order. Quotations should<br>be around everything after the operator.<br>`"This matches only resources with the whole<br>sentence."`<br>`This matches resources with any of the<br>words.`<br>`"us-east-1"` – matches only resources that<br>associated with that exact Region.<br>`us-east-1` – matches any resource that<br>contain "us" or "east" or "1".<br>`-tag:"environment=production"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ``keyword`\*`                                                | Prefix wildcard matching. You can place a wildcard character<br>(an asterisk `*`) at only the end of the string.<br>Resource Explorer includes in the results only the resources with values<br>that start with the prefix text before the `*`. The<br>following example matches all AWS Regions that begin with<br>`us-east`.<br>`region:us-east*` ImportantUnified Search automatically inserts a wildcard character (`*`) operator at the<br>end of the first keyword in the string. This means that unified search results include resources<br>that match any string that starts with the specified keyword.The search performed by the **Query*<br>• text box on the [Resource search](https://console.aws.amazon.com/resource-explorer/home#/explorer "https://console.aws.amazon.com/resource-explorer/home#/explorer") page in the<br>Resource Explorer console does ***not*\*\*<br>automatically append a wildcard character. You can insert a `*` manually after<br>any term in the search string.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `value``,``value`                                            | `OR` operator. You can place a comma<br>(`,`) between multiple values in a filter. The<br>following example causes Resource Explorer to return search results that<br>match any of the values in the `region:` filter.<br>`service:EC2 region:us-west-2,us-east-1`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `-`keyword``                                                 | `NOT` operator. You can place a hyphen<br>(`-`) at the beginning of its keyword or filter<br>to invert the search results. Resource Explorer **_excludes_**<br>from the results any resources that match the keyword or filter<br>that follows this operator. The following example causes all<br>resources associated with the Amazon EC2 service to be excluded from<br>the results.<br>`-service:ec2`<br>ImportantIf you use the AWS CLI `search` command and your<br>`--query-string` parameter value has the<br>`-` operator as the first character, you must<br>separate the parameter name from its value with an equal<br>sign character (`=`) instead of the usual space<br>character. If you use the space character, the CLI<br>misinterprets the string. For example, the following query<br>fails.<br>`<br>aws resource-explorer-2 search --query-string "-tag:none region:us-east-1"<br>`<br>The following corrected query string, with an<br>`=` replacing the space, works as<br>expected.<br>``<br>aws resource-explorer-2 search --query-string`=`"-tag:none region:us-east-1"<br>``<br>If you change the order of the filters in the query string<br>so that the `-` isn't the first character in the<br>parameter value, you can use the standard space character.<br>The following query string works.<br>`<br>aws resource-explorer-2 search --query-string "region:us-east-1 -tag:none"<br>` |
| `\`<special<br>character>``                                  | You can escape special characters that must be included<br>exactly as shown rather than interpreted. If your text includes<br>one of the special characters ( `<br>• "<br>• : = \`), you<br>must precede that character with a backslash (`\`) to<br>ensure that the character is taken literally. The following<br>example shows how to use a free-form text keyword that includes<br>the hyphen (`-`) character<br>(`"my-key-word"`).<br>Also, to prevent Resource Explorer from breaking up the expression at the<br>hyphens into three separate keywords, you can surround the<br>entire phrase in double quotation marks.<br>`"my\-key\-word"`<br>To insert a literal backslash, insert two backslash characters<br>in a row. The first backslash is interpreted as the escape and<br>the second backslash is the literal character to insert.<br>`"some_text\\some_more_text"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

###### Note

If the view includes the tags attached to the resources, then the
`Search` operation doesn't throw validation errors for search
strings, because a filter that's not valid could also be interpreted as a free-form
text search. For example, even though `cat:blue`
**_looks_** like a
filter, Resource Explorer can't parse it as one because `cat:` isn't one of the
valid, defined filters. Instead Resource Explorer interprets the whole string as a free-form
search string to allow it to match things like a tag key name or a piece of an
ARN.

The operation does throw a validation error if either of the following is
true:

- The view doesn't include information about tags

- The search query explicitly uses a tag filter (`tag.key:`,
  `tag.value:`, or `tag:`)

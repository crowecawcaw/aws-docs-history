# Troubleshooting Resource Explorer search issues

Use the information here to help you diagnose and fix common errors that can occur when
you search for resources by using Resource Explorer.

###### Topics

- [Why are some resources
  missing from my Resource Explorer search results?](#troubleshooting_search_missing-resources "#troubleshooting_search_missing-resources")
- [Why are some searches limited to 1,000
  results?](#troubleshooting_limited_results "#troubleshooting_limited_results")
- [Why are my resources not appearing in
  Unified Search results in the console?](#troubleshooting_search_unified "#troubleshooting_search_unified")
- [Why does Unified Search in
  the console and Resource Explorer sometimes give different results?](#troubleshooting_search_unified_different "#troubleshooting_search_unified_different")
- [What permissions do I need to be
  able to search for resources?](#troubleshooting_search_permissions "#troubleshooting_search_permissions")

## Why are some resources

missing from my Resource Explorer search results?

The following list provides reasons why some resources might not appear in your search
results as expected:

**Initial indexing isn't complete**

After you first access Resource Explorer, the service automatically enables search
capabilities [based on your IAM permissions](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md"). It can then take up to
36 hours for indexing and replication to the aggregator index to complete.
Try your search again later.

**The resource is new**

It can take a few minutes for a new resource to be discovered by Resource Explorer
and added to the local index. Try again in a few minutes.

**Information about a new resource in one Region hasn’t
yet been propagated to the aggregator index**

It can take some time for details about a new resource discovered in one
Region to be indexed in its own Region and then replicated to the aggregator
index for the account. The new resource can appear in cross-Region search
results only after replication is complete. Try your search again
later.

**The resource exists in a different Region, and the
searched Region doesn't contain the aggregator index**

You can search for resources across all Regions in the account only by
using a view in the Region that contains the aggregator index. Searches in
any other Region return resources from only the Region in which you perform
the search.

**Filters on the view exclude that
resource**

Every view can include filters in the configuration that restrict which
results can be included in search results made with that view. Ensure that
the resource you're looking for matches the filters in the view that you're
using to search. For more about filters, see [Filters](using-search-query-syntax.md#query-syntax-filters "using-search-query-syntax.md#query-syntax-filters").

**The resource type is not supported by
Resource Explorer**

Some resource types aren't supported by Resource Explorer. For more information, see
[Resource types you can search for with
Resource Explorer](supported-resource-types.md "supported-resource-types.md").

**User indexes aren't configured in the console
Region**

If a user index isn't configured in a Region, you will see partial results.
For more information, see [Understanding the immediate
resource discovery experience](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md").

**Your views don't include tags**

Tags are required by the Resource Explorer widget. If your views don't include tags,
the resources won't be included in your results. For more information, see
[Adding tags to views](configure-views-tag.md "configure-views-tag.md").

**Your search uses the wrong search query
syntax**

Search in Resource Explorer is unique to this service. Without the correct syntax,
you won't find the resources you expect. For more information, see [Search query syntax reference for Resource Explorer](using-search-query-syntax.md "using-search-query-syntax.md").

**You have recently tagged your
resources**

After you tag a resource, there may be a 30 second delay before the
resource appears in your search results.

**The resource type doesn't support tag
filters**

If tag filters aren't supported by the resource type, they won't display
in the Resource Explorer widget. Resource types that don't support tag filters
are:

- `cloudfront:cache-policy`
- `cloudfront:origin-access-identity`
- `cloudfront:function`
- `cloudfront:origin-request-policy`
- `cloudfront:realtime-log-config`
- `cloudfront:response-headers-policy`
- `cloudwatch:dashboard`
- `docdb:globalcluster`
- `elasticache:globalreplicationgroup`
- `iam:group`
- `lambda:code-signing-config`
- `lambda:event-source-mapping`
- `ssm:windowtarget`
- `ssm:windowtask`
- `rds:auto-backup`
- `rds:global-cluster`
- `s3:accesspoint`

## Why are some searches limited to 1,000

results?

If your query includes free-form text, the Resource Explorer console will use the
`Search` operation, but if your query does not include free-form text,
Resource Explorer uses the `ListResources` operation. `Search` operations are
limited to 1,000 results that are sorted by relevancy, while `ListResource`
operations have no upper limit and are not sorted by relevancy. To see resources beyond
1,000 results when using free-form text (and the `Search` operation), you
must use additional filters.

## Why are my resources not appearing in

Unified Search results in the console?

[Unified Search](../../../awsconsolehelpdocs/latest/gsg/using-search.md "../../../awsconsolehelpdocs/latest/gsg/using-search.md") results are available in the search bar at the top of every
AWS Management Console page when you have, at minimum, the permissions in the
`AWSResourceExplorerReadOnlyAccess` managed policy. If you don't have
access to resource results, obtain permission from your administrator or sign in with a
role that has this permission.

## Why does Unified Search in

the console and Resource Explorer sometimes give different results?

Unified Search results are available in the search bar at the top of every AWS Management Console
page. When you use Unified Search, the Unified Search process automatically inserts a
wildcard character (`*`) to the end of the first term that you type in the
query string. That wildcard character isn't visible in the Unified Search box, but it
does affect the results.

###### Important

Unified Search automatically inserts a wildcard character (`*`) operator at the
end of the first keyword in the string. This means that unified search results include resources
that match any string that starts with the specified keyword.

The search performed by the **Query** text box on the [Resource search](https://console.aws.amazon.com/resource-explorer/home#/explorer "https://console.aws.amazon.com/resource-explorer/home#/explorer") page in the
Resource Explorer console does **_not_**
automatically append a wildcard character. You can insert a `*` manually after
any term in the search string.

## What permissions do I need to be

able to search for resources?

To search, you must have permission to perform _both_
of the following operations on a view that resides in the Region in which you call the
operation:

- `resource-explorer-2:GetView`
- `resource-explorer-2:Search`
- `resource-explorer-2:ListResources`

This can be done by adding a statement similar to the following example to a policy
assigned to your IAM principal.

```
        {
            "Effect": "Allow",
            "Action": [
                "resource-explorer-2:GetView",
                "resource-explorer-2:Search"
            ],
            "Resource": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-View-Name/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111"
        }
```

You can replace the Amazon Resource Number (ARN) of a specific view with an ARN that
includes a wildcard (`*`) to grant permission to all matching views.

If you don't specify a view in your request, Resource Explorer automatically uses the [default
view](configure-views-set-default.md "configure-views-set-default.md") for the Region in which you made the request. If you
don't have permissions to use the default view, talk to your administrator.

###### Note

Even if you see a resource in the results of a Resource Explorer search query, you need
permissions on the resource itself to be able to interact with that resource.



# Pagination
<a name="acxd-common-types-pagination"></a>

## nextToken
<a name="acxd-common-types-pagination-nexttoken"></a>

Type: String

An opaque pagination token returned in list responses when more results are available. Pass it back in the next request to retrieve the next page. When there are no more pages, `nextToken` is `null` or absent.

## maxResults
<a name="acxd-common-types-pagination-maxresults"></a>

Type: Integer

The maximum number of items to return per page. Default and maximum vary by resource (typically 1–500).
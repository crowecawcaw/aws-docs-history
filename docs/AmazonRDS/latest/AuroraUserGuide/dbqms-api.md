# Database Query Metadata Service (DBQMS) API reference

The Database Query Metadata Service (`dbqms`) is an internal-only service. It provides your recent and
saved queries for the query editor on the AWS Management Console for multiple AWS services, including Amazon RDS.

###### Supported DBQMS actions

- [CreateFavoriteQuery](#CreateFavoriteQuery "#CreateFavoriteQuery")
- [CreateQueryHistory](#CreateQueryHistory "#CreateQueryHistory")
- [CreateTab](#CreateTab "#CreateTab")
- [DeleteFavoriteQueries](#DeleteFavoriteQueries "#DeleteFavoriteQueries")
- [DeleteQueryHistory](#DeleteQueryHistory "#DeleteQueryHistory")
- [DeleteTab](#DeleteTab "#DeleteTab")
- [DescribeFavoriteQueries](#DescribeFavoriteQueries "#DescribeFavoriteQueries")
- [DescribeQueryHistory](#DescribeQueryHistory "#DescribeQueryHistory")
- [DescribeTabs](#DescribeTabs "#DescribeTabs")
- [GetQueryString](#GetQueryString "#GetQueryString")
- [UpdateFavoriteQuery](#UpdateFavoriteQuery "#UpdateFavoriteQuery")
- [UpdateQueryHistory](#UpdateQueryHistory "#UpdateQueryHistory")
- [UpdateTab](#UpdateTab "#UpdateTab")

## CreateFavoriteQuery

Save a new favorite query. Each user can create up to 1000 saved queries. This limit is subject to change in the future.

## CreateQueryHistory

Save a new query history entry.

## CreateTab

Save a new query tab. Each user can create up to 10 query tabs.

## DeleteFavoriteQueries

Delete one or more saved queries.

## DeleteQueryHistory

Delete query history entries.

## DeleteTab

Delete query tab entries.

## DescribeFavoriteQueries

List saved queries created by a user in a given account.

## DescribeQueryHistory

List query history entries.

## DescribeTabs

List query tabs created by a user in a given account.

## GetQueryString

Retrieve full query text from a query ID.

## UpdateFavoriteQuery

Update the query string, description, name, or expiration date.

## UpdateQueryHistory

Update the status of query history.

## UpdateTab

Update the query tab name and query string.

# Identifying which Regions display full versus partial

resource results

AWS Resource Explorer provides different levels of search results depending on your permissions and
the type of index in each Region. All Regions have Resource Explorer-owned indexes that provide partial
results (all tagged resources and supported untagged resources created after the
[immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md") release. Accessing partial results requires that you have, at minimum,
the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy).
Regions with user-owned indexes provide complete search results. You can identify which type
of results you'll receive in each Region by checking the index types using the procedures on
this page.

The search results you receive depend on both your permissions and the index type:

- **Full results:** Available in Regions with
  user-owned indexes when you have, at minimum, the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy (and the
  service-linked role exists in the account)
- **Partial results:** Available in all Regions through
  Resource Explorer-owned indexes when you have, at minimum, the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy, or in
  Regions where user-owned indexes have been deleted

###### Important

Users can search for resources in all Regions, but the completeness of results varies
by index type. Regions with user-owned indexes provide complete search results and
replicate to the aggregator index for cross-Region search (when enabled). Regions with
only Resource Explorer-owned indexes provide partial results (all tagged resources and supported
untagged resources created after the [immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md") release) but are not included in
cross-Region search replication.

## Checking index types and result

completeness in Regions

You can check which Regions have user-owned indexes (providing full results) versus
Resource Explorer-owned indexes (providing partial results) by using the AWS Management Console, by using
commands in the AWS Command Line Interface (AWS CLI), or by using API operations in an AWS SDK. All
Regions have Resource Explorer-owned indexes by default, while user-owned indexes are created when
users with appropriate permissions complete setup in a Region.

AWS Management Console

###### To check index types and result completeness by Region

1. Open the **[Settings](https://console.aws.amazon.com/resource-explorer/home#/settings "https://console.aws.amazon.com/resource-explorer/home#/settings")** page in the Resource Explorer console.
2. The list in the **Indexes** section shows
   user-owned indexes that provide complete search results. The value
   in the **Type** column indicates whether the index
   is a **Local** index for its Region, or the
   **Aggregator** index for the AWS account.
   Regions not listed have only Resource Explorer-owned indexes, which provide
   partial results.
3. To see which Regions have only Resource Explorer-owned indexes (partial
   results), choose **Create indexes**. Available
   Regions in this list have only Resource Explorer-owned indexes and will provide
   partial search results until you create user-owned indexes for full
   results.

AWS CLI

###### To check index types and result completeness by Region

Run the following command to see which AWS Regions have user-owned
indexes (providing complete results). Regions not listed have only
Resource Explorer-owned indexes (providing partial results).

```
`$` `aws resource-explorer-2 list-indexes`
`{
 "Indexes": [
 {
 "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
 "Region": "us-east-1",
 "Type": "AGGREGATOR"
 },
 {
 "Arn": "arn:aws:resource-explorer-2:us-west-2:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd22222222",
 "Region":"us-west-2",
 "Type":"LOCAL"
 }
 ]
}`
```

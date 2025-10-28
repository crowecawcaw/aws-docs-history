AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Demoting the aggregator index to a local

index

You can demote an aggregator index to a local index, such as when you want to move the
aggregator index to a different AWS Region.

When you demote an aggregator index to a local index, Resource Explorer stops replicating the indexes
from other AWS Regions. It also starts an asynchronous background task to delete any
replicated information from other Regions. Until that asynchronous task completes, some
cross-Region results can continue to appear in search results.

###### Notes

- After you demote an aggregator index, you must wait 24 hours before
  you can promote either the same index or the index in a different Region to be
  the new aggregator index for the account.
- After demoting an aggregator index, it can take up to 36 hours for the
  background processes to complete and for all resource information from other
  Regions to disappear from results from searches performed in this Region.
- If you demote a member account within an organization wide view, the member
  may be removed from multi-account search.
  You can check the status of the background task by viewing the list of indexes on the
  **[Settings](https://console.aws.amazon.com/resource-explorer/home#/settings "https://console.aws.amazon.com/resource-explorer/home#/settings")** page or by using the [GetIndex](../apireference/API_GetIndex.md "../apireference/API_GetIndex.md") operation. When the
  asynchronous tasks complete, the `Status` field from the index changes from
  `UPDATING` to `ACTIVE`. At that time, only results from the local
  Region appear in query results.

AWS Management Console

###### To demote an aggregator index to a local index

1. Open the Resource Explorer **[Settings](https://console.aws.amazon.com/resource-explorer/home#/settings "https://console.aws.amazon.com/resource-explorer/home#/settings")** page.
2. In the **Indexes** section, select the check box next
   to the Region that contains the aggregator index that you want to demote to
   a local index, and then choose **Change index
   type**.
3. In the **Change index type for <_Region name_>** dialog, choose
   **Local index**, and then choose **Save
   changes**.

AWS CLI

###### To demote an aggregator index to a local index

The following example demotes the specified aggregator index to a local
index. You must call the operation in the AWS Region that currently
contains the aggregator index.

```
`$` `aws resource-explorer-2 update-index-type \
 --arn arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111 \
 --type LOCAL \
 --region us-east-1``{
 "Arn":"arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
 "LastUpdatedAt":"2022-07-13T18:41:58.799Z",
 "State":"UPDATING",
 "Type":"LOCAL"
}`
```

The operation works asynchronously and starts with `State` set to
`UPDATING`. To check if the operation has completed, you can run
the following command and look for the value `ACTIVE` in the
`State` response field. You must run this command in the Region
the contains the index you want to check.

```
`$` `aws resource-explorer-2 get-index --region us-east-1``{
 "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
 "CreatedAt": "2022-10-12T21:31:37.277000+00:00",
 "LastUpdatedAt": "2022-10-12T21:31:37.677000+00:00",
 "ReplicatingFrom": [
 "us-west-2",
 "us-east-2",
 "us-west-1"
 ],
 "State": "ACTIVE",
 "Tags": {},
 "Type": "LOCAL"
}`
```

# Promoting a local index to be the

aggregator index for the account

For cross-region search functionality, Resource Explorer provides a streamlined banner workflow that
allows you to enable cross-region search with a single click. If you see a
**Complete setup and enable cross-Region search** banner, you can
choose **Enable cross-Region search in all Regions** for automatic setup or
**Customize Region setup** for granular control. Alternatively, you
have the option to manually create an aggregator index in one AWS Region by promoting an
existing user-owned (local) index from the **Settings** page . This
procedure describes the manual process for promoting a user-owned (local) index to be the
aggregator index for the account.

###### Important

- You can have only one aggregator index in an AWS account. If the account already
  has an aggregator index, you must first either [demote it to a local
  index](manage-aggregator-region-turn-off.md "manage-aggregator-region-turn-off.md") or delete it.
- After deleting or changing which Region contains the aggregator index, you must
  wait 24 hours before you can promote another index to be the
  aggregator index.

AWS Management Console

###### To promote a user-owned (local) index to be the aggregator index for the

account

1. **Primary method - Banner workflow:** If
   you see a **Complete setup and enable cross-Region
   search** banner or banner notification, you can use the
   guided workflow:
   1. For automatic setup across all regions, choose
      **Enable cross-Region search in all
      Regions**, or
   2. For customized configuration, choose **Customize
      Region setup** to access granular setup
      options.

2. **Alternative method:** The
   **Settings** page.
   1. Open the Resource Explorer **[Settings](https://console.aws.amazon.com/resource-explorer/home#/settings "https://console.aws.amazon.com/resource-explorer/home#/settings")** page.
   2. In the **Indexes** section, select the check
      box next to the index that you want to promote, and then choose
      **Change index type**.
   3. In the **Change index type for <_Region name_>** dialog,
      choose **aggregator index**, and then choose
      **Save changes**.

AWS CLI

###### To promote a user-owned (local) index to be the aggregator index for the

account

The following example command updates the index in the specified
AWS Region from type `LOCAL` to type `AGGREGATOR`.
You must call the operation from the AWS Region that you want to contain
the aggregator index. For information about the banner workflow option, see the
Console tab above.

```
`$` `aws resource-explorer-2 update-index-type \
 --arn arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111 \
 --type AGGREGATOR \
 --region us-east-1``{
 "Arn":"arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
 "LastUpdatedAt":"2022-07-13T18:41:58.799Z",
 "State":"UPDATING",
 "Type":"AGGREGATOR"
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
 "Type": "AGGREGATOR"
}`
```

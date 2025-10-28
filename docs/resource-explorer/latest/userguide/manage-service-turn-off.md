AWS Resource Explorer now provides immediate access to resource search and
discovery capabilities in a Region. With this launch, you no longer need to activate
Resource Explorer to discover your resources. [Learn more](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md")

# Turning off Resource Explorer

When you no longer need to search for resources in a specific AWS Region, you can turn
off AWS Resource Explorer in only that Region by deleting its index, or you can delete Resource Explorer in all
AWS Regions. When you do this, Resource Explorer stops scanning for new or updated resources in that
Region. If your account contains an aggregator index, then replication from the deleted index
stops, and the information from the deleted index is removed from the aggregator index and stops
appearing in search results. It can take up to 24 hours for all resources from the
deleted index to disappear from search results in the Region with the aggregator index.

###### Note

When you register the first AWS Region, Resource Explorer creates [a service linked role (SLR) named
AWSServiceRoleForResourceExplorer](security_iam_service-linked-roles.md#slr-permissions "security_iam_service-linked-roles.md#slr-permissions") in the AWS account. Resource Explorer **_doesn't_** delete this SLR automatically. After
you delete the Resource Explorer index in every Region in the account, you can use the IAM
console to delete the SLR if you won't use Resource Explorer in the future. If you do delete the
role and you then choose to turn on Resource Explorer again in at least one AWS Region, Resource Explorer
re-creates the service-linked role automatically.

## Turning off Resource Explorer in one

AWS Region

You can turn off Resource Explorer in an AWS Region by using the AWS Management Console, by using commands
in the AWS Command Line Interface (AWS CLI), or by using API operations in an AWS SDK.

If you turn off Resource Explorer for a member account, and the member is in an organization wide
view, it will be removed from the multi-account search results.

If your account includes a managed view (a view managed by an AWS service), the
managed view must be deleted before you can turn off Resource Explorer. Review [AWS managed views](aws-managed-views.md "aws-managed-views.md") for instructions on removing a managed view from your
account and prompting the managing service to delete the view.

If you no longer want to support searching for resources in one or more of the
AWS Regions in your account, perform the steps in the following procedure.

###### Note

If the index you delete is the aggregator index for the AWS account, you must
wait 24 hours before you can promote another local index to be the
aggregator index for the account. Users can't perform account-wide searches using
Resource Explorer until another aggregator index is configured.

AWS Management Console

###### To delete the Resource Explorer index in an AWS Region

1. Open the Resource Explorer **[Settings](https://console.aws.amazon.com/resource-explorer/home#/settings "https://console.aws.amazon.com/resource-explorer/home#/settings")** page.
2. In the **Indexes** section, select the check
   boxes next to the AWS Regions with the indexes that you want to
   delete, and then choose **Delete**.
3. On the **Delete indexes** page, verify that you
   selected only indexes that you want to delete. Type
   `delete` in the
   **Confirm** text box, and then choose
   **Delete indexes**.

Resource Explorer displays a green banner at the top of the page to indicate
success, or a red banner if there is an error with one or more of
the selected Regions.

AWS CLI

###### To delete the Resource Explorer index in an AWS Region

If you no longer want to support searching for resources in one or
more of the AWS Regions in your account, run the following
commands.

Run the following command for each Region with the indexes that you want
to delete. You must run the command in the Region with the index you want to
delete. The following example command deletes the Resource Explorer index in the
US West (Oregon) (`us-west-2`).

```
`$` `aws resource-explorer-2 delete-index \
 --arn arn:aws:resource-explorer-2:us-west-2:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd22222222 \
 --region us-west-2``{
 "Arn": "arn:aws:resource-explorer-2:us-west-2:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd22222222",
 "State": "DELETING"
}`
```

Because Resource Explorer performs some of the deletion cleanup work as asynchronous
tasks in the background, the response might indicate that the operation is
`DELETING`. This status indicates that the background
processes are not yet complete. You can check for final completion by
running the following command, and checking for the `State` to
change to `DELETED`.

```
`$` `aws resource-explorer-2 get-index \
 --region us-west-2``{
 "Arn": "arn:aws:resource-explorer-2:us-west-2:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
 "CreatedAt": "2022-07-12T18:59:10.503000+00:00",
 "LastUpdatedAt": "2022-07-13T18:41:58.799000+00:00",
 "ReplicatingFrom": [],
 "State": "DELETED",
 "Tags": {},
 "Type": "LOCAL"
}`
```

## Turning off Resource Explorer in all

AWS Regions

If you want to turn off AWS Resource Explorer completely, perform the following procedure.

###### Note

Resource Explorer creates a service linked role named AWSServiceRoleForResourceExplorer in the account when you
create an index in the first AWS Region for an account. Resource Explorer _does
not_ automatically delete this service linked role. After you delete
the Resource Explorer index in every Region, you can then use the IAM console to delete the
role if you're sure you won't be using Resource Explorer again in the future. If you do delete
the role and you then choose to start Resource Explorer in at least one AWS Region, Resource Explorer
recreates the service-linked role.

If your account includes a managed view (a view managed by an AWS service), the
managed view must be deleted before you can turn off Resource Explorer. Review [AWS managed views](aws-managed-views.md "aws-managed-views.md") for instructions on removing a managed view from your
account and prompting the managing service to delete the view.

You can turn off Resource Explorer by using the AWS Management Console, by using commands in the AWS Command Line Interface
(AWS CLI), or by using API operations in an AWS SDK.

AWS Management Console
If you no longer want to support searching for resources in any
AWS Region in your AWS account, perform the steps in the following
procedure.

###### To turn off Resource Explorer in all AWS Regions

1. Open the Resource Explorer **[Settings](https://console.aws.amazon.com/resource-explorer/home#/settings "https://console.aws.amazon.com/resource-explorer/home#/settings")** page.
2. In the **Indexes** section, select the check
   boxes next to all registered AWS Regions, and then choose
   **Delete**.

###### Tip

You can check the box in the table header row next to
**Index** to check the boxes for all
Regions in a single step. 3. On the **Delete indexes** page, verify that you
want to delete all indexes. Type `delete` in
the **Confirm** text box, and then choose
**Delete indexes**.

Resource Explorer displays a green banner at the top of the page to indicate
success, or a red banner if there is an error with one or more of
the selected Regions.

AWS CLI

###### To turn off Resource Explorer in all AWS Regions

If you no longer want to support searching for resources in any
AWS Regions in your account, run the following command to find the ARN
of every index in each AWS Region in which you previously turned on
Resource Explorer.

```
`$` `aws resource-explorer-2 list-indexes --query Indexes[*].Arn``[
"arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
"arn:aws:resource-explorer-2:us-west-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd22222222",
"arn:aws:resource-explorer-2:us-west-2:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd33333333"
]`
```

For each response, run the following command to delete the Resource Explorer index in
that Region.

```
`$` `aws resource-explorer-2 delete-index \
 --arn arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111 \
 --region us-east-1``{
 "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
 "State": "DELETING"
}`
```

Repeat the previous command in each additional Region.

Because Resource Explorer performs some of the cleanup as asynchronous tasks in the
background, the response might indicate that the operation is
`DELETING`. This status indicates that the background
processes are not yet complete. You can check for final completion by
running the following command, and checking for the status to change to
`DELETED`.

```
$ aws resource-explorer-2 get-index \
    --region us-east-1
{
    "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111",
    "CreatedAt": "2022-07-12T18:59:10.503000+00:00",
    "LastUpdatedAt": "2022-07-13T18:41:58.799000+00:00",
    "ReplicatingFrom": [],
    "State": "DELETED",
    "Tags": {},
    "Type": "LOCAL"
}
```



# Disable Lake query federation
<a name="query-disable-federation"></a>

**Note**  
AWS CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](cloudtrail-lake-service-availability-change.md).

You can disable federation by using the CloudTrail console, AWS CLI, or [DisableFederation](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DisableFederation.html) API operation. When you disable federation, CloudTrail disables the integration with AWS Glue, AWS Lake Formation, and Amazon Athena. After disabling Lake query federation, you can no longer query your event data in Athena. No CloudTrail Lake data is deleted when you disable federation and you can continue to run queries in CloudTrail Lake.

This section describes how to disable federation using the CloudTrail console and AWS CLI.

------
#### [ CloudTrail console ]

The following procedure shows you how to disable Lake query federation on an existing event data store.

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1. In the navigation pane, under **Lake**, choose **Event data stores**.

1. Choose the event data store that you want to update. This opens the event data store's details page.

1. In **Lake query federation**, choose **Edit** and then choose **Disable**.

1. Choose **Save changes**. The **Federation status** changes to `Disabled`.

------
#### [ AWS CLI ]

To disable federation on the event data store, run the **aws cloudtrail disable-federation** command. The event data store is specified by `--event-data-store`, which accepts an event data store ARN or the ID suffix of the ARN.

```
aws cloudtrail disable-federation
--event-data-store arn:aws:cloudtrail:{{region}}:{{account-id}}:eventdatastore/{{eds-id}}
```

**Note**  
If this is an organization event data store, use the account ID for the management account.

------
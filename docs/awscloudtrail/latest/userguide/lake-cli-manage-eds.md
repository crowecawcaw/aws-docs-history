# Managing event data stores with the AWS CLI

This section describes several other commands that you can run to get information about your event data stores,
start and stop ingestion on an event data store, and enable and disable [federation](query-federation.md "query-federation.md") on an event data store.

###### Topics

- [Get an event data store with the AWS CLI](#lake-cli-get-eds "#lake-cli-get-eds")
- [List all event data stores in an account with the AWS CLI](#lake-cli-list-eds "#lake-cli-list-eds")
- [Add resource tag keys and IAM global conditions keys, and expand event size](#lake-cli-put-event-configuration "#lake-cli-put-event-configuration")
- [Get the event configuration for an event data store](#lake-cli-get-event-configuration "#lake-cli-get-event-configuration")
- [Get the resource-based policy for
  an event data store with the AWS CLI](#lake-cli-get-resource-policy "#lake-cli-get-resource-policy")
- [Attach a resource-based policy to
  an event data store with the AWS CLI](#lake-cli-put-resource-policy "#lake-cli-put-resource-policy")
- [Delete the resource-based policy attached to
  an event data store with the AWS CLI](#lake-cli-delete-resource-policy "#lake-cli-delete-resource-policy")
- [Stop ingestion on an event data store with the AWS CLI](#lake-cli-stop-ingestion-eds "#lake-cli-stop-ingestion-eds")
- [Start ingestion on an event data store with the AWS CLI](#lake-cli-start-ingestion-eds "#lake-cli-start-ingestion-eds")
- [Enable federation on an event data store](#lake-cli-enable-federation-eds "#lake-cli-enable-federation-eds")
- [Disable federation on an event data store](#lake-cli-disable-federation-eds "#lake-cli-disable-federation-eds")
- [Restore an event data store with the AWS CLI](#lake-cli-restore-eds "#lake-cli-restore-eds")

## Get an event data store with the AWS CLI

The following example AWS CLI **get-event-data-store** command returns information about the event data store
specified by the required `--event-data-store` parameter, which accepts
an ARN or the ID suffix of the ARN.

```
aws cloudtrail get-event-data-store \
--event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE
```

The following is an example response. Creation and last updated times are in
`timestamp` format.

```
{
    "EventDataStoreARN": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE",
    "Name": "s3-data-events-eds",
    "Status": "ENABLED",
    "AdvancedEventSelectors": [
        {
            "Name": "Log DeleteObject API calls for a specific S3 bucket",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Data"
                    ]
                },
                {
                    "Field": "eventName",
                    "Equals": [
                        "DeleteObject"
                    ]
                },
                {
                    "Field": "resources.ARN",
                    "StartsWith": [
                        "arn:aws:s3:::`amzn-s3-demo-bucket`"
                    ]
                },
                {
                    "Field": "readOnly",
                    "Equals": [
                        "false"
                    ]
                },
                {
                    "Field": "resources.type",
                    "Equals": [
                        "AWS::S3::Object"
                    ]
                }
            ]
        }
    ],
    "MultiRegionEnabled": true,
    "OrganizationEnabled": false,
    "BillingMode": "FIXED_RETENTION_PRICING",
    "RetentionPeriod": 2557,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-11-09T22:20:36.344000+00:00",
    "UpdatedTimestamp": "2023-11-09T22:20:36.476000+00:00"
}
```

## List all event data stores in an account with the AWS CLI

The following example AWS CLI **list-event-data-stores** command returns information about all event data
stores in an account, in the current Region. Optional parameters include
`--max-results`, to specify a maximum number of results that you want
the command to return on a single page. If there are more results than your
specified `--max-results` value, run the command again adding the
returned `NextToken` value to get the next page of results.

```
aws cloudtrail list-event-data-stores
```

The following is an example response.

```
{
    "EventDataStores": [
        {
            "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE7-cad6-4357-a84b-318f9868e969",
            "Name": "management-events-eds"
        },
        {
            "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE6-88e1-43b7-b066-9c046b4fd47a",
            "Name": "config-items-eds"
        },
        {
            "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLEf-b314-4c85-964e-3e43b1e8c3b4",
            "Name": "s3-data-events"
        }
    ]
}
```

## Add resource tag keys and IAM global conditions keys, and expand event size

Run the AWS CLI `put-event-configuration` command to expand the maximum event
size and add up to 50 resource tag keys and 50 IAM global condition keys to
provide additional metadata about your events.

The `put-event-configuration` command accepts the following arguments:

- `--event-data-store` – Specify the ARN of
  the event data store or the ID suffix of the ARN. This parameter is required.
- `--max-event-size` – Set to `Large` to set the maximum
  event size to 1 MB. By default, the value is `Standard`,
  which specifies a maximum event size of 256 KB.

###### Note

In order to add resource tag keys or IAM global conditions keys, you must
set the event size to `Large` to
ensure all of your added keys are included in the event.

- `--context-key-selectors` – Specify the type of keys
  you want included in the events collected by your event data store. You can include resource tag
  keys and IAM global condition keys. Information about the added resource tags and IAM global condition keys is shown in the `eventContext`
  field in the event. For more information, see [Enrich CloudTrail events by adding resource tag
  keys and IAM global condition keys](cloudtrail-context-events.md "cloudtrail-context-events.md").
  - Set the `Type` to `TagContext` to pass in an array of up to 50 resource tag keys. If you add resource tags,
    CloudTrail events will include the selected tag keys associated with the resources that were involved in the API call.
    API events related to deleted resources will not have resource tags.
  - Set the `Type` to `RequestContext` to pass in an array of up to 50 IAM global condition keys. If you add IAM global condition keys,
    CloudTrail events will include information about the selected condition keys that were evaluated during the authorization process,
    including additional details about the principal, session, network, and the request itself.

The following example sets the maximum event size to `Large` and adds two
resource tag keys `myTagKey1` and `myTagKey2`.

```
aws cloudtrail put-event-configuration \
--event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE \
--max-event-size Large \
--context-key-selectors '[{"Type":"TagContext", "Equals":["myTagKey1","myTagKey2"]}]'
```

The next example sets the maximum event size to `Large` and adds an IAM;
global condition key (`aws:MultiFactorAuthAge`).

```
aws cloudtrail put-event-configuration \
--event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE \
--max-event-size Large \
--context-key-selectors '[{"Type":"RequestContext", "Equals":["aws:MultiFactorAuthAge"]}]'
```

The final example removes all resource tag keys and IAM global condition keys
and sets the maximum event size to `Standard`.

```
aws cloudtrail put-event-configuration \
--event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE \
--max-event-size Standard \
--context-key-selectors
```

## Get the event configuration for an event data store

Run the AWS CLI `get-event-configuration` command
to return the event configuration for an event data store that collects CloudTrail events. This command returns the maximum event size
and lists the resource tag keys and IAM global condition keys (if any) that are included in CloudTrail events.

```
aws cloudtrail get-event-configuration \
--event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE
```

## Get the resource-based policy for

an event data store with the AWS CLI

The following example runs the `get-resource-policy` command on an organization event data store.

```
aws cloudtrail get-resource-policy --resource-arn arn:aws:cloudtrail:us-east-1:888888888888:eventdatastore/example6-d493-4914-9182-e52a7934b207
```

Because the command was run on an organization event data store, the output will show both the provided resource-based policy and the [DelegatedAdminResourcePolicy](cloudtrail-lake-organizations.md#cloudtrail-lake-organizations-eds-rbp "cloudtrail-lake-organizations.md#cloudtrail-lake-organizations-eds-rbp") generated
for the delegated administrator accounts.

## Attach a resource-based policy to

an event data store with the AWS CLI

To run queries on a dashboard during a manual or scheduled refresh, you need to attach a resource-based policy to
every event data store that is associated with a widget on the dashboard.
This allows CloudTrail Lake to run the queries on your behalf. For more information about the resource-based policy, see
[Example:
Allow CloudTrail to run queries to refresh a dashboard](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds-dashboard").

The following example attaches a resource-based policy to an event data store
that allows CloudTrail to run queries on a dashboard when the dashboard is refreshed. The
policy is created in a separate file, `policy.json`, with
the following example policy statement:

JSON

```
`{ "Version":"2012-10-17", "Statement": [{ "Sid": "EDSPolicy", "Effect":
 "Allow", "Principal": { "Service": "cloudtrail.amazonaws.com" }, "Resource":
 "`arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/event_data_store_ID`",
 "Action": "cloudtrail:StartQuery", "Condition": { "StringEquals": { "AWS:SourceArn":
 "`arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`",
 "AWS:SourceAccount": "`123456789012`" } } } ] }`

```

Replace `123456789012` with your account ID,
`arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/event_data_store_ID`
with the ARN of the event data store for which CloudTrail will run queries, and
`arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`
with the ARN of the dashboard.

```
aws cloudtrail put-resource-policy \
--resource-arn `eds-arn` \
--resource-policy file://`policy.json`
```

The following is the example response.

```
{ "ResourceArn": "arn:aws:cloudtrail:`us-east-1`:`123456789012`:eventdatastore/`EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`", "ResourcePolicy": "`policy-statement`" }
```

For additional policy examples, see [Resource-based policy examples for event data stores](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds "security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-eds").

## Delete the resource-based policy attached to

an event data store with the AWS CLI

The following examples deletes the resource-based policy attached to an event data store. Replace `eds-arn` with the ARN of the event data store.

```
aws cloudtrail delete-resource-policy --resource-arn `eds-arn`
```

This command produces no output if it's successful.

## Stop ingestion on an event data store with the AWS CLI

The following example AWS CLI **stop-event-data-store-ingestion** command stops an event data store from ingesting events.
To stop ingestion, the event data store `Status` must be `ENABLED`
and the `eventCategory` must be `Management`, `Data`, or `ConfigurationItem`.
The event data store is specified by `--event-data-store`, which accepts an event data store ARN, or the
ID suffix of the ARN. After you run **stop-event-data-store-ingestion**, the
state of the event data store changes to `STOPPED_INGESTION`.

The event data store does count towards your account maximum of ten
event data stores when its state is `STOPPED_INGESTION`.

```
aws cloudtrail stop-event-data-store-ingestion \
--event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE
```

There is no response if the operation is successful.

## Start ingestion on an event data store with the AWS CLI

The following example AWS CLI **start-event-data-store-ingestion** command starts event ingestion on an event data store.
To start ingestion, the event data store `Status` must be `STOPPED_INGESTION`
and the `eventCategory` must be `Management`, `Data`, or `ConfigurationItem`.
The event data store is specified by `--event-data-store`, which accepts an event data store ARN, or the
ID suffix of the ARN. After you run **start-event-data-store-ingestion**, the
state of the event data store changes to `ENABLED`.

```
aws cloudtrail start-event-data-store-ingestion --event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE
```

There is no response if the operation is successful.

## Enable federation on an event data store

To enable federation, run the **aws cloudtrail enable-federation**
command, providing the required `--event-data-store` and `--role`
parameters. For `--event-data-store`, provide the event data store ARN (or
the ID suffix of the ARN). For `--role`, provide the ARN for your federation
role. The role must exist in your account and provide the [required minimum
permissions](query-federation.md#query-federation-permissions-role "query-federation.md#query-federation-permissions-role").

```
aws cloudtrail enable-federation \
--event-data-store arn:aws:cloudtrail:`region`:`account-id`:eventdatastore/`eds-id`
--role arn:aws:iam::`account-id`:role/`federation-role-name`
```

This example shows how a delegated administrator can enable
federation on an organization event data store by specifying the ARN
of the event data store in the management account and the ARN of the
federation role in the delegated administrator account.

```
aws cloudtrail enable-federation \
--event-data-store arn:aws:cloudtrail:`region`:`management-account-id`:eventdatastore/`eds-id`
--role arn:aws:iam::`delegated-administrator-account-id`:role/`federation-role-name`
```

## Disable federation on an event data store

To disable federation on the event data store, run the **aws
cloudtrail disable-federation** command. The event data
store is specified by `--event-data-store`, which accepts
an event data store ARN or the ID suffix of the ARN.

```
aws cloudtrail disable-federation \
--event-data-store arn:aws:cloudtrail:`region`:`account-id`:eventdatastore/`eds-id`
```

###### Note

If this is an organization event data store, use the account ID
for the management account.

## Restore an event data store with the AWS CLI

The following example AWS CLI **restore-event-data-store** command restores an event data store that is pending
deletion. The event data store is specified by `--event-data-store`,
which accepts an event data store ARN or the ID suffix of the ARN. You can only
restore a deleted event data store within the seven-day wait period after
deletion.

```
aws cloudtrail restore-event-data-store \
--event-data-store EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE
```

The response includes information about the event data store, including its ARN,
advanced event selectors, and the status of restoration.

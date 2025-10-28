# Delete an event data store with the AWS CLI

This section demonstrates how to delete an event data store by running the AWS CLI `delete-event-data-store` command

To delete an event data store, specify the `--event-data-store` by providing the event data store ARN, or the
ID suffix of the ARN. After you run **delete-event-data-store**, the
final state of the event data store is `PENDING_DELETION`, and the event
data store is automatically deleted after a wait period of 7 days.

After you run **delete-event-data-store** on an event data store,
you cannot run **list-queries**, **describe-query**,
or **get-query-results** on queries that are using the disabled data
store. The event data store does count towards your account maximum of ten
event data stores in an AWS Region when it is pending deletion.

###### Note

You can't delete an event data store if `--termination-protection-enabled`
is set or its `FederationStatus` is `ENABLED`.

To delete an event data store with an `eventCategory` of `ActivityAuditLog`, you must first delete the integration's channel.
You can delete the channel by using the `aws cloudtrail delete-channel` command. For more information, see
[Delete a channel to delete an integration with the AWS CLI](lake-cli-delete-integration.md "lake-cli-delete-integration.md").

```
aws cloudtrail delete-event-data-store \
--event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE
```

There is no response if the operation is successful.

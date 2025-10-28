# Update a channel with the AWS CLI

This section describes how you can use the AWS CLI to update a channel for a CloudTrail Lake integration.
You can run the `update-channel` command to update the name of the channel
or to specify a different destination event data store. You cannot update the source of a channel.

When you run the command, the `--channel` parameter
is required.

The following is an
example that demonstrates how to update the channel name and destination.

```
aws cloudtrail update-channel \
--channel aws:cloudtrail:us-east-1:123456789012:channel/EXAMPLE8-0558-4f7e-a06a-43969EXAMPLE \
--name "new-channel-name" \
--destinations '[{"Type": "EVENT_DATA_STORE", "Location": "EXAMPLEf852-4e8f-8bd1-bcf6cEXAMPLE"}, {"Type": "EVENT_DATA_STORE", "Location": "EXAMPLEg922-5n2l-3vz1- apqw8EXAMPLE"}]'
```

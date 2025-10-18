# Create an integration to log events from outside AWS with the AWS CLI

This section describes how you can use the AWS CLI to create a CloudTrail Lake integration to log events from outside of AWS.

In the AWS CLI, you create an integration in four commands (three if you already have an event data store that meets the
 criteria). Event data stores that you use as the destinations for an integration
 must be for a single Region and single account; they cannot be multi-region, they
 cannot log events for organizations in AWS Organizations, and they can only include activity events. 
 The event type in the console must be **Events from
 integrations**. In the API, the `eventCategory`
 value must be `ActivityAuditLog`. For more information
 about integrations, see [Create an integration with an event
 source outside of AWS](query-event-data-store-integration.md "query-event-data-store-integration.md").

1. Run [**create-event-data-store**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html") to create an
 event data store, if you do not already have one or more event data stores
 that you can use for the integration.


The following example AWS CLI command creates an event data store that logs
 events from outside AWS. For activity events, the
 `eventCategory` field selector value is
 `ActivityAuditLog`. The event data store has a retention
 period of 90 days set. By default, the event data store collects events from
 all Regions, but because this is collecting non-AWS events, set it to a
 single Region by adding the `--no-multi-region-enabled` option.
 Termination protection is enabled by default, and the event data store does
 not collect events for accounts in an organization.



```
aws cloudtrail create-event-data-store \
--name my-event-data-store \
--no-multi-region-enabled \
--retention-period 90 \
--advanced-event-selectors '[
    {
      "Name": "Select all external events",
      "FieldSelectors": [
          { "Field": "eventCategory", "Equals": ["ActivityAuditLog"] }
        ]
    }
  ]'
```

The following is an example response.



```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLEf852-4e8f-8bd1-bcf6cEXAMPLE",
    "Name": "my-event-data-store",
    "AdvancedEventSelectors": [
        {
           "Name": "Select all external events",
           "FieldSelectors": [
              {
                  "Field": "eventCategory",
                  "Equals": [
                      "ActivityAuditLog"
                    ]
                }
            ]
        }
    ],
    "MultiRegionEnabled": true,
    "OrganizationEnabled": false,
    "BillingMode": "EXTENDABLE_RETENTION_PRICING",
    "RetentionPeriod": 90,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-10-27T10:55:55.384000-04:00",
    "UpdatedTimestamp": "2023-10-27T10:57:05.549000-04:00"
}
```

You'll need the event data store ID (the suffix of the ARN, or
 `EXAMPLEf852-4e8f-8bd1-bcf6cEXAMPLE` in the preceding
 response example) to go on to the next step and create your channel.
2. Run the [**create-channel**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-channel.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-channel.html") command to create a
 channel that allows a partner or source application to send events to an
 event data store in CloudTrail.


A channel has the following components:




**Source**

CloudTrail uses this information to determine the partners that are
 sending event data to CloudTrail on your behalf. A source is required,
 and can be either `Custom` for all valid non-AWS
 events, or the name of a partner event source. A maximum of one
 channel is allowed per source.


For information about the `Source` values for available partners, see [Additional information about integration partners](query-event-data-store-integration.md#cloudtrail-lake-partner-information "query-event-data-store-integration.md#cloudtrail-lake-partner-information").



**Ingestion status**

The channel status shows when the last events were received
 from a channel source.



**Destinations**

The destinations are the CloudTrail Lake event data stores that are
 receiving events from the channel. You can change destination
 event data stores for a channel.




To stop receiving events from a source, delete the channel.


You need the ID of at least one destination event data store to run this
 command. The valid type of destination is `EVENT_DATA_STORE`. You
 can send ingested events to more than one event data store. The following
 example command creates a channel that sends events to two event data
 stores, represented by their IDs in the `Location` attribute of
 the `--destinations` parameter. The `--destinations`,
 `--name`, and `--source` parameters are required.
 To ingest events from a CloudTrail partner, specify the name of the partner as the
 value of `--source`. To ingest events from your own applications
 outside AWS, specify `Custom` as the value of
 `--source`.



```
aws cloudtrail create-channel \
    --region us-east-1 \
    --destinations '[{"Type": "EVENT_DATA_STORE", "Location": "EXAMPLEf852-4e8f-8bd1-bcf6cEXAMPLE"}, {"Type": "EVENT_DATA_STORE", "Location": "EXAMPLEg922-5n2l-3vz1- apqw8EXAMPLE"}]'
    --name my-partner-channel \
    --source $partnerSourceName \
```

In the response to your **create-channel** command, copy
 the ARN of the new channel. You need the ARN to run
 the `put-resource-policy` and `put-audit-events` commands in the next steps.
3. Run the **put-resource-policy** command to attach a resource policy to the channel. 
 Resource policies are JSON policy documents that specify what actions a specified principal can perform on the resource and
 under what conditions. The accounts defined as principals in the channel's resource
 policy can call the `PutAuditEvents` API to deliver events. 
 


###### Note

If you do not create a resource policy for the channel, only the channel owner can call the `PutAuditEvents` API on the channel.


The information required for the policy is determined by the integration
 type.




	* For a direction integration, CloudTrail requires the policy to contain
	 the partner's AWS account IDs, and requires you to enter the
	 unique external ID provided by the partner. CloudTrail automatically adds
	 the partner's AWS account IDs to the resource policy when you
	 create an integration using the CloudTrail console. Refer to the [partner's documentation](query-event-data-store-integration.md#cloudtrail-lake-partner-information#lake-integration-partner-documentation "query-event-data-store-integration.md#cloudtrail-lake-partner-information#lake-integration-partner-documentation")
	 to learn how to get the AWS account numbers required for the policy.
	* For a solution integration, you 
	 must specify at least one AWS account ID as principal, and can optionally enter an external ID to prevent against confused deputy.
The following are requirements for the resource policy:




	* The resource ARN defined in the policy must match the channel ARN the policy is attached to.
	* The policy contains only one action: cloudtrail-data:PutAuditEvents
	* The policy contains at least one statement. The policy can have a maximum of 20
	 statements.
	* Each statement contains at least one principal. A statement can have a maximum of 50 principals.

```
aws cloudtrail put-resource-policy \
    --resource-arn "channelARN" \
    --policy "{
    "Version": "2012-10-17",		 	 	 
    "Statement":
    [
        {
            "Sid": "ChannelPolicy",
            "Effect": "Allow",
            "Principal":
            {
                "AWS":
                [
                    "arn:aws:iam::111122223333:root",
                    "arn:aws:iam::444455556666:root",
                    "arn:aws:iam::123456789012:root"
                ]
            },
            "Action": "cloudtrail-data:PutAuditEvents",
            "Resource": "arn:aws:cloudtrail:us-east-1:777788889999:channel/EXAMPLE-80b5-40a7-ae65-6e099392355b",
            "Condition":
            {
                "StringEquals":
                {
                    "cloudtrail:ExternalId": "UniqueExternalIDFromPartner"
                }
            }
        }
    ]
}"
                    
```

For more information about resource policies, see [AWS CloudTrail resource-based policy examples](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md").
4. Run the [`PutAuditEvents`](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_PutAuditEvents.html "https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_PutAuditEvents.html") API to ingest
 your activity events into CloudTrail. You'll need the payload of events that
 you want CloudTrail to add. Be sure that there is no sensitive or
 personally-identifying information in event payload before ingesting it into
 CloudTrail. Note that the `PutAuditEvents` API uses the
 `cloudtrail-data` CLI endpoint, not the
 `cloudtrail` endpoint.


The following examples show how to use the
 **put-audit-events** CLI command. The
 **--audit-events** and **--channel-arn**
 parameters are required. The **--external-id** parameter 
 is required if an external ID is defined in the resource policy. You 
 need the ARN of the channel that you created in
 the preceding step. The value of **--audit-events** is a JSON
 array of event objects. `--audit-events` includes a required ID
 from the event, the required payload of the event as the value of
 `EventData`, and an [optional checksum](#lake-cli-integration-checksum.title "#lake-cli-integration-checksum.title")
 to help validate the integrity of the event after ingestion into
 CloudTrail.



```
aws cloudtrail-data put-audit-events \
--channel-arn $ChannelArn \
--external-id $UniqueExternalIDFromPartner \
--audit-events \
id="event_ID",eventData='"{event_payload}"' \
id="event_ID",eventData='"{event_payload}"',eventDataChecksum="optional_checksum"
```

The following is an example command with two event examples.



```
aws cloudtrail-data put-audit-events \
--channel-arn arn:aws:cloudtrail:us-east-1:123456789012:channel/EXAMPLE8-0558-4f7e-a06a-43969EXAMPLE \
--external-id UniqueExternalIDFromPartner \
--audit-events \
id="EXAMPLE3-0f1f-4a85-9664-d50a3EXAMPLE",eventData='"{\"eventVersion\":\0.01\",\"eventSource\":\"custom1.domain.com\", ...
\}"' \
id="EXAMPLE7-a999-486d-b241-b33a1EXAMPLE",eventData='"{\"eventVersion\":\0.02\",\"eventSource\":\"custom2.domain.com\", ...
\}"',eventDataChecksum="EXAMPLE6e7dd61f3ead...93a691d8EXAMPLE"
```

The following example command adds the `--cli-input-json`
 parameter to specify a JSON file (`custom-events.json`)
 of event payload.



```
aws cloudtrail-data put-audit-events --channel-arn $channelArn --external-id $UniqueExternalIDFromPartner --cli-input-json file://custom-events.json --region us-east-1
```

The following are the sample contents of the example JSON file,
 `custom-events.json`.



```
{
    "auditEvents": [
      {
        "eventData": "{\"version\":\"eventData.version\",\"UID\":\"UID\",
        \"userIdentity\":{\"type\":\"CustomUserIdentity\",\"principalId\":\"principalId\",
        \"details\":{\"key\":\"value\"}},\"eventTime\":\"2021-10-27T12:13:14Z\",\"eventName\":\"eventName\",
        \"userAgent\":\"userAgent\",\"eventSource\":\"eventSource\",
        \"requestParameters\":{\"key\":\"value\"},\"responseElements\":{\"key\":\"value\"},
        \"additionalEventData\":{\"key\":\"value\"},
        \"sourceIPAddress\":\"12.34.56.78\",\"recipientAccountId\":\"152089810396\"}",
        "id": "1"
      }
   ]
}
```
You can verify that the integration is working, and CloudTrail is ingesting events from
 the source correctly, by running the [**get-channel**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-channel.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-channel.html") command. The output of
 **get-channel** shows the most recent time stamp that CloudTrail
 received events.


```
aws cloudtrail get-channel --channel arn:aws:cloudtrail:us-east-1:01234567890:channel/EXAMPLE8-0558-4f7e-a06a-43969EXAMPLE
```

## (Optional) Calculate a checksum
 value


The checksum that you specify as the value of `EventDataChecksum`
 in a `PutAuditEvents` request helps you verify that CloudTrail receives the
 event that matches with the checksum; it helps verify the integrity of events.
 The checksum value is a base64-SHA256 algorithm that you calculate by running
 the following command.



```
printf %s "{"eventData": "{\"version\":\"eventData.version\",\"UID\":\"UID\",
        \"userIdentity\":{\"type\":\"CustomUserIdentity\",\"principalId\":\"principalId\",
        \"details\":{\"key\":\"value\"}},\"eventTime\":\"2021-10-27T12:13:14Z\",\"eventName\":\"eventName\",
        \"userAgent\":\"userAgent\",\"eventSource\":\"eventSource\",
        \"requestParameters\":{\"key\":\"value\"},\"responseElements\":{\"key\":\"value\"},
        \"additionalEventData\":{\"key\":\"value\"},
        \"sourceIPAddress\":\"`source_IP_address`\",
        \"recipientAccountId\":\"`recipient_account_ID`\"}",
        "id": "1"}" \
| openssl dgst -binary -sha256 | base64 ``` The command returns the checksum. The following is an example. ``` EXAMPLEDHjkI8iehvCUCWTIAbNYkOgO/t0YNw+7rrQE= ``` The checksum value becomes the value of `EventDataChecksum` in your `PutAuditEvents` request. If the checksum doesn't match with the one for the provided event, CloudTrail rejects the event with an `InvalidChecksum` error.

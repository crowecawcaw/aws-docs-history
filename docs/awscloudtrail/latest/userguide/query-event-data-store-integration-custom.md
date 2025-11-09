# Create a custom integration with the console

You can use CloudTrail to log and store user activity data from any source in your
hybrid environments, such as in-house or SaaS applications hosted on-premises or in
the cloud, virtual machines, or containers. Perform the first half of this procedure
in the CloudTrail Lake console, then call the [`PutAuditEvents`](../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md "../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md") API to ingest events,
providing your channel ARN and event payload. After you use the
`PutAuditEvents` API to ingest your application activity into CloudTrail,
you can use CloudTrail Lake to search, query, and analyze the data that is logged from
your applications.

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. From the navigation pane, under **Lake**, choose **Integrations**.
3. On the **Add integration** page, enter a name for your
   channel. The name can be 3-128 characters. Only letters, numbers, periods,
   underscores, and dashes are allowed.
4. Choose **My custom integration**.
5. From **Event delivery location**, choose to
   log the same activity events to existing event data stores, or
   create a new event data store.

If you choose to create a new event data store, enter a name for the event
data store and specify the retention period in days. You can keep the event data in an event data store for up to 3,653 days (about 10 years) if you choose the **One-year extendable retention pricing** option,
or up to 2,557 days (about 7 years) if you choose the **Seven-year retention pricing** option.

If you choose to log activity events to
one or more existing event data stores, choose the event data stores from the list.
The event data stores can only include activity events.
The event type in the console must be **Events from
integrations**. In the API, the `eventCategory`
value must be `ActivityAuditLog`. 6. In **Resource policy**, configure the resource policy for
the integration's channel. Resource policies are JSON
policy documents that specify what actions a specified principal can perform
on the resource and under what conditions. The accounts defined as
principals in the resource policy can call the `PutAuditEvents`
API to deliver events to your channel.

###### Note

If you do not create a resource policy for the channel, only the channel owner can call the `PutAuditEvents` API on the channel.

    1. (Optional) Enter a unique external ID to provide an extra layer of protection. The external ID is a unique string such as
     an account ID or a randomly generated string, to prevent against confused deputy.


    ###### Note

    If the resource policy includes an external ID, all calls to the
     `PutAuditEvents` API must include the external ID. However,
     if the policy does not define an external ID, you can still call the `PutAuditEvents`
     API and specify an `externalId` parameter.
    2. Choose **Add AWS
     account** to specify each AWS account ID to add as a
     principal in the resource policy for the channel.

7. (Optional) In the **Tags** area, you can add up to 50 tag
   key and value pairs to help you identify, sort, and control access to your
   event data store and channel. For more information about how to use IAM
   policies to authorize access to an event data store based on tags, see [Examples: Denying
   access to create or delete event data stores based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-eds-tags"). For
   more information about how you can use tags in AWS, see [Tagging
   your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") in the
   _AWS General Reference_.
8. When you are ready to create the new integration, choose **Add
   integration**. There is no review page. CloudTrail creates the
   integration, but to integrate your custom events, you must specify the
   channel ARN in a [`PutAuditEvents`](../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md "../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md") request.
9. Call the `PutAuditEvents` API to ingest your activity events
   into CloudTrail. You can add up
   to 100 activity events (or up to 1 MB) per `PutAuditEvents` request. You'll need the channel ARN that you created in preceding steps,
   the payload of events that you want CloudTrail to add, and the external ID (if specified for your resource policy). Be sure that there is
   no sensitive or personally-identifying information in event payload before
   ingesting it into CloudTrail. Events that you ingest into CloudTrail must follow the
   [CloudTrail Lake integrations event
   schema](query-integration-event-schema.md "query-integration-event-schema.md").

###### Tip

Use [AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") to be sure you are running the
most current AWS APIs.

The following examples show how to use the
**put-audit-events** CLI command. The
**--audit-events** and **--channel-arn**
parameters are required. You need the ARN of the channel that you created in
the preceding steps, which you can copy from the integration details page.
The value of **--audit-events** is a JSON array of event
objects. `--audit-events` includes a required ID from the event,
the required payload of the event as the value of `EventData`,
and an [optional
checksum](#event-data-store-integration-custom-checksum "#event-data-store-integration-custom-checksum") to help validate the integrity of the event after
ingestion into CloudTrail.

```
aws cloudtrail-data put-audit-events \
--region `region` \
--channel-arn $ChannelArn \
--audit-events \
id="`event_ID`",eventData='"{`event_payload`}"' \
id="`event_ID`",eventData='"{`event_payload`}"',eventDataChecksum="`optional_checksum`"
```

The following is an example command with two event examples.

```
aws cloudtrail-data put-audit-events \
--region us-east-1 \
--channel-arn arn:aws:cloudtrail:us-east-1:01234567890:channel/EXAMPLE8-0558-4f7e-a06a-43969EXAMPLE \
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
aws cloudtrail-data put-audit-events \
--channel-arn $channelArn \
--cli-input-json file://custom-events.json \
--region us-east-1
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
        \"sourceIPAddress\":\"`source_IP_address`\",\"recipientAccountId\":\"`recipient_account_ID`\"}",
        "id": "1"
      }
   ]
}
```

## (Optional)

Calculate a checksum value

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
 | openssl dgst -binary -sha256 | base64
```

The command returns the checksum. The following is an example.

```
EXAMPLEHjkI8iehvCUCWTIAbNYkOgO/t0YNw+7rrQE=
```

The checksum value becomes the value of `EventDataChecksum` in your
`PutAuditEvents` request. If the checksum doesn't match with the
one for the provided event, CloudTrail rejects the event with an
`InvalidChecksum` error.

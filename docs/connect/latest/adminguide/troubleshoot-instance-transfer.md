# Troubleshooting instance transfer

###### Important

This content is for IT administrators who have experience investigating network and
telephony issues. You must be familiar with accessing data in Amazon Connect contact records.

## Locate instance transfer information

Amazon Connect provides information in the contact record for each connected call. If a call
transfers between two different instances, you can view this information in the contact
record.

The following example shows the `connect:CrossInstanceInfo` segment
attributes:

```
"Contact": {
    ...
    "SegmentAttributes": {
        "connect:CrossInstanceInfo": {
            "ValueMap": {
                "RelatedInitialContactARN": {
                    "ValueArn": "`arn:aws:connect:us-west-2:111111111111:instance/fead664d-f209-4779-840e-e9e3d3ad8093/contact/609a5b3a-e28a-41a5-a86d-a0cff9529eeb`"
                },
                "RelatedContactARN": {
                    "ValueArn": "`arn:aws:connect:us-west-2:111111111111:instance/fead664d-f209-4779-840e-e9e3d3ad8093/contact/609a5b3a-e28a-41a5-a86d-a0cff9529eeb`"
                }
            }
        },
        "connect:ConnectionType": {
            "ValueString": "CONNECT"
        }
    }
    ...
}
```

For parameter descriptions, see [Segment attributes](connect-attrib-list.md#attribs-segment-attributes "connect-attrib-list.md#attribs-segment-attributes"). You must set up instance-to-instance
calls and follow the architectural guidance.

## Understand instance transfer scenarios

Calls can move between instances multiple times, creating complicated call flows. To
simplify validation, there are two scenarios that can be repeat throughout this process.

### Scenario 1: Outbound initiated call

This scenario occurs when you make an outbound call to another on-network Amazon Connect
number without any existing call in the system.

**How it works:**

- The system adds the inbound contact ARN on the second instance to the `RelatedInitialContactARN` and `RelatedContactARN` segment
  attributes on the first contact.
- For the inbound call on the second instance, both `RelatedInitialContactARN` and `RelatedContactARN` are set
  to the original outbound contact ARN.

###### Note

This scenario only occurs on the first original outbound call.

### Scenario 2: Transfer an existing inbound call

This scenario occurs when you transfer an existing inbound contact to a phone
number in any of your Amazon Connect instances. The instance (referred to as the
'second instance' below) can be the same instance that the call is transferring
from.

**On the first instance there are two contacts:**

1. The inbound contact:
   - `InitialContactID` and `PreviousContactID`
     are blank, as this is the initial contact.
   - `NextContactId` references the transfer contact below.
   - `connect:CrossInstanceInfo` is not populated.

2. The transfer contact:
   - `InitialContactID` and `PreviousContactID`
     reference the inbound contact above.
   - `connect:CrossInstanceInfo` is populated with 2 nested
     attributes, `RelatedInitialContactARN` and `RelatedContactARN`. Both contain the contact ARN that was
     generated on the second instance, detailed below.

**On the second instance, there is one contact:**

1. The inbound contact:
   - `InitialContactID`, `PreviousContactID`, and `NextContactID` are all blank.
   - `connect:CrossInstanceInfo` is populated with 2 nested
     attributes, `RelatedInitialContactARN` and `RelatedContactARN`.
   - `RelatedInitialContactARN` is populated with the
     inbound contact ARN in the first instance. (In case of multiple
     transfer, this value will be the ARN of the inbound contact that
     initiated the latest transfer - Want to make sure if this is clear,
     otherwise, we can remove this)
   - `RelatedContactARN` is populated with the transfer
     contact ARN in the first instance

###### Important

If multiple transfers occur within the original instance before the instance
to instance transfer, the system only references the external transfer and the
original inbound call. Internal transfers are not referenced.

## Analyze your call flow

You can use the preceding information to debug how your call flowed through your
environment.

###### To trace a call flow

1. Start with the inbound call to the instance.
2. Look up the inbound call in the contact record.
3. If the call was transferred, the record provides both the original inbound
   call from the previous instance and the outbound call from that instance to the
   current one.
4. Repeat this pattern to track back through all instance transfer
   between different instances.

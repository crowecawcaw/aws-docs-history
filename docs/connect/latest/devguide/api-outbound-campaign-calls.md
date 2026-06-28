# Best practices for using PutDialRequestBatch for outbound campaign calling

This topic provides guidance and best practices for using the [PutDialRequestBatch](../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md "../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md") API for outbound campaign calling. PutDialRequestBatch
takes in a list of [DialRequest](../../../connect-outbound/latest/APIReference/API_DialRequest.md "../../../connect-outbound/latest/APIReference/API_DialRequest.md") to
be dialed as part of an outbound campaign.

- Before using [PutDialRequestBatch](../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md "../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md"), always use the [StartCampaign](../../../connect-outbound/latest/APIReference/API_StartCampaign.md "../../../connect-outbound/latest/APIReference/API_StartCampaign.md") API to start the outbound campaign.
- In [DialRequest](../../../connect-outbound/latest/APIReference/API_DialRequest.md "../../../connect-outbound/latest/APIReference/API_DialRequest.md"), set `expirationTime`—the timestamp when
  a dial request expires—to a future time, preferably a few minutes in the
  future to allow the outbound campaigns dialer algorithm to attempt to dial.

Note the following failure codes:

    + `InvalidInput`: There's a request input mismatch with the
     parameters defined in [DialRequest](../../../connect-outbound/latest/APIReference/API_DialRequest.md "../../../connect-outbound/latest/APIReference/API_DialRequest.md"). Fix the request input and try again.
    + `RequestThrottled`: There aren't enough agents or telecom
     capacity available. The service maintains an upper limit on the number of
     records it can accept. When this limit is reached, the service returns a
     `RequestThrottled` message. This is a signal for you to stop
     sending more records and instead wait before attempting to retry, allowing
     the service to process and clear some records so it has room to accept
     more.
    + `UnknownError`: There is an internal failure in outbound
     campaigns. Please try again.

## Recommendations for tracking contact dispositions

A contact disposition is a type of state for a contact. It is either assigned by an
agent from a pre-defined list that you provide (for example, **Sold**,
**Wrong person**, **Right person, didn't sell**)
or assigned by Connect Customer for a contact (for example, `EXPIRED`,
`CONTACT_FLOW_DISCONNECT`, or `TELECOM_PROBLEM`). For outbound
campaigns, the contact disposition is assigned by Connect Customer.

You can use Connect Customer contact records or contact events to track the contact
dispositions for outbound campaigns. The key attribute to track contact disposition is
DisconnectReason, which indicates how the voice contact was terminated.

Disconnect reasons can be grouped into the following 3 categories:

- **Success**: A contact is successfully dialed
  out. Values: `CUSTOMER_DISCONNECT | AGENT_DISCONNECT |
 THIRD_PARTY_DISCONNECT | BARGED | CONTACT_FLOW_DISCONNECT |
 OTHER`
- **Expired**: This is expected behavior of the
  dialing algorithm. When the dialing algorithm determines insufficient dialing
  capacity (for example, because all agents are occupied or all telecom capacity
  is being used) during the duration set by the `expirationTime` parameter, Connect Customer does not attempt to call such endpoints. In other words, those endpoints
  are expired. If you need higher throughput, you can submit a request for higher
  dialing capacity. Values: `EXPIRED`
- **Failed**: Outbound campaigns failed a dial
  attempt because there are specific systematic errors. Values:
  `OUTBOUND_DESTINATION_ENDPOINT_ERROR | OUTBOUND_RESOURCE_ERROR |
 OUTBOUND_ATTEMPT_FAILED | TELECOM_PROBLEM`

For a description of each of these values, see DisconnectReason in the [Contact
records data model](../adminguide/ctr-data-model.md "../adminguide/ctr-data-model.md") topic in the _Connect Customer Administrator
Guide_.

If the disconnect reason is expired or failed type, take one of the following next
steps:

| Disconnect reason value               | Recommendation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EXPIRED`                             | We recommend that you use [PutDialRequestBatch](../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md "../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md") to create a new contact for this<br>destination with a different client token.                                                                                                                                                                                                                                                                                                                                                                |
| `OUTBOUND_DESTINATION_ENDPOINT_ERROR` | Check whether the current configuration of your Connect Customer<br>instance allows this destination to be dialed. For more information,<br>see [Countries you can call by default](../adminguide/country-code-allow-list.md "../adminguide/country-code-allow-list.md").                                                                                                                                                                                                                                                                                                                                                                          |
| `OUTBOUND_RESOURCE_ERROR`             | • Check whether your Connect Customer instance allows<br>outbound calls. For more information, see [Enable outbound calls](../adminguide/enable-outbound-calls.md "../adminguide/enable-outbound-calls.md").<br>• Check that the following resources exist: queue, flow,<br>Connect Customer source phone number, and campaign.<br>• After fixing the configuration of the instance, use [PutDialRequestBatch](../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md "../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md") to create a new contact for<br>this destination with a different client token. |
| `OUTBOUND_ATTEMPT_FAILED`             | There is an unidentified error. We recommend that you use [PutDialRequestBatch](../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md "../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md") to create a new contact for this<br>destination with a different client token.                                                                                                                                                                                                                                                                                                                                |
| `TELECOM_PROBLEM`                     | Disconnected due to an issue with connecting the call from the<br>carrier, network congestion, network error, etc. We recommend that<br>you use [PutDialRequestBatch](../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md "../../../connect-outbound/latest/APIReference/API_PutDialRequestBatch.md") to create a new contact for this<br>destination with a different client token.                                                                                                                                                                                                                                          |

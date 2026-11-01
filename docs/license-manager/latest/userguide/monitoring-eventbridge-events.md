

# License Manager event structure and change events
<a name="monitoring-eventbridge-events"></a>

Each License Manager event has a `source` of `aws.license-manager`. The `detail-type` field names the event. This topic covers the `License Change`, `Grant Change`, and `License Token Change` events. License Manager also sends `License Consumption Change` events. For the full list of License Manager events, see [AWS License Manager events](https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-license-manager.html) in the *AWS Events Reference*.

**Note**  
Delegate grantees don't receive `License Token Change` or `License Consumption Change` events.

## Event structure
<a name="monitoring-eventbridge-structure"></a>

The fields in the `detail` object depend on the event type. The following examples show these differences. In `License Change` and `Grant Change` events, fields for the other resource type are `null`. `Grant Change` events also include `granteePrincipalArn`. This field is the Amazon Resource Name (ARN) of the principal that receives the grant. The `eventType` field shows what changed.

The following example shows a `License Change` event for a new license:

```
{
 "version": "0",
 "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "detail-type": "License Change",
 "source": "aws.license-manager",
 "account": "123456789012",
 "time": "2025-09-15T21:53:33Z",
 "region": "us-west-2",
 "resources": [
   "arn:aws:license-manager::123456789012:license:l-5805db4afcda4f788aa92f1a05601e29"
 ],
 "detail": {
   "licenseArn": "arn:aws:license-manager::123456789012:license:l-5805db4afcda4f788aa92f1a05601e29",
   "licenseVersion": "1",
   "licenseStatus": "AVAILABLE",
   "grantStatus": null,
   "grantArn": null,
   "grantVersion": null,
   "eventType": "LICENSE_CREATED",
   "entitlements": null,
   "eventTimestamp": "2025-09-15 21:53:33"
 }
}
```

The following example shows a `Grant Change` event for a new grant that is pending acceptance:

```
{
 "version": "0",
 "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
 "detail-type": "Grant Change",
 "source": "aws.license-manager",
 "account": "123456789012",
 "time": "2020-03-15T15:24:31Z",
 "region": "us-east-1",
 "resources": [
   "arn:aws:license-manager::123456789012:license:l-123e4567e89b12d3a456426655440000"
 ],
 "detail": {
   "licenseArn": null,
   "licenseVersion": null,
   "licenseStatus": null,
   "grantStatus": "PENDING_ACCEPT",
   "grantArn": "arn:aws:license-manager::123456789012:grant:g-123e4567e89b12d3a456426655440001",
   "granteePrincipalArn": "arn:aws:iam::111122223333:root",
   "grantVersion": "1",
   "eventType": "GRANT_CREATED",
   "entitlements": null,
   "eventTimestamp": "2020-03-15 15:24:31"
 }
}
```

The following example shows a `License Token Change` event for a new license token:

```
{
 "version": "0",
 "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
 "detail-type": "License Token Change",
 "source": "aws.license-manager",
 "account": "123456789012",
 "time": "2020-03-15T15:24:31Z",
 "region": "us-east-1",
 "resources": [
   "tokenId:12345678-1234-1234-1234-123456789012"
 ],
 "detail": {
   "licenseArn": "arn:aws:license-manager::123456789012:license:l-123e4567e89b12d3a456426655440000",
   "tokenId": "12345678-1234-1234-1234-123456789012",
   "tokenExpirationTime": "2020-03-15T15:24:31Z",
   "eventType": "TOKEN_CREATED",
   "eventTimestamp": "2020-03-15 15:24:31"
 }
}
```

## Event types
<a name="monitoring-eventbridge-change-events"></a>

The `eventType` field and the `licenseStatus` or `grantStatus` field together show what changed. `License Token Change` events don't include a status field.


**License Manager event types**  

| detail-type | Scenario | eventType | Status | 
| --- | --- | --- | --- | 
| `License Change` | License created | `LICENSE_CREATED` | `AVAILABLE` | 
| `License Change` | License activated or license attribute updated | `LICENSE_UPDATED` | `AVAILABLE` | 
| `License Change` | License deactivated | `LICENSE_UPDATED` | `DEACTIVATED` | 
| `License Change` | License expired | `LICENSE_EXPIRED` | `EXPIRED` | 
| `License Change` | License deleted | `LICENSE_DELETED` | `DELETED` | 
| `Grant Change` | Grant created and automatically accepted | `GRANT_CREATED` | `DISABLED` | 
| `Grant Change` | Grant created, pending acceptance | `GRANT_CREATED` | `PENDING_ACCEPT` | 
| `Grant Change` | Grant accepted | `GRANT_UPDATED` | `DISABLED` | 
| `Grant Change` | Grant rejected | `GRANT_UPDATED` | `REJECTED` | 
| `Grant Change` | Grant activated | `GRANT_UPDATED` | `ACTIVE` | 
| `Grant Change` | Grant deactivated | `GRANT_UPDATED` | `DISABLED` | 
| `Grant Change` | Grant deleted | `GRANT_DELETED` | `DELETED` | 
| `License Token Change` | License token created | `TOKEN_CREATED` | None | 
| `License Token Change` | License token about to expire (within 15 days) | `TOKEN_ABOUT_TO_EXPIRE` | None | 
| `License Token Change` | License token deleted | `TOKEN_DELETED` | None | 
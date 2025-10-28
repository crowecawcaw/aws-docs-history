# Monitor billing assignment requests

for shared Capacity Reservations

Amazon EC2 sends Amazon EventBridge events when the state of a billing assignment request
changes.

- Events are sent to the Capacity Reservation owner when a request enters the following
  states: `accepted` | `rejected` |
  `expired` | `revoked`.
- Events are sent to the requested consumer account when a request
  enters the following states: `pending` | `expired`
  | `cancelled` | `revoked`. For more information about Amazon EventBridge, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md"). The following is the Amazon EventBridge event pattern. ``{ "version":"0", "id":"12345678-1234-1234-1234-123456789012", "detail-type":"On-Demand Capacity Reservation Billing Ownership Request `pending|accepted|rejected|cancelled|revoked|expired`", "source":"aws.ec2", "account":"`account_id`", "time":"`state_change_timestamp`", "region":"`region`", "resources":[ "arn:aws:ec2:`region`:`cr_owner_account_id`:capacity-reservation/`cr_id`" ], "detail":{ "capacity-reservation-id":"`cr_id`", "updateTime":`timestamp`, "ownerAccountId":"`cr_owner_account_id`", "unusedReservationChargesOwnerID":"`consumer_account_id`", "status":"`pending|accepted|rejected|cancelled|revoked|expired`", "statusMessage":"`message` } }`` The following is an example of an event that is sent to the Capacity Reservation owner (`222222222222`) when a consumer account (`111111111111`) accepts a billing assignment request for a shared Capacity Reservation (`cr-01234567890abcdef`). `{ "version":"0", "id":"12345678-1234-1234-1234-123456789012", "detail-type":"On-Demand Capacity Reservation Billing Ownership Request accepted", "source":"aws.ec2", "account":"222222222222", "time":"2024-09-01Thh:59:59Z", "region":"us-east-1", "resources":[ "arn:aws:ec2:us-east-1:222222222222:capacity-reservation/cr-01234567890abcdef" ], "detail":{ "capacity-reservation-id":"cr-01234567890abcdef", "updateTime":"2024-08-01Thh:59:59Z", "ownerAccountId":"222222222222", "unusedReservationChargesOwnerID":"111111111111", "status":"accepted", "statusMessage":"billing transfer status message" } }`

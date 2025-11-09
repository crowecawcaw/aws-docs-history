# Automating Savings Plans with Amazon EventBridge

EventBridge helps you automate your AWS services and respond automatically to system events such
as application availability issues or resource changes. Events from AWS services are delivered
to EventBridge in near-real time. Events are emitted on a best-effort basis. Based on the rules you
create, EventBridge calls one or more target actions when an event matches the values that you specify in
a rule.

The actions that can be automatically triggered include the following:

- Invoking an AWS Lambda function
- Invoking Amazon EC2 Run Command
- Relaying the event to Amazon Kinesis Data Streams
- Activating an AWS Step Functions state machine
- Notifying an Amazon SNS topic or an AWS SMS queue
  Some examples of using CloudWatch Events with Savings Plans include:

- Activating a Lambda function when a Savings Plans retires.
- Notifying an Amazon SNS topic when a Savings Plans is marked `payment-failed` or
  `active`.
  For more information, see the [Amazon CloudWatch Events User Guide](../../../AmazonCloudWatch/latest/events.md "../../../AmazonCloudWatch/latest/events.md").

## Sample events from Savings Plans

This section includes example events from Savings Plans. Savings Plans generate two types of events. State
change events that are triggered upon state changes, and state change alerts events that notify
an upcoming state change that will occur in one or seven days.

### Savings Plans state change event

Savings Plans state changes are generated when a Savings Plans transitions from one state to
another. For example, `payment-pending` state changes to `active`, or an
`active` state changes to `retired`.

```
{
    "version": "0",
    "id": "999cccaa-eaaa-0000-1111-123456789012",
    "detail-type": "Savings Plans State Change",
    "source": "aws.savingsplans",
    "account": "123456789012",
    "time": "2020-09-16T20:43:05Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:savingsplans::123456789012:savingsplan/07ec53ab-91c3-4ac5-bde6-79fd53192252"
    ],
    "detail": {
        "severity": "INFO",
        "previousState": "payment-pending",
        "currentState": "active",
        "message": "PaymentSuccessful"
    }
}
```

The state change event contains fields for resources (Savings Plans ARNs), previous state, current
state, severity, and message.

| Possible values for state change events | previousState   | currentState | severity                                                                     | message |
| --------------------------------------- | --------------- | ------------ | ---------------------------------------------------------------------------- | ------- |
| queued                                  | payment-pending | INFO         | `QueuedPurchaseFulfillment`                                                  |
| queued                                  | payment-failed  | ERROR        | `LimitExceededException`<br>or<br>`SavingsPlanOfferingNotAvailableException` |
| queued                                  | queued-deleted  | INFO         | `SavingsPlanQueuedDeleted`                                                   |
| payment-pending                         | active          | INFO         | `PaymentSuccessful`                                                          |
| payment-pending                         | payment-failed  | ERROR        | `LimitExceededException`<br>or<br>`PaymentUnsuccessful`                      |
| active                                  | retired         | INFO         | `SavingsPlanExpiration`                                                      |
| active                                  | pending-return  | INFO         | `SavingsPlanReturnRequested`                                                 |
| pending-return                          | returned        | INFO         | `SavingsPlanReturnSuccessful`                                                |
| pending-return                          | active          | ERROR        | `SavingsPlanReturnUnsuccessful`                                              |

### Savings Plans state change alert event

Savings Plans state change alerts are generated when a Savings Plans transitions from the
`queued` state to `active`, or `active` to `retired`
in one or seven days. This is a proactive notification to alert you if any Savings Plans is
retiring, or a queued state is fulfilled.

```
{
    "version": "0",
    "id": "999cccaa-eaaa-0000-1111-123456789012",
    "detail-type": "Savings Plans State Changange Alert",
    "source": "aws.savingsplans",
    "account": "123456789012",
    "time": "2020-09-16T00:15:00Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:savingsplans::123456789012:savingsplan/07ec53ab-91c3-4ac5-bde6-79fd53192252",
        "arn:aws:savingsplans::123456789012:savingsplan/19a9fa12-911a-18ed-9aa1-3a2615149a14"
    ],
    "detail": {
        "currentState": "queued",
        "nextState": "active",
        "remainingdays": "1",
        "nextStateChangeDate": "2020-09-17",
        "message": "queued savings plans will go to active state on 2020-09-17"
    }
}
```

The state change alert event contains fields for resources (Savings Plans ARNs), current state, next
state, remaining days, next state change date, and message.

| Possible values for state change alert events | currentState | nextState | remainingDays                                                  | message |
| --------------------------------------------- | ------------ | --------- | -------------------------------------------------------------- | ------- |
| queued                                        | active       | 1         | Queued Savings Plans will go to active state on `YYYY-MM-DD`.  |
| queued                                        | active       | 7         | Queued Savings Plans will go to active state on `YYYY-MM-DD`.  |
| active                                        | retired      | 1         | Active Savings Plans will go to retired state on `YYYY-MM-DD`. |
| active                                        | retired      | 7         | Active Savings Plans will go to retired state on `YYYY-MM-DD`. |

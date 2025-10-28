# Monitoring Account Management events with EventBridge

Amazon EventBridge, formerly called CloudWatch Events, helps you monitor events that are specific to and
initiate target actions that use other AWS services. Events from AWS services are
delivered to EventBridge in near real time.

Using EventBridge, you can create _rules_ that match incoming
_events_ and route them to _targets_ for
processing.

For more information, see [Getting started with
Amazon EventBridge](../../../eventbridge/latest/userguide/eventbridge-getting-set-up.md "../../../eventbridge/latest/userguide/eventbridge-getting-set-up.md") in the _Amazon EventBridge User Guide_.

## Account Management events

The following examples show events for Account Management. Events are produced on a best-effort
basis.

Only events that are specific to enabling and disabling Regions and API calls via CloudTrail
are currently available for Account Management.

###### Event types

- [Event for enabling and disabling Regions](#event-example-1 "#event-example-1")

### Event for enabling and disabling Regions

When you enable or disable a Region in an account, either from the Console or from
the API, an asynchronous task is kicked off. The initial request will be logged as a
CloudTrail event in the target account. In addition, an EventBridge event will be sent to the
calling account when either the enable or disable process has started, and again
once either process has completed.

The following example event shows how a request will be sent indicating that on
`2020-09-30` the `ap-east-1` Region was
`ENABLED` for account `123456789012`.

```
{
   "version":"0",
   "id":"11112222-3333-4444-5555-666677778888",
   "detail-type":"Region Opt-In Status Change",
   "source":"aws.account",
   "account":"123456789012",
   "time":"2020-09-30T06:51:08Z",
   "region":"us-east-1",
   "resources":[
      "arn:aws:account::123456789012:account"
   ],
   "detail":{
      "accountId":"123456789012",
      "regionName":"ap-east-1",
      "status":"ENABLED"
   }
}
```

There are four possible statuses which match the statuses returned by the
`GetRegionOptStatus` and `ListRegions` APIs:

- `ENABLED` – The Region has been successfully enabled for
  the `accountId` indicated
- `ENABLING` – The Region is in the process of being
  enabled for the `accountId` indicated
- `DISABLED` – The Region has been successfully disabled
  for the `accountId` indicated
- `DISABLING` – The Region is in the process of being
  disabled for the `accountId` indicated

The following sample event pattern, creates a rule that captures all Region
events.

```
{
   "source":[
      "aws.account"
   ],
   "detail-type":[
      "Region Opt-In Status Change"
   ]
}
```

The following sample event pattern, creates a rule that captures only
`ENABLED` and `DISABLED` Region events.

```
{
   "source":[
      "aws.account"
   ],
   "detail-type":[
      "Region Opt-In Status Change"
   ],
   "detail":{
      "status":[
         "DISABLED",
         "ENABLED"
      ]
   }
}
```

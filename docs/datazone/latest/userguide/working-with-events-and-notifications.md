# Amazon DataZone events and

notifications

Amazon DataZone keeps you informed of important activities within your data portal, such as
subscription requests, updates, comments, and system events. Amazon DataZone provides you with this
information by delivering messages in the dedicated inbox in the data portal or via the Amazon
EventBridge default bus.

## Events via the dedicated inbox in the

Amazon DataZone data portal

Amazon DataZone provides a dedicated inbox in the data portal where you can see and take action
on your messages. Recent messages also surface on the home page, project page, and catalog page.
For example, if a user requests access to a data asset, publishing project’s owners and
contributors of that asset see the request in the data portal and once an action is taken,
project members of the subscribing project related to this request see the notification in the
data portal. There are two types of messages:

- Tasks - these messages inform the recipient that there is action needed somewhere. They
  have an optional status field which you can use for tracking.
- Events - these messages are informational and have no assigned status. Events provide an
  audit trail of recent updates.

In Amazon DataZone, messages are generated for the following event types:

| Event category                     | Event name                                       | Event description                                                                                                        | Event type |
| ---------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ---------- |
| Subscription                       | Subscription request created                     | Event is generated when a subscription request is created                                                                | Task       |
| Subscription                       | Subscription request accepted                    | Event is generated when a subscription request is accepted                                                               | Event      |
| Subscription                       | Subscription request rejected                    | Event is generated when a subscription request is rejected                                                               | Event      |
| Subscription                       | Subscription request deleted                     | Event is generated when a subscription request is deleted                                                                | Event      |
| Project                            | Project creation succeeded                       | Event is generated when project creation succeeds                                                                        | Event      |
| Project membership                 | Project member addition succeeded                | Event is generated when a new member is added to a project                                                               | Event      |
| Project membership                 | Project member removal succeeded                 | Event is generated when a member is removed to a project                                                                 | Event      |
| Project membership                 | Project member role change succeeded             | Event is generated a member's role in the project is changed                                                             | Event      |
| Environment                        | Environment deployment started                   | Event is generated when a environment deployment is initiated                                                            | Event      |
| Environment                        | Environment deployment completed                 | Event is generated when a environment deployment completes successfully                                                  | Event      |
| Environment                        | Environment deployment failed                    | Event is generated when a environment deployment fails                                                                   | Event      |
| Environment                        | Environment deployment custom workflow initiated | Event is generated when a environment with custom workflow is initiated                                                  | Event      |
| Data asset                         | Asset added to inventory                         | Event is generated when a new data asset is added to inventory i.e. added to catalog in<br>draft state                   | Event      |
| Data asset                         | Asset published                                  | Event is generated when a new data asset is published i.e. available for<br>subscription                                 | Event      |
| Data asset                         | Asset schema changed                             | Event is generated when a asset schema has changed since previous ingestion job                                          | Event      |
| Subscribing                        | Subscription created                             | Event is generated when someone requests to subscribe to a data asset                                                    | Task       |
| Subscribing                        | Subscription approved                            | Event is generated when a subscription is approved by the publlishing project owner or<br>contributor                    | Event      |
| Subscribing                        | Subscription rejected                            | Event is generated when a subscription is rejected by the publlishing project owner or<br>contributor                    | Event      |
| Subscribing                        | Subscription deleted                             | Event is generated when a subscription is canceled by the subscriber                                                     | Event      |
| Subscribing                        | Subscription grant requested                     | Event is generated when a someone requests access to an asset                                                            | Event      |
| Subscribing                        | Subscription grant completed                     | Event is generated when a subscription is granted access to the asset by the<br>publlishing project owner or contributor | Event      |
| Subscribing                        | Subscription grant failed                        | Event is generated when a subscription grant fails                                                                       | Event      |
| Subscribing                        | Subscription grant revoke requested              | Event is generated when a subscription grant revoked is initiated by the publlishing<br>project owner or contributor     | Event      |
| Subscribing                        | Subscription grant revoke completed              | Event is generated when a subscription grant revoke is completed                                                         | Event      |
| Subscribing                        | Subscription grant revoke failed                 | Event is generated when a subscription grant revoke fails                                                                | Event      |
| Automated business name generation | Business name generated succeeded                | Eventis generated when the automated business name generated job completes<br>successfully                               | Event      |
| Automated business name generation | Business name generated failed                   | Event is generated when the automated business name generated job fails                                                  | Event      |
| Data source run                    | Data source created                              | Event is generated when a new data source is created                                                                     | Event      |
| Data source run                    | Data source updated                              | Event is generated when an existing data source is updated                                                               | Event      |
| Data source run                    | Data source run triggered                        | Event is generated when a data source run is initiated                                                                   | Event      |
| Data source run                    | Data source run succeeded                        | Event is generated when a data source run succeeds                                                                       | Event      |
| Data source run                    | Data source run failed                           | Event is generated when a data source run fails                                                                          | Event      |

To view tasks in your data portal inbox, complete the following steps:

1. Navigate to the Amazon DataZone data portal using the data portal URL and log in using your SSO
   or AWS credentials. If you’re an Amazon DataZone administrator, you can obtain the data portal URL
   by accessing the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone")
   in the AWS account where the Amazon DataZone domain was created.
2. In the data portal, to view a pop up with the recent set of tasks, select the bell icon
   next to the Search bar.
3. Select View all to view all tasks. You can change views and see all events by selecting
   the Events tab.
4. You can filter the search by the event subject, active or inactive status, or date
   range.
5. Choose any individual task to navigate to the location where you can respond to the
   task.

To view events in your data portal inbox, complete the following steps:

1. Navigate to the Amazon DataZone data portal using the data portal URL and log in using your SSO
   or AWS credentials. If you’re an Amazon DataZone administrator, you can obtain the data
   portal URL by accessing the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone")
   in the AWS account where the Amazon DataZone root domain was created.
2. In the data portal, to view the pop up for the recent set of events, select the bell icon
   next to the Search bar.
3. Select View all to view all events. You can change views and see all tasks by selecting
   the Tasks tab.
4. Filter the search by the event subject or date range.
5. Choose any individual event to navigate to the location where you can view details about
   that event.

## Events via Amazon EventBridge default bus

In addition to sending messages to your dedicated inbox in the data portal, DataZone also
sends these messages to your Amazon EventBridge default event bus in the same AWS account where
your Amazon DataZone root domain is hosted. This enables event-driven automation, such as subscription
fulfillment or custom integrations with other tools. You can create rules that match incoming
[Amazon
EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") and send them to [Amazon
EventBridge targets](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md") for processing. A single rule can send an event to multiple targets,
which can then run in parallel.

Here's a sample event:

```

{
  "version": "0",
  "id": "bd3d6239-2877-f464-0572-b1d76760e085",
  "detail-type": "Subscription Request Created",
  "source": "aws.datazone",
  "account": "111111111111",
  "time": "2023-11-13T17:57:00Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "version": "655",
    "metadata": {
      "domain": "dzd_bc8e1ez8r2a6xz",
      "user": "44f864b8-50a1-70cc-736f-c1f763934ab7",
      "id": "5jbc0lie0sr99j",
      "version": "1",
      "typeName": "SubscriptionRequestEntityType",
      "owningProjectId": "6oy92hwk937pgn",
      "awsAccountId": "111111111111",
      "clientToken": "e781b7b5-78c5-4608-961e-3792a6c3ff0d"
    },
    "data": {
      "autoApproved": true,
      "requesterId": "44f864b8-50a1-70cc-736f-c1f763934ab7",
      "status": "PENDING",
      "subscribedListings": [
        {
          "id": "ayzstznnx4dxyf",
          "ownerProjectId": "5a3se66qm88947",
          "version": "12"
        }
      ],
      "subscribedPrincipals": [
        {
          "id": "6oy92hwk937pgn",
          "type": "PROJECT"
        }
      ]
    }
  }
}

```

The full list of detail-types supported by Amazon DataZone include:

- Subscription Request Created
- Subscription Request Accepted
- Subscription Request Rejected
- Subscription Request Deleted
- Subscription Grant Requested
- Subscription Grant Completed
- Subscription Grant Failed
- Subscription Grant Revoke Requested
- Subscription Grant Revoke Completed
- Subscription Grant Revoke Failed
- Asset Added To Inventory
- Asset Added To Catalog
- Asset Schema Changed
- Data Source Status Change
- Data Source Created
- Data Source Updated
- Data Source Run Triggered
- Data Source Run Succeeded
- Data Source Run Failed
- Domain Creation Succeeded
- Domain Creation Failed
- Domain Deletion Succeeded
- Domain Deletion Failed
- Environment Deployment Started
- Environment Deployment Completed
- Environment Deployment Failed
- Environment Deletion Started
- Environment Deletion Completed
- Environment Deletion Failed
- Project Creation Succeeded
- Project Member Addition Succeeded
- Project Member Removal Succeeded
- Project Member Role Change Succeeded
- Environment Deployment Customer Workflow Initiated
- Business Name Generation Succeeded
- Business Name Generation Failed

For more information, see [Amazon
EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

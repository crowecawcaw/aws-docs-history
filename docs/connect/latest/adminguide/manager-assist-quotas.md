# Service quotas

The following quotas apply during preview. These quotas might change
as the capability matures, so check this page for updates.

## Quotas

| Quota                  | Default value                                                                                                         | Scope                   | Adjustable               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------ |
| Maximum message length | 15,000 characters                                                                                                     | Per message             | No                       |
| Request rate           | Subject to the Connect Customer agent assist<br>`SendMessage` rate quota, which varies by AWS<br>Region               | Per account, per Region | Yes, through AWS Support |
| Chat context           | Responses reflect the recent turns in a chat. In a very long<br>chat, the earliest turns are no longer<br>referenced. | Per chat                | No                       |

## Behavior when a quota is reached

| Quota reached                      | Behavior                                                                                                          |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Message length (15,000 characters) | The message box shows a character count, and you cannot submit<br>the message until you shorten it.               |
| Request rate                       | Additional questions are throttled and return a rate limit<br>error. Wait a moment, and then try again.           |
| Chat context                       | Responses no longer reflect the earliest turns in the chat.<br>Provide the relevant context in your next message. |

## Request a quota increase

The request rate is the only adjustable quota. Because it is governed by the
Connect Customer agent assist `SendMessage` service quota, request an increase through AWS
Support rather than in the Service Quotas console. The maximum message length and chat
context quotas are fixed application quotas during preview, and cannot be
increased.

## Regional differences

The request rate varies by AWS Region. The maximum message length and chat context
behavior are the same in all Regions where manager assist is available.

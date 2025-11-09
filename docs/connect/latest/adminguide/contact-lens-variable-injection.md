# Specify variables for certain

parameters when creating or managing rules using Amazon Connect APIs

When you create or manage rules programmatically using Amazon Connect APIs (such as
[CreateRule](../APIReference/API_CreateRule.md "../APIReference/API_CreateRule.md") or
[UpdateRule](../APIReference/API_UpdateRule.md "../APIReference/API_UpdateRule.md")),
you can specify variables for certain parameters. The variables are resolved at
runtime when the action is triggered, based on the value of the [EventSourceName](../APIReference/API_RuleTriggerEventSource.md "../APIReference/API_RuleTriggerEventSource.md") parameter.

For example, let's say you're setting up a task action and you want to add
more context. Following is an example of how you could use variable injections
to include the ID of the contact and the ID of the agent in the
`Description` field of the task:

- Customer is unhappy about the phone call. A swear word was detected
  during the conversation with agent
  `$.ContactLens.PostCall.Agent.AgentId` in the contact
  `$.ContactLens.PostCall.ContactId`
  When the action is triggered, his string would resolve to "Customer is unhappy
  about the phone call. A swear word was detected during a conversation with agent
  12345678-1234-1234-1234-EXAMPLEID012 in the contact
  87654321-1234-1234-1234-EXAMPLEID345"

The following table lists each event source, and the JSONPath to use for
fields that support variable injection.

| EventSourceName                 | JSONPath Reference                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OnPostCallAnalysisAvailable     | $.ContactLens.PostCall.ContactId<br>$.ContactLens.PostCall.Agent.AgentId<br>$.ContactLens.PostCall.Queue.QueueId                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| OnRealTimeCallAnalysisAvailable | $.ContactLens.RealTimeCall.ContactId<br>$.ContactLens.RealTimeCall.Agent.AgentId<br>$.ContactLens.RealTimeCall.Queue.QueueId                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| OnPostChatAnalysisAvailable     | $.ContactLens.PostChat.ContactId<br>$.ContactLens.PostChat.Agent.AgentId<br>$.ContactLens.PostChat.Queue.QueueId                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| OnSalesforceCaseCreate          | $.ThirdParty.Salesforce.CaseCreate.CaseNumber<br>$.ThirdParty.Salesforce.CaseCreate.Name<br>$.ThirdParty.Salesforce.CaseCreate.Email<br>$.ThirdParty.Salesforce.CaseCreate.Phone<br>$.ThirdParty.Salesforce.CaseCreate.Company<br>$.ThirdParty.Salesforce.CaseCreate.Type<br>$.ThirdParty.Salesforce.CaseCreate.Reason<br>$.ThirdParty.Salesforce.CaseCreate.Origin<br>$.ThirdParty.Salesforce.CaseCreate.Subject<br>$.ThirdParty.Salesforce.CaseCreate.Priority<br>$.ThirdParty.Salesforce.CaseCreate.CreatedDate<br>$.ThirdParty.Salesforce.CaseCreate.Description |
| OnZendeskTicketCreate           | $.ThirdParty.Zendesk.TicketCreate.Id<br>$.ThirdParty.Zendesk.TicketCreate.Priority<br>$.ThirdParty.Zendesk.TicketCreate.CreatedAt                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| OnZendeskTicketStatusUpdate     | $.ThirdParty.Zendesk.TicketStatusUpdate.Id<br>$.ThirdParty.Zendesk.TicketStatusUpdate.Priority<br>$.ThirdParty.Zendesk.TicketStatusUpdate.CreatedAt                                                                                                                                                                                                                                                                                                                                                                                                                  |

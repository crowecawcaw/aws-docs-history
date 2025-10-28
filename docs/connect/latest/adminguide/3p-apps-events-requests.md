# Events and requests when granting

third-party applications access to Amazon Connect

This topic lists the permissions you must explicitly give to third party
applications to access Amazon Connect data.

###### Note

If you are a developer, review how to create applications that react to
events: [Integrate application with Amazon Connect Agent Workspace agent data](../../../agentworkspace/latest/devguide/integrate-with-agent-data.md "../../../agentworkspace/latest/devguide/integrate-with-agent-data.md").

When you onboard third-party applications by using the API or the onboarding UI in
the AWS Management Console, you must explicitly give third-party applications permissions to
Amazon Connect data. You can also edit the permissions on an existing app.

To understand the effects of assigning a particular permission, review the
following permissions, description, and corresponding requests and events.

For example, if you assign the permission `User.Details.View` to the
application, then it will have the ability to make the following requests:
`agent.getName` and `agent.getARN`. If your app attempts
to subscribe to an event or make a request for data that it does not have permission
for, your app may not function as intended.

To learn more about each request and event, see the [API Reference](../../../agentworkspace/latest/devguide/api-reference-3p-apps-events-and-requests.md "../../../agentworkspace/latest/devguide/api-reference-3p-apps-events-and-requests.md").

| Permission                   | Description                                                                              | Requests                                                                                                                                                                                            | Events                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| User.Details.View            | Details about the agent, such as their full name and User ARN                            | agent/getName agent/getARN                                                                                                                                                                          |                                                                              |
| User.Configuration.View      | Configuration information about the agent, such as their associated routing profile      | agent/getRoutingProfile agent/getChannelConcurrency agent/getExtension getLanguage agent/listAvailabilityStates agent/listQuickConnects voice/getOutboundCallPermission voice/listDialableCountries | onLanguageChanged                                                            |
| User.Status.View             | Details about the agent's status                                                         | agent/getState                                                                                                                                                                                      | agent/onStateChanged                                                         |
| Contact.Details.View         | Details about the contact available in the workspace                                     | contact/getInitialContactId contact/getChannelType contact/getStateDuration contact/getQueue contact/getQueueTimestamp                                                                              | contact/onCleared contact/onMissed contact/onStartingAcw contact/onConnected |
| Contact.CustomerDetails.View | Details about your customers, such as the phone number they're calling from (Voice only) | voice/getInitialCustomerPhoneNumber                                                                                                                                                                 |                                                                              |
| Contact.Attributes.View      | Metadata about the contact                                                               | contact/getAttribute contact/getAttributes                                                                                                                                                          |                                                                              |
| User.Status.Edit             | Modify agent status                                                                      | agent/setAvailabilityState agent/setAvailabilityStateByName agent/setOffline                                                                                                                        |                                                                              |
| Contact.Details.Edit         | Contact edit capabilities, like making outbound calls or transferring calls.             | voice/createOutboundCall contact/transfer contact/addParticipant contact/accept contact/clear                                                                                                       |                                                                              |
| \*                           | Provides access to all requests and events.                                              |                                                                                                                                                                                                     |                                                                              |

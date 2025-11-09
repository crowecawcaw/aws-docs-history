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

| Permission                   | Description                                                                                 | Requests                                                                                                                                                                                                                 | Events                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| User.Details.View            | Details about the agent, such as their full name and User<br>ARN                            | agent/getName<br>agent/getARN                                                                                                                                                                                            |                                                                                       |
| User.Configuration.View      | Configuration information about the agent, such as their<br>associated routing profile      | agent/getRoutingProfile<br>agent/getChannelConcurrency<br>agent/getExtension<br>getLanguage<br>agent/listAvailabilityStates<br>agent/listQuickConnects<br>voice/getOutboundCallPermission<br>voice/listDialableCountries | onLanguageChanged                                                                     |
| User.Status.View             | Details about the agent's status                                                            | agent/getState                                                                                                                                                                                                           | agent/onStateChanged                                                                  |
| Contact.Details.View         | Details about the contact available in the workspace                                        | contact/getInitialContactId<br>contact/getChannelType<br>contact/getStateDuration<br>contact/getQueue<br>contact/getQueueTimestamp                                                                                       | contact/onCleared<br>contact/onMissed<br>contact/onStartingAcw<br>contact/onConnected |
| Contact.CustomerDetails.View | Details about your customers, such as the phone number they're<br>calling from (Voice only) | voice/getInitialCustomerPhoneNumber                                                                                                                                                                                      |                                                                                       |
| Contact.Attributes.View      | Metadata about the contact                                                                  | contact/getAttribute<br>contact/getAttributes                                                                                                                                                                            |                                                                                       |
| User.Status.Edit             | Modify agent status                                                                         | agent/setAvailabilityState<br>agent/setAvailabilityStateByName<br>agent/setOffline                                                                                                                                       |                                                                                       |
| Contact.Details.Edit         | Contact edit capabilities, like making outbound calls or<br>transferring calls.             | voice/createOutboundCall<br>contact/transfer<br>contact/addParticipant<br>contact/accept<br>contact/clear                                                                                                                |                                                                                       |
| \*                           | Provides access to all requests and events.                                                 |                                                                                                                                                                                                                          |                                                                                       |

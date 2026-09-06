

# Events and requests for 3P apps
<a name="3p-apps-events-requests"></a>

**Note**  
If you are a developer, review how to create applications that react to events: [Integrate application with Connect Customer agent workspace agent data](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-with-agent-data.html).

You must explicitly give third-party applications permission to access Connect Customer data. Assign permissions with the API or in the AWS Management Console. You can also edit the permissions on an existing app.

To understand the effects of assigning a particular permission, review the following permissions, description, and corresponding requests and events. 

For example, if you assign `User.Details.View` to an application, the application can make the `agent.getName` and `agent.getARN` requests. If your app subscribes to an event or requests data that it doesn't have permission for, the app might not work as expected.

 To learn more about each request and event, see the [API Reference](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-events-and-requests.html).


| Permission | Description | Requests | Events | 
| --- | --- | --- | --- | 
| User.Details.View | Details about the agent, such as their full name and user ARN | agent/getName<br />agent/getARN |  | 
| User.Configuration.View | Configuration information about the agent, such as their associated routing profile | agent/getRoutingProfile<br />agent/getChannelConcurrency<br />agent/getExtension<br />getLanguage<br />agent/listAvailabilityStates<br />agent/listQuickConnects<br />voice/getOutboundCallPermission<br />voice/listDialableCountries | onLanguageChanged | 
| User.Status.View | Details about the agent's status | agent/getState | agent/onStateChanged | 
| Contact.Details.View | Details about the contact open in the workspace | contact/getInitialContactId<br />contact/getChannelType<br />contact/getStateDuration<br />contact/getQueue<br />contact/getQueueTimestamp | contact/onCleared<br />contact/onMissed<br />contact/onStartingAcw<br />contact/onConnected | 
| Contact.CustomerDetails.View | Details about your customers, such as the phone number they're calling from (Voice only) | voice/getInitialCustomerPhoneNumber |  | 
| Contact.Attributes.View | Metadata about the contact | contact/getAttribute<br />contact/getAttributes |  | 
| User.Status.Edit | Modify agent status | agent/setAvailabilityState<br />agent/setAvailabilityStateByName<br />agent/setOffline |  | 
| Contact.Details.Edit | Contact edit capabilities, such as making outbound calls or transferring calls | voice/createOutboundCall<br />contact/transfer<br />contact/addParticipant<br />contact/accept<br />contact/clear |  | 
| \* | Provides access to all requests and events. |  |  | 
# Service request management

###### Topics

- [When to use a service request](service-request-when-to-use.md "service-request-when-to-use.md")
- [How service request management works](service-request-resolution.md "service-request-resolution.md")
- [Testing a service request in AMS](service-request-testing.md "service-request-testing.md")
- [Creating a service request in AMS](gui-ex-create-service-request.md "gui-ex-create-service-request.md")
- [Monitoring and updating service requests in AMS](update-monitor-review-service-requests.md "update-monitor-review-service-requests.md")
- [Responding to an AMS-generated service requests](respond-to-sent-generated-sr.md "respond-to-sent-generated-sr.md")
  Service requests are communications to AMS created by you to ask for information or advice.
  A good example of a standard service request is for guidance or help in configuring an AMS service,
  like Alarm Manager, Patch Orchestrator, and so forth. You can also receive service requests from AMS; these are called
  outbound service requests or service notifications. To see a list of your service requests, and outbound service requests,(service notifications),
  sent to you by AMS, look on the **Service requests** page of the AMS console.

To learn more about outbound service requests, see
[Responding to an AMS-generated service requests](respond-to-sent-generated-sr.md "respond-to-sent-generated-sr.md").

You create an AWS Managed Services (AMS) service request by using the AMS console or, programmatically, by using the Support API.
For details on using the API, see
[Support API](../../../awssupport/latest/user/Welcome.md "../../../awssupport/latest/user/Welcome.md"). For AMS choose the `sentinel-service-request` service code.

After your service request is received by the AMS operations team, it is prioritized according to your service level agreement.
To be kept informed at each step of the service request resolution process, be sure to fill in the **CC Emails** option, and,
if you will connect by federation, log in before following the link in the email AMS sends.

Use the AMS console **Create Service Request** page to perform the following tasks:

- Create and update a service request
- Get a list of, and detailed information about, all of your current service requests
- Narrow your search for service requests by dates and incident identifiers, including requests that have been resolved
- Add communications and file attachments to your requests, and add email recipients for case correspondence
- Resolve service requests
- Rate service request communications

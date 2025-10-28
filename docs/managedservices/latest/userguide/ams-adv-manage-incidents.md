# Incident management

###### Topics

- [What is incident management?](what-is-incident-mgmt.md "what-is-incident-mgmt.md")
- [Incident management service commitments](incident-serv-commits.md "incident-serv-commits.md")
- [Incident management examples](incident-mgmt-examples.md "incident-mgmt-examples.md")
  Incidents are AWS service performance issues that impact your managed environment, as determined by AWS Managed Services (AMS)
  or you. Incidents identified by the AMS team are first received as "events": a change in system state
  captured by monitoring. If a configured threshold is breached, the event triggers an alarm, also called an alert.
  The AMS operations team determines if the event is non-impacting, an incident (a service interruption or degradation),
  or a problem (the underlying root cause of one or more resolved incidents).

The AMS team also receives incidents identified by you through the Support center
or programmatically using the [AWS Support API](../../../awssupport/latest/user/Welcome.md "../../../awssupport/latest/user/Welcome.md") with the service code
`sentinel-report-incident`.

After your incident is received by the AMS operations team, it's reviewed to ensure that the incident is not better classified as a service request.
If it should be classified as a service request, it's immediately reclassified and the AMS service
request team takes over and you are notified. If the incident can be resolved by the receiving
operator, steps are taken to immediately to resolve the incident. AMS operators consult internal documentation for a
resolution and, if needed, escalate the incident to other support resources until the incident is resolved. To be kept informed at each step of
the incident resolution process, be sure to fill in the **CC Emails** option, and, if you'll connect by federation, log in
before following the link in the email that AMS sends. After it is resolved, the AMS operations team documents the incident and resolution for future use.

If an incident resolution requires infrastructure changes, a security review might be needed. Infrastructure changes that might require a security review include
those related to IAM, or resource-based policy, or risk approvals. Those types of incidents require an AMS Operations engineer to create an RFC before making the change,
and your approval to that RFC is required. For example, should the incident resolution
require the update of an IAM policy, there would be an AMS security review and then an AMS Operations engineer would create an RFC with the
Management | Advanced stack components | Identity and Access Management (IAM) | Update entity or policy change type (ct-27tuth19k52b4) and wait for you to
approve the RFC before proceeding.

###### Note

AMS now allows incident resolution that requires infrastructure changes to be made without the additional step of RFC approval. If the changes needed
to resolve the incident do NOT require a security review (the change is not related to IAM, or resource-based policy, or risk approvals), AMS can make the
changes based on your approval received in the incident, without needing separate approval in an RFC.

For definitions of incident management terms, see
[AMS Key Terms](key-terms.md "key-terms.md").

To understand the escalation path of incidents, see
[Getting help](faq-get-help.md "faq-get-help.md").

For a description of AMS response to incidents, see
[AMS incident response](sec-incident-response.md "sec-incident-response.md").

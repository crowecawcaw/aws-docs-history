# Work with contacts

You can enter satellite data, identify antenna locations, communicate, and schedule antenna
time for selected satellites by using the AWS Ground Station console, AWS CLI, or the AWS SDK in the language
of your choice. You can review, cancel, and reschedule contact reservations up to 15 minutes
before contact start\*. In addition, you can view the details of
your reserved minutes pricing plan if you are using the AWS Ground Station reserved minutes pricing model.

AWS Ground Station supports cross-region data delivery. The dataflow endpoint configs that are part of
the mission profile you select determine to which region(s) the data is delivered. For more
information about using cross-region data delivery, see
[Use cross-region data delivery](dataflows.md "dataflows.md").

To schedule contacts, your resources must be configured. If you have not configured your
resources,
see [Get started](getting-started.md "getting-started.md").
When [ReserveContact](../APIReference/API_ReserveContact.md "../APIReference/API_ReserveContact.md")
is called, AWS Ground Station takes a snapshot of the mission profile and config resources
for use during the contact pass. Changes to these resources using the
[UpdateMissionProfile](../APIReference/API_UpdateMissionProfile.md "../APIReference/API_UpdateMissionProfile.md")
and [UpdateConfig](../APIReference/API_UpdateConfig.md "../APIReference/API_UpdateConfig.md")
APIs will not be reflected in contacts reserved prior to the updates. If you need the resource changes applied to an already
scheduled contact, you must first cancel the contact using [CancelContact](../APIReference/API_CancelContact.md "../APIReference/API_CancelContact.md"),
and then reschedule it using [ReserveContact](../APIReference/API_ReserveContact.md "../APIReference/API_ReserveContact.md").

\* Cancelled contacts may incur costs when cancelled too close to the time
of contact. For more information on cancelled contacts see: [Ground Station FAQs](https://aws.amazon.com/ground-station/faqs/ "https://aws.amazon.com/ground-station/faqs/").

###### Topics

- [Understand contact lifecycle](contacts.md "contacts.md")

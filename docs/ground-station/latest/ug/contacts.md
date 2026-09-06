

# Work with contacts
<a name="contacts"></a>

 You can enter satellite data, identify antenna locations, communicate, and schedule antenna time for selected satellites by using the AWS Ground Station console, AWS CLI, or the AWS SDK in the language of your choice. You can review, cancel, and reschedule contact reservations up to 15 minutes before contact start\*. You can also update a contact to specify an ephemeris override — including azimuth/elevation, OEM, or TLE tracking data — or change the target satellite. For more information, see [Update contacts and contact versioning](contacts.versioning.md). In addition, you can view the details of your reserved minutes pricing plan if you are using the AWS Ground Station reserved minutes pricing model. 

 AWS Ground Station supports cross-region data delivery. The dataflow endpoint configs that are part of the mission profile you select determine to which region(s) the data is delivered. For more information about using cross-region data delivery, see [Use cross-region data delivery](dataflows.cross-region-data-delivery.md). 

 To schedule contacts, your resources must be configured. If you have not configured your resources, see [Get started](getting-started.md). When [ ReserveContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ReserveContact.html) is called, AWS Ground Station takes a snapshot of the mission profile and config resources for use throughout the contact's lifecycle. Changes to these resources using the [ UpdateMissionProfile](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateMissionProfile.html) and [UpdateConfig](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateConfig.html) APIs will not be reflected in contacts reserved prior to the updates. If you need the resource changes applied to an already scheduled contact, you must first cancel the contact using [ CancelContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CancelContact.html), and then reschedule it using [ReserveContact](https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ReserveContact.html). 

 \* Cancelled contacts may incur costs when cancelled too close to the time of contact. For more information on cancelled contacts see: [Ground Station FAQs](https://aws.amazon.com/ground-station/faqs/). 

**Topics**
+ [Understand contact lifecycle](contacts.lifecycle.md)
+ [Understand contact billing](contacts.billing.md)
+ [Update contacts and contact versioning](contacts.versioning.md)
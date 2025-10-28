**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Synchronizing customer data across AWS Regions

Regardless of the architecture design that you choose, make sure that your customer data
is synchronized across the AWS Regions that you intend to use. In this case, "customer
data" refers to the contact information for your customers (such as their email addresses,
phone numbers, name, or company). It also refers to the preference data for your
customers—that is, their opt-in and opt-out preferences. Finally, it refers to
information about whether they're able to receive messages from you.

In a resilient architecture, it's important to keep all of this information synchronized
across all of the AWS Regions in which you use Amazon Pinpoint. This chapter contains example
architectures that you can use to keep this information synchronized.

###### Topics in this chapter:

- [Synchronizing endpoint information](customerdata-endpoints.md "customerdata-endpoints.md")
- [Synchronizing event data](customerdata-events.md "customerdata-events.md")

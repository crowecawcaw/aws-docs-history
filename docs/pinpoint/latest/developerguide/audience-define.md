**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Use endpoints to represent your audience in

Amazon Pinpoint

In Amazon Pinpoint, each member of your audience is represented by one or more endpoints. When
you use Amazon Pinpoint to send a message, you direct that message to endpoints that represent
the members of your target audience. Each endpoint definition includes a message
destination—such as a device token, email address, or phone number. It also includes
data about your users and their devices. Before you analyze, segment, or engage your
audience, you must add endpoints to your Amazon Pinpoint project.

As your audience grows and changes, so does your endpoint data. To view the latest
information that Amazon Pinpoint has about your audience, you can look up endpoints individually, or
you can export all of the endpoints from an Amazon Pinpoint project. By looking at your endpoint data, you
can see the following information about your users:

- Their device and platform.
- Their time zone.
- The versions of your app that are installed on their device.
- Their city and country location.
- Other custom attributes and metrics that you record.
  The Amazon Pinpoint console also provides analytics for the demographics and custom attributes that
  are captured in your endpoints.

The following topics explain how to work with endpoints in Amazon Pinpoint.
For information about adding endpoints automatically using your Android, iOS, or
JavaScript client, see [Register Amazon Pinpoint endpoints in your application](integrate-endpoints.md "integrate-endpoints.md").

###### Topics

- [Add endpoints](audience-define-endpoints.md "audience-define-endpoints.md")
- [Associate users with endpoints](audience-define-user.md "audience-define-user.md")
- [Add a batch of endpoints](audience-define-endpoints-batch.md "audience-define-endpoints-batch.md")
- [Import endpoints](audience-define-import.md "audience-define-import.md")
- [Export endpoints from Amazon Pinpoint to Amazon S3 buckets](audience-define-export.md "audience-define-export.md")
- [Look up endpoints in an Amazon Pinpoint project](audience-define-lookup.md "audience-define-lookup.md")
- [List endpoint IDs](audience-define-list-ids.md "audience-define-list-ids.md")
- [Manage endpoint maximum](audience-define-auto-inactive.md "audience-define-auto-inactive.md")
- [Delete endpoints](audience-define-remove.md "audience-define-remove.md")

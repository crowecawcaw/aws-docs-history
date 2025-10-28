**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Chart reference for Amazon Pinpoint analytics

The **Analytics** pages on the Amazon Pinpoint console provide overviews of key
metrics. They also provide dashboards that give details about campaigns, demographics,
funnels, usage, revenue, and more. You can filter many of these dashboards by date for further
analysis. You can also filter some of these dashboards by other attributes, such as event or channel
attributes.

###### Topics

- [Endpoints and users in Amazon Pinpoint analytics](#analytics-endpoints-users "#analytics-endpoints-users")
- [Exporting dashboards](#analytics-exporting "#analytics-exporting")
- [Overview charts](analytics-overview.md "analytics-overview.md")
- [Usage charts](analytics-usage.md "analytics-usage.md")
- [Revenue charts](analytics-revenue.md "analytics-revenue.md")
- [Events charts](analytics-events.md "analytics-events.md")
- [Demographics charts](analytics-demographics.md "analytics-demographics.md")
- [Campaign charts](analytics-campaigns.md "analytics-campaigns.md")
- [Transactional messaging charts](analytics-transactional-messages.md "analytics-transactional-messages.md")

## Endpoints and users in Amazon Pinpoint analytics

Some of the charts and metrics in these dashboards provide data about
_endpoints_. Others provide data about
_users_.

An _endpoint_ is a destination that you can send messages
to—such as a user's mobile device, email address, or phone number. Before you can
see data about endpoints, your application must register endpoints with Amazon Pinpoint, or
you must import your endpoint definitions into Amazon Pinpoint.

A _user_ is an individual who has a unique user ID. This ID can be
associated with one or more endpoints. For example, if a person uses your app on more
than one device, your app could assign that person's user ID to the endpoint for each
device. Before you can see data about users, your application must assign user IDs to
endpoints, or you must import endpoint definitions that include user IDs.

For information about registering endpoints and assigning user IDs within a mobile
app, see [Registering endpoints
in your application](../developerguide/integrate-endpoints.md "../developerguide/integrate-endpoints.md") in the _Amazon Pinpoint Developer Guide_.
For information about registering endpoints and assigning user IDs for other types of
applications, see [Adding endpoints to Amazon Pinpoint](../developerguide/audience-define-endpoints.md "../developerguide/audience-define-endpoints.md") in
the _Amazon Pinpoint Developer Guide_. For information about importing endpoint
definitions, see [Importing segments](segments-importing.md "segments-importing.md").

## Exporting dashboards

You can export data from the dashboards that appear on the
**Analytics** pages of the Amazon Pinpoint console. When you export data from
a dashboard, Amazon Pinpoint creates a .zip file that contains a comma-separated values (.csv)
file with the data for each section of the dashboard. You can open these .csv files by
using any modern spreadsheet or data analysis application.

To export data from a dashboard, choose a date range for the data (and other
attributes, if applicable), and then choose **Download CSV**.

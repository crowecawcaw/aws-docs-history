# Configure Salesforce for AppFabric

Salesforce makes cloud-based software designed to help businesses find more
prospects, close more deals, and wow customers with amazing service.
Salesforce’s Customer 360 offers a complete suite of products, unites
sales, service, marketing, commerce, and IT teams with a single, shared view of customer
information, helping organizations grow relationships with customers and employees
alike.

You can use AWS AppFabric to receive audit logs and user data from Salesforce,
normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the
data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Salesforce](#salesforce-appfabric-support "#salesforce-appfabric-support")
- [Connecting AppFabric to your Salesforce account](#salesforce-appfabric-connecting "#salesforce-appfabric-connecting")

## AppFabric support for Salesforce

AppFabric supports receiving user information and audit logs from
Salesforce.

### Prerequisites

To use AppFabric to transfer audit logs from Salesforce to supported
destinations, you must meet the following requirements:

- You must have a [Performance, Enterprise, or Unlimited edition](https://help.salesforce.com/s/articleView?id=sf.overview_edition.htm&type=5 "https://help.salesforce.com/s/articleView?id=sf.overview_edition.htm&type=5") of
  Salesforce. Contact Salesforce to upgrade
  to one of these editions.
- If you are seeking to have AppFabric transfer hourly event log files with
  [full set of log events](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm") from Salesforce, you must
  subscribe to Event Monitoring as part of the [Shield Features](https://www.salesforce.com/editions-pricing/platform/shield/ "https://www.salesforce.com/editions-pricing/platform/shield/") of Salesforce. Otherwise, AppFabric
  will transfer limited events (i.e. Login, Logout, InsecureExternalAssets,
  API Total Usage, CORS Violation, and HostnameRedirects ELF Events) from
  Salesforce’s standard daily log file. You can check if
  your Salesforce account is already subscribed to Shield
  Features by going to **Setup** > **Event
  Manager**. If you see 19 or more events listed, your account is
  subscribed to the Event Monitoring. If you do not have Event Monitoring, you
  can purchase a subscription to this add-on by contacting
  Salesforce.
- You need to [opt-in for Event Log File generation](https://help.salesforce.com/s/articleView?id=release-notes.rn_security_em_generate_event_log_files.htm&release=244&type=5 "https://help.salesforce.com/s/articleView?id=release-notes.rn_security_em_generate_event_log_files.htm&release=244&type=5") in the
  Salesforce settings.
- You should use the System Administrator Profile to create an OAuth
  application and log in with the same credentials for AppFabric.

###### Note

The API Total Usage, CORS Violation Record, Hostname Redirects, Insecure
External Assets, Login, and Logout events are available at no additional cost in
supported editions of Salesforce. Contact
Salesforce to purchase the remaining event types. For more
information about Salesforce event types, see [EventLogFile Supported Event Types](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_supportedeventtypes.htm") on the Salesforce
website.

AppFabric can support up to 100,000 events per event type per log file instance
(daily or hourly, depending on Event Monitoring add-on subscription). A log file
exceeding the threshold might cause the entire log file to be excluded from
ingestion.

### Rate limit considerations

Salesforce imposes rate limits on the Salesforce
API. For more information about the Salesforce API rate limits, see
[API Request Limits and Allocations](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm "https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm") on the Salesforce
website. If the combination of AppFabric and your existing Salesforce API
applications exceed Salesforce’s limits, audit logs appearing in
AppFabric might be delayed.

### Data delay considerations

You might see up to 6 hours delay on daily log file or up to 29 hours delay on
hourly log file for an audit event to be delivered to your destination. This is due
to delay in audit events made available by the application as well as due to
precautions taken to reduce data loss. However, this might be customizable at an
account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Salesforce account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Salesforce. To find the information required to authorize
Salesforce with AppFabric, use the following steps.

### Create an OAuth application

AppFabric integrates with the Salesforce using OAuth. To create an
OAuth application in Salesforce, use the following steps:

1. [Login to your
   Salesforce account.](https://login.salesforce.com "https://login.salesforce.com")
2. Go to the **Setup page** as described in the [Salesforce documentation](https://help.salesforce.com/s/articleView?id=sf.basics_nav_setup.htm&type=5 "https://help.salesforce.com/s/articleView?id=sf.basics_nav_setup.htm&type=5").
3. Search for **App Manager** in the quick find.
4. Choose **New Connected App**.
5. Enter the required information into the form fields.
6. Choose **Enable OAuth settings**.
7. Be sure to **turn off** the following options:
   - Require Proof Key for Code Exchange (PKCE) Extension For Supported
     Authorization Flows
   - Require secret for Web Server Flow
   - Require secret for Refresh Token Flow
   - Enable Refresh Token Rotation

8. Enter a URL with the following format in the **Callback
   URL** text box, and choose **Save**
   changes.

```
https://`<region>`.console.aws.amazon.com/appfabric/oauth2
```

In this URL, `<region>` is the code for the
AWS Region in which you configured your AppFabric app bundle. For example, the
code for the US East (N. Virginia) Region is `us-east-1`.
For that Region, the redirect URL is
`https://`us-east-1`.console.aws.amazon.com/appfabric/oauth2`. 9. Fill in the scopes as needed (described in the following [Required scopes](#salesforce-required-scopes "#salesforce-required-scopes") section). All other fields
can be left with their default values. 10. Choose **Save**. 11. Complete the following steps to verify the refresh token policy for the
new OAuth app:

    1. On the **Setup page**, enter **Connected
     Apps** into the Quick Find text box, and then choose
     **Manage Connected Apps**.
    2. Choose **Edit** next to the newly created
     app.
    3. Make sure that the **Refresh token is valid until
     revoked** option is selected.
    4. Save your changes.

12. Complete the following steps to verify that audit logs are being
    generated:
    1.  On the **Setup page**, enter **Event Log
        File** into the Quick Find text box, and then choose
        **Event Log File Browser**.
    2.  Confirm that event logs are listed in the **Event Log File
        Browser**.

13. Navigate to the created app, and choose **View** from the
    drop-down.
14. Choose **Manage Consumer Details**.

You will be redirected to a new tab where you will need to verify your
identity. On that tab, make a note of the **Consumer Key**
and **Consumer Secret** values. You will need these later
to sign in.

### Required scopes

You must add the following scopes to your Salesforce OAuth
application:

- Manage user data via APIs (`API`).
- Perform request at anytime (`refresh_token` and
  `offline_access`).

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric is the subdomain of
your Salesforce
**My Domain**. You can find your **My Domain**
subdomain in your browser's address bar between `https://` and
`.my.salesforce.com`.

To find your Salesforce
**My Domain**, use the following instructions from the
Salesforce home screen.

1. Go to the **Setup page** as described in the [Salesforce documentation](https://help.salesforce.com/s/articleView?id=sf.basics_nav_setup.htm&type=5 "https://help.salesforce.com/s/articleView?id=sf.basics_nav_setup.htm&type=5").
2. Search for **Company Settings** in the quick find,
   and choose **My Domain** in the results.

#### Tenant name

Enter a name that identifies this unique Salesforce
organization. AppFabric uses the tenant name to label the app authorizations and any
ingestions created from the app authorization.

#### Client ID

AppFabric will request a client ID. To find your client ID in
Salesforce, use the following steps:

1. Navigate to the **Setup** page.
2. Choose **Setup**, and then choose **App
   Manager**.
3. Choose the created app, and choose **View** from
   drop-down menu.
4. Choose **Manage Consumer Details**. You will be
   redirected to a new tab.
5. Verify your identity, and then look for the **Consumer
   Key** value.
6. Enter the **Consumer Key** into the client ID field
   in AppFabric.

#### Client secret

AppFabric will request your client secret. The **Client secret**
in AppFabric is the **Consumer Secret** in
Salesforce. To find your Secret in Salesforce,
use the following steps:

1. Navigate to the **Setup** page.
2. Choose **Setup**, and then choose **App
   Manager**.
3. Choose the created app, and choose **View** from
   drop-down menu.
4. Choose **Manage Consumer Details**. You will be
   redirected to a new tab.
5. Verify your identity, and then look for the **Consumer
   Secret** value.
6. Enter the **Consumer Secret** into the client secret
   field in AppFabric.

#### Approve authorization

After creating the app authorization in AppFabric, you will receive a pop-up
window from Salesforce to approve the authorization. At the
approval page, make sure to use the Salesforce System
Administrator Role or a Salesforce user that have View Event Log
Files and API Enabled user permissions while authorizing. Choose
**Allow** to approve the AppFabric authorization.

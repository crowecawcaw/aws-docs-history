# Configure Asana for AppFabric

Asana is a work management platform that helps individuals, teams, and
organizations orchestrate work, from daily tasks to cross-functional strategic initiatives.
It provides a living system of clarity where everyone can communicate, collaborate, and
coordinate work. With Asana, teams integrate critical business tools into one
place so work moves forward no matter where it happens.

You can use AWS AppFabric for security to audit logs and user data from Asana,
normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the
data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for Asana](#asana-appfabric-support "#asana-appfabric-support")
- [Connecting AppFabric to your Asana account](#asana-appfabric-connecting "#asana-appfabric-connecting")

## AppFabric support for Asana

AppFabric supports receiving user information and audit logs from
Asana.

### Prerequisites

To use AppFabric to transfer audit logs from Asana to supported
destinations, you must meet the following requirements:

- You must have an **Enterprise account** with
  Asana. For more information about creating or upgrading
  to an Asana Enterprise account, see [Asana
  Enterprise](https://asana.com/enterprise "https://asana.com/enterprise") on the Asana website.
- You must have a user with the **Super Admin**
  role in your Asana account. For more information about roles,
  see [Admin and super admin roles in Asana](https://help.asana.com/hc/en-us/articles/14141552580635-Admin-and-super-admin-roles-in-Asana "https://help.asana.com/hc/en-us/articles/14141552580635-Admin-and-super-admin-roles-in-Asana") on the
  Asana website.

### Rate limit considerations

Asana imposes rate limits on the Asana API. For more
information about the Asana API rate limits, see [Rate limits](https://developers.asana.com/docs/rate-limits "https://developers.asana.com/docs/rate-limits") on the
_Asana Developers Guide_ website. If the
combination of AppFabric and your existing Asana applications exceed the
limit, audit logs appearing in AppFabric might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Asana account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Asana. To find the information required to authorize
Asana with AppFabric, use the following steps.

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric is called the domain
ID in Asana. To find the domain ID, use the following
instructions from the Asana home screen:

1. Choose your account profile picture and select **Admin
   Console**.
2. Then select **Settings**.
3. Scroll to **Domain Settings**.
4. Enter the domain ID from this section into the AppFabric Tenant ID
   configuration.

#### Tenant name

Enter a name that identifies this unique Asana organization.
AppFabric uses the tenant name to label the app authorizations and any ingestions
created from the app authorization.

#### Service account token

You must have a service account token from an Asana service
account to enter into the AppFabric Asana app authorization. If you
don't have a service account token, use the following instructions:

1. To create a service account, follow the instructions in [Service Accounts](https://help.asana.com/hc/en-us/articles/14217496838427-Service-Accounts "https://help.asana.com/hc/en-us/articles/14217496838427-Service-Accounts") on the _Asana
   Guide_ website.
2. Copy and save the token from the bottom of the **Add service
   account** page the first time you view the **Add
   service account** page.
3. If you close the **Add service account** page before
   saving the token, you must edit your service account, generate a new
   token, and save it.

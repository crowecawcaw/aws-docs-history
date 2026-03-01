# Configure Singularity Cloud for AppFabric

The Singularity Cloud platform protects your enterprise from threats of all
categories, at all stages. Its patented artificial intelligence extends security from known
signatures and patterns to the most sophisticated attacks, such as zero-day and
ransomware.

You can use AWS AppFabric to receive audit logs and user data from Singularity
Cloud, normalize the data into Open Cybersecurity Schema Framework (OCSF)
format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

###### Note

Singularity Cloud documentation can be access only after you sign in to
your Singularity Cloud account. Therefore, we cannot link directly to the
Singularity Cloud documentation from this document.

###### Topics

- [AppFabric support for Singularity Cloud](#singularity-cloud-appfabric-support "#singularity-cloud-appfabric-support")
- [Connecting AppFabric to your Singularity Cloud account](#singularity-cloud-appfabric-connecting "#singularity-cloud-appfabric-connecting")

## AppFabric support for Singularity Cloud

AppFabric supports receiving user information and audit logs from Singularity
Cloud.

### Prerequisites

To use AppFabric to transfer audit logs from Singularity Cloud to
supported destinations, you must have an administrator role in your
Singularity Cloud account. For more information about the
Singularity Cloud API rate limits, sign in to your Singularity
Cloud account, browse the documentation section, and search for
**roles**.

### Rate limit considerations

Singularity Cloud imposes rate limits on the Singularity
Cloud API. For more information about the Singularity
Cloud API rate limits, sign in to your Singularity Cloud account, browse
the documentation section, and search for **API rate
limits**.

### Data delay considerations

You might see up to a 30 minute delay an audit event to be delivered to your
destination. This is due to delay in audit events made available by the application
as well as due to precautions taken to reduce data loss. However, this might be
customizable at an account-level. For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your Singularity Cloud account

After you create your app bundle within the AppFabric service, you must authorize AppFabric
with Singularity Cloud. To find the information required to authorize
Singularity Cloud with AppFabric, use the following steps.

### Create an API token for Singularity Cloud

Complete the following procedure to create an API token that is associated to a
service user. The API token will not be linked to a specific console user or email
address.

###### Note

Create a new user or copy the service user to get a new API token before or
after a service user API token expires.

1. Sign in to your Singularity Cloud account.
2. In the **Settings** toolbar, choose
   **Users**, and then choose **Service
   Users**.
3. Choose **Actions**, and then select **Create New
   Service User**.
4. In **Create New Service User** page, enter a name,
   description, and expiration date for the service user.
5. Choose **Next**.
6. In the **Select Scope of Access** section, select the
   scope.
   - Select **Account** for the access level.
   - Select the account for which you want to get audit logs.

7. Choose **Create User**.

The API token is generated. A window opens and shows the token string with
a message indicating this is the last time you can view the token. 8. (Optional) Choose **Copy API Token** and store it in a
safe location. 9. Choose **Close**.

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. The tenant ID in AppFabric will be the
subdomain of the Sentinel One website address where you sign in
to the service. For example, if you sign in to your Singularity
Cloud account at the `example-company-1.sentinelone.net`
address, your tenant ID is `example-company-1`.

#### Tenant name

Enter a name that identifies this unique Singularity Cloud
organization. AppFabric uses the tenant name to label the app authorizations and any
ingestions created from the app authorization.

#### Service account token

Use the token that you generated using the steps in the [Create an API token for Singularity Cloud](#singularity-cloud-api-token "#singularity-cloud-api-token") section of this guide. If you
misplace or are unable to locate the token, you can generate a new one by
following the same steps again.

###### Note

If a new API token is generated in the **Singularity
Cloud** console while AppFabric is ingesting the audit logs, the
ingestions will stop. If this happens you will need to update the app
authorization with a new API token to resume audit log ingestion.

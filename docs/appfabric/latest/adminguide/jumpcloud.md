# Configure JumpCloud for AppFabric

JumpCloud Inc. is an American enterprise software company that provides a cloud-based
directory platform for identity management. It centralizes and simplifies identity management,
allowing users to securely access their systems, apps, networks, and file servers with a single
set of credentials, regardless of platform, protocol, provider, or location.

You can use AWS AppFabric to receive audit logs and user data from JumpCloud, normalize the data
into Open Cybersecurity Schema Framework (OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3)
bucket or an Amazon Data Firehose stream.

###### Topics

- [AppFabric support for JumpCloud](#jumpcloud-appfabric-support "#jumpcloud-appfabric-support")
- [Connecting AppFabric to your
  JumpCloud account](#jumpcloud-appfabric-connecting "#jumpcloud-appfabric-connecting")

## AppFabric support for JumpCloud

AppFabric supports receiving user information and audit logs from
JumpCloud.

### Prerequisites

To use AppFabric to transfer audit logs from JumpCloud to supported
destinations, you must meet the following requirements:

- You must have an active paid JumpCloud subscription plan. For more
  information, see [Select a package that's
  right for you](https://jumpcloud.com/pricing "https://jumpcloud.com/pricing") on the JumpCloud website.
- You must have the "Admins with Billing" role.

### Rate limit considerations

JumpCloud doesn't publish rate limits. You must create a support case or
reach out to your JumpCloud Customer team. If the combination of AppFabric and your
existing JumpCloud API applications exceed JumpCloud's limits,
audit logs appearing in AppFabric might be delayed.

### Data delay considerations

You might see up to a 30-minute delay for an audit event to be delivered to your
destination. This is due to delays in audit events made available by the application, and due to
precautions taken to reduce data loss. However, this might be customizable at an account-level.
For assistance, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Connecting AppFabric to your

JumpCloud account

After you create your app bundle within the AppFabric service, you must authorize AppFabric with
JumpCloud. To find the information required to authorize JumpCloud
with AppFabric, follow the steps in the next section.

### Create an Organization token from the

JumpCloud account

AppFabric uses an API key to integrate with JumpCloud To create an API key in
JumpCloud, follow these steps:.

1. [Sign in to your
   JumpCloud](https://console.jumpcloud.com/login/admin "https://console.jumpcloud.com/login/admin") account as an administrator.
2. In the Admin Portal, choose your account initials, located n the top-right, and choose
   **My API Key** from the menu.
3. Choose **Generate New API Key**, or select an existing key.

###### Note

JumpCloud only allows one active API key. Generating a new API key will
revoke access to the current API key. This will render all calls using the previous API key
inaccessible. You will have to update any existing integrations that use the previous API key
with the new key value.

### App authorizations

#### Tenant ID

AppFabric will request your tenant ID. Here “Organization Id” will be the Tenant Id. To find
the "Organization Id", follow these steps.

1. Sign in to your JumpCloud account.
2. In the navigation pane, choose **Settings**, then
   **Organization Profile**, then **General**.
3. Choose the "eye" icon to remove the obscured view.
4. Choose the "double-page" icon to copy the ID.

#### Tenant name

Enter a name that identifies this unique JumpCloud organization. AppFabric uses
the tenant name to label the app authorizations and any ingestions created from the app
authorization.

#### Service account token

AppFabric will request your service account token. In AppFabric, this is the organization API
token that you created in [Create an Organization token from the
JumpCloud account](#jumpcloud-appfabric-access-token "#jumpcloud-appfabric-access-token"), earlier in this topic.

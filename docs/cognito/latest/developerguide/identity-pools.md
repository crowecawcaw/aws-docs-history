# Identity pools console overview

Amazon Cognito identity pools provide temporary AWS credentials for users who are guests
(unauthenticated) and for users who have been authenticated and received a token. An identity
pool is a store of user identifiers linked to your external identity providers.

One way to understand the features and options of identity pools is to create one in the
Amazon Cognito console. You can explore the effect of different settings on authentication flows,
role-based and attribute-based access control, and guest access. From there, you can proceed
to later chapters in this guide and add the appropriate components to your application so that
you can implement identity pool authentication.

###### Topics

- [Create an identity pool](#identity-pools-create "#identity-pools-create")
- [User IAM roles](#user-iam-roles "#user-iam-roles")
- [Authenticated and
  unauthenticated identities](#authenticated-and-unauthenticated-identities "#authenticated-and-unauthenticated-identities")
- [Activate or deactivate guest
  access](#enable-or-disable-unauthenticated-identities "#enable-or-disable-unauthenticated-identities")
- [Change the role
  associated with an identity type](#change-the-role-associated-with-an-identity-type "#change-the-role-associated-with-an-identity-type")
- [Edit identity providers](#enable-or-edit-authentication-providers "#enable-or-edit-authentication-providers")
- [Delete an identity pool](#delete-an-identity-pool "#delete-an-identity-pool")
- [Delete an identity from an
  identity pool](#delete-an-identity-from-an-identity-pool "#delete-an-identity-from-an-identity-pool")
- [Using Amazon Cognito Sync with identity pools](#identity-pools-sync "#identity-pools-sync")

## Create an identity pool

###### To create a new identity pool in the console

1. Sign in to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home")
   and select **Identity pools**.
2. Choose **Create identity pool**.
3. In **Configure identity pool trust**, choose to set up your
   identity pool for **Authenticated access**, **Guest
   access**, or both.
   1. If you chose **Authenticated access**, select one or more
      **Identity types** that you want to set as the source of
      authenticated identities in your identity pool. If you configure a **Custom
      developer provider**, you can't modify or delete it after you create your
      identity pool.

4. In **Configure permissions**, choose a default IAM role for
   authenticated or guest users in your identity pool.
   1. Choose to **Create a new IAM role** if you want Amazon Cognito to
      create a new role for you with basic permissions and a trust relationship with your
      identity pool. Enter an **IAM role name** to identify your new
      role, for example `myidentitypool_authenticatedrole`. Select
      **View policy document** to review the permissions that Amazon Cognito
      will assign to your new IAM role.
   2. You can choose to **Use an existing IAM role** if you already
      have a role in your AWS account that you want to use. You must configure your
      IAM role trust policy to include `cognito-identity.amazonaws.com`.
      Configure your role trust policy to only allow Amazon Cognito to assume the role when it
      presents evidence that the request originated from an authenticated user in your
      specific identity pool. For more information, see [Role trust and permissions](iam-roles.md#role-trust-and-permissions "iam-roles.md#role-trust-and-permissions").

5. In **Connect identity providers**, enter the details of the
   identity providers (IdPs) that you chose in **Configure identity pool
   trust**. You might be asked to provide OAuth app client information, choose a
   Amazon Cognito user pool, choose an IAM IdP, or enter a custom identifier for a developer
   provider.
   1. Choose the **Role settings** for each IdP. You can assign users
      from that IdP the **Default role** that you set up when you
      configured your **Authenticated role**, or you can **Choose
      role with rules**. With a Amazon Cognito user pool IdP, you can also
      **Choose role with preferred_role in tokens**. For more
      information about the `cognito:preferred_role` claim, see [Assigning precedence values to
      groups](cognito-user-pools-user-groups.md#assigning-precedence-values-to-groups "cognito-user-pools-user-groups.md#assigning-precedence-values-to-groups").
      1. If you chose **Choose role with rules**, enter the source
         **Claim** from your user's authentication, the
         **Operator** that you want to compare the claim by, the
         **Value** that will cause a match to this role choice, and
         the **Role** that you want to assign when the **Role
         assignment** matches. Select **Add another** to
         create an additional rule based on a different condition.
      2. Choose a **Role resolution**. When your user's claims don't
         match your rules, you can deny credentials or issue credentials for your
         **Authenticated role**.

   2. Configure **Attributes for access control** for each IdP.
      Attributes for access control maps user claims to [principal tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md") that Amazon Cognito
      applies to their temporary session. You can build IAM policies to filter user
      access based on the tags that you apply to their session.
      1. To apply no principal tags, choose **Inactive**.
      2. To apply principal tags based on `sub` and `aud`
         claims, choose **Use default mappings**.
      3. To create your own custom schema of attributes to principal tags, choose
         **Use custom mappings**. Then enter a **Tag
         key** that you want to source from each **Claim**
         that you want to represent in a tag.

6. In **Configure properties**, enter a **Name**
   under **Identity pool name**.
7. Under **Basic (classic) authentication**, choose whether you want
   to **Activate basic flow**. With the basic flow active, you can bypass
   the role selections you made for your IdPs and call [AssumeRoleWithWebIdentity](../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md "../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md") directly. For more information, see [Identity pools authentication flow](authentication-flow.md "authentication-flow.md").
8. Under **Tags**, choose **Add tag** if you want to
   apply [tags](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md")
   to your identity pool.
9. In **Review and create**, confirm the selections that you made for
   your new identity pool. Select **Edit** to return to the wizard and
   change any settings. When you're done, select **Create identity
   pool**.

## User IAM roles

An IAM role defines the permissions for your users to access AWS resources, like
[Amazon Cognito Sync](cognito-sync.md "cognito-sync.md"). Users of your application
will assume the roles you create. You can specify different roles for authenticated and
unauthenticated users. To learn more about IAM roles, see [IAM roles](iam-roles.md "iam-roles.md").

## Authenticated and

unauthenticated identities

Amazon Cognito identity pools support both authenticated and unauthenticated identities.
Authenticated identities belong to users who are authenticated by any supported identity
provider. Unauthenticated identities typically belong to guest users.

- To configure authenticated identities with a public login provider, see [Identity pools third-party identity
  providers](external-identity-providers.md "external-identity-providers.md").
- To configure your own backend authentication process, see [Developer-authenticated identities](developer-authenticated-identities.md "developer-authenticated-identities.md").

## Activate or deactivate guest

access

Amazon Cognito identity pools guest access (unauthenticated identities) provides a unique
identifier and AWS credentials for users who do not authenticate with an identity
provider. If your application allows users who do not log in, you can activate access for
unauthenticated identities. To learn more, see [Getting started with Amazon Cognito identity
pools](getting-started-with-identity-pools.md "getting-started-with-identity-pools.md").

###### To update guest

access in an identity pool

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **User access** tab.
3. Locate **Guest access**. In an identity pool that doesn't currently
   support guest access, **Status** is
   **Inactive**.
   1. If **Guest access** is **Active** and you want
      to deactivate it, select **Deactivate**.
   2. If **Guest access** is **Inactive** and you
      want to activate it, select **Edit**.
      1. Choose a default IAM role for guest users in your identity pool.
         1. Choose to **Create a new IAM role** if you want Amazon Cognito
            to create a new role for you with basic permissions and a trust relationship
            with your identity pool. Enter an **IAM role name** to
            identify your new role, for example
            `myidentitypool_authenticatedrole`. Select **View
            policy document** to review the permissions that Amazon Cognito will
            assign to your new IAM role.
         2. You can choose to **Use an existing IAM role** if you
            already have a role in your AWS account that you want to use. You must
            configure your IAM role trust policy to include
            `cognito-identity.amazonaws.com`. Configure your role trust
            policy to only allow Amazon Cognito to assume the role when it presents evidence that
            the request originated from an authenticated user in your specific identity
            pool. For more information, see [Role trust and permissions](iam-roles.md#role-trust-and-permissions "iam-roles.md#role-trust-and-permissions").
         3. Select **Save changes**.
         4. To activate guest access, select **Activate** in the
            **User access** tab.

## Change the role

associated with an identity type

Every identity in your identity pool is either authenticated or unauthenticated.
Authenticated identities belong to users who are authenticated by a public login provider
(Amazon Cognito user pools, Login with Amazon, Sign in with Apple, Facebook, Google, SAML, or any
OpenID Connect Providers) or a developer provider (your own backend authentication process).
Unauthenticated identities typically belong to guest users.

For each identity type, there is an assigned role. This role has a policy attached to it
that dictates which AWS services that role can access. When Amazon Cognito receives a request, the
service determines the identity type, determines the role assigned to that identity type,
and uses the policy attached to that role to respond. By modifying a policy or assigning a
different role to an identity type, you can control which AWS services an identity type
can access. To view or modify the policies associated with the roles in your identity pool,
see the [AWS IAM Console](https://console.aws.amazon.com/iam/home "https://console.aws.amazon.com/iam/home").

###### To change the identity pool default authenticated or unauthenticated role

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **User access** tab.
3. Locate **Guest access** or **Authenticated
   access**. In an identity pool that isn't currently configured for that access
   type, **Status** is **Inactive**. Select
   **Edit**.
4. Choose a default IAM role for guest or authenticated users in your identity
   pool.
   1. Choose to **Create a new IAM role** if you want Amazon Cognito to
      create a new role for you with basic permissions and a trust relationship with your
      identity pool. Enter an **IAM role name** to identify your new
      role, for example `myidentitypool_authenticatedrole`. Select
      **View policy document** to review the permissions that Amazon Cognito
      will assign to your new IAM role.
   2. You can choose to **Use an existing IAM role** if you already
      have a role in your AWS account that you want to use. You must configure your
      IAM role trust policy to include `cognito-identity.amazonaws.com`.
      Configure your role trust policy to only allow Amazon Cognito to assume the role when it
      presents evidence that the request originated from an authenticated user in your
      specific identity pool. For more information, see [Role trust and permissions](iam-roles.md#role-trust-and-permissions "iam-roles.md#role-trust-and-permissions").

5. Select **Save changes**.

## Edit identity providers

If you allow your users to authenticate using consumer identity providers (for example,
Amazon Cognito user pools, Login with Amazon, Sign in with Apple, Facebook, or Google), you can
specify your application identifiers in the Amazon Cognito identity pools (federated identities)
console. This associates the application ID (provided by the public login provider) with
your identity pool.

You can also configure authentication rules for each provider from this page. Each
provider allows up to 25 rules. The rules are applied in the order you save for each
provider. For more information, see [Using role-based access control](role-based-access-control.md "role-based-access-control.md").

###### Warning

Changing the linked IdP application ID in your identity pool prevents existing users
from authenticating with that identity pool. For more information, see [Identity pools third-party identity
providers](external-identity-providers.md "external-identity-providers.md").

###### To update an identity pool identity provider (IdP)

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **User access** tab.
3. Locate **Identity providers**. Choose the identity provider that
   you want to edit. If you want to add a new IdP, select **Add identity
   provider**.
   1. If you chose **Add identity provider**, choose one of the
      **Identity types** that you want to add.

4. To change the application ID, choose **Edit** in **Identity
   provider information**.
5. To change the role that Amazon Cognito requests when it issues credentials to users who have
   authenticated with this provider, choose **Edit** in **Role
   settings**.
   1. You can assign users from that IdP the **Default role** that
      you set up when you configured your **Authenticated role**, or you
      can **Choose role with rules**. With a Amazon Cognito user pool IdP, you can
      also **Choose role with preferred_role in tokens**. For more
      information about the `cognito:preferred_role` claim, see [Assigning precedence values to
      groups](cognito-user-pools-user-groups.md#assigning-precedence-values-to-groups "cognito-user-pools-user-groups.md#assigning-precedence-values-to-groups").
      1. If you chose **Choose role with rules**, enter the source
         **Claim** from your user's authentication, the
         **Operator** that you want to compare the claim by, the
         **Value** that will cause a match to this role choice, and
         the **Role** that you want to assign when the **Role
         assignment** matches. Select **Add another** to
         create an additional rule based on a different condition.
      2. Choose a **Role resolution**. When your user's claims don't
         match your rules, you can deny credentials or issue credentials for your
         **Authenticated role**.

6. To change the principal tags that Amazon Cognito assigns when it issues credentials to users
   who have authenticated with this provider, choose **Edit** in
   **Attributes for access control**.
   1. To apply no principal tags, choose **Inactive**.
   2. To apply principal tags based on `sub` and `aud` claims,
      choose **Use default mappings**.
   3. To create your own custom schema of attributes to principal tags, choose
      **Use custom mappings**. Then enter a **Tag
      key** that you want to source from each **Claim** that
      you want to represent in a tag.

7. Select **Save changes**.

## Delete an identity pool

You can't undo identity pool deletion. After you delete an identity pool, all apps and
users that depend on it stop working.

###### To delete an identity pool

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select the radio button
   next to the identity pool that you want to delete.
2. Select **Delete**.
3. Enter or paste the name of your identity pool and select
   **Delete**.

###### Warning

When you select the Delete button, you will permanently delete your identity pool and
all the user data it contains. Deleting an identity pool will cause applications and other
services using the identity pool to stop working.

## Delete an identity from an

identity pool

When you delete an identity from an identity pool, you remove the identifying
information that Amazon Cognito has stored for that federated user. When your user requests
credentials again, they receive a new identity ID if your identity pool still trusts their
identity provider. You can't undo this operation.

###### To delete an identity

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **Identity browser** tab.
3. Select the check boxes next to the identities that you want to delete and choose
   **Delete**. Confirm that you want to delete the identities and choose
   **Delete**.

## Using Amazon Cognito Sync with identity pools

Amazon Cognito Sync is an AWS service and client library that makes it possible to sync
application-related user data across devices. Amazon Cognito Sync can synchronize user profile data
across mobile devices and the web without using your own backend. The client libraries cache
data locally so that your app can read and write data regardless of device connectivity
status. When the device is online, you can synchronize data. If you set up push sync, you
can notify other devices immediately that an update is available.

### Managing

datasets

If you have implemented Amazon Cognito Sync functionality in your application, the Amazon Cognito
identity pools console enables you to manually create and delete datasets and records for
individual identities. Any change you make to an identity's dataset or records in the
Amazon Cognito identity pools console isn't saved until you select **Synchronize**
in the console. The change isn't visible to the end user until the identity calls
**Synchronize**. The data being synchronized from other devices for
individual identities is visible once you refresh the list datasets page for a particular
identity.

#### Create a dataset for an

identity

Amazon Cognito Sync associates a dataset with one identity. You can populate your dataset with
identifying information about the user that the identity represents, then sync that
information to all of your user's devices.

###### To add a dataset and dataset records to an identity

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **Identity browser** tab.
3. Select the identity that you want to edit.
4. In **Datasets**, choose **Create
   dataset**.
5. Enter a **Dataset name** and select **Create
   dataset**.
6. If you want to add records to your dataset, choose your dataset from identity
   details. In **Records**, select **Create
   record**.
7. Enter a **Key** and **Value** for your record.
   Choose **Confirm**. Repeat to add more records.

#### Delete a dataset

associated with an identity

###### To delete a dataset and its records from an identity

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **Identity browser** tab.
3. Select the identity that contains the dataset that you want to delete.
4. In **Datasets**, choose the radio button next to the dataset
   that you want to delete.
5. Select **Delete**. Review your choice and select
   **Delete** again.

### Bulk publish data

Bulk publish can be used to export data already stored in your Amazon Cognito Sync store to a
Amazon Kinesis stream. For instructions on how to bulk publish all of your streams, see [Implementing Amazon Cognito Sync streams](cognito-streams.md "cognito-streams.md").

### Activate push synchronization

Amazon Cognito automatically tracks the association between identity and devices. Using the
push sync feature, you can make sure that every instance of a given identity is notified
when identity data changes. Push sync makes it so that, whenever the dataset changes for
an identity, all devices associated with that identity receive a silent push notification
informing them of the change.

You can activate push sync in the Amazon Cognito console.

###### To activate push synchronization

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **Identity pool properties** tab.
3. In **Push synchronization**, select
   **Edit**
4. Select **Activate push synchronization with your identity
   pool**.
5. Choose one of the Amazon Simple Notification Service (Amazon SNS) **Platform applications**
   that you created in the current AWS Region. Amazon Cognito publishes push notifications to
   your platform application. Select **Create platform application** to
   navigate to the Amazon SNS console and create a new one.
6. To publish to your platform application, Amazon Cognito assumes an IAM role in your
   AWS account. Choose to **Create a new IAM role** if you want
   Amazon Cognito to create a new role for you with basic permissions and a trust relationship
   with your identity pool. Enter an **IAM role name** to identify
   your new role, for example `myidentitypool_authenticatedrole`. Select
   **View policy document** to review the permissions that Amazon Cognito will
   assign to your new IAM role.
7. You can choose to **Use an existing IAM role** if you already
   have a role in your AWS account that you want to use. You must configure your IAM
   role trust policy to include `cognito-identity.amazonaws.com`. Configure
   your role trust policy to only allow Amazon Cognito to assume the role when it presents
   evidence that the request originated from an authenticated user in your specific
   identity pool. For more information, see [Role trust and permissions](iam-roles.md#role-trust-and-permissions "iam-roles.md#role-trust-and-permissions").
8. Select **Save changes**.

### Set up Amazon Cognito Streams

Amazon Cognito Streams gives developers control and insight into their data stored in
Amazon Cognito Sync. Developers can now configure a Kinesis stream to receive events as data. Amazon Cognito can
push each dataset change to a Kinesis stream you own in real time. For instructions on how to
set up Amazon Cognito Streams in the Amazon Cognito console, see [Implementing Amazon Cognito Sync streams](cognito-streams.md "cognito-streams.md").

### Set up Amazon Cognito Events

Amazon Cognito Events allows you to run an AWS Lambda function in response to important events
in Amazon Cognito Sync. Amazon Cognito Sync raises the Sync Trigger event when a dataset is synchronized. You
can use the Sync Trigger event to take an action when a user updates data. For
instructions on setting up Amazon Cognito Events from the console, see [Customizing workflows with Amazon Cognito Events](cognito-events.md "cognito-events.md").

To learn more about AWS Lambda, see [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/").

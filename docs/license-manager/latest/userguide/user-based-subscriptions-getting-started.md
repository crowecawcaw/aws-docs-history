# Get started with user-based

subscriptions in License Manager

The following steps detail how you can get started with using user-based subscriptions.
These steps assume you have already implemented the required prerequisites. For more
information, see the [Prerequisites to create
user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-prerequisites "user-based-subscriptions.md#usubs-prerequisites").

###### Steps

- [Step 1: Subscribe to a
  product](user-based-subscriptions-getting-started.md#user-based-subscriptions-subscribe-products "user-based-subscriptions-getting-started.md#user-based-subscriptions-subscribe-products")
- [Step 2: Register your
  Active Directory in License Manager](user-based-subscriptions-getting-started.md#user-based-subscriptions-configure-ad "user-based-subscriptions-getting-started.md#user-based-subscriptions-configure-ad")
- [Step 3: Configure RDS license
  server](user-based-subscriptions-getting-started.md#usubs-configure-rds "user-based-subscriptions-getting-started.md#usubs-configure-rds")
- [Step 4: Launch an instance to
  provide user-based subscriptions](user-based-subscriptions-getting-started.md#user-based-subscriptions-launch-instance "user-based-subscriptions-getting-started.md#user-based-subscriptions-launch-instance")
- [Step 5: Associate users to a user-based
  subscription instance](user-based-subscriptions-getting-started.md#user-based-subscriptions-associate-users "user-based-subscriptions-getting-started.md#user-based-subscriptions-associate-users")

## Step 1: Subscribe to a

product

Microsoft products like Office or Visual Studio require an active subscription before
you can associate Active Directory users to an instance that includes those products.
Subscription products that display a **Subscribe in AWS Marketplace** button in the **Marketplace Subscription Status** column are not subscribed yet.

When you subscribe to a Microsoft user-based subscription product from the AWS Marketplace, License Manager
automatically adds a subscription to Microsoft Remote Desktop Services (RDS) for your
account, if you don't already have one. RDS is required in order to remotely access the
graphical desktops and subscription based Windows applications on EC2 instances launched from
license-included AMIs.

You can subscribe to your products directly on the AWS Marketplace using the following
links:

- [Visual
  Studio Professional](https://aws.amazon.com/marketplace/pp/prodview-zo3zltrbpgr5i "https://aws.amazon.com/marketplace/pp/prodview-zo3zltrbpgr5i")
- [Visual
  Studio Enterprise](https://aws.amazon.com/marketplace/pp/prodview-dzstlnjdl3izg "https://aws.amazon.com/marketplace/pp/prodview-dzstlnjdl3izg")
- [Office LTSC
  Professional Plus](https://aws.amazon.com/marketplace/pp/prodview-bh46d5p2hapns "https://aws.amazon.com/marketplace/pp/prodview-bh46d5p2hapns")
- [Win Remote
  Desktop Services SAL](https://aws.amazon.com/marketplace/pp/prodview-buamtl3v3xaes "https://aws.amazon.com/marketplace/pp/prodview-buamtl3v3xaes")

###### Discover and subscribe to products from the License Manager console

You can also discover the required products to subscribe to from the License Manager
console.

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, under **User-based
   subscriptions**, choose **Products**.
3. Choose a product’s name or choose the **Subscribe in AWS Marketplace** button to display subscription details.
4. For each of the listed Marketplace products, select **View subscription options**. Review the terms and choose **Subscribe** to proceed.

If you accept the terms, the product subscription will need to be processed. The
subscription will have an in progress message until it completes. You can repeat these
steps for any other configured products you require. Once all of the required products
have an active subscription, you can proceed with registering your Active Directory with the product.

###### Note

Your estimated bill for charges on the number of users and related costs takes
48 hours to appear for billing periods that haven't closed (marked as
**Pending** billing status) in AWS Billing. For more
information, see [Viewing your monthly
charges](../../../awsaccountbilling/latest/aboutv2/invoice.md "../../../awsaccountbilling/latest/aboutv2/invoice.md") in the _AWS Billing User Guide_.

## Step 2: Register your

Active Directory in License Manager

License Manager requires that subscription users are defined in Active Directory in order to
associate the users with user-based subscriptions. This can be either an AWS Managed Microsoft AD
or a self-managed Active Directory, depending on your subscriptions.

- If you subscribe only to stand-alone Microsoft Office or Visual Studio products,
  you must configure an AWS Managed Microsoft AD.
- If you subscribe to [Win Remote Desktop Services SAL](https://aws.amazon.com/marketplace/pp/prodview-buamtl3v3xaes "https://aws.amazon.com/marketplace/pp/prodview-buamtl3v3xaes"),
  then you can use either an AWS Managed Microsoft AD or a self-managed Active Directory.

To use Microsoft Office with user-based subscriptions, you must grant License Manager permission to
update your VPC configuration. When you configure your VPC, License Manager creates
[VPC
endpoints](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") on your behalf. These endpoints are required for your resources
to connect to activation servers and remain in compliance.

You must configure DNS forwarding for any additional VPCs that you register for
user-based subscriptions. If you have user-based subscriptions in multiple
AWS Regions, each Region must have its own Active Directory with DNS forwarding
configured.

###### Important

You must allow License Manager to create the required [service-linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") before you can proceed. For more information, see the
[Prerequisites to create
user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-prerequisites "user-based-subscriptions.md#usubs-prerequisites").

Registration steps differ in the console, depending on which products you've subscribed
to. If you've subscribed to `Win Remote Desktop Services SAL`, select the
**Microsoft RDS SAL** tab. If you subscribe to Microsoft Office or
Visual Studio and do NOT subscribe to RDS SAL, select the **Stand-alone
MSO subscriptions** tab.

Microsoft RDS SAL

###### Register AWS Managed Microsoft AD

To register AWS Managed Microsoft AD as your Active Directory for user-based subscriptions,
follow these steps:

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Navigate to **User-based subscriptions** under
   **Settings** in the left navigation pane.
3. In the **Remote Desktop Services (RDS)** tab on the
   **User based subscriptions** page, choose
   **Register Active Directory**.
4. Select the **AWS Managed Active Directory**
   option to enter details.
5. Select your managed directory from the **AWS Active Directory**
   list, or create a new managed directory and then come back and select it.
6. Choose **Register** to register your AWS Managed Active
   Directory.

###### Register self-managed Active Directory

To register a self-managed Active Directory for user-based subscriptions,
follow these steps:

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Navigate to **User-based subscriptions** under
   **Settings** in the left navigation pane.
3. In the **Remote Desktop Services (RDS)** tab on the
   **User based subscriptions** page, choose
   **Register Active Directory**.
4. Select the **Self-managed Active Directory**
   option to enter details.
5. Enter the **Active Directory domain**.
6. Select the version for your **Active Directory IP Addresses**,
   then enter the primary and secondary IP addresses for your directory.
7. In the **Networking** section, select the
   **VPC** and two **Subnets** where
   your Active Directory resides.
8. Select the administrative credentials **Secret**
   that you created as part of the prerequisites for your Microsoft RDS
   subscription.

Stand-alone MSO subscriptions

###### Register AWS Managed Microsoft AD

To register AWS Managed Microsoft AD as your Active Directory for user-based Microsoft Office
and Visual Studio subscriptions, follow these steps:

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Navigate to **User-based subscriptions** under
   **Settings** in the left navigation pane.
3. On the **User based subscriptions** page, select the
   tab for the Microsoft Office or Visual Studio subscription product that you want
   to register, and then choose
   **Register Active Directory**.
4. Select your managed directory from the **AWS Active Directory**
   list, or create a new managed directory and then come back and select it.
5. Choose **Register** to register your AWS Managed Active
   Directory.

When you register your Active Directory, License Manager creates two network interfaces so that the
service can communicate with your directory. The network interface will have a description
similar to _AWS created network interface for LicenseManager
`<directory_id>`_.

###### Active Directory registration from the AWS CLI

You can register your Active Directory as the identity provider for
user-based subscriptions with the [RegisterIdentityProvider](../../../license-manager-user-subscriptions/latest/APIReference/API_RegisterIdentityProvider.md "../../../license-manager-user-subscriptions/latest/APIReference/API_RegisterIdentityProvider.md") operation.

```
aws license-manager-user-subscriptions register-identity-provider --product "`<product-name>`" --identity-provider "ActiveDirectoryIdentityProvider={DirectoryId=`<directory_id>`}"
```

###### Configure Active Directory and your VPC for user-based subscriptions

(AWS CLI)

You can register your Active Directory as the identity provider and configure
your VPC for user-based subscriptions with the [RegisterIdentityProvider](../../../license-manager-user-subscriptions/latest/APIReference/API_RegisterIdentityProvider.md "../../../license-manager-user-subscriptions/latest/APIReference/API_RegisterIdentityProvider.md") operation.

```
aws license-manager-user-subscriptions register-identity-provider --product "`<product_name>`" --identity-provider "ActiveDirectoryIdentityProvider={DirectoryId=`<directory_id>`}" --settings "Subnets=[`subnet-1234567890abcdef0`,`subnet-021345abcdef6789`],SecurityGroupId=`sg-1234567890abcdef0`"
```

For more information about the available software products, see
[Supported software products for
user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-software "user-based-subscriptions.md#usubs-software").

## Step 3: Configure RDS license

server

The Microsoft Remote Desktop Services (RDS) license server issues Subscriber Access
Licenses (SALs) to Active Directory users when they access EC2 instances that provide
user-based subscription Microsoft products. After you've completed steps 1 and 2, you
can configure your license server, as follows.

Ensure that you've completed the [User-based subscription prerequisites](user-based-subscriptions.md#usubs-prerequisites "user-based-subscriptions.md#usubs-prerequisites") for RDS before you begin. This process
assumes that you have already set up your Active Directory.

###### Configure RDS license server for user-based subscriptions (Console)

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Navigate to the **User-based subscriptions** page, under
   **Settings** in the left navigation pane.
3. On the **Remote Desktop Services (RDS)** tab, you should
   see one or more Active Directories in the list. There may be a prompt displayed
   to let you know that you need to configure RDS for your Active Directory.
4. From the prompt or from the **Actions** menu, choose
   **Configure RDS License Server**.
5. In the **Configure RDS License Server** dialog, You can configure
   the following settings:

**Active Directory**

This section has key details for the directory that's connected to
the RDS license server that you configure.

**Secret**

You must choose an existing secret or create a new one for the
credentials that are used for user administration tasks on the license
server. The first part of the secret name must follow the pattern that's
described in Administrative credentials secret section of the
[User-based subscription prerequisites](user-based-subscriptions.md#usubs-prerequisites "user-based-subscriptions.md#usubs-prerequisites").

**Tags**

You can optionally enter tags for your license server resource. 6. Choose **Configure** to save your settings.

## Step 4: Launch an instance to

provide user-based subscriptions

After you have subscribed to a product, you must launch instances for your users to
connect to from the AWS Marketplace AMI that includes the product. After you launch an instance,
AWS Systems Manager attempts to join the instance to the Active Directory domain and perform additional
configuration and hardening on the resource. The configurations to make the instance
ready to use can take around 20 minutes to complete. You can confirm the resource is
ready to use from the **User association** page of the License Manager console by
checking for a **Health status** of **Active** for the
instance.

To launch an instance with user-based subscriptions, see [Launch an instance from a license included AMI](usubs-launch-instance.md "usubs-launch-instance.md").

## Step 5: Associate users to a user-based

subscription instance

Once you have subscribed to the required product’s AWS Marketplace AMI, you can subscribe users
to a product and associate them to an instance that provides the product. You can subscribe
users to products and associate them with an instance in a single step, or separately.
When you subscribe a user, the directory is checked to ensure that the user identity is
present. One subscription is created for each user you subscribe to the product.

Each user must have a subscription to both Windows Server Remote Desktop Services
Subscriber Access License (RDS SAL) and the product they will use.

When your account has subscribed to RDS SAL as detailed in [Step 1: Subscribe to a
product](#user-based-subscriptions-subscribe-products "#user-based-subscriptions-subscribe-products"), License Manager automatically subscribes
the users in your Active Directory to RDS SAL when they subscribe to a user-based
subscription product.

###### Note

If a user who has never subscribed logs into an instance that is associated
with RDS SAL, License Manager automatically subscribes them and begins Microsoft RDS billing. Billing
continues until they are unsubscribed and their license token that was issued by the
RDS SAL license server expires.

Similarly, if a previously subscribed user unsubscribes, but continues to log in
after their RDS SAL license token expires, they are automatically re-subscribed,
and billing continues until they are again unsubscribed and their token expires.

For more information about subscription charges and billing, see [Subscription charges in License Manager](user-based-subscriptions.md#usubs-subscription-charges "user-based-subscriptions.md#usubs-subscription-charges").

The **Products** page in License Manager displays active subscriptions by
listing their **Marketplace subscription status** as
**Active**. In the product details page, License Manager displays active
user subscriptions with a **Status** of
**Subscribed**.

###### Important

If your Active Directory is not configured with the product, a notification bar
appears at the top of the console advising you to adjust the directory settings. On
the notification bar, choose **Open settings** to access the
**Settings** page in License Manager and edit your directory.

Each user must have a subscription to both RDS SAL and the product they will use.
Subscribing users to a product in which the **Marketplace subscription
status** is **Inactive** will fail.

When you select an instance to associate users to, you can optionally
subscribe them to the products that the instance provides if they're not already
subscribed. Use one of the following methods to subscribe and associate users.

Console
To associate users to an instance, follow these steps:

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, under **User-based
   subscriptions**, choose **User
   association**.
3. Select the instance that you want to associate users with, then
   choose one of the following options:

**Associate users**

Specify up to 5 user names that exist in your directory,
including the **Domain name** if they exist in a
trusted domain, and choose **Associate**.
_If you use this method, users must already be subscribed
to the products that the instance provides._

**Subscribe & Associate users**

Specify up to 5 user names that exist in your directory,
including the **Domain name** if they exist in a
trusted domain, and choose **Subscribe &
Associate**.

###### (Optional) Review user associations

On the **User association** page, the users you
selected are displayed under **Users** with
an **Association Status** of **Associated**.

###### (Optional) Review subscribed users

On the **Products** page, choose the
**Product name**. Subscribed users are displayed
under **Users** with a **Status** of
**Subscribed**.

AWS CLI
You can associate users with an instance launched to provide the
user-based subscription with the [AssociateUser](../../../license-manager-user-subscriptions/latest/APIReference/API_AssociateUser.md "../../../license-manager-user-subscriptions/latest/APIReference/API_AssociateUser.md") operation.

```
aws license-manager-user-subscriptions associate-user --username `<user_name>` --instance-id `<instance_id>` --identity-provider  ""ActiveDirectoryIdentityProvider" = {"DirectoryId" = "`<directory_id>`"}"
```

###### To associate self-managed Active Directory users to an instance

(AWS CLI)

You can associate users from your self-managed Active Directory with an instance
launched to provide the user-based subscription with the [AssociateUser](../../../license-manager-user-subscriptions/latest/APIReference/API_AssociateUser.md "../../../license-manager-user-subscriptions/latest/APIReference/API_AssociateUser.md") operation.

```
aws license-manager-user-subscriptions associate-user --username `<user_name>` --instance-id `<instance_id>` --identity-provider  ""ActiveDirectoryIdentityProvider" = {"DirectoryId" = "`<directory_id>`"}" --domain `<self-managed-domain-name>`
```

For more information about the available software products, see
[Supported software products for
user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-software "user-based-subscriptions.md#usubs-software").

You can subscribe users to a product using one of the following methods.

Console

###### Subscribe users to a product (Console)

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, under **User-based
   subscriptions**, choose
   **Products**.
3. Select a product to subscribe users to in which the
   **Marketplace subscription status** is
   **Active**.
4. If the product is Microsoft RDS, select the registered Active Directory
   that contains the users to subscribe.
5. Choose **Subscribe user** to continue.
6. Specify up to 20 user names that exist in your directory,
   including the **Domain name** if they exist in a
   trusted domain, and choose **Subscribe**.

Users that have a subscription are displayed under
**Users** with a **Status** of
**Subscribed**.

AWS CLI

###### Subscribe users to a product (AWS CLI)

You can subscribe users to a product that is registered with your
identity provider using the [StartProductSubscription](../../../license-manager-user-subscriptions/latest/APIReference/API_StartProductSubscription.md "../../../license-manager-user-subscriptions/latest/APIReference/API_StartProductSubscription.md") operation.

```
aws license-manager-user-subscriptions start-product-subscription --username `<user_name>` --product `<product_name>` --identity-provider ""ActiveDirectoryIdentityProvider" = {"DirectoryId" = "`<directory_id>`"}"
```

###### Subscribe users to a product with a self-managed Active Directory

(AWS CLI)

You can subscribe users from your self-managed Active Directory to a product that
is registered with your AWS Managed Microsoft AD directory using the [StartProductSubscription](../../../license-manager-user-subscriptions/latest/APIReference/API_StartProductSubscription.md "../../../license-manager-user-subscriptions/latest/APIReference/API_StartProductSubscription.md") operation.

```
aws license-manager-user-subscriptions start-product-subscription --username `<user_name>` --product `<product_name>` --identity-provider 'ActiveDirectoryIdentityProvider" = {"DirectoryId" = "`<directory_id>`"}' --domain `<self-managed-domain-name>`
```

For more information about the available software products, see [Supported software products for
user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-software "user-based-subscriptions.md#usubs-software").

Users that have a subscription will be displayed under
**Users** with a **Status** of
**Subscribed**.

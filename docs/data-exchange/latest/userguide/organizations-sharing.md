# Sharing AWS Data Exchange license subscriptions in an

organization

When you subscribe to AWS Data Exchange products, an agreement is created that grants you license to
use those products. If your AWS account is a member of an organization, you can share that
license for AWS Data Exchange products with the other accounts in that organization.

###### Note

For more information about AWS Organizations, see the [AWS Organizations User
Guide](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md").

The following topics outline the process of sharing the licenses across accounts.

###### Topics

- [Prerequisites for license sharing](#license-sharing-prereqs "#license-sharing-prereqs")
- [Step 1: View your licenses](#view-share-licenses "#view-share-licenses")
- [Step 2: Share your licenses](#share-licenses "#share-licenses")

## Prerequisites for license sharing

Before you can share licenses for data products, you must first set up license sharing for
your organization. Complete the following tasks to set up license sharing for your
organization:

- Give AWS Marketplace permission to manage licenses on your behalf so that it can create the
  associated license grants when you purchase or share your licenses. For more information, see
  [Service-linked roles
  for AWS Marketplace](../../../marketplace/latest/buyerguide/buyer-using-service-linked-roles.md "../../../marketplace/latest/buyerguide/buyer-using-service-linked-roles.md") in the _AWS Marketplace Buyer Guide_.
- Set up AWS License Manager for first use. For more information, see [Getting started
  with AWS License Manager](../../../license-manager/latest/userguide/getting-started.md "../../../license-manager/latest/userguide/getting-started.md") in the _AWS License Manager User
  Guide_.

## Step 1: View your licenses

The following topics outline the process of viewing your licenses.

###### Topics

- [Viewing all licenses](#view-all-licenses "#view-all-licenses")
- [Viewing a single license](#view-single-licenses "#view-single-licenses")

### Viewing all licenses

You can use the AWS License Manager console to view all of the licenses for AWS Data Exchange products that
you purchased.

###### To view all licenses for your subscribed products

1. Sign in to the [AWS Management
   Console](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. Open the [AWS License Manager
   console](https://console.aws.amazon.com/license-manager "https://console.aws.amazon.com/license-manager").
3. In the left navigation pane, choose **Granted licenses**.
4. View all the licenses for your subscribed products.

### Viewing a single license

You can use the AWS License Manager console to view a single license for an AWS Data Exchange data grant.

###### To view a license for a single subscription

1. Sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. Under **My subscriptions**, choose \***\*Subscriptions\*\***.
3. Choose a subscription.
4. On the next page, choose **View license** or **Distribute with License Manager**.
   What you see varies, depending on the data grant's distribution permissions.
5. View the details on the **License detail** page.

## Step 2: Share your licenses

You can manage and share your licenses with other accounts in your organization by using
AWS License Manager.

For more details about using License Manager with AWS managed licenses, see [Granted
licenses](../../../license-manager/latest/userguide/granted-licenses.md "../../../license-manager/latest/userguide/granted-licenses.md") and [Seller issued licenses](../../../license-manager/latest/userguide/granted-licenses.md "../../../license-manager/latest/userguide/granted-licenses.md") in
the _AWS License Manager User Guide_.

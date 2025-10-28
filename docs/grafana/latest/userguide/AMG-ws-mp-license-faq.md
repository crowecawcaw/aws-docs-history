# FAQ for AWS Marketplace Enterprise users

Previously, you may have purchased a license for Grafana Enterprise through AWS Marketplace.
You can no longer purchase new licenses through AWS Marketplace, and you can not renew any
license that was previously purchased through AWS Marketplace. The following FAQ may help you
depending on the state of your AWS Marketplace license.

## I subscribed to a 30-day free trial from

AWS Marketplace, but I haven't associated it with my workspace. Can I apply it
now?

No. The free trials are no longer supported in Amazon Managed Grafana.

## I purchased a 30-day free trial from

AWS Marketplace, and I already associated it with my workspace. What will happen to
my trial?

Your free trial will continue until it expires. If you want to upgrade and use
the Enterprise plugins, you can upgrade through the
Amazon Managed Grafana console, as described in the previous section.

## I have a AWS Marketplace paid license that hasn't

yet expired, but I want to use Amazon Managed Grafana managed Enterprise plugins. How do I
do that?

As long as you have a current AWS Marketplace license, you can only associate that license
with your workspaces. You can only upgrade in the Amazon Managed Grafana console after
your AWS Marketplace license expires (or you cancel it through AWS Marketplace).

The following questions and answers provide more details.

## I purchased a full Grafana Enterprise

license from AWS Marketplace and associated it with one or more workspaces. What will
happen to those?

When your license expires (after 30 days, unless you have autorenewal turned on),
any Enterprise data sources that you are using in your workspace will stop working.
If you wish to continue using Enterprise data sources, you can [upgrade to use Enterprise plugins](AMG-workspace-manage-enterprise.md "AMG-workspace-manage-enterprise.md")
directly from the Amazon Managed Grafana console.

## It sounds like there will be downtime

associated with my license expiring, where my workspace can't access any
Enterprise plugins. How do I avoid that?

There will be some downtime associated with your license expiring, as you switch
to the new Enterprise plugins license. However, you can minimize this.

###### Note

The following steps need to be performed precisely to minimize downtime. We
recommend that you read them carefully before beginning.

To get the new [pricing](https://aws.amazon.com/grafana/pricing "https://aws.amazon.com/grafana/pricing"),
we recommend that you upgrade to Amazon Managed Grafana Enterprise
plugins, rather than continue using the AWS Marketplace license.

###### To switch from AWS Marketplace Enterprise license to Amazon Managed Grafana Enterprise plugins while

minimizing downtime.

1. To prepare, first go to the [Grafana Labs
   website](https://grafana.com/partners/amg/support "https://grafana.com/partners/amg/support"), and sign into your account (or create a new one).
   Get your Grafana Labs token that you will use later in the process.

For more details on this part of the process, see [Link your account with
Grafana Labs](AMG-workspace-register-enterprise.md "AMG-workspace-register-enterprise.md"). 2. Sign into the [AWS Marketplace
console](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/"), and choose **Manage subscriptions**
from the left menu. 3. Find the subscription that you want to switch, and choose
**Manage**. This will bring up details about your
subscription.

###### Note

This page shows your service end date. You can wait until
you are nearing that date to continue these steps, to maximize use of your
current subscription before canceling. 4. Choose **Actions**, and select **Cancel
subscription**.

This cancels your subscription in AWS Marketplace. However, you can
continue to use the Enterprise data sources until Amazon Managed Grafana automatically
removes your license at the end of the day (local time for your
workspace).

For more information about canceling subscriptions in AWS Marketplace, see
[Cancel
your product subscription](../../../marketplace/latest/buyerguide/cancel-subscription.md "../../../marketplace/latest/buyerguide/cancel-subscription.md") in the _AWS Marketplace Buyer
Guide_. 5. After your subscription is canceled in AWS Marketplace, cancel it in Amazon Managed Grafana:

    1. Sign into [the Amazon Managed Grafana
     console](https://console.aws.amazon.com/grafana "https://console.aws.amazon.com/grafana").
    2. From the left menu, choose **All workspaces**.
    3. Choose the name of the workspace you are switching.
    4. Under **Enterprise license**, choose
     **Manage**.
    5. Choose **None** and then
     **Save**. This will remove the AWS Marketplace license from
     Amazon Managed Grafana

When the Enterprise license is removed, you will no longer be able to
access Enterprise plugins in your workspace. 6. You can now upgrade in the Amazon Managed Grafana console. Follow the instructions in
the [Managing your access to Amazon Managed Grafana
Enterprise plugins](AMG-workspace-manage-enterprise.md "AMG-workspace-manage-enterprise.md") topic, using the Grafana
Labs token you created in the first step.

###### Note

Your workspace is not able to access Enterprise data sources from the time
you cancel the license in Amazon Managed Grafana until when you upgrade to access Enterprise
plugins. This is
typically around 10-15 minutes, but can take longer, depending on how quickly
you can perform these steps. Making sure that you have the Grafana Labs token
ready will minimize this time.

## I have an AWS Marketplace license with autorenew.

Will that continue?

Yes. The AWS Marketplace subscription is retired, and you can't manually renew it, but
if you had autorenew set up, it will continue until you
turn it off. When you do that, you can upgrade, following the instructions in the
previous answers.

To get the new [pricing](https://aws.amazon.com/grafana/pricing "https://aws.amazon.com/grafana/pricing"),
we recommend that you upgrade to Amazon Managed Grafana Enterprise
plugins, rather than continue using the AWS Marketplace license.

## I have an AWS Marketplace license that I haven't yet

associated with a workspace, can I use it?

Yes, you can associate that AWS Marketplace license and use it until it expires. That will
happen within 30 days, unless you turned on autorenew. See the
previous questions and answers for more information.

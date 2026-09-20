

# Subscription management
<a name="al-subscription-management"></a>

A subscription associates a provider with the ambient documentation agent. You need an active subscription before you can start a streaming session.

**Topics**
+ [Create a subscription](#al-create-subscription)
+ [Deactivate a subscription](#al-deactivate-subscription)
+ [Reactivate a subscription](#al-reactivate-subscription)

## Create a subscription
<a name="al-create-subscription"></a>

To create a subscription, call the `CreateSubscription` API operation. This generates a unique `subscriptionId` that you use to authorize the user and start streaming sessions. Subscriptions are automatically created in activated mode.

**Tip**  
Create the subscription on the user’s first use to align subscription start with actual usage.

## Deactivate a subscription
<a name="al-deactivate-subscription"></a>

To temporarily stop a subscription from accepting new streaming sessions, call the `DeactivateSubscription` API operation. A deactivated subscription retains its configuration and can be reactivated later. In-progress streams complete normally.

**Important**  
Deactivating a subscription immediately forfeits any remaining free trial period. If a subscription that was deactivated during a free trial is reactivated later, it is reactivated as a paid subscription.

## Reactivate a subscription
<a name="al-reactivate-subscription"></a>

Deactivated subscriptions can be reactivated by calling the `ActivateSubscription` API operation with the `subscriptionId`. Paid metering begins immediately upon reactivation.
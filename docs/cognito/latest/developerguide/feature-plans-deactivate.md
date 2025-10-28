# Turning off features to change feature

plans

Feature plans add configuration options to your user pool. You can configure and use
these features only when the related feature plan is active. For example, you can configure
access token customization in the Plus and Essentials plans, but not in the Lite plan. To
deactivate these features, you must deactivate each active component. The **Switch
to** option in the **Settings** menu in the Amazon Cognito console
notifies you of the features you must deactivate before you can change your feature plan.
With this chapter, you can learn the changes that deactivation makes to your user pool
configuration, and how to turn off these features individually.

**Access token customization**

To switch to a plan that doesn't include access token customization, you must
remove the [pre token
generation Lambda trigger](user-pool-lambda-pre-token-generation.md#user-pool-lambda-pre-token-generation-accesstoken "user-pool-lambda-pre-token-generation.md#user-pool-lambda-pre-token-generation-accesstoken") from your user pool. To add a new pre token
generation trigger without access token customization, assign a new function to the
trigger and configure it for `V1_0` events. These version one trigger
events can process changes to ID tokens only.

To manually deactivate access token customization, remove your pre token
generation trigger and add a new version one trigger.

**Threat protection**

To switch to a plan without threat protection, deactivate all features from the
**Threat protection** menu of your user pool.

**Log export**

To switch to a plan without log export, deactivate it from the **Log
streaming** menu of your user pool. Your user pool no longer generates
local or exported user-activity logs. You can also send a [SetLogDeliveryConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_SetLogDeliveryConfiguration.md "../../../cognito-user-identity-pools/latest/APIReference/API_SetLogDeliveryConfiguration.md") API request that removes any configuration with
an `EventSource` value of `UserActivity`.

**Email MFA**

To switch to a plan without email MFA, go to the **Sign-in** menu
of your user pool. Edit **Multi-factor authentication** and deselect
**Email message** as one of the available **MFA
methods**.

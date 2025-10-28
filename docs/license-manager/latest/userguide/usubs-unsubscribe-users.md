# Unsubscribe users from user-based

product subscriptions in License Manager

You must unsubscribe a user from a Microsoft Office or Visual Studio user-based subscription product
to stop incurring charges for them. Microsoft RDS is billed on a per user, per month basis based on a combination of the user subscription and the client access license (CAL) token that's issued from the license server when the user connects to an instance that provides the subscription product. For more information, see
[Microsoft RDS billing in License Manager](user-based-subscriptions.md#usubs-billing-rds "user-based-subscriptions.md#usubs-billing-rds").

###### Important

For Microsoft Office or Visual Studio user-based subscription products, you must first disassociate
the Active Directory user from all instances where they are currently associated before you
can unsubscribe them.

###### Unsubscribe users from user-based product subscriptions

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, under **User-based subscriptions**,
   choose **Products**.
3. Select the product that you want to unsubscribe users from.
4. Select the user names to unsubscribe, then choose **Unsubscribe
   users**.

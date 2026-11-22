

# Turning off a procurement system integration

There are two different things you might mean by turning the integration off, and they work differently.

**Turning off one connection** is something you do yourself. Select the connection on the [**External system**](https://console.aws.amazon.com/marketplace/buying-policies/approvers-and-routing?region=us-east-1&tab=external-system) tab of the **Approvers and routing** page and disable or remove it in the edit section that appears, or manage it from the [AWS Billing and Cost Management console](https://console.aws.amazon.com/costmanagement/home#/e-invoicing-preference/procurement-portal-preference/). Disabling is reversible: the connection stays in your account and you can enable it again later. You can disable or remove connections while more than one remains.

**Turning off the integration entirely** requires help from AWS. To remove your last connection and end the integration, contact [AWS Marketplace Support on the AWS website](https://aws.amazon.com/marketplace/help/contact-us).

Removing the integration isn't how you stop governing purchases. If you only want purchases to stop going to your procurement system, remove the approval rule that sends them there, or update it to send them to another approver. The connection can stay as it is.

**Important**  
Disabling a connection doesn't remove the approval requirement. AWS Marketplace tells the buyer that the request can't be delivered rather than leaving them waiting. If you want those purchases to complete without approval, change or remove the rule that requires it.

## Purchases that are already waiting
<a name="procurement-integration-disabling-in-flight"></a>

Changing or removing a rule doesn't disturb a buyer who is already waiting for approval. The rules that applied when they submitted the purchase continue to apply to it, so their purchase isn't cancelled and doesn't change course underneath them.

Taking the integration away is different. A purchase that is waiting for approval from a procurement system you have disconnected can no longer get it.

If you need one of those purchases to go ahead anyway, your management account can approve it directly. For more information about overriding an approval, see [Overriding an approval](procurement-system-supported-scenarios.md#procurement-system-scenarios-override).
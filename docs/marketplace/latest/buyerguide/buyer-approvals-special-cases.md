

# Special cases for buyer approvals

The following table describes how buyer approvals work in less common scenarios.


| Scenario | Details | 
| --- | --- | 
| Purchase request matches more than one rule | Each Require approval rule that the purchase request matches creates an approval request. If more than one matching rule uses the same approval routing, such as the same approval chain, the AWS Marketplace console, or your external system, only one approval request is created for that routing. If any matching rule is a Decline purchase rule, the purchase is declined, and no approval requests are created. The requests are reviewed at the same time. AWS Marketplace creates the agreement only after every request is approved. If any approval request is declined, the purchase can't proceed, even if the other approval requests are approved. If the buyer cancels the purchase request, all of its approval requests are cancelled. | 
| Offer has expired when the approval is complete | The request is approved, but AWS Marketplace can't create the agreement. If the offer expiration date is extended after the request is approved, you can manually accept the private offer without routing the request for approval again. | 
| Mandatory purchase order (PO) required, but approved without a PO | The request is approved, but AWS Marketplace can't create the agreement until a PO is added. Add the PO, and then manually accept the offer without routing the request for approval again. | 
| Annual purchases | Products with annual pricing, such as AMI and container products, require a usage agreement for the product. Before you request approval for an annual purchase, get approval for the usage-based purchase or accept the usage agreement. If an annual purchase is approved without a usage agreement, the annual agreement fails. In that case, accept the usage-based agreement, and then manually subscribe to the annual agreement. | 
| Offer sets | Rules apply individually to each offer in an offer set. If some offers require approval and others don't, approval rules run independently for each offer. | 
| Account moves to another organization during review | The request isn't routed to the new organization automatically. Route the request again in the new organization, where that organization's approval rules apply, if it has any. | 
| Usage-based (pay-as-you-go) purchases | Purchase amount criteria don't include usage-based charges, because those amounts aren't known at the time of purchase. To require approval for usage-based purchases, use the Pricing type criterion. | 
| Purchases in another currency | Purchase amount criteria apply to one currency only. To set amounts for another currency, create a separate rule. | 
| Account or OU with its own Private Marketplace experience | Approval rules from the most specific level apply, in this order: account, OU, and then organization. For more information, see [Where approval rules apply](buyer-approvals.md#buyer-approvals-scope). | 
| Purchases that approval rules don't apply to | Approval rules don't apply to the following:+ Amazon Bedrock serverless purchases made through the Amazon Bedrock console. Approval rules apply to private offers for Amazon Bedrock serverless models, which you accept in AWS Marketplace.<br />+ Automatic renewals of an existing agreement. The auto-renewal terms are reviewed as part of the initial approval request.<br />+ Downgrades from a private offer to public pricing. When a private offer expires, access continues, and usage is billed at the public pay-as-you-go rate. | 


# AWS Direct Connect pricing
<a name="pricing-overview"></a>

**Important**  
AWS pricing is subject to change. For current pricing, see the [Direct Connect pay-as-you-go pricing page](https://aws.amazon.com/directconnect/pricing/pay-as-you-go/). Pricing examples in this guide are illustrative only and might not reflect current pricing.

## How Direct Connect pricing works
<a name="pricing-how-it-works"></a>

With Direct Connect, you pay only for what you use. There is no minimum fee and no up-front commitment. You pay as you go for the resources that you provision and the data that you transfer.

Your Direct Connect charges fall into the following categories, which are described in this chapter:
+ [Capacity (port-hour) charges](#pricing-capacity)
+ [Data transfer out (DTO)](#pricing-data-transfer)
+ [Cross-connect and colocation fees](#pricing-cross-connect)

For current rates in each AWS Region and Direct Connect location, see the [Direct Connect pay-as-you-go pricing page](https://aws.amazon.com/directconnect/pricing/pay-as-you-go/).

## Capacity (port-hour) charges
<a name="pricing-capacity"></a>

Capacity charges, also called port-hour charges, are billed for each hour that a connection is provisioned, from the time you create the connection until you delete it. Port-hour charges apply whether or not you send traffic over the connection.

The port-hour rate varies by the port speed of the connection and by the type of connection, such as a dedicated connection or a hosted connection. For more information about the difference between dedicated and hosted connections, see [Dedicated and hosted connection billing](#pricing-dedicated-vs-hosted).

For current port-hour rates, see the [Direct Connect pay-as-you-go pricing page](https://aws.amazon.com/directconnect/pricing/pay-as-you-go/).

## Data transfer out (DTO)
<a name="pricing-data-transfer"></a>

Data transfer out (DTO) refers to data that is sent from AWS to your network over an Direct Connect connection. DTO over Direct Connect is priced based on the Direct Connect location where the data is sent and the source or destination AWS Region.

Data transfer *into* AWS over Direct Connect is not charged.

**Example Illustrative data transfer out charge**  
Suppose you transfer data out from AWS to your network through an Direct Connect location in the Contiguous United States. In this example, data transfer out is billed at an illustrative rate of $0.02 per GB. This rate is provided only as an example, is subject to change, and might not reflect current pricing. For the full per-Region and per-location data transfer out rates, see the [Direct Connect pay-as-you-go pricing page](https://aws.amazon.com/directconnect/pricing/pay-as-you-go/).

## Cross-connect and colocation fees
<a name="pricing-cross-connect"></a>

To use Direct Connect, you establish a cross-connect at an Direct Connect location. The cross-connect and any associated colocation fees are billed by the colocation provider or Direct Connect Partner that operates the facility, not by AWS. Contact the facility operator for information about these charges.

## Dedicated and hosted connection billing
<a name="pricing-dedicated-vs-hosted"></a>

Direct Connect offers dedicated connections and hosted connections, and the way each is billed differs at a high level:
+ A *dedicated connection* is a physical connection that you request through AWS. AWS bills the port-hour charge for a dedicated connection directly to your AWS account.
+ A *hosted connection* is provisioned by an Direct Connect Partner on your behalf. Port-hour billing arrangements for hosted connections can involve the Partner. Contact your Direct Connect Partner for details about how your hosted connection is billed.

For current port-hour rates for dedicated and hosted connections, see the [Direct Connect pay-as-you-go pricing page](https://aws.amazon.com/directconnect/pricing/pay-as-you-go/).
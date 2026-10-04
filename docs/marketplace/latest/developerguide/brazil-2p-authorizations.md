

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Brazil 2P Authorizations
<a name="brazil-2p-authorizations"></a>

Any ISV can authorize the AWS Brazil 2P distributor account, `664418980131`, to distribute a product in AWS Marketplace. When the `ResellerAccountId` of your Resale Authorization is `664418980131`, AWS Marketplace applies additional requirements.

Your Resale Authorization must meet all of the following requirements:
+ **Product type** – The product must be a SaaS product. Other product types aren't supported.
+ **Distribution role** – `ResellerRole` must be `Distributor`.
+ **Quantity** – The `AvailabilityRule` must set `OffersMaxQuantity` to `1`, which allows the distributor to create one offer from the Resale Authorization.
+ **Currency** – All pricing terms and payment schedule terms must use `USD`.
+ **Buyer targeting** – The `BuyerTargetingTerm` must specify exactly one buyer account.
+ **Legal terms** – The `BuyerLegalTerm` must use `CustomEula`, and you can't include a `ResaleLegalTerm`.
+ **Net payment terms** – Net payment terms aren't supported.

**Important**  
The [AWS Brazil 2P Distribution Program Seller Terms](https://s3.amazonaws.com/aws-mp-rcmp/AWS-Brazil-2P-Distribution-Program-Seller-Terms.pdf) apply to you and the entity you represent ("you") if you authorize Amazon AWS Serviços Brasil Ltda. to distribute to companies incorporated in Brazil, as seller of record, the rights to access and use your software identified in a distribution authorization that you create in AWS Marketplace.
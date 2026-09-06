

# FOCUS 1.0 with AWS columns conformance gaps
<a name="table-dictionary-focus-1-0-aws-conformance"></a>

The following table provides all of the conformance gaps that might exist in an export of the FOCUS 1.0 with AWS columns table. A particular conformance gap will not apply to your export if you're not receiving cost and usage data for the related scenario.




- ****Missing data****
  - **Affected column:** ContractedUnitPrice / **FOCUS 1.0 requirement:** ContractedUnitPrice must not be null for Usage and Purchase ChargeCategory line items that are not corrections. / **Conformance gap description:** ContractedUnitPrice might be null for certain product offerings.
  - **Affected column:** InvoiceIssuerName / **FOCUS 1.0 requirement:** InvoiceIssuerName must not be null. / **Conformance gap description:** InvoiceIssuerName might be null for certain charges.
  - **Affected column:** ListUnitPrice / **FOCUS 1.0 requirement:** ListUnitPrice must not be null for Usage and Purchase ChargeCategory line items that are not corrections. / **Conformance gap description:** ListUnitPrice might be null for certain product offerings.
  - **Affected column:** PricingUnit / **FOCUS 1.0 requirement:** PricingUnit must not be null for Usage and Purchase ChargeCategory line items that are not corrections. / **Conformance gap description:** PricingUnit might be null for certain product offerings.
  - **Affected column:** PublisherName / **FOCUS 1.0 requirement:** PublisherName must not be null. / **Conformance gap description:** PublisherName may be null for certain charges.
  - **Affected column:** SkuId / **FOCUS 1.0 requirement:** SkuId must not be null for Usage and Purchase ChargeCategory line items that are not corrections. / **Conformance gap description:** SkuId might be null for certain product offerings.
  - **Affected column:** SkuPriceId / **FOCUS 1.0 requirement:** SkuPriceId must not be null for Usage and Purchase ChargeCategory line items that are not corrections. / **Conformance gap description:** SkuPriceId might be null for certain line items when it should not be.

- ****Incorrect data****
  - **Affected column:** ConsumedQuantity
  - **FOCUS 1.0 requirement:** ConsumedQuantity is a required column for showing the amount of usage you actually used.
  - **Conformance gap description:** ConsumedQuantity will contain the amount of usage you were charged for. This means that ConsumedQuantity could be incorrect in situations where a minimum charge quantity applied for a particular service.<br />For example, there is a 10MB minimum for an Athena query and a 10 minute minimum Glue crawler run. For these services, ConsumedQuantity will show the value that includes the minimum charged quantity.


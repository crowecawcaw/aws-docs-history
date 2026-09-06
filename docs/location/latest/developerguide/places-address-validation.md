

# Address validation
<a name="places-address-validation"></a>

Amazon Location Service provides address validation through Amazon Location Service Jobs, enabling you to verify and standardize large volumes of addresses in bulk. Address validation checks addresses against authoritative datasets to confirm they exist and are deliverable, then formats them according to official postal standards.

Address validation supports addresses from Australia, Canada, United Kingdom, and United States.

Key capabilities include:
+ **Address standardization** — Formats addresses with consistent abbreviations, capitalization, and punctuation. Corrects errors such as spelling mistakes and adds missing components such as postal codes and street names.
+ **Deliverability verification** — Confirms that addresses exist and are deliverable by checking them against authoritative address datasets.
+ **Geographic coordinates** — Optionally returns latitude and longitude for validated addresses, available in the United States, Canada, and Australia.
+ **Country-specific postal attributes** — Provides postal system data specific to each country, such as USPS delivery point codes for US addresses and Australia Post identifiers for Australian addresses.

Address validation is available as a bulk processing operation through Amazon Location Service Jobs. You upload your address data to Amazon Simple Storage Service, submit a validation job, and retrieve standardized results when processing is complete.

For complete details about address validation features, input and output schemas, and use cases, see [Address validation](address-validation-concepts.md).
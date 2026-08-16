# AWS extension for OCSF

OCSF [schemas](https://schema.ocsf.io/ "https://schema.ocsf.io/") can be extended by adding new attributes, objects, categories, profiles and event classes.
A schema is the aggregation of core schema entities and extensions.

Extensions to OCSF allow a particular vendor or customer to augment an existing schema by adding attributes to provide domain-specific customization, improve data interoperability, and add more detailed context for security analysis.

The AWS Extension for Open Cybersecurity Schema Framework (OCSF) provides attribute definitions for cloud resources within OCSF events.
This extension adds a `cloud_resources` profile that extends the OCSF `resource_details` object with cloud-specific resource attributes. With these attributes, security teams can analyze resource configurations, potential vulnerabilities, and threat detection metadata.

## Extended `resource_details` object

The AWS Extension extends the `resource_details` object with attributes mentioned in the list of attribute references below.
These attributes ensure proper identification and classification of cloud resources across different providers within standardized event frameworks.

## AWS Extension for OCSF attribute reference

The [Basic attributes](aws-extension-basic-attributes.md "aws-extension-basic-attributes.md") and [Resource specific objects](aws-extension-resource-specific-objects.md "aws-extension-resource-specific-objects.md") sections provide examples of each of the attributes that are part of the AWS OCSF extension to resource\_details.

Each of the attribute definitions contains an OCSF status outlining its current relationship to the public OCSF schema:

- **Existing**: This attribute was already in standard OCSF resource\_details and is now part of the AWS extension.
- **New**: The attribute is not part of OCSF and was introduced as part of the AWS extension.
  It does not exist in the core OCSF schema.
- **Added to resource\_details**: The attribute is defined in OCSF but not part of resource\_details.

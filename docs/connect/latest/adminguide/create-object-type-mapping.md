

# Create an object type mapping in Connect Customer Customer Profiles
<a name="create-object-type-mapping"></a>

An object type mapping tells Customer Profiles how to ingest a specific type of data from a source application—such as Salesforce, Zendesk, or Amazon S3—into a unified standard profile object. You can then display that data (for example, customer address and email) to your agents using the [Connect Customer agent workspace](customer-profile-access.md).

There are two ways to create an object type mapping:
+ **Connect Customer console**: a no-code experience. See [Create an object type mapping in the Connect Customer console](create-mapping-console.md).
+ **Customer Profiles API**: use [PutProfileObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutProfileObjectType.html). For the JSON model, see [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md) and [Key definitions in Customer Profiles object type mappings](mapping-key-definitions.md).

The topics in this section describe how to create a mapping in the console, generate one with generative AI, and update and validate a mapping over time.

**Topics**
+ [Create an object type mapping in the Connect Customer console](create-mapping-console.md)
+ [Generate a mapping with generative AI in Customer Profiles](genai-powered-data-mapping.md)
+ [Update and validate an object type mapping in Customer Profiles](update-and-validate-mapping.md)
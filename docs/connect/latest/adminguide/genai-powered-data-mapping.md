

# Generate a mapping with generative AI in Customer Profiles
<a name="genai-powered-data-mapping"></a>

With the generative AI-powered data mapping capability in Connect Customer Customer Profiles, you can reduce the time needed to create unified profiles and deliver more personalized customer experiences.

When you add customer data from any of the more than 70 available no-code data connectors—such as Adobe Analytics, Salesforce, or Amazon S3—Customer Profiles analyzes the source data and automatically determines how to organize and combine data from disparate sources into unified profiles. You can review and complete the setup before ingestion begins.

Generative AI powered customer data mapping is available in the following regions:
+ US East (N. Virginia)
+ US West (Oregon)
+ Africa (Cape Town)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Asia Pacific (Seoul)
+ Canada (Central)
+ Europe (Frankfurt)
+ Europe (London)

## Set up generative AI-powered data mapping
<a name="set-up-genai-powered-data-mapping"></a>

1. Open the Connect Customer Customer Profiles console.

1. On the **Data source integrations** tab, choose **Add data source integration**.

1. Set up the connection. Select the data source from the drop-down list of supported connectors.  
![The data source from drop-down that has all supported connectors available.](https://docs.aws.amazon.com/connect/latest/adminguide/images/genai-augmented-data-mapping-1.png)

1. Map data. Choose to auto-generate the data mapping, select an existing mapping template, or create one from scratch.  
![Map data.](https://docs.aws.amazon.com/connect/latest/adminguide/images/genai-augmented-data-mapping-2.png)

1. Review the mapping summary. The auto-generated summary shows all customer attributes. Make edits to ingestion keys and confirm before starting data ingestion. For details on fields and keys, see [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md) and [Key definitions in Customer Profiles object type mappings](mapping-key-definitions.md).  
![Review mapping summary. Review the auto-generated mapping results summary that shows all the customer attributes.](https://docs.aws.amazon.com/connect/latest/adminguide/images/genai-augmented-data-mapping-3.png)

## How it works
<a name="genai-powered-data-mapping-how-it-works"></a>

Generation runs in four phases:

1. Customer Profiles fetches source attributes and, if available, sample data from your data source, then determines the most appropriate target object type. For an Amazon S3 source, the first CSV file found in the selected bucket and prefix is used as sample data. For other sources, attributes are fetched through AppFlow.

1. A large language model (LLM) processes each custom attribute and maps it to a standard customer profile attribute.

1. The LLM selects suitable attributes to serve as keys, such as customer identifiers.

1. A timestamp format detector parses timestamps to maintain the correct chronological order of records.

**Note**  
Generative AI produces a starting point that you review and confirm before any data is ingested. Always check the suggested keys—especially the unique and profile keys—against your understanding of the source data. If generation can't produce a valid mapping, fall back to [manual mapping in the console](create-mapping-console.md).

For errors and warnings you might see during generation, see [Troubleshoot object type mappings in Customer Profiles](object-type-mapping-troubleshooting.md).
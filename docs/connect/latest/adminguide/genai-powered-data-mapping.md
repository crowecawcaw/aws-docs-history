

# Generative AI powered data mapping in Connect Customer
<a name="genai-powered-data-mapping"></a>

Connect Customer Customer Profiles provides a generative AI powered customer data mapping capability that significantly reduces the time needed to create unified profiles, enabling you to help provide more personalized customer experiences.

With this capability, when contact center administrators add customer data from any of the 70\+ available no-code data connectors such as Adobe Analytics, Salesforce, or Amazon Simple Storage Service (S3), Connect Customer Customer Profiles will analyze the data from these sources to automatically determine how to organize and combine data that exists in different formats across disparate sources into unified profiles in Connect Customer. Contact center administrators can review and complete the setup of customer profiles, so they can provide agents with relevant customer information and dynamically personalize IVRs and chatbots to improve customer satisfaction and agent productivity.

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

## Set up generative AI powered data mapping
<a name="set-up-genai-powered-data-mapping"></a>

1. Open the Connect Customer Customer Profiles console.

1. On the **Data source integrations** tab, choose **Add data source integration**.

1. Set up the connection. Select the data source from drop-down that has all supported connectors available.  
![The data source from drop-down that has all supported connectors available.](http://docs.aws.amazon.com/connect/latest/adminguide/images/genai-augmented-data-mapping-1.png)

1. Map data. Select the option to auto-generate data mapping, or select an already existing mapping template or create one from scratch..  
![Map data.](http://docs.aws.amazon.com/connect/latest/adminguide/images/genai-augmented-data-mapping-2.png)

1. Review mapping summary. Review the auto-generated mapping results summary that shows all the customer attributes. Make edits to ingestion keys and confirm before starting data ingestion. For more on field mappings and keys, see [Object type mapping definition details in Connect Customer Customer Profiles](object-type-mapping-definition-details.md).  
![Review mapping summary. Review the auto-generated mapping results summary that shows all the customer attributes.](http://docs.aws.amazon.com/connect/latest/adminguide/images/genai-augmented-data-mapping-3.png)

## How it works
<a name="genai-powered-data-mapping-how-it-works"></a>

The system works in four phases. In the first phase, Customer Profiles fetches source attributes and, if available, samples data from your data source, subsequently determining the most appropriate object type for the target. For an Amazon S3 data source, the first CSV file found in the selected Amazon S3 bucket and prefix will be used as the sample data. For other data sources, Customer Profiles fetches source attributes through AppFlow. In the second phase, a large language model (LLM) is leveraged to further process each of the custom attributes and map them to standard customer profile attributes. LLM is used again in the third phase to select the suitable attributes that can serve as keys, such as customer identifiers. Finally in the fourth phase, the timestamp format detector parses the timestamps to maintain the right chronological order of the records. The system is able to generate the mapping for up to 120 attributes in less than 20 seconds after combining the prediction results.

## Generative AI powered data mapping troubleshooting
<a name="genai-powered-data-mapping-troubleshooting"></a>

The following sections display the possible error messages that you might encounter. It also provides the cause and resolution for each issue.

### Error: Could not parse object string into JSON
<a name="genai-powered-data-mapping-parse-object-error"></a>

The object string in the request is not a valid JSON. Review the object string in the request and verify that it is valid JSON.

### Error: Value at 'objects' failed to satisfy constraint: Member must have length less than or equal to 5
<a name="genai-powered-data-mapping-failed-constraint-error"></a>

There are too many objects in the request. Up to five objects are allowed in a request. Reduce the number of objects to five or less.

### Error: Breached limit of 120 attributes
<a name="genai-powered-data-mapping-breached-limit"></a>

Up to 120 attributes are allowed in a JSON object, including nested JSON attributes. Remove some attributes that don't need to be mapped from the JSON object.

![Up to 120 attributes are allowed in a JSON object, including nested JSON attributes.](http://docs.aws.amazon.com/connect/latest/adminguide/images/genai-augmented-data-mapping-breached-limit.png)


### Warning: We couldn't find a **unique key**, which distinguishes your data. We couldn't find a **profile key**, which identifies your profiles.
<a name="genai-powered-data-mapping-unique-key-warning"></a>

The model could not find a valid object type from given object. Change the input or use manual mapping approach as suggested.

![The model could not find a valid object type from given object. Change the input or use manual mapping approach as suggested.](http://docs.aws.amazon.com/connect/latest/adminguide/images/genai-augmented-data-mapping-unique-key-warning.png)

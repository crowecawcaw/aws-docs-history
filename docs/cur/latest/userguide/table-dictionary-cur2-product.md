

# Product columns
<a name="table-dictionary-cur2-product"></a>

Product columns contain data about the product that is being charged in the line item.



| Column name | Description | Data type | 
| --- | --- | --- | 
| product | A map column containing key-value pairs of multiple product attributes and their values for a given line item.<br />A product attribute only appears in the map column if it has a value that applies to the specific line item. Any product column that appeared in legacy CUR, but is not part of the CUR 2.0 static schema, appears in this map column. <br />The keys of this column can be queried as individual columns by using the dot operator. For more information, see [Data query](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-data-query.html).<br />For some AWS services, the map includes additional service-specific attributes. For the list of these attributes and the services that populate them, see [Service-specific product attributes](#table-dictionary-cur2-product-service-attributes). | map <string, string> | 
| product\_comment | A comment regarding the product. | string | 
| product\_fee\_code | The code that refers to the fee. | string | 
| product\_fee\_description | The description for the product fee. | string | 
| product\_from\_location | Describes the location where the usage originated from. | string | 
| product\_from\_location\_type | Describes the location type where the usage originated from. | string | 
| product\_from\_region\_code | Describes the source Region code for the AWS service. | string | 
| product\_instanceSKU | The SKU of the product instance | string | 
| product\_instance\_family | Describes your Amazon EC2 instance family. Amazon EC2 provides you with a large number of options across 10 different instance types, each with one or more size options, organized into distinct instance families optimized for different types of applications. | string | 
| product\_instance\_type | Describes the instance type, size, and family, which define the CPU, networking, and storage capacity of your instance. | string | 
| product\_location | Describes the Region that your Amazon S3 bucket resides in. | string | 
| product\_location\_type | Describes the endpoint of your task. | string | 
| product\_operation | Describes the specific AWS operation that this line item covers. | string | 
| product\_pricing\_unit | The smallest billing unit for an AWS service. For example, 0.01c per API call. | string | 
| product\_product\_family | The category for the type of product. For Amazon Bedrock line items, this is populated with the unified value Amazon Bedrock, so that all Amazon Bedrock usage can be identified under a single product family. | string | 
| product\_region\_code | A Region is a physical location around the world where data centers are clustered. AWS calls each group of logical data centers an Availability Zone (AZ). Each AWS Region consists of multiple, isolated, and physically separate AZs within a geographical area. The Region code attribute has the same name as an AWS Region, and specifies where the AWS service is available. | string | 
| product\_sku | A unique code for a product. The SKU is created by combining the `ProductCode`, `UsageType`, and `Operation`. For size-flexible RIs, the SKU uses the instance that was used. For example, if you used a `t2.micro` instance and AWS applied a `t2.small` RI discount to the usage, the line item SKU is created with the `t2.micro`. | string | 
| product\_servicecode | This identifies the specific AWS service to the customer as a unique short abbreviation. | string | 
| product\_to \_location\_type | Describes the destination location of the service usage. | string | 
| product\_to\_location | Describes the location usage destination. | string | 
| product\_to\_region\_code | Describes the source Region code for the AWS service. | string | 
| product\_usagetype | Describes the usage details of the line item. | string | 

## Service-specific product attributes
<a name="table-dictionary-cur2-product-service-attributes"></a>

For certain AWS services, the product map column includes additional standardized attributes that describe service-specific cost drivers beyond the static schema columns. These attributes are stored as keys within the product map rather than as static top-level columns, and you can query each one by using the dot operator (for example, product.provider). For more information about querying map keys, see [Data query](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-data-query.html).

These attributes let you filter, group, and compare costs along service-specific dimensions without parsing free-text description fields. For example, for Amazon Bedrock usage you can group costs by product.provider to compare spending across model providers, or by product.inference\_type to separate input token costs from output token costs.

The **Applies to** column indicates which AWS service populates each attribute.



| Map key | Description | Example values | Applies to | 
| --- | --- | --- | --- | 
| provider | The provider of the foundation model. | Amazon, Anthropic, Meta, Cohere | Amazon Bedrock | 
| model | The model name, corresponding to the model name shown in the Amazon Bedrock console Model catalog. | Claude 3.5 Sonnet, Nova Pro, Llama 3 | Amazon Bedrock | 
| inference\_type | The type of usage being metered (the token type). | input tokens, output tokens, image generation | Amazon Bedrock | 
| feature | The inference serving mode, describing how the request is processed. | On-Demand, Batch | Amazon Bedrock | 
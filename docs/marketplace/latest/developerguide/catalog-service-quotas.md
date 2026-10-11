

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Service quotas for AWS Marketplace Catalog API
<a name="catalog-service-quotas"></a>

The AWS Marketplace Catalog API has the following quotas.


**Request quotas**  

|  **API operations**  |  **Request rate (per AWS account)**  | 
| --- | --- | 
| ListEntities | 10 per second | 
| DescribeEntity | 20 per second | 
| StartChangeSet | 5 per second | 
| ListChangeSets | 5 per second | 
| DescribeChangeSet | 10 per second | 
| CancelChangeSet | 5 per second | 
| TagResource | 5 per second | 
| UntagResource | 5 per second | 
| ListTagsForResource | 5 per second | 
| PutResourcePolicy | 5 per second | 
| GetResourcePolicy | 5 per second | 
| DeleteResourcePolicy | 5 per second | 

If you are a third-party integration partner that calls the AWS Marketplace Catalog API on behalf of multiple seller accounts, your requests are also subject to the following per-integration-partner rate limits. These limits apply across all seller accounts you access. For best practices on working within these limits, see [Integration partner best practices](catalog-apis.md#integration-partner-best-practices).


**Integration partner rate limits**  

| **API operation** | **Request rate (per integration partner)** | 
| --- | --- | 
| ListEntities | 50 per second | 
| DescribeEntity | 100 per second | 
| StartChangeSet | 25 per second | 
| ListChangeSets | 25 per second | 
| DescribeChangeSet | 50 per second | 
| CancelChangeSet | 25 per second | 


**Product pricing dimension quotas**  

| **Description** | **Limit** | 
| --- | --- | 
| Maximum number of unique contract dimensions (also known as Entitled dimensions) that can be included in a private offer or public offer. Contract dimensions in offers count towards the maximum number of unique contract dimensions per product.  | 200 | 
| Maximum number of unique contract dimensions (also known as Entitled  dimensions) per product. This is inclusive of all unique contract dimensions in both private offers and public offers. Dimensions in the restricted state count towards this limit. | 200 | 
| Maximum number of unique usage dimensions (also known as ExternallyMetered dimensions) that can be included in a private offer or public offer. These usage dimensions in offers count towards the maximum number of unique usage dimensions per product. | 200 | 
| Maximum number of unique usage dimensions (also known as ExternallyMetered dimensions) per product. This is inclusive of all unique usage dimensions in both private offers and public offers. Dimensions in the restricted state count towards this limit.  | 200 | 


**Account quotas**  

|  **Quota**  |  **Description**  | 
| --- | --- | 
| Maximum number of open StartChangeSet requests per account | 250 | 
| Maximum number of Offers created or updated concurrently per account | 20 | 
| Maximum number of OfferSets created or updated concurrently per account | 20 | 


**Request history retention quotas**  

|  **Description**  |  **Quota**  | 
| --- | --- | 
| Retention period for change requests. This applies after the end time of each change request. | 90 days | 

**Note**  
 Change requests and entities are different. Entities exist perpetually regardless of their type or state. For example, [seller product](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-seller-products.html), [offer](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-private-offers.html), [resale authorization](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-resale-authorizations.html), and [private marketplace experience](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-private-marketplace.html) *entities* are never deleted even if they are in the draft state.
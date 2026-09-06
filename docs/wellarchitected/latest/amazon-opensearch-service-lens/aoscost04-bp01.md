

# AOSCOST04-BP01 Apply cost allocation tags to your OpenSearch resources for detailed cost tracking and analysis
<a name="aoscost04-bp01"></a>

 Improve cost visibility and enhance financial reporting by applying cost allocation tags to track and analyse costs associated with each resource in your OpenSearch Service domain. 

 **Level of risk exposed if this best practice is not established:** Low 

 **Desired outcome**: Cost allocation tags are applied to enable detailed cost tracking and analysis of your OpenSearch Service domain. 

 **Benefits of establishing this best practice:** 
+  **Improved cost visibility**: Applying cost allocation tags to Amazon OpenSearch Service resources enables detailed cost tracking and analysis using AWS Cost Explorer, providing a clear understanding of costs associated with each resource. 
+  **Enhanced financial reporting**: By categorizing workloads using key-value pairs (for example, environment, project, department), you can provide accurate financial reporting and separate costs for better expense management. 

## Implementation guidance
<a name="implementation-guidance-54"></a>
+  Assign unique tags to your OpenSearch Service domains, and use key-value pairs to categorize workloads by attributes such as environment (like development, production, and QA testing), project, or department. 
+  Use tags to track cost usage and manage expenses with AWS Cost Explorer. This best practice helps you segment your costs and improve the accuracy of your financial reporting. 
+  For more detail on tagging, see [Tagging OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html). 

## Resources
<a name="resources-53"></a>
+  [Using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) 
+  [What is AWS Billing and Cost Management and Cost Management?](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html) 
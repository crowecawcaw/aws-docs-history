

# AOSSUS03-BP02 Reduce unnecessary or redundant data from your domain
<a name="aossus03-bp02"></a>

 Reduce storage costs, improve resource utilization, and enhance resource management by removing unnecessary or redundant data from your domain. 

 **Level of risk exposed if this best practice is not established:** Medium 

 **Desired outcome:** You have removed unnecessary or redundant data from your domain to support sustainability goals. 

 **Benefits of establishing this best practice:** 
+  Reduced storage costs and increased cost efficiency 
+  Improved resource utilization and reduced waste 
+  Enhanced ability to manage and optimize resources 

## Implementation guidance
<a name="implementation-guidance-61"></a>

 You can reduce unneeded and redundant data through various methods, like using indexing strategies, implementing ISM, and archiving data. 
+  Run `_cat/indices?v` to list your indices 
+  Use `DELETE /<index-name>` to remove unnecessary or redundant indices 

## Resources
<a name="resources-61"></a>
+  [Index State Management in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism.html) 
+  [Cat Indices](https://opensearch.org/docs/latest/api-reference/cat/cat-indices/) 
+  [Delete Index](https://opensearch.org/docs/latest/api-reference/index-apis/delete-index/) 
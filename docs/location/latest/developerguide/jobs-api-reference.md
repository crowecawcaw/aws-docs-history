

# Jobs APIs
<a name="jobs-api-reference"></a>

The Amazon Location Jobs APIs provide programmatic access to bulk address validation capabilities through REST endpoints. All operations use standard AWS authentication.
+ **StartJob**: Initiates a new Amazon Location bulk processing job. For more information, See [StartJob](start-job-api.md).
+ **GetJob**: Retrieves comprehensive information about a specific job. For more information, See [GetJob](get-job-api.md).
+ **CancelJob**: Stops a running or pending job. For more information, See [CancelJob](cancel-job-api.md).
+ **ListJobs**: Retrieves a paginated list of jobs. For more information, See [ListJobs](list-jobs-api.md).

The following table presents business use cases that you can solve using Jobs API actions. Currently, `ValidateAddress` is the only supported action.


| **Business need** | **Job action** | 
| --- | --- | 
|  +  **Healthcare systems and insurers:** Validate patient and provider addresses for claims processing, care coordination, and regulatory reporting requirements. <br />+  **Financial services and insurance carriers:** Standardize customer addresses to support identity verification workflows, risk assessment, and fraud prevention. <br />+  **Retail and e-commerce operations:** Clean customer databases to reduce shipping failures, improve delivery rates, and optimize fulfillment costs. <br />+  **Transportation and logistics providers:** Validate delivery addresses to optimize routes and reduce failed deliveries across last-mile operations. <br />+  **Data migration and database maintenance:** Validate and clean address records during system migrations and ongoing database maintenance to maintain data quality. <br />+  **Analytics, reporting, and entity resolution:** Standardize addresses for location-based analytics, demographic analysis, and Customer Relationship Management (CRM) database cleanup through entity resolution workflows.  | `ValidateAddress` | 
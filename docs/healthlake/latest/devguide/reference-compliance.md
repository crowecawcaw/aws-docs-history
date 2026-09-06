

# Compliance reference for AWS HealthLake
<a name="reference-compliance"></a>

AWS HealthLake provides features designed to help you track and report API usage in alignment with CMS (Centers for Medicare & Medicaid Services) interoperability requirements. These features enable you to categorize API transactions by CMS-mandated categories and automatically capture usage metrics for compliance reporting purposes.

**Understanding Your Compliance Responsibilities**  
Using AWS HealthLake and its CMS interoperability endpoints is **not sufficient on its own** to achieve CMS compliance. You are responsible for:  
Correctly mapping your API workflows to the appropriate CMS category endpoints based on your specific use cases and regulatory obligations
Implementing proper authentication and authorization controls that meet CMS requirements
Ensuring your FHIR resources and data exchanges comply with applicable CMS regulations and implementation guides
Configuring and monitoring the CloudWatch metrics to support your compliance reporting needs
Understanding which CMS rules apply to your organization and implementing the appropriate technical and operational controls

AWS HealthLake provides the infrastructure and tooling to support your compliance efforts, but you must use these features appropriately based on your specific regulatory requirements. Simply routing API calls through these endpoints does not automatically make your application compliant with CMS regulations.

**Topics**
+ [CMS](reference-compliance-cms.md)
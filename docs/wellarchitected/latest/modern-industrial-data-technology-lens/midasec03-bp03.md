

# MIDASEC03-BP03 Identify source data and set data classifications
<a name="midasec03-bp03"></a>

 Discover and classify data at the source (for example, sensors, PLCs, MES, and ERP systems) to apply appropriate controls from ingestion onward. 

 **Desired outcome:** Data is classified and governed from the moment it enters the system, helping prevent downstream risk exposure. 

 **Benefits of establishing this best practice:** Improves control over high-risk data, simplifies pipeline security, and enhances lineage tracking and compliance auditing. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-16"></a>

 Build data ingestion pipelines with tagging and classification integrated into the ingestion and cataloging layers. 

### Implementation steps
<a name="implementation-steps-17"></a>
+  Identify all upstream data sources contributing to the system. 
+  Use edge and gateway services to apply initial metadata or tags. 
+  Ingest data into AWS using services like Amazon Kinesis, AWS IoT Core, or AWS IoT SiteWise with classification. 
+  Catalog and tag datasets in AWS Glue or AWS Lake Formation. 

## Resources
<a name="resources-17"></a>
+  [AWS Lake Formation](https://aws.amazon.com/lake-formation/) 
+  [AWS Glue](https://aws.amazon.com/glue/) 
+  [ What is AWS IoT SiteWise? ](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html) 


# DSSEC07-BP03 Track data lineage
<a name="dssec07-bp03"></a>

 Organizations in highly regulated industries implement data lineage tracking to demonstrate that data localization, data residency, and data privacy requirements are met. Data lineage provides visibility of the complete journey of data from source to consumption. This capability becomes essential for demonstrating audit readiness and maintaining trust in data-driven decision making. 

 **Desired outcome:** 
+  Data movement, transformations, and dependencies are tracked automatically across data pipelines through lineage capabilities. 
+  Organizations maintain visibility into data flows and possess audit-ready documentation of data handling practices. 

 **Common anti-patterns:** 
+  Manual lineage documentation that becomes outdated quickly and fails to capture real-time data transformations and dependencies. 
+  Siloed lineage tracking that only covers specific tools or solutions without providing full visibility across the data estate. 
+  Reactive lineage capture that attempts to reconstruct data flows after issues occur rather than proactively tracking lineage during data processing. 

 **Benefits of establishing this best practice:** 
+  Enhanced regulatory adherence through detailed audit trails that demonstrate data handling practices and support regulatory reporting requirements. 
+  Improved data governance by providing visibility into data quality, transformation logic, and impact analysis for schema changes and system modifications. 
+  Increased data trust by enabling data consumers to understand data origins, transformation history, and quality measures before making business decisions. 
+  Reduced compliance costs through automated documentation and audit trail generation that removes manual effort and reduces audit preparation time. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Establish a data lineage tracking strategy. Implement automated lineage capture using AWS services. Use services that integrate with your existing data processing tools and solutions. Deploy a centralized lineage repository that can store, query, and visualize complex data relationships and integrate with governance tools. 

 Key AWS services for data lineage implementation include Amazon SageMaker AI Catalog — the governance capability of Amazon SageMaker AI Unified Studio, built on Amazon DataZone — for centralized governance and lineage visualization, and AWS Glue for automated lineage capture from extract, transform, and load (ETL) processes. The same lineage capability remains available directly in Amazon DataZone. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assess current data environment and lineage requirements**: Conduct an inventory of your data sources, processing systems, and consumption patterns. Identify critical data flows that require lineage tracking based on regulatory requirements, business criticality, and data sensitivity levels. Document data classification levels and associated lineage requirements: 
   +  **Highly sensitive data**: Full column-level lineage with transformation details 
   +  **Regulated data**: Table-level lineage with processing metadata 
   +  **Internal data**: Basic flow tracking with key transformation points 

1.  **Enable data lineage in Amazon SageMaker AI Catalog or Amazon DataZone**: Amazon SageMaker AI Catalog (built on Amazon DataZone) and Amazon DataZone both provide OpenLineage-compatible lineage that you can capture and visualize across your data estate. This strengthens your data privacy posture in several ways. First, column-level lineage traces exactly where sensitive data (such as personally identifiable information (PII)) is stored and how it is processed in downstream activities, providing the transparency required to demonstrate compliance with data privacy legislation such as GDPR. Second, lineage versioning creates a historical audit trail of how data has been transformed over time, supporting data subject access requests and regulatory inquiries by documenting the chain of custody for personal data. Third, by visualizing upstream and downstream dependencies, lineage helps you assess the impact of changes to data pipelines on privacy-sensitive data flows before those changes are made, reducing the risk of unintended exposure. Follow the [Amazon SageMaker AI Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/datazone-data-lineage.html) or [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/datazone-data-lineage.html) documentation to enable lineage. See the resources (Related documents) section for additional technical measures you can apply. 

1.  **Add cross-border data flow tracking**: Use these data lineage capabilities to track and document cross-border data transfers. Lineage events captured through the PostLineageEvent API record the flow of data between source and target systems as standard OpenLineage run events. For AWS resources (such as AWS Glue tables or Amazon Redshift tables), the AWS Region is embedded in the resource ARN that is the lineage node's sourceIdentifier (for example, arn:aws:glue:<region>:<account-id>:table/<database>/<table-name>). This means the source and target regions can be derived directly from the upstream and downstream lineage nodes. The resulting lineage records can then be queried through the GetLineageNode and ListLineageNodeHistory APIs to support compliance analysis, for example, verifying that source and target resources reside within the same jurisdiction, or flagging transfers that cross regulatory boundaries. 

1.  **Protect lineage metadata with the same rigor as the data it describes**: Lineage metadata might reveal sensitive information, including data relationships, transformation logic, and access patterns that are security-sensitive. Implement access controls on lineage data and encrypt lineage metadata at rest. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC07-BP01 Understand your data classification scheme](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_identify_data.html) 
+  [SEC07-BP02 Apply data protection controls based on data sensitivity](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_define_protection.html) 
+  [SEC07-BP03 Automate identification and classification](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_auto_classification.html) 
+  [SEC07-BP04 Define scalable data lifecycle management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_lifecycle_management.html) 

 **Related documents:** 
+  [Building end-to-end data lineage for one-time and complex queries using Amazon Athena, Amazon Redshift, Amazon Neptune, and dbt](https://aws.amazon.com/blogs/big-data/building-end-to-end-data-lineage-for-one-time-and-complex-queries-using-amazon-athena-amazon-redshift-amazon-neptune-and-dbt/) 
+  [Capture data lineage from dbt, Apache Airflow, and Apache Spark with Amazon SageMaker AI](https://aws.amazon.com/blogs/big-data/capture-data-lineage-from-dbt-apache-airflow-and-apache-spark-with-amazon-sagemaker/) 
+  [Announcing the general availability of data lineage in the next generation of Amazon SageMaker AI and Amazon DataZone](https://aws.amazon.com/blogs/aws/announcing-the-general-availability-of-data-lineage-in-the-next-generation-of-amazon-sagemaker-and-amazon-datazone/) 
+  [Automate data lineage in Amazon SageMaker AI using AWS Glue crawlers supported data sources](https://aws.amazon.com/blogs/big-data/automate-data-lineage-in-amazon-sagemaker-using-aws-glue-crawlers-supported-data-sources/) 
+  [Build data lineage for data lakes using AWS Glue, Amazon Neptune, and Spline](https://aws.amazon.com/blogs/big-data/build-data-lineage-for-data-lakes-using-aws-glue-amazon-neptune-and-spline/) 
+  [Enhance data governance through column-level lineage in Quick](https://aws.amazon.com/blogs/business-intelligence/enhance-data-governance-through-column-level-lineage-in-amazon-quicksight/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Empower your data journey with Amazon DataZone's data lineage (ANT207-NEW)](https://www.youtube.com/watch?v=p9h2JJSLq4c) 
+  [AWS Summit Tel Aviv 2024 - Tracing Data from Streaming to Iceberg Lakes with OpenLineage (DEM301) - In Hebrew](https://www.youtube.com/watch?v=W4dyBnXpYRk) 

 **Related services:** 
+  [Amazon DataZone](https://aws.amazon.com/datazone/) 
+  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) 
+  [AWS Glue](https://aws.amazon.com/glue/) 
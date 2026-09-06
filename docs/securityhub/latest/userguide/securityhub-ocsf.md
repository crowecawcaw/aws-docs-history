

# Security Hub and the Open Cybersecurity Schema Framework (OCSF)
<a name="securityhub-ocsf"></a>

 Security Hub uses the Open Cybersecurity Schema Framework (OCSF) as the standard format for all security findings. This topic describes OCSF and how Security Hub implements it. 

## OCSF overview
<a name="ocsf-overview"></a>

 Security Hub findings are formatted using OCSF (Open Cybersecurity Schema Framework). OCSF is an open-source project that delivers an extensible framework for developing schemas, along with a vendor-agnostic core security schema. Vendors and other data producers can adopt and extend the schema for their specific domains. Data producers can map differing schemas to help security teams simplify data ingestion and normalization, so that data scientists and analysts can work with a common language for threat detection and investigation. The goal is to provide an open standard, adopted in any environment, application, or solution, while complementing existing security standards and processes. 

 The framework consists of data types, an attribute dictionary, and a taxonomy. Although not limited to cybersecurity or events, the initial focus is on cybersecurity event schemas. OCSF is independent of storage format, data collection methods, and ETL processes. 

 Security Hub currently supports findings in OCSF schema version 1.6. 

## Related resources
<a name="related-resources"></a>

 For more information about OCSF and its implementation, see the following resources: 
+ [Public OCSF Documentation](https://schema.ocsf.io/)
+ [OCSF Extension Usage Documentation](https://schema.ocsf.io/1.0.0/extensions/)
+ [OCSF Core Schema Reference](https://schema.ocsf.io/1.0.0/)
+ [OCSF Extensions Registry](https://github.com/ocsf/ocsf-schema/tree/main/extensions)
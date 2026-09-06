

# SAP workload tags
<a name="SAP-tags"></a>

Use the following tables for migration plans using MAP 2.0 for SAP Migration.



## Short MPE IDs
<a name="sap-tags-short-ids"></a>


**SAP workload tags with short ID**  

| Source | Destination | Tag key | Tag value | 
| --- | --- | --- | --- | 
| On-premises | AWS | map-migrated | sap{{5-digit MPE ID}} | 

## Long MPE IDs
<a name="sap-tags-long-ids"></a>


**SAP workload tags with long ID**  

| Source | Destination | Tag key | Tag value | 
| --- | --- | --- | --- | 
| On-premises | AWS | map-migrated | sap{{10 alphanumeric MPE ID characters}} | 



**Note**  
The prefix for SAP workload tags is `sap`. Do not use this tag for migration plans that are not part of MAP 2.0 for SAP. Use uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md).



Ensure you define the MAP tags as part of your infrastructure definition when using the AWS Launch Wizard for SAP to deploy your SAP workloads. For more information about the AWS Launch Wizard for SAP, see [Deploy an SAP application with AWS Launch Wizard](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-deploying.html) in the *AWS Launch Wizard user guide*. For a complete list of services included in MAP 2.0 for SAP, see the MAP 2.0 Included Services list: **https://s3-us-west-2.amazonaws.com/map-2.0-customer-documentation/included-services/MAP\_Included\_Services\_List.pdf**. 
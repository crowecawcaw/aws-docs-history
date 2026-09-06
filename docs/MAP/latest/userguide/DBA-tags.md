

# Database and analytics tags
<a name="DBA-tags"></a>

Use the following tables for migration plans whose Migration Tracking and Incentive Guide includes database and analytics MAP credits. 



## Short MPE IDs
<a name="dba-short-ids"></a>


**Database and analytics tags with short IDs**  

| Source | Destination | Tag key | Tag value | 
| --- | --- | --- | --- | 
| On-premises Commercial DB&A  | Any AWS DB&A Service  | map-migrated | comm{{5-digit MPE ID}} | 
| On-premises non-commercial DB&A | Any AWS DB&A Service  | map-migrated | mig{{5-digit MPE ID}} | 
| On-premises Commercial DB&A | EC2 | map-migrated | mig{{5-digit MPE ID}} | 
| On-premises non-commercial DB&A | EC2 | map-migrated | mig{{5-digit MPE ID}} | 
| EC2 Commercial DB&A | Any AWS DB&A Service  | map-migrated | comm\_ec2\_{{5-digit MPE ID}} | 
| EC2 non-commercial DB&A | Any AWS DB&A Service  | map-migrated | mig\_ec2\_{{5-digit MPE ID}} | 

## Long MPE IDs
<a name="dba-long-ids"></a>


**Database and analytics tags with long IDs**  

| Source | Destination | Tag key | Tag value | 
| --- | --- | --- | --- | 
| On-premises Commercial DB&A  | Any AWS DB&A Service  | map-migrated | comm{{10 alphanumeric MPE ID characters}} | 
| On-premises non-commercial DB&A | Any AWS DB&A Service  | map-migrated | mig{{10 alphanumeric MPE ID characters}} | 
| On-premises Commercial DB&A | EC2 | map-migrated | mig{{10 alphanumeric MPE ID characters}} | 
| On-premises non-commercial DB&A | EC2 | map-migrated | mig{{10 alphanumeric MPE ID characters}} | 
| EC2 Commercial DB&A | Any AWS DB&A Service  | map-migrated | comm\_ec2\_{{10 alphanumeric MPE ID characters}} | 
| EC2 non-commercial DB&A | Any AWS DB&A Service  | map-migrated | mig\_ec2\_{{10 alphanumeric MPE ID characters}} | 



**Note**  
Use lowercase letters for the `comm`, `mig`, `comm_ec2_`, and `mig_ec2_` prefixes and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md).



A commercial database is defined as any third-party database engine, data warehouse, or analytics offering for which you have paid a fee for use rights, enhancements, maintenance, or support for that third party offering. A non-commercial database is defined as any third-party database engine, data warehouse, or analytics offering for which you have not paid a fee for use rights, enhancements, maintenance, or support for that third party offering. For a complete list of services that are included in MAP – Database & Analytics (DB&A), see the MAP 2.0 Included Services list: **https://s3-us-west-2.amazonaws.com/map-2.0-customer-documentation/included-services/MAP\_Included\_Services\_List.pdf**. 



## Special scenario
<a name="special-scenario"></a>

If your destination database is changed from EC2 to any AWS DB&A service after your initial migration, then use the following tables to tag your DB&A service. 



### Short MPE IDs
<a name="dba-special-short-ids"></a>


**EC2 to database and analytics tags with short IDs after migration**  

| Source | Destination | Tag key | Tag value | 
| --- | --- | --- | --- | 
| EC2 Commercial DB&A | Any AWS DB&A Service  | map-migrated | comm{{5-digit MPE ID}} | 
| EC2 non-commercial DB&A | Any AWS DB&A Service  | map-migrated | mig{{5-digit MPE ID}} | 

### Long MPE IDs
<a name="dba-special-long-ids"></a>


**EC2 to database and analytics tags with long IDs after migration**  

| Source | Destination | Tag key | Tag value | 
| --- | --- | --- | --- | 
| EC2 Commercial DB&A | Any AWS DB&A Service  | map-migrated | comm{{10 alphanumeric MPE ID characters}} | 
| EC2 non-commercial DB&A | Any AWS DB&A Service  | map-migrated | mig{{10 alphanumeric MPE ID characters}} | 

**Note**  
Use lowercase letters for the `comm` and `mig` prefixes and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md).
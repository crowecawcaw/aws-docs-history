

# Database and analytics tags

Use the following tables for migration plans whose Migration Tracking and Incentive Guide includes database and analytics MAP credits.




**Database and analytics tags**  

| Source | Destination | Tag key | Tag value | 
| --- | --- | --- | --- | 
| On-premises Commercial DB&A | Any AWS DB&A Service | aws-apn-id | comm{{PRM ID}} | 
| On-premises non-commercial DB&A | Any AWS DB&A Service | aws-apn-id | mig{{PRM ID}} | 
| On-premises Commercial DB&A | EC2 | aws-apn-id | comm{{PRM ID}} | 
| On-premises non-commercial DB&A | EC2 | aws-apn-id | mig{{PRM ID}} | 
| EC2 Commercial DB&A | Any AWS DB&A Service | aws-apn-id | comm\_ec2\_{{PRM ID}} | 
| EC2 non-commercial DB&A | Any AWS DB&A Service | aws-apn-id | mig\_ec2\_{{PRM ID}} | 



**Note**  
Use lowercase letters for the `mig`, `mig_ec2_`, `comm`, and `comm_ec2_` prefixes. For more information about your PRM ID, see [PRM ID length](mpe-length.md).



A commercial database is defined as any third-party database engine, data warehouse, or analytics offering for which you have paid a fee for use rights, enhancements, maintenance, or support for that third party offering. A non-commercial database is defined as any third-party database engine, data warehouse, or analytics offering for which you have not paid a fee for use rights, enhancements, maintenance, or support for that third party offering. For a complete list of services that are included in MAP – Database & Analytics (DB&A), see the MAP 2.0 Included Services list: **https://s3-us-west-2.amazonaws.com/map-2.0-customer-documentation/included-services/MAP\_Included\_Services\_List.pdf**.
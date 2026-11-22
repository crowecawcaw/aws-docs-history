

# Oracle tags

Use the following tables for migration plans using MAP 2.0 for Oracle Migration.




**Oracle workload tags**  

| Source | Destination | Tag key | Tag value | 
| --- | --- | --- | --- | 
| On-premises | AWS | aws-apn-id | oracle{{PRM ID}} | 



**Note**  
The prefix for Oracle workload tags is `oracle`. Do not use this tag for migration plans that are not part of MAP 2.0 for Oracle. For more information about your PRM ID, see [PRM ID length](mpe-length.md).



Ensure you define the MAP tags as part of your infrastructure definition when using the AWS Launch Wizard to deploy your Oracle workloads. For more information about the AWS Launch Wizard, see [Get started with AWS Launch Wizard](https://docs.aws.amazon.com/launchwizard/latest/userguide/what-is-launch-wizard.html) in the *AWS Launch Wizard user guide*. For a complete list of services included in MAP 2.0 for Oracle, see the MAP 2.0 Included Services list: **https://s3-us-west-2.amazonaws.com/map-2.0-customer-documentation/included-services/MAP\_Included\_Services\_List.pdf**. 
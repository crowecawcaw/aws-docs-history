

# Other examples

Use the following examples to further help you tag your migrated workloads.

## Example 1: Re-hosting using AWS Transform MGN (MGN)
<a name="Example1"></a>

Use this example if you are moving from on-premises to AWS using a lift-and-shift (re-hosting) migration pattern, and decided to use MGN for the migration.




**Re-hosting using MGN example**  

| Tag key (automated) | Tag value (automated) | 
| --- | --- | 
| aws-apn-id | mig{{PRM ID}} | 

**Note**  
Use lowercase letters for the `mig` prefix . For more information about your PRM ID, see [PRM ID length](mpe-length.md).



## Example 2: DataCenter Migration (mix of migration patterns)
<a name="Example2"></a>

Use this example if you are moving different workloads from on-premises to AWS using various migration patterns (re-hosting, re-architecting, etc.) as part of general MAP.




**DataCenter migration (mix of migration patterns) example**  

| Tag key | Tag value | 
| --- | --- | 
| aws-apn-id | mig{{PRM ID}} | 

**Note**  
Use lowercase letters for the `mig` prefix . For more information about your PRM ID, see [PRM ID length](mpe-length.md).



## Example 3: Migrate commercial database from EC2 to RDS
<a name="Example3"></a>

Use this example if you are moving a commercial database from Amazon EC2 instances on AWS to Amazon RDS as part of MAP for Database and Analytics.




**Migrate commercial database from EC2 to RDS example**  

| Tag key | Tag value | 
| --- | --- | 
| aws-apn-id | comm\_ec2\_{{PRM ID}} | 

**Note**  
Use lowercase letters for the `comm_ec2_` prefix. For more information about your PRM ID, see [PRM ID length](mpe-length.md).



## Example 4: Database modernization
<a name="Example4"></a>

Use this example if you are moving on-premises commercial database server to Amazon DynamoDB. This example is for a Migration Plan that is eligible for Database & Analytics MAP Credits.




**Database modernization example**  

| Tag key | Tag value | 
| --- | --- | 
| aws-apn-id | comm{{PRM ID}} | 

**Note**  
Use lowercase letters for the `comm` prefix. For more information about your PRM ID, see [PRM ID length](mpe-length.md).


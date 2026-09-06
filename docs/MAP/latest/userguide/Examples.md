

# Other examples
<a name="Examples"></a>

Use the following examples to further help you tag your migrated workloads.

## Example 1: Re-hosting using AWS Transform MGN (MGN)
<a name="Example1"></a>

Use this example if you are moving from on-premises to AWS using a lift-and-shift (re-hosting) migration pattern, and decided to use MGN for the migration.



### Short MPE IDs
<a name="mgn-setup-short-ids"></a>


**Re-hosting using MGN with short ID example**  

| Tag key (automated) | Tag value (automated) | 
| --- | --- | 
| map-migrated | mig{{5-digit MPE ID}} | 

### Long MPE IDs
<a name="mgn-setup-long-ids"></a>


**Re-hosting using MGN with long ID example**  

| Tag key (automated) | Tag value (automated) | 
| --- | --- | 
| map-migrated | mig{{10 alphanumeric MPE ID characters}} | 

**Note**  
Use lowercase letters for the `mig` prefix and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md).



## Example 2: DataCenter Migration (mix of migration patterns)
<a name="Example2"></a>

Use this example if you are moving different workloads from on-premises to AWS using various migration patterns (re-hosting, re-architecting, etc.) as part of general MAP.



### Short MPE IDs
<a name="cfn-setup-short-ids"></a>


**DataCenter migration (mix of migration patterns) with short ID example**  

| Tag key | Tag value | 
| --- | --- | 
| map-migrated | mig{{5-digit MPE ID}} | 

### Long MPE IDs
<a name="cfn-setup-long-ids"></a>


**DataCenter migration (mix of migration patterns) with long ID example**  

| Tag key | Tag value | 
| --- | --- | 
| map-migrated | mig{{10 alphanumeric MPE ID characters}} | 

**Note**  
Use lowercase letters for the `mig` prefix and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md).



## Example 3: Migrate commercial database from EC2 to RDS
<a name="Example3"></a>

Use this example if you are moving a commercial databases from Amazon EC2 instances on AWS to Amazon RDS as part of MAP for Database and Analytics.



### Short MPE IDs
<a name="cdk-setup-short-ids"></a>


**Migrate commercial database from EC2 to RDS with short ID example**  

| Tag key | Tag value | 
| --- | --- | 
| map-migrated | comm\_ec2\_{{5-digit MPE ID}} | 

### Long MPE IDs
<a name="cdk-setup-long-ids"></a>


**Migrate commercial database from EC2 to RDS with long ID example**  

| Tag key | Tag value | 
| --- | --- | 
| map-migrated | comm\_ec2\_{{10 alphanumeric MPE ID characters}} | 

**Note**  
Use lowercase letters for the `comm_ec2_` prefix and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md).



## Example 4: Database modernization
<a name="Example4"></a>

Use this example if you are moving from on-premises commercial database server to Amazon DynamoDB. This example is for a Migration Plan that is eligible for Database & Analytics MAP Credits.



### Short MPE IDs
<a name="tageditor-setup-short-ids"></a>


**Database modernization with short ID example**  

| Tag key | Tag value | 
| --- | --- | 
| map-migrated | comm{{5-digit MPE ID}} | 

### Long MPE IDs
<a name="tageditor-setup-long-ids"></a>


**Database modernization with long ID example**  

| Tag key | Tag value | 
| --- | --- | 
| map-migrated | comm{{10 alphanumeric MPE ID characters}} | 

**Note**  
Use lowercase letters for the `comm` prefix and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md).
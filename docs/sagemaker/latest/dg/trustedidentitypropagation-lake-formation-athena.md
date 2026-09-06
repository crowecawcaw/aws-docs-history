

# Connect Studio JupyterLab notebooks to Lake Formation and Athena with trusted identity propagation enabled
<a name="trustedidentitypropagation-lake-formation-athena"></a>

AWS Lake Formation and Amazon Athena work together to provide a comprehensive data lake solution with fine-grained access control and serverless query capabilities. Lake Formation centralizes permissions management for your data lake, while Athena provides interactive query services. When integrated with trusted identity propagation, this combination enables data scientists to access only the data they're authorized to see, with all queries and data access automatically logged for compliance and auditing purposes. The following page provides information and instructions on how to connect trusted identity propagation with Amazon SageMaker Studio to Lake Formation and Athena

To connect Studio to Lake Formation and Athena with trusted identity propagation enabled, ensure you have completed the following setups:
+  [Setting up trusted identity propagation for Studio](trustedidentitypropagation-setup.md) 
+  [Create a Lake Formation role](https://docs.aws.amazon.com/lake-formation/latest/dg/prerequisites-identity-center.html) 
+  [Connect Lake Formation with IAM Identity Center](https://docs.aws.amazon.com/lake-formation/latest/dg/connect-lf-identity-center.html) 
+ Create Lake Formation resources:
  +  [Database](https://docs.aws.amazon.com/lake-formation/latest/dg/creating-database.html) 
  +  [Tables](https://docs.aws.amazon.com/lake-formation/latest/dg/creating-tables.html) 
+  [Create Athena workgroup](https://docs.aws.amazon.com/athena/latest/ug/creating-workgroups.html) 
  + Choose **AthenaSQL** for the engine
  + Choose **IAM Identity Center** for authentication method
  + Create a new service role
    + Ensure that the IAM Identity Center users have access to the query result location using Amazon S3 Access Grants
+  [Granting database permissions using the named resource method](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-database-permissions.html) 
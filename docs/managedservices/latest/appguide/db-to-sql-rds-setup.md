# Setting up

Complete these tasks to begin the import process.

1. Submit an RFC to create an RDS stack using Deployment | Advanced stack components | RDS database stack | Create (ct-2z60dyvto9g6c).
   _Do not use the target DB name_ (`RDSDBName` parameter) in
   the creation request, the target DB will be created during the import. Make sure to allow enough space (`RDSAllocatedStorage` parameter).
   For details on doing this, see the AMS Change Management Guide
   [RDS DB Stack | Create](../ctref/deployment-advanced-rds-database-stack-create.md "../ctref/deployment-advanced-rds-database-stack-create.md").
2. Submit an RFC to create the transit S3 bucket (if does not exist already) using Deployment | Advanced stack components | S3 storage | Create
   (ct-1a68ck03fn98r). For details on doing this, see the AMS Change Management Guide
   [S3 Storage | Create](../ctref/deployment-advanced-s3-storage-create.md "../ctref/deployment-advanced-s3-storage-create.md").
3. Submit a Management | Other | Other | Update (ct-1e1xtak34nx76) RFC to implement the `customer_rds_s3_role` with these details:

In the console:

    * Subject: "To support MS SQL Server Database Import, implement `customer_rds_s3_role` on this account.
    * Transit S3 bucket name: `BUCKET_NAME`.
    * Contact information: `EMAIL`.

With an ImportDbParams.json file for the CLI:

```
{
       "Comment": "{"Transit S3 bucket name":"`BUCKET_NAME`"}",
       "Priority": "High"
     }
}
```

4. Submit a Management | Other | Other | Update RFC requesting AMS to set the `SQLSERVER_BACKUP_RESTORE` option to the RDS
   created in step 1 (use the stack ID from the step 1 output, and the `customer_rds_s3_role` IAM role in this request, in this request).
5. Submit an RFC to create an EC2 instance (you can use any existing EC2 or on-premise workstation/instances), and
   install Microsoft SQL Management Studio on the instance.

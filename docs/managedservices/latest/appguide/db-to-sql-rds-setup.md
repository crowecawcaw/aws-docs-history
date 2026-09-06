

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Setting up
<a name="db-to-sql-rds-setup"></a>

Complete these tasks to begin the import process.

1. Submit an RFC to create an RDS stack using Deployment \| Advanced stack components \| RDS database stack \| Create (ct-2z60dyvto9g6c). *Do not use the target DB name* (`RDSDBName` parameter) in the creation request, the target DB will be created during the import. Make sure to allow enough space (`RDSAllocatedStorage` parameter). For details on doing this, see the AMS Change Management Guide [RDS DB Stack \| Create](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-rds-database-stack-create.html).

1. Submit an RFC to create the transit S3 bucket (if does not exist already) using Deployment \| Advanced stack components \| S3 storage \| Create (ct-1a68ck03fn98r). For details on doing this, see the AMS Change Management Guide [S3 Storage \| Create](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-s3-storage-create.html).

1. Submit a Management \| Other \| Other \| Update (ct-1e1xtak34nx76) RFC to implement the `customer_rds_s3_role` with these details:

   In the console:
   + Subject: "To support MS SQL Server Database Import, implement `customer_rds_s3_role` on this account.
   + Transit S3 bucket name: {{BUCKET\_NAME}}.
   + Contact information: {{EMAIL}}.

   With an ImportDbParams.json file for the CLI:

   ```
   {
          "Comment": "{"Transit S3 bucket name":"{{BUCKET_NAME}}"}",
          "Priority": "High"
        }
   }
   ```

1. Submit a Management \| Other \| Other \| Update RFC requesting AMS to set the `SQLSERVER_BACKUP_RESTORE` option to the RDS created in step 1 (use the stack ID from the step 1 output, and the `customer_rds_s3_role` IAM role in this request, in this request).

1. Submit an RFC to create an EC2 instance (you can use any existing EC2 or on-premise workstation/instances), and install Microsoft SQL Management Studio on the instance.
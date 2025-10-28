# Cleanup

Once you have imported the database, you might want to remove unnecessary resources, follow these steps.

1. Delete the backup file (.bak) from the S3 bucket. You can use the S3 console to do this. For the CLI command to delete an object
   from an S3 bucket, see [rm](../../../cli/latest/reference/s3/rm.md "../../../cli/latest/reference/s3/rm.md") in the AWS CLI Command Reference.
2. Delete the S3 bucket if you’re not planning to use it. For steps on doing that, see [Delete Stack](../ctref/ex-stack-delete-col.md "../ctref/ex-stack-delete-col.md").
3. If you’re not planning to do MS SQL imports, submit a Management | Other | Other | Update (ct-0xdawir96cy7k) RFC and request that AMS delete
   the IAM role `customer_rds_s3_role`.

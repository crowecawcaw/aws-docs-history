

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Cleanup
<a name="db-to-sql-rds-cleanup"></a>

Once you have imported the database, you might want to remove unnecessary resources, follow these steps.

1. Delete the backup file (.bak) from the S3 bucket. You can use the S3 console to do this. For the CLI command to delete an object from an S3 bucket, see [rm](https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html) in the AWS CLI Command Reference.

1. Delete the S3 bucket if you’re not planning to use it. For steps on doing that, see [Delete Stack](https://docs.aws.amazon.com/managedservices/latest/ctref/ex-stack-delete-col.html).

1. If you’re not planning to do MS SQL imports, submit a Management \| Other \| Other \| Update (ct-0xdawir96cy7k) RFC and request that AMS delete the IAM role `customer_rds_s3_role`.
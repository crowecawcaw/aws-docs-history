

# Enabling RDS for SQL Server integration with S3
<a name="Appendix.SQLServer.Options.S3-integration.enabling"></a>

In the following section, you can find how to enable Amazon S3 integration with Amazon RDS for SQL Server. To work with S3 integration, your DB instance must be associated with the IAM role that you previously created before you use the `S3_INTEGRATION` feature-name parameter.

**Note**  
To add an IAM role to a DB instance, the status of the DB instance must be **available**.

## Console
<a name="Appendix.SQLServer.Options.S3-integration.enabling.console"></a>

**To associate your IAM role with your DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose the RDS for SQL Server DB instance name to display its details.

1. On the **Connectivity & security** tab, in the **Manage IAM roles** section, choose the IAM role to add for **Add IAM roles to this instance**.

1. For **Feature**, choose **S3\_INTEGRATION**.  
![Add the S3_INTEGRATION role.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/ora-s3-integration-role.png)

1. Choose **Add role**.

## AWS CLI
<a name="Appendix.SQLServer.Options.S3-integration.enabling.cli"></a>

**To add the IAM role to the RDS for SQL Server DB instance**
+ The following AWS CLI command adds your IAM role to an RDS for SQL Server DB instance named `{{mydbinstance}}`.  
**Example**  

  For Linux, macOS, or Unix:

  ```
  aws rds add-role-to-db-instance \
  	   --db-instance-identifier {{mydbinstance}} \
  	   --feature-name S3_INTEGRATION \
  	   --role-arn {{your-role-arn}}
  ```

  For Windows:

  ```
  aws rds add-role-to-db-instance ^
  	   --db-instance-identifier {{mydbinstance}} ^
  	   --feature-name S3_INTEGRATION ^
  	   --role-arn {{your-role-arn}}
  ```

  Replace `{{your-role-arn}}` with the role ARN that you noted in a previous step. `S3_INTEGRATION` must be specified for the `--feature-name` option.


# Configuring AWS Secrets Manager in the AWS Schema Conversion Tool
<a name="CHAP_UserInterface.SecretsManager"></a>

AWS SCT can use database credentials that you store in AWS Secrets Manager. You can fill in all values in the database connection dialog box from Secrets Manager. To use Secrets Manager, make sure that you store AWS profiles in the AWS Schema Conversion Tool.

For more information about using AWS Secrets Manager, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*. For more information about storing AWS profiles, see [Managing Profiles in the AWS Schema Conversion Tool](CHAP_UserInterface.Profiles.md).

**To retrieve database credentials from Secrets Manager**

1. Start the AWS Schema Conversion Tool and create a new project.

1. Choose **Add source** or **Add target** to add a new database to your project.

1. Choose a database platform and then choose **Next**.

1. For **AWS Secret**, choose the secret you want to use.

1. Choose **Populate**. Then AWS SCT fills in all values in the database connection dialog box.

1. Choose **Test connection** to verify that AWS SCT can connect to your database.

1. Choose **Connect** to connect to your database.

 AWS SCT supports secrets that have the following structure. 

```
{
  "username": "secret_user",
  "password": "secret_password",
  "engine": "oracle",
  "host": "secret_host.eu-west-1.compute.amazonaws.com",
  "port": "1521",
  "dbname": "ora_db"
}
```

In this structure, the `username` and `password` values are required, and all other values are optional. Make sure that the values that you store in Secrets Manager include all database credentials. 
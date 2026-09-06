

# Step 4: Store Database Credentials in AWS Secrets Manager
<a name="dm-postgresql-step-4"></a>

To connect to your source and target databases in an AWS DMS migration project, store your database credentials in AWS Secrets Manager. Make sure that you replicate these secrets to your AWS Region.

 **To store your source database credentials in AWS Secrets Manager ** 

1. Sign in to the AWS Management Console and open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose your AWS Region.

1. Choose **Store a new secret**. The **Choose secret type** page opens.

1. For **Secret type**, choose **Credentials for other database**.

1. For **User name** and **Password**, enter the credentials of the database user that you created for your source database in [Step 2](dm-postgresql-step-2.md).

1. For **Database**, choose **PostgreSQL**.

1. For **Server address**, **Database name**, and **Port**, enter your PostgreSQL database connection information.

1. Choose **Next**. The **Configure secret** page opens.

1. For **Secret name**, enter `dm-postgresql-source`.

1. Choose **Next**. The **Configure rotation** page opens.

1. Choose **Next**. The **Review** page opens.

1. Choose **Store**.

 **To store your target database credentials in AWS Secrets Manager ** 

1. Sign in to the AWS Management Console and open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose your AWS Region.

1. Choose **Store a new secret**. The **Choose secret type** page opens.

1. For **Secret type**, choose **Credentials for Amazon RDS database**.

1. For **User name** and **Password**, enter the credentials of the database user that you created for your target database in [Step 3](dm-postgresql-step-3.md).

1. For **Database**, choose your Amazon RDS for PostgreSQL DB instance.

1. Choose **Next**. The **Configure secret** page opens.

1. For **Secret name**, enter `dm-postgresql-target`.

1. Choose **Next**. The **Configure rotation** page opens.

1. Choose **Next**. The **Review** page opens.

1. Choose **Store**.

Use these secrets when you create your migration project in [Step 7](dm-postgresql-step-7.md).
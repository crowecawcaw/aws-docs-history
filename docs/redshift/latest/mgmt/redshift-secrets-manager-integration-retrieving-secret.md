Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Retrieving the

Amazon Resource Name (ARN) of the secret in Amazon Redshift

You can view the Amazon Resource Name (ARN) for any secrets being managed by AWS Secrets Manager
using the Amazon Redshift console. Once you have the secret’s ARN, you can view details about
your secret and the encrypted data in your secret using AWS Secrets Manager. For more information
on retrieving secrets using the ARN, see [Retrieve
secrets](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md") in the _AWS Secrets Manager User Guide_.

**Viewing the details about a secret for an Amazon Redshift provisioned cluster**

View the Amazon Resource Name (ARN) for your cluster's secret using the
Amazon Redshift console with the following procedure:

1. Sign in to the AWS Management Console and open the Amazon Redshift console.
2. In the **Cluster overview** pane,
   choose the cluster whose secret you want to view.
3. Choose the **Properties** tab.
4. View the secret's ARN under **Admin
   credentials ARN**. This ARN is the identifier for the
   secret, which you can use in AWS Secrets Manager to view the secret's details.

**Viewing the details about a secret for an Amazon Redshift Serverless namespace**

View the Amazon Resource Name (ARN) for your serverless namespace's secret
using the Amazon Redshift console with the following procedure:

1. Sign in to the AWS Management Console and open the Amazon Redshift console.
2. From the **Provisioned clusters**
   dashboard, choose **Go to Serverless**
   in the upper right of the page.
3. From the **Serverless dashboard**,
   scroll to the **Namespaces /
   Workgroups** pane and choose the namespace whose secret
   you want to view.
4. In the **General information** pane,
   view the secret's ARN under **Admin credentials
   ARN**. This ARN is the identifier for the secret, which
   you can use in AWS Secrets Manager to view the secret's details.

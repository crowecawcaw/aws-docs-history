

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Retrieving the Amazon Resource Name (ARN) of the secret in Amazon Redshift
<a name="redshift-secrets-manager-integration-retrieving-secret"></a>

You can view the Amazon Resource Name (ARN) for any secrets being managed by AWS Secrets Manager using the Amazon Redshift console. Once you have the secret’s ARN, you can view details about your secret and the encrypted data in your secret using AWS Secrets Manager. For more information on retrieving secrets using the ARN, see [Retrieve secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the *AWS Secrets Manager User Guide*. 

**Viewing the details about a secret for an Amazon Redshift provisioned cluster**  
View the Amazon Resource Name (ARN) for your cluster's secret using the Amazon Redshift console with the following procedure:  

1. Sign in to the AWS Management Console and open the Amazon Redshift console. 

1. In the **Cluster overview** pane, choose the cluster whose secret you want to view. 

1. Choose the **Properties** tab.

1. View the secret's ARN under **Admin credentials ARN**. This ARN is the identifier for the secret, which you can use in AWS Secrets Manager to view the secret's details. 

**Viewing the details about a secret for an Amazon Redshift Serverless namespace**  
View the Amazon Resource Name (ARN) for your serverless namespace's secret using the Amazon Redshift console with the following procedure:  

1. Sign in to the AWS Management Console and open the Amazon Redshift console. 

1. From the **Provisioned clusters** dashboard, choose **Go to Serverless** in the upper right of the page.

1. From the **Serverless dashboard**, scroll to the **Namespaces / Workgroups** pane and choose the namespace whose secret you want to view.

1. In the **General information** pane, view the secret's ARN under **Admin credentials ARN**. This ARN is the identifier for the secret, which you can use in AWS Secrets Manager to view the secret's details. 
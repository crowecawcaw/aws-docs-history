

# Configuring Amazon Redshift
<a name="Redshift-config"></a>

 After adding your Amazon Redshift data source to your workspace, configure Amazon Redshift settings as the following:

## Prerequisites
<a name="Redshift-prerequisites"></a>
+  You have access to **Amazon Redshift** from your account.

## **Connection details** settings
<a name="Redshift-connection-details"></a>

**Configure Connection details settings**

1.  In the **Connection Details** menu, select the authentication provider (recommended: **Workspace IAM Role**). 

1.  Choose the **Default Region** you want to query. 

## **Authentication** settings
<a name="Redshift-Authentication"></a>

**Configure **Authentication** settings**

1.  In the **Authentication** menu, choose either the **Temporary Credentials** or **AWS Secrets Manager** tab as your access credentials provider. For details on Temporary Credentials and AWS Secrets Manager, refer to [AWS managed policy: AmazonGrafanaRedshiftAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonGrafanaRedshiftAccess)

1.  If you choose **Temporary credentials** which is by default, follow the steps below. If you choose **AWS Secrets Manager**, enter your **AWS Secrets Manager** credentials in the input fields. 

1.  Choose the **Cluster Identifier** of the cluster you created in Amazon Redshift.

   For more information about the Redshift cluster, see [ Redshift connections](https://docs.aws.amazon.com/redshift/latest/gsg/connection.html).

1.  Choose your targeted Redshift database.

1.  Select the database user you created for the above cluster. 

1.  Choose **Save & Test**. 

The following is an example of the ** Temporary Credentials** settings.

![Temporary Credentials example](http://docs.aws.amazon.com/grafana/latest/userguide/images/redshift.png)


The following is an example of the **AWS Secrets Manager** menu.

![Secrets Manager example](http://docs.aws.amazon.com/grafana/latest/userguide/images/secretsmanager.png)

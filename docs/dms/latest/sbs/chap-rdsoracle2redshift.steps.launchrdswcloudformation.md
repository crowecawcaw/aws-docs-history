# Step 1: Launch the RDS Instances in a VPC by Using the AWS CloudFormation Template

Before you begin, you’ll need to download an AWS CloudFormation template. Follow these instructions:

1. Download the following archive to your computer: `http://docs.aws.amazon.com/dms/latest/sbs/samples/dms-sbs-RDSOracle2Redshift.zip`
2. Extract the AWS CloudFormation template (`Oracle_Redshift_For_DMSDemo.template`) from the archive.
3. Copy and paste the `Oracle_Redshift_For_DMSDemo.template` file into your current directory.
   Now you need to provision the necessary AWS resources for this walkthrough.

4. Sign in to the AWS Management Console and open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
5. Choose **Create stack**.
6. On the **Select Template** page, choose **Upload a template to Amazon S3**.
7. Click **Choose File**, and then choose the `Oracle_Redshift_For_DMSDemo.template` file that you extracted from the `dms-sbs-RDSOracle2Redshift.zip` archive.
8. Choose **Next**. On the **Specify Details** page, provide parameter values as shown following.

| Parameter              | Action                                                                                                                                                                                                                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Stack Name**         | Enter `OracletoRedshiftDWusingDMS`.                                                                                                                                                                                                                                                                                                   |
| **OracleDBName**       | Provide a unique name for your database. The name should begin with a letter. The default is `ORCL`.                                                                                                                                                                                                                                  |
| **OracleDBUsername**   | Specify the admin (DBA) user for managing the Oracle instance. The default is `oraadmin`.                                                                                                                                                                                                                                             |
| **OracleDBPassword**   | Provide the password for the admin user. The default is `oraadmin123`                                                                                                                                                                                                                                                                 |
| **RedshiftDBName**     | Provide any unique name for your database. The name should begin with a letter. The default is `test`.                                                                                                                                                                                                                                |
| **RedshiftDBUsername** | Provide the password for the master user. The default is `Redshift#123`.                                                                                                                                                                                                                                                              |
| **ClientIP**           | Specify the IP address in CIDR (x.x.x.x/32) format for your local computer. You can get your IP address from whatsmyip.org. Your RDS instances' security group will allow ingress to this IP address. The default is access from anywhere (0.0.0.0/0), which is not recommended; you should use your IP address for this walkthrough. |

![Specify Details page](images/sbs-rdsor2redshift3.png) 6. Choose **Next**. On the **Options** page, choose **Next**. 7. On the **Review** page, review the details, and if they are correct choose **Create**.

![replication instance](images/sbs-rdsor2redshift5.png) 8. AWS can take about 20 minutes or more to create the stack with an Amazon RDS for Oracle instance and an Amazon Redshift cluster.

![Create Stack page](images/sbs-rdsor2redshift6.png) 9. After the stack is created, select the **OracletoRedshiftDWusingDMS** stack, and then choose the **Outputs** view. Record the JDBC connection strings, **OracleJDBCConnectionString** and **RedshiftJDBCConnectionString**, for use later in this walkthrough to connect to the Oracle and Amazon Redshift databases.

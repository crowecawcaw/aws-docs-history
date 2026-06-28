# Using Identity based federation with Parquet tables

## Overview

This tutorial demonstrates how to use TIP identity with EMR on EC2 cluster to propagate user identities from IAM Identity Center (IDC) to AWS Lake Formation for data access authorization
based on TIP identity. The IDC user will use EMR-Studio to run analysis on the Parquet table. We will see permission management using Named Data Catalog Resource as well
with Tag based permission. In this tutorial we grant access to the table to IDC user **aws-dataengineer** using Named Catalog method and IDC user **aws-datanalyst** using LF-Tag
based method.

In this tutorial, we grant access to the table using two methods:

- Named Catalog method for IDC user **aws-dataengineer**
- LF-Tag based method for IDC user **aws-datanalyst**

### Prerequisites

Follow the Prerequisites section to create:

- A trusted-identity enabled EMR Security configuration
- EMR studio
- Lake Formation with IAM Identity Center and trusted identity propagation

### Create an EMR Cluster with trusted-identity propagation

Choose either Option A or B to create
your Amazon EMR cluster.

#### Option A: Create EMR Cluster with TIP Security Configuration Using CLI

Create an EMR cluster using the following command. Replace the `corresponding values` based on your
configurations.

###### Note

Refer to Prerequisites section to create the IAM roles and security configurations.

```
aws emr create-cluster \
--name "EMRWithTIP-Parquet" \
--log-uri "`S3 log location`" \
--release-label "emr-7.2.0" \
--service-role "`EMR service role`" \
--security-configuration "`Name of EMR security configuration`" \
--ec2-attributes '{"Instance Profile":"`EC2 Instance profile`","EmrManagedMasterSecurityGroup":"`master security group`","EmrManagedSlaveSecurityGroup":"`core and task security group`","AdditionalMasterSecurityGroups":[],"AdditionalSlaveSecurityGroups":[],"SubnetId":"`Subnet-id`"}' \
--tags 'for-use-with-amazon-emr-managed-policies=true' \
--applications Name=Hadoop Name=JupyterEnterpriseGateway Name=Livy Name=Spark \
--instance-groups '[{"InstanceCount":1,"InstanceGroupType":"MASTER","Name":"cfnMaster","InstanceType":"m5.2xlarge","EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"VolumeType":"gp2","SizeInGB":32},"VolumesPerInstance":4}]}},{"InstanceCount":1,"InstanceGroupType":"CORE","Name":"cfnCore","InstanceType":"m5.2xlarge","EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"VolumeType":"gp2","SizeInGB":32},"VolumesPerInstance":4}]}}]' \
--scale-down-behavior "TERMINATE_AT_TASK_COMPLETION" \
--auto-termination-policy '{"IdleTimeout":3600}' \
--configurations '[{"Classification":"spark-hive-site","Properties":{"hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"}}]' \
--region "`Region`"
```

In your EMR console, you should be able to see the below screenshots after
the cluster is created.

![IAM Identity Center](images/emr-tut-cluster-info-summary.png)

New cluster summary.

#### Option B: Create EMR on EC2 Cluster Using Console

1. Open the EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Select **Clusters** from the left navigation panel under EMR on EC2 and choose **Create cluster**.

![IAM Identity Center](images/emr-tut-parquet-create-cluster.png)

Creating a cluster. 3. Configure the following settings:

    1. Provide the cluster name.
    2. Choose the latest version release.
    3. Select **Custom** for Application bundle.
    4. For AWS Glue Data Catalog settings, choose **Use for Spark table metadata**.



    ![IAM Identity Center](images/emr-tut-parquet-new-cluster.png)

    Cluster configuration.
    5. Keep the defaults for cluster configuration cluster scaling sections.
    6. Under **Networking**, go to the **Virtual private cloud (VPC)** field. Enter the name of your VPC or
     choose **Browse** to select your VPC. Alternatively, choose **Create VPC** to create a VPC that you
     can use for your cluster.
    7. Under the **cluster termination and node replacement** section, choose **Manually terminate cluster** as
     termination option.
    8. Under **Security configuration and key pair** When configuring security settings, select the EMR security configuration you created
     earlier. To enable SSH access to the cluster, you'll need to set up a key pair. Click on **Create key pair**, which will open the EC2 key pair
     page. Provide a name for your new key pair and create it. After creating the key pair, return to the **Create cluster** page and select your newly created
     key pair from the dropdown menu.
    9. For IAM roles, you can either use existing EMR service roles and EC2 instance profiles, or create new ones if none are configured
     for your account.



    ![IAM Identity Center](images/emr-tut-parquet-securtiy-config.png)

    Security configuration.
    10. Finally, review the set up and choose **Create cluster**.

#### Prepare Your Data

###### Note

This step is needed only if you haven't deployed the CloudFormation stack under Prerequisites tutorial.

1. **Copy Data to Your S3 Bucket** – Replace `<your_account_id>` with your account ID. This bucket
   is created by CloudFormation template under Prerequisites section.

```
aws s3 cp s3://aws-blogs-artifacts-public/artifacts/BDB-3528/data/tutorial/cust.parquet s3://tip-blog-s3-lf-`<your_account_id>`/parquet/
```

2. **Create Table in Athena** – Use this command to create the table:

```
CREATE EXTERNAL TABLE `customer_parquet`(
  `data_key` bigint,
  `data_load_date` string,
  `data_location` string,
  `customer_email` string,
  `customer_name` string,
  `comment1` string,
  `comment2` string)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://tip-blog-s3-lf-`your_account_id`/parquet/'
```

This query is kept simple purposely. You might have to add the database name or make small adjustments for it to parse correctly in your environment. 3. Query the sample data using Athena:

![IAM Identity Center](images/emr-tut-parquet-query.png)

Prepare data.

#### AWS Lake Formation permission set up

Follow the AWS Lake Formation setup in the prerequisite section to set up AWS Lake Formation to manage permissions for your AWS Glue Data Catalog objects and Amazon S3 data locations registration that
consists your parquet file. The next step is to Grant permissions to users and groups. Your data lake administrator can grant permissions to IAM Identity Center users and groups on Data Catalog resources
(databases, tables, and views) to allow easy data access.

##### A. Provide Database level permissions to users and groups

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. Select **Data permissions** under **Permissions** in the Lake Formation console.
3. Select **Grant**.
4. On the Grant data lake permissions page, choose, **IAM Identity Center users and groups**.
5. Select **Add** to choose the users and groups to grant permissions. Choose users and groups and click on **Assign**.

![IAM Identity Center](images/emr-tut-assign-users-groups.png)

Assign users. 6. Next, choose **Named Data Catalog resources** to grant permissions to desired Catalog, Database and Table. For this tutorial choose:

    * Your account default catalog under **Catalogs**
    * emr\_tip\_tutorial under **Databases**

7. For Database permissions, select **Create table** and **Describe**. 8. Select **Grant**.

![IAM Identity Center](images/emr-tut-assign-grant.png)

Assign grant.

##### B. Provide table level permission to users and groups

1. Again select **Data permissions** under **Permissions** in the Lake Formation console.
2. Select **Grant**.
3. On the Grant data lake permissions page,
   choose, **IAM Identity Center users and groups**.
4. Select **Add** to choose the users and groups to grant permissions. Choose users and
   groups and click on **Assign**
5. Next, choose **Named Data Catalog resources** to grant permissions and choose:

   - Your account default catalog under **Catalogs**
   - emr\_tip\_tutorial under **Databases**
   - customer\_parquet table under **Tables**

6. For Table permissions, select **Select** and **Describe**.
7. Select **Grant**.

![IAM Identity Center](images/emr-tut-lf-tables.png)

Lake Formation tables.

![IAM Identity Center](images/emr-tut-lf-principals.png)

Lake Formation principals.

![IAM Identity Center](images/emr-tut-lf-table-perms.png)

Table permissions.

##### Grant LakeFormation permission to IDC user (using LF-Tags)

Before we do this, lets add tags to our table created above. We are doing this step manually from the console for demonstration
purpose and you can also use automations or the CLI to do this.

1. Create a LF-Tag names confidentiality with values as private, sensitive & public.

![IAM Identity Center](images/emr-tut-add-lf.png)

Adding an LF tag. 2. Assign the tag for the customer table created earlier.

![IAM Identity Center](images/emr-tut-edit-lf-tags.png)

Edit an LF tag. 3. In LakeFormation **Data permissions** tab, click **Grant** and proceed to grant permissions on the LF-Tag to aws-datanalyst IDC user. We grant the tag value as public to this user. As the table is tagged "sensitive" as shown in previous step, this table should not be accessible to the user.

##### Verify access

1. Login to EMR Studio with the IDC user you granted permissions to in Prerequisites to setup EMR with TIP step.
2. Navigate to **Workspaces** and create a workspace in EMR Studio. Now click on that workspace to open it.
3. Attach the workspace to EMR on EC2 cluster created for Parquet in above step and select PySpark kernel in the notebook.
4. Enter the following query in the notebook to read from the customer table as shown below:

```
spark.sql("select * from `database_name`.customer_parquet").show()
```

![IAM Identity Center](images/enr-tut-spark-job-progress.png)

Job progress.

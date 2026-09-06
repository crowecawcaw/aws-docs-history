

# Using Identity based federation with Delta Lake tables
<a name="emr-trusted-identity-auth-delta-lake"></a>

## Overview
<a name="identity-federation-delta-tables"></a>

This tutorial demonstrates how to use trusted identity with an EMR on EC2 cluster to propagate user identities to AWS Lake Formation for data access authorization for Delta Lake tables. The IDC user will use EMR Studio to run analysis on the table. We will see permission management using Named Data Catalog Resource, but Tag Based permission is supported as well.

### Prerequisites
<a name="identity-federation-delta-prereqs"></a>

Follow the prerequisites section to create and integrated trusted identity enabled EMR Security configuration, integrate EMR studio and Lake Formation with Identity center and trusted identity propagation.

### Setup EMR cluster with trusted identity propagation and Delta enabled.
<a name="identity-federation-delta-setup"></a>

1. **Create an EMR Cluster with Delta Lake and trusted-identity propagation Security configuration** – Create an EMR cluster with the below sample command. Replace the {{corresponding values}} based on your configurations. Refer to the Prerequisites to create the IAM roles and security configurations:

   ```
    aws emr create-cluster \
    --name "EMRWithTIP-DeltaLake" \
    --log-uri "{{S3 log location example s3://aws-logs-xxxxxxx-us-east-1/logs}}" \
    --release-label "emr-7.2.0" \
    --service-role "{{EMR service role example -  arn:aws:iam::12345678934:role/emrtip-EMREC2ServiceRole-MCwLOR8VNJVG}}" \
    --security-configuration "{{Name of EMR security configuration example: IdentityCenterConfiguration-with-lf-tip}}" \
    --ec2-attributes '{"InstanceProfile":"{{EC2 Instance profile name example: AmazonEMR-InstanceProfile-20250217T165212}}","EmrManagedMasterSecurityGroup":"{{security group name}}","EmrManagedSlaveSecurityGroup":"{{security group name}}","AdditionalMasterSecurityGroups":[],"AdditionalSlaveSecurityGroups":[],"SubnetId":"{{Subnet-id}}"}' \
    --tags 'for-use-with-amazon-emr-managed-policies=true' \
    --applications Name=Hadoop Name=JupyterEnterpriseGateway Name=Livy Name=Spark \
    --configurations '[{"Classification":"delta-defaults","Properties":{"delta.enabled":"true"}},{"Classification":"spark-hive-site","Properties":{"hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"}}]' \
    --instance-groups '[{"InstanceCount":1,"InstanceGroupType":"MASTER","Name":"cfnMaster","InstanceType":"m5.2xlarge","EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"VolumeType":"gp2","SizeInGB":32},"VolumesPerInstance":4}]}},{"InstanceCount":1,"InstanceGroupType":"CORE","Name":"cfnCore","InstanceType":"m5.2xlarge","EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"VolumeType":"gp2","SizeInGB":32},"VolumesPerInstance":4}]}}]' \
    --scale-down-behavior "TERMINATE_AT_TASK_COMPLETION" \
    --auto-termination-policy '{"IdleTimeout":3600}' \
    --region "{{Region example: us-east-1}}"
   ```

1. **Sample Delta Lake table (Optional)** – Create a sample Delta table with the below command. Ignore if you already have an existing Delta Lake table.

   Run the below command to copy the sample Delta Lake table into your S3 bucket. (Replace **account\_id**with your account Id. This bucket is created by CloudFormation template, which is described in the Prerequisites.

   ```
   aws s3 sync s3://aws-bigdata-blog/artifacts/delta-lake-crawler/sample_delta_table/ s3://tip-blog-s3-lf-{{account_id}}/delta_table/
   ```

   Run the below command in Amazon Athena to create sample Delta Lake table:

   ```
   CREATE EXTERNAL TABLE emr_tip_tutorial.sample_delta_table
   LOCATION 's3://tip-blog-s3-lf-{{account_id}}/delta_table/'
   TBLPROPERTIES (
   'table_type'='DELTA'
   );
   ```

   Sample data in the table:  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-delta-query.png)

1. Grant LakeFormation permission to IDC user **aws-dataengineer**:  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-delta-named-resource.png)

   Grant permissions:  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-delta-named-resource-perms.png)

   Table permissions:  
![IAM Identity Center](http://docs.aws.amazon.com/emr/latest/ManagementGuide/images/emr-tut-delta-resource-table-perms.png)

### Query Delta Lake from an EMR cluster with trusted-identity propagation and Delta Lake enabled
<a name="identity-federation-delta-query-tables"></a>

1. Login to EMR Studio with the IDC user you granted permissions to in the above steps.

1. Navigate to **Workspaces** and create a workspace in EMR Studio. Now click that workspace to open it.

1. Attach the workspace to EMR on EC2 cluster created for Delta Lake in the above step.

1. Upload the notebook Deltalake.ipynb, to configure the Spark session for Delta Lake and query the table.
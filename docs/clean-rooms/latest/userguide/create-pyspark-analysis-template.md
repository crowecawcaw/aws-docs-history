

# Creating a PySpark analysis template
<a name="create-pyspark-analysis-template"></a>

**Note**  
Parameters are user-provided strings that can contain arbitrary content.  
Review the code to ensure parameters are handled safely to prevent unexpected behavior in your analysis.
Design parameter handling to work safely regardless of what parameter values are provided at submission time.

**PySpark versions**

When you create a PySpark analysis template, you choose the PySpark version for the template. Use PySpark 2.0 for new analysis templates. PySpark 1.0 remains supported, and existing PySpark 1.0 analysis templates continue to work as before.

The following table compares the features that each version supports.


| Feature | PySpark 1.0 | PySpark 2.0 (recommended) | 
| --- | --- | --- | 
| Result output formats | CSV only | CSV or Parquet | 
| CSV formatting | Original CSV formatting | Updated. For example, PySpark 2.0 writes Boolean values as `true` and `false`, includes milliseconds in `TIMESTAMP_NTZ` values, and writes empty strings as `""`.<br />For the full list of changes, see [Differences between PySpark 1.0 and PySpark 2.0 analysis templates](pyspark-template-versions.md). | 
| Permissions for the service role that writes job results | The role must allow the `s3:GetBucketLocation` and `s3:ListBucket` actions on the result bucket. For more information, see [Create a service role to write results of a PySpark job](setting-up-roles.md#create-role-pyspark-job). | Same as PySpark 1.0 | 
| User script and virtual environment | See [Creating a user script](create-user-script.md) and [Creating a virtual environment (optional)](create-virtual-environment.md). | Same as PySpark 1.0 | 

As the member who receives results, you choose the result format for your membership. To receive results in Parquet format, the analysis template must use PySpark 2.0. For how to set the result format, see the API and AWS CLI information later in this topic.

**Prerequisites**

 Before you create a PySpark analysis template, you must have:
+ A membership in an active AWS Clean Rooms collaboration
+ Access to at least one configured table in the active collaboration
+ Permissions to create analysis templates
+ A Python user script and a virtual environment created and stored in S3
  + S3 bucket has versioning enabled. For more information, see [Using versioning in S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
  + S3 bucket can calculate SHA-256 checksums for uploaded artifacts. For more information, see [Using checksums](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html)
+ Permissions to read code from an S3 bucket

  For information about creating the required service role, see [Create a service role to read code from an S3 bucket (PySpark analysis template role)](setting-up-roles.md#create-role-pyspark-analysis-template).

For information about how to create a PySpark analysis template using the AWS SDKs, see the [AWS Clean Rooms API Reference](https://docs.aws.amazon.com/clean-rooms/latest/apireference/Welcome.html).

When you use the API or the AWS CLI, specify the PySpark version in the `format` parameter of the `CreateAnalysisTemplate` operation:
+ `PYSPARK_2_0` – PySpark 2.0 (recommended)
+ `PYSPARK_1_0` – PySpark 1.0

To receive results in Parquet format, set `resultFormat` to `PARQUET` in your membership's job result configuration. This requires an analysis template with the `PYSPARK_2_0` format. If you set the result format to Parquet, jobs that use a `PYSPARK_1_0` analysis template fail validation.

The following procedure describes the process of creating a PySpark analysis template using the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home). It assumes that you have already created a user script and virtual environment files and stored your user script and virtual environment files in an Amazon S3 bucket.

**Note**  
The member who creates the PySpark analysis template must also be the member who receives results.

**To create a PySpark analysis template**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with the AWS account that will function as the collaboration creator.

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration.

1. On the **Templates** tab, go to the **Analysis templates** table.

1. Choose **Create analysis template**.

1. On the **Create analysis template** page, for **Details**, 

   1. Enter a **Name** for the analysis template.

   1. (Optional) Enter a **Description**.

   1. For **Format**, choose the **PySpark** option.

   1. Choose the PySpark version for the analysis template. AWS Clean Rooms recommends PySpark 2.0. For more information, see [Differences between PySpark 1.0 and PySpark 2.0 analysis templates](pyspark-template-versions.md).

1. For **Definition**,

   1. Review the **Prerequisites** and ensure each prerequisite is met before continuing.

   1. For **Entry point file**, enter the S3 bucket or choose **Browse S3**.

   1. (Optional) For **Libraries file**, enter the S3 bucket or choose **Browse S3**.

1. For **Tables referenced in the definition**, 
   + If all tables referenced in the definition have been associated to the collaboration:
     + Leave the **All tables referenced in the definition have been associated to the collaboration** checkbox selected.
     + Under **Tables associated to the collaboration**, choose all associated tables that are referenced in the definition. 
   + If all tables referenced in the definition haven't been associated to the collaboration:
     + Clear the **All tables referenced in the definition have been associated to the collaboration** checkbox.
     + Under **Tables associated to the collaboration**, choose all associated tables that are referenced in the definition.
     + Under **Tables that will be associated later**, enter a table name. 
     + Choose **List another table** to list another table.

1. For **Parameters – optional**, if you want to add parameters to make your analysis template reusable:

   1. Choose **Add parameter**.

   1. Enter a **Parameter name**.

      Parameter names must start with a letter or underscore, followed by alphanumeric characters or underscores.

   1. For **Type**, **STRING** is automatically selected as the only supported type for PySpark analysis templates.

   1. (Optional) Enter a **Default value** for the parameter.

      If you provide a default value, job runners can use this value when running jobs without explicitly providing a parameter value.

   1. To add more parameters, choose **Add another parameter** and repeat the previous steps.
**Note**  
You can define up to 50 parameters per PySpark analysis template. Each parameter value can be up to 1,000 characters.

1. For **Error message configuration**, choose one of the following:
   + **Basic error messages** – returns basic error messages without exposing underlying data. Recommended for production workloads.
   + **Detailed error messages** – returns detailed error messages for faster troubleshooting. Recommended in development and testing environments. May expose sensitive data, including personally identifiable information (PII).
**Note**  
When using **Detailed error messages**, all data provider members must approve this setting for the template.

1. Specify the **Service access** permissions by selecting an **Existing service role name** from the dropdown list. To view the minimum permissions that the role needs, choose **View policy document**.

   1. The list of roles are displayed if you have permissions to list roles.

      If you don't have permissions to list roles, you can enter the Amazon Resource Name (ARN) of the role that you want to use.

   1. View the service role by choosing the **View in IAM** external link.

      If there are no existing service roles, the option to **Use an existing service role** is unavailable.

      By default, AWS Clean Rooms doesn't attempt to update the existing role policy to add necessary permissions. 
**Note**  
AWS Clean Rooms requires permissions to query according to the analysis rules. For more information about permissions for AWS Clean Rooms, see [AWS managed policies for AWS Clean Rooms](security-iam-awsmanpol.md).
If the role doesn’t have sufficient permissions for AWS Clean Rooms, you receive an error message stating that the role doesn't have sufficient permissions for AWS Clean Rooms. The role policy must be added before proceeding.
If you can’t modify the role policy, you receive an error message stating that AWS Clean Rooms couldn't find the policy for the service role.

1. If you want to enable **Tags** for the configured table resource, choose **Add new tag** and then enter the **Key** and **Value** pair.

1. Choose **Create**.

1. You are now ready to inform your collaboration member that they can [Review an analysis template](review-analysis-template.md). (Optional if you want to query your own data.)

**Important**  
Don't modify or remove artifacts (user scripts or virtual environments) after creating an analysis template.  
Doing so will:  
Cause all future analysis jobs using this template to fail.
Require creation of a new analysis template with new artifacts.
Not affect previously completed analysis jobs.
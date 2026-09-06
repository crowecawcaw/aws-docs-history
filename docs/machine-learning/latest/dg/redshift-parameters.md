

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Required Parameters for the Create Datasource Wizard
<a name="redshift-parameters"></a>

 To allow Amazon ML to connect to your Amazon Redshift database and read data on your behalf, you must provide the following: 
+ The Amazon Redshift `ClusterIdentifier`
+ The Amazon Redshift database name
+ The Amazon Redshift database credentials (user name and password)
+ The Amazon ML Amazon Redshift AWS Identity and Access Management (IAM) role
+ The Amazon Redshift SQL query
+ (Optional) The location of the Amazon ML schema
+ The Amazon S3 staging location (where Amazon ML puts the data before it creates the datasource)

Additionally, you need to ensure that the IAM users or roles who create Amazon Redshift datasources (whether through the console or by using the `CreateDatasourceFromRedshift` action) have the `iam:PassRole` permission.

**Amazon Redshift `ClusterIdentifier`**  
 Use this case-sensitive parameter to enable Amazon ML to find and connect to your cluster. You can obtain the cluster identifier (name) from the Amazon Redshift console. For more information about clusters, see [Amazon Redshift Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html). 

**Amazon Redshift Database Name**  
 Use this parameter to tell Amazon ML which database in the Amazon Redshift cluster contains the data that you want to use as your datasource. 

**Amazon Redshift Database Credentials**  
 Use these parameters to specify the username and password of the Amazon Redshift database user in whose context the security query will be executed.   
Amazon ML requires an Amazon Redshift username and password to connect to your Amazon Redshift database. After unloading the data to Amazon S3, Amazon ML never reuses your password, nor does it store it. 

**Amazon ML Amazon Redshift Role**  
 Use this parameter to specify the name of the IAM role that Amazon ML should use to configure the security groups for the Amazon Redshift cluster and the bucket policy for the Amazon S3 staging location.  
If you don't have an IAM role that can access Amazon Redshift, Amazon ML can create a role for you. When Amazon ML creates a role, it creates and attaches a customer managed policy to an IAM role. The policy that Amazon ML creates grants Amazon ML permission to access only the cluster that you specify.  
If you already have an IAM role to access Amazon Redshift, you can type the ARN of the role, or choose the role from the drop down list. IAM roles with Amazon Redshift access are listed at the top of the drop down.  
The IAM role must have the following contents:    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
    {
        "Effect": "Allow",
        "Principal": {
            "Service": "machinelearning.amazonaws.com"
        },
        "Action": "sts:AssumeRole",
        "Condition": {
            "StringEquals": { "aws:SourceAccount": "{{123456789012}}" },
           "ArnLike": { "aws:SourceArn": "arn:aws:machinelearning:us-east-1:{{123456789012}}:datasource/*" }
        }
    }]
}
```
For more information about Customer Managed Policies, see [Customer Managed Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) in the *IAM User Guide*.

**Amazon Redshift SQL Query**  
 Use this parameter to specify the SQL SELECT query that Amazon ML executes on your Amazon Redshift database to select your data. Amazon ML uses the Amazon Redshift [UNLOAD](https://docs.aws.amazon.com/redshift/latest/dg/t_Unloading_tables.html) action to securely copy the results of your query to an Amazon S3 location.   
 Amazon ML works best when input records are in a random order (shuffled). You can easily shuffle the results of your Amazon Redshift SQL query by using the Amazon Redshift **random()** function. For example, let's say that this is the original query:   

```
 "SELECT col1, col2, … FROM training_table" 
```
 You can embed random shuffling by updating the query like this:   

```
 "SELECT col1, col2, … FROM training_table ORDER BY random()" 
```

**Schema Location (Optional) **  
Use this parameter to specify the Amazon S3 path to your schema for the Amazon Redshift data that Amazon ML will export.  
If you don't provide a schema for your datasource, the Amazon ML console automatically creates an Amazon ML schema based on the data schema of the Amazon Redshift SQL query. Amazon ML schemas have fewer data types than Amazon Redshift schemas, so it is not a one-to-one conversion. The Amazon ML console converts Amazon Redshift data types to Amazon ML data types using the following conversion scheme.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/machine-learning/latest/dg/redshift-parameters.html)
To be converted to Amazon ML `Binary` data types, the values of the Amazon Redshift Booleans in your data must be supported Amazon ML Binary values. If your Boolean data type has unsupported values, Amazon ML converts them to the most specific data type it can. For example, if an Amazon Redshift Boolean has the values `0`, `1`, and `2`, Amazon ML converts the Boolean to a `Numeric` data type. For more information about supported binary values, see [Using the AttributeType Field](creating-a-data-schema-for-amazon-ml.md#assigning-data-types).  
If Amazon ML can't figure out a data type, it defaults to `Text`.   
After Amazon ML converts the schema, you can review and correct the assigned Amazon ML data types in the Create Datasource wizard, and revise the schema before Amazon ML creates the datasource. 

**Amazon S3 Staging Location**  
 Use this parameter to specify the name of the Amazon S3 staging location where Amazon ML stores the results of the Amazon Redshift SQL query. After creating the datasource, Amazon ML uses the data in the staging location instead of returning to Amazon Redshift.  
Because Amazon ML assumes the IAM role defined by the Amazon ML Amazon Redshift role, Amazon ML has permissions to access any objects in the specified Amazon S3 staging location. Because of this, we recommend that you store only files that don't contain sensitive information in the Amazon S3 staging location. For example, if your root bucket is `s3://mybucket/`, we suggest that you create a location to store only the files that you want Amazon ML to access, such as `s3://mybucket/AmazonMLInput/`. 
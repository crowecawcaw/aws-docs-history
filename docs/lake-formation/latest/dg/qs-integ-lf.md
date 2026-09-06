

# Using AWS Lake Formation with Quick
<a name="qs-integ-lf"></a>

 Quick supports exploring datasets managed by Lake Formation permissions in Amazon S3 using Athena.

Both Standard and Enterprise edition users of Quick integrate with Lake Formation, but slightly differently.
+ Enterprise edition – Grant fine-grained access control (FGAC) permissions to individual Quick users and groups to access databases and tables. 
+ Standard edition – Grant permissions to IAM roles to access databases and tables.

**Note**  
By default, Quick uses a role named `aws-quicksight-service-role-v0`. You can also define custom roles with required permissions that enable Quick to access Athena.

For more information, see [Authorizing connections through AWS Lake Formation](https://docs.aws.amazon.com/quicksight/latest/user/lake-formation.html) 

## Additional resources
<a name="add-resources-qs"></a>

**Blog posts**
+ [ Enable fine-grained permissions for Quick authors in AWS Lake Formation](https://aws.amazon.com/blogs/big-data/enable-fine-grained-permissions-for-amazon-quicksight-authors-in-aws-lake-formation/)
+  [Securely analyze your data with AWS Lake Formation and Quick](https://aws.amazon.com/blogs/big-data/securely-analyze-your-data-with-aws-lake-formation-and-amazon-quicksight/)
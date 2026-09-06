

# Using Amazon Q Developer with Amazon EMR Studio
<a name="emr-setup"></a>

This page describes how to set up and activate Amazon Q Developer for Amazon EMR Studio. Once activated, Amazon Q can make code recommendations automatically as you write your ETL code.

**Note**  
Amazon Q supports Python, which can be used to code ETL scripts for Spark jobs in Amazon EMR Studio.

Use the following procedure to set up Amazon EMR Studio to work with Amazon Q.

1. Set up [Amazon EMR Studio Notebook](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-create.html).

1. Attach the following policy to the IAM user role for Amazon EMR Studio Notebook.
**Note**  
The `codewhisperer` prefix is a legacy name from a service that merged with Amazon Q Developer. For more information, see [Amazon Q Developer rename - Summary of changes](service-rename.md). 

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "AmazonQDeveloperPermissions",
               "Effect": "Allow",
               "Action": [
                   "codewhisperer:GenerateRecommendations"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Open the [Amazon EMR console](https://console.aws.amazon.com/emr).

1. Under Amazon EMR Studio, choose **Workspaces (Notebooks).**

1. Select your desired Workspace and choose **Quick launch**.
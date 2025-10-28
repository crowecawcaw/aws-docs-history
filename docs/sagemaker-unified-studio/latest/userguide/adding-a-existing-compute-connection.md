# Connecting to an existing Amazon Redshift resource

After you have gained access to an Amazon Redshift resource, you can add a
connection to the compute resource in the Amazon SageMaker Unified Studio console. Complete the following steps to
add a serverless or cluster compute to the project space:

1. Go to the **Compute** section of your project in Amazon SageMaker Unified Studio.
2. Select the **Data warehouse** tab.
3. Choose **Add compute**.
4. Choose **Connect to existing compute resources**, then choose **Next**.
5. Select the type of compute resource you want to add, then choose **Next**.
6. Under **Connection properties**, provide the JDBC URL or the compute you want
   to add. If the compute resource is in the same account as your Amazon SageMaker Unified Studio project, you can
   select the compute resource from a dropdown menu. For more information, see [Gaining access to Amazon Redshift resources](compute-prerequisite-redshift.md "compute-prerequisite-redshift.md").
7. Under **Authentication**, provide the credential type you want to use to access the resource.
   The credential type must be one of the following options: Username and password, IAM
   credentials, AWS Secrets Manager.
8. Provide the credentials according to the authentication method you selected.
9. Under **Name**, input the name of the Amazon Redshift Serverless or
   Amazon Redshift Cluster you want to add.
10. Under **Description**, provide a description of the compute resource.
11. Choose **Add compute**. The Amazon SageMaker Unified Studio project Compute and Data pages then display information for
    that resource.

###### Note

Some credentials provide more information than others on the Compute page. Using a username and password enables Amazon SageMaker Unified Studio to display more information for a resource.

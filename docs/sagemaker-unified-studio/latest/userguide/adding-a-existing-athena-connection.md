# Connecting to an existing Amazon Athena resource

After you have gained access to an Amazon Athena workgroup, you can add a connection to the compute resource in the Amazon SageMaker Unified Studio console. Complete the following steps to add a Amazon Athena workgroup to the project space:

1. Navigate to the **Compute** section of your project in Amazon SageMaker Unified Studio.
2. Select the **SQL analytics** tab.
3. Choose **Add compute**.
4. Choose **Connect to existing compute resources**, then choose **Next**.
5. Select **Amazon Athena workgroup**, then choose **Next**.
6. Under **Connection properties**, provide the Amazon Athena workgroup ARN you want to add. If the compute resource is in the same account as your Amazon SageMaker Unified Studio project, you can select the compute resource from a dropdown menu. For more information, see [Gaining access to Amazon Athena resources](compute-prerequisite-athena.md "compute-prerequisite-athena.md").
7. If you have access role, provide access role credentials. For project role, you don't have to provide any credentials.
8. Under **Name**, enter the name of the Amazon Athena workgroup you want to add.
9. Under **Description**, provide a description of the compute resource.
10. Choose **Add compute**. The Amazon SageMaker Unified Studio project Compute and Data pages then display information for that resource.

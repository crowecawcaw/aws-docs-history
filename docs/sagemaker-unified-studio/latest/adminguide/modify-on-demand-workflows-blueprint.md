# Modify the OnDemandWorkflows

blueprint for creating workflow environments in a shared VPC

In order to support creating workflow environments in a shared VPC setup, where the
VPC is in one AWS account and the project and the Amazon Managed Workflows for Apache
Airflow (Amazon MWAA) environment are in another AWS account, the domain administrator
must complete the following procedure to modify the endpointManagement parameter of the
OnDemand Workflows blueprint.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector
   in the top navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose the domain’s name from the
   list. The name is a hyperlink.
3. On the domain's details page, navigate to the **Project
   profiles** tab.
4. In the **Project profiles** tab, choose a project profile,
   for example, **All capabilities**. The name of the project
   profile is a hyperlink.
5. On the project profile details page, choose **OnDemand
   Workflows** blueprint.
6. In the **OnDemand Workflows** details page, choose
   **Edit**.
7. In the **Blueprint parameters** section, choose
   **endpointManagement** and then choose
   **Edit**.
8. In the **Edit blueprint parameter** pop up window, choose
   **Customer** in the **Value** drop-down.

This value defines whether the VPC endpoints configured for the environment
are created and managed by the customer or by Amazon MWAA. If
**Value** is set to **SERVICE**, Amazon
MWAA creates and manages the required VPC endpoints in your VPC. If
**Value** is set to **CUSTOMER**, you must
create and manage the VPC endpoints for your VPC. If you choose to create an
environment in a shared VPC, you must set this value to
**CUSTOMER**.
The domain users can then [create workflow environments](../userguide/create-workflow-environment.md "../userguide/create-workflow-environment.md") and the domain administrators then can follow
the steps and procedures described [here](https://aws.amazon.com/blogs/big-data/introducing-shared-vpc-support-on-amazon-mwaa/ "https://aws.amazon.com/blogs/big-data/introducing-shared-vpc-support-on-amazon-mwaa/") to automate deployment of Amazon Amazon MWAA environments using
customer-managed endpoints in a VPC.

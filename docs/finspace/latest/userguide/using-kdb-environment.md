

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Managing kdb environments
<a name="using-kdb-environment"></a>

The following sections provide a detailed overview of the operations that you can perform by using a Managed kdb Insights environment.

## Creating a kdb environment
<a name="create-kdb-environment"></a>

**Note**  
You can only create one kdb environment per Region per AWS account.

**To create a kdb environment**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose **Kdb environments**.

1. On the getting started page, choose **Create kdb environment**.

1. On **Create kdb environment** page, enter the environment name and description.

1. Choose a symmetric encryption KMS key to encrypt data in your kdb environment. If a KMS key is not available in the Region where you want to create your FinSpace environment, create a new key.

   For more information, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.

1. (Optional) Add a new tag to assign it to your kdb environment. For more information, see [AWS tags](https://docs.aws.amazon.com/finspace/latest/userguide/create-an-amazon-finspace-environment.html#aws-tags). 
**Note**  
You can only add up to 50 tags to your environment.

1. Choose **Create kdb environment**. The environment creation process begins and the environment details page opens. The environment creation process takes few minutes to finish in the background. 

   You can view the status of environment creation under the kdb environment configuration section.

   After the environment is successfully created, you can add network configuration, databases, and clusters to the environment.

## Updating a kdb environment
<a name="update-kdb-environment"></a>

**To update a kdb environment**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose **Kdb environments**.

1. From the kdb environments table, choose the name of the environment.

1. On the environment details page, choose **Edit**.

1. Edit the environment details.
**Note**  
You can only edit the **Name** and **Description** .

1. Choose **Update kdb environment**. You can view the updated details on the environment details page. 

## Viewing kdb environment details
<a name="view-kdb-environment"></a>

**To view and get details of a kdb environment**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose **Kdb environments**. 

1. From the kdb environments table, choose the name of the environment.

   The environment details page opens where you can view details about the environment, add or view network configuration, create new databases, and add clusters.

## Deleting a kdb environment
<a name="delete-kdb-environment"></a>

**Note**  
This action is irreversible. Deleting a kdb environment will delete all resources (users, clusters, and databases) and their metadata in the account. After you initiate a deletion request, the billing for resources in an environment will stop immediately.

**To delete a kdb environment**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose **Kdb environments**.

1. From the kdb environments table, choose the name of the environment.

1. On the environment details page, choose **Delete**.

1. On the confirmation dialog box, enter *confirm*.

1. Choose **Delete**.
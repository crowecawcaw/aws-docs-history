After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Managing kdb environments

The following sections provide a detailed overview of the operations that you can
perform by using a Managed kdb Insights environment.

## Creating a kdb environment

###### Note

You can only create one kdb environment per Region per AWS account.

###### To create a kdb environment

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. On the getting started page, choose **Create kdb
   environment**.
4. On **Create kdb environment** page, enter the environment
   name and description.
5. Choose a symmetric encryption KMS key to encrypt data in your kdb
   environment. If a KMS key is not available in the Region where you want to
   create your FinSpace environment, create a new key.

For more information, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in
the _AWS Key Management Service Developer Guide_. 6. (Optional) Add a new tag to assign it to your kdb environment. For more
information, see [AWS tags](create-an-amazon-finspace-environment.md#aws-tags "create-an-amazon-finspace-environment.md#aws-tags").

###### Note

You can only add up to 50 tags to your environment. 7. Choose **Create kdb environment**. The environment creation
process begins and the environment details page opens. The environment creation
process takes few minutes to finish in the background.

You can view the status of environment creation under the kdb environment
configuration section.

After the environment is successfully created, you can add network
configuration, databases, and clusters to the
environment.

## Updating a kdb environment

###### To update a kdb environment

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose **Edit**.
5. Edit the environment details.

###### Note

You can only edit the **Name** and
**Description**
. 6. Choose **Update kdb environment**. You can view the updated
details on the environment details page.

## Viewing kdb environment details

###### To view and get details of a kdb environment

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.

The environment details page opens where you can view details about the
environment, add or view network configuration, create new databases, and add
clusters.

## Deleting a kdb environment

###### Note

This action is irreversible. Deleting a kdb environment will delete all
resources (users, clusters, and databases) and their metadata in the account.
After you initiate a deletion request, the billing for resources in an environment
will stop immediately.

###### To delete a kdb environment

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose **Delete**.
5. On the confirmation dialog box, enter _confirm_.
6. Choose **Delete**.



After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Managing kdb users
<a name="finspace-managed-kdb-users"></a>

The following sections provide a detailed overview of the operations that you can perform by using Managed kdb Insights users. A kdb user is required in order to establish a connection to a Managed kdb cluster. For more information, see [Interacting with a kdb cluster](interacting-with-kdb-clusters.md).

## Creating a kdb user
<a name="create-kdb-user"></a>

**To create a user**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose **Kdb environments**.

1. From the kdb environments table, choose the name of the environment.

1. On the environment details page, choose the **Users** tab.

1. Choose **Add user**.

1. On the **Add user** page, a unique name for the user.

1. Choose an IAM role available in your account to associate it with the user. This role will be used later when you connect to a cluster.
**Note**  
The IAM role that you choose must have connect cluster permissions.

1. (Optional) Add a new tag to assign it to your kdb user. For more information, see [AWS tags](https://docs.aws.amazon.com/finspace/latest/userguide/create-an-amazon-finspace-environment.html#aws-tags). 
**Note**  
You can only add up to 50 tags to your user.

1. Choose **Add user**. The environment details page opens and the table under **Users** lists the newly added user.

## Updating a kdb user
<a name="update-kdb-user"></a>

**Note**  
You can only modify the IAM role associated with a user.

**To update a kdb user**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose **Kdb environments**.

1. From the kdb environments table, choose the name of the environment.

1. On the environment details page, choose the **Users** tab.

1. From the list of users, choose the one that you want to update.

1. Choose **Edit**.

1. Choose a new IAM role to associate with this user.

1. Choose **Update user**.

## Deleting a kdb user
<a name="delete-kdb-user"></a>

**Note**  
This action is irreversible.

**To delete a kdb user**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. Choose **Kdb environments**.

1. From the kdb environments table, choose the name of the environment.

1. On the environment details page, choose the **Users** tab.

1. From the list of users, choose the one that you want to delete.

1. Choose **Delete**.

1. On the confirmation dialog box, enter *confirm*.

1. Choose **Delete**.


**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Delete an AWS Mainframe Modernization runtime environment
<a name="delete-environments-m2"></a>

Use the AWS Mainframe Modernization console to delete an AWS Mainframe Modernization runtime environment.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md).

## Delete a runtime environment
<a name="delete-environments-m2.console"></a>

If you need to delete an AWS Mainframe Modernization runtime environment, make sure that you delete any deployed applications from the environment first. You can't delete a runtime environment where applications are deployed.

**To delete an environment**

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/).

1. In the AWS Region selector, choose the Region where the environment that you want to delete was created.

1. On the **Environments** page, choose the environment that you want to delete, and then choose **Actions** and **Delete environment**.

1. In the **Delete environment** window, enter `delete` to confirm that you want to delete the runtime environment, and then choose **Delete**.
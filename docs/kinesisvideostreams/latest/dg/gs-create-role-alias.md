

# Create the AWS IoT role alias
<a name="gs-create-role-alias"></a>

Follow these procedures to create an AWS IoT role alias for the IAM role that you created in [Create an IAM role](gs-create-role.md). A role alias is an alternate data model that points to the IAM role. An AWS IoT credentials provider request must include a role alias to indicate which IAM role to assume in order to obtain temporary credentials from the AWS Security Token Service (AWS STS). For more information, see [How to use a certificate to get a security token](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html#authorizing-direct-aws.walkthrough).

**Create the AWS IoT role alias**

1. Sign in to the AWS Management Console and open the AWS IoT Core console at [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/).

1. Verify that the appropriate Region is selected.

1. On the left navigation, select **Security** and then choose **Role Aliases**.

1. Choose **Create role alias**.

1. Enter a name for your role alias.  
**Example**  

   **Example:** `KvsEdgeAgentRoleAlias`

1. In the **Role** dropdown, select the IAM role you created in [Create an IAM role](gs-create-role.md).

1. Choose **Create**. On the next page, you see a note that your role alias was successfully created.

1. Search for and select the newly created role alias. Make note of the **Role alias ARN**. You need this for the AWS IoT policy in the next step.
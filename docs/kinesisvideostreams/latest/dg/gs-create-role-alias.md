# Create the AWS IoT role alias

Follow these procedures to create an AWS IoT role alias for the IAM role that you
created in [Create an IAM role](gs-create-role.md "gs-create-role.md"). A role alias is an alternate data model
that points to the IAM role. An AWS IoT credentials provider request must include a
role alias to indicate which IAM role to assume in order to obtain temporary
credentials from the AWS Security Token Service (AWS STS). For more information, see [How to use a certificate to get a security token](../../../iot/latest/developerguide/authorizing-direct-aws.md#authorizing-direct-aws.walkthrough "../../../iot/latest/developerguide/authorizing-direct-aws.md#authorizing-direct-aws.walkthrough").

###### Create the AWS IoT role alias

1. Sign in to the AWS Management Console and open the AWS IoT Core console at
   [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. Verify that the appropriate Region is selected.
3. On the left navigation, select **Security** and then
   choose **Role Aliases**.
4. Choose **Create role alias**.
5. Enter a name for your role alias.

###### Example

**Example:**
`KvsEdgeAgentRoleAlias` 6. In the **Role** dropdown, select the IAM role you
created in [Create an IAM role](gs-create-role.md "gs-create-role.md"). 7. Choose **Create**. On the next page, you see a note that
your role alias was successfully created. 8. Search for and select the newly created role alias. Make note of the
**Role alias ARN**. You need this for the AWS IoT policy
in the next step.

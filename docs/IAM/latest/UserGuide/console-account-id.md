# Viewing your AWS account ID

If you are signed into the console, you can view the account ID for your AWS account
using the following methods.

## To view your AWS account ID

Console
The AWS account ID is displayed when you go to the IAM
**Dashboard** in the AWS account section. You can
also view your account ID in the navigation bar at the upper right. Choose
your user name, and the account ID is displayed above your user name.

![Account information drop-down box with account ID highlighted](images/find-account-id.png)

AWS CLI
Use the following command to view your user ID, account ID, and your user
ARN:

- [aws sts
  get-caller-identity](../../../cli/latest/reference/sts/get-caller-identity.md "../../../cli/latest/reference/sts/get-caller-identity.md")

API
Use the following API to view your user ID, account ID, and your user
ARN:

- [GetCallerIdentity](../../../STS/latest/APIReference/API_GetCallerIdentity.md "../../../STS/latest/APIReference/API_GetCallerIdentity.md")

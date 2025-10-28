# View application details with CodeDeploy

You can use the CodeDeploy console, the AWS CLI, or the CodeDeploy APIs to view details about all
applications associated with your AWS account.

###### Topics

- [View application details
  (console)](#applications-view-details-console "#applications-view-details-console")
- [View application details (CLI)](#applications-view-details-cli "#applications-view-details-cli")

## View application details

(console)

To use the CodeDeploy console to view application details:

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, and choose **Getting started**. 3. To view additional application details, choose the application name in the
list.

## View application details (CLI)

To use the AWS CLI to view application details, call the
**get-application** command, the
**batch-get-application** command, or the
**list-applications** command.

To view details about a single application, call the [get-application](../../../cli/latest/reference/deploy/get-application.md "../../../cli/latest/reference/deploy/get-application.md")
command, specifying the application name.

To view details about multiple applications, call the
[batch-get-applications](../../../cli/latest/reference/deploy/batch-get-applications.md "../../../cli/latest/reference/deploy/batch-get-applications.md") command, specifying multiple application
names.

To view a list of application names, call the [list-applications](../../../cli/latest/reference/deploy/list-applications.md "../../../cli/latest/reference/deploy/list-applications.md")
command.

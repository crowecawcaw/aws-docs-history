# Delete an application in CodeDeploy

You can use the CodeDeploy console, the AWS CLI, or a CodeDeploy API action to delete applications.
For information about using the CodeDeploy API action, see [DeleteApplication](../APIReference/API_DeleteApplication.md "../APIReference/API_DeleteApplication.md").

###### Warning

Deleting an application removes information about the application from the CodeDeploy
system, including all related deployment group information and deployment details.
Deleting an application created for an EC2/On-Premises deployment does not
remove any application revisions from instances nor does it delete revisions from Amazon S3
buckets. Deleting an application created for an EC2/On-Premises deployment
does not terminate any Amazon EC2 instances or deregister any on-premises instances. This
action cannot be undone.

###### Topics

- [Delete an application (console)](#applications-delete-console "#applications-delete-console")
- [Delete an application (AWS CLI)](#applications-delete-cli "#applications-delete-cli")

## Delete an application (console)

To use the CodeDeploy console to delete an application:

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, then choose **Applications**. 3. In the list of applications, choose the the application you want to
delete.

A page appears containing details about the application. 4. Choose **Delete application** on the top-right. 5. When prompted, enter `delete` to confirm you want to
delete the application, and then choose **Delete**.

## Delete an application (AWS CLI)

To use the AWS CLI to delete an application, call the [delete-application](../../../cli/latest/reference/deploy/delete-application.md "../../../cli/latest/reference/deploy/delete-application.md")
command, specifying the application name. To view a list of application names, call the
[list-applications](../../../cli/latest/reference/deploy/list-applications.md "../../../cli/latest/reference/deploy/list-applications.md") command.

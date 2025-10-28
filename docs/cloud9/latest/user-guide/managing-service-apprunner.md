AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Managing App Runner services

After creating an App Runner service, you can manage it by using the AWS Explorer pane to carry
out the following activities:

- [Pausing and resuming App Runner services](#pause-resume-apprunner "#pause-resume-apprunner")
- [Deploying App Runner services](#deploying-apprunner "#deploying-apprunner")
- [Viewing logs streams for App Runner](#viewing-logs-apprunner "#viewing-logs-apprunner")
- [Deleting App Runner services](#deleting-apprunner "#deleting-apprunner")

## Pausing and resuming App Runner services

If you need to disable your web application temporarily and stop the code from running, you
can pause your AWS App Runner service. App Runner reduces the compute capacity for the service
to zero. When you're ready to run your application again, resume your App Runner service. App Runner
provisions new compute capacity, deploys your application to it, and runs the application.

###### Important

You're billed for App Runner only when it's running. Therefore, you can pause and resume your
application as needed to manage costs. This is particularly helpful in development and testing
scenarios.

## To pause your App Runner service

1. Open AWS Explorer, if it isn't already open.
2. Expand **App Runner** to view the list of services.
3. Right-click your service and choose **Pause**.
4. In the dialog box that displays, choose **Confirm**.

While the service is pausing, the service status changes from **Running**
to **Pausing** and then to **Paused**.

## To resume your App Runner service

1. Open AWS Explorer, if it isn't already open.
2. Expand **App Runner** to view the list of services.
3. Right-click your service and choose **Resume**.

While the service is resuming, the service status changes from
**Resuming** to **Running**.

## Deploying App Runner services

If you choose the manual deployment option for your service, you need to explicitly initiate
each deployment to your service.

1. Open AWS Explorer, if it isn't already open.
2. Expand **App Runner** to view the list of services.
3. Right-click your service and choose **Start Deployment**.
4. While your application is being deployed, the service status changes from
   **Deploying** to **Running**.
5. To confirm that your application is successfully deployed, right-click the same service
   and choose **Copy Service URL**.
6. To access your deployed web application, paste the copied URL into the address bar of your
   web browser.

## Viewing logs streams for App Runner

Use CloudWatch Logs to monitor, store, and access your log streams for services such as App Runner. A log
stream is a sequence of log events that share the same source.

1. Expand **App Runner** to view the list of service instances.
2. Expand a specific service instance to view the list of log groups. (A log group is a group
   of log streams that share the same retention, monitoring, and access control settings.)
3. Right-click a log group and choose **View Log Streams**.
4. From the command pane, choose a log stream from the group.

The AWS Cloud9 IDE displays the list of log events that make up the stream. You can choose to
load older or newer events into the editor.

## Deleting App Runner services

###### Important

If you delete your App Runner service, it's permanently removed and your stored data is deleted.
If you need to recreate the service, App Runner needs to fetch your source again and build it if it's
a code repository. Your web application gets a new App Runner domain.

1. Open AWS Explorer, if it isn't already open.
2. Expand **App Runner** to view the list of services.
3. Right-click a service and choose **Delete Service**.
4. In the AWS Toolkit command pane, enter _delete_ and then press
   **Enter** to confirm.

The deleted service displays the **Deleting** status, and then the
service disappears from the list.

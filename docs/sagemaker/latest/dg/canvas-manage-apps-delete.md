# Delete an application

If you want to terminate your SageMaker Canvas workspace instance, you can either log out from the
SageMaker Canvas application or delete your application from the SageMaker AI console. A _workspace instance_ is dedicated for your use from when you start
using SageMaker Canvas to the point when you stop using it. Deleting the application only terminates
the workspace instance and stops workspace instance charges. Models and datasets aren’t
affected, but Quick build tasks automatically restart when you relaunch the
application.

To delete your Canvas application through the AWS console, first close the browser
tab in which your Canvas application was open. Then, use the following procedure to
delete your SageMaker Canvas application.

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin
   configurations**.
3. Under **Admin configurations**, choose
   **Domains**.
4. On the **Domains** page, choose your domain.
5. On the **Domain details** page, choose **Resources**.
6. Under **Applications**, find the application that says
   **Canvas** in the **App type** column.
7. Select the checkbox next to the Canvas application and choose **Stop**.
   You have now successfully stopped the application and terminated the workspace instance.

You can also terminate the workspace instance by [logging
out](canvas-log-out.md "canvas-log-out.md") from within the SageMaker Canvas application.



AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner recent updates on September 17, 2021
<a name="release-2021-09-17-recent"></a>

We recently made some important updates to AWS App Runner.

**Release date:** September 17, 2021

## Changes
<a name="release-2021-09-17-recent.changes"></a>

The following list summarizes key updates we've made to AWS App Runner since it was launched in May.
+ *Date/time filter for log search* – You can now add a date/time range filter to your application log searches in the App Runner console. Application logs can build up as your service application is running. A date/time range can help you focus on the period of time you're investigating.
+ *IDE integration* – You can now develop your application code and deploy it to App Runner right from within your [JetBrains](https://aws.amazon.com/about-aws/whats-new/2021/05/introducing-aws-app-runner-integration-in-the-aws-toolkit-for-jetbrains-ides/) or [Visual Studio Code](https://aws.amazon.com/about-aws/whats-new/2021/08/aws-app-runner-aws-toolkit-vs-code/) IDE.
+ *App2Container integration* – [AWS App2Container](https://aws.amazon.com/app2container/) now supports [deployment of containerized applications to App Runner](https://aws.amazon.com/about-aws/whats-new/2021/05/aws-app2container-supports-deployment-of-containerized-applications-to-aws-app-runner/).
+ *Long-running actions* – We fixed many stability issues that resulted in errors during long-running actions (for example, `CreateService` and `UpdateService`).
+ *Improved logging* – When actions take a long time to complete, we added more service logging and improved existing service log events. You now have more information about the progress, success, or failure of your service actions. You can more easily identify which step failed and take appropriate action to fix the issue.
+ *Custom path for IAM role* – You can now add the App Runner trust policies in AWS Identity and Access Management (IAM) roles defined in custom paths, and use such roles as App Runner service roles. This enables you to follow security best practices of your organization.
+ *Environment variable updates* – You can now update environment variables for existing services. Previously, to update environment variables or their values, you had to terminate and recreate your service.
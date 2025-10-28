# Diagnose issues and get support

The following sections describe how to diagnose issues with RStudio on Amazon SageMaker AI. To get
support for RStudio on Amazon SageMaker AI, contact Amazon SageMaker AI support. For help with purchasing an RStudio
license or modifying the number of license seats, contact [sales@rstudio.com](mailto:sales@rstudio.com "mailto:sales@rstudio.com").

## Upgrade your version

If you receive a warning that there is a version mismatch between your RSession and
RStudioServerPro apps, then you must upgrade the version of your RStudioServerPro app. For
more information, see [RStudio Versioning](rstudio-version.md "rstudio-version.md").

## View Metrics and Logs

You can monitor your workflow performance while using RStudio on Amazon SageMaker AI. View data logs
and information about metrics with the RStudio administrative dashboard or Amazon CloudWatch.

### View your RStudio logs from the RStudio

administrative dashboard

You can view metrics and logs directly from the RStudio administrative dashboard.

1. Log in to your **Amazon SageMaker AI domain**.
2. Navigate to the RStudio administrative dashboard following the steps in [Use the RStudio administrative dashboard](rstudio-admin.md "rstudio-admin.md").
3. Select the **Logs** tab.

### View your RStudio logs from

Amazon CloudWatch Logs

Amazon CloudWatch monitors your AWS resources and the applications that you run on AWS in real
time. You can use Amazon CloudWatch to collect and track metrics, which are variables that you can
measure for your resources and applications. To ensure that your RStudio apps have
permissions for Amazon CloudWatch, you must include the permissions described in [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md"). You don’t need to do any
setup to gather Amazon CloudWatch Logs.

The following steps show how to view Amazon CloudWatch Logs for your RSession.

These logs can be found in the `/aws/sagemaker/studio` log stream from the
AWS CloudWatch console.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Select `Logs` from the left side. From the dropdown menu, select `Log
groups`.
3. On the `Log groups` screen, search for `aws/sagemaker/studio`. Select the Log group.
4. On the `aws/sagemaker/studio` `Log group` screen, navigate to the `Log streams` tab.
5. To find the logs for your domain, search `Log streams` using the following
   format:

```
`<DomainId>`/domain-shared/rstudioserverpro/default
```

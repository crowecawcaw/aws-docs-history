# Logging out of Amazon SageMaker Canvas

After completing your work in Amazon SageMaker Canvas, you can log out or configure your application
to automatically terminate the _workspace instance_.
A workspace instance is dedicated for your use every time you launch a Canvas application,
and you are billed for as long as the instance runs. Logging out or terminating the workspace instance
stops the workspace instance billing. For more information, see [SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

The following sections describe how to log out of your Canvas application and how to
configure your application to automatically shut down on a schedule.

## Log out of Canvas

When you log out of Canvas, your models and datasets aren't affected. Any quick or
standard model builds or [large data processing
jobs](canvas-export-data.md#canvas-export-data-s3 "canvas-export-data.md#canvas-export-data-s3") continue running even if you log out.

To log out, choose the **Log out** button (
![Filter icon in the SageMaker Canvas app.](images/studio/canvas/logout-icon.png)
) on the left panel of the SageMaker Canvas application.

You can also log out from the SageMaker Canvas application by closing your browser tab and then [deleting the application](canvas-manage-apps-delete.md "canvas-manage-apps-delete.md") in the console.

After you log out, SageMaker Canvas tells you to relaunch in a different tab. Logging in takes
around 1 minute. If you have an administrator who set up SageMaker Canvas for you,
use the instructions they gave you to log back in. If don't have an administrator, see
the procedure for accessing SageMaker Canvas in [Prerequisites for setting up Amazon SageMaker Canvas](canvas-getting-started.md#canvas-prerequisites "canvas-getting-started.md#canvas-prerequisites").

## Automatically shut down Canvas

If you’re a Canvas administrator, you might want to regularly shut down
applications to reduce costs. You can either create a schedule to shut down active
Canvas applications, or you can create an automation to shut down Canvas
applications as soon as they’re _idle_ (meaning the
user hasn’t been active for 2 hours).

You can create these solutions using AWS Lambda functions that call the
`DeleteApp` API and delete Canvas applications given certain
conditions. For more information about these solutions and access to CloudFormation templates
that you can use, see the blog [Optimizing costs for Amazon SageMaker Canvas with automatic shutdown of idle apps](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-for-amazon-sagemaker-canvas-with-automatic-shutdown-of-idle-apps/ "https://aws.amazon.com/blogs/machine-learning/optimizing-costs-for-amazon-sagemaker-canvas-with-automatic-shutdown-of-idle-apps/") .

###### Note

You might experience missing [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")
metrics if there was an error when setting up your idle shut down schedule or a CloudWatch
error. We recommend that you add a CloudWatch alarm that monitors for missing metrics. If
you encounter this issue, reach out to Support for help.

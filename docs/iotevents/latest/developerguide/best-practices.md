End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Best practices for AWS IoT Events

Follow these best practices to get the maximum benefit from AWS IoT Events.

###### Topics

- [Enable Amazon CloudWatch logging when
  developing AWS IoT Events detector models](#best-practices-cw-logs "#best-practices-cw-logs")
- [Publish regularly to save your detector model when working
  in the AWS IoT Events console](#best-practices-console "#best-practices-console")

## Enable Amazon CloudWatch logging when

developing AWS IoT Events detector models

Amazon CloudWatch monitors your AWS resources and the applications that you run on AWS in
real time. With CloudWatch, you gain system-wide visibility into resource use, application
performance, and operational health. When you develop or debug an AWS IoT Events detector model, CloudWatch
helps you know what AWS IoT Events is doing, and any errors that it encounters.

###### To enable CloudWatch

1. If you haven't already, follow the steps in [Setting up permissions for AWS IoT Events](iotevents-permissions.md "iotevents-permissions.md") to create a role with an attached policy that
   grants permission to create and manage CloudWatch logs for AWS IoT Events.
2. Go to the [AWS IoT Events console](https://console.aws.amazon.com/iotevents/ "https://console.aws.amazon.com/iotevents/").
3. In the navigation pane, choose **Settings**.
4. On the **Settings** page, choose **Edit**.
5. On the **Edit logging options** page, in the **Logging options** section, do the following:
   1. For **Level of verbosity**, select an option.
   2. For **Select role**, select a role with sufficient permissions to
      perform the logging actions that you chose.
   3. (Optional) If you chose **Debug** for the **Level of
      verbosity**, you can add Debug targets by doing the following:
      1. Under **Debug targets**, choose **Add Model Option**.
      2. Enter a **Detector Model Name** and (optional)
         **KeyValue** to specify the detector models and specific detectors
         (instances) to log.

6. Choose **Update**.

Your logging options are successfully updated.

## Publish regularly to save your detector model when working

in the AWS IoT Events console

When you use the AWS IoT Events console, your work in progress is saved locally in your
browser. However,
you must choose **Publish** to save your detector model to AWS IoT Events. After you
publish a detector model, your published work will become available in any browser that you
use to access your account.

###### Note

If you don't publish your work, it will not be saved. After you publish a detector
model, you can't change its name. However, you can continue modifying its definition.

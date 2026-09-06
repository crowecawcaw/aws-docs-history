

# Get recommendations from EC2 instance type finder
<a name="get-ec2-instance-type-recommendations"></a>

EC2 instance type finder considers your use case, workload type, CPU manufacturer preference, and how you prioritize price and performance, as well as additional parameters that you can specify. It then uses this data to provide suggestions and guidance for Amazon EC2 instance types that are best suited to your new workloads.

With so many instance types available, finding the right instance types for your workload can be time-consuming and complex. By using the EC2 instance type finder, you can remain up to date with the latest instance types and achieve the best price-performance for your workloads.

You can get suggestions and guidance for EC2 instance types using the Amazon EC2 console. You can also go directly to Amazon Q to ask for instance type advice. For more information, see the [Amazon Q Developer User Guide](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html).

If you're looking for instance type recommendations for an *existing* workload, use AWS Compute Optimizer. For more information, see [Get EC2 instance recommendations from Compute Optimizer](ec2-instance-recommendations.md).

## Use the EC2 instance type finder
<a name="use-ec2-instance-type-finder"></a>

In the Amazon EC2 console, you can get instance type suggestions from the EC2 instance type finder in the launch instance wizard, when creating a launch template, or on the **Instance types** page.

Use the following instructions to get suggestions and guidance for EC2 instance types using the EC2 instance type finder in the Amazon EC2 console. To view an animation of the steps, see [View an animation: Get instance type suggestions using the EC2 instance type finder](#use-ec2-instance-type-finder-animation).

**To get instance type suggestions using the EC2 instance type finder**

1. Start your process using any of the following:
   + Follow the procedure to [launch an instance](ec2-launch-instance-wizard.md). Next to **Instance type**, choose the **Get advice** link.
   + Follow the procedure to [create a launch template](create-launch-template.md#create-launch-template-define-parameters). Next to **Instance type**, choose the **Get advice** link.
   + In the navigation pane, choose **Instance Types**, and then choose the **Instance type finder** button.

1. In the **Get advice on instance type selection** screen, do the following:

   1. Specify your instance type requirements by selecting options for **Workload type**, **Use case**, **Priority**, and **CPU manufacturers**.

   1. (Optional) To specify more detailed requirements for your workload, do the following:

      1. Expand **Advanced parameters**.

      1. To add a parameter, select a parameter, choose **Add**, and specify a value for the parameter. Repeat for each additional parameter that you want to add. To indicate no minimum or maximum value, leave the field empty.

      1. To remove a parameter after adding it, choose the **X** next to the parameter.

   1. Choose **Get instance type advice**.

      Amazon EC2 provides you with suggestions for instance families matching your specified requirements.

1. To view the details of each instance type within the suggested instance families, choose **View recommended instance family details**.

1. Select an instance type that meets your requirements, and then choose **Actions**, **Launch instance** or **Actions**, **Create launch template**.

   Alternatively, if you started the process in the launch instance wizard or the launch template page, and you prefer to go back to your original flow, make note of the instance type you’d like to use. Then, in the launch instance wizard or launch template, for **Instance type**, choose the instance type, and complete the procedure to launch an instance or create a launch template.

### View an animation: Get instance type suggestions using the EC2 instance type finder
<a name="use-ec2-instance-type-finder-animation"></a>

![Getting instance type suggestions using the instance type finder.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/use-ec2-instance-type-finder-animation.gif)

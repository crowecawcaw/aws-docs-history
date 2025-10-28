# Shut Down Data Wrangler

When you are not using Data Wrangler, it is important to shut down the instance on which it runs to
avoid incurring additional fees.

To avoid losing work, save your data flow before shutting Data Wrangler down. To save your data
flow in Studio Classic, choose **File** and then choose **Save Data Wrangler
Flow**. Data Wrangler automatically saves your data flow every 60 seconds.

###### To shut down the Data Wrangler instance in Studio Classic

1. In Studio Classic, select the **Running Instances and Kernels** icon
   (
   ![Icon of a gear or cog symbol representing settings or configuration options.](images/icons/studio_classic_dw_instances.png)
   ).
2. Under **RUNNING APPS** is the
   **sagemaker-data-wrangler-1.0** app. Select the shutdown icon
   (
   ![Power button icon with a circular shape and vertical line symbol.](images/icons/Shutdown_light.png)
   )
   next to this app .

Data Wrangler runs on an ml.m5.4xlarge instance. This instance disappears from
**RUNNING INSTANCES** when you shut down the Data Wrangler app.

###### Important

If you open Data Wrangler again, an Amazon EC2 instance starts running the application and you will
be charged for the compute. In addition to compute, you are also charged for the storage
that you use. For example, you're charged for any Amazon S3 buckets that you're using with Data Wrangler.

If you find that you're still getting charged for Data Wrangler after shutting down your
applications, there's a Jupyter extension that you can use to automatically shut down
idle sessions. For information about the extension, see [SageMaker-Studio-Autoshutdown-Extension](https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension "https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension").

After you shut down the Data Wrangler app, it has to restart the next time you open a Data Wrangler flow
file. This can take a few minutes.

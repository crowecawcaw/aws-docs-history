# Shut down the Amazon SageMaker Debugger Insights instance

###### Note

On 6/30/27, AWS will discontinue support for Amazon SageMaker Profiler. After 6/30/27, you will no longer be able to access the Profiler console or Profiler resources.
For more information, see [Profiler availability change](profiler-availability-change.md "profiler-availability-change.md").

When you are not using the SageMaker Debugger Insights dashboard, you should shut down the
app instance to avoid incurring additional fees.

**To shut down the SageMaker Debugger Insights app instance in
Studio Classic**

![An animated screenshot that shows how to shut down a SageMaker Debugger Insights dashboard instance.](images/debugger/debugger-studio-insights-shut-down.png)

1. In Studio Classic, select the **Running Instances and
   Kernels** icon (
   ![Running instances icon.](images/icons/Running_squid.png)
   ).
2. Under the **RUNNING APPS** list, look for the
   **sagemaker-debugger-1.0** app. Select the
   shutdown icon (
   ![Shutdown icon.](images/icons/Shutdown_light.png)
   ) next to the app. The SageMaker Debugger Insights dashboards run on an
   `ml.m5.4xlarge` instance. This instance also disappears from the
   **RUNNING INSTANCES** when you shut down the
   **sagemaker-debugger-1.0** app.

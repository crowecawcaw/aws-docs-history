

# Setting the execution timeout for test runs in AWS Device Farm
<a name="how-to-set-default-timeout-for-test-runs"></a>

You can set a value for how long a test run should execute before you stop each device from running a test. The default execution timeout is 150 minutes per device, but you can set a value as low as 5 minutes. You can use the AWS Device Farm console, AWS CLI, or AWS Device Farm API to set the execution timeout. 

**Important**  
The execution timeout option should be set to the *maximum duration* for a test run, along with some buffer. For example, if your tests take 20 minutes per device, you should choose a timeout of 30 minutes per device.

If the execution exceeds your timeout, the execution on that device is forcibly stopped. Partial results are available, if possible. You are billed for execution up to that point, if you're using the metered billing option. For more information about pricing, see [Device Farm Pricing](https://aws.amazon.com/device-farm/pricing/).

You might want to use this feature if you know how long a test run is supposed to take to execute on each device. When you specify an execution timeout for a test run, you can avoid the situation where a test run is stuck for some reason and you are being billed for device minutes when no tests are being executed. In other words, using the execution timeout feature lets you stop that run if it's taking longer than expected.

You can set the execution timeout in two places, at the project level and the test run level. 

## Prerequisites
<a name="how-to-set-default-timeout-prerequisites"></a>

1. Complete the steps in [Setting up](setting-up.md).

1. Create a project in Device Farm. Follow the instructions in [Creating a project in AWS Device Farm](how-to-create-project.md), and then return to this page.

## Set the execution timeout for a project
<a name="how-to-set-execution-timeout-project-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. If you already have a project, choose it from the list. Otherwise, choose **New project**, enter a name for your project, then choose **Submit**.

1. Choose **Project settings**.

1. On the **General** tab, for **Execution timeout**, enter a value or use the slider bar.

1. Choose **Save**.

   All the test runs in your project now use the execution timeout value that you specified, unless you override the timeout value when you schedule a run.

## Set the execution timeout for a test run
<a name="how-to-set-execution-timeout-test-run-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. If you already have a project, choose it from the list. Otherwise, choose **New project**, enter a name for your project, then choose **Submit**.

1. Choose **Create a new run**.

1. Follow the steps to choose an application, configure your test, select your devices, and specify a device state.

1. On **Review and start run**, for **Set execution timeout**, enter a value or use the slider bar.

1. Choose **Confirm and start run**.
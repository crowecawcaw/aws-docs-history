

# Getting started with Device Farm
<a name="getting-started"></a>

This walkthrough shows you how to use Device Farm to test a native Android or iOS app. You use the Device Farm console to create a project, upload an .apk or .ipa file, run a suite of standard tests, and then view the results.

**Note**  
Device Farm is available only in the `us-west-2` (Oregon) AWS Region.

**Topics**
+ [Prerequisites](#getting-started-prepare)
+ [Step 1: Sign in to the console](#getting-started-console)
+ [Step 2: Create a project](#getting-started-create-project)
+ [Step 3: Create and start a run](#getting-started-create-run)
+ [Step 4: View the run's results](#getting-started-view-run-results)
+ [Next steps](#getting-started-next-steps)

## Prerequisites
<a name="getting-started-prepare"></a>

Before you begin, make sure you have completed the following requirements:
+ Complete the steps in [Setting up](setting-up.md). You need an AWS account and an AWS Identity and Access Management (IAM) user with permission to access Device Farm.
+ For Android, you can bring an .apk (Android app package) file, or use the sample application we provide. For iOS, you need an .ipa (iOS app archive) file. You upload the file to Device Farm later in this walkthrough.
**Note**  
Make sure that your .ipa file is built for an iOS device and not for a simulator.
+ (Optional) You need a test from one of the testing frameworks that Device Farm supports. You upload this test package to Device Farm, and then run the test later in this walkthrough. If you don't have a test package available, you can specify and run a standard built-in test suite. For more information, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md).

## Step 1: Sign in to the console
<a name="getting-started-console"></a>

You can use the Device Farm console to create and manage projects and runs for testing. You learn about projects and runs later in this walkthrough.
+ Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

## Step 2: Create a project
<a name="getting-started-create-project"></a>

To test an app in Device Farm, you must first create a project.

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. Under **Mobile Device Testing Projects**, choose **Create project**.

1. Under **Create project**, enter a **Project Name** (for example, **MyDemoProject**).

1. Choose **Create**.

   The console opens the **Automated tests** page of your newly created project.

## Step 3: Create and start a run
<a name="getting-started-create-run"></a>

Now that you have a project, you can create and then start a run. For more information, see [Runs](test-runs.md).

1. On the **Automated tests** tab, choose **Create run**. Alternatively, you can follow the in-console tutorial by selecting **Create run with tutorial**.

1. Under **Select app and run type**, in the **Run type** section, select your run type. Select **Android app** if you do not have an app ready for testing, or if you are testing an android (.apk) app. Select **iOS app** if you are testing an iOS (.ipa) app.

1. Under **Select app**, in the **App selection options** section, choose **Select sample app provided by Device Farm** if you do not have an app available for testing. If you are bringing your own app, select **Upload own app**, and choose your application file. If you're uploading an iOS app, be sure to choose **iOS device**, as opposed to a simulator.

1. Under **Configure test**, in the **Select test framework** section, choose one of the testing frameworks or built-in test suites. For information about each option, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md).
   + If you have not yet packaged your tests for Device Farm, choose **Built-in: Fuzz** to run a standard, built-in test suite. You can keep the default values for **Event count**, **Event throttle**, and **Randomizer seed**. For more information, see [Running Device Farm's built-in fuzz test (Android and iOS)](test-types-built-in-fuzz.md).
   + If you have a test package from one of the supported testing frameworks, choose the corresponding testing framework, and then upload the file that contains your tests.

1. Under **Select devices**, choose **Use Device Pool** and **Top Devices**.

1. (Optional) To add additional configuration, open the **Additional configuration** dropdown. In this section, you can do any of the following:
   + To provide other data for Device Farm to use during the run, next to **Add extra data**, choose **Choose File**, and then browse to and choose the .zip file that contains the data.
   + To install an additional app for Device Farm to use during the run, next to **Install other apps**, choose **Choose File**, and then browse to and choose the .apk or .ipa file that contains the app. Repeat this for other apps you want to install. You can change the installation order by dragging and dropping the apps after you upload them. 
   + To specify whether Wi-Fi, Bluetooth, GPS, or NFC is enabled during the run, next to **Set radio states**, select the appropriate boxes.
   + To preset the device latitude and longitude for the run, next to **Device location**, enter the coordinates.
   + To preset the device locale for the run, in **Device locale**, choose the locale.
   + Select **Enable video recording** to record video during testing.
**Note**  
Setting the device radio state and locale are options only available for Android native tests at this time.
**Note**  
If you have private devices, configuration specific to private devices is also displayed.

1. (Optional) To configure run-level properties, update the **Run Settings** section. Here you can do the following:
   + Assign your run with a custom **Run name**. If no name is provided, the Device Farm console will name your run 'My Device Farm run' by default.
   + Choose **Generate test report** under **Test Insights** to get a detailed structured test report for each job and an aggregated summary at the run level. This insight is generated in addition to any test report that you might generate as part of your test execution.
   + Assign a **Job timeout**, which is the maximum number of minutes a job can run on a device. If your tests are complete before the job timeout, the job completes, and you are not charged for the remainder of the job timeout. The default is 150 minutes.
   + Choose a **Billing method**. By default, if you do not have slots purchased on your account, the Device Farm console selects Metered. If you have slots, the console defaults to Unmetered.

1. At the bottom of the page, choose **Confirm and start run** to schedule the run.

Device Farm starts the run as soon as devices are available, typically within a few minutes. To view the run status, on the **Automated tests** page of your project, choose the name of your run. One the run page, under **Devices**, each device starts with the pending icon ![Device Farm scheduled a job.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-calendar.png) in the device table, then switches to the running icon ![Device Farm progress indicator.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/df-run-progress.png) when the test begins. As each test finishes, the console displays a test result icon next to the device name. When all tests are complete, the pending icon next to the run changes to a test result icon.

## Step 4: View the run's results
<a name="getting-started-view-run-results"></a>

To view test results from the run, on the **Automated tests** page of your project, choose the name of your run. A summary page displays:
+ The total number of tests, by outcome.
+ Lists of tests with unique warnings or failures.
+ A list of devices with test results for each.
+ Any screenshots captured during the run, grouped by device.
+ A section to download the parsing result.

For more information, see [Viewing test reports in Device Farm](how-to-use-reports.md).

## Next steps
<a name="getting-started-next-steps"></a>

For more information about Device Farm, see [Concepts](concepts.md).
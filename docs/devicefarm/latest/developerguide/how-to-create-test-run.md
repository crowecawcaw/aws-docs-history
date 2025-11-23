# Creating a test run in Device Farm

You can use the Device Farm console, AWS CLI, or Device Farm API to create a test run. You can also use a supported plugin,
such as the Jenkins or Gradle plugins for Device Farm. For more information about plugins, see [Tools and plugins](aws-device-farm-tools-plugins.md "aws-device-farm-tools-plugins.md"). For information
about runs, see [Runs](test-runs.md "test-runs.md").

###### Topics

- [Prerequisites](#how-to-create-test-run-prerequisites "#how-to-create-test-run-prerequisites")
- [Create a test run (console)](#how-to-create-test-run-console "#how-to-create-test-run-console")
- [Create a test run (AWS CLI)](#how-to-create-test-run-cli "#how-to-create-test-run-cli")
- [Create a test run (API)](#how-to-create-test-run-api "#how-to-create-test-run-api")
- [Next steps](#how-to-create-test-run-console-next-steps "#how-to-create-test-run-console-next-steps")

## Prerequisites

You must have a project in Device Farm. Follow the instructions in [Creating a project in AWS Device Farm](how-to-create-project.md "how-to-create-project.md"), and then return to this page.

## Create a test run (console)

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. In the navigation pane, choose **Mobile Device Testing**, and then choose
   **Projects**.
3. If you already have a project, you can upload your tests to it. Otherwise, choose **New
   project**, enter a **Project Name**, and then choose
   **Create**.
4. Open your project, and then choose **Create run**.
5. (Optional) Under **Run settings**, in the **Run name** section, enter a name for your run.
   If no name is provided, the Device Farm console will name your run 'My Device Farm run' by default.
6. (Optional) Under **Run settings**, in the **Job timeout** section, you can specify the
   execution timeout for your test run. If you're using unlimited testing slots, confirm that **Unmetered**
   is selected under **Billing method**.
7. Under **Run settings**, in the **Run type** section, select your run type.
   Select **Android app** if you do not have an app ready for testing, or if you are testing an android (.apk) app.
   Select **iOS app** if you are testing an iOS (.ipa) app. Select **Web app** if you want to test
   web applications.
8. Under **Select app**, in the **App selection options** section, choose
   **Select sample app provided by Device Farm** if you do not have an app available for testing.
   If you are bringing your own app, select **Upload own app**, and choose your application file.
   If you're uploading an iOS app, be sure to choose **iOS device**, as opposed to a simulator.
9. Under **Configure test**, choose one of the available test frameworks.

###### Note

If you don't have any tests available, choose **Built-in: Fuzz** to run a
standard, built-in test suite. If you choose **Built-in: Fuzz**, and the
**Event count**, **Event throttle**, and
**Randomizer seed** boxes appear, you can change or keep the values.

For information about the available test suites, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md "test-types.md"). 10. If you didn't choose **Built-in: Fuzz**, select **Choose File** under
**Select test package**. Browse to and choose the file that contains your tests. 11. For your testing environment, choose **Run your test in our standard environment** or
**Run your test in a custom environment**. For more
information, see [Test environments in AWS Device Farm](test-environments.md "test-environments.md"). 12. If you're using a custom test environment, you can optionally do the following:

    * If you want to edit the default test spec in a custom test environment, choose
     **Edit** to update the default YAML specification.
    * If you changed the test spec, choose **Save as New** to update it.
    * You may configure envirnonment variables. Variables supplied here will take precedence over any that may be configured on the parent project.

13. Under **Select devices**, do one of the following:

        * To choose a built-in device pool to run the tests against, for **Device
         pool**, choose **Top Devices**.
        * To create your own device pool to run the tests against, follow the instructions in [Creating a device pool](how-to-create-device-pool.md "how-to-create-device-pool.md"), and
         then return to this page.
        * If you created your own device pool earlier, for **Device pool**, choose
         your device pool.
        * Select **Manually select devices** and choose the desired devices you want
         to run against. This configuration will not be saved.

    For more information, see [Device support in AWS Device Farm](devices.md "devices.md").

14. (Optional) To add additional configuration, open the **Additional configuration** dropdown.
    In this section, you can do any of the following:
    - To provide an execution role ARN, or override one configured on the parent project, use the Exectuion role ARN field.
    - To provide other data for Device Farm to use during the run, next to **Add extra
      data**, choose **Choose File**, and then browse to and choose
      the .zip file that contains the data.
    - To install an additional app for Device Farm to use during the run, next to **Install
      other apps**, choose **Choose File**, and then browse to and
      choose the .apk or .ipa file that contains the app. Repeat this for other apps you want to
      install. You can change the installation order by dragging and dropping the apps after you
      upload them.
    - To specify whether Wi-Fi, Bluetooth, GPS, or NFC is enabled during the run, next to
      **Set radio states**, select the appropriate boxes.
    - To preset the device latitude and longitude for the run, next to **Device
      location**, enter the coordinates.
    - To preset the device locale for the run, in **Device locale**, choose the
      locale.
    - Select **Enable video recording** to record video during testing.
    - Select **Enable app performance data capture** to capture performance data from the device.

###### Note

Setting the device radio state and locale are options only available for Android native tests
at this time.

###### Note

If you have private devices, configuration specific to private devices is also displayed. 15. At the bottom of the page, choose **Create run** to schedule the run.

Device Farm starts the run as soon as devices are available, typically within a few minutes. During your test
run, the Device Farm console displays a pending icon
![Device Farm scheduled a job.](images/df-run-calendar.png)
in the run table. Each device in the run will
also start with the pending icon, then switch to the running icon
![Device Farm progress indicator.](images/df-run-progress.png)
when the test begins. As
each test finishes, a test result icon is displayed next to the device name. When all tests have been
completed, the pending icon next to the run changes to a test result icon.

If you want to stop the test run, see [Stopping a run in AWS Device Farm](how-to-stop-test-runs.md "how-to-stop-test-runs.md").

## Create a test run (AWS CLI)

You can use the AWS CLI to create a test run.

###### Topics

- [Step 1: Choose a project](#how-to-create-test-run-cli-step1 "#how-to-create-test-run-cli-step1")
- [Step 2: Choose a device pool](#how-to-create-test-run-cli-step2 "#how-to-create-test-run-cli-step2")
- [Step 3: Upload your application file](#how-to-create-test-run-cli-step3 "#how-to-create-test-run-cli-step3")
- [Step 4: Upload your test scripts package](#how-to-create-test-run-cli-step4 "#how-to-create-test-run-cli-step4")
- [Step 5: (Optional) Upload your custom test
  spec](#how-to-create-test-run-cli-step5 "#how-to-create-test-run-cli-step5")
- [Step 6: Schedule a test run](#how-to-create-test-run-cli-step6 "#how-to-create-test-run-cli-step6")

### Step 1: Choose a project

You must associate your test run with a Device Farm project.

1. To list your Device Farm projects, run **list-projects**. If you do not have a
   project, see [Creating a project in AWS Device Farm](how-to-create-project.md "how-to-create-project.md").

Example:

```
aws devicefarm list-projects
```

The response includes a list of your Device Farm projects.

```
`{
 "projects": [
 {
 "name": "MyProject",
 "arn": "arn:aws:devicefarm:us-west-2:123456789101:project:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
 "created": 1503612890.057
 }
 ]
}`
```

2. Choose a project to associate with your test run, and make a note of its Amazon Resource Name
   (ARN).

### Step 2: Choose a device pool

You must choose a device pool to associate with your test run.

1. To view your device pools, run **list-device-pools**, specifying your project
   ARN.

Example:

```
aws devicefarm list-device-pools --arn `arn:MyProjectARN`
```

The response includes the built-in Device Farm device pools, such as **Top Devices**,
and any device pools previously created for this project:

```
`{
 "devicePools": [
 {
 "rules": [
 {
 "attribute": "ARN",
 "operator": "IN",
 "value": "[\"arn:aws:devicefarm:us-west-2::device:example1\",\"arn:aws:devicefarm:us-west-2::device:example2\",\"arn:aws:devicefarm:us-west-2::device:example3\"]"
 }
 ],
 "type": "CURATED",
 "name": "Top Devices",
 "arn": "arn:aws:devicefarm:us-west-2::devicepool:example",
 "description": "Top devices"
 },
 {
 "rules": [
 {
 "attribute": "PLATFORM",
 "operator": "EQUALS",
 "value": "\"ANDROID\""
 }
 ],
 "type": "PRIVATE",
 "name": "MyAndroidDevices",
 "arn": "arn:aws:devicefarm:us-west-2:605403973111:devicepool:example2"
 }
 ]
}`
```

2. Choose a device pool, and make a note of its ARN.

You can also create a device pool, and then return to this step. For more information, see
[Create a device pool (AWS CLI)](how-to-create-device-pool.md#how-to-create-device-pool-cli "how-to-create-device-pool.md#how-to-create-device-pool-cli").

### Step 3: Upload your application file

To create your upload request and get an
Amazon Simple Storage Service
(Amazon S3) presigned upload URL, you need:

- Your project ARN.
- The name of your app file.
- The type of the upload.

For more information, see [**create-upload**](../../../cli/latest/reference/devicefarm/create-upload.md "../../../cli/latest/reference/devicefarm/create-upload.md").

1. To upload a file, run **create-upload** with the
   `–-project-arn`, `--name`, and
   `--type` parameters.

This example creates an upload for an Android app:

```
aws devicefarm create-upload -–project-arn arn:MyProjectArn -–name `MyAndroid.apk` -–type ANDROID_APP
```

The response includes your app upload ARN and a presigned URL.

```
`{
 "upload": {
 "status": "INITIALIZED",
 "name": "MyAndroid.apk",
 "created": 1535732625.964,
 "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL",
 "type": "ANDROID_APP",
 "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE"
 }
}`
```

2. Make a note of the app upload ARN and the presigned URL.
3. Upload your app file using the Amazon S3 presigned URL. This example uses **curl**
   to upload an Android .apk file:

```
curl -T MyAndroid.apk "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL"
```

For more information, see [Uploading objects using
presigned URLs](../../../AmazonS3/latest/userguide/PresignedUrlUploadObject.md "../../../AmazonS3/latest/userguide/PresignedUrlUploadObject.md") in the _Amazon Simple Storage Service User Guide_. 4. To check the status of your app upload, run **get-upload** and specify the ARN
of the app upload.

```
aws devicefarm get-upload –-arn arn:MyAppUploadARN
```

Wait until the status in the response is **SUCCEEDED** before you upload your
test scripts package.

```
`{
 "upload": {
 "status": "SUCCEEDED",
 "name": "MyAndroid.apk",
 "created": 1535732625.964,
 "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL",
 "type": "ANDROID_APP",
 "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
 "metadata": "{"valid": true}"
 }
}`
```

### Step 4: Upload your test scripts package

Next, you upload your test scripts package.

1. To create your upload request and get an Amazon S3 presigned upload URL, run
   **create-upload** with the `–-project-arn`,
   `--name`, and `--type` parameters.

This example creates an Appium Java TestNG test package upload:

```
aws devicefarm create-upload –-project-arn `arn:MyProjectARN` -–name `MyTests.zip` –-type APPIUM_JAVA_TESTNG_TEST_PACKAGE
```

The response includes your test package upload ARN and a presigned URL.

```
`{
 "upload": {
 "status": "INITIALIZED",
 "name": "MyTests.zip",
 "created": 1535738627.195,
 "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL",
 "type": "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
 "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE"
 }
}`
```

2. Make a note of the ARN of the test package upload and the presigned URL.
3. Upload your test scripts package file using the Amazon S3 presigned URL. This example uses
   **curl** to upload a zipped Appium TestNG scripts file:

```
curl -T MyTests.zip "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL"
```

4. To check the status of your test scripts package upload, run **get-upload** and
   specify the ARN of the test package upload from step 1.

```
aws devicefarm get-upload –-arn arn:MyTestsUploadARN
```

Wait until the status in the response is **SUCCEEDED** before you continue to
the next, optional step.

```
`{
 "upload": {
 "status": "SUCCEEDED",
 "name": "MyTests.zip",
 "created": 1535738627.195,
 "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL",
 "type": "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
 "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
 "metadata": "{"valid": true}"
 }
}`
```

### Step 5: (Optional) Upload your custom test

spec

If you're running your tests in a standard test environment, skip this
step.

Device Farm maintains a default test spec file for each supported test type. Next, you
download your default test spec and use it to create a custom test spec upload for
running your tests in a custom test environment. For more information, see [Test environments in AWS Device Farm](test-environments.md "test-environments.md").

1. To find the upload ARN for your default test spec, run
   **list-uploads** and specify your project ARN.

```
aws devicefarm list-uploads --arn `arn:MyProjectARN`
```

The response contains an entry for each default test spec:

```
`{
 "uploads": [
 {

 {
 "status": "SUCCEEDED",
 "name": "Default TestSpec for Android Appium Java TestNG",
 "created": 1529498177.474,
 "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL",
 "type": "APPIUM_JAVA_TESTNG_TEST_SPEC",
 "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE"
 }
 }
 ]
}`
```

2. Choose your default test spec from the list. Make a note of its upload
   ARN.
3. To download your default test spec, run **get-upload** and
   specify the upload ARN.

Example:

```
aws devicefarm get-upload –-arn `arn:MyDefaultTestSpecARN`
```

The response contains a presigned URL where you can download your default
test spec. 4. This example uses **curl** to download the default test
spec and save it as `MyTestSpec.yml`:

```
curl "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL" > MyTestSpec.yml
```

5. You can edit the default test spec to meet your testing requirements, and
   then use your modified test spec in future test runs. Skip this step to use
   the default test spec as-is in a custom test environment.
6. To create an upload of your custom test spec, run
   **create-upload**, specifying your test spec name, test
   spec type, and project ARN.

This example creates an upload for an Appium Java TestNG custom test
spec:

```
aws devicefarm create-upload --name MyTestSpec.yml --type APPIUM_JAVA_TESTNG_TEST_SPEC --project-arn `arn:MyProjectARN`
```

The response includes the test spec upload ARN and presigned URL:

```
`{
 "upload": {
 "status": "INITIALIZED",
 "category": "PRIVATE",
 "name": "MyTestSpec.yml",
 "created": 1535751101.221,
 "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL",
 "type": "APPIUM_JAVA_TESTNG_TEST_SPEC",
 "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE"
 }
}`
```

7. Make a note of the ARN for the test spec upload and the presigned
   URL.
8. Upload your test spec file using the Amazon S3 presigned URL. This example uses
   **curl** to upload an Appium JavaTestNG test spec:

```
curl -T MyTestSpec.yml "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL"
```

9. To check the status of your test spec upload, run
   **get-upload** and specify the upload ARN.

```
aws devicefarm get-upload –-arn `arn:MyTestSpecUploadARN`
```

Wait until the status in the response is **SUCCEEDED**
before you schedule your test run.

```
`{
 "upload": {
 "status": "SUCCEEDED",
 "name": "MyTestSpec.yml",
 "created": 1535732625.964,
 "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/ExampleURL",
 "type": "APPIUM_JAVA_TESTNG_TEST_SPEC",
 "arn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE",
 "metadata": "{"valid": true}"
 }
}`
```

To update your custom test spec, run **update-upload**,
specifying the upload ARN for the test spec. For more information, see
[**update-upload**](../../../cli/latest/reference/devicefarm/update-upload.md "../../../cli/latest/reference/devicefarm/update-upload.md").

### Step 6: Schedule a test run

To schedule a test run with the AWS CLI, run **schedule-run**, specifying:

- The project ARN from [step 1](#how-to-create-test-run-cli-step1 "#how-to-create-test-run-cli-step1").
- The device pool ARN from [step
  2](#how-to-create-test-run-cli-step2 "#how-to-create-test-run-cli-step2").
- The app upload ARN from [step 3](#how-to-create-test-run-cli-step3 "#how-to-create-test-run-cli-step3").
- The test package upload ARN from [step
  4](#how-to-create-test-run-cli-step4 "#how-to-create-test-run-cli-step4").

If you are running tests in a custom test environment, you also need your test spec ARN from [step 5](#how-to-create-test-run-cli-step5 "#how-to-create-test-run-cli-step5").

###### To schedule a run in a standard test environment

- Run **schedule-run**, specifying your project ARN, device pool ARN, application
  upload ARN, and test package information.

Example:

```
aws devicefarm schedule-run --project-arn `arn:MyProjectARN` --app-arn `arn:MyAppUploadARN` --device-pool-arn `arn:MyDevicePoolARN` --name `MyTestRun` --test type=APPIUM_JAVA_TESTNG,testPackageArn=`arn:MyTestPackageARN`

```

The response contains a run ARN that you can use to check the status of your test run.

```
`{
 "run": {
 "status": "SCHEDULING",
 "appUpload": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345appEXAMPLE",
 "name": "MyTestRun",
 "radios": {
 "gps": true,
 "wifi": true,
 "nfc": true,
 "bluetooth": true
 },
 "created": 1535756712.946,
 "totalJobs": 179,
 "completedJobs": 0,
 "platform": "ANDROID_APP",
 "result": "PENDING",
 "devicePoolArn": "arn:aws:devicefarm:us-west-2:123456789101:devicepool:5e01a8c7-c861-4c0a-b1d5-12345devicepoolEXAMPLE",
 "jobTimeoutMinutes": 150,
 "billingMethod": "METERED",
 "type": "APPIUM_JAVA_TESTNG",
 "testSpecArn": "arn:aws:devicefarm:us-west-2:123456789101:upload:5e01a8c7-c861-4c0a-b1d5-12345specEXAMPLE",
 "arn": "arn:aws:devicefarm:us-west-2:123456789101:run:5e01a8c7-c861-4c0a-b1d5-12345runEXAMPLE",
 "counters": {
 "skipped": 0,
 "warned": 0,
 "failed": 0,
 "stopped": 0,
 "passed": 0,
 "errored": 0,
 "total": 0
 }
 }
}`
```

For more information, see [**schedule-run**](../../../cli/latest/reference/devicefarm/schedule-run.md "../../../cli/latest/reference/devicefarm/schedule-run.md").

###### To schedule a run in a custom test environment

- The steps are the almost the same as those for the standard test environment, with an
  additional `testSpecArn` attribute in the `--test`
  parameter.

Example:

```
aws devicefarm schedule-run --project-arn `arn:MyProjectARN` --app-arn `arn:MyAppUploadARN` --device-pool-arn `arn:MyDevicePoolARN` --name `MyTestRun` --test testSpecArn=`arn:MyTestSpecUploadARN`,type=`APPIUM_JAVA_TESTNG`,testPackageArn=`arn:MyTestPackageARN`
```

###### To check the status of your test run

- Use the **get-run** command and specify the run ARN:

```
aws devicefarm get-run --arn arn:aws:devicefarm:us-west-2:111122223333:run:5e01a8c7-c861-4c0a-b1d5-12345runEXAMPLE
```

For more information, see [**get-run**](../../../cli/latest/reference/devicefarm/get-run.md "../../../cli/latest/reference/devicefarm/get-run.md"). For information about using Device Farm with the AWS CLI, see [AWS CLI reference](cli-ref.md "cli-ref.md").

## Create a test run (API)

The steps are the same as those described in the AWS CLI section. See [Create a test run (AWS CLI)](#how-to-create-test-run-cli "#how-to-create-test-run-cli").

You need this information to call the [`ScheduleRun`](../APIReference/API_ScheduleRun.md "../APIReference/API_ScheduleRun.md") API:

- A project ARN. See [Create a project (API)](how-to-create-project.md#how-to-create-project-api "how-to-create-project.md#how-to-create-project-api") and [`CreateProject`](../APIReference/API_CreateProject.md "../APIReference/API_CreateProject.md").
- An application upload ARN. See [`CreateUpload`](../APIReference/API_CreateUpload.md "../APIReference/API_CreateUpload.md").
- A test package upload ARN. See [`CreateUpload`](../APIReference/API_CreateUpload.md "../APIReference/API_CreateUpload.md").
- A device pool ARN. See [Creating a device pool](how-to-create-device-pool.md "how-to-create-device-pool.md") and [`CreateDevicePool`](../APIReference/API_CreateDevicePool.md "../APIReference/API_CreateDevicePool.md").

###### Note

If you're running tests in a custom test environment, you also need your test spec upload ARN. For
more information, see [Step 5: (Optional) Upload your custom test
spec](#how-to-create-test-run-cli-step5 "#how-to-create-test-run-cli-step5") and [`CreateUpload`](../APIReference/API_CreateUpload.md "../APIReference/API_CreateUpload.md").

For information about using the Device Farm API, see [Automating Device Farm](api-ref.md "api-ref.md").

## Next steps

In the Device Farm console, the clock icon
![Device Farm scheduled a job.](images/df-run-calendar.png)
changes to a result icon such as
success
![The test succeeded.](images/df-run-success.png)
when the run is complete. A report for the run appears as soon as
tests are complete. For more information, see [Reports in AWS Device Farm](reports.md "reports.md").

To use the report, follow the instructions in [Viewing test reports in Device Farm](how-to-use-reports.md "how-to-use-reports.md").

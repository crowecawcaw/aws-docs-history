# Running Device Farm's built-in fuzz test (Android and iOS)

Device Farm's built-in fuzz test randomly sends user interface events to devices and then reports results.

For more information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md "test-types.md").

###### To run the built-in fuzz test

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose
   **Projects**.
3. In the list of projects, choose the project where you want to run the built-in fuzz test.

###### Tip

You can use the search bar to filter the project list by name.

To create a project, follow the instructions in [Creating a project in AWS Device Farm](how-to-create-project.md "how-to-create-project.md"). 4. Choose **Create run**. 5. Under **Run settings**, select your run type in the **Run type** section.
Select **Android app** if you do not have an app ready for testing, or if you are testing an
android (.apk) app. Select **iOS app** if you are testing an iOS (.ipa) app. 6. Under **Select app**, choose **Select sample app provided by Device Farm**
if you do not have an app available for testing. If you are bringing your own app, select **Upload own app** , and choose your application file. 7. Under **Configure test**, in the **Select test framework** section,
choose **Built-in: Fuzz**. 8. If any of the following settings appear, you can either accept the default values or specify your
own:

    * **Event count**: Specify a number between 1 and 10,000,
     representing the number of user interface events for the fuzz test to perform.
    * **Event throttle**: Specify a number between 0 and 1,000,
     representing the number of milliseconds for the fuzz test to wait before performing the next
     user interface event.
    * **Randomizer seed**: Specify a number for the fuzz test to use
     for randomizing user interface events. Specifying the same number for subsequent fuzz tests
     ensures identical event sequences.

9. Complete the remaining instructions to select devices and
   start the run.

# Getting started with Appium testing

For most Appium users, using Device Farm for Appium testing requires only minor changes to your existing test configuration.

At a high level, there are three steps to using Device Farm for client-side Appium tests:

1. First, you need to [create a remote access session](how-to-create-session.md "how-to-create-session.md")
   for testing a Device Farm device. You can include your apps as a part of your remote access request, or install apps after the session has started.
2. Once the session is running, you can [copy the Appium endpoint URL](appium-endpoint-interaction.md "appium-endpoint-interaction.md"), and use it either through a stand-alone tool (like [Appium Inspector](https://github.com/appium/appium-inspector "https://github.com/appium/appium-inspector")) or from your Appium test code in your IDE. The URL will be valid for the duration of the remote access session.
3. And finally, once your Appium test has started, you can [review your Appium server logs](appium-endpoint-server-logs.md "appium-endpoint-server-logs.md") live during the test execution alongside the video stream of your device.

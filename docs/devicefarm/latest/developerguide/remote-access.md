

# Remote access in AWS Device Farm
<a name="remote-access"></a>

 Remote access, or manual testing, allows you to swipe, gesture, and interact with a device through your web browser in real time to test functionality and reproduce customer issues. You interact with a specific device by creating a remote access session with that device. The following key features are supported on Remote Access:
+ **App(s) upload:** Upload app files (.apk, .ipa) or test on web browsers.
+ **Appium Endpoint:** Connect to an Appium Endpoint right from your remote access session.
+ **Orientation change:** Change between Portrait and Landscape mode.
+ **Network shaping:** Select a pre-configured network profile or create your own.
+ **Location mocking:** Mock a location by providing the latitude and longitude.
+ **Screenshot:** Capture the screenshot of any screen.
+ **Video recording:** Capture the video of your entire test run.
+ **Logs:** Stream live log for Appium and get device, network, and activity logs at the end of your session.

A session in Device Farm is a real-time interaction with an actual, physical device hosted in a web browser. A session displays the single device you select when you start the session. A user can start more than one session at a time with the total number of simultaneous devices limited by the number of device slots you have. You can purchase device slots based on the device family (Android or iOS devices). For more information, see [Device Farm Pricing](https://aws.amazon.com/device-farm/pricing/). 

Device Farm currently offers a subset of devices for remote access testing. New devices are added to the device pool all the time.

Device Farm captures video of each remote access session and generates logs of activity during the session. These results include any information you provide during a session.

**Note**  
For security reasons, we recommend that you avoid providing or entering sensitive information, such as account numbers, personal login information, and other details during a remote access session. If possible, use alternatives developed specifically for testing, such as test accounts.

**Topics**
+ [Creating a remote access session in AWS Device Farm](how-to-create-session.md)
+ [Using a remote access session in AWS Device Farm](how-to-use-session.md)
+ [Retrieving the results of a remote access session in AWS Device Farm](how-to-access-session-results.md)
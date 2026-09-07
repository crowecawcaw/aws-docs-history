

This guide documents the classic version of the AWS Wickr administration console, released before March 13, 2025. For documentation on the new AWS Wickr administration console, see [ Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Install and pair the Wickr plugin for ATAK
<a name="install-and-pair"></a>

The Android Team Awareness Kit (ATAK) is an Android solution used by the US military, state, and governmental agencies that require situational awareness capabilities for mission planning, execution, and incident response. ATAK has a plugin architecture which allows developers to add functionality. It enables users to navigate using GPS and geospatial map data overlaid with real-time situational awareness of ongoing events. In this document, we show you how to install the Wickr plugin for ATAK on an Android device and pair it with the Wickr client. This allows you to message and collaborate on Wickr without exiting the ATAK application.

## Install the Wickr plugin for ATAK
<a name="install"></a>

Complete the following procedure to install the Wickr plugin for ATAK on an Android device.

1. Go to the Google Play store, and install the Wickr for ATAK plugin.

1. Open the ATAK application on your Android device.

1. In the ATAK application, choose the menu icon (![Menu icon](http://docs.aws.amazon.com/wickr/latest/adminguide-classic/images/atak_hamburger_icon.png)) at the top-right of the screen, and then choose **Plugins**.

1. Choose **Import**.

1. On the **Select Import Type** pop-up, choose **Local SD** and navigate to where you saved the Wickr plugin for ATAK .apk file.

1. Choose the plugin file and follow the prompts to install it.
**Note**  
If you are asked to send the plugin file for scanning, choose **No**.

1. The ATAK application will ask if you would like to load the plugin. Choose **OK**.

The Wickr plugin for ATAK is now installed. Continue to the following Pair ATAK with Wickr section to finish the process.

## Pair ATAK with Wickr
<a name="pair"></a>

Complete the following procedure to pair the ATAK application with Wickr after you successfully installed the Wickr plugin for ATAK.

1. In the ATAK application, choose the menu icon (![Menu icon](http://docs.aws.amazon.com/wickr/latest/adminguide-classic/images/atak_hamburger_icon.png)) at the top-right of the screen, and then choose **Wickr Plugin**.

1. Choose **Pair Wickr**.

   A notification prompt will appear asking you to review permissions for the Wickr plugin for ATAK. If the notification prompt doesn't appear, open the Wickr client and go to **Settings**, then **Connected Apps**. You should see the plugin under the **Pending** section of the screen.

1. Choose **Approve** to pair.

1. Choose **Open Wickr ATAK Plugin** button to go back to the ATAK application.

   You have now successfully paired the ATAK plugin and Wickr, and can use the plugin to send messages and collaborate using Wickr without exiting the ATAK application.
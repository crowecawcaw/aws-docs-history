# Update the AWS IoT SiteWise Edge application configuration

There are a few things to consider when updating an AWS IoT SiteWise Edge application configuration
on **Siemens Industrial Edge**.

###### Note

Any change to the AWS IoT SiteWise Edge application configuration requires a restart of the
application.

###### Reasons to restart the AWS IoT SiteWise Edge application

- A new Siemens Databus user for the AWS IoT SiteWise Edge application.
- A change to the gateway configuration file (your
  **SiteWise_Edge_Gateway_Config** file).
- A proxy configuration update (which also requires a full IEVD reboot)
- To enable debug logs for debugging issues

## Restarting the application

1. In your Siemens Industrial Edge Management instance, choose **Edge Management** in the
   **Platform Applications** section.
2. Choose **My Installed Apps**.
3. Select the AWS IoT SiteWise Edge application.
4. Choose **Restart**.

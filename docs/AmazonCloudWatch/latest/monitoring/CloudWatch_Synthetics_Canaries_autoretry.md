# Configuring your canary to retry automatically

When you create or update a canary, you can configure your canaries to automatically attempt additional runs when the scheduled one fails. This helps differentiate between genuine failures and temporary glitches,
 providing more reliable results. This feature is ideal for building more resilient monitoring systems while reducing false alarms and manual intervention.

###### To create a auto retry canary

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, **Synthetics Canaries**.
3. Choose **Create Canary**.
4. Under **Additional configuration**, **Auto-retry,** select the desired maximum retry number.
###### To update the maximum retry number for a canary

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, **Synthetics Canaries**.
3. You can do one of the following:




	* Select the canary and choose **Actions**, **Enable auto-retry**, and adjust the maximum retries.
	* Select the canary and choose **Actions**, **Edit**. In the **Edit detail** page, under **Additional configuration**, **Auto-retry**, adjust the retry configuration.
**Limitations**

Here are the limitations to configure auto retry.


* Supported only on runtime versions `syn-nodejs-puppeteer-10.0` or newer, `syn-nodejs-playwright-2.0` or newer, or 
 `syn-python-selenium-5.1` or newer, or `syn-nodejs-3.0` or newer.
* Long running canaries which timeout after ten minutes are limited to one retry. All other canaries can support upto two retries

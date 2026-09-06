

# Integrating device tokens with Amazon SNS for mobile notifications
<a name="mobile-push-send-devicetoken"></a>

When you first register an app and mobile device with a notification service, such as Apple Push Notification Service (APNs) and Firebase Cloud Messaging (FCM), device tokens or registration IDs are returned by the service. These tokens/IDs are added to Amazon SNS to create an endpoint for the app and device, using the [`PlatformApplicationArn`](https://docs.aws.amazon.com/sns/latest/api/API_PlatformApplication.html) API. Once the endpoint is created, an [`EndpointArn`](https://docs.aws.amazon.com/sns/latest/api/API_Endpoint.html) is returned, which Amazon SNS uses to direct notifications to the correct app/device.

You can add device tokens or registration IDs to Amazon SNS in the following ways:
+ Manually add a single token via the AWS Management Console
+ Upload several tokens using the [`CreatePlatformEndpoint`](https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformEndpoint.html) API
+ Register tokens for future devices

****To manually add a device token or registration ID****

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home).

1. In the navigation pane, select **Push Notifications**.

1. In the **Platform applications** section, select your application, and then choose **Edit**. If you haven't already created a platform application, follow the [Creating an Amazon SNS platform application](mobile-push-send-register.md) guide to do so now.

1. Choose **Create Endpoint**.

1. In the **Endpoint Token** box, enter the **token** or **registration ID**, depending on the notification service you're using (for example, FCM registration ID).

1. (Optional) Enter additional data in the **User Data** field. This data must be UTF-8 encoded and less than 2 KB.

1. Choose **Create Endpoint**.

Once the endpoint is created, you can send messages directly to the mobile device or to mobile devices subscribed to an Amazon SNS topic.

****To upload several tokens using the `CreatePlatformEndpoint` API****

The following steps show how to use the sample Java app (`bulkupload` package) provided by AWS to upload several tokens (device tokens or registration IDs) to Amazon SNS. You can use this sample app to help you get started with uploading your existing tokens. 
**Note**  
The following steps use the Eclipse Java IDE. The steps assume you have installed the AWS SDK for Java and you have the AWS security credentials for your AWS account. For more information, see [AWS SDK for Java](http://aws.amazon.com/sdkforjava/). For more information about credentials, see [AWS security credentials](https://docs.aws.amazon.com/general/latest/gr/getting-aws-sec-creds.html) in the *IAM User Guide*. 

1. Download and unzip the [snsmobilepush.zip](samples/snsmobilepush.zip) file. 

1. Create a new **Java project** in Eclipse and import the `SNSSamples` folder to the project. 

1. Download the [OpenCSV library](http://sourceforge.net/projects/opencsv/) and add it to the build path.

1. In the `BulkUpload.properties` file, specify the following: 
   + Your `ApplicationArn` (platform application ARN).
   + The absolute path to your CSV file containing the tokens.
   + Logging filenames for successful and failed tokens. For example, `goodTokens.csv` and `badTokens.csv`.
   + (Optional) A configuration for delimiter, quote character, and number of threads to use.

   Your completed `BulkUpload.properties` should look similar to the following:

   ```
   applicationarn: arn:aws:sns:us-west-2:111122223333:app/FCM/fcmpushapp
   csvfilename: C:\\mytokendirectory\\mytokens.csv
   goodfilename: C:\\mylogfiles\\goodtokens.csv
   badfilename: C:\\mylogfiles\\badtokens.csv
   delimiterchar: ','
   quotechar: '"'
   numofthreads: 5
   ```

1.  Run the **BatchCreatePlatformEndpointSample.java** application to upload the tokens to Amazon SNS. Tokens uploaded successfully will be logged in `goodTokens.csv`, while malformed tokens will be logged in `badTokens.csv`.

**To register tokens from devices for future app installations**

You have two options for this process:

**Use the Amazon Cognito service**  
Your mobile app can use temporary security credentials to create endpoints. Amazon Cognito is recommended to generate temporary credentials. For more information, see the *[Amazon Cognito Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/)*   
To track app [registrations](application-event-notifications.md), use Amazon SNS events to receive notifications when new endpoint ARNs are created.  
Alternatively, you can use the [`ListEndpointByPlatformApplication`](https://docs.aws.amazon.com/sns/latest/api/API_ListEndpointsByPlatformApplication.html) API to retrieve the list of registered endpoints.

**Use a proxy server**  
If your app infrastructure already supports device registration on installation, you can use your server as a proxy. It will forward device tokens to Amazon SNS via the [`CreatePlatformEndpoint`](https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformEndpoint.html) API.  
The endpoint ARN created by Amazon SNS will be returned and can be stored by your server for future message publishing.
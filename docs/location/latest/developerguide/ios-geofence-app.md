

# Create an iOS application
<a name="ios-geofence-app"></a>

Follow these procedures to build an iOS application using Amazon Location Service.

Clone the project files from [GitHub](https://github.com/aws-geospatial/amazon-location-samples-ios/tree/main/tracking-with-geofence-notifications).

## Create Amazon Location resources for your app
<a name="qs-ios-tracking-resources"></a>

You can generate Amazon Location Service resources once your AWS account is ready. These resources will be essential for executing the provided code snippets.

**Note**  
If you haven't created an AWS account yet, please [create an AWS account](https://portal.aws.amazon.com/billing/signup#/start/email).

To begin you will need to create a Amazon Cognito Identity Pool Id, use the following procedure:

1. In the AWS console, navigate to the Amazon Cognito service and then select **Identity pools** from the left side menu and select **Create Identity pool**. 

1. Make sure **Guest Access** is checked, and press **Next** to continue.

1. Next create a new IAM role or Use an existing IAM role.

1. Enter an Identity pool name, and make sure Identity Pool has access to Amazon Location `(geo)` resources for the map and tracker you will be creating in the next procedure.

1. 

Now you need to create and style a map in the AWS Amazon Location console, use the following procedure:

1. Navigate to the [Maps section](https://console.aws.amazon.com/location/maps/home) in the Amazon Location console and select **Create Map** to preview available map styles.

1. Give the new map resource a **Name** and **Description**. Record the name you assign to the map resource, as it is used later in the tutorial.

1. When choosing a map style, consider the map data provider. Refer to section 82 of the [AWS service terms](http://aws.amazon.com/service-terms) for more details.

1.  Accept the [Amazon Location Terms and Conditions](https://aws.amazon.com/service-terms/#:~:text=82.%20Amazon%20Location%20Service), then select **Create Map**. After map has been created, you can interact with the map by zooming in, out, or panning in any direction.

To create a tracker using the Amazon Location console

1.  Open the [Amazon Location Service console](https://console.aws.amazon.com/location/).

1.  In the left navigation pane, choose **Trackers**.

1.  Choose **Create tracker**.

1.  Fill in the all the required fields.

1.  Under **Position filtering**, choose the option that best fits how you intend to use your tracker resource. If you do not set Position filtering, the default setting is TimeBased. For more information, see Trackers in this guide, and PositionFiltering in the Amazon Location Service Trackers API Reference.

1.  Choose **Create tracker** to finish.

## Create a Geofence Collection
<a name="qs-ios-tracking-geofence"></a>

When creating a geofence collection you can use either the console, API or CLI. The following procedures walk you through each option.

Create a geofence collection using the Amazon Location console:

1.  Open the Amazon Location Service console at https://console.aws.amazon.com/location/.

1.  In the left navigation pane, choose Geofence Collections.

1.  Choose Create geofence collection.

1.  Provide a name and description for the collection.

1.  Under EventBridge rule with CloudWatch as a target, you can create an optional EventBridge rule to get started reacting to geofence events. This enables Amazon Location to publish events to Amazon CloudWatch Logs.

1.  Choose Create geofence collection.

Create a geofence collection using the Amazon Location APIs:

Use the CreateGeofenceCollection operation from the Amazon Location Geofences APIs. The following example uses an API request to create a geofence collection called `{{GOECOLLECTION_NAME}}`.

```
POST /geofencing/v0/collections
Content-type: application/json
    {
        "CollectionName": "{{GOECOLLECTION_NAME}}",
        "Description": "Geofence collection 1 for shopping center",
        "Tags": { 
            "Tag1" : "Value1"
                }
    }
```

Create a geofence collection using AWS CLI commands:

Use the create-geofence-collection command. The following example uses an AWS CLI to create a geofence collection called `{{GOECOLLECTION_NAME}}`.

```
aws location \ create-geofence-collection \
    --collection-name "{{GOECOLLECTION_NAME}}" \
    --description "Shopping center geofence collection" \
    --tags Tag1=Value1                 
```

## Link a tracker to a geofence collection
<a name="qs-ios-tracking-link-geofence"></a>

To link a tracker to a geofence collection you can use either the console, API, or CLI. The following procedures walk you through each option.

Link a tracker resource to a geofence collection using the Amazon Location Service console:

1. Open the Amazon Location console.

1. In the left navigation pane, choose **Trackers**.

1. Under **Device Trackers**, select the name link of the target tracker.

1. Under **Linked Geofence Collections**, choose **Link Geofence Collection**.

1. In the **Linked Geofence Collection window**, select a geofence collection from the dropdown menu.

1. Choose **Link**.

1. After you link the tracker resource, it will be assigned an Active status.

Link a tracker resource to a geofence collection using the Amazon Location APIs:

Use the ``AsssociateTrackerConsumer operation from the Amazon Location Trackers APIs. The following example uses an API request that associates ExampleTracker with a geofence collection using its Amazon Resource Name (ARN).

```
POST /tracking/v0/trackers/ExampleTracker/consumers
Content-type: application/json
        {
           "ConsumerArn": "arn:aws:geo:us-west-2:123456789012:geofence-collection/{{GOECOLLECTION_NAME}}"
        }
```

Link a tracker resource to a geofence collection using AWS CLI commands:

Use the `associate-tracker-consumer ` command. The following example uses an AWS CLI to create a geofence collection called `{{GOECOLLECTION_NAME}}`.

```
aws location \
associate-tracker-consumer \
    --consumer-arn "arn:aws:geo:us-west-2:123456789012:geofence-collection/{{GOECOLLECTION_NAME}}" \
    --tracker-name "ExampleTracker"
```

## Use AWS Lambda with MQTT
<a name="qs-ios-tracking-lambda"></a>

Create a Lambda function:

To create a connection between AWS IoT Core and Amazon Location Service, you need an AWS Lambda function to process messages forwarded by EventBridge CloudWatch events. This function will extract any positional data, format it for Amazon Location Service, and submit it through the Amazon Location Tracker API. You can create this function through the AWS Lambda console, or you can use the AWS Command Line Interface (AWS CLI) or the AWS Lambda APIs. To create a Lambda function that publishes position updates to Amazon Location using the console:

1.  Open the AWS Lambda console at https://console.aws.amazon.com/lambda/.

1. From the left navigation, choose Functions.

1. Choose Create Function, and make sure that Author from scratch is selected.

1. Fill out the following boxes:
   + a Function name
   + for the **Runtime** option, choose Node.js 16.x.

1. Choose Create function.

1. Choose the Code tab to open the editor.

1. Overwrite the placeholder code in index.js with the following:

   ```
   const AWS = require('aws-sdk')
   const iot = new AWS.Iot();
   exports.handler =  function(event) {
                 console.log("event===>>>", JSON.stringify(event));
                 var param = {
                   endpointType: "iot:Data-ATS"
                 };
                 iot.describeEndpoint(param, function(err, data) {
                   if (err) {
                     console.log("error===>>>", err, err.stack); // an error occurred
                   } else {
                     var endp = data['endpointAddress'];
                     const iotdata = new AWS.IotData({endpoint: endp});    
                     const trackerEvent = event["detail"]["EventType"];
                     const src = event["source"];
                     const time = event["time"];
                     const gfId = event["detail"]["GeofenceId"];
                     const resources = event["resources"][0];  
                     const splitResources = resources.split(".");  
                     const geofenceCollection = splitResources[splitResources.length - 1];
                     const coordinates = event["detail"]["Position"];                               
                     const deviceId = event["detail"]["DeviceId"]; 
                     console.log("deviceId===>>>", deviceId);
                     const msg =  {
                         "trackerEventType" : trackerEvent,
                         "source" : src,
                         "eventTime" : time,
                         "geofenceId" : gfId,
                         "coordinates": coordinates, 
                         "geofenceCollection": geofenceCollection
                       };
                     const params = {
                       topic: `${deviceId}/tracker`,
                       payload: JSON.stringify(msg),
                       qos: 0
                     };
                     iotdata.publish(params, function(err, data) {
                         if (err) {
                           console.log("error===>>>", err, err.stack); // an error occurred
                         } else {
                           console.log("Ladmbda triggered===>>>", trackerEvent);  // successful response 
                         }
                     }); 
                   }
                 });
               }
   ```

1. Choose Deploy to save the updated function.

1. Choose the Configuration tab.

1. In the Triggers section, click on Add trigger.

1. Select EventBridge (CloudWatch Events) in Source field.

1. Select `Existing Rules` radio option.

1. Enter the rule name like this `AmazonLocationMonitor-GEOFENCECOLLECTION\_NAME`.

1. Click on the Add button.

1. This will also attach `Resource-based policy statements` in permissions tab

MQTT Test Client

1. Open the [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/).

1. In the left navigation pane, choose MQTT test client.

1. You'll see a section titled **MQTT test client** where you can configure your MQTT connection.

1. After configuring the necessary settings, click on the **Connect** button to establish a connection to the MQTT broker using the provided parameters.

1. Make note of the Endpoint value.

Once connected, you can subscribe to MQTT topics or publish messages to topics using the respective input fields provided in the MQTT test client interface. Next you will attach the MQTT Policy:

1.  On the left side menu, under **Manage** expand **Security** option and click on **Policies**.

1. Click on **Create Policy** button.

1. Enter a policy name.

1. On **Policy Document** select **JSON** tab.

1. Copy paste the policy shown below, but make sure to update all elements with your `{{REGION}}` and `{{ACCOUNT_ID}}`:

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
                   {
                     "Action": [
                       "iot:Connect",
                       "iot:Publish",
                       "iot:Subscribe",
                       "iot:Receive"
                     ],
                     "Resource": [
                       "arn:aws:iot:{{REGION}}:{{ACCOUNT_ID}}:client/${cognito-identity.amazonaws.com:sub}",
                       "arn:aws:iot:{{REGION}}:{{ACCOUNT_ID}}:topic/${cognito-identity.amazonaws.com:sub}",
                       "arn:aws:iot:{{REGION}}:{{ACCOUNT_ID}}:topicfilter/${cognito-identity.amazonaws.com:sub}/",
                       "arn:aws:iot:{{REGION}}:{{ACCOUNT_ID}}:topic/${cognito-identity.amazonaws.com:sub}/tracker"
                      ],
                      "Effect": "Allow"
                    }
                  ]
   }
   ```

1. Select the **Create** button to finish.

## Set up sample app code
<a name="qs-ios-tracking-setup-sample"></a>

In order to setup the sample code you must have the following tools installed:
+ Git
+ XCode 15.3 or Later
+ iOS Simulator 16 or later

Use this procedure to set up the sample app code:

1. Clone the git repository from this URL: [https://github.com/aws-geospatial/amazon-location-samples-ios/tree/main/tracking-with-geofence-notifications](https://github.com/aws-geospatial/amazon-location-samples-ios/tree/main/tracking-with-geofence-notifications).

1. Open the `AWSLocationSampleApp.xcodeproj` project file.

1. Wait for the package resolution process.

1. **Optional**: On the project navigation menu rename `ConfigTemplate.xcconfig` to `Config.xcconfig` and fill in the following values:

   ```
   IDENTITY_POOL_ID = `{{YOUR_IDENTITY_POOL_ID}}`
   MAP_NAME = `{{YOUR_MAP_NAME}}`
   TRACKER_NAME = `{{YOUR_TRACKER_NAME}}`
   WEBSOCKET_URL = `{{YOUR_MQTT_TEST_CLIENT_ENDPOINT}}`
   GEOFENCE_ARN = `{{YOUR_GEOFENCE_COLLECTION_NAME}}`
   ```

## Use the sample app
<a name="qs-ios-tracking-usage"></a>

After setting up the sample code you can now run the app on an iOS simulator or a physical device.

1. Build and run the app.

1. The app will ask you for location and notification permissions. You need to allow them.

1. Tap on `Cognito Configuration` button.

1. If you have not filled the values in `Config.xcconfig` file you need to fill out the field with the resources values you have created previously in the configuration screen.

   ```
   IDENTITY_POOL_ID = `{{YOUR_IDENTITY_POOL_ID}}`
   MAP_NAME = `{{YOUR_MAP_NAME}}`
   TRACKER_NAME = `{{YOUR_TRACKER_NAME}}`
   WEBSOCKET_URL = `{{YOUR_MQTT_TEST_CLIENT_ENDPOINT}}`
   GEOFENCE_ARN = `{{YOUR_GEOFENCE_COLLECTION_NAME}}`
   ```

1. Save the configuration

1. You can now see the Filter options for time, distance and accuracy. Use them as per your need.

1. Go to `Tracking` tab in the app and you will see the map and `Start Tracking` button.

1. If you have installed the app on a simulator you may want to simulate location changes. This can be done in Features -> Location menu option. For example select Features -> Location -> Freeway Drive.

1. Tap on `Start Tracking` button. You should see the tracking points on the map.

1. The app is also tracking the locations in the background. So, when you move the app in the background it will ask for your permission to continue tracking in background mode.

1. You can stop the tracking by tapping on `Stop Tracking` button.
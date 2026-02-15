# How to use Tracking SDKs

This topic provides information about how to use Tracking SDKs.

The Amazon Location mobile tracking SDK provides utilities which help easily
authenticate, capture device positions, and send position updates to Amazon Location
Trackers. The SDK supports local filtering of location updates with configurable
update intervals. This reduces data costs and optimizes intermittent
connectivity for your iOS applications.

The iOS tracking SDK is available on GitHub: [Amazon Location Mobile Tracking SDK for iOS](https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios "https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios").

This section covers the following topics for the Amazon Location mobile tracking iOS
SDK:

###### Topics

- [Installation](#loc-mobile-tracking-install-ios "#loc-mobile-tracking-install-ios")
- [Usage](#loc-mobile-tracking-usage-ios "#loc-mobile-tracking-usage-ios")
- [Filters](#loc-mobile-tracking-ios-filters "#loc-mobile-tracking-ios-filters")
- [iOS Mobile SDK tracking
  functions](#loc-mobile-tracking-functions "#loc-mobile-tracking-functions")
- [Examples](#loc-mobile-tracking-example-ios "#loc-mobile-tracking-example-ios")

## Installation

Use the following procedure to install the mobile tracking SDK for
iOS:

1. In your Xcode project, go to **File** and select
   **Add Package Dependencies**.
2. Type the following URL: [https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios/](https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios/ "https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-ios/")
   into the search bar and press the enter key.
3. Select the `amazon-location-mobile-tracking-sdk-ios`
   package and click on **Add Package**.
4. Select the `AmazonLocationiOSTrackingSDK` package
   product and click on **Add Package**.

## Usage

The following procedure shows you how to create an authentication helper
using credentials from Amazon Cognito.

1. After installing the library, you need to add one or both of the
   descriptions into your `info.plist` file:

```
Privacy - Location When In Use Usage Description
Privacy - Location Always and When In Use Usage Description
```

2. Next, import the AuthHelper in your class:

```
import AmazonLocationiOSAuthSDKimport AmazonLocationiOSTrackingSDK
```

3. Then you will create an `AuthHelper` object and use it
   with the AWS SDK, by creating an authentication helper using
   credentials from Amazon Cognito.

```
let authHelper = AuthHelper()
let locationCredentialsProvider = authHelper.authenticateWithCognitoUserPool(identityPoolId: "`My-Cognito-Identity-Pool-Id`", region: "`My-region`") //example: us-east-1
let locationTracker = LocationTracker(provider: locationCredentialsProvider, trackerName: "`My-tracker-name`")

// Optionally you can set ClientConfig with your own values in either initialize or in a separate function
// let trackerConfig = LocationTrackerConfig(locationFilters: [TimeLocationFilter(), DistanceLocationFilter()],

     trackingDistanceInterval: 30,
     trackingTimeInterval: 30,
     logLevel: .debug)

// locationTracker = LocationTracker(provider: credentialsProvider, trackerName: "My-tracker-name",config: trackerConfig)
// locationTracker.setConfig(config: trackerConfig)
```

## Filters

The Amazon Location mobile tracking iOS SDK has three inbuilt location
filters.

- `TimeLocationFilter`: Filters the current location to
  be uploaded based on a defined time interval.
- `DistanceLocationFilter`: Filters location updates
  based on a specified distance threshold.
- `AccuracyLocationFilter`: Filters location updates by
  comparing the distance moved since the last update with the current
  location's accuracy.

This example adds filters in the `LocationTracker` at the
creation time:

```
val config = LocationTrackerConfig(
    trackerName = "MY-TRACKER-NAME",
    logLevel = TrackingSdkLogLevel.DEBUG,
    accuracy = Priority.PRIORITY_HIGH_ACCURACY,
    latency = 1000,
    frequency = 5000,
    waitForAccurateLocation = false,
    minUpdateIntervalMillis = 5000,
    locationFilters = mutableListOf(TimeLocationFilter(), DistanceLocationFilter(), AccuracyLocationFilter())
)

locationTracker = LocationTracker(
    applicationContext,
    locationCredentialsProvider,
    config,
)
```

This example enables and disables filter at runtime with
`LocationTracker`:

```
// To enable the filter
locationTracker?.enableFilter(TimeLocationFilter())

// To disable the filter
locationTracker?.disableFilter(TimeLocationFilter())
```

## iOS Mobile SDK tracking

functions

The Amazon Location mobile tracking SDK for iOS includes the following
functions:

- **Class**: `LocationTracker`

`init(provider: LocationCredentialsProvider, trackerName:
 String, config: LocationTrackerConfig? = nil)`

This is an initializer function to create a
`LocationTracker` object. It requires instances of
`LocationCredentialsProvider` ,
`trackerName` and optionally an instance of
`LocationTrackingConfig`. If the config is not
provided it will be initialized with default values.

- **Class**: `LocationTracker`

`setTrackerConfig(config:
 LocationTrackerConfig)`

This sets Tracker's config to take effect at any point after
initialization of location tracker.

- **Class**: `LocationTracker`

`getTrackerConfig()`

This gets the location tracking config to use or modify in your
app.

Returns: `LocationTrackerConfig`

- **Class**: `LocationTracker`

`getDeviceId()`

Gets the location tracker's generated device Id.

Returns: `String?`

- **Class**: `LocationTracker`

`startTracking()`

Starts the process of accessing the user's location and sending it
to the AWS tracker.

- **Class**: `LocationTracker`

`resumeTracking()`

Resumes the process of accessing the user's location and sending
it to the AWS tracker.

- **Class**: `LocationTracker`

`stopTracking()`

Stops the process of tracking the user's location.

- **Class**: `LocationTracker`

`startBackgroundTracking(mode:
 BackgroundTrackingMode)`

Starts the process of accessing the user's location and sending it
to the AWS tracker while the application is in the background.
`BackgroundTrackingMode` has the following options:

    + `Active:` This option doesn't automatically
     pauses location updates.
    + `BatterySaving:` This option automatically
     pauses location updates.
    + `None:` This option overall disables background
     location updates.

- **Class**: `LocationTracker`

`resumeBackgroundTracking(mode:
 BackgroundTrackingMode)`

Resumes the process of accessing the user's location and sending
it to the AWS tracker while the application is in the
background.

- **Class**: `LocationTracker`

`stopBackgroundTracking()`

Stops the process of accessing the user's location and sending it
to the AWS tracker while the application is in the
background.

- **Class**: `LocationTracker`

`getTrackerDeviceLocation(nextToken: String?, startTime:
 Date? = nil, endTime: Date? = nil, completion: @escaping
 (Result<GetLocationResponse, Error>)`

Retrieves the uploaded tracking locations for the user's device
between start and end date and time.

Returns: `Void`

- **Class**:
  `LocationTrackerConfig`

`init()`

This initializes the LocationTrackerConfig with default
values.

- **Class**:
  `LocationTrackerConfig`

`init(locationFilters: [LocationFilter]? = nil,
 trackingDistanceInterval: Double? = nil, trackingTimeInterval:
 Double? = nil, trackingAccuracyLevel: Double? = nil,
 uploadFrequency: Double? = nil, desiredAccuracy:
 CLLocationAccuracy? = nil, activityType: CLActivityType? = nil,
 logLevel: LogLevel? = nil)`

This initializes the `LocationTrackerConfig` with
user-defined parameter values. If a parameter value is not provided
it will be set to a default value.

- **Class**: `LocationFilter`

`shouldUpload(currentLocation: LocationEntity,
 previousLocation: LocationEntity?, trackerConfig:
 LocationTrackerConfig)`

The `LocationFilter` is a protocol that users can
implement for their custom filter implementation. A user would need
to implement `shouldUpload` function to compare previous
and current location and return if the current location should be
uploaded.

## Examples

This sections details examples of using the Amazon Location Mobile Tracking SDK
for iOS.

###### Note

Ensure that the necessary permissions are set in the
`info.plist` file. These are the same permissions listed
in the [Usage](#loc-mobile-tracking-usage-ios "#loc-mobile-tracking-usage-ios") section.

The following example demonstrates functionality for tracking device
location and retrieving tracked locations:

```
Privacy - Location When In Use Usage Description
Privacy - Location Always and When In Use Usage Description
```

Start tracking the location:

```
do {
    try locationTracker.startTracking()
    }
catch TrackingLocationError.permissionDenied {
        // Handle permissionDenied by showing the alert message or opening the app settings
        }
```

Resume tracking the location:

```
do {
    try locationTracker.resumeTracking()
    }
catch TrackingLocationError.permissionDenied {
    // Handle permissionDenied by showing the alert message or opening the app settings
    }
```

Stop tracking the location:

```
locationTracker.stopTracking()
```

Start background tracking:

```
do {
    locationTracker.startBackgroundTracking(mode: .Active) // .Active, .BatterySaving, .None
    }
catch TrackingLocationError.permissionDenied {
   // Handle permissionDenied by showing the alert message or opening the app settings
   }
```

Resume background tracking:

```
do {
    locationTracker.resumeBackgroundTracking(mode: .Active)
    }
catch TrackingLocationError.permissionDenied {
    // Handle permissionDenied by showing the alert message or opening the app settings
    }
```

To stop background tracking:

```
locationTracker.stopBackgroundTracking()
```

Retrieve device's tracked locations from the tracker:

```
func getTrackingPoints(nextToken: String? = nil) {
let startTime: Date = Date().addingTimeInterval(-86400) // Yesterday's day date and time
let endTime: Date = Date()
locationTracker.getTrackerDeviceLocation(nextToken: nextToken, startTime: startTime, endTime: endTime, completion: { [weak self] result in
    switch result {
    case .success(let response):

        let positions = response.devicePositions
        // You can draw positions on map or use it further as per your requirement

        // If nextToken is available, recursively call to get more data
        if let nextToken = response.nextToken {
            self?.getTrackingPoints(nextToken: nextToken)
        }
    case .failure(let error):
        print(error)
    }
})
}
```

The Amazon Location mobile tracking SDK provides utilities which help easily
authenticate, capture device positions, and send position updates to Amazon Location
Trackers. The SDK supports local filtering of location updates with configurable
update intervals. This reduces data costs and optimizes intermittent
connectivity for your Android applications.

The Android tracking SDK is available on GitHub: [Amazon Location Mobile Tracking SDK for Android](https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-android "https://github.com/aws-geospatial/amazon-location-mobile-tracking-sdk-android"). Additionally, both the
mobile authentication SDK and the AWS SDK are available on the [AWS Maven repository](https://central.sonatype.com/artifact/software.amazon.location/tracking "https://central.sonatype.com/artifact/software.amazon.location/tracking"). The Android tracking SDK is designed to
work with the general AWS SDK.

This section covers the following topics for the Amazon Location mobile tracking
Android SDK:

###### Topics

- [Installation](#loc-mobile-tracking-install-android "#loc-mobile-tracking-install-android")
- [Usage](#loc-mobile-tracking-usage-android "#loc-mobile-tracking-usage-android")
- [Filters](#loc-mobile-tracking-android-filters "#loc-mobile-tracking-android-filters")
- [Android Mobile SDK tracking
  functions](#loc-mobile-tracking-functions "#loc-mobile-tracking-functions")
- [Examples](#loc-mobile-tracking-example-android "#loc-mobile-tracking-example-android")

## Installation

To install the SDK, add the following lines to the dependencies section of
your build.gradle file in Android Studio:

```
implementation("software.amazon.location:tracking:0.0.1")
implementation("software.amazon.location:auth:0.0.1")
implementation("com.amazonaws:aws-android-sdk-location:2.72.0")
```

## Usage

This procedure shows you how to use the SDK to authenticate and create the
`LocationTracker` object:

###### Note

This procedure assumes you have imported the library mentioned in the
[Installation](#loc-mobile-tracking-install-android "#loc-mobile-tracking-install-android")
section.

1. Import the following classes in your code:

```
import software.amazon.location.tracking.LocationTracker
import software.amazon.location.tracking.config.LocationTrackerConfig
import software.amazon.location.tracking.util.TrackingSdkLogLevel
import com.amazonaws.services.geo.AmazonLocationClient
import software.amazon.location.auth.AuthHelper
import software.amazon.location.auth.LocationCredentialsProvider
```

2. Next create an `AuthHelper`, since the
   `LocationCredentialsProvider` parameter is required
   for creating a `LocationTracker` object:

```
// Create an authentication helper using credentials from Amazon Cognito
val authHelper = AuthHelper(applicationContext)
val locationCredentialsProvider : LocationCredentialsProvider = authHelper.authenticateWithCognitoIdentityPool("My-Cognito-Identity-Pool-Id")

```

3. Now, use the `LocationCredentialsProvider` and
   `LocationTrackerConfig` to create a
   `LocationTracker` object:

```
val config = LocationTrackerConfig(
    trackerName = "MY-TRACKER-NAME",
    logLevel = TrackingSdkLogLevel.DEBUG,
    accuracy = Priority.PRIORITY_HIGH_ACCURACY,
    latency = 1000,
    frequency = 5000,
    waitForAccurateLocation = false,
    minUpdateIntervalMillis = 5000,
)
locationTracker = LocationTracker(
    applicationContext,
    locationCredentialsProvider,
    config,
)
```

## Filters

The Amazon Location mobile tracking Android SDK has three inbuilt location
filters.

- `TimeLocationFilter`: Filters the current location to
  be uploaded based on a defined time interval.
- `DistanceLocationFilter`: Filters location updates
  based on a specified distance threshold.
- `AccuracyLocationFilter`: Filters location updates by
  comparing the distance moved since the last update with the current
  location's accuracy.

This example adds filters in the `LocationTracker` at the
creation time:

```
val config = LocationTrackerConfig(
    trackerName = "MY-TRACKER-NAME",
    logLevel = TrackingSdkLogLevel.DEBUG,
    accuracy = Priority.PRIORITY_HIGH_ACCURACY,
    latency = 1000,
    frequency = 5000,
    waitForAccurateLocation = false,
    minUpdateIntervalMillis = 5000,
    locationFilters = mutableListOf(TimeLocationFilter(), DistanceLocationFilter(), AccuracyLocationFilter())
)
locationTracker = LocationTracker(
    applicationContext,
    locationCredentialsProvider,
    config,
)
```

This example enables and disables filter at runtime with
`LocationTracker`:

```
// To enable the filter
locationTracker?.enableFilter(TimeLocationFilter())

// To disable the filter
locationTracker?.disableFilter(TimeLocationFilter())
```

## Android Mobile SDK tracking

functions

The Amazon Location mobile tracking SDK for Android includes the following
functions:

- **Class**: `LocationTracker`

`constructor(context: Context,locationCredentialsProvider:
 LocationCredentialsProvider,trackerName: String)`, or
`constructor(context: Context,locationCredentialsProvider:
 LocationCredentialsProvider,clientConfig:
 LocationTrackerConfig)`

This is an initializer function to create a
`LocationTracker` object. It requires instances of
`LocationCredentialsProvider` ,
`trackerName` and optionally an instance of
`LocationTrackingConfig`. If the config is not
provided it will be initialized with default values.

- **Class**: `LocationTracker`

`start(locationTrackingCallback:
 LocationTrackingCallback)`

Starts the process of accessing the user's location and sending it
to an Amazon Location tracker.

- **Class**: `LocationTracker`

`isTrackingInForeground()`

Checks if location tracking is currently in progress.

- **Class**: `LocationTracker`

`stop()`

Stops the process of tracking the user's location.

- **Class**: `LocationTracker`

`startTracking()`

Starts the process of accessing the user's location and sending it
to the AWS tracker.

- **Class**: `LocationTracker`

`startBackground(mode: BackgroundTrackingMode,
 serviceCallback: ServiceCallback)`

Starts the process of accessing the user's location and sending it
to the AWS tracker while the application is in the background.
`BackgroundTrackingMode` has the following
options:

    + `ACTIVE_TRACKING`: This option actively tracks
     a user's location updates.
    + `BATTERY_SAVER_TRACKING`: This option tracks
     user's location updates every 15 minutes.

- **Class**: `LocationTracker`

`stopBackgroundService()`

Stops the process of accessing the user's location and sending it
to the AWS tracker while the application is in the
background.

- **Class**: `LocationTracker`

`getTrackerDeviceLocation()`

Retrieves the device location from Amazon Location services.

- **Class**: `LocationTracker`

`getDeviceLocation(locationTrackingCallback:
 LocationTrackingCallback?)`

Retrieves the current device location from the fused location
provider client and uploads it to Amazon Location tracker.

- **Class**: `LocationTracker`

`uploadLocationUpdates(locationTrackingCallback:
 LocationTrackingCallback?)`

Uploads the device location to Amazon Location services after filtering
based on the configured location filters.

- **Class**: `LocationTracker`

`enableFilter(filter: LocationFilter)`

Enables a particular location filter.

- **Class**: `LocationTracker`

`checkFilterIsExistsAndUpdateValue(filter:
 LocationFilter)`

Disable particular location filter.

- **Class**:
  `LocationTrackerConfig`

`LocationTrackerConfig( // Required var trackerName: String,
 // Optional var locationFilters: MutableList = mutableListOf(
 TimeLocationFilter(), DistanceLocationFilter(), ), var logLevel:
 TrackingSdkLogLevel = TrackingSdkLogLevel.DEBUG, var accuracy:
 Int = Priority.PRIORITY_HIGH_ACCURACY, var latency: Long = 1000,
 var frequency: Long = 1500, var waitForAccurateLocation: Boolean
 = false, var minUpdateIntervalMillis: Long = 1000, var
 persistentNotificationConfig: NotificationConfig =
 NotificationConfig())`

This initializes the `LocationTrackerConfig` with
user-defined parameter values. If a parameter value is not provided,
it will be set to a default value.

- **Class**: `LocationFilter`

`shouldUpload(currentLocation: LocationEntry,
 previousLocation: LocationEntry?): Boolean`

The `LocationFilter` is a protocol that users can
implement for their custom filter implementation. You need to
implement the `shouldUpload` function to compare previous
and current location and return if the current location should be
uploaded.

## Examples

The following code sample shows the mobile tracking SDK
functionality.

This example uses the `LocationTracker` to start and stop
tracking in background:

```
// For starting the location tracking
locationTracker?.startBackground(
BackgroundTrackingMode.ACTIVE_TRACKING,
object : ServiceCallback {
    override fun serviceStopped() {
        if (selectedTrackingMode == BackgroundTrackingMode.ACTIVE_TRACKING) {
            isLocationTrackingBackgroundActive = false
        } else {
            isLocationTrackingBatteryOptimizeActive = false
        }
    }
},
)

// For stopping the location tracking
locationTracker?.stopBackgroundService()
```

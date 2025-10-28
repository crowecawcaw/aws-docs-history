# How to use authentication helpers

This section provides additional information about authentication helpers.

The Amazon Location JavaScript authentication utilities assistw in authenticating when making Amazon Location Service API calls from JavaScript applications.
These utilities specifically support authentication using API keys or Amazon Cognito.

**Installation**

- Install this library using NPM:

```
npm install @aws/amazon-location-utilities-auth-helper
```

- To use it directly in the browser, include the following in your HTML file:

```
<script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-utilities-auth-helper@1"></script>
```

### Usage

To use the authentication helpers, import the library and call the necessary utility functions.
This library supports authenticating requests from the Amazon Location Service SDKs,
including the [Maps](../../../AWSJavaScriptSDK/v3/latest/client/geo-maps.md "../../../AWSJavaScriptSDK/v3/latest/client/geo-maps.md"),
[Places](../../../AWSJavaScriptSDK/v3/latest/client/geo-places.md "../../../AWSJavaScriptSDK/v3/latest/client/geo-places.md"), and
[Routes](../../../AWSJavaScriptSDK/v3/latest/client/geo-routes.md "../../../AWSJavaScriptSDK/v3/latest/client/geo-routes.md") standalone SDKs, as well as
rendering maps with [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js "https://github.com/maplibre/maplibre-gl-js").

**Usage with Modules**

This example demonstrates the use of the standalone Places SDK to make a request authenticated with API keys:

```
npm install @aws-sdk/geo-places-client

import { GeoPlacesClient, GeocodeCommand } from "@aws-sdk/geo-places-client";
import { withAPIKey } from "@aws/amazon-location-utilities-auth-helper";

const authHelper = withAPIKey("<API Key>", "<Region>");
const client = new GeoPlacesClient(authHelper.getClientConfig());

const input = { ... };
const command = new GeocodeCommand(input);
const response = await client.send(command);
```

This example demonstrates the use of the standalone Routes SDK to make a request authenticated with API keys:

```
npm install @aws-sdk/geo-routes-client

import { GeoRoutesClient, CalculateRoutesCommand } from "@aws-sdk/geo-routes-client";
import { withAPIKey } from "@aws/amazon-location-utilities-auth-helper";

const authHelper = withAPIKey("<API Key>", "<Region>");
const client = new GeoRoutesClient(authHelper.getClientConfig());

const input = { ... };
const command = new CalculateRoutesCommand(input);
const response = await client.send(command);
```

This example uses the Location SDK with API key authentication:

```
npm install @aws-sdk/client-location

import { LocationClient, ListGeofencesCommand } from "@aws-sdk/client-location";
import { withAPIKey } from "@aws/amazon-location-utilities-auth-helper";

const authHelper = withAPIKey("<API Key>", "<Region>");
const client = new LocationClient(authHelper.getClientConfig());

const input = { ... };
const command = new ListGeofencesCommand(input);
const response = await client.send(command);
```

**Usage with Browser**

Utility functions are accessible under the amazonLocationAuthHelper global object when used directly in a browser environment.

This example demonstrates a request with the Amazon Location Client, authenticated using API keys:

```
<script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-client@1"></script>

const authHelper = amazonLocationClient.withAPIKey("<API Key>", "<Region>");
const client = new amazonLocationClient.GeoRoutesClient(authHelper.getClientConfig());
const input = { ... };
const command = new amazonLocationClient.routes.CalculateRoutesCommand(input);
const response = await client.send(command);
```

This example demonstrates rendering a map with MapLibre GL JS, authenticated with an API key:

```
<script src="https://cdn.jsdelivr.net/npm/maplibre-gl@4"></script>

const apiKey = "<API Key>";
const region = "<Region>";
const styleName = "Standard";

const map = new maplibregl.Map({
  container: "map",
  center: [-123.115898, 49.295868],
  zoom: 10,
  style: `https://maps.geo.${region}.amazonaws.com/v2/styles/${styleName}/descriptor?key=${apiKey}`,
});
```

This example demonstrates rendering a map with MapLibre GL JS using Amazon Cognito:

```
<script src="https://cdn.jsdelivr.net/npm/maplibre-gl@4"></script>
<script src="https://cdn.jsdelivr.net/npm/@aws/amazon-location-utilities-auth-helper@1"></script>

const identityPoolId = "<Identity Pool ID>";
const authHelper = await amazonLocationAuthHelper.withIdentityPoolId(identityPoolId);

const map = new maplibregl.Map({
  container: "map",
  center: [-123.115898, 49.295868],
  zoom: 10,
  style: `https://maps.geo.${region}.amazonaws.com/v2/styles/${styleName}/descriptor`,
  ...authHelper.getMapAuthenticationOptions(),
});
```

**Alternative Usage with Authenticated Identities**

You can modify the withIdentityPoolId function to include custom parameters for authenticated identities:

```
const userPoolId = "<User Pool ID>";

const authHelper = await amazonLocationAuthHelper.withIdentityPoolId(identityPoolId, {
  logins: {
    [`cognito-idp.${region}.amazonaws.com/${userPoolId}`]: "cognito-id-token"
  }
});
```

The Amazon Location Service Mobile Authentication SDK for iOS helps authenticate requests to Amazon Location Service APIs from iOS applications.
It specifically supports authentication via API keys or Amazon Cognito.

**Installation**

- Open Xcode and go to **File > Add Package Dependencies**.
- Type the package URL ([https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios/](https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios/ "https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios/")) into the search bar and press Enter.
- Select the "amazon-location-mobile-auth-sdk-ios" package and click **Add Package**.
- Choose the "AmazonLocationiOSAuthSDK" package product and click **Add Package**.

### Usage

After installing the library, use the `AuthHelper` class to configure client settings for either API keys or Amazon Cognito.

**API Keys**

Here is an example using the standalone Places SDK with API key authentication:

```
import AmazonLocationiOSAuthSDK
import AWSGeoPlaces

func geoPlacesExample() {
    let apiKey = "<API key>"
    let region = "<Region>"

    let authHelper = try await AuthHelper.withApiKey(apiKey: apiKey, region: region)
    let client: GeoPlacesClient = GeoPlacesClient(config: authHelper.getGeoPlacesClientConfig())

    let input = AWSGeoPlaces.SearchTextInput(
        biasPosition: [-97.7457518, 30.268193],
        queryText: "tacos"
    )

    let output = try await client.searchText(input: input)
}
```

Here is an example using the standalone Routes SDK with API key authentication:

```
import AmazonLocationiOSAuthSDK
import AWSGeoRoutes

func geoRoutesExample() {
    let apiKey = "<API key>"
    let region = "<Region>"

    let authHelper = try await AuthHelper.withApiKey(apiKey: apiKey, region: region)
    let client: GeoRoutesClient = GeoRoutesClient(config: authHelper.getGeoRoutesClientConfig())

    let input = AWSGeoRoutes.CalculateRoutesInput(
        destination: [-123.1651031, 49.2577281],
        origin: [-97.7457518, 30.268193]
    )

    let output = try await client.calculateRoutes(input: input)
}
```

Here is an example using the Location SDK with API key authentication:

```
import AmazonLocationiOSAuthSDK
import AWSLocation

func locationExample() {
    let apiKey = "<API key>"
    let region = "<Region>"

    let authHelper = try await AuthHelper.withApiKey(apiKey: apiKey, region: region)
    let client: LocationClient = LocationClient(config: authHelper.getLocationClientConfig())

    let input = AWSLocation.ListGeofencesInput(
        collectionName: "<Collection name>"
    )

    let output = try await client.listGeofences(input: input)
}
```

Here is an example using the standalone Places SDK with Amazon Cognito:

```
import AmazonLocationiOSAuthSDK
import AWSGeoPlaces

func geoPlacesExample() {
    let identityPoolId = "<Identity Pool ID>"

    let authHelper = try await AuthHelper.withIdentityPoolId(identityPoolId: identityPoolId)
    let client: GeoPlacesClient = GeoPlacesClient(config: authHelper.getGeoPlacesClientConfig())

    let input = AWSGeoPlaces.SearchTextInput(
        biasPosition: [-97.7457518, 30.268193],
        queryText: "tacos"
    )

    let output = try await client.searchText(input: input)
}
```

Here is an example using the standalone Routes SDK with Amazon Cognito:

```
import AmazonLocationiOSAuthSDK
import AWSGeoRoutes

func geoRoutesExample() {
    let identityPoolId = "<Identity Pool ID>"

    let authHelper = try await AuthHelper.withIdentityPoolId(identityPoolId: identityPoolId)
    let client: GeoRoutesClient = GeoRoutesClient(config: authHelper.getGeoRoutesClientConfig())

    let input = AWSGeoRoutes.CalculateRoutesInput(
        destination: [-123.1651031, 49.2577281],
        origin: [-97.7457518, 30.268193]
    )

    let output = try await client.calculateRoutes(input: input)
}
```

Here is an example using the Location SDK with Amazon Cognito:

```
import AmazonLocationiOSAuthSDK
import AWSLocation

func locationExample() {
    let identityPoolId = "<Identity Pool ID>"

    let authHelper = try await AuthHelper.withIdentityPoolId(identityPoolId: identityPoolId)
    let client: LocationClient = LocationClient(config: authHelper.getLocationClientConfig())

    let input = AWSLocation.ListGeofencesInput(
        collectionName: "<Collection name>"
    )

    let output = try await client.listGeofences(input: input)
}
```

The Amazon Location Service Mobile Authentication SDK for Android helps you authenticate requests to Amazon Location Service APIs from
Android applications, specifically supporting authentication using Amazon Cognito.

**Installation**

- This authentication SDK works with the overall AWS Kotlin SDK. Both SDKs are published to Maven Central. Check the latest version of the [auth SDK](https://mvnrepository.com/artifact/software.amazon.location/auth "https://mvnrepository.com/artifact/software.amazon.location/auth") on Maven Central.
- Add the following lines to the dependencies section of your `build.gradle` file in Android Studio:

```
implementation("software.amazon.location:auth:1.1.0")
implementation("org.maplibre.gl:android-sdk:11.5.2")
implementation("com.squareup.okhttp3:okhttp:4.12.0")
```

- For the standalone Maps, Places, and Routes SDKs, add the following lines:

```
implementation("aws.sdk.kotlin:geomaps:1.3.65")
implementation("aws.sdk.kotlin:geoplaces:1.3.65")
implementation("aws.sdk.kotlin:georoutes:1.3.65")
```

- For the consolidated Location SDK that includes Geofencing and Tracking, add the following line:

```
implementation("aws.sdk.kotlin:location:1.3.65")
```

### Usage

Import the following classes in your code:

```
// For the standalone Maps, Places, and Routes SDKs
import aws.sdk.kotlin.services.geomaps.GeoMapsClient
import aws.sdk.kotlin.services.geoplaces.GeoPlacesClient
import aws.sdk.kotlin.services.georoutes.GeoRoutesClient

// For the consolidated Location SDK
import aws.sdk.kotlin.services.location.LocationClient

import software.amazon.location.auth.AuthHelper
import software.amazon.location.auth.LocationCredentialsProvider
import software.amazon.location.auth.AwsSignerInterceptor
import org.maplibre.android.module.http.HttpRequestUtil
import okhttp3.OkHttpClient
```

You can create an `AuthHelper` and use it with the AWS Kotlin SDK:

**Example: Credential Provider with Identity Pool ID**

```
private suspend fun exampleCognitoLogin() {
    val authHelper = AuthHelper.withCognitoIdentityPool("MY-COGNITO-IDENTITY-POOL-ID", applicationContext)

    var geoMapsClient = GeoMapsClient(authHelper?.getGeoMapsClientConfig())
    var geoPlacesClient = GeoPlacesClient(authHelper?.getGeoPlacesClientConfig())
    var geoRoutesClient = GeoRoutesClient(authHelper?.getGeoRoutesClientConfig())

    var locationClient = LocationClient(authHelper?.getLocationClientConfig())
}
```

**Example: Credential Provider with Custom Credential Provider**

```
private suspend fun exampleCustomCredentialLogin() {
    var authHelper = AuthHelper.withCredentialsProvider(MY-CUSTOM-CREDENTIAL-PROVIDER, "MY-AWS-REGION", applicationContext)

    var geoMapsClient = GeoMapsClient(authHelper?.getGeoMapsClientConfig())
    var geoPlacesClient = GeoPlacesClient(authHelper?.getGeoPlacesClientConfig())
    var geoRoutesClient = GeoRoutesClient(authHelper?.getGeoRoutesClientConfig())

    var locationClient = LocationClient(authHelper?.getLocationClientConfig())
}
```

**Example: Credential Provider with API Key**

```
private suspend fun exampleApiKeyLogin() {
    var authHelper = AuthHelper.withApiKey("MY-API-KEY", "MY-AWS-REGION", applicationContext)

    var geoMapsClient = GeoMapsClient(authHelper?.getGeoMapsClientConfig())
    var geoPlacesClient = GeoPlacesClient(authHelper?.getGeoPlacesClientConfig())
    var geoRoutesClient = GeoRoutesClient(authHelper?.getGeoRoutesClientConfig())

    var locationClient = LocationClient(authHelper?.getLocationClientConfig())
}
```

You can use `LocationCredentialsProvider` to load the MapLibre map. Here is an example:

```
HttpRequestUtil.setOkHttpClient(
    OkHttpClient.Builder()
        .addInterceptor(
            AwsSignerInterceptor(
                "geo",
                "MY-AWS-REGION",
                locationCredentialsProvider,
                applicationContext
            )
        )
        .build()
)
```

Use the created clients to make calls to Amazon Location Service. Here is an example that searches for places near a specified latitude and longitude:

```
val suggestRequest = SuggestRequest {
       biasPosition = listOf(-97.718833, 30.405423)
       maxResults = MAX_RESULT
       language = "PREFERRED-LANGUAGE"
   }
val nearbyPlaces = geoPlacesClient.suggest(suggestRequest)
```

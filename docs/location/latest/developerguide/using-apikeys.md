# Use API keys to authenticate

###### Note

API keys are available to use only with **map**,
**place**, and **route** resources, and you can't modify or create those resources. If
your application needs access to other resources or actions for unauthenticated
users, you can use Amazon Cognito to provide access along with, or instead of, API keys.
For more information, see [Use Amazon Cognito to authenticate](authenticating-using-cognito.md "authenticating-using-cognito.md").

_API keys_ are a key value that is associated with
specific Amazon Location Service resources or API in your AWS account, and specific actions that you
can perform on those resources. You can use an API key in your application to make
unauthenticated calls to the Amazon Location APIs for those resources.

For example, if you associate an API key with a resource and/or the
`GetPlace*` API, then an application that uses that API key will be able
to call specific APIs. That same API key would not give permissions to change or update
any resource or call APIs that it isn't associated with.

When you call Amazon Location Service APIs in your applications, you typically make this call as an
_authenticated user_ who is authorized to make the
API calls. However, there are some cases where you don't want to authenticate every user
of your application.

For example, you might want a web application that shows your business location to be
available to anyone using the website, whether they are logged in or not. In this case,
one alternative is to use API keys to make the API calls.

See [API key best practices](#api-keys-best-practices "#api-keys-best-practices") for additional information about when to
use API keys.

For more information about working with keys using the Amazon Location Service API, see the following
topics in the _Amazon Location Service API Reference_:

- [CreateKey](../APIReference/API_WaypointMetadata_CreateKey.md "../APIReference/API_WaypointMetadata_CreateKey.md")
- [DeleteKey](../APIReference/API_WaypointMetadata_DeleteKey.md "../APIReference/API_WaypointMetadata_DeleteKey.md")
- [DescribeKey](../APIReference/API_WaypointMetadata_DescribeKey.md "../APIReference/API_WaypointMetadata_DescribeKey.md")
- [ListKeys](../APIReference/API_WaypointMetadata_ListKeys.md "../APIReference/API_WaypointMetadata_ListKeys.md")

## Create an API key for Amazon Location Service

You can create an API key through the Amazon Location Service console, AWS CLI, or Amazon Location API.
Continue with the appropriate procedures below.

Amazon Location console

###### To create an API key using the Amazon Location Service console

1. In the [**Amazon Location console**](https://console.aws.amazon.com/location "https://console.aws.amazon.com/location"), choose
   **API keys** from the left menu.
2. On the **API keys** page, choose
   **Create API key**.
3. On the **Create API key** page,
   fill in the following information:
   - **Name** – A name for your API
     key, such as `ExampleKey`.
   - **Description** – An optional
     description for your API key.
   - **Resources** – In the
     dropdown, choose the Amazon Location resources to give access
     to with this API key. You can add more than one resource
     by choosing **Add resource**.
   - **Actions** – Specify the
     actions you want to authorize with this API key. You
     must select at least one action to match each resource
     type you have selected. For example, if you selected a
     place resource, you must select at least one of the
     choices under **Places
     Actions**.
   - **Expiration time** –
     Optionally, add an expiration date and time for your API
     key. For more information, see [API key best practices](#api-keys-best-practices "#api-keys-best-practices").
   - **Client restrictions** –
     Optionally, add one or more web domains or one or more
     Android or Apple apps where you can use the API key. For
     example, if the API key is to allow an application
     running on the website `example.com`, then
     you could put `*.example.com/` as an allowed
     referrer.
   - **Tags** – Optionally, add
     tags to the API key.

4. Choose **Create API key** to create the API
   key.
5. On the detail page for the API key, you can see information
   about the API key that you have created. Choose **Show
   API key** to see the key value that you use when
   calling Amazon Location APIs. The key value will have the format
   `v1.public.`a1b2c3d4...``.

AWS CLI

1. Use the [create-key](../../../cli/latest/reference/location/create-key.md "../../../cli/latest/reference/location/create-key.md") command. The following example creates
   an API key called `ExampleKey` with no expiration
   date and access to a single map resource.

```
aws location \
  create-key \
  --key-name ExampleKey \
  --restrictions '{"AllowActions":["geo-maps:*"],"AllowResources":["arn:aws:geo-maps:region::provider/default"]}' \
  --no-expiry
```

2. The response includes the API key value to use when accessing
   resources in your applications. The key value will have the
   format `v1.public.a1b2c3d4...`. To learn more about
   using the API key to render maps, see [Use an API key to call an Amazon Location
   API](#using-apikeys-in-api "#using-apikeys-in-api"). The response to create-key
   looks like the following:

```
{
    "Key": "v1.public.a1b2c3d4...",
    "KeyArn": "arn:aws:geo:region:accountId:api-key/ExampleKey",
    "KeyName": "ExampleKey",
    "CreateTime": "2023-02-06T22:33:15.693Z"
}
```

3. You can also use `describe-key` to find the key
   value at a later time. The following example shows how to call
   `describe-key` on an API key named
   `ExampleKey`.

```
aws location describe-key \
    --key-name ExampleKey
```

Amazon Location API
Use the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation from the Amazon Location APIs. The following
example is an API request to create an API key called
`ExampleKey` with no expiration date and access to a
single map resource.

```
POST /metadata/v0/keys HTTP/1.1
Content-type: application/json
{
  "KeyName": "ExampleKey",
  "NoExpiry": true,
  "Restrictions": {
    "AllowActions": [
      "geo-places:*",
      "geo-routes:*",
      "geo-maps:*"
    ],
    "AllowResources": [
      "arn:aws:geo-places:Region::provider/default",
      "arn:aws:geo-routes:Region::provider/default",
      "arn:aws:geo-maps:Region::provider/default"
    ]
  }
}
```

The response includes the API key value to use when accessing
resources in your applications. The key value will havethe format
`v1.public.a1b2c3d4...`.

You can also use the [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md") API to find the key value for a key at a later
time.

## Use an API key to call an Amazon Location

API

After you create an API key, you can use the key value to make calls to Amazon Location
APIs in your application.

API
The APIs that support API keys have an additional parameter that takes
the API key value. For example, if you call the `GetPlace`
API, you can fill in the [key](../APIReference/API_GetPlace.md#API_GetPlace_RequestSyntax "../APIReference/API_GetPlace.md#API_GetPlace_RequestSyntax") parameter, as follows

```
curl --request GET —url 'https://places.geo.eu-central-1.amazonaws.com/v2/place/{`PLACEID`}?key={`APIKEY`}&language=jp'
```

AWS CLI
When you use the `--key` parameter, you should also use the
`--no-sign-request` parameter, to avoid signing with Sig
v4.

```
aws geo-places get-place --place-id $`PLACEID` --language jp --key $`APIKEY`
```

SDK (web)
Use the following code:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Display a map</title>
        <meta property="og:description" content="Initialize a map in an HTML element with MapLibre GL JS." />
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel='stylesheet' href='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.css' />
        <script src='https://unpkg.com/maplibre-gl@4.x/dist/maplibre-gl.js'></script>
        <style>
            body { margin: 0; }
            #map { height: 100vh; }
        </style>
    </head>
    <body>

        <div id="map"></div>
        <script>

            const apiKey = "<api key>"; // check how to create api key for Amazon Location
            const mapStyle = "Standard";  // eg. Standard, Monochrome, Hybrid, Satellite
            const awsRegion = "eu-central-1"; // eg. us-east-2, us-east-1, us-west-2, ap-south-1, ap-southeast-1, ap-southeast-2, ap-northeast-1, ca-central-1, eu-central-1, eu-west-1, eu-west-2, eu-south-2, eu-north-1, sa-east-1
            const styleUrl = `https://maps.geo.${awsRegion}.amazonaws.com/v2/styles/${mapStyle}/descriptor?key=${apiKey}`;


            const map = new maplibregl.Map({
                container: 'map', // container id
                style: styleUrl, // style URL
                center: [25.24,36.31], // starting position [lng, lat]
                zoom: 2, // starting zoom
            });
        </script>
    </body>
</html>
```

SDK (iOS, Swift)
Use the following code:

```
import UIKit
import MapLibre

class ViewController: UIViewController {
    let apiKey = "`Enter your API key`" // The previously-created API Key to use
    let regionName = "`Enter your region name`" // The service region - us-east-1, ap-south-1, etc
    var mapView: MLNMapView!

    override func viewDidLoad() {
        super.viewDidLoad()
        loadMap()
    }

    func loadMap() {
        let styleName = "Standard" // The map style - Standard, Monochrome, Hybrid, Satellite
        let colorName = "Light" // The color scheme - Light, Dark

        // The Amazon Location Service map style URL that MapLibre will use to render the maps.
        let styleURL = URL(string: "https://maps.geo.\(regionName).amazonaws.com/v2/styles/\(styleName)/descriptor?key=\(apiKey)&color-scheme=\(colorName)")

        // Initialize MapLibre
        mapView = MLNMapView(frame: view.bounds)
        mapView.styleURL = styleURL
        mapView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        // Set the starting camera position and zoom level for the map
        mapView.setCenter(CLLocationCoordinate2D(latitude: 49.246559, longitude: -123.063554), zoomLevel: 10, animated: false)
        view.addSubview(mapView!)
    }
}
```

SDK (Android, Kotlin)
Use the following code:

```
class MapActivity : Activity(), OnMapReadyCallback {

    private lateinit var mBinding: ActivityMapBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        initializeMap(savedInstanceState)
    }

    private fun initializeMap(savedInstanceState: Bundle?) {
        // Init MapLibre
        // See the MapLibre Getting Started Guide for more details
        // https://maplibre.org/maplibre-native/docs/book/android/getting-started-guide.html
        MapLibre.getInstance(this@MapActivity)
        mBinding = ActivityMapBinding.inflate(layoutInflater)
        setContentView(mBinding.root)
        mBinding.mapView.onCreate(savedInstanceState)
        mBinding.mapView.getMapAsync(this)
    }

    override fun onMapReady(mapLibreMap: MapLibreMap) {
        mapLibreMap.setStyle(Style.Builder().fromUri(getMapUrl())) {
            // Set the starting camera position
            mapLibreMap.cameraPosition = CameraPosition.Builder().target(LatLng(49.246559, -123.063554)).zoom(10.0).build()
            mapLibreMap.uiSettings.isLogoEnabled = false
            mapLibreMap.uiSettings.attributionGravity = Gravity.BOTTOM or Gravity.END
            mapLibreMap.uiSettings.setAttributionDialogManager(AttributionDialogManager(this, mapLibreMap))
        }
    }

    // Return the Amazon Location Service map style URL
    // MapLibre will use this to render the maps.
    // awsRegion: The service region - us-east-1, ap-south-1, etc
    // mapStyle: The map style - Standard, Monochrome, Hybrid, Satellite
    // API_KEY: The previously-created API Key to use
    // colorName: The color scheme to use - Light, Dark
    private fun getMapUrl() =
           "https://maps.geo.${getString(R.string.awsRegion)}.amazonaws.com/v2/styles/${getString(R.string.mapStyle)}/descriptor?key=${BuildConfig.API_KEY}&color-scheme=${getString(R.string.colorName)}"

    override fun onStart() {
        super.onStart()
        mBinding.mapView.onStart()
    }

    override fun onResume() {
        super.onResume()
        mBinding.mapView.onResume()
    }

    override fun onPause() {
        super.onPause()
        mBinding.mapView.onPause()
    }

    override fun onStop() {
        super.onStop()
        mBinding.mapView.onStop()
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        mBinding.mapView.onSaveInstanceState(outState)
    }

    override fun onLowMemory() {
        super.onLowMemory()
        mBinding.mapView.onLowMemory()
    }

    override fun onDestroy() {
        super.onDestroy()
        mBinding.mapView.onDestroy()
    }
}
```

## Restrict API key usage by request

origin

You can configure API keys with client restrictions that limit access to specific
domains or mobile applications. When restricting by domain, requests will be
authorized only if the HTTP Referer header matches the value that you provide. When
restricting by Android or Apple application, requests will be authorized only if the
application identifier HTTP header fields match the values that you provide.

For more information, see [ApiKeyRestrictions](../APIReference/API_geotags_ApiKeyRestrictions.md "../APIReference/API_geotags_ApiKeyRestrictions.md") in the _Amazon Location Service API
Reference_.

**Android application identifiers:**

- `X-Android-Package`:

A unique identifier for Android applications, defined in the app's
`build.gradle` file, typically following a reverse-domain
format.

Example:

`com.mydomain.appname`

- `X-Android-Cert`:

The SHA-1 hash of the signing certificate used to sign the Android
APK.

Example:

`BB:0D:AC:74:D3:21:E1:43:67:71:9B:62:91:AF:A1:66:6E:44:5D:75`

**Apple application identifiers:**

- `X-Apple-Bundle-Id` :

A unique identifier for Apple (iOS, macOS, etc.) applications, defined in
the app's `Info.plist`, typically following a reverse-domain
format.

Example:

`com.mydomain.appname`

## API key best practices

API keys include a plain text _value_ that gives access to one
or more resources or APIs in your AWS account. If someone copies your API key,
they can access those same resources and APIs. To minimize the potential impact,
review the following best practices:

- **Limit the API key**

To avoid the situation above, it is best to limit your API key. When you
create the key, you can specify the domain, Android app or Apple app where
the key can be used.

- **Manage API key lifetimes**

You can create API keys that work indefinitely. However, if you want to
create a temporary API key, rotate API keys on a regular basis, or revoke an
existing API key, you can use _API key
expiration_.

    + You can set the expiration time for an API key when you create or
     update it.
    + When an API key reaches its expiration time, the key is
     automatically deactivated. Inactive keys can no longer be used to
     make requests.
    + You can change a temporary key to a permanent key by removing the
     expiration time.
    + You can delete an API key 90 days after deactivating it.
    + If you attempt to deactivate an API key that has been used within
     the last seven days, you'll be prompted to confirm that you want to
     make the change.


    If you are using the Amazon Location Service API or the AWS CLI, set the
     `ForceUpdate` parameter to `true`,
     otherwise you'll receive an error.

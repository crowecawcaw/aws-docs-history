# Use Amazon Cognito to authenticate

You can use Amazon Cognito authentication as an alternative to directly using AWS Identity and Access Management (IAM)
users with frontend SDK requests.

Amazon Cognito provides authentication, authorization, and user management for web and mobile
apps. You can use Amazon Cognito unauthenticated identity pools with Amazon Location as a way for
applications to retrieve temporary, scoped-down AWS credentials.

For more information, see [Getting Started with User Pools](../../../cognito/latest/developerguide/getting-started-with-cognito-user-pools.md "../../../cognito/latest/developerguide/getting-started-with-cognito-user-pools.md") in the _Amazon Cognito
Developer Guide_.

You may want to use this form of authentication for the following reasons:

- **Unauthenticated users** – If you have a website
  with anonymous users, you can use Amazon Cognito identity pools.

For more information, see the section on Use Amazon Cognito to authenticate.

- **Your own authentication** – If you would like
  to use your own authentication process, or combine multiple authentication
  methods, you can use Amazon Cognito Federated Identities.

For more information, see [Getting Started with Federated Identities](../../../cognito/latest/developerguide/getting-started-with-identity-pools.md "../../../cognito/latest/developerguide/getting-started-with-identity-pools.md") in the _Amazon Cognito Developer Guide_.

## Use Amazon Cognito and Amazon Location Service

You can use AWS Identity and Access Management (IAM) policies associated with unauthenticated identity
roles with the following actions:

Maps
List of maps actions

- `geo-maps:GetStaticMap`
- `geo-maps:GetTile`

###### Note

Resource names for the actions above are:

```
arn:aws:geo-maps:region::provider/default
```

Places
List of place actions:

- `geo-places:Geocode`
- `geo-places:ReverseGeocode`
- `geo-places:SearchNearby`
- `geo-places:SearchText`
- `geo-places:Autocomplete`
- `geo-places:Suggest`
- `geo-places:GetPlace`

###### Note

Resource names for the actions above are:

```
arn:aws:geo-places:region::provider/default
```

Routes
List of routes actions:

- `geo-routes:CalculateRoutes`
- `geo-routes:CalculateRouteMatrix`
- `geo-routes:CalculateIsolines`
- `geo-routes:OptimizeWaypoints`
- `geo-routes:SnapToRoads`

###### Note

Resource names for the actions above are:

```
arn:aws:geo-routes:region::provider/default
```

Geofences and Trackers
List of Geofences and Trackers actions

- `geo:GetGeofence`
- `geo:ListGeofences`
- `geo:PutGeofence`
- `geo:BatchDeleteGeofence`
- `geo:BatchPutGeofence`
- `geo:BatchEvaluateGeofences`
- `geo:GetDevicePosition*`
- `geo:ListDevicePositions`
- `geo:BatchDeleteDevicePositionHistory`
- `geo:BatchGetDevicePosition`
- `geo:BatchUpdateDevicePosition`

###### Note

Resource names for the actions above are:

```
arn:aws:geo:region:accountID:tracker/ExampleTracker
```

Previous version
List of previous version actions:

- `geo:GetMap*`
- `geo:SearchPlaceIndexForText`
- `geo:SearchPlaceIndexForPosition`
- `geo:GetPlace`
- `geo:CalculateRoute`
- `geo:CalculateRouteMatrix`

###### Note

Resource names for the actions above are:

**Maps**

```
arn:aws:geo:region:accountID:map/ExampleMap
```

**Places**

```
arn:aws:geo:region:accountID:place-index/ExamplePlaceIndex
```

**Routes**

```
arn:aws:geo:region:accountID:route-calculator/ExampleCalculator
```

## Create an Amazon Cognito identity pool

You can create Amazon Cognito identity pools to allow unauthenticated guest access to your
application through the Amazon Cognito console, the AWS CLI, or the Amazon Cognito APIs.

###### Important

The pool that you create must be in the same AWS account and AWS Region as
the Amazon Location Service resources that you're using.

Console
**To create an identity pool using the Amazon Cognito
console**

1. Go to the [Amazon
   Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
2. Choose **Manage Identity Pools.**
3. Choose **Create new identity pool**, then
   enter a name for your identity pool.
4. From the **Unauthenticated identities**
   collapsible section, choose **Enable access to
   unauthenticated identities**.
5. Choose **Create Pool**.
6. Choose which IAM roles you want to use with your identity
   pool.
7. Expand **View Details**.
8. Under **Unauthenticated identities**, enter a
   role name.
9. Expand the **View Policy Document** section,
   then choose **Edit** to add your policy.
10. Add your policy to grant access to your resources.

###### Note

See the [Use Amazon Cognito and Amazon Location Service](#cognito-and-location "#cognito-and-location") section
above for a list of actions.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
  Sid": "RoutesReadOnly",
  Effect": "Allow",
  Action": [
        // add comma separated value from the previous section
      ],
  Resource": "`value from previous section`"
    }
  ]
}
```

11. Choose **Allow** to create your identity
    pools.

## Use the Amazon Cognito identity pool in web

The following example exchanges the unauthenticated identity pool that you created
for credentials that are then used to call `CalculateIsolines`. To
simplify this work, the example uses the Amazon Location [How to use authentication helpers](how-to-auth-helper.md "how-to-auth-helper.md") procedures. This is in place of both getting and
refreshing the credentials.

This example uses the AWS SDK for JavaScript v3.

```
import { GeoRoutesClient, CalculateIsolinesCommand , } from "@aws-sdk/client-geo-routes"; // ES Modules import
import { withIdentityPoolId } from "@aws/amazon-location-utilities-auth-helper";

const identityPoolId = "<identity pool ID>"; // for example, us-east-1:1sample4-5678-90ef-aaaa-1234abcd56ef

const authHelper = await withIdentityPoolId(identityPoolId);

const client = new GeoRoutesClient({
    ...authHelper.getClientConfig(),
    region: "<region>", // The region containing the identity pool
});

const input = {
    DepartNow: true,
    TravelMode: "Car",
    Origin: [-123.12327, 49.27531],
    Thresholds: {
        Time: [5, 10, 30],
    },
};

const command = new CalculateIsolinesCommand(input);
const response = await client.send(command);

console.log(JSON.stringify(response, null, 2))
```

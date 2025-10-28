# Authenticating your requests

Once you create a tracker resource and you're ready to begin evaluating device
positions against geofences, choose how you would authenticate your requests:

- To explore ways you can access the services, see [Authenticate with Amazon Location Service](access.md "access.md").
- If you want to publish device positions with unauthenticated requests,you
  may want to use Amazon Cognito.

**Example**

The following example shows using an Amazon Cognito identity pool for
authorization, using [AWS JavaScript SDK v3](https://aws.amazon.com/sdk-for-javascript/ "https://aws.amazon.com/sdk-for-javascript/"), and the Amazon Location [Web](how-to-auth-helper.md#loc-sdk-auth-web "how-to-auth-helper.md#loc-sdk-auth-web").

```
import { LocationClient, BatchUpdateDevicePositionCommand } from "@aws-sdk/client-location";
import { withIdentityPoolId } from "@aws/amazon-location-utilities-auth-helper";

// Unauthenticated identity pool you created
const identityPoolId = "`us-east-1:1234abcd-5678-9012-abcd-sample-id`";

// Create an authentication helper instance using credentials from Cognito
const authHelper = await withIdentityPoolId(identityPoolId);

const client = new LocationClient({
  region: "`us-east-1`", // The region containing both the identity pool and tracker resource
  ...authHelper.getLocationClientConfig(), // Provides configuration required to make requests to Amazon Location
});

const input = {
  TrackerName: "`ExampleTracker`",
  Updates: [
    {
      DeviceId: "`ExampleDevice-1`",
      Position: [-123.4567, 45.6789],
      SampleTime: new Date("2020-10-02T19:09:07.327Z"),
    },
    {
      DeviceId: "`ExampleDevice-2`",
      Position: [-123.123, 45.123],
      SampleTime: new Date("2020-10-02T19:10:32Z"),
    },
  ],
};

const command = new BatchUpdateDevicePositionCommand(input);

// Send device position updates
const response = await client.send(command);

```

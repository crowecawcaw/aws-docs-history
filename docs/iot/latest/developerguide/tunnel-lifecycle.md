# Secure tunnel lifecycle

Tunnels can have the status `OPEN` or `CLOSED`. Connections
to the tunnel can have the status `CONNECTED` or
`DISCONNECTED`. The following shows how the different tunnel and
connection statuses work.

1. When you open a tunnel, it has a status of `OPEN`. The tunnel's
   source and destination connection status is set to
   `DISCONNECTED`.
2. When a device (source or destination) connects to the tunnel, the
   corresponding connection status changes to `CONNECTED`.
3. When a device disconnects from the tunnel while the tunnel status remains
   `OPEN`, the corresponding connection status changes back to
   `DISCONNECTED`. A device can connect to and disconnect from a
   tunnel repeatedly as long as the tunnel remains `OPEN`.

###### Note

The client access tokens (CAT) can only be used once to connect to a
tunnel. To reconnect to the tunnel, rotate the client access tokens
using the [RotateTunnelAccessToken](../apireference/API_iot-secure-tunneling_RotateTunnelAccessToken.md "../apireference/API_iot-secure-tunneling_RotateTunnelAccessToken.md") API operation or the [rotate-tunnel-access-token](../../../cli/latest/reference/iotsecuretunneling/rotate-tunnel-access-token.md "../../../cli/latest/reference/iotsecuretunneling/rotate-tunnel-access-token.md") CLI command. For examples, see
[Resolving AWS IoT secure tunneling
connectivity issues by rotating client access tokens](iot-secure-tunneling-troubleshooting.md "iot-secure-tunneling-troubleshooting.md"). 4. When you call `CloseTunnel` or the tunnel remains
`OPEN` for longer than the `MaxLifetimeTimeout`
value, a tunnel's status becomes `CLOSED`. You can configure
`MaxLifetimeTimeout` when calling `OpenTunnel`.
`MaxLifetimeTimeout` defaults to 12 hours if you do not
specify a value.

###### Note

A tunnel cannot be reopened when it is `CLOSED`. 5. You can call `DescribeTunnel` and `ListTunnels` to
view tunnel metadata while the tunnel is visible. The tunnel can be visible
in the AWS IoT console for at least three hours before it is deleted.

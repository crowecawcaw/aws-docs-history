# Amazon DCV server channels

Counters in this set provide information about individual channels in a client connection. There can be additional channels for extensions.

Channel names are:

- `dcv::main`
- `dcv::display`
- `dcv::input`
- `dcv::audio`
- `dcv::filestorage`
- `dcv::clipboard`
  Incoming filestorage traffic is attributed to the `dcv::filestorage` channel.

Outgoing filestorage traffic is included in the **HTTP Download** counters in **DCV Server Connections**.

###### Note

Counters in this set are a subset of the ones in **DCV Server Connections**.

| Counter name          | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| Receive Rate bits/sec | Rate in bits per second at which data is received via the channel |
| Received Bytes        | Total number of bytes received via the channel                    |
| Send Rate bits/sec    | Rate in bits per second at which data is sent via the channel     |
| Sent Bytes            | Total number of bytes sent via the channel                        |

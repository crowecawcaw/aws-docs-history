# Generate and Sign IVS Playback

Tokens

For details on working with JWTs and the supported libraries for signing tokens, visit
[jwt.io](https://jwt.io/ "https://jwt.io/"). On the jwt.io interface, you must enter
your private key to sign tokens. The public key is needed only if you want to verify
tokens.

## Token Schema

All JWTs have three fields: header, payload, and signature.

- The **header** specifies:
  - `alg` is the signing algorithm. This is ES384, an ECDSA
    signature algorithm that uses the SHA-384 hash algorithm.
  - `typ` is the token type, JWT.

```
{
  "alg": "ES384",
  "typ": "JWT"
}
```

- The **payload** contains data specific to
  Amazon IVS:
  - `channel-arn` is a reference for the video-playback
    request.
  - `access-control-allow-origin` is an optional field that
    can be used to restrict playback to a specified [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin "https://developer.mozilla.org/en-US/docs/Glossary/Origin"); i.e., to make a stream viewable from only a
    specified website. For example, you may want to prevent people from
    embedding the player on other websites. By default, playback is
    allowed on all origins. (Note that this restricts only the browser
    client; it does not restrict playback from a non-browser client.)
    This field may contain multiple origins, separated by commas.
    Wildcard domains are allowed: each origin may begin its hostname
    with \* (example: https://\*.amazon.com). If
    `strict-origin-enforcement` is `true`, at
    most 5 domains may be specified; otherwise, there is no
    maximum.
  - `strict-origin-enforcement` is an optional field that
    can be used to strengthen the origin restriction specified in the
    `access-control-allow-origin` field. By default, the
    `access-control-allow-origin` restriction applies
    only to the multivariant playlist. If
    `strict-origin-enforcement` is enabled, the server
    will enforce a requirement that the requesting origin matches the
    token for all playback requests (including multivariant playlist,
    variant playlist, and segments). This means that all clients
    (including non-browser clients) will have to provide a valid
    origin-request header with each request. Use the
    `setOrigin` method to set the header in the IVS iOS
    and Android player SDKs. It is set automatically in web browsers
    except iOS Safari. For iOS Safari, you need to add
    `crossorigin="anonymous"` to the video element, to
    ensure that the origin request header is sent. Example:
    `<video crossorigin="anonymous"></video>`.
  - `single-use-uuid` is an optional field which contains a
    valid [universally unique identifier (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier "https://en.wikipedia.org/wiki/Universally_unique_identifier") that you generate
    as part of authoring the token. If you add this field and a UUID
    value, the associated token that you generate is invalidated once it
    is used to fetch a multivariant playlist and watch a stream.
    Single-use auth tokens make it more difficult for malicious users to
    share a stream on your private channels with other viewers. Note
    that when using the `single-use-uuid` claim, the maximum
    value for the `exp` claim is 10 minutes in the
    future.
  - `viewer-id` is an optional field which contains an ID
    used for tracking and referring to the viewer to whom the token is
    granted. This field is required to enable the ability to revoke the
    viewing session of the viewer in the future. The maximum length is
    40 characters, and the value must qualify as a string. Do not use
    this field for personally identifying, confidential, or sensitive
    information. Note that when using `viewer-id`, the
    maximum value for `exp` is 10 minutes in the
    future.
  - `viewer-session-version` is an optional field which
    contains a version to associate with this viewer session. When
    revoking viewer sessions, this value can be used to filter which
    viewer sessions are revoked. For example, specifying a Unix
    timestamp here would enable revocation of all sessions started
    before the specified time. The value must be a 64-bit signed integer
    (Int64). This field is meant to be provided (optionally) alongside
    `viewer-id`; it does nothing on its own. The default
    value is 0.
  - `maximum-resolution` allows you to specify manifest
    filtering by resolution for a viewer session, based on viewer
    entitlements. For example, setting this field to `HD`
    means the viewer will receive a resolution less than or equal to
    `HD`.
  - `exp` is a Unix UTC timestamp for when the token
    expires. This does not indicate the length of time that the stream
    can be viewed. The token is validated when the viewer initializes
    playback, not throughout the stream. Enter this value as an integer
    type value.

  Note that a Unix timestamp is a numeric value representing the
  number of seconds from 1970-01-01T00:00:00Z UTC until the specified
  UTC date/time, ignoring leap seconds. Different languages measure
  Unix timestamps in different units; e.g., JavaScript’s
  `Date.now()` returns the time in milliseconds. (See
  `exp` in the [JWT RFC section 4.1.4](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4 "https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4").)

```
{
    "aws:channel-arn": "<channel_arn>",
    "aws:access-control-allow-origin": "<your-origin>",
    "aws:strict-origin-enforcement": true,
    "aws:single-use-uuid": "<UUID>",
    "aws:viewer-id": "<viewer_id>",
    "aws:viewer-session-version": "<viewer_session_version>",
    "aws:maximum-resolution": "SD" | "HD" | "FULL_HD",
    "exp": <unix timestamp>
}
```

- To create the **signature**, use the private
  key with the algorithm specified in the header (ES384) to sign the encoded
  header and encoded payload.

```
ECDSASHA384(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  <private-key>
)
```

## Instructions

1. Generate the token’s signature with the ES384 signing algorithm and a
   private key that is associated with one of your playback-key resources (see
   the `ECDSASHA384` example above).
2. Assemble the token.

```
base64UrlEncode(header) + "." +
base64UrlEncode(payload) + "." +
base64UrlEncode(signature)
```

3. Append the signed token to the playback URL as a query parameter.

```
https://b37c565f6d790a14a0e78afaa6808a80.us-west-2.playback.live-video.net/
api/video/v1/aws.ivs.us-west-2.123456789.
channel.fbc789c1-2c56-4ce6-a30a-d99275dc4481.m3u8?token=<token>
```

## Node.js Example

Below is one way to generate a token on the back end (via a microservice or
serverless application) using Node.js.

```
import jwt from "jsonwebtoken";

const getToken = () => {
  const privateChannelArn = process.env.DEMO_PRIVATE_CHANNEL_ARN; // private channel ARN
  const privateChannelPrivateKey = process.env.DEMO_PRIVATE_CHANNEL_PRIVATE_KEY; // playback private key

  const payload = {
    "aws:channel-arn": privateChannelArn,
    "aws:access-control-allow-origin": "*",
    "exp": Date.now() + (60 * 1000), // expires in 1 minute
  };

  const token = jwt.sign(payload, privateChannelPrivateKey, { algorithm: 'ES384' });
  return token;
}

```

In your frontend application, you can retrieve this token and append it to the
playback URL of the private channel, as shown below.

```
const streamUrl = `https://b37c565f6d790a14a0e78afaa6808a80.us-west-2.playback.live-video.net/api/video/v1/aws.ivs.us-west-2.123456789.channel.fbc789c1-2c56-4ce6-a30a-d99275dc4481.m3u8?token.m3u8?token=${token}`
const ivsPlayer = IVSPlayer.create();
ivsPlayer.attachHTMLVideoElement(document.getElementById('video-player'));
ivsPlayer.load(streamUrl);
ivsPlayer.play();

```

# Step 3: Distribute Participant

Tokens

Now that you have a stage, you need to create tokens and distribute them to
participants, to enable the participants to join the stage and start sending and
receiving video. There are two approaches to generating tokens:

- [Create](#getting-started-distribute-tokens-self-signed "#getting-started-distribute-tokens-self-signed")
  tokens with a key pair.
- [Create tokens with the
  IVS real-time-streaming API](#getting-started-distribute-tokens-api "#getting-started-distribute-tokens-api").
  Both of these approaches are described below.

## Creating Tokens with

a Key Pair

You can create tokens on your server application and distribute them to
participants to join a stage. You need to generate an ECDSA public/private key pair
to sign the JWTs and import the public key to IVS. Then IVS can verify the tokens at
the time of stage join.

IVS does not offer key expiry. If your private key is compromised, you must delete
the old public key.

### Create a New Key Pair

There are various ways to create a key pair. Below, we give two
examples.

To create a new key pair in the console, follow these steps:

1. Open the [Amazon IVS
   console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs"). Choose your stage’s region if you are not already
   on it.
2. In the left navigation menu, choose **Real-time
   streaming > Public keys**.
3. Choose **Create public key**. A **Create public key** dialog appears.
4. Follow the prompts and choose **Create**.
5. Amazon IVS generates a new key pair. The public key is imported as a
   public key resource and the private key is immediately made available
   for download. The public key can also be downloaded later if
   necessary.

Amazon IVS generates the key on the client side and does not store the
private key. **_Be sure you
save the key; you cannot retrieve it
later._**

To create a new P384 EC key pair with OpenSSL (you may have to install [OpenSSL](https://www.openssl.org/source/ "https://www.openssl.org/source/") first), follow these
steps. This process enables you to access both the private and public keys. You
need the public key only if you want to test verification of your tokens.

```
openssl ecparam -name secp384r1 -genkey -noout -out priv.pem
openssl ec -in priv.pem -pubout -out public.pem
```

Now import your new public key, using the instructions below.

### Import the

Public Key

Once you have a key pair, you can import the public key into IVS. The private
key is not needed by our system but is employed by you to sign tokens.

To import an existing public key with the console:

1. Open the [Amazon IVS
   console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs"). Choose your stage’s region if you are not already
   on it.
2. In the left navigation menu, choose **Real-time
   streaming > Public keys**.
3. Choose **Import**. An **Import public key** dialog appears.
4. Follow the prompts and choose **Import**.
5. Amazon IVS imports your public key and generates a public key
   resource.

To import an existing public key with the CLI:

```
aws ivs-realtime import-public-key --public-key-material "`cat public.pem`" --region <aws-region>
```

You can omit `--region <aws-region>` if the region is in your
local AWS configuration file.

Here is an example response:

```
{
    "publicKey": {
        "arn": "arn:aws:ivs:us-west-2:123456789012:public-key/f99cde61-c2b0-4df3-8941-ca7d38acca1a",
        "fingerprint": "98:0d:1a:a0:19:96:1e:ea:0a:0a:2c:9a:42:19:2b:e7",
        "publicKeyMaterial": "-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEVjYMV+P4ML6xemanCrtse/FDwsNnpYmS\nS6vRV9Wx37mjwi02hObKuCJqpj7x0lpz0bHm5v1JBvdZYAd/r2LR5aChK+/GM2Wj\nl8MG9NJIVFaw1u3bvjEjzTASSfS1BDX1\n-----END PUBLIC KEY-----\n",
        "tags": {}
    }
}
```

### API

Request

```
POST /ImportPublicKey HTTP/1.1
{
  "publicKeyMaterial": "<pem file contents>"
}
```

### Generate and Sign the Token

For details on working with JWTs and the supported libraries for signing
tokens, visit [jwt.io](https://jwt.io/ "https://jwt.io/"). On the jwt.io
interface, you must enter your private key to sign tokens. The public key is
needed only if you want to verify tokens.

All JWTs have three fields: header, payload, and signature.

The JSON schemas for the JWT’s header and payload are described below.
Alternatively you can copy a sample JSON from the IVS console. To get the header
and payload JSON from the IVS console:

1. Open the [Amazon IVS
   console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs"). Choose your stage’s region if you are not already
   on it.
2. In the left navigation menu, choose **Real-time
   streaming > Stages**.
3. Select the stage you want to use. Select **View
   details**.
4. In the **Participant tokens** section,
   select the drop-down next to **Create
   token**.
5. Select **Build token header and
   payload**.
6. Fill in the form and copy the JWT header and payload shown at the
   bottom of the popup.

#### Token Schema: Header

The header specifies:

- `alg` is the signing algorithm. This is ES384, an ECDSA
  signature algorithm that uses the SHA-384 hash algorithm.
- `typ` is the token type, JWT.
- `kid` is the ARN of the public key used to sign the
  token. It must be the same ARN returned from the [GetPublicKey](../RealTimeAPIReference/API_GetPublicKey.md "../RealTimeAPIReference/API_GetPublicKey.md") API request.

```
{
  "alg": "ES384",
  "typ": "JWT"
  “kid”: “arn:aws:ivs:123456789012:us-east-1:public-key/abcdefg12345”
}

```

#### Token Schema: Payload

The payload contains data specific to IVS. All fields except
`user_id` are mandatory.

- `RegisteredClaims` in the JWT specification are
  reserved claims that need to be provided for stage token to be
  valid:
  - `exp` (expiration time) is a Unix UTC timestamp
    for when the token expires. (A Unix timestamp is a numeric
    value representing the number of seconds from
    1970-01-01T00:00:00Z UTC until the specified UTC date/time,
    ignoring leap seconds.) The token is validated when the
    participant joins a stage. IVS provides tokens with a
    default 12-hour TTL, which we recommend; this can be
    extended to a maximum of 14 days from the issued at time
    (iat). This must be an integer type value.
  - `iat` (issued at time) is a Unix UTC timestamp
    for when the JWT was issued. (See the note for
    `exp` about Unix timestamps.) It must be an
    integer type value.
  - `jti` (JWT ID) is the participant ID used for
    tracking and referring to the participant to whom the token
    is granted. Every token must have a unique participant ID.
    It must be a case-sensitive string, up to 64 characters
    long, containing only alphanumeric, hyphen (-), and
    underscore (\_) characters. No other special characters are
    allowed.

- `user_id` is an optional, customer-assigned name to
  help identify the token; this can be used to link a participant to a
  user in the customer’s own systems. This should match the
  `userId` field in the [CreateParticipantToken](../RealTimeAPIReference/API_CreateParticipantToken.md "../RealTimeAPIReference/API_CreateParticipantToken.md") API request. It can be any UTF-8
  encoded text and is a string of up to 128 characters. _This field is exposed to all stage participants
  and should not be used for personally identifying, confidential,
  or sensitive information._
- `resource` is the ARN of the stage; e.g.,
  `arn:aws:ivs:us-east-1:123456789012:stage/oRmLNwuCeMlQ`.
- `topic` is the ID of the stage, which can be extracted
  from stage ARN. For example, if the stage ARN is
  `arn:aws:ivs:us-east-1:123456789012:stage/oRmLNwuCeMlQ`,
  the stage ID is `oRmLNwuCeMlQ`.
- `events_url` must be the events endpoint returned from
  the CreateStage or GetStage operation. We recommend that you cache
  this value at stage-creation time; the value can be cached for up to
  14 days. An example value is
  `wss://global.events.live-video.net`.
- `whip_url` must be the WHIP endpoint returned from the
  CreateStage or GetStage operation. We recommend that you cache this
  value at stage-creation time; the value can be cached for up to 14
  days. An example value is
  `https://453fdfd2ad24df.global-bm.whip.live-video.net`.
- `capabilities` specifies the capabilities of the token;
  valid values are `allow_publish` and
  `allow_subscribe`. For subscribe-only tokens, set
  only `allow_subscribe` to `true`.
- `attributes` is an optional field where you can specify
  application-provided attributes to encode into the token and attach
  to a stage. Map keys and values can contain UTF-8 encoded text. The
  maximum length of this field is 1 KB total. _This field is
  exposed to all stage participants and should not be used for
  personally identifying, confidential, or sensitive
  information._
- `version` must be `1.0`.

```
{
  "exp": 1697322063,
  "iat": 1697149263,
  "jti": "Mx6clRRHODPy",
  "user_id": "<optional_customer_assigned_name>",
  "resource": "<stage_arn>",
  "topic": "<stage_id>",
  "events_url": "wss://global.events.live-video.net",
  "whip_url": "https://114ddfabadaf.global-bm.whip.live-video.net",
  "capabilities": {
    "allow_publish": true,
    "allow_subscribe": true
  },
  "attributes": {
    "optional_field_1": "abcd1234",
    "optional_field_2": "false"
  },
  "version": "1.0"
}

```

#### Token Schema: Signature

To create the signature, use the private key with the algorithm specified
in the header (ES384) to sign the encoded header and encoded payload.

```
ECDSASHA384(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  <private-key>
)
```

#### Instructions

1. Generate the token’s signature with an ES384 signing algorithm and
   a private key that is associated with the public key provided to
   IVS.
2. Assemble the token.

```
base64UrlEncode(header) + "." +
base64UrlEncode(payload) + "." +
base64UrlEncode(signature)

```

## Creating Tokens with the IVS

Real-Time Streaming API

![Distribute participant tokens: Stage token workflow](images/Distribute_Participant_Tokens.png)

As shown above, a client application asks your server application for a token, and
the server application calls CreateParticipantToken using an AWS SDK or SigV4
signed request. Since AWS credentials are used to call the API, the token should
be generated in a secure server-side application, not the client-side
application.

When creating a participant token, you can optionally specify attributes and/or
capabilities:

- You can specify application-provided attributes to encode into the token
  and attach to a stage. Map keys and values can contain UTF-8 encoded text.
  The maximum length of this field is 1 KB total. _This field is
  exposed to all stage participants and should not be used for personally
  identifying, confidential, or sensitive information._
- You can specify capabilities enabled by the token. The default is
  `PUBLISH` and `SUBSCRIBE`, which allows the
  participant to send and receive audio and video, but you could issue tokens
  with a subset of capabilities. For example, you could issue a token with
  only the `SUBSCRIBE` capability for moderators. In that case, the
  moderators could see the participants that are sending video but not send
  their own video.

For details, see [CreateParticipantToken](../RealTimeAPIReference/API_CreateParticipantToken.md "../RealTimeAPIReference/API_CreateParticipantToken.md").

You can create participant tokens via the console or CLI for testing and
development, but most likely you will want to create them with the AWS SDK in your
production environment.

You will need a way to distribute tokens from your server to each client (e.g.,
via an API request). We do not provide this functionality. For this guide, you can
simply copy and paste the tokens into client code in the following steps.

**Important**: Treat tokens as opaque; i.e., do not
build functionality based on token contents. The format of tokens could change in
the future.

### Console

Instructions

1. Navigate to the stage you created in the prior step.
2. Select **Create token**. The **Create token** window appears.
3. Enter a user ID to be associated with the token. This can be any UTF-8
   encoded text.
4. Select **Create**.
5. Copy the token. _Important: Be sure to save the
   token; IVS does not store it and you cannot retrieve it
   later_.

### CLI Instructions

Creating a token with the AWS CLI requires that you first download and
configure the CLI on your machine. For details, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md"). Note that generating tokens
with the AWS CLI is good for testing purposes, but for production use, we
recommend that you generate tokens on the server side with the AWS SDK (see
instructions below).

1. Run the `create-participant-token` command with the stage
   ARN. Include any or all of the following capabilities:
   `"PUBLISH"`, `"SUBSCRIBE"`.

```
aws ivs-realtime create-participant-token --stage-arn arn:aws:ivs:us-west-2:376666121854:stage/VSWjvX5XOkU3 --capabilities '["PUBLISH", "SUBSCRIBE"]'
```

2. This returns a participant token:

```
{
    "participantToken": {
        "capabilities": [
            "PUBLISH",
            "SUBSCRIBE"
        ],
        "expirationTime": "2023-06-03T07:04:31+00:00",
        "participantId": "tU06DT5jCJeb",
        "token": "eyJhbGciOiJLTVMiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2NjE1NDE0MjAsImp0aSI6ImpGcFdtdmVFTm9sUyIsInJlc291cmNlIjoiYXJuOmF3czppdnM6dXMtd2VzdC0yOjM3NjY2NjEyMTg1NDpzdGFnZS9NbzhPUWJ0RGpSIiwiZXZlbnRzX3VybCI6IndzczovL3VzLXdlc3QtMi5ldmVudHMubGl2ZS12aWRlby5uZXQiLCJ3aGlwX3VybCI6Imh0dHBzOi8vNjZmNzY1YWM4Mzc3Lmdsb2JhbC53aGlwLmxpdmUtdmlkZW8ubmV0IiwiY2FwYWJpbGl0aWVzIjp7ImFsbG93X3B1Ymxpc2giOnRydWUsImFsbG93X3N1YnNjcmliZSI6dHJ1ZX19.MGQCMGm9affqE3B2MAb_DSpEm0XEv25hfNNhYn5Um4U37FTpmdc3QzQKTKGF90swHqVrDgIwcHHHIDY3c9eanHyQmcKskR1hobD0Q9QK_GQETMQS54S-TaKjllW9Qac6c5xBrdAk"
    }
}
```

3. Save this token. You will need this to join the stage and send and
   receive video.

### AWS SDK

Instructions

You can use the AWS SDK to create tokens. Below are instructions for the
AWS SDK using JavaScript.

**Important:** This code must be executed on the
server side and its output passed to the client.

**Prerequisite:** To use the code sample below,
you need to install the aws-sdk/client-ivs-realtime package. For details, see
[Getting started with the AWS SDK for JavaScript](../../../sdk-for-javascript/v3/developer-guide/getting-started.md "../../../sdk-for-javascript/v3/developer-guide/getting-started.md").

```
import { IVSRealTimeClient, CreateParticipantTokenCommand } from "@aws-sdk/client-ivs-realtime";

const ivsRealtimeClient = new IVSRealTimeClient({ region: 'us-west-2' });
const stageArn = 'arn:aws:ivs:us-west-2:123456789012:stage/L210UYabcdef';
const createStageTokenRequest = new CreateParticipantTokenCommand({
  stageArn,
});
const response = await ivsRealtimeClient.send(createStageTokenRequest);
console.log('token', response.participantToken.token);
```

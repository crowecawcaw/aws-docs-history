

# Step 3: Distribute Tokens
<a name="getting-started-distribute-tokens"></a>

Now that you have a stage, create and distribute the tokens that clients use to join it. Each client needs a participant token to join a stage and send or receive video. Applications that use a `RealTimeConnection` also need a connection token.

A participant token authorizes a participant to join one specific stage and defines that participant's publish and subscribe capabilities. A connection token authorizes a shared network connection that a client can reuse while moving between stages in the same AWS account and Region. A connection token does not replace a participant token. The client needs a participant token for every stage that it joins.

There are two approaches to generating tokens:
+ [Create tokens with a key pair](#getting-started-distribute-tokens-self-signed).
+ [Create tokens with the IVS real-time-streaming API](#getting-started-distribute-tokens-api).

Both of these approaches are described below.

## Creating Tokens with a Key Pair
<a name="getting-started-distribute-tokens-self-signed"></a>

You can create participant tokens and connection tokens on your server application by signing JWTs with an ECDSA public/private key pair. Import the public key into IVS so IVS can verify the JWT signature when a client connects.

**Important**  
IVS does not offer key expiry. If your private key is compromised, you must delete the old public key.

### Create a New Key Pair
<a name="getting-started-distribute-tokens-self-signed-create-key-pair"></a>

There are various ways to create a key pair. Below, we give two examples.

To create a new key pair in the console, follow these steps:

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs). Choose your stage's region if you are not already on it.

1. In the left navigation menu, choose **Real-time streaming > Public keys**.

1. Choose **Create public key**. A **Create public key** dialog appears.

1. Follow the prompts and choose **Create**.

1. Amazon IVS generates a new key pair. The public key is imported as a public key resource and the private key is immediately made available for download. The public key can also be downloaded later if necessary.

   Amazon IVS generates the key on the client side and does not store the private key. ***Be sure you save the key; you cannot retrieve it later.***

To create a new P384 EC key pair with OpenSSL (you might have to install [OpenSSL](https://www.openssl.org/source/) first), follow these steps. This process enables you to access both the private and public keys. You need the public key only if you want to test verification of your tokens.

```
openssl ecparam -name secp384r1 -genkey -noout -out priv.pem
openssl ec -in priv.pem -pubout -out public.pem
```

Now import your new public key, using the instructions below.

### Import the Public Key
<a name="getting-started-distribute-tokens-import-public-key"></a>

Once you have a key pair, you can import the public key into IVS. The private key is not needed by our system but is employed by you to sign tokens.

To import an existing public key with the console:

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs). Choose your stage's region if you are not already on it.

1. In the left navigation menu, choose **Real-time streaming > Public keys**.

1. Choose **Import**. An **Import public key** dialog appears.

1. Follow the prompts and choose **Import**.

1. Amazon IVS imports your public key and generates a public key resource.

To import an existing public key with the CLI:

```
aws ivs-realtime import-public-key --public-key-material "`cat public.pem`" --region <aws-region>
```

You can omit `--region <aws-region>` if the region is in your local AWS configuration file.

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

### API Request
<a name="getting-started-distribute-tokens-create-api"></a>

```
POST /ImportPublicKey HTTP/1.1
{
  "publicKeyMaterial": "<pem file contents>"
}
```

## Participant Tokens
<a name="getting-started-distribute-tokens-participant-tokens"></a>

A participant token authorizes one participant to join one stage. It contains the stage ARN and ID, endpoints, optional participant attributes, and publish and subscribe capabilities.

### Create Participant Tokens with a Key Pair
<a name="getting-started-distribute-tokens-self-signed-generate-sign"></a>

For details on working with JWTs and the supported libraries for signing tokens, visit [jwt.io](https://jwt.io/). On the jwt.io interface, you must enter your private key to sign tokens. The public key is needed only if you want to verify tokens.

All JWTs have three fields: header, payload, and signature.

The JSON schemas for the JWT's header and payload are described below. Alternatively you can copy a sample JSON from the IVS console. To get the header and payload JSON from the IVS console:

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs). Choose your stage's region if you are not already on it.

1. In the left navigation menu, choose **Real-time streaming > Stages**.

1. Select the stage you want to use. Select **View details**.

1. In the **Participant tokens** section, select the drop-down next to **Create token**.

1. Select **Build token header and payload**.

1. Fill in the form and copy the JWT header and payload shown at the bottom of the popup.

#### Token Schema: Header
<a name="getting-started-distribute-tokens-self-signed-generate-sign-header"></a>

The header specifies:
+ `alg` is the signing algorithm. This is ES384, an ECDSA signature algorithm that uses the SHA-384 hash algorithm.
+ `typ` is the token type, JWT.
+ `kid` is the ARN of the public key used to sign the token. It must be the same ARN returned from the [GetPublicKey](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetPublicKey.html) API request.

```
{
  "alg": "ES384",
  "typ": "JWT"
  "kid": "arn:aws:ivs:123456789012:us-east-1:public-key/abcdefg12345"
}
```

#### Token Schema: Payload
<a name="getting-started-distribute-tokens-self-signed-generate-sign-payload"></a>

The payload contains data specific to IVS. All fields except `user_id` are mandatory.
+ `RegisteredClaims` in the JWT specification are reserved claims that need to be provided for stage token to be valid:
  + `exp` (expiration time) is a Unix UTC timestamp for when the token expires. (A Unix timestamp is a numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.) The token is validated when the participant joins a stage. IVS provides tokens with a default 12-hour TTL, which we recommend; this can be extended to a maximum of 14 days from the issued at time (iat). This must be an integer type value.
  + `iat` (issued at time) is a Unix UTC timestamp for when the JWT was issued. (See the note for `exp` about Unix timestamps.) It must be an integer type value.
  + `jti` (JWT ID) is the participant ID used for tracking and referring to the participant to whom the token is granted. Every token must have a unique participant ID. It must be a case-sensitive string, up to 64 characters long, containing only alphanumeric, hyphen (-), and underscore (\_) characters. No other special characters are allowed.
+ `user_id` is an optional, customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer's own systems. This should match the `userId` field in the [CreateParticipantToken](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateParticipantToken.html) API request. It can be any UTF-8 encoded text and is a string of up to 128 characters. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
+ `resource` is the ARN of the stage; for example, `arn:aws:ivs:us-east-1:123456789012:stage/oRmLNwuCeMlQ`.
+ `topic` is the ID of the stage, which can be extracted from stage ARN. For example, if the stage ARN is `arn:aws:ivs:us-east-1:123456789012:stage/oRmLNwuCeMlQ`, the stage ID is `oRmLNwuCeMlQ`.
+ `events_url` must be the events endpoint returned from the CreateStage or GetStage operation. We recommend that you cache this value at stage-creation time; the value can be cached for up to 14 days. An example value is `wss://global.events.live-video.net`.
+ `whip_url` must be the WHIP endpoint returned from the CreateStage or GetStage operation. We recommend that you cache this value at stage-creation time; the value can be cached for up to 14 days. An example value is `https://453fdfd2ad24df.global-bm.whip.live-video.net`.
+ `capabilities` specifies the capabilities of the token; valid values are `allow_publish` and `allow_subscribe`. For subscribe-only tokens, set only `allow_subscribe` to `true`.
+ `attributes` is an optional field where you can specify application-provided attributes to encode into the token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
+ `version` must be `1.0`.

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
<a name="getting-started-distribute-tokens-self-signed-generate-sign-signature"></a>

To create the signature, use the private key with the algorithm specified in the header (ES384) to sign the encoded header and encoded payload.

```
ECDSASHA384(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  <private-key>
)
```

#### Instructions
<a name="getting-started-distribute-tokens-self-signed-generate-sign-instructions"></a>

1. Generate the token's signature with an ES384 signing algorithm and a private key that is associated with the public key provided to IVS.

1. Assemble the token.

   ```
   base64UrlEncode(header) + "." +
   base64UrlEncode(payload) + "." +
   base64UrlEncode(signature)
   ```

## Creating Tokens with the IVS Real-Time Streaming API
<a name="getting-started-distribute-tokens-api"></a>

![Distribute participant tokens: Stage token workflow](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/Distribute_Participant_Tokens.png)


As shown above, a client application asks your server application for a token, and the server application calls `CreateParticipantToken` using an AWS SDK or SigV4 signed request. Since AWS credentials are used to call the API, the token should be generated in a secure server-side application, not the client-side application.

When creating a participant token, you can optionally specify attributes and/or capabilities:
+ You can specify application-provided attributes to encode into the token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.*
+ You can specify capabilities enabled by the token. The default is `PUBLISH` and `SUBSCRIBE`, which allows the participant to send and receive audio and video, but you could issue tokens with a subset of capabilities. For example, you could issue a token with only the `SUBSCRIBE` capability for moderators. In that case, the moderators could see the participants that are sending video but not send their own video.

For details, see [CreateParticipantToken](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateParticipantToken.html).

You can create participant tokens through the console or CLI for testing and development, but most likely you will want to create them with the AWS SDK in your production environment.

You will need a way to distribute tokens from your server to each client (for example, through an API request). We do not provide this functionality. For this guide, you can simply copy and paste the tokens into client code in the following steps.

**Important**: Treat tokens as opaque; do not build functionality based on token contents. The format of tokens could change in the future.

### Console Instructions
<a name="getting-started-distribute-tokens-console"></a>

1. Navigate to the stage you created in the prior step.

1. Select **Create token**. The **Create token** window appears.

1. Enter a user ID to be associated with the token. This can be any UTF-8 encoded text.

1. Select **Create**.

1. Copy the token. *Important: Be sure to save the token; IVS does not store it and you cannot retrieve it later.*

### CLI Instructions
<a name="getting-started-distribute-tokens-cli"></a>

Creating a token with the AWS CLI requires that you first download and configure the CLI on your machine. For details, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html). Note that generating tokens with the AWS CLI is good for testing purposes, but for production use, we recommend that you generate tokens on the server side with the AWS SDK (see instructions below).

1. Run the `create-participant-token` command with the stage ARN. Include any or all of the following capabilities: `"PUBLISH"`, `"SUBSCRIBE"`.

   ```
   aws ivs-realtime create-participant-token --stage-arn arn:aws:ivs:us-west-2:123456789012:stage/VSWjvX5XOkU3 --capabilities '["PUBLISH", "SUBSCRIBE"]'
   ```

1. This returns a participant token:

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

1. Save this token. You will need it to join the stage and send and receive video.

### AWS SDK Instructions
<a name="getting-started-distribute-tokens-sdk"></a>

You can use the AWS SDK to create tokens. Below are instructions for the AWS SDK using JavaScript.

**Important:** This code must be executed on the server side and its output passed to the client.

**Prerequisite:** To use the code sample below, you need to install the aws-sdk/client-ivs-realtime package. For details, see [Getting started with the AWS SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started.html).

```
import { IVSRealTimeClient, CreateParticipantTokenCommand } from "@aws-sdk/client-ivs-realtime";

const ivsRealtimeClient = new IVSRealTimeClient({ region: 'us-west-2' });
const stageArn = 'arn:aws:ivs:us-west-2:123456789012:stage/VSWjvX5XOkU3';
const createStageTokenRequest = new CreateParticipantTokenCommand({
  stageArn,
});
const response = await ivsRealtimeClient.send(createStageTokenRequest);
console.log('token', response.participantToken.token);
```

## Connection Tokens
<a name="getting-started-distribute-tokens-connection-tokens"></a>

A connection token is a self-signed JWT that authorizes a shared network connection. A client can reuse this connection while moving between stages in the same AWS account and Region, until the token expires.

Create and sign connection tokens on your server with the key pair created earlier. Send the connection token to the client before it begins a workflow that moves between stages. The client creates one `RealTimeConnection` and supplies it whenever it creates a stage. The client then uses the appropriate participant token for each stage that it joins.

### Token Header
<a name="getting-started-distribute-tokens-connection-tokens-header"></a>

Use the token header described in [Create Participant Tokens with a Key Pair](#getting-started-distribute-tokens-self-signed-generate-sign).

### Token Payload
<a name="getting-started-distribute-tokens-connection-tokens-payload"></a>

```
{
    "exp": 1697322063,
    "iat": 1697149263,
    "jti": "Mx6clRRHODPy",
    "account_id": "123456789012",
    "region": "us-west-2",
    "events_url": "wss://global.events.live-video.net",
    "version": "1.0"
}
```

The payload contains data specific to IVS. All fields are mandatory:
+ `RegisteredClaims` in the JWT specification are reserved claims that must be present for the token to be valid:
  + `exp` (expiration time) is a Unix UTC timestamp for when the token expires. A token can expire up to four weeks after its creation time.
  + `iat` (issued-at time) is a Unix UTC timestamp for when the JWT was issued.
  + `jti` (JWT ID) is a unique token ID. Generate a new, case-sensitive ID for every Connection token. The ID can contain up to 64 alphanumeric characters, hyphens (-), and underscores (\_).
+ `account_id` is the AWS account ID that owns the stages.
+ `region` is the home Region of the IVS public key used to sign the token.
+ `events_url` must be `wss://global.events.live-video.net`.
+ `version` must be `1.0`.

A connection token does not contain a stage ARN, stage ID, WHIP endpoint, participant capabilities, participant attributes, or user ID. Those values belong in the participant token for the stage that the client joins.

Sign the token as described in [Create Participant Tokens with a Key Pair](#getting-started-distribute-tokens-self-signed-generate-sign), using the connection token header and payload above.
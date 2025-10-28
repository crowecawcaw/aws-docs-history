# Create or Import an IVS Playback Key

Amazon IVS allows a maximum of three key pairs that can be used to sign and verify
playback tokens. Amazon IVS does not offer any key rotations.

**_Once imported, playback keys cannot be
updated._** Instead, you must delete the existing playback
key and import a new key.

You need to generate an [ECDSA
public/private key pair](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm "https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm") to sign the JWTs and upload the public key to Amazon
IVS as a playback-key resource. Then Amazon IVS can verify the signature in playback
requests.

## Creating a New Key Pair

There are various ways to create a key pair; below, we give two examples.

### Console Instructions

To create a new key pair in the console, follow these steps. Note this process
enables you to download only the private key.

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs").
   Choose your channel’s region if you are not already on it.
2. In the left navigation menu, choose **Playback
   security > Playback keys**.
3. Choose **Create playback key**. A **Create playback key** dialog appears.
4. Enter a name for the playback key and choose **Create**.
5. Amazon IVS generates a new key pair. The public key of this pair is saved
   to your AWS account and will be used to verify any playback requests that contain
   a token signed with the private key.

The private key is immediately downloaded to your machine and is not saved
in the console or available for future download.
**_Be sure you save
the private key; you cannot retrieve it later._**

### OpenSSL Instructions

**Note:** You may have to install [OpenSSL](https://www.openssl.org/source/ "https://www.openssl.org/source/") before following these instructions.

To create a new P384 EC key pair with OpenSSL, follow these
steps. This process enables you to access both the private and public keys. You need
the public key only if you want to test verification of your tokens.

```
openssl ecparam -name secp384r1 -genkey -noout -out priv.pem
openssl ec -in priv.pem -pubout -out public.pem
```

Now import your new public key, using the instructions below.

## Importing an Existing Public

Key

If you already have a key pair, you can import the public key into IVS. The
private key is not needed by our system but is employed by you to sign
tokens.

### Console Instructions

To import an existing public key with the console:

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs").
   Choose your channel’s region if you are not already on it.
2. In the left navigation menu, choose **Playback
   security > Playback keys**.
3. Choose **Import**. An **Import playback key** dialog appears.
4. Give the imported key a name, and browse for the public key file
   (or paste the public key file contents), then choose
   **Import**.
5. Amazon IVS imports your public key and generates a playback key
   resource.

### CLI Instructions

To import an existing public key with the CLI:

```
aws ivs import-playback-key-pair --public-key-material "`cat public.pem`" --region <aws-region>
```

You can omit `--region <aws-region>` if the region is in your local
AWS configuration file.

Here is an example response:

```
{
   "keyPair": {
      "arn": "arn:aws:ivs:us-west-2:693991300569:playback-key/f99cde61-c2b0-4df3-8941-ca7d38acca1a",
      "fingerprint": "98:0d:1a:a0:19:96:1e:ea:0a:0a:2c:9a:42:19:2b:e7",
      "tags": {}
   }
}
```

### API Request

For usage information, see [ImportPlaybackKeyPair](../LowLatencyAPIReference/API_ImportPlaybackKeyPair.md "../LowLatencyAPIReference/API_ImportPlaybackKeyPair.md")
in the _IVS Low-Latency Streaming API Reference_.

```
POST /ImportPlaybackKeyPair HTTP/1.1
	{
	  "publicKeyMaterial": "<pem file contents>"
	}
```

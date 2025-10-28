# Verifying the

signature of an Amazon SNS message when using HTTP query-based requests

Verifying the signature of an Amazon SNS message when using HTTP query-based requests ensures
the message's authenticity and integrity. This process confirms that the message originates
from Amazon SNS and has not been tampered with during transit. By parsing the message,
constructing the correct string to sign, and validating the signature against a trusted
public key, you safeguard your system against spoofing and unauthorized message
alterations.

1.  Extract **key-value pairs** from the JSON document in the
    HTTP POST request body sent by Amazon SNS. These fields are required to construct the **string to sign**.

        * `Message`
        * `Subject` (if present)
        * `MessageId`
        * `Timestamp`
        * `TopicArn`
        * `Type`

    For example:

```
MESSAGE_FILE="message.json"
FIELDS=("Message" "MessageId" "Subject" "Timestamp" "TopicArn" "Type")
```

###### Note

If any field contains escaped characters (for example, `\n`), convert
them to their **original form** to ensure an exact
match. 2. Locate the `SigningCertURL` field in the Amazon SNS message. This certificate
contains the public key needed to verify the message signature. For example:

```
SIGNING_CERT_URL=$(jq -r '.SigningCertURL' "$MESSAGE_FILE")
```

3. Ensure the `SigningCertURL` is from a trusted AWS domain (for example,
   https://sns.us-east-1.amazonaws.com). Reject any URLs **outside AWS domains** for security reasons.
4. Download the **X.509 certificate** from the provided URL.
   For example:

```
curl -s "$SIGNING_CERT_URL" -o signing_cert.pem
```

5. Extract the **public key** from the downloaded X.509
   certificate. The public key allows you to decrypt the message's signature and verify its
   integrity. For example:

```
openssl x509 -pubkey -noout -in signing_cert.pem > public_key.pem
```

6. Different message types require different key-value pairs in the string to sign.
   Identify the **message type** (`Type` field in the
   Amazon SNS message) to determine which **key-value pairs** to
   include:
   - **Notification message** – Includes
     `Message`, `MessageId`, `Subject` (if present),
     `Timestamp`, `TopicArn`, and `Type`.
   - **SubscriptionConfirmation** or **UnsubscribeConfirmation message** – Includes `Message`,
     `MessageId`, `SubscribeURL`, `Timestamp`,
     `Token`, `TopicArn`, and `Type`.

7. Amazon SNS requires the string to sign to follow a strict, fixed field order for
   verification. **Only the explicitly required fields must be
   included**—no extra fields can be added. Optional fields, such as
   `Subject`, must be included only if present in the message and must appear in
   the exact position defined by the required field order. For example:

```
KeyNameOne\nValueOne\nKeyNameTwo\nValueTwo
```

###### Important

Do not add a newline character at the end of the string. 8. Arrange the **key-value pairs** in byte-sort order
(alphabetical by key name). 9. Construct the **string to sign** using the following
format example:

```
STRING_TO_SIGN=""
for FIELD in "${FIELDS[@]}"; do
    VALUE=$(jq -r --arg field "$FIELD" '.[$field]' "$MESSAGE_FILE")
    STRING_TO_SIGN+="$FIELD\n$VALUE"
    # Append a newline after each field except the last one
    if [[ "$FIELD" != "Type" ]]; then
        STRING_TO_SIGN+="\n"
    fi
done
```

**Notification message example:**

```
Message
My Test Message
MessageId
4d4dc071-ddbf-465d-bba8-08f81c89da64
Subject
My subject
Timestamp
2019-01-31T04:37:04.321Z
TopicArn
arn:aws:sns:us-east-2:123456789012:s4-MySNSTopic-1G1WEFCOXTC0P
Type
Notification
```

**SubscriptionConfirmation example:**

```
Message
Please confirm your subscription
MessageId
3d891288-136d-417f-bc05-901c108273ee
SubscribeURL
https://sns.us-east-2.amazonaws.com/...
Timestamp
2024-01-01T00:00:00.000Z
Token
abc123...
TopicArn
arn:aws:sns:us-east-2:123456789012:MyTopic
Type
SubscriptionConfirmation
```

10. The `Signature` field in the message is Base64-encoded. You need to
    **decode** it to compare its **raw
    binary form** with the **derived hash**. For
    example:

```
SIGNATURE=$(jq -r '.Signature' "$MESSAGE_FILE")
echo "$SIGNATURE" | base64 -d > signature.bin
```

11. Use the `SignatureVersion` field to select the hash algorithm:
    - For `SignatureVersion`**1**, use **SHA1** (for example, `-sha1`).
    - For `SignatureVersion`**2**, use **SHA256** (for example, `-sha256`).

12. To confirm the authenticity of the Amazon SNS message, generate a **hash** of the constructed string and verify the signature using the **public key**.

```
openssl dgst -sha256 -verify public_key.pem -signature signature.bin <<< "$STRING_TO_SIGN"
```

If the signature is valid, the output is `Verified OK`. Otherwise, the
output is `Verification Failure`.

## Example script with error

handling

The following example script automates the verification process:

```
#!/bin/bash

# Path to the local message file
MESSAGE_FILE="message.json"

# Extract the SigningCertURL and Signature from the message
SIGNING_CERT_URL=$(jq -r '.SigningCertURL' "$MESSAGE_FILE")
SIGNATURE=$(jq -r '.Signature' "$MESSAGE_FILE")

# Fetch the X.509 certificate
curl -s "$SIGNING_CERT_URL" -o signing_cert.pem

# Extract the public key from the certificate
openssl x509 -pubkey -noout -in signing_cert.pem > public_key.pem

# Define the fields to include in the string to sign
FIELDS=("Message" "MessageId" "Subject" "Timestamp" "TopicArn" "Type")

# Initialize the string to sign
STRING_TO_SIGN=""

# Iterate over the fields to construct the string to sign
for FIELD in "${FIELDS[@]}"; do
    VALUE=$(jq -r --arg field "$FIELD" '.[$field]' "$MESSAGE_FILE")
    STRING_TO_SIGN+="$FIELD\n$VALUE"
    # Append a newline after each field except the last one
    if [[ "$FIELD" != "Type" ]]; then
        STRING_TO_SIGN+="\n"
    fi
done

# Verify the signature
echo -e "$STRING_TO_SIGN" | openssl dgst -sha256 -verify public_key.pem -signature <(echo "$SIGNATURE" | base64 -d)
```

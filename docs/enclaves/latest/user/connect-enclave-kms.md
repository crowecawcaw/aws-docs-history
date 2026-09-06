

# Getting started: Connect an enclave with AWS KMS for cryptographic attestation and secrets management
<a name="connect-enclave-kms"></a>

Use this pattern to access secrets only from inside a validated enclave.

You build an enclave from an enclave image file (EIF) that you generate from a Docker image. The EIF contains unencrypted copies of all code and data, so unencrypted secrets must not be part of the EIF. To make secret data accessible only from inside an enclave, use AWS KMS. AWS KMS can grant permission for decrypt operations exclusively to enclaves launched from a particular EIF. For more information, see [Using cryptographic attestation with AWS KMS](https://docs.aws.amazon.com/enclaves/latest/user/kms.html) and [Cryptographic attestation](set-up-attestation.md).

To authenticate the enclave to AWS KMS, provide an attestation document as part of your AWS KMS operation request. This attestation document contains cryptographic hashes (PCR values) of the enclave state, including PCR0, which is a hash over the entire EIF. AWS root of trust signs the document. This signature gives AWS KMS assurance that the request originates from an AWS Nitro confidential compute environment.

An enclave does not have network access. It communicates only with its parent instance over vsock. To access AWS KMS from within the enclave, use the `vsock-proxy` and `kmstool-enclave-cli` tools provided by AWS.

**Topics**
+ [Communication overview](#kms-schematics)
+ [Integrate this pattern in your own application](#kms-integration-pattern)
+ [Example: Decrypt a secret with AWS tooling](#kms-example)

## Communication overview
<a name="kms-schematics"></a>

The following diagram shows how an enclave uses AWS KMS and cryptographic attestation to decrypt a secret.

![An incoming HTTPS request flows from the parent instance into the enclave over vsock. The enclave calls kmstool-enclave-cli, which obtains an attestation document from the Nitro Secure Module and sends a decrypt request to AWS KMS through the vsock proxy on the parent instance.](http://docs.aws.amazon.com/enclaves/latest/user/images/enclave-kms-attestation.png)


*Figure 2: Decrypt with AWS KMS and cryptographic attestation*

The preceding diagram shows how your application interacts with AWS KMS through a prepackaged CLI tool named `kmstool-enclave-cli`.

1. The parent instance passes credentials and ciphertext into the enclave over virtio-vsock. For more information, see [Getting started: Using the virtio-vsock](enclave-networking.md).

1. Your application invokes the `kmstool-enclave-cli` binary through a system call.

1. The CLI utility generates an ephemeral private/public key pair.

1. The CLI utility requests an attestation document from the Nitro Secure Module (NSM) device and includes the public key.

1. The CLI creates a AWS KMS decrypt request by using a standard AWS SDK and attaches the attestation document from the previous step. The SDK dials out to an HTTPS AWS KMS endpoint over vsock.

1. The `vsock-proxy` process on the parent instance listens on CID `3`, port `8000`. It accepts the connection and transparently forwards the packets to the configured AWS KMS endpoint. A secure, bidirectional TLS connection is established between the AWS KMS endpoint and the enclave.

1. AWS KMS receives the decrypt request, validates the attestation document, and decrypts the payload. If the attestation document contains a public key, AWS KMS uses this key to re-encrypt the plaintext so that only the owner of the matching private key can read the sensitive information.

1. The CLI receives the AWS KMS response and decrypts the payload with the ephemeral private key from step 3.

1. The connection closes.

## Integrate this pattern in your own application
<a name="kms-integration-pattern"></a>

**Inside the enclave**  
Inside the enclave, complete the following steps.

1. Receive AWS credentials from the parent instance. You need these credentials to authenticate to AWS KMS. Pass them as part of your own data channel. For more information, see [Getting started: Using the virtio-vsock](enclave-networking.md).

1. Generate a local ephemeral private/public key pair for plaintext encryption of decrypt responses.

1. Obtain an attestation document from the Nitro Secure Module (NSM) device and include the ephemeral public key.

1. All AWS SDKs natively support attestation documents through the `Recipient` field. For more information, see [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) in the *AWS Key Management Service Developer Guide*.

**Inside the parent instance**  
Inside the parent instance, complete the following steps.

1. Provide a mechanism to get fresh AWS credentials from IMDSv2 and pass them into the enclave with the ciphertext.

1. Use the default `vsock-proxy` service provided by AWS to connect to AWS KMS. Add the specific AWS KMS endpoint to the allow list.

## Example: Decrypt a secret with AWS tooling
<a name="kms-example"></a>

The following example walks you through setting up a vsock-based communication channel between the enclave and the parent instance, and decrypting a secret from inside the enclave by using a CLI tool provided by AWS named `kmstool-enclave-cli`.

**Note**  
Use the same Region consistently throughout this example. The Region that you specify when you encrypt the secret (Step 1), the AWS KMS endpoints in the `vsock-proxy` allow list (Step 2), and the Region that you pass to `kmstool-enclave-cli` (Step 3) must all match. This example uses `us-east-1`.

**Topics**
+ [Prerequisites](#kms-example-prerequisites)
+ [Step 1: Create a AWS KMS key and encrypt a secret](#kms-example-step1)
+ [Step 2: Prepare the parent instance](#kms-example-step2)
+ [Step 3: Run inside the enclave](#kms-example-step3)
+ [Step 4: Provide the ciphertext by using curl](#kms-example-step4)

### Prerequisites
<a name="kms-example-prerequisites"></a>

**Important**  
This example builds on the [Getting started: Using the virtio-vsock](enclave-networking.md) example, and it reuses the scripts created in that example. Complete that example before you begin.

Ensure that you have the following before you begin.
+ The `vsock-proxy` systemd service on the parent instance, which is required to communicate with the AWS KMS endpoint.
+ The [kmstool-enclave-cli](https://github.com/aws/aws-nitro-enclaves-sdk-c/tree/main/bin/kmstool-enclave-cli) binary on GitHub, or a similar binary, inside the enclave.

### Step 1: Create a AWS KMS key and encrypt a secret
<a name="kms-example-step1"></a>

1. Create a symmetric AWS KMS key by following the steps in [Creating symmetric encryption AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-symmetric-cmk.html) in the *AWS Key Management Service Developer Guide*. Note the key ID. Use the following command templates to encode your secret and pass it to AWS KMS for encryption. Replace the key ID placeholder with your key ID.

   ```
   ciphertext=$( echo "Hello World" | base64 )
   aws kms encrypt --key-id "<alias/your-key-alias-or-key-id>" --plaintext ${ciphertext} --output text --query CiphertextBlob --region us-east-1
   ```

1. Run the `nitro-cli describe-enclaves` command to get the PCR0 value for the AWS KMS key resource policy.

   If you started the enclave in debug mode, use the following value for PCR0.

   ```
   000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
   ```

   Otherwise, use the PCR0 value from the output of the `nitro-cli describe-enclaves` command, for example:

   ```
   b078785234059e040259dd555d9008041240568772950f08602812b301e4b2b94c0ca68c50218564437d6d43b38f1de2
   ```

1. Update the following AWS KMS key policy template with the correct Amazon EC2 role ARN and `kms:RecipientAttestation:PCR0` value, and then follow the steps in [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-overview.html) in the *AWS Key Management Service Developer Guide* to set the policy.

   ```
   {
     "Sid" : "Enable enclave data processing",
     "Effect" : "Allow",
     "Principal" : {
       "AWS" : "<arn:aws:iam::111122223333:role/data-processing>"
     },
     "Action": [
       "kms:Decrypt"
     ],
     "Resource" : "*",
     "Condition": {
       "StringEqualsIgnoreCase": {
         "kms:RecipientAttestation:PCR0": "<EIF image sha384>"
       }
     }
   }
   ```

### Step 2: Prepare the parent instance
<a name="kms-example-step2"></a>

Use the `vsock-proxy` systemd service provided by AWS as a vsock-to-TCP outbound proxy. This proxy allows the enclave to dial out to AWS KMS. Before you start the systemd service on the parent instance, add the specific AWS KMS endpoints, including the Region, to the `vsock-proxy.yaml` allow list, as shown in the following example.

```
VSOCK_PROXY_YAML=/etc/nitro_enclaves/vsock-proxy.yaml
cat <<'EOF' > $VSOCK_PROXY_YAML
allowlist:
- {address: kms.us-east-1.amazonaws.com, port: 443}
- {address: kms-fips.us-east-1.amazonaws.com, port: 443}
EOF

systemctl enable --now nitro-enclaves-vsock-proxy.service
```

### Step 3: Run inside the enclave
<a name="kms-example-step3"></a>

1. Create a Dockerfile that includes the `kmstool_enclave_cli` binary and the libraries provided by AWS. For more information, see the [kmstool-enclave-cli](https://github.com/aws/aws-nitro-enclaves-sdk-c/tree/main/bin/kmstool-enclave-cli) documentation on GitHub.

   The CLI requires parameters such as the Region, AWS credentials, and the ciphertext. Transfer these into the enclave and export them as environment variables. For more information, see [Step 1: Prepare and run the enclave](enclave-networking.md#vsock-example-step1). By default, you don't need to specify the AWS KMS key ID because it is encoded in the ciphertext.

1. Update the `per_request.sh` file from [Step 1: Prepare and run the enclave](enclave-networking.md#vsock-example-step1) to invoke the `kmstool_enclave_cli` binary and return the standard output as the result.

   ```
   REGION=us-east-1
   /app/kmstool_enclave_cli decrypt \
     --region ${REGION} \
     --proxy-port 8000 \
     --aws-access-key-id ${AWS_ACCESS_KEY_ID} \
     --aws-secret-access-key ${AWS_SECRET_ACCESS_KEY} \
     --aws-session-token ${AWS_SESSION_TOKEN} \
     --ciphertext ${CIPHERTEXT}
   ```

1. Rebuild the enclave Dockerfile, convert the container to an enclave image file, and run the enclave as described in [Step 1: Prepare and run the enclave](enclave-networking.md#vsock-example-step1).

### Step 4: Provide the ciphertext by using curl
<a name="kms-example-step4"></a>

Use `curl` to post your ciphertext to the local HTTPS endpoint.

```
curl -k --header "Content-Type: application/json" \
  --request POST \
  --data '{"ciphertext":"MySecretCipherText"}' \
  https://localhost:8443 | jq '.'
```

The output is similar to the following.

```
{
  "enclaveResult": "\"Hello World\\n\""
}
```

The HTTPS server on the parent instance parsed the `curl` request. It augmented the payload with fresh AWS credentials from IMDSv2 and sent it into the enclave. Inside the enclave, the payload was passed to `kmstool-enclave-cli` through environment variables. `kmstool-enclave-cli` created an attestation document and dialed out to AWS KMS through the `vsock-proxy` that you configured. AWS KMS validated the attestation document and decrypted the payload. The decrypted result was returned to the enclave and used as the response to your `POST` request.
# Locally verify an image after signing

After you sign a container image using AWS Signer and Notation, you or an
authorized member of your team can verify the origin and integrity of the image by
cryptographic means.

Complete the following steps to verify that an image is valid with
Notation.

###### To verify an image

1. A trust store is required for verification. If you used the installer for
   the AWS Signer plugin and Notation, a trust store for both AWS commercial and AWS GovCloud (US) Regions was set up automatically
   and provisioned with a root certificate. For more information, see [Prerequisites for signing container
   images](image-signing-prerequisites.md "image-signing-prerequisites.md").
2. Set up a trust policy that includes the trust store for your partition.

The following example includes trust stores for both the AWS commercial and AWS GovCloud (US) Region. You can choose to include one or both in your trust policy depending on where you are verifying your signed images. To verify images signed in AWS commercial Regions, set `signingAuthority` to `aws-signer-ts`. To verify images signed in AWS GovCloud (US) Region, set `signingAuthority` to `aws-us-gov-signer-ts`.

###### Important

Signatures are isolated to AWS partitions. Calls to [GetRevocationStatus](../api/API_GetRevocationStatus.md "../api/API_GetRevocationStatus.md") with a cross-partition signature will return a validation exception error.

```
{
   "version":"1.0",
   "trustPolicies":[
      {
         "name":"aws-signer-tp",
         "registryScopes":[
            "*"
         ],
         "signatureVerification":{
            "level":"strict"
         },
         "trustStores":[
            "signingAuthority:aws-signer-ts",
            "signingAuthority:aws-us-gov-signer-ts"
         ],
         "trustedIdentities":[
            "arn:aws:signer:`Region`:`111122223333`:/signing-profiles/`ecr_signing_profile`",
            "arn:aws:signer:`Region`:`111122223333`:/signing-profiles/`ecr_signing_profile2`"
         ]
      }
   ]
}
```

3. Import the policy into Notation.

```
`$` **notation policy import `mypolicy.json`**
```

Output:

```
Existing trust policy configuration found, do you
want to overwrite it? [y/N] **y**

Trust policy configuration imported successfully.
```

4. Verify the signature, specifying the signature using the repository name
   and the SHA digest.

###### Note

You can specify the AWS Region and credentials profile that the Notation plugin uses
to interact with AWS Signer by assigning a value to the `AWS_PROFILE`
environment variable, or by passing the **--plugin-config
aws-profile=${`profile-name`}**
argument to the Notation **verify** command.

```
`$` **notation verify `111122223333`.dkr.ecr.region.amazonaws.com/`curl@SHA256_digest`**
```

Output:

```
Successfully verified signature for `111122223333`.dkr.ecr.us-west-2.amazonaws.com/`curl@SHA256_digest`
```

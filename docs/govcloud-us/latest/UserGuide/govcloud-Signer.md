# AWS Signer in AWS GovCloud (US)

AWS Signer is a fully managed code-signing service to ensure the trust and integrity of your code. Organizations validate code against a digital signature to confirm that the code is unaltered and from a trusted publisher. With AWS Signer, your security administrators have a single place to define your signing environment, including what AWS Identity and Access Management (IAM) role can sign code and in what Regions. AWS Signer manages the code-signing certificate’s public and private keys, and enables central management of the code-signing lifecycle. Integration with [AWS CloudTrail](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md") helps you track who is generating code signatures and to meet your compliance requirements.

## How AWS Signer differs for AWS GovCloud (US)

The following differences exist between AWS Signer in AWS GovCloud (US) and standard regions:

- AWS Signer only supports the container image signing feature (platform id: `Notation-OCI-SHA384-ECDSA`) and Lambda Zip signing feature (platform id: `AWSLambda-SHA384-ECDSA`) with AWS Signer APIs, the AWS CLI, and the console.
- AWS Signer automatically uses the GovCloud partition specific root certificate when signing.
- Signature revocation is only valid within the same AWS partition that an artifact was signed in. The [GetRevocationStatus API](../../../signer/latest/api/API_GetRevocationStatus.md "../../../signer/latest/api/API_GetRevocationStatus.md") will not return the revocation information for any signatures or profiles that were revoked in other partitions.
- If you’re signing container images, you must complete the following steps:
  1.  You must use the AWS GovCloud specific root certificate when verifying container images signed in the GovCloud Region. You can install the GovCloud root certificate either using the AWS Signer plugin for Notation, which includes the GovCloud root certificate, or by directly downloading the [GovCloud root certificate](https://d2hvyiie56hcat.cloudfront.net/aws-us-gov-signer-notation-root.cert "https://d2hvyiie56hcat.cloudfront.net/aws-us-gov-signer-notation-root.cert"). For more information, see [Prerequisites for signing container images](https://d2hvyiie56hcat.cloudfront.net/image-signing-prerequisites.cert "https://d2hvyiie56hcat.cloudfront.net/image-signing-prerequisites.cert").
  2.  In your trust policy, you must set `signingAuthority` to `aws-us-gov-signer-ts`. For example:

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
              "signingAuthority:aws-us-gov-signer-ts"
           ],
           "trustedIdentities":[
              "arn:aws:signer:region:111122223333:/signing-profiles/ecr_signing_profile",
              "arn:aws:signer:region:111122223333:/signing-profiles/ecr_signing_profile2"
           ]
        }
     ]
  }
  ```

  For more information about setting up trust policies for image verification, see [Verify an image locally after signing](../../../signer/latest/developerguide/image-verification.md "../../../signer/latest/developerguide/image-verification.md").

## Documentation for AWS Signer

[AWS Signer documentation](../../../signer/index.md "../../../signer/index.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.

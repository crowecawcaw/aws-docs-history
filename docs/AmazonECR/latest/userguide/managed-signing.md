# Managed signing

Amazon ECR managed signing automatically signs your container images by generating cryptographic signatures using [AWS Signer](../../../signer/latest/developerguide/Welcome.md "../../../signer/latest/developerguide/Welcome.md") when images are pushed to Amazon ECR. This eliminates the need to install and configure client-side tools and allows you to centrally govern signing as a registry configuration.

## Prerequisites

To configure managed signing, you create a signing configuration with Amazon ECR that references one or more Signer signing profiles and, optionally, repository filters that restrict which repositories should have their images signed. Once configured, Amazon ECR managed signing automatically signs images as they are pushed using the identity of the entity pushing the image.

Before you can configure managed signing, you must have the following:

- **A Signer signing profile** — Create at least one Signer [signing profile](../../../signer/latest/developerguide/signing-profiles.md "../../../signer/latest/developerguide/signing-profiles.md").
  A signing profile is a unique AWS Signer resource that you can use to perform signing operations in
  Amazon ECR. Signing profiles enable you to sign and verify code artifacts, such as container images
  and AWS Lambda deployment bundles. Each signing profile designates the signing platform to sign
  for, a platform ID, and other platform-specific information. For example, a signing profile ARN
  looks like this: `arn:`partition`:signer:`region`:`account-id`:/signing-profiles/`profile-name``.
- **IAM permissions** — The IAM principal that pushes the image must have the necessary IAM
  permissions to access the relevant Signer signing profile and the relevant ECR repository. You
  need to modify the identity-based policy for the IAM principal to include permissions for both
  ECR repository operations and Signer signing operations. The following example policy shows the
  required permissions:

```
{
   "Version": "2012-10-17",
   "Statement": [
   {
       "Sid":"UploadSignaturePermissions",
       "Effect":"Allow",
       "Action":[
           "ecr:CompleteLayerUpload",
           "ecr:UploadLayerPart",
           "ecr:InitiateLayerUpload",
           "ecr:BatchCheckLayerAvailability",
           "ecr:PutImage"
       ],
       "Resource":"arn:aws:ecr:`region`:`account-id`:repository/`repository-name`"
   },
   {
       "Sid": "SignPermissions",
       "Effect": "Allow",
       "Action": [
           "signer:SignPayload"
       ],
       "Resource": "arn:aws:signer:`region`:`account-id`:/signing-profiles/`signing-profile-name`"
   }
   ]
}
```

With Amazon ECR managed signing, you can create multiple signing rules (up to 10 per registry) to create stronger security boundaries. For example, you might run multiple build pipelines and want to limit which repositories each pipeline can sign. Within each rule, you configure a signing profile and specify repository name filters. When a new image is pushed, Amazon ECR matches which signing rule and signing profile can sign the image. If there are multiple matches, Amazon ECR generates multiple signatures.

###### Note

If you verify signatures manually, you still need to install the Notation CLI.

###### Note

Amazon ECR managed signing is available in all AWS Regions where container image signing with AWS Signer is available.

## Getting started

Follow these steps to configure managed signing. You provide Amazon ECR with a reference to
a Signer signing profile and, optionally, filters that restrict which repositories should have their
images signed.

AWS Management Console
Use the following steps to configure managed signing using the
AWS Management Console.

1. Open the [Amazon ECR console](https://console.aws.amazon.com/ecr/private-registry/repositories "https://console.aws.amazon.com/ecr/private-registry/repositories"). In the left navigation pane, select **Private registry**,
   **Features & settings**, **Managed signing**.
2. On the **Signing rules** page, select **Create rule**.
3. On the **Signing profile** page, under **Select a AWS
   signer profile**, choose **Create new AWS signer profile**,
   enter a **Profile name**, and, optionally, change the **Signature
   validity period**. Then select **Next**.
4. On the **Filters** page, under **Select repositories**,
   enter a **Repository name filter**. Then select
   **Next**.
5. On the **Review and create** page, verify the **AWS Signer
   profile** and **Repository name filters** you have entered. If everything looks correct, select
   **Save**.

AWS CLI
Use the following AWS CLI commands to configure managed signing.

- **Create a signing rule**

Create a signing configuration with your signing profile ARN. Create a JSON file with the following contents:

```
{
    "rules": [
        {
            "signingProfileArn": "arn:aws:signer:`region`:`account-id`:/signing-profiles/`profile-name`",
            "repositoryFilters": [
                {
                    "filter": "`test*`",
                    "filterType": "WILDCARD_MATCH"
                }
            ]
        }
    ]
}
```

Then run the following command:

```
`aws ecr --region `region` \
 put-signing-configuration \
 --signing-configuration file://signing-config.json`
```

You should see the API response containing the signing configuration.

- **View your signing configuration**

Retrieve your signing configuration:

```
`aws ecr --region `region` \
 get-signing-configuration`
```

You should see the API response containing the signing configuration.

- **Check image signing status**

Push an image to your repository. For example:

```
`docker pull ubuntu

IMAGE_NAME="`account-id`.dkr.ecr.`region`.amazonaws.com/`repository-name`"
IMAGE_TAG="${IMAGE_NAME}:`test-1`"

docker tag ubuntu $IMAGE_TAG
docker push $IMAGE_TAG`
```

After pushing, use your image tag to check the signing status:

```
`aws ecr --region `region` \
 describe-image-signing-status \
 --repository-name `repository-name` \
 --image-id imageTag=`test-1``
```

If the repository name matches your repository filter defined in the signing configuration, you should see signing status in the API response. If the status is successful, you should see a signature pushed to your repository.

- **Delete your signing configuration**

Delete your signing configuration:

```
`aws ecr --region `region` \
 delete-signing-configuration`
```

You should see the API response containing the deleted signing configuration.

## Considerations

The following limitations and capabilities apply to managed signing:

- **Cross-region signing is not supported** — Signing profiles must be in the same region as your Amazon ECR registry. You cannot use a signing profile from one region to sign images in a registry located in a different region.
- **Cross-account signing is supported** — Signing profiles can be in different accounts than your Amazon ECR registry. This enables organizations to centrally manage signing profiles while allowing developers in other accounts to use them. For more information, see [Set up cross-account signing for Signer](../../../signer/latest/developerguide/signing-profile-cross-account.md "../../../signer/latest/developerguide/signing-profile-cross-account.md") in the _AWS Signer Developer Guide_.
- **Signatures cannot be signed** — You cannot sign signatures themselves. Only container images can be signed.

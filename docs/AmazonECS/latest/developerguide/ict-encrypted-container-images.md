

# Encrypted container images
<a name="ict-encrypted-container-images"></a>

## Overview
<a name="ict-encrypted-container-images-overview"></a>

Container image layers are visible to the parent instance unless encrypted. Encrypted images follow the [OCI image encryption specification on the GitHub website](https://github.com/containers/ocicrypt). Only layers are encrypted; the manifest and image config remain in plaintext so that registries and container runtimes can inspect them.

When a confidential task uses an encrypted image, the parent instance pulls the encrypted layer blobs from the registry and transfers them into the Nitro Sandbox without unpacking them. The sandbox unwraps the layer encryption key through AWS KMS and decrypts each layer before unpacking it. The parent instance never sees plaintext layer data.

**Important**  
Encrypted images require `CONFIDENTIAL_SANDBOX`. In `ISOLATED_SANDBOX` the parent instance unpacks image layers itself and cannot decrypt them, so a task that references an encrypted image fails to start with an image pull error.

**Important**  
Every layer of the image must be encrypted. Confidential tasks do not support an image that mixes encrypted and plaintext layers. The image pull fails with an error naming the layers that are not encrypted. Encrypt the whole image, as [Encrypting an image](#ict-encrypt-an-image) describes.

## Prerequisites
<a name="ict-encrypted-container-images-prerequisites"></a>

Before you encrypt an image, make sure you have the following:
+ An AWS KMS symmetric key for encrypting image layers.
+ [skopeo on the GitHub website](https://github.com/containers/skopeo), an open source tool for copying container images between registries without a local Docker daemon.
+ The `nitro-sandbox-keyprovider` binary installed on your build machine. For instructions on downloading and verifying it, see [Getting the CLI tools](ict-get-cli-tools.md).
+ Create an ocicrypt keyprovider configuration file at `/etc/ocicrypt.json` with the following contents:

  ```
  {
    "key-providers": {
      "awskms": {
        "cmd": {
          "path": "/usr/local/bin/nitro-sandbox-keyprovider",
          "args": []
        }
      }
    }
  }
  ```
+ The task IAM role must have `kms:Decrypt` permission on the AWS KMS key. The sandbox decrypts with the task role credentials; the task execution role needs no AWS KMS permission.

## Encrypting an image
<a name="ict-encrypt-an-image"></a>

Use skopeo to encrypt the image. It copies the image from a source registry to a destination registry and encrypts the layers in transit.

If your destination registry is Amazon ECR, authenticate skopeo to it first:

```
aws ecr get-login-password --region aa-example-1 \
  | skopeo login --username AWS --password-stdin \
    111122223333.dkr.ecr.aa-example-1.amazonaws.com
```

Then encrypt the image:

Replace {{aa-example-1}}, {{111122223333}}, {{mrk-example}}, and {{registry.example.com/myimage}} with your values:

```
OCICRYPT_KEYPROVIDER_CONFIG=/etc/ocicrypt.json \
  skopeo copy \
    --encryption-key provider:awskms:arn:aws:kms:aa-example-1:111122223333:key/mrk-example \
    docker://registry.example.com/myimage:latest \
    docker://registry.example.com/myimage:encrypted
```

Replace the KMS key ARN and image repository with your values. The encrypted image has the same manifest structure, but each layer descriptor gains a `+encrypted` media type suffix and annotations containing the wrapped key material.

**Note**  
For a multi-architecture source (a manifest list), skopeo copies only the instance matching your build host by default. Pass `--all` to encrypt and copy every instance in the list, or use the global `--override-os` and `--override-arch` options before the `copy` subcommand to select a different single instance. A task fails to start if the encrypted repository has no instance for the instance architecture it is placed on.

**Important**  
`--encryption-key provider:awskms:…` must be given a full AWS KMS key ARN (`arn:aws:kms:<region>:<account>:key/<id>`). Bare key IDs and aliases are rejected because the recorded ARN must unambiguously identify the key that produced the ciphertext. The keyprovider uses the AWS Region from the ARN for the KMS `Encrypt` call and writes the full ARN into the encrypted image so the guest can select the correct Regional endpoint and pass the ARN as `KeyId` to `Decrypt`.

## Deploying a task with an encrypted image
<a name="ict-deploy-a-task-with-an-encrypted-image"></a>

1. Reference the encrypted image in your task definition and set `trustedExecutionConfiguration.isolationMode` to `CONFIDENTIAL_SANDBOX`.

1. Generate the attestation policy from that task definition with `ecs-nitro-sandbox-genpolicy`, as described in [Generating a policy](ict-confidential-policy-configuration.md#ict-generate-a-policy). The tool detects encrypted layers from the image manifest; you don't need to specify an extra option.

1. In the AWS KMS key policy, add the PCR17 and PCR8 condition that the tool prints with `--output pcrs` to the statement that allows the task role `kms:Decrypt`, as described in [Attestation and PCR values](ict-confidential-policy-configuration.md#ict-attestation-and-pcr-values).

**Important**  
If a container doesn't run as root, set its `user` in the task definition to a numeric `uid:gid`. The policy generator resolves a user name through the image's `/etc/passwd` and `/etc/group`, which it can't read from encrypted layers, so a named user, whether set in the task definition or by the image's `USER` instruction, fails policy generation. For more information about allowing an unpinned identity, see [Allowing an unpinned identity](ict-confidential-policy-configuration.md#ict-allow-an-unpinned-identity).

**Important**  
The task needs a network path to AWS KMS. The sandbox calls `kms:Decrypt` over the task's elastic network interface, not from the instance, so the task's subnet and security group must allow outbound HTTPS to AWS KMS. For more information about connecting to AWS KMS from a private subnet, see [Connecting to AWS KMS through a VPC endpoint](https://docs.aws.amazon.com/kms/latest/developerguide/kms-vpc-endpoint.html).

## Troubleshooting a task that fails to start
<a name="ict-encrypted-image-troubleshooting"></a>

A task that can't decrypt its image stops with `TaskFailedToStart`. The stopped reason in `DescribeTasks` names the cause:
+ `KMS Decrypt failed` with `AccessDeniedException`: the key policy denied the task role. For more information, see [Checking whether the policy matches the task definition](ict-confidential-policy-configuration.md#ict-check-policy-in-sync).
+ A AWS KMS connection timeout: the task has no network path to AWS KMS. Check the route table and security group of the subnets in the task's `networkConfiguration`.

## Identifying images in operator tooling
<a name="ict-image-identity-in-operator-tooling"></a>

For a multi-architecture encrypted image, the image digest that `DescribeTasks` reports in task and container status is the digest of the platform-specific manifest, not the digest of the manifest list.


# Getting the CLI tools
<a name="ict-get-cli-tools"></a>

Two command line tools support isolated and confidential tasks. Run both tools on your workstation or in your build pipeline, not on the instance:
+ `ecs-nitro-sandbox-genpolicy` generates an attestation policy from an Amazon ECS task definition. For more information about attestation policies, see [Confidential policy configuration](ict-confidential-policy-configuration.md).
+ `nitro-sandbox-keyprovider` is an ocicrypt key provider, backed by AWS KMS, that [skopeo on the GitHub website](https://github.com/containers/skopeo) uses to encrypt container images for confidential mode. For more information, see [Encrypted container images](ict-encrypted-container-images.md).

Both tools ship together in a single signed release of the Nitro Sandboxes runtime binaries, which AWS publishes for Linux on `x86_64` and `aarch64` under the [AWS Intellectual Property License](https://aws.amazon.com/legal/aws-ip-license-terms/). The tools require glibc 2.34 or later. You do not need an AWS account to download them.

## Downloading the tools
<a name="ict-get-cli-tools-download"></a>

Download the archive for your architecture. These links resolve to the latest release, so you do not need to track version numbers:
+ To download the tools for `x86_64`, choose [nitro-sandboxes-runtime.tar.gz](https://d1uvmbvklg8rt.cloudfront.net/latest/x86_64/nitro-sandboxes-runtime.tar.gz).
+ To download the tools for `aarch64`, choose [nitro-sandboxes-runtime.tar.gz](https://d1uvmbvklg8rt.cloudfront.net/latest/aarch64/nitro-sandboxes-runtime.tar.gz).

Extract the archive with the following `tar` command. It expands flat, with no directories, and contains both tools along with a `LICENSE` and `ATTRIBUTION` file:

```
tar -xzf nitro-sandboxes-runtime.tar.gz
```

**Note**  
Depending on your version of `tar`, extraction might print `implausibly old time stamp` warnings for the archive members. This is expected and does not indicate a problem: the archive uses fixed timestamps for reproducible builds, and `tar` still exits successfully.

Place the tools you need — `ecs-nitro-sandbox-genpolicy`, `nitro-sandbox-keyprovider`, or both — in `/usr/local/bin`, a directory on your `PATH`. If you install `nitro-sandbox-keyprovider` elsewhere, update the `path` in `/etc/ocicrypt.json` to match. To confirm that what you downloaded is what AWS published, verify the download before you use the tools, as described in the next section.

## Verifying your download
<a name="ict-get-cli-tools-verify"></a>

AWS signs each release so that you can confirm it is intact and came from AWS. This step is optional but recommended. Alongside each archive, AWS publishes a checksum manifest (`SHA256SUM`). The manifest lists a SHA-256 hash for the archive and for each binary in it. AWS also publishes a detached signature over that manifest (`SHA256SUM.sig`). AWS produces the signature with an asymmetric AWS KMS key (ECDSA on the NIST P-384 curve). You verify the signature with the public key provided in the following procedure.

1. Create the public key file. Copy the following into a text file named `nitro-sandboxes-runtime-v1.pub`:

   ```
   -----BEGIN PUBLIC KEY-----
   MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAESqdVXO82n+Zh5+IFLh1xjmxZLkjjZWvf
   DCS927SdVYjP0AZ92XCxS+ucrs9cjuNlTaDARTHov2XVfMVgau8TEPFKGDRmVZXJ
   c25CVihKHLFK8T8hNMIL+fbGcvE2fwIO
   -----END PUBLIC KEY-----
   ```

1. Download the checksum manifest and its signature for your architecture into the same directory as the archive:
   + x86\_64: [SHA256SUM](https://d1uvmbvklg8rt.cloudfront.net/latest/x86_64/SHA256SUM) and [SHA256SUM.sig](https://d1uvmbvklg8rt.cloudfront.net/latest/x86_64/SHA256SUM.sig)
   + aarch64: [SHA256SUM](https://d1uvmbvklg8rt.cloudfront.net/latest/aarch64/SHA256SUM) and [SHA256SUM.sig](https://d1uvmbvklg8rt.cloudfront.net/latest/aarch64/SHA256SUM.sig)

1. Verify the signature over the manifest. The digest is SHA-384 (it pairs with the P-384 key), even though the hashes listed inside the manifest are SHA-256:

   ```
   openssl dgst -sha384 -verify nitro-sandboxes-runtime-v1.pub \
     -signature SHA256SUM.sig SHA256SUM
   ```

   The command prints `Verified OK` on success. Any other output means the manifest or signature is not what AWS published; do not use the download.

1. Verify the downloaded archive and the extracted tools against the signed manifest:

   ```
   sha256sum -c SHA256SUM
   ```

   The `SHA256SUM` manifest covers the archive and each binary in it, so `sha256sum` prints one `OK` line per file. Any `FAILED` line means that file does not match what AWS published; do not use the download.
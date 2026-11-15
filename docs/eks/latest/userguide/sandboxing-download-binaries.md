

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Download and verify the runtime binaries
<a name="sandboxing-download-binaries"></a>

If you build your own node images instead of using the AMIs that AWS manages, you install the Nitro Sandbox runtime binaries yourself. AWS publishes them as a signed release for each supported architecture (`x86_64` and `aarch64`), under the AWS Intellectual Property License. The binaries require glibc 2.34 or later. You do not need an AWS account to download or verify a release.

This topic covers the runtime binaries release. The host-kernel patch series and the guest image that you also need to build an AMI are published separately. For the full build procedure, see [Create and update a Nitro Sandbox AMI](sandboxing-ami-create-update.md).

## What a release contains
<a name="sandboxing-release-contents"></a>

For each architecture, AWS publishes the following files:


| File | Contents | 
| --- | --- | 
|  `nitro-sandboxes-runtime.tar.gz`  | The runtime binaries — the shim (`containerd-shim-nitro-sandbox-v2`), `eks-nitro-sandbox-genpolicy`, and `nitro-sandbox-keyprovider` — plus `LICENSE` and `ATTRIBUTION`. The archive extracts flat, with no directories. | 
|  `SHA256SUM`  | SHA-256 hashes of the archive and of each binary. This is the file that AWS signs. | 
|  `SHA256SUM.sig`  | The detached signature over `SHA256SUM`. | 

The download links resolve to the latest release, so you do not need to track version numbers. To pin a specific release instead, replace `latest` in the download and verification URLs with the release version (for example, `0.1.4274.0`).

**Note**  
Verify the release with the `SHA256SUM` file you download separately (alongside the archive), not the `SHA256SUM` file found inside the extracted archive. The two have the same name but different contents: the downloaded manifest is the one AWS signs and covers the archive and each binary, while the copy inside the archive covers a different set of files. The signature verification in the next section succeeds only against the downloaded manifest.

## Download a release
<a name="sandboxing-download-location"></a>

Download the archive for your node architecture:
+ x86\_64: [nitro-sandboxes-runtime.tar.gz](https://d1uvmbvklg8rt.cloudfront.net/latest/x86_64/nitro-sandboxes-runtime.tar.gz) 
+ aarch64: [nitro-sandboxes-runtime.tar.gz](https://d1uvmbvklg8rt.cloudfront.net/latest/aarch64/nitro-sandboxes-runtime.tar.gz) 

Extract the archive:

```
tar -xzf nitro-sandboxes-runtime.tar.gz
```

**Note**  
Depending on your version of `tar`, extraction might print `implausibly old time stamp` warnings for the archive members. This is expected and does not indicate a problem: the archive uses fixed timestamps for reproducible builds, and `tar` still exits successfully.

To confirm that what you downloaded is what AWS published, verify the download before you use the binaries, as described in the next section.

## Verify a release
<a name="sandboxing-verify-binaries"></a>

 AWS signs each release so that you can confirm it is intact and came from AWS. This step is optional but recommended. Alongside each archive, AWS publishes a checksum manifest (`SHA256SUM`) and a detached signature over that manifest (`SHA256SUM.sig`). The signature is produced with an asymmetric AWS KMS key (ECDSA on the NIST P-384 curve). You verify the signature with the public key.

1. Create the public key file. Copy the following into a text file named `nitro-sandboxes-runtime-v1.pub`:

   ```
   -----BEGIN PUBLIC KEY-----
   MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAESqdVXO82n+Zh5+IFLh1xjmxZLkjjZWvf
   DCS927SdVYjP0AZ92XCxS+ucrs9cjuNlTaDARTHov2XVfMVgau8TEPFKGDRmVZXJ
   c25CVihKHLFK8T8hNMIL+fbGcvE2fwIO
   -----END PUBLIC KEY-----
   ```

1. Download the checksum manifest and its signature for your architecture into the same directory as the archive. For x86\_64, download [SHA256SUM](https://d1uvmbvklg8rt.cloudfront.net/latest/x86_64/SHA256SUM) and [SHA256SUM.sig](https://d1uvmbvklg8rt.cloudfront.net/latest/x86_64/SHA256SUM.sig). For aarch64, download [SHA256SUM](https://d1uvmbvklg8rt.cloudfront.net/latest/aarch64/SHA256SUM) and [SHA256SUM.sig](https://d1uvmbvklg8rt.cloudfront.net/latest/aarch64/SHA256SUM.sig).

1. Verify the signature over the manifest. The digest is SHA-384 (it pairs with the P-384 key), even though the hashes listed inside the manifest are SHA-256:

   ```
   openssl dgst -sha384 -verify nitro-sandboxes-runtime-v1.pub \
     -signature SHA256SUM.sig SHA256SUM
   ```

   The command prints `Verified OK` on success. Any other output means the manifest or signature is not what AWS published; do not use the download.

1. Verify the downloaded archive and the extracted binaries against the signed manifest:

   ```
   sha256sum -c SHA256SUM
   ```

   The `SHA256SUM` manifest covers the archive and each binary in it, so `sha256sum` prints one `OK` line per file. Any `FAILED` line means that file does not match what AWS published; do not use the download.
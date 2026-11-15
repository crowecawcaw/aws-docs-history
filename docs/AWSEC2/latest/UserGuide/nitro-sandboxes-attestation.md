

# Attest a Nitro Sandbox
<a name="nitro-sandboxes-attestation"></a>

A Nitro Sandbox in confidential mode can prove to an external service which code it runs and on which parent instance it runs. The Nitro System records measurements in the platform configuration registers (PCRs) of the Nitro Security Module (NSM) in the Nitro Sandbox. Your workload requests an attestation document from the NSM, and presents it to a service such as AWS Key Management Service (AWS KMS).

Attestation works like attestation for Nitro Enclaves. For more information, see [Cryptographic attestation](https://docs.aws.amazon.com/enclaves/latest/user/set-up-attestation.html) in the *AWS Nitro Enclaves User Guide*.

The measurements and the key policy rules apply to every Nitro Sandbox in confidential mode. The procedures use a Nitro Sandbox that you launch with Firecracker, as described in [Run Nitro Sandboxes with Firecracker](nitro-sandboxes-run-firecracker.md). For attestation of pods and tasks that Amazon Elastic Kubernetes Service (Amazon EKS) or Amazon Elastic Container Service (Amazon ECS) runs in Nitro Sandboxes, see [Sandboxing on Amazon EKS with isolated and confidential pods](https://docs.aws.amazon.com/eks/latest/userguide/sandboxing.html) in the *Amazon EKS User Guide* and [Isolated and confidential tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html) in the *Amazon Elastic Container Service Developer Guide*.

The Nitro System doesn't measure the contents of block devices. Put the code that you want to attest in the initial RAM disk, or have the initial RAM disk verify or decrypt the file systems that it mounts.

**Topics**
+ [Nitro Sandbox measurements](#nitro-sandboxes-attestation-pcrs)
+ [Add attestation to a guest image](#nitro-sandboxes-attestation-image)
+ [Compute the expected PCR values](#nitro-sandboxes-attestation-expected)
+ [Get an attestation document](#nitro-sandboxes-attestation-document)
+ [Use attestation with AWS KMS](#nitro-sandboxes-attestation-kms)

## Nitro Sandbox measurements
<a name="nitro-sandboxes-attestation-pcrs"></a>

A PCR starts as 48 zero bytes, and each measurement extends it: the new value is the SHA-384 hash of the old value followed by the measurement. The Nitro System locks PCRs 0 to 15 before the guest kernel runs.

The following table lists the PCRs of a Nitro Sandbox in confidential mode. All values are SHA-384 hashes.


**Nitro Sandbox PCRs**  

| PCR | Measurement | Difference from Nitro Enclaves | 
| --- | --- | --- | 
| PCR0 | The image: the kernel, the kernel command line, and the initial RAM disks, followed by the feature flags of the image. The flags record launch settings, such as CPU overcommit and hot plug, so a change to these settings changes PCR0. | Includes the feature flags. The value differs from the PCR0 that the Nitro Enclaves CLI (nitro-cli) reports for the same files. | 
| PCR1 | The kernel, the kernel command line, and the first initial RAM disk. | None | 
| PCR2 | The initial RAM disks after the first. If the image has one initial RAM disk, PCR2 holds the measurement of empty input. | None | 
| PCR3 | The ARN of the IAM role in the instance profile of the parent instance, if the parent instance has one. | Keeps its value in debug mode. In Nitro Enclaves, it reads as zero in debug mode. | 
| PCR4 | The instance ID of the parent instance. | Keeps its value in debug mode. In Nitro Enclaves, it reads as zero in debug mode. | 
| PCR5 | The PCI functions that the Nitro Sandbox has at boot, or a fixed value when hot plug is on. | New for Nitro Sandboxes | 
| PCR6 | The whole image file that the Nitro System boots. | New for Nitro Sandboxes | 
| PCR16 to PCR31 | Not set by the Nitro System. Your workload can extend and lock them, for example to record a policy that it loads at runtime. | None | 

After the VMM attaches the boot devices, and before the guest starts, the Nitro System extends PCR5 once for each PCI function, in bus, device, and function order. Each measurement is a 12-byte identity: the vendor ID, device ID, subsystem vendor ID, subsystem ID, base class and subclass, and a reserved zero field. The Nitro System doesn't measure PCI bridges or the NSM.

If the Nitro System measures no function, PCR5 holds the measurement of the string `EMPTY`. If you enable hot plug, PCR5 holds the measurement of the string `HOTPLUG_ENABLED` instead, because devices can change after boot, and PCR5 does not identify the devices.

For an image that you build with `eif_build`, PCR6 is the value that `eif_build` prints. The image records its build time, so PCR6 changes with every build, unless you pass the same `--build-time` value to every build. When Firecracker builds the image at launch, PCR6 also changes with the memory size and the number of vCPUs. Use PCR0 instead of PCR6 in key policies.

In debug mode, PCR0, PCR1, PCR2, PCR5, and PCR6 read as zero, but PCR3 and PCR4 keep the values of the parent instance. A key policy that checks only PCR3 or PCR4 therefore also releases secrets to a Nitro Sandbox in debug mode. For how to write a key policy that prevents this, see [Use attestation with AWS KMS](#nitro-sandboxes-attestation-kms).

## Add attestation to a guest image
<a name="nitro-sandboxes-attestation-image"></a>

The following procedures extend the guest image from [Prepare a guest image](nitro-sandboxes-run-firecracker.md#nitro-sandboxes-guest-image). At boot, the init script generates an RSA key pair, requests an attestation document that contains the public key, and sends the document to the parent instance over vsock. It then waits for the response from AWS KMS, decrypts the secret, and starts your workload.

The first procedure builds a small program, **nsm-attest**, that requests the attestation document from the NSM and writes it to a file. The program uses the NSM API library, as described in [Get an attestation document](#nitro-sandboxes-attestation-document).

**To build the **nsm-attest** program**

1. Install a C linker and the Rust toolchain, with the target for static binaries. For other ways to install Rust, see [Install Rust](https://www.rust-lang.org/tools/install) on the Rust website.

   ```
   sudo dnf install -y gcc
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal
   . "$HOME/.cargo/env"
   rustup target add $(uname -m)-unknown-linux-musl
   ```

1. Create a directory for the program, and save the following content as `nsm-attest/Cargo.toml`.

   ```
   mkdir -p nsm-attest/src
   ```

   ```
   [package]
   name = "nsm-attest"
   version = "0.1.0"
   edition = "2021"
   
   [dependencies]
   aws-nitro-enclaves-nsm-api = "0.4"
   serde_bytes = "0.11"
   ```

1. Save the following content as `nsm-attest/src/main.rs`.

   ```
   // Requests an attestation document from the NSM and writes it to a file.
   // Usage: nsm-attest attest --public-key key.der --output attestation.bin
   use aws_nitro_enclaves_nsm_api::api::{Request, Response};
   use aws_nitro_enclaves_nsm_api::driver::{nsm_exit, nsm_init, nsm_process_request};
   use serde_bytes::ByteBuf;
   use std::{env, fs, process::exit};
   
   fn usage() -> ! {
       eprintln!("usage: nsm-attest attest --public-key FILE --output FILE");
       exit(2);
   }
   
   fn main() {
       let args: Vec<String> = env::args().collect();
       if args.get(1).map(String::as_str) != Some("attest") {
           usage();
       }
       let (mut public_key, mut output) = (None, None);
       let mut i = 2;
       while i + 1 < args.len() {
           match args[i].as_str() {
               "--public-key" => public_key = Some(fs::read(&args[i + 1]).expect("read public key")),
               "--output" => output = Some(args[i + 1].clone()),
               _ => usage(),
           }
           i += 2;
       }
       let (Some(public_key), Some(output)) = (public_key, output) else {
           usage()
       };
   
       let fd = nsm_init();
       if fd < 0 {
           eprintln!("cannot open /dev/nsm");
           exit(1);
       }
       let request = Request::Attestation {
           user_data: None,
           nonce: None,
           public_key: Some(ByteBuf::from(public_key)),
       };
       let response = nsm_process_request(fd, request);
       nsm_exit(fd);
       match response {
           Response::Attestation { document } => fs::write(&output, document).expect("write document"),
           other => {
               eprintln!("NSM error: {:?}", other);
               exit(1);
           }
       }
   }
   ```

1. Build the program as a static binary, so that it runs from the initial RAM disk, and install it in `/usr/local/bin`.

   ```
   cd nsm-attest
   cargo build --release --target $(uname -m)-unknown-linux-musl
   sudo install -m 755 target/$(uname -m)-unknown-linux-musl/release/nsm-attest /usr/local/bin/
   cd ..
   ```

**To add attestation to the guest image**

1. Install **socat**. The guest image and the parent instance use it to exchange files over vsock.

   ```
   sudo dnf install -y socat
   ```

1. In `sandbox-init`, add the following lines before the line that starts your workload.

   ```
   # Request an attestation document that carries a new public key.
   cd /tmp
   openssl genrsa -out key.pem 2048
   openssl rsa -in key.pem -pubout -outform DER -out key.der
   nsm-attest attest --public-key key.der --output attestation.bin
   
   # Send the document to the parent instance over vsock port 5005, and
   # receive the KMS response on port 5006.
   until socat -u OPEN:attestation.bin VSOCK-CONNECT:2:5005; do sleep 1; done
   until socat -u VSOCK-CONNECT:2:5006 CREATE:response.cms; do sleep 1; done
   openssl cms -decrypt -inform DER -in response.cms -inkey key.pem -out secret.bin
   ```

   The script waits until the parent instance completes the exchange in [Use attestation with AWS KMS](#nitro-sandboxes-attestation-kms). Your workload can then read the secret from `/tmp/secret.bin`.

1. Build the initial RAM disk again, with the additional programs.

   ```
   sudo dracut --force --no-hostonly --reproducible --no-early-microcode \
       --modules bash \
       --add-drivers "virtio_pci virtio_net vmw_vsock_virtio_transport nsm" \
       --install "mount modprobe ip sleep openssl socat /usr/local/bin/nsm-attest /etc/pki/tls/openssl.cnf" \
       --include "$PWD/sandbox-init" /init \
       --kver $(uname -r) initrd.img
   sudo chown "$(id -un):" initrd.img
   ```

## Compute the expected PCR values
<a name="nitro-sandboxes-attestation-expected"></a>

You need the expected PCR values to write a key policy. To get them, build the image in advance with `eif_build`, which prints the measurements of the image, and launch that image. `eif_build` is part of the [aws-nitro-enclaves-image-format](https://github.com/aws/aws-nitro-enclaves-image-format) project on the GitHub website.

Build the image with the same settings that you launch the Nitro Sandbox with, such as CPU overcommit and hot plug. If the settings of the image don't match the launch configuration, the launch fails. The example builds an image for dedicated vCPUs, so the Nitro Sandbox doesn't use CPU overcommit.

**To compute PCR0, PCR1, and PCR2**

1. Install `eif_build` from the aws-nitro-enclaves-image-format project. The command uses the Rust toolchain from [Add attestation to a guest image](#nitro-sandboxes-attestation-image) and installs `eif_build` in `~/.cargo/bin`.

   ```
   sudo dnf install -y openssl-devel
   cargo install --git https://github.com/aws/aws-nitro-enclaves-image-format eif_build
   ```

1. Build the image from the files of [Add attestation to a guest image](#nitro-sandboxes-attestation-image), with the default command line of Firecracker.

   ```
   eif_build --kernel vmlinuz \
       --cmdline "panic=1 initcall_blacklist=i8042_init" \
       --ramdisk initrd.img \
       --pcie-virtio \
       --output sandbox.eif
   ```

   The `--pcie-virtio` option builds the image for a Nitro Sandbox in confidential mode without CPU overcommit or hot plug.

1. Copy the PCR0, PCR1, and PCR2 values from the output. PCR0 depends on the files, the command line, and the settings. PCR1 and PCR2 depend only on the files and the command line.

   The following is example output.

   ```
   Output file: sandbox.eif
   {
     "HashAlgorithm": "Sha512_48 { .. }",
     "PCR0": "294af39e266a15be97de5d99b210f81fb9147044d9eb456ad808eeb8b2c2498cfebd4cf57e669228a2a8cde356722f25",
     "PCR1": "61f2b585b0994827830d1dbc2f0011cc30cdc9fd65e1e24eb99666442020676a1b9adf63008df638ca0a228e342d953c",
     "PCR2": "21b9efbc184807662e966d34f390821309eeac6802309798826296bf3e8bec7c10edb30948c90ba67310f7b964fc500a",
     "PCR6": "fb9718a5397717ed57cb42c2a6c4dea98e22f4bc21df1808ad8dde4ed8c1c450c123fdab9f2fa3c065e005357a768be6"
   }
   ```

1. In `sandbox.json` from [Launch a Nitro Sandbox](nitro-sandboxes-run-firecracker.md#nitro-sandboxes-launch), set `kernel_image_path` to the image file, remove `initrd_path`, and remove `cpu_overcommit` from the `enclave` object. On instances with two threads per core, use an even number of vCPUs.

   ```
   "boot-source": {
       "kernel_image_path": "sandbox.eif"
   }
   ```

PCR3 and PCR4 extend the zero value with the role ARN and the instance ID as text. Compute them with the following commands. If you change the instance profile of the parent instance, PCR3 changes.

```
python3 -c 'import hashlib, sys; print(hashlib.sha384(b"\0" * 48 + sys.argv[1].encode()).hexdigest())' {{arn:aws:iam::111122223333:role/parent-instance-role}}
python3 -c 'import hashlib, sys; print(hashlib.sha384(b"\0" * 48 + sys.argv[1].encode()).hexdigest())' {{i-1234567890abcdef0}}
```

PCR5 depends on the devices that the parent instance attaches and on the order in which Firecracker adds them. To get the expected value, launch the Nitro Sandbox once with the final device configuration, and read PCR5 in the Nitro Sandbox with the `DescribePCR` request of the NSM API or from an attestation document. Use PCR5 in a key policy only if your device configuration does not change.

## Get an attestation document
<a name="nitro-sandboxes-attestation-document"></a>

In a Nitro Sandbox in confidential mode, the Linux `nsm` driver (`CONFIG_NSM`) exposes the NSM as `/dev/nsm`. If the driver is a module, as in the AL2023 kernel, load it with `modprobe nsm` before you request a document.

To request an attestation document, use the NSM API library from the [aws-nitro-enclaves-nsm-api](https://github.com/aws/aws-nitro-enclaves-nsm-api) project on the GitHub website, as the **nsm-attest** program in [Add attestation to a guest image](#nitro-sandboxes-attestation-image) does. The project provides the `aws-nitro-enclaves-nsm-api` Rust crate and a C library (`libnsm`). Pass the public key of an RSA key pair that your workload generates, because AWS KMS encrypts its response to this key. Build your program as a static binary, or include its libraries in the initial RAM disk.

You can also pass a nonce and user data for your own verifier. The same library extends and locks PCRs 16 to 31.

To use attestation with your own service, verify the signature and certificate chain of the attestation document. The chain ends at the same AWS Nitro Enclaves root certificate as for Nitro Enclaves. For more information, see the [NSM attestation process](https://github.com/aws/aws-nitro-enclaves-nsm-api/blob/main/docs/attestation_process.md) documentation on the GitHub website.

## Use attestation with AWS KMS
<a name="nitro-sandboxes-attestation-kms"></a>

AWS KMS accepts attestation documents from a Nitro Sandbox for the `Decrypt`, `DeriveSharedSecret`, `GenerateDataKey`, `GenerateDataKeyPair`, and `GenerateRandom` operations. When a request includes an attestation document, AWS KMS does not return plaintext. It returns `CiphertextForRecipient`, which only the private key in the Nitro Sandbox can decrypt. For more information, see [Condition keys for Nitro Enclaves](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-nitro-enclave.html) in the *AWS Key Management Service Developer Guide*.

The following procedure uses an AWS KMS key. If you need a new key, use the [create-key](https://docs.aws.amazon.com/cli/latest/reference/kms/create-key.html) command, which prints the ARN of the key.

```
aws kms create-key --description "{{Nitro Sandbox secrets}}" \
    --query KeyMetadata.Arn --output text
```

**To release a secret only to an attested Nitro Sandbox**

1. Save the key policy of your AWS KMS key as `policy.json`, and add the following statement to its `Statement` array.

   ```
   aws kms get-key-policy \
       --key-id {{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}} \
       --policy-name default \
       --query Policy \
       --output text > policy.json
   ```

   ```
   {
       "Sid": "AllowDecryptFromAttestedNitroSandbox",
       "Effect": "Allow",
       "Principal": {
           "AWS": "arn:aws:iam::{{111122223333}}:role/{{parent-instance-role}}"
       },
       "Action": [
           "kms:Decrypt",
           "kms:GenerateDataKey"
       ],
       "Resource": "*",
       "Condition": {
           "StringEqualsIgnoreCase": {
               "kms:RecipientAttestation:PCR0": "{{PCR0_value}}",
               "kms:RecipientAttestation:PCR3": "{{PCR3_value}}"
           }
       }
   }
   ```

   The statement allows the role of the parent instance to decrypt and to create data keys only for a Nitro Sandbox that runs the expected image on a parent instance with the expected IAM role. Replace the PCR values with the values from [Compute the expected PCR values](#nitro-sandboxes-attestation-expected). Use the `kms:RecipientAttestation:PCR{{N}}` condition keys with the `StringEqualsIgnoreCase` operator. The `kms:RecipientAttestation:ImageSha384` condition key compares PCR0. In a key policy, `"Resource": "*"` refers to the AWS KMS key that the policy is attached to, not to all keys.

   Always include PCR0, PCR1, or `kms:RecipientAttestation:ImageSha384` in the condition. PCR3 and PCR4 identify only the parent instance, which also chooses the image that it launches, and they keep their values in debug mode. Make sure that no other policy allows the principal to use the key without the attestation condition.

1. Apply the key policy with the [put-key-policy](https://docs.aws.amazon.com/cli/latest/reference/kms/put-key-policy.html) command. The command replaces the whole policy, so keep the statements that give your key administrators access.

   ```
   aws kms put-key-policy \
       --key-id {{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}} \
       --policy-name default \
       --policy file://policy.json
   ```

1. Encrypt the secret with the AWS KMS key. Use a principal that has `kms:Encrypt` permission, for example on your workstation, and use the [encrypt](https://docs.aws.amazon.com/cli/latest/reference/kms/encrypt.html) command. Then copy `secret.enc` to the parent instance.

   ```
   aws kms encrypt \
       --key-id {{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}} \
       --plaintext fileb://{{secret.txt}} \
       --query CiphertextBlob \
       --output text | base64 --decode > secret.enc
   ```

1. Launch the image that you built in [Compute the expected PCR values](#nitro-sandboxes-attestation-expected), with the `sandbox.json` that you changed there. If the Nitro Sandbox from [Launch a Nitro Sandbox](nitro-sandboxes-run-firecracker.md#nitro-sandboxes-launch) still runs, stop it first, so that it releases the TAP device, and remove its socket file. Run the command in the directory that contains `sandbox.eif`.

   ```
   sudo rm -f {{/run/sandbox/v.sock}}
   sudo firecracker --no-api --config-file sandbox.json
   ```

   Run the commands in the following steps in another terminal on the parent instance.

1. Receive the attestation document. When the Nitro Sandbox connects to port {{N}} of CID 2, Firecracker forwards the connection to the Unix socket `{{uds_path}}_{{N}}` on the parent instance. The following command returns after the Nitro Sandbox has sent the document. The attestation document is not secret.

   ```
   sudo socat -u UNIX-LISTEN:{{/run/sandbox/v.sock}}_5005 CREATE:attestation.bin
   ```

1. Use the [decrypt](https://docs.aws.amazon.com/cli/latest/reference/kms/decrypt.html) command with the attestation document. The parent instance uses its own credentials.

   ```
   aws kms decrypt \
       --key-id {{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}} \
       --ciphertext-blob fileb://secret.enc \
       --recipient KeyEncryptionAlgorithm=RSAES_OAEP_SHA_256,AttestationDocument@=fileb://attestation.bin \
       --query CiphertextForRecipient \
       --output text | base64 --decode > response.cms
   ```

   To create a data key instead, use the [generate-data-key](https://docs.aws.amazon.com/cli/latest/reference/kms/generate-data-key.html) command. The following example keeps both parts of the response. Store `data-key.enc`, so that you can decrypt the data key again later with the decrypt command.

   ```
   aws kms generate-data-key \
       --key-id {{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}} \
       --key-spec AES_256 \
       --recipient KeyEncryptionAlgorithm=RSAES_OAEP_SHA_256,AttestationDocument@=fileb://attestation.bin \
       --query '[CiphertextBlob,CiphertextForRecipient]' \
       --output text > data-key.txt
   cut -f1 data-key.txt | base64 --decode > data-key.enc
   cut -f2 data-key.txt | base64 --decode > response.cms
   ```

1. Send the response to the Nitro Sandbox on port 5006. The init script decrypts it with its private key into `secret.bin`, and then starts your workload. The parent instance can't decrypt the response, because AWS KMS encrypts it to the public key in the attestation document.

   ```
   sudo socat -u OPEN:response.cms UNIX-LISTEN:{{/run/sandbox/v.sock}}_5006
   ```

If the attestation document does not match the key policy, AWS KMS returns an `AccessDeniedException` error.

The Nitro Sandbox can also call AWS KMS itself with the same command, if its guest image contains the AWS Command Line Interface (AWS CLI). For this, the parent instance gives it a network path to the AWS KMS endpoint, such as a network interface with NAT, credentials for the key policy principal, and the Region, for example in the `AWS_REGION` environment variable. The credentials don't need to be secret from the parent instance, because the attestation condition determines whether AWS KMS releases the secret.
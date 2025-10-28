# Create a Linux AMI with custom UEFI Secure

Boot keys

These instructions show you how to create a Linux AMI with UEFI Secure Boot and
custom-made private keys. Amazon Linux supports UEFI Secure Boot starting with AL2023
release 2023.1. For more information, see [UEFI Secure Boot on AL2023](../../../linux/al2023/ug/uefi-secure-boot.md "../../../linux/al2023/ug/uefi-secure-boot.md")
in the _Amazon Linux 2023 User Guide_.

###### Important

The following procedure is intended for **advanced users
only**. You must have sufficient knowledge of SSL and Linux distribution
boot flow to use these procedures.

###### Prerequisites

- The following tools will be used:
  - OpenSSL – [https://www.openssl.org/](https://www.openssl.org/ "https://www.openssl.org/")
  - efivar – [https://github.com/rhboot/efivar](https://github.com/rhboot/efivar "https://github.com/rhboot/efivar")
  - efitools – [https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git/](https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git/ "https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git/")
  - [get-instance-uefi-data](../../../cli/latest/reference/ec2/get-instance-uefi-data.md "../../../cli/latest/reference/ec2/get-instance-uefi-data.md") command

- Your Linux instance must have been launched with a Linux AMI that supports
  UEFI boot mode, and have non-volatile data present.
  Newly created instances without UEFI Secure Boot keys are created in
  `SetupMode`, which allows you to enroll your own keys. Some AMIs come
  preconfigured with UEFI Secure Boot and you cannot change the existing keys. If you
  want to change the keys, you must create a new AMI based on the original AMI.

You have two ways to propagate the keys in the variable store, which are described
in Option A and Option B that follow. Option A describes how to do this from within
the instance, mimicking the flow of real hardware. Option B describes how to create
a binary blob, which is then passed as a base64-encoded file when you create the
AMI. For both options, you must first create the three key pairs, which are used for
the chain of trust.

###### To create a Linux AMI that supports UEFI Secure Boot, first create

the three key pairs, and then complete either Option A or Option B, but not both:

- [Task 1: Create key
  pairs](#uefi-secure-boot-create-three-key-pairs "#uefi-secure-boot-create-three-key-pairs")
- [Task 2 - Option A: Add keys to the variable
  store from within the instance](#uefi-secure-boot-optionA "#uefi-secure-boot-optionA")
- [Task 2 - Option B: Create a binary blob
  containing a pre-filled variable store](#uefi-secure-boot-optionB "#uefi-secure-boot-optionB")

## Task 1: Create key

pairs

UEFI Secure Boot is based on the following three key databases, which are used
in a chain of trust: the platform key (PK), the key exchange key (KEK), and the
signature database (db).¹

You create each key on the instance. To prepare the public keys in a format
that is valid for the UEFI Secure Boot standard, you create a certificate for
each key. `DER` defines the SSL format (binary encoding of a format).
You then convert each certificate into a UEFI signature list, which is the
binary format that is understood by UEFI Secure Boot. And finally, you sign each
certificate with the relevant key.

###### Tasks

- [Prepare to create the
  key pairs](#uefisb-prepare-to-create-key-pairs "#uefisb-prepare-to-create-key-pairs")
- [Key pair 1: Create the platform
  key (PK)](#uefisb-create-key-pair-1 "#uefisb-create-key-pair-1")
- [Key pair 2: Create the key
  exchange key (KEK)](#uefisb-create-key-pair-2 "#uefisb-create-key-pair-2")
- [Key pair 3: Create the signature
  database (db)](#uefisb-create-key-pair-3 "#uefisb-create-key-pair-3")
- [Sign the boot image (kernel)
  with the private key](#uefi-secure-boot-sign-kernel "#uefi-secure-boot-sign-kernel")

### Prepare to create the

key pairs

Before creating the key pairs, create a globally unique identifier (GUID)
to be used in key generation.

1. [Connect to the instance](connect.md "connect.md").
2. Run the following command in a shell prompt.

```
uuidgen --random > GUID.txt
```

### Key pair 1: Create the platform

key (PK)

The PK is the root of trust for UEFI Secure Boot instances. The private PK
is used to update the KEK, which in turn can be used to add authorized keys
to the signature database (db).

The X.509 standard is used for creating the key pair. For information
about the standard, see [X.509](https://en.wikipedia.org/wiki/X.509 "https://en.wikipedia.org/wiki/X.509") on _Wikipedia_.

###### To create the PK

1. Create the key. You must name the variable `PK`.

```
openssl req -newkey rsa:4096 -nodes -keyout PK.key -new -x509 -sha256 -days 3650 -subj "/CN=`Platform key`/" -out PK.crt
```

The following parameters are specified:

    * `-keyout PK.key` – The private key
     file.
    * `-days 3650` – The number of days that
     the certificate is valid.
    * `-out PK.crt` – The certificate that is
     used to create the UEFI variable.
    * `CN=`Platform key``
     – The common name (CN) for the key. You can enter the
     name of your own organization instead of
     `Platform key`.

2. Create the certificate.

```
openssl x509 -outform DER -in PK.crt -out PK.cer
```

3. Convert the certificate into a UEFI signature list.

```
cert-to-efi-sig-list -g "$(< GUID.txt)" PK.crt PK.esl
```

4. Sign the UEFI signature list with the private PK
   (self-signed).

```
sign-efi-sig-list -g "$(< GUID.txt)" -k PK.key -c PK.crt PK PK.esl PK.auth
```

### Key pair 2: Create the key

exchange key (KEK)

The private KEK is used to add keys to the db, which is the list of
authorized signatures to boot on the system.

###### To create the KEK

1. Create the key.

```
openssl req -newkey rsa:4096 -nodes -keyout KEK.key -new -x509 -sha256 -days 3650 -subj "/CN=Key Exchange Key/" -out KEK.crt
```

2. Create the certificate.

```
openssl x509 -outform DER -in KEK.crt -out KEK.cer
```

3. Convert the certificate into a UEFI signature list.

```
cert-to-efi-sig-list -g "$(< GUID.txt)" KEK.crt KEK.esl
```

4. Sign the signature list with the private PK.

```
sign-efi-sig-list -g "$(< GUID.txt)" -k PK.key -c PK.crt KEK KEK.esl KEK.auth
```

### Key pair 3: Create the signature

database (db)

The db list contains authorized keys that are authorized to be booted on
the system. To modify the list, the private KEK is necessary. Boot images
will be signed with the private key that is created in this step.

###### To create the db

1. Create the key.

```
openssl req -newkey rsa:4096 -nodes -keyout db.key -new -x509 -sha256 -days 3650 -subj "/CN=Signature Database key/" -out db.crt
```

2. Create the certificate.

```
openssl x509 -outform DER -in db.crt -out db.cer
```

3. Convert the certificate into a UEFI signature list.

```
cert-to-efi-sig-list -g "$(< GUID.txt)" db.crt db.esl
```

4. Sign the signature list with the private KEK.

```
sign-efi-sig-list -g "$(< GUID.txt)" -k KEK.key -c KEK.crt db db.esl db.auth
```

### Sign the boot image (kernel)

with the private key

For Ubuntu 22.04, the following images require signatures.

```
/boot/efi/EFI/ubuntu/shimx64.efi
/boot/efi/EFI/ubuntu/mmx64.efi
/boot/efi/EFI/ubuntu/grubx64.efi
/boot/vmlinuz
```

###### To sign an image

Use the following syntax to sign an image.

```
sbsign --key db.key --cert db.crt --output `/boot/vmlinuz` `/boot/vmlinuz`
```

###### Note

You must sign all new kernels.
`/boot/vmlinuz` will usually
symlink to the last installed kernel.

Refer to the documentation for your distribution to find out about your
boot chain and required images.

¹ Thanks to the ArchWiki community for all of the work they have done. The commands for creating the PK, creating the KEK,
creating the DB, and signing the image are from [Creating keys](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot#Creating_keys "https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot#Creating_keys"), authored by the ArchWiki Maintenance Team and/or the ArchWiki contributors.

## Task 2 - Option A: Add keys to the variable

store from within the instance

After you have created the [three
key pairs](#uefi-secure-boot-create-three-key-pairs "#uefi-secure-boot-create-three-key-pairs"), you can connect to your instance and add the keys to the
variable store from within the instance by completing the following steps.
Alternatively, complete the steps in [Task 2 - Option B: Create a binary blob
containing a pre-filled variable store](#uefi-secure-boot-optionB "#uefi-secure-boot-optionB").

###### Option A steps:

- [Step 1: Launch an instance that will
  support UEFI Secure Boot](#step1-launch-uefi-sb "#step1-launch-uefi-sb")
- [Step 2: Configure an instance to
  support UEFI Secure Boot](#step2-launch-uefi-sb "#step2-launch-uefi-sb")
- [Step 3: Create an AMI from the
  instance](#step3-launch-uefi-sb "#step3-launch-uefi-sb")

### Step 1: Launch an instance that will

support UEFI Secure Boot

When you [launch an
instance](LaunchingAndUsingInstances.md "LaunchingAndUsingInstances.md") with the following prerequisites, the instance will then
be ready to be configured to support UEFI Secure Boot. You can only enable
support for UEFI Secure Boot on an instance at launch; you can't enable it
later.

###### Prerequisites

- **AMI** – The Linux AMI must support UEFI boot
  mode. To verify that the AMI supports UEFI boot mode, the AMI boot
  mode parameter must be **uefi**. For
  more information, see [Determine the boot mode parameter of an Amazon EC2 AMI](ami-boot-mode.md "ami-boot-mode.md").

Note that AWS only provides Linux AMIs configured to support UEFI
for Graviton-based instance types. AWS currently does not provide
x86_64 Linux AMIs that support UEFI boot mode. You can configure
your own AMI to support UEFI boot mode for all architectures. To
configure your own AMI to support UEFI boot mode, you must perform a
number of configuration steps on your own AMI. For more information,
see [Set the boot mode of an Amazon EC2 AMI](set-ami-boot-mode.md "set-ami-boot-mode.md").

- **Instance type** – All
  virtualized instance types that support UEFI also support UEFI
  Secure Boot. Bare metal instance types do not support UEFI Secure
  Boot. For the instance types that support UEFI Secure Boot, see
  [Requirements for UEFI boot mode](launch-instance-boot-mode.md "launch-instance-boot-mode.md").
- Launch your instance after the release of UEFI Secure Boot. Only
  instances launched after May 10, 2022 (when UEFI Secure Boot was
  released) can support UEFI Secure Boot.

After you’ve launched your instance, you can verify that it is ready to be
configured to support UEFI Secure Boot (in other words, you can proceed to
[Step 2](#step2-launch-uefi-sb "#step2-launch-uefi-sb")) by checking whether
UEFI data is present. The presence of UEFI data indicates that non-volatile
data is persisted.

###### To verify whether your instance is ready for Step 2

Use the [get-instance-uefi-data](../../../cli/latest/reference/ec2/get-instance-uefi-data.md "../../../cli/latest/reference/ec2/get-instance-uefi-data.md") command and
specify the instance ID.

```
aws ec2 get-instance-uefi-data --instance-id `i-1234567890abcdef0`
```

The instance is ready for Step 2 if UEFI data is present in the output. If
the output is empty, the instance cannot be configured to support UEFI
Secure Boot. This can happen if your instance was launched before UEFI
Secure Boot support became available. Launch a new instance and try
again.

### Step 2: Configure an instance to

support UEFI Secure Boot

#### Enroll the key pairs in your

UEFI variable store on the instance

###### Warning

You must sign your boot images _after_ you enroll the keys, otherwise you won’t be
able to boot your instance.

After you create the signed UEFI signature lists (`PK`,
`KEK`, and `db`), they must be enrolled into
the UEFI firmware.

Writing to the `PK` variable is possible only if:

- No PK is enrolled yet, which is indicated if the
  `SetupMode` variable is `1`. Check
  this by using the following command. The output is either
  `1` or `0`.

```
efivar -d -n 8be4df61-93ca-11d2-aa0d-00e098032b8c-SetupMode
```

- The new PK is signed by the private key of the existing
  PK.

###### To enroll the keys in your UEFI variable store

The following commands must be run on the instance.

If SetupMode is enabled (the value is `1`), the keys can be
enrolled by running the following commands on the instance:

```
`[ec2-user ~]$` efi-updatevar -f db.auth db
```

```
`[ec2-user ~]$` efi-updatevar -f KEK.auth KEK
```

```
`[ec2-user ~]$` efi-updatevar -f PK.auth PK
```

###### To verify that UEFI Secure Boot is enabled

To verify that UEFI Secure Boot is enabled, follow the steps in [Verify whether an Amazon EC2 instance is enabled for
UEFI Secure Boot](verify-uefi-secure-boot.md "verify-uefi-secure-boot.md").

You can now export your UEFI variable store with the [get-instance-uefi-data](../../../cli/latest/reference/ec2/get-instance-uefi-data.md "../../../cli/latest/reference/ec2/get-instance-uefi-data.md") CLI command, or
you continue to the next step and sign your boot images to reboot into a
UEFI Secure Boot-enabled instance.

### Step 3: Create an AMI from the

instance

To create an AMI from the instance, you can use the console or the
`CreateImage` API, CLI, or SDKs. For the console
instructions, see [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md "creating-an-ami-ebs.md"). For the API instructions, see
[CreateImage](../APIReference/API_CreateImage.md "../APIReference/API_CreateImage.md").

###### Note

The `CreateImage` API automatically copies the UEFI variable store of the
instance to the AMI. The console uses the `CreateImage` API.
After you launch instances using this AMI, the instances will have the
same UEFI variable store.

## Task 2 - Option B: Create a binary blob

containing a pre-filled variable store

After you have created the [three
key pairs](#uefi-secure-boot-create-three-key-pairs "#uefi-secure-boot-create-three-key-pairs"), you can create a binary blob containing a pre-filled
variable store containing the UEFI Secure Boot keys. Alternatively, complete the
steps in [Task 2 - Option A: Add keys to the variable
store from within the instance](#uefi-secure-boot-optionA "#uefi-secure-boot-optionA").

###### Warning

You must sign your boot images _before_
you enroll the keys, otherwise you won’t be able to boot your
instance.

###### Option B steps:

- [Step 1: Create
  a new variable store or update an existing one](#uefi-secure-boot-create-or-update-variable "#uefi-secure-boot-create-or-update-variable")
- [Step
  2: Upload the binary blob on AMI creation](#uefi-secure-boot-upload-binary-blob-on-ami-creation "#uefi-secure-boot-upload-binary-blob-on-ami-creation")

### Step 1: Create

a new variable store or update an existing one

You can create the variable store _offline_ without a running instance by using the
python-uefivars tool. The tool can create a new variable store from your
keys. The script currently supports the EDK2 format, the AWS format, and a
JSON representation that is easier to edit with higher-level tooling.

###### To create the variable store offline without a running

instance

1. Download the tool at the following link.

```
https://github.com/awslabs/python-uefivars
```

2. Create a new variable store from your keys by running the
   following command. This will create a base64-encoded binary blob in
   `your_binary_blob`.bin. The tool also
   supports updating a binary blob via the `-I`
   parameter.

```
./uefivars.py -i none -o aws -O `your_binary_blob`.bin -P PK.esl -K KEK.esl --db db.esl --dbx dbx.esl
```

### Step

2: Upload the binary blob on AMI creation

Use [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") to pass your UEFI
variable store data. For the `--uefi-data` parameter, specify
your binary blob, and for the `--boot-mode` parameter,
specify `uefi`.

```
aws ec2 register-image \
    --name uefi_sb_tpm_register_image_test \
    **--uefi-data $(cat `your_binary_blob`.bin)** \
    --block-device-mappings "DeviceName=/dev/sda1,Ebs= {SnapshotId=`snap-0123456789example`,DeleteOnTermination=true}" \
    --architecture x86_64 \
    --root-device-name /dev/sda1 \
    --virtualization-type hvm \
    --ena-support \
    **--boot-mode uefi**
```

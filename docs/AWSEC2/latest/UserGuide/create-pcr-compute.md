# Compute PCR measurements for a custom AMI

The `nitro-tpm-pcr-compute` utility enables you to generate the reference measurements
for an Attestable AMI during build time based on its Unified Kernel Image (UKI).

The sample Amazon Linux 2023 image description automatically installs the utility in the built image in
the `/usr/bin/` directory. The sample image description also includes a script with the
commands needed to run the utility to generate the reference measurements during image build time. If you are using
the sample image description, you don't need to install the utility or run it manually. For more
information, see [Build the sample Amazon Linux 2023 image description](build-sample-ami.md "build-sample-ami.md").

## Install the `nitro-tpm-pcr-compute` utility

If you are using Amazon Linux 2023, you can install the `nitro-tpm-pcr-compute` utility
from the Amazon Linux repository as follows.

```
sudo yum install aws-nitro-tpm-tools
```

The tools are installed in the `/usr/bin` directory.

## Use the `nitro-tpm-pcr-compute` utility

The utility provides a single command, `nitro-tpm-pcr-compute`, for generating
the reference measurements.

When you run the command, you must specify the following:

- Unified kernel image (`UKI.efi`) — Required for Standard boot and UEFI.

###### To generate the reference measurements for an Attestable AMI:

Use the following command and parameters:

```
/usr/bin/nitro-tpm-pcr-compute \
--image `UKI.efi`
```

The utility returns the reference measurements in the following JSON format:

```
{
  "Measurements": {
    "HashAlgorithm": "SHA384 { ... }",
    "PCR4": "`PCR4_measurement`",
    "PCR7": "`PCR7_measurement`"
  }
}
```

For a practical example of how to use the `nitro-tpm-pcr-compute` utility,
see the `edit_boot_install.sh` script included in the [sample Amazon Linux 2023 image description](build-sample-ami.md "build-sample-ami.md").

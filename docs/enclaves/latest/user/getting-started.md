# Getting started with the Hello Enclaves sample application

The following tutorial walks you through the basics of using AWS Nitro Enclaves. It shows you how to
launch an enclave-enabled parent instance, how to build an enclave image file, how to validate that
an enclave is running, and how to terminate an enclave when it is no longer needed.

The tutorial uses the _Hello Enclaves_ sample application.

###### Important

The steps for Windows and Linux parent instances are mostly similar. However, the
`nitro-cli build-enclave` command referenced in **Step 2: Build
the enclave image file** is not supported on Windows instances. If you are using a
Windows instance, you must complete this step on a Linux instance and then transfer the enclave
image file (`.eif`) to your Windows parent instance before continuing with the
remainder of the tutorial.

###### Steps

- [Step 1: Prepare the enclave-enabled parent instance](#launch-instance "#launch-instance")
- [Step 2: Build the enclave image file](#build "#build")
- [Step 3: Run the enclave](#run "#run")
- [Step 4: Validate the enclave](#validate "#validate")
- [Step 5: Terminate the enclave](#terminate "#terminate")

## Step 1: Prepare the enclave-enabled parent instance

Launch the parent instance that you will use to create the enclave, and prepare the instance
to run Nitro Enclaves.

###### To prepare the parent instance

1. Launch the instance using the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command and set the `--enclave-options` parameter to `true`.
   At a minimum, you must also specify a Windows or Linux AMI and a supported instance type. For more
   information, see [Requirements](nitro-enclave.md#nitro-enclave-reqs "nitro-enclave.md#nitro-enclave-reqs").

The following example command launches an `m5.xlarge` instance using the Amazon Linux 2 Kernel
5.10 AMI.

```
`$` `aws ec2 run-instances \
--image-id `ami-0b5eea76982371e91` \
--count 1 \
--instance-type `m5.xlarge` \
--key-name `your_key_pair` \
--enclave-options 'Enabled=true'`
```

2. Connect to the parent instance. For more information about connecting to an instance, see
   the following topics in the _Amazon EC2 User Guide_.
   - [Connect to your Linux instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md")
   - [Connect to your Windows instance](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md")

3. Install the AWS Nitro Enclaves CLI on the parent instance.
   - If you are using a Linux parent instance, you must preallocate the memory and vCPUs. For
     the purposes of this tutorial, you must preallocate at least 2 vCPUs and 512 MiB of memory.
     For more information, see [Install the Nitro Enclaves CLI on Linux](nitro-enclave-cli-install.md "nitro-enclave-cli-install.md").
   - If you are using a Windows parent instance, see [Install the Nitro Enclaves CLI on
     Windows](nitro-enclave-cli-install-win.md "nitro-enclave-cli-install-win.md").

## Step 2: Build the enclave image file

###### Important

Only Linux-based operating systems can run inside an enclave. Therefore, you must use a Linux instance to
build your enclave image file `.eif`. As a result of this, the `nitro-cli build-enclave`
command referenced in this section is not supported on Windows instances. If you are using a Windows parent
instance, you must complete this step on a Linux instance and then transfer the resulting enclave image file
(`.eif`) to your Windows parent instance.

In this case, you must launch a temporary Linux instance and install the AWS Nitro Enclaves CLI on that
instance. For more information, see [Install the Nitro Enclaves CLI on Linux](nitro-enclave-cli-install.md "nitro-enclave-cli-install.md").

After you have launched the temporary Linux instance and you have installed the AWS Nitro Enclaves CLI,
connect to that instance and perform the steps described here. After you have completed the steps, transfer
the enclave image file (`.eif`) to your Windows parent instance, reconnect to your Windows
parent instance and continue with **Step 3: Run the enclave**.

The Hello Enclave application is located in the `/usr/share/nitro_enclaves/examples/hello` directory.

###### To build the enclave image file

1. Build a docker image from the application. The following command builds a Docker
   image named `hello` with a tag of `latest`.

```
`$` `docker build /usr/share/nitro_enclaves/examples/hello -t hello`
```

2. Run the following command to verify that the Docker image has been built.

```
`$` `docker image ls`
```

3. Convert the Docker image to an enclave image file by using the [nitro-cli build-enclave](cmd-nitro-build-enclave.md "cmd-nitro-build-enclave.md")
   command. The following command builds an enclave image file named
   `hello.eif`.

```
`$` `nitro-cli build-enclave --docker-uri hello:latest --output-file hello.eif`
```

Example output

```
Start building the Enclave Image...
Enclave Image successfully created.
"Measurements": {
    "HashAlgorithm": "Sha384 { ... }",
    "PCR0": "2bb885ee2104203393c0d2f335f14061a9cd9154e4ede772a6a474d3679348fb33c4917d54fee3f11f9e7a49a0ef305c",
    "PCR1": "aca6e62ffbf5f7deccac452d7f8cee1b94048faf62afc16c8ab68c9fed8c38010c73a669f9a36e596032f0b973d21895",
    "PCR2": "40686da348b450210dcdd234fbb95826ecf81f67e4496b6182ba8eb7ab018977dce07448cd0b7ef44346dc1e283e3e64"
    }
}
```

The `hello.eif` enclave image file has now been built. Note that the command
output includes a set of hashes—`PCR0`, `PCR1`, and
`PCR2`. These hashes are measurements of the enclave image and boot up
process, and they can be used in the attestation process. The attestation process will not be
used in this tutorial.

## Step 3: Run the enclave

You can now use the `hello.eif` enclave image file to run the enclave. In this tutorial,
you will run an enclave with 2 vCPUs and 512 MiB of memory using the `hello.eif` enclave
image file. You will also create the enclave in debug mode.

###### Note

Enclaves booted in debug mode generate attestation documents with PCRs that are made up entirely
of zeros (`000000000000000000000000000000000000000000000000`). These attestation
documents cannot be used for cryptographic attestation.

Use the [nitro-cli run-enclave](cmd-nitro-run-enclave.md "cmd-nitro-run-enclave.md")
command. Specify the vCPUs, memory, and the path to the enclave image file, and include
the `--debug-mode` option.

```
`$` `nitro-cli run-enclave --cpu-count 2 --memory 512 --enclave-cid 16 --eif-path hello.eif --debug-mode`
```

Example output

```
Start allocating memory...
Started enclave with enclave-cid: 16, memory: 512 MiB, cpu-ids: [1, 3]
{
    "EnclaveID": "i-05f6ed443aEXAMPLE-enc173dfe3eEXAMPLE",
    "ProcessID": 7077,
    "EnclaveCID": 16,
    "NumberOfCPUs": 2,
    "CPUIDs": [
        1,
        3
    ],
    "MemoryMiB": 512
}
```

The enclave is now running. In this sample output, the enclave is created with an ID of
`i-05f6ed443aEXAMPLE-enc173dfe3eEXAMPLE`, and an enclave context identifier
(EnclaveCID) of `16`. The EnclaveCID is like an IP address for the local socket (vsock)
between the parent instance and the enclave.

## Step 4: Validate the enclave

Now that you have created the enclave, you can use the [nitro-cli describe-enclaves](cmd-nitro-describe-enclaves.md "cmd-nitro-describe-enclaves.md") command to verify that it is running.

```
`$` `nitro-cli describe-enclaves`
```

```
{
    "EnclaveID": "i-05f6ed443aEXAMPLE-enc173dfe3eEXAMPLE",
    "ProcessID": 7077,
    "EnclaveCID": 16,
    "NumberOfCPUs": 2,
    "CPUIDs": [
        1,
        3
        ],
    "MemoryMiB": 512,
    "State": "RUNNING",
    "Flags": "DEBUG_MODE"
}
```

The command provides information about the enclave, including the enclave ID, number of
vCPUs, amount of memory, and its state. In this case, the enclave is in the
`RUNNING` state.

Additionally, because you created the enclave in debug mode, you can use the [nitro-cli console](cmd-nitro-console.md "cmd-nitro-console.md") command to view the read-only console output of the enclave.

```
`$` `nitro-cli console --enclave-id `i-05f6ed443aEXAMPLE-enc173dfe3eEXAMPLE``
```

Example output

```
Hello from the enclave side!
Hello from the enclave side!
Hello from the enclave side!
```

In this case, the Hello Enclave application is designed to print `Hello from the enclave side!` to
the console every five seconds.

## Step 5: Terminate the enclave

If you no longer need the enclave, you can use the `nitro-cli terminate-enclave`
command to terminate it.

```
`$` `nitro-cli terminate-enclave --enclave-id `i-05f6ed443aEXAMPLE-enc173dfe3eEXAMPLE``
```

Example output

```
Successfully terminated enclave i-05f6ed443aEXAMPLE-enc173dfe3eEXAMPLE.
{
    "EnclaveID": "i-05f6ed443aEXAMPLE-enc173dfe3eEXAMPLE",
    "Terminated": true
}
```

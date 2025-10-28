# Creating an enclave

After your enclave applications have been packaged as an enclave image file
(`.eif`), you are ready to create the enclave.

###### Important

You can build enclave images files using the Nitro CLI on any Linux environment,
including outside of AWS. To manage the lifecycle of an instance—such as with the
`run-enclave` command—you will need to use the Nitro CLI on a
parent instance (EC2 instance with Nitro Enclave enabled).

To create the enclave, you need to do the following:

###### Steps

- [Launch the parent instance](#launch-parent "#launch-parent")
- [Create the enclave](#boot-enclave "#boot-enclave")

## Launch the parent instance

First, you need to launch the parent instance. The parent instance is the instance from
which you allocate the resources for the enclave. You also use this instance to
manage the lifecycle of the enclave. For more information about the supported
instance types and sizes, see [Requirements](nitro-enclave.md#nitro-enclave-reqs "nitro-enclave.md#nitro-enclave-reqs").

After you launch the parent instance, make a note of the instance ID. You'll need it to
generate PCR4, which is needed for attestation. For more information, see [Where to get an enclave's measurements](set-up-attestation.md#where "set-up-attestation.md#where").

Console

###### To launch the parent instance using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Launch instance**.
3. (Optional) Under **Name and tags**, for
   **Name**, enter a descriptive name for your
   instance.
4. Under **Application and OS Images (Amazon Machine Image)**,
   choose **Quick Start**, and then choose the operating system
   (OS) for your instance.
5. Under **Key pair (login)**, for **Key pair
   name**, choose an existing key pair or create a new one.
6. In the **Summary** panel, choose **Launch
   instance**.

AWS CLI

###### To launch a parent instance using the AWS CLI

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command and set the `--enclave-options` parameter to `Enabled=true`.

For example, the following command launches a single `m5.2xlarge` instance
using an AMI with an ID of `ami-12345abcde67890a1` and a key
pair named `my_key`, and it enables Nitro Enclaves.

```
aws ec2 run-instances \
    --image-id `ami-12345abcde67890a1` \
    --count 1 \
    --instance-type `m5.2xlarge` \
    --key-name `my_key` \
    --enclave-options 'Enabled=true'
```

After you launch the parent instance, you must install the AWS Nitro Enclaves CLI and the development tools. If
you're using a Linux parent instance, see [Install the Nitro Enclaves CLI on Linux](nitro-enclave-cli-install.md "nitro-enclave-cli-install.md"). If you're using a Windows parent instance, see
[Install the Nitro Enclaves CLI on
Windows](nitro-enclave-cli-install-win.md "nitro-enclave-cli-install-win.md").

## Create the enclave

After you have launched the parent instance, you can create the enclave using the enclave image
file (`.eif`). When you create the enclave, it boots the enclave application and its
dependencies from the enclave image file into the enclave.

###### Note

You must have the Nitro Enclaves CLI installed on the parent instance in order to create the
enclave. For more information, see [Nitro Enclaves Command Line Interface](nitro-enclave-cli.md "nitro-enclave-cli.md").

###### To create the enclave

On the parent instance, use the [nitro-cli run-enclave](cmd-nitro-run-enclave.md "cmd-nitro-run-enclave.md")
CLI command and, at a minimum, specify the following:

- The number of vCPUs to allocate to the enclave
- The amount of memory (in MiB) to allocate to the enclave
- An enclave image file

For example, the following command creates an enclave with `4` vCPUs,
`1600` MiB of memory, a context ID of `10`, and it uses an
enclave image file named `sample.eif`, which is located in the same
directory from which the command is being run.

```
nitro-cli run-enclave \
    --cpu-count `2` \
    --memory `1600` \
    --eif-path `sample.eif` \
    --enclave-cid `10`
```

The following is example output.

```
Instance CPUs [1, 3] going offline
Started enclave with enclave-cid: 10, memory: 1600 MiB, cpu-ids: [1, 3]
Sending image to cid: 10 port: 7000
{
"EnclaveID": "i-abc12345def67890a-enc9876abcd543210ef12",
"EnclaveCID": 10,
"NumberOfCPUs": 2,
"CPUIDs": [
    1,
    3
],
"MemoryMiB": 1600
}
```

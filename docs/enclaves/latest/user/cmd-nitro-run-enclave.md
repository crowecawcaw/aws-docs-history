# nitro-cli run-enclave

Launches a new enclave. This command partitions the specified number of vCPUs and
the amount of memory from the Amazon EC2 parent instance to create the enclave. You also
need to provide an enclave image file (`.eif`) that contains the
operating system and the applications that you want to run inside the
enclave.

###### Important

If you attempt to start an enclave with an enclave image file that is signed
with a certificate that is no longer valid, the `nitro-cli
 run-enclave` command fails with errors `E36`,
`E39`, and `E11`.

## Syntax

```
nitro-cli run-enclave
    [--enclave-name `enclave_name`]
    [--cpu-count `number_of_vcpus`
    --cpu-ids `list_of_vcpu_ids`]
    --memory `amount_of_memory_in_MiB`
    --eif-path `path_to_enclave_image_file`
    [--enclave-cid `cid_number`]
    [--debug-mode]
    [--attach-console]
```

Alternatively, pass the enclave settings using a JSON file as follows.

```
nitro-cli run-enclave --config `config_file.json`
```

The following is an example JSON file.

```
{
    "enclave_name": `enclave_name`,
    "cpu_count": `number_of_vcpus`,
    "cpu_ids": `list_of_vcpu_ids`,
    "memory_mib": `amount_of_memory_in_MiB`,
    "eif_path": "`path_to_enclave_image_file`",
    "enclave_cid": `cid_number`,
    "debug_mode": `true|false`,
    "attach_console": `true|false`
}
```

## Options

**`--enclave-name`**

A unique name for the enclave. You can use this name to reference
the enclave when using the `nitro-cli console` and
`nitro-cli terminate-enclave` commands.

If you do not specify a name, the name of the enclave image file
(.eif) is used as the enclave name.

Type: String

Required: No

**`--cpu-count`**

The number of vCPUs to allocate to the enclave.

###### Note

- Amazon EC2 instances support multithreading, which enables
  multiple threads to run concurrently on a single CPU
  core. Each thread is represented as a virtual CPU (vCPU)
  on the instance. For more information about vCPUs, see
  [Optimize CPU options](../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md "../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md") in the _Amazon EC2
  User Guide_.
- If the parent instance is enabled for multithreading,
  you must specify an even number of vCPUs.

The number of vCPUs that you can allocate to an enclave depends on
the size and configuration of the parent instance. If the parent
instance is enabled for multithreading, you must leave at least 2
vCPUs for the parent instance. If multithreading is not enabled, you
must leave at least 1 vCPU for the parent instance. For example, if
your parent instance has 4 vCPUs and it is enabled for
multithreading, you can allocate up to 2 vCPUs to the
enclave.

You must specify either `--cpu-count` or
`--cpu-ids`. If you specify this option, omit
`--cpu-ids`.

Type: Integer

Required: Conditional

**`--cpu-ids`**

The IDs of the vCPUs to allocate to the enclave.

###### Note

- Amazon EC2 instances support multithreading, which enables
  multiple threads to run concurrently on a single CPU
  core. Each thread is represented as a virtual CPU (vCPU)
  on the instance. For more information about vCPUs, see
  [Optimize CPU options](../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md "../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md") in the _Amazon EC2
  User Guide_.
- If the parent instance is enabled for multithreading,
  you must specify an even number of vCPUs.

The number of vCPUs that you can allocate to an enclave depends on
the size and configuration of the parent instance. If the parent
instance is enabled for multithreading, you must leave at least 2
vCPUs for the parent instance. If multithreading is not enabled, you
must leave at least 1 vCPU for the parent instance. For example, if
your parent instance has 4 vCPUs and it is enabled for
multithreading, you can allocate up to 2 vCPUs to the
enclave.

You must specify either `--cpu-count` or
`--cpu-ids`. If you specify this option, omit
`--cpu-count`.

Type: String

Required: Conditional

**`--memory`**

The amount of memory (in MiB) to allocate to the enclave.

The amount of memory that you can allocate to an enclave depends
on the size of the parent instance and the applications that you
intend to run on it. The specified amount of memory cannot exceed
the amount of memory provided by the parent instance. You must leave
enough memory for the applications running on the parent instance.
You must allocate a minimum of `64` MiB of memory to the
enclave.

Type: Integer (MiB)

Required: Yes

**`--eif-path`**

The path to the enclave image file.

Type: String

Required: Yes

**`--enclave-cid`**

The context identifier (CID) for the enclave. The CID is the
socket address used by the _vsock_ socket. Only
CIDs of `4` and higher can be specified. If you omit this
option, a random CID is allocated to the enclave.

Type: Integer

Required: No

**`--debug-mode`**

Indicates whether to run the enclave in debug mode. Specify this
option to enable debug mode, or omit it to disable debug
mode.

If you enable debug mode, you can view the enclave's console in
read-only mode using the `nitro-cli console` command.
Enclaves booted in debug mode generate attestation documents with
PCRs that are made up entirely of zeros.

Required: No

**`--attach-console`**

Attach the enclave console immediately after starting the
enclave.

**`--config`**

The path to a .json configuration file that specifies the
parameters for the enclave. If you specify `--config`,
the specified JSON file must include the required and optional
parameters as described above, and you must not specify any other
parameters in the command itself.

Type: String

Required: No

## Output

**`EnclaveName`**

The unique name of the enclave.

Type: String

**`EnclaveID`**

The unique ID of the enclave.

Type: String

**`ProcessID`**

The process identifier (PID) of the process holding the enclave's
resources.

Type: String

**`EnclaveCID`**

The context ID (CID) of the enclave.

Type: Integer

**`NumberOfCPUs`**

The number of vCPUs allocated to the enclave from the parent
instance.

Type: Integer

**`CPUIDs`**

The IDs of the vCPUs allocated to the enclave from the parent
instance.

Type: String

**`MemoryMiB`**

The amount of memory (in MiB) allocated to the enclave from the
parent instance.

Type: Integer

## Examples

### Example 1: Inline parameters

The following example creates an enclave with `2` vCPUs,
`1600` MiB of memory, and a context ID of `10`. It
also uses an enclave image file named `sample.eif`, which is
located in the same directory from which the command is being run.

**Command**

```
nitro-cli run-enclave --enclave-name `my-enclave` --cpu-count `2` --memory `1600` --eif-path `sample.eif` --enclave-cid `10`
```

**Output**

```
Start allocating memory...
Started enclave with enclave-cid: 10, memory: 1600 MiB, cpu-ids: [1, 3]
{
    "EnclaveName": "my_enclave",
    "EnclaveID": "i-abc12345def67890a-enc9876abcd543210ef12",
    "ProcessID": 12345,
    "EnclaveCID": 10,
    "NumberOfCPUs": 2,
    "CPUIDs": [
        1,
        3
    ],
    "MemoryMiB": 1600
}
```

### Example 2: Config file

The following example creates an enclave with `2` vCPUs,
`1600` MiB of memory, and a context ID of `10`. It
also uses an enclave image file named `sample.eif`, which is
located in the same directory from which the command is being run.

**Command**

```
nitro-cli run-enclave --config `enclave_config.json`
```

The following is an example of the `enclave_config.json`
file.

```
{
    "enclave_name": "my_enclave",
    "cpu_count": 2,
    "memory_mib": 1600,
    "eif_path": "sample.eif",
    "enclave_cid": 10,
    "debug_mode": true
}
```

**Output**

```
Start allocating memory...
Started enclave with enclave-cid: 10, memory: 1600 MiB, cpu-ids: [1, 3]
{
    "EnclaveName": "my_enclave",
    "EnclaveID": "i-abc12345def67890a-enc9876abcd543210ef12",
    "ProcessID": 12345,
    "EnclaveCID": 10,
    "NumberOfCPUs": 2,
    "CPUIDs": [
        1,
        3
    ],
    "MemoryMiB": 1600
}

```

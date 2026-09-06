

# nitro-cli describe-enclaves
<a name="cmd-nitro-describe-enclaves"></a>

Describes an enclave.

## Syntax
<a name="cmd-nitro-describe-enclaves-syntax"></a>

```
nitro-cli describe-enclaves
```

## Options
<a name="cmd-nitro-describe-enclaves-options"></a>

This command has no options.

## Output
<a name="cmd-nitro-describe-enclaves-output"></a>

**`EnclaveName`**  
The unique name of the enclave.  
Type: String

**`EnclaveID`**  
The unique ID of the enclave.  
Type: String

**`ProcessID`**  
[Linux parent instances only] The process identifier (PID) of the process holding the enclave's resources.  
Type: String

**`EnclaveCID`**  
The unique context ID (CID) of the enclave. The CID is the socket address used by the *vsock* socket.  
Type: Integer

**`NumberOfCPUs`**  
The number of vCPUs allocated to the enclave from the parent instance.  
Type: Integer

**`CPUIDs`**  
[Linux parent instances only] The IDs of the vCPUs allocated to the enclave from the parent instance.  
Type: Integer

**`MemoryMiB`**  
The amount of memory (in MiB) allocated to the enclave from the parent instance.  
Type: Integer

**`State`**  
The current status of the enclave.  
Possible values: `running` \| `terminating`  
Type: String

**`Flags`**  
Indicates if the enclave is in debug mode. `None` indicates that debug mode is disabled. `Debug` indicates that debug mode is enabled.  
Possible values: `None` \| `Debug`  
Type: String

## Example
<a name="cmd-nitro-describe-enclave-example"></a>

The following example describes an enclave.

**Command**

```
nitro-cli describe-enclaves
```

**Output**

```
[
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
        "MemoryMiB": 1600,
        "State": "RUNNING",
        "Flags": "NONE"
    }
]
```
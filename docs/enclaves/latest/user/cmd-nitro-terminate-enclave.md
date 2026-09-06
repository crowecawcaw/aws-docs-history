

# nitro-cli terminate-enclave
<a name="cmd-nitro-terminate-enclave"></a>

Terminates a specific enclave or all enclaves owned by the current user.

To terminate a specific enclave, specify `--enclave-name` or `--enclave-id`. To terminate all enclaves, specify `--all`.

## Syntax
<a name="cmd-nitro-terminate-enclave-syntax"></a>

```
nitro-cli terminate-enclave 
    [--enclave-id {{enclave_id}}]
    [--enclave-name {{enclave_name}}]
    [--all]
```

## Options
<a name="cmd-nitro-terminate-enclave-options"></a>

**`--enclave-name`**  
The unique name of the enclave to terminate. You must specify either `--enclave-name` or `--enclave-id`.  
Type: String  
Required: Conditional

**`--enclave-id`**  
The unique ID of the enclave to terminate. You must specify either `--enclave-id` or `--enclave-name`.  
Type: String  
Required: Conditional

**`--all`**  
Indicates whether to terminate all of the enclaves owned by the current user. If you specify this option, omit `--enclave-id` and `--enclave-name`.  
Required: No

## Example
<a name="cmd-nitro-terminate-enclave-examples"></a>

### Example: Terminate specific enclave
<a name="cmd-nitro-terminate-enclave-example1"></a>

The following example terminates an enclave with an ID of `i-abc12345def67890a-enc9876abcd543210ef12`.

**Command**

```
nitro-cli terminate-enclave --enclave-id {{i-abc12345def67890a-enc9876abcd543210ef12}}
```

**Output**

```
Successfully terminated enclave i-abc12345def67890a-enc9876abcd543210ef12.
{
  "EnclaveID": "i-abc12345def67890a-enc9876abcd543210ef12",
  "Terminated": true
}
```

### Example: Terminate all running enclaves
<a name="cmd-nitro-terminate-enclave-example2"></a>

The following example terminates all of the enclaves owned by the current user.

**Command**

```
nitro-cli terminate-enclave --all
```

**Output**

```
Successfully terminated enclave i-abc12345def67890a-enc9876abcd543210ef12.
{
  "EnclaveID": "i-abc12345def67890a-enc9876abcd543210ef12",
  "Terminated": true
}
```
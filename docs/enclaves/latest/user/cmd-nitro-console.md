# nitro-cli console

Enters a read-only console for the specified enclave. This enables you to view the
enclave's console output to assist with troubleshooting. You can use this command
only on an enclave that was launched with the `--debug-mode`
option.

## Syntax

```
nitro-cli console
    [--enclave-name `enclave_name`]
    [--enclave-id `enclave_id`]
    [--disconnect-timeout `number_of_seconds`]
```

## Options

**`--enclave-name`**

The unique name of the enclave. You must specify either
`--enclave-name` or `--enclave-id`.

Type: String

Required: Conditional

**`--enclave-id`**

The unique ID of the enclave. You must specify either
`--enclave-id` or `--enclave-name`.

Type: String

Required: Conditional

**`--disconnect-timeout`**

The number of seconds after which to automatically disconnect idle
console sessions.

Type: Integer

Required: No

## Example

The following command enters a read-only console for an enclave with an ID of
`i-05f6ed443ae428c95-enc173dfe3e2b1c87b`. The session
automatically disconnects if the connection is idle for `60`
seconds.

**Command**

```
nitro-cli console --enclave-id `i-05f6ed443ae428c95-enc173dfe3e2b1c87b` --disconnect-timeout `60`
```

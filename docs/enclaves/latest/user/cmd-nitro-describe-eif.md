# nitro-cli describe-eif

Describes the specified enclave image file (`.eif`). The output is a
static description of the enclave image file that includes the enclave image file
version, build measurements, signing certificate information, the result of the CRC
and signature check, and the metadata added at build time.

## Syntax

```
nitro-cli describe-eif
    --eif-path `path_to_enclave_image_file`
```

## Options

**`--eif-path`**

The path to the enclave image file.

Type: String

Required: Yes

## Output

**`Measurements`**

The cryptographic measurements (SHA384 hashes) that are unique to
the enclave image file.

Type: String

## Example

The following example describes an enclave image file named
`sample.eif`.

**Command**

```
nitro-cli describe-eif --eif-path `image.eif`
```

**Output**

```
{
  "Measurements": {
    "HashAlgorithm": "Sha384 { ... }",
    "PCR0": "EXAMPLE59044e337c00068c2c033546641e37aa466b853ca486dd149f641f15071961db2a0827beccea9cade3EXAMPLE",
    "PCR1": "EXAMPLE7783d0c23167299fbe5a69622490a9bdf82e94a0a1a48b0e7c56130c0c1e6555de7c0aa3d7901fbc58EXAMPLE",
    "PCR2": "EXAMPLE4b51589e8374b7f695b4649d1f1e9b528b05ab75a49f9a0a4a1ec36be81280caab0486f660b9207ac0EXAMPLE"
  }
}
```

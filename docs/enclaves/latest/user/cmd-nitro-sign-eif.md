# nitro-cli sign-eif

Signs an existing enclave image file (`.eif`). You must specify a
private key and a signing certificate. For the private key, you can use a KMS key
ARN or a local private key file.

The signature is added to the enclave image file (`.eif`). The
signature is updated if it already exists in the enclave image file.

The command returns a set of measurements (SHA384 hashes) that are unique to the
enclave image file. These measurements are provided in the form of platform
configuration registers (PCRs). The PCRs are used during the enclave's attestation
process. For more information, see [Nitro Enclaves concepts](nitro-enclave-concepts.md "nitro-enclave-concepts.md").

For example, when using Nitro Enclaves with AWS Key Management Service (AWS KMS), you can specify these
PCRs in condition keys for customer managed keys policies. When an application in the enclave
performs an AWS KMS operation, AWS KMS compares the PCRs in the enclave's signed
attestation document with the PCRs specified in the condition keys of the KMS key
policy before allowing the operation.

## Syntax

```
nitro-cli sign-eif
    --eif-path /path/to/eif
    --private-key key
    --signing-certificate certificate.pem
```

## Options

**`--eif-path`**

The path to the enclave image file.

Type: String

Required: Yes

**`--private-key`**

The private key to use to sign the enclave image file. This can be
a KMS key ARN, or a path to a local private key file. Only ECDSA
keys are supported for signing.

Type: String

Required: Yes

**`--signing-certificate`**

The signing key to use to sign the enclave image file.

Type: String

Required: Yes

###### Important

Ensure that the specified certificate is valid. If you start an enclave
with an invalid certificate, then the `nitro-cli run-enclave`
command fails with errors `E36`, `E39`, and
`E11`. For more information, see [Nitro Enclaves CLI error
codes](cli-errors.md "cli-errors.md").

## Output

**`Measurements`**

The cryptographic measurements (SHA384 hashes) that are unique to
the enclave image file. The command output includes an additional
PCR, `PCR8` that can be used in condition keys for KMS
key policies. For more information, see [Where
to get an enclave's measurements](set-up-attestation.md#where "set-up-attestation.md#where").

Type: String

## Example

The following example signs the enclave image file `sample.eif`
with the given KMS key.

**Command**

```
nitro-cli sign-eif --eif-path `sample.eif` --private-key arn:aws:kms:eu-west-1:`123456789321:key/abcdef12-3456-789a-bcde-111122223333` --signing-certificate certificate.pem
```

**Output**

```
Enclave Image successfully signed.{
"Measurements": {
"HashAlgorithm": "Sha384 { ... }",
    "PCR0": "EXAMPLE59044e337c00068c2c033546641e37aa466b853ca486dd149f641f15071961db2a0827beccea9cade3EXAMPLE",
    "PCR1": "EXAMPLE7783d0c23167299fbe5a69622490a9bdf82e94a0a1a48b0e7c56130c0c1e6555de7c0aa3d7901fbc58EXAMPLE",
    "PCR2": "EXAMPLE4b51589e8374b7f695b4649d1f1e9b528b05ab75a49f9a0a4a1ec36be81280caab0486f660b9207ac0EXAMPLE",
    "PCR8": "EXAMPLEdcca7f74398ae152d6ee245d8ac2cd430fb63644b46bf47b7d36b53b91c7597edda2d5df772cc81b72EXAMPLE"
  }
}
```

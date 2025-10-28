# nitro-cli build-enclave

Converts a Docker image into an enclave image file (`.eif`). You can
specify either a local directory containing a Dockerfile, or a Docker image in a
Docker repository.

###### Important

This command is not supported on Windows. If you are using a Windows parent
instance, you must run this command on a Linux computer and then transfer the
enclave image file (`.eif`) to the Windows parent instance.

You can build enclave images files using the Nitro CLI on any Linux environment,
including outside of AWS. To manage the lifecycle of an instance—such as with the
`run-enclave` command—you will need to use the Nitro CLI on a
parent instance (EC2 instance with Nitro Enclave enabled).

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
nitro-cli build-enclave
    --docker-uri `repository`:`tag`
    [--docker-dir `/path_to/dockerfile_directory` ]
    --output-file `file-location`
    [--private-key `key`]
    --signing-certificate `certificate.pem`
    [--name `image_name`]
    [--version `image_version`]
```

## Options

**`--docker-uri`**

The uniform resource identifier (URI) of a Docker image in a
Docker repository. The URI is specified using the
`repository`:`tag` format.

Type: String

Required: Yes

**`--docker-dir`**

The path to a local directory containing a Dockerfile.

Type: String

Required: No

**`--output-file`**

The file name of the enclave image file that is created.

Type: String

Required: Yes

**`--private-key`**

The private key to use to sign the enclave image file. This can be
a KMS key ARN, or a path to a local private key file. For more
information, see [Key
ARN](../../../kms/latest/developerguide/concepts.md#key-id-key-ARN "../../../kms/latest/developerguide/concepts.md#key-id-key-ARN").

Only ECDSA keys are supported for code for signing. If you specify
`--private-key` then you must also specify
`--signing-certificate`. If you specify this
parameter, the command creates a signed enclave image file. The
command output will include an additional PCR, `PCR8`,
which can be used in condition keys for KMS key policies. For more
information, see [Where to get an enclave's measurements](set-up-attestation.md#where "set-up-attestation.md#where").

Type: String

Required: No

**`--signing-certificate`**

The signing key to use to sign the enclave image file. If you
specify `--signing-certificate` then you must also
specify `--private-key`. If you specify these parameters,
the command creates a signed enclave image file. The command output
will include and additional PCR, `PCR8`, which can be
used in condition keys for KMS key policies. For more information,
see [Where to get an enclave's measurements](set-up-attestation.md#where "set-up-attestation.md#where").

###### Important

Ensure that the specified certificate is still valid. If you
attempt to start an enclave with an enclave image file that is
signed with a certificate that is no longer valid, the
`nitro-cli run-enclave` fails with errors
`E36`, `E39`, and
`E11`.

Type: String

Required: No

## Output

**`Measurements`**

The cryptographic measurements (SHA384 hashes) that are unique to
the enclave image file.

Type: String

## Example

The following example converts a Docker image with a URI of
`sample:latest` to an enclave image file named
`sample.eif`.

**Command**

```
nitro-cli build-enclave --docker-uri `sample:latest` --output-file `sample.eif`
```

**Output**

```
Enclave Image successfully created.
{
  "Measurements": {
    "HashAlgorithm": "Sha384 { ... }",
    "PCR0": "EXAMPLE59044e337c00068c2c033546641e37aa466b853ca486dd149f641f15071961db2a0827beccea9cade3EXAMPLE",
    "PCR1": "EXAMPLE7783d0c23167299fbe5a69622490a9bdf82e94a0a1a48b0e7c56130c0c1e6555de7c0aa3d7901fbc58EXAMPLE",
    "PCR2": "EXAMPLE4b51589e8374b7f695b4649d1f1e9b528b05ab75a49f9a0a4a1ec36be81280caab0486f660b9207ac0EXAMPLE"
  }
}
```

The following example converts a Docker image with a URI of
`sample:latest` to an enclave image file named
`sample.eif`, and signs it using a KMS key.

**Command**

```
nitro-cli build-enclave --docker-uri `sample:latest` --output-file `sample.eif --private-key arn:aws:kms:eu-west-1:`123456789321:key/abcdef12-3456-789a-bcde-111122223333` --signing-certificate certificate.pem`
```

**Output**

```
Enclave Image successfully created.{
"Measurements": {
"HashAlgorithm": "Sha384 { ... }",
    "PCR0": "EXAMPLE59044e337c00068c2c033546641e37aa466b853ca486dd149f641f15071961db2a0827beccea9cade3EXAMPLE",
    "PCR1": "EXAMPLE7783d0c23167299fbe5a69622490a9bdf82e94a0a1a48b0e7c56130c0c1e6555de7c0aa3d7901fbc58EXAMPLE",
    "PCR2": "EXAMPLE4b51589e8374b7f695b4649d1f1e9b528b05ab75a49f9a0a4a1ec36be81280caab0486f660b9207ac0EXAMPLE",
    "PCR8": "EXAMPLEdcca7f74398ae152d6ee245d8ac2cd430fb63644b46bf47b7d36b53b91c7597edda2d5df772cc81b72EXAMPLE"
  }
}
```

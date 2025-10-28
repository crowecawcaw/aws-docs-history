# nitro-cli pcr

Returns the platform configuration register (PCR) value for a specified input file
or PEM certificate. You can use this command to identify the files and signing
certificate that were used to sign an enclave by comparing the command output with
PCR values in the enclave's build measurements.

## Syntax

```
nitro-cli pcr
    [--input `path_to_file`]
    [--signing-certificate `path_to_certificate`]
```

## Options

**`--input`**

The path to the file for which to generate the platform
configuration register (PCR) value.

You must specify either `--input` or
`--signing-certificate`.

Type: String

Required: Conditional

**`--signing-certificate`**

The path to the PEM certificate for which to generate PCR8. This
option is used to specifically request the PCR8 value by performing
deserialisation of the certificate and PEM format validation.

You must specify either `--input` or
`--signing-certificate`.

Type: String

Required: Conditional

## Output

**`PCR`**

The platform configuration register (PCR) value for the specified
input file or PEM certificate.

Type: String

## Example

The following example generates the PCR8 value for a PEM certificate named
`cert.pem`.

**Command**

```
nitro-cli pcr --signing-certificate `cert.pem`
```

**Output**

```
{
    "PCR8": "example39de75e8ed2939e95examplea96f2c79eaf5d5ac3bacf2cb76c75a31f9examplef55b29f0acd256b8example"
}
```

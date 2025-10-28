# Attest an Amazon EC2 instance with AMD SEV-SNP

Attestation is a process that allows your instance to prove its state and identity. After
you enable AMD SEV-SNP for your instance, you can request an AMD SEV-SNP attestation report from
the underlying processor. The AMD SEV-SNP attestation report contains a cryptographic hash,
called the launch measurement, of the initial guest memory contents and initial vCPU state.
The attestation report is signed with a VLEK signature that chains back to an AMD root of
trust. You can use the launch measurement included in the attestation report to validate that
the instance is running in a genuine AMD environment and to validate the initial boot code
that was used to launch the instance.

###### Prerequisite

Launch an instance that is enabled for AMD SEV-SNP. For more information, see
[Enable AMD SEV-SNP for an EC2 instance](snp-work-launch.md "snp-work-launch.md").

###### Steps

- [Step 1: Get the attestation report](#snp-att-get-report "#snp-att-get-report")
- [Step 2: Validate the attestation report signature](#snp-att-validate-signature "#snp-att-validate-signature")

## Step 1: Get the attestation report

In this step, you install and build the `snpguest` utility, and then
use it to request the AMD SEV-SNP attestation report and certificates.

1. Connect to your instance.
2. Run the following commands to build the `snpguest` utility
   from the [snpguest repository](https://github.com/virtee/snpguest "https://github.com/virtee/snpguest").

```
`$` git clone https://github.com/virtee/snpguest.git
`$` cd snpguest
`$` cargo build -r
`$` cd target/release
```

3. Generate a request for the attestation report. The utility requests the attestation
   report from the host, and writes it to a binary file with the provided request data.

The following example creates a random request string, and uses it as the request file
(`request-file.txt`). When the command returns the attestation report it's
stored in the file path that you specify (`report.bin`). In this case, the
utility stores the report in the current directory.

```
`$` ./snpguest report `report.bin` `request-file.txt` --random
```

4. Request the certificates from host memory, and store them as PEM files. The
   following example stores the files in the same directory as the `snpguest`
   utility. If certificates already exist in the specified directory, those certificates are
   overwritten.

```
`$` ./snpguest certificates PEM `./`
```

## Step 2: Validate the attestation report signature

The attestation report is signed with a certificate, called the Versioned Loaded Endorsement
Key (VLEK), which is issued by AMD for AWS. In this step, you can validate that the VLEK
certificate is issued by AMD, and that the attestation report is signed by that VLEK certificate.

1. Download the VLEK root of trust certificates from the official AMD website to the
   current directory.

```
`$` sudo curl --proto '=https' --tlsv1.2 -sSf https://kdsintf.amd.com/vlek/v1/Milan/cert_chain -o ./cert_chain.pem
```

2. Use `openssl` to validate that the VLEK certificate is signed by the AMD root
   of trust certificates.

```
`$` sudo openssl verify --CAfile ./cert_chain.pem vlek.pem
```

The following is example output.

```
vlek.pem: OK
```

3. Use the `snpguest` utility to validate that the attestation report is signed
   by the VLEK certificate.

```
`$` ./snpguest verify attestation ./ report.bin
```

The following is example output.

```
Reported TCB Boot Loader from certificate matches the attestation report.
Reported TCB TEE from certificate matches the attestation report.
Reported TCB SNP from certificate matches the attestation report.
Reported TCB Microcode from certificate matches the attestation report.
VEK signed the Attestation Report!
```

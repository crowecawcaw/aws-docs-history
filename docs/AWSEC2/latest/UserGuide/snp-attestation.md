

# Attest an Amazon EC2 instance with AMD SEV-SNP
<a name="snp-attestation"></a>

Attestation is a process that allows your instance to prove its state and identity. After you enable AMD SEV-SNP for your instance, you can request an AMD SEV-SNP attestation report from the underlying processor. The AMD SEV-SNP attestation report contains a cryptographic hash, called the launch measurement, of the initial guest memory contents and initial vCPU state. The attestation report is signed with a VCEK signature (on Dedicated Hosts) or a VLEK signature (on shared tenancy) that chains back to an AMD root of trust. You can use the launch measurement included in the attestation report to validate that the instance is running in a genuine AMD environment and to validate the initial boot code that was used to launch the instance.

**Prerequisite**  
Launch an instance that is enabled for AMD SEV-SNP. For more information, see [Enable AMD SEV-SNP for an EC2 instance](snp-work-launch.md).

**Topics**
+ [Attestation for instances on Dedicated Hosts](#snp-att-dedicated-hosts)
+ [Attestation for instances on shared tenancy](#snp-att-shared-tenancy)

## Attestation for instances on Dedicated Hosts
<a name="snp-att-dedicated-hosts"></a>

Dedicated Hosts use a Versioned Chip Endorsement Key (VCEK), a unique per-chip signing key, to sign the attestation report. You must validate the chain of trust from the VCEK certificate back to AMD's root of trust.

**Note**  
The currently supported processor model is `milan`.

**Prerequisites**  
An instance running on an AMD SEV-SNP enabled Dedicated Host with Git, Cargo, and Perl installed.

### Step 1: Build the snpguest utility
<a name="snp-att-dh-build"></a>

In this step, you install and build the `snpguest` utility, which you use to generate the attestation report, fetch the required certificates, and validate the attestation report.

1. Connect to your instance.

1. Verify the prerequisites are installed.

   ```
   $ perl --version; cargo --version; git --version
   ```

1. Run the following commands to build the `snpguest` utility from the [snpguest repository](https://github.com/virtee/snpguest).

   ```
   $ git clone https://github.com/virtee/snpguest.git
   $ cd snpguest
   $ cargo build -r
   $ cd target/release
   ```

### Step 2: Generate the attestation report
<a name="snp-att-dh-report"></a>

Generate a request for the attestation report. The `snpguest` utility requests the attestation report from the AMD Secure Processor through the host, and writes it to a binary file. The following example creates a random request nonce and stores the report in `report.bin`.

```
$ ./snpguest report {{report.bin}} {{request-file.txt}} --random
```

### Step 3: Fetch and validate the VCEK certificate chain
<a name="snp-att-dh-certs"></a>

The attestation report is signed by the VCEK, which is unique to the AMD chip on your Dedicated Host. You must validate the chain of trust from the VCEK back to AMD's root of trust.

1. Fetch the VCEK certificate from the AMD Key Distribution Service (KDS). The certificate is identified by the chip ID and TCB version from the attestation report.

   ```
   $ ./snpguest fetch vcek pem ./ ./report.bin --processor-model milan
   ```

1. Fetch the AMD root certificates (AMD Root Key (ARK) and AMD SEV Key (ASK)) that form the chain of trust.

   ```
   $ ./snpguest fetch ca PEM ./ milan --endorser vcek
   ```

1. Verify the certificate chain.

   ```
   $ ./snpguest verify certs ./
   ```

   The following is example output.

   ```
   The AMD ARK was self-signed!
   The AMD ASK was signed by the AMD ARK!
   The VCEK was signed by the AMD ASK!
   ```

**Optional:** For additional transparency, you can independently verify the chain by downloading the certificates directly from AMD and using `openssl`.

```
$ curl --proto '=https' --tlsv1.2 -sSf https://kdsintf.amd.com/vcek/v1/Milan/cert_chain -o ./cert_chain.pem
$ openssl verify --CAfile ./cert_chain.pem vcek.pem
```

The following is example output.

```
vcek.pem: OK
```

### Step 4: Validate the attestation report signature
<a name="snp-att-dh-validate"></a>

Verify that the attestation report was signed by the VCEK certificate. This confirms that the report was generated on genuine AMD hardware and has not been tampered with.

```
$ ./snpguest verify attestation ./ report.bin
```

The following is example output.

```
Reported TCB Boot Loader from certificate matches the attestation report.
Reported TCB TEE from certificate matches the attestation report.
Reported TCB SNP from certificate matches the attestation report.
Reported TCB Microcode from certificate matches the attestation report.
VEK signed the Attestation Report!
```

The TCB (Trusted Computing Base) version fields confirm that the firmware versions in the certificate match those reported in the attestation report. The final line confirms the VCEK signed the report.

## Attestation for instances on shared tenancy
<a name="snp-att-shared-tenancy"></a>

Shared tenancy instances use a Versioned Loaded Endorsement Key (VLEK), which is issued by AMD for AWS. You must validate the chain of trust from the VLEK certificate back to AMD's root of trust.

### Step 1: Build the snpguest utility
<a name="snp-att-st-build"></a>

In this step, you install and build the `snpguest` utility, which you use to generate the attestation report, fetch the required certificates, and validate the attestation report.

1. Connect to your instance.

1. Run the following commands to build the `snpguest` utility from the [snpguest repository](https://github.com/virtee/snpguest).

   ```
   $ git clone https://github.com/virtee/snpguest.git
   $ cd snpguest
   $ cargo build -r
   $ cd target/release
   ```

### Step 2: Generate the attestation report
<a name="snp-att-st-report"></a>

Generate a request for the attestation report. The `snpguest` utility requests the attestation report from the host, and writes it to a binary file. The following example creates a random request nonce and stores the report in `report.bin`.

```
$ ./snpguest report {{report.bin}} {{request-file.txt}} --random
```

Request the certificates from host memory, and store them as PEM files.

```
$ ./snpguest certificates PEM {{./}}
```

### Step 3: Fetch and validate the VLEK certificate chain
<a name="snp-att-st-certs"></a>

The attestation report is signed by the VLEK, which is issued by AMD for AWS. You must validate the chain of trust from the VLEK back to AMD's root of trust.

1. Download the VLEK root of trust certificates from the official AMD Key Distribution Service to the current directory.

   ```
   $ sudo curl --proto '=https' --tlsv1.2 -sSf https://kdsintf.amd.com/vlek/v1/Milan/cert_chain -o ./cert_chain.pem
   ```

1. Use `openssl` to validate that the VLEK certificate is signed by the AMD root of trust certificates.

   ```
   $ sudo openssl verify --CAfile ./cert_chain.pem vlek.pem
   ```

   The following is example output.

   ```
   vlek.pem: OK
   ```

### Step 4: Validate the attestation report signature
<a name="snp-att-st-validate"></a>

Verify that the attestation report was signed by the VLEK certificate. This confirms that the report was generated on genuine AMD hardware and has not been tampered with.

```
$ ./snpguest verify attestation ./ report.bin
```

The following is example output.

```
Reported TCB Boot Loader from certificate matches the attestation report.
Reported TCB TEE from certificate matches the attestation report.
Reported TCB SNP from certificate matches the attestation report.
Reported TCB Microcode from certificate matches the attestation report.
VEK signed the Attestation Report!
```
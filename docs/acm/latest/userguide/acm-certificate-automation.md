# AWS Workload Credentials Provider

The AWS Workload Credentials Provider automates the use of [public](acm-exportable-certificates.md "acm-exportable-certificates.md") and [private](export-private.md "export-private.md") TLS certificates
exported from ACM. The provider periodically retrieves certificates and their private
keys, writes them to configured paths, and optionally runs a command to reload dependent
services such as web servers.

###### Tip

For publicly trusted certificates, you can instead use the ACME protocol to automate
issuance and renewal directly on your hosts with industry-standard ACME clients,
without exporting certificates from ACM. For more information, see [ACME certificate automation](acm-acme.md "acm-acme.md").

You can use the Workload Credentials Provider with the following compute
environments:

- Amazon Elastic Compute Cloud (Amazon EC2)
- On-premises servers with AWS credentials
  The Workload Credentials Provider uses IAM role assumption to retrieve
  certificates. It runs natively as a system service on both Linux and Windows under a
  dedicated low-privilege user and writes certificate files with restricted permissions.

###### Important

Only exportable certificates can be used with this provider. For more information, see
[AWS Certificate Manager exportable public certificates](acm-exportable-certificates.md "acm-exportable-certificates.md")
and [Exporting a private certificate](export-private.md "export-private.md").

The AWS Workload Credentials Provider is open source. For source code and contributions,
see the [GitHub repository](https://github.com/aws/aws-workload-credentials-provider "https://github.com/aws/aws-workload-credentials-provider").

## How certificate automation works

The provider uses a scheduler that refreshes each configured certificate on a
fixed interval:

- The refresh interval is 24 hours.
- On each cycle, the provider exports the certificate, compares it against the
  files on disk, and writes new files only if the content has changed.
- When certificate files are updated, the configured
  `refresh_command` runs (for example, to reload NGINX or
  Apache).
- If certificate content hasn't changed, the refresh command is skipped.

The provider performs an initial refresh on every system boot and shortly after
service startup, with a small random jitter to avoid synchronized API calls when
multiple providers start simultaneously across the fleet.

The provider also supports dynamic configuration reload, allowing you to add, remove,
or modify certificates without reinstalling. For more information, see
[Dynamic configuration reload](#acm-cert-automation-reload "#acm-cert-automation-reload").

## Prerequisites

Before you install the provider, ensure you have the following:

- A Linux instance with systemd (Amazon Linux 2023, Ubuntu 20.04+, or
  RHEL 8+)
- Or a Windows instance running Windows Server 2016 or later with
  PowerShell 5.1 or later
- Administrator access to run the installer
- An exportable certificate in ACM
- An IAM role with ACM export permissions (see
  [Required permissions](#acm-cert-automation-permissions "#acm-cert-automation-permissions"))
- AWS credentials available on the instance (instance profile, environment
  variables, or credential file)

## Install the provider

The following table lists download links for pre-built provider binaries. Releases for
Windows are signed. Once you have downloaded the binary for your platform, proceed to running the installer.

| Platform | Architecture | Download URL                                                                                                                                                                                                                                             | Checksum (SHA-256)                                               |
| -------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Linux    | x86-64       | [Download for Linux x86-64 (3.1.1)](https://artifacts.awcp.global.on.aws/3.1.1/x86_64-unknown-linux-gnu/aws-workload-credentials-provider "https://artifacts.awcp.global.on.aws/3.1.1/x86_64-unknown-linux-gnu/aws-workload-credentials-provider")       | 471c1978f8bf63a0aeefb425e974ac3c816c7e04feb302236512eea375160de4 |
| Linux    | Aarch64      | [Download for Linux AArch64 (3.1.1)](https://artifacts.awcp.global.on.aws/3.1.1/aarch64-unknown-linux-gnu/aws-workload-credentials-provider "https://artifacts.awcp.global.on.aws/3.1.1/aarch64-unknown-linux-gnu/aws-workload-credentials-provider")    | 8b09dc4e58b84379f580a9ae179940bcb3de0338421f638a43376bf73380ffb6 |
| Windows  | x86-64       | [Download for Windows x86-64 (3.1.1)](https://artifacts.awcp.global.on.aws/3.1.1/x86_64-pc-windows-msvc/aws-workload-credentials-provider.exe "https://artifacts.awcp.global.on.aws/3.1.1/x86_64-pc-windows-msvc/aws-workload-credentials-provider.exe") | 5fbdac4017e630556b94b90e5ed9ed11be69ac7a47e67655e20181ce990dbe12 |

Linux
On Amazon EC2 and other Linux instances, you can install the provider using
the RPM package (available for AL2023). You can also build and install
from source.

###### Option A: Install the RPM package (AL2023)

1. ###### Install the package

Install the RPM package. The package manager finds the latest
version for you:

```
sudo dnf install aws-workload-credentials-provider
```

The RPM package installs the binary and helper scripts to
`/opt/aws/workload-credentials-provider/`. It creates the
`aws-wcp` service user, then installs and starts the
AWS Secrets Manager and token services. It also stages the ACM
certificate automation service, which you enable in a later
step. 2. ###### Create a configuration file

Create a TOML configuration file with your certificate details. For
examples, see [Configure the provider](#acm-cert-automation-configure "#acm-cert-automation-configure"). 3. ###### Enable certificate automation

Run the ACM setup script with your configuration file to install,
enable, and start the certificate automation service:

```
sudo /opt/aws/workload-credentials-provider/bin/install-acm.sh --config /path/to/your/config.toml
```

The setup script accepts the following options:

    * `--config <file>` – The
     configuration file with ACM certificate entries.
    * `--no-start` – Install the service but
     don't start it.
    * `--no-privileges` – Skip Linux
     capabilities on the service.
    * `--no-sudoers` – Skip sudoers generation
     for refresh commands.

###### Option B: Build and install from source

1. ###### Build the provider from source

Alternatively, you can build the provider from source. Follow the
instructions at [Install Rust](https://www.rust-lang.org/tools/install "https://www.rust-lang.org/tools/install")
on the Rust website to install the Rust toolchain.

```
cargo build --release
```

The executable is at `target/release/aws-workload-credentials-provider`. 2. ###### Create a configuration file

Create a TOML configuration file with your certificate details. For examples,
see [Configure the provider](#acm-cert-automation-configure "#acm-cert-automation-configure"). The installer copies this
file to `/etc/aws-workload-credentials-provider/config.toml` automatically when
you use the `--config` option. 3. ###### Run the installer

Run the install script as root:

```
cd aws_workload_credentials_provider_common/configuration
sudo ./install --config /path/to/your/config.toml
```

4. ###### (Optional) Provide AWS credentials

On Amazon EC2 instances with an attached instance profile, the provider obtains
credentials automatically. For other environments, create a systemd override
file to inject credentials:

```
sudo mkdir -p /etc/systemd/system/aws-workload-credentials-provider-acm.service.d
sudo tee /etc/systemd/system/aws-workload-credentials-provider-acm.service.d/creds.conf > /dev/null <<EOF
[Service]
Environment="AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE"
Environment="AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
Environment="AWS_REGION=us-west-2"
EOF
sudo systemctl daemon-reload
sudo systemctl restart aws-workload-credentials-provider-acm
```

Windows

1. ###### Build the provider from source

Alternatively, you can build the provider from source for Windows.
Follow the instructions at [Install Rust](https://www.rust-lang.org/tools/install "https://www.rust-lang.org/tools/install")
on the Rust website to install the Rust toolchain.

```
cargo build --release
```

The executable is at `target\release\aws-workload-credentials-provider.exe`. 2. ###### Create a configuration file

Create a TOML configuration file with your certificate details. For examples,
see [Configure the provider](#acm-cert-automation-configure "#acm-cert-automation-configure"). The installer copies this
file to `C:\ProgramData\AWS\WorkloadCredentialsProvider\config.toml`
automatically when you use the `-Config` parameter. 3. ###### Run the installer

Run the install script as Administrator:

```
cd aws_workload_credentials_provider_common\configuration
.\install.ps1 -Config C:\path\to\your\config.toml
```

To install without starting the service:

```
.\install.ps1 -Config C:\path\to\your\config.toml -NoStart
```

4. ###### (Optional) Provide AWS credentials

On Amazon EC2 instances with an attached instance profile, the provider obtains
credentials automatically through IMDS. For other environments, set
environment variables for the service through the Windows Registry:

```
$regPath = "HKLM:\SYSTEM\CurrentControlSet\Services\AWSWorkloadCredentialsProvider-ACM"
$envVars = @(
    "AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE",
    "AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    "AWS_REGION=us-west-2"
)
New-ItemProperty -Path $regPath -Name "Environment" -Value $envVars -PropertyType MultiString -Force
Restart-Service AWSWorkloadCredentialsProvider-ACM
```

## Configure the provider

Create a TOML configuration file with your certificate details. The installer copies
this file to `/etc/aws-workload-credentials-provider/config.toml` when you use the
`--config` option.

NGINX

```
[logging]
log_level = "info"
log_to_file = true

[capabilities.acm]
enabled = true

[[capabilities.acm.certificates]]
certificate_arn = "arn:aws:acm:us-west-2:123456789012:certificate/abcd1234-5678-90ab-cdef-EXAMPLE11111"
role_arn = "arn:aws:iam::123456789012:role/ACMExportRole"
certificate_path = "/etc/pki/tls/certs/example.com.crt"
private_key_path = "/etc/pki/tls/private/example.com.key"
chain_path = "/etc/pki/tls/certs/example.com-chain.pem"
refresh_command = "/usr/sbin/nginx -s reload"
```

Apache

```
[logging]
log_level = "info"
log_to_file = true

[capabilities.acm]
enabled = true

[[capabilities.acm.certificates]]
certificate_arn = "arn:aws:acm:us-west-2:123456789012:certificate/abcd1234-5678-90ab-cdef-EXAMPLE11111"
role_arn = "arn:aws:iam::123456789012:role/ACMExportRole"
certificate_path = "/etc/ssl/certs/example.com.crt"
private_key_path = "/etc/ssl/private/example.com.key"
chain_path = "/etc/ssl/certs/example.com-chain.pem"
refresh_command = "/bin/systemctl reload httpd"
```

Apache (Windows)

```
[logging]
log_level = "info"
log_to_file = true

[capabilities.acm]
enabled = true

[[capabilities.acm.certificates]]
certificate_arn = "arn:aws:acm:us-west-2:123456789012:certificate/abcd1234-5678-90ab-cdef-EXAMPLE11111"
role_arn = "arn:aws:iam::123456789012:role/ACMExportRole"
certificate_path = 'C:\Apache24\conf\ssl\example.com.crt'
private_key_path = 'C:\Apache24\conf\ssl\example.com.key'
chain_path = 'C:\Apache24\conf\ssl\example.com-chain.pem'
refresh_command = 'C:\Apache24\bin\httpd.exe -k restart'
```

###### Note

When `chain_path` is omitted, the certificate chain is appended to
the file at `certificate_path` to produce a fullchain file. This is
compatible with web servers that expect a single file containing the certificate
and its chain.

### Dynamic configuration reload

You can update the provider's configuration without reinstalling by running the
`acm reload` command. This validates the new configuration, updates
permissions to match the new certificate paths, and restarts the service.

Certificates removed from the configuration stop being refreshed. New certificates
begin their first export immediately. Each certificate runs as an independent task,
so a failure in one does not affect others.

Linux

```
aws-workload-credentials-provider acm reload --config /path/to/new-config.toml
```

Windows

```
& 'C:\Program Files\AWS\WorkloadCredentialsProvider\bin\aws-workload-credentials-provider.exe' acm reload -Config C:\path\to\new-config.toml
```

## Required permissions

### Base credentials

The provider's base credentials (instance profile or environment) must be able to
assume the role specified in each certificate's `role_arn`:

```
{
    "Effect": "Allow",
    "Action": "sts:AssumeRole",
    "Resource": "arn:aws:iam::123456789012:role/ACMExportRole"
}
```

### Certificate export role

The role specified in `role_arn` requires the following
permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "acm:ExportCertificate",
            "Resource": "arn:aws:acm:us-west-2:123456789012:certificate/*"
        }
    ]
}
```

The role's trust policy must allow the provider's base identity to assume it:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::123456789012:role/EC2InstanceRole"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

### Refresh command permissions (Linux)

On Linux, the provider executes the configured `refresh_command` through
`sudo`. The installer generates a sudoers entry at
`/etc/sudoers.d/aws-workload-credentials-provider` that permits the provider user to run
the exact configured command without a password prompt.

###### Important

Ensure `/etc/sudoers` includes the `/etc/sudoers.d`
directory. The installer warns if this include directive is not present. Without
it, the generated sudoers file has no effect and refresh commands will
fail.

On Windows, the provider triggers the `refresh_command` as a SYSTEM
scheduled task.

## Verify the installation

After installation, verify the provider is running and certificates are being
written:

Linux

1. **Check service status:**

```
sudo systemctl status aws-workload-credentials-provider-acm
```

2. **Review provider logs:**

```
cat /opt/aws/workload-credentials-provider/logs/acm_provider.log
```

3. **Verify certificate files exist:**

```
ls -la /etc/pki/tls/certs/example.com.crt
ls -la /etc/pki/tls/private/example.com.key
```

4. **Validate certificate content:**

```
openssl x509 -in /etc/pki/tls/certs/example.com.crt -noout -subject -dates
```

Windows

1. **Check service status:**

```
Get-Service AWSWorkloadCredentialsProvider-ACM | Format-List Name, Status, StartType
```

2. **Review provider logs:**

```
Get-Content "C:\ProgramData\AWS\WorkloadCredentialsProvider\logs\acm_provider.log" -Tail 20
```

3. **Verify certificate files exist:**

```
Get-Item C:\certs\example.com.crt
Get-Item C:\certs\example.com.key
```

4. **Validate certificate content:**

```
$cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\certs\example.com.crt")
$cert | Select-Object Subject, NotBefore, NotAfter
```

## Configuration reference

| Field                                             | Required | Default | Description                                                                                          |
| ------------------------------------------------- | -------- | ------- | ---------------------------------------------------------------------------------------------------- |
| `logging.log_level`                               | No       | `info`  | Logging verbosity: `debug`, `info`,<br>`warn`, `error`, `none`                                       |
| `logging.log_to_file`                             | No       | `true`  | Write logs to file (`true`) or stdout/stderr<br>(`false`)                                            |
| `capabilities.acm.enabled`                        | No       | `false` | Enable or disable the ACM capability                                                                 |
| `certificates[].certificate_arn`                  | Yes      | —       | ARN of the ACM certificate to export                                                                 |
| `certificates[].role_arn`                         | Yes      | —       | IAM role ARN to assume for the<br>`ExportCertificate` call                                           |
| `certificates[].certificate_path`                 | Yes      | —       | Absolute path to write the certificate file                                                          |
| `certificates[].private_key_path`                 | Yes      | —       | Absolute path to write the private key file                                                          |
| `certificates[].chain_path`                       | No       | —       | Absolute path to write the certificate chain. If omitted, chain is<br>appended to `certificate_path` |
| `certificates[].refresh_command`                  | No       | —       | Command to run after certificate files are updated. Must be an<br>absolute path                      |
| `certificates[].certificate_and_chain_permission` | No       | `0600`  | File permissions for cert and chain files (Linux `mode`<br>format)                                   |
| `certificates[].key_permission`                   | No       | `0600`  | File permissions for the private key file (Linux `mode`<br>format)                                   |

## Logging

On Linux, the provider logs to
`/opt/aws/workload-credentials-provider/logs/acm_provider.log`.

On Windows, the provider logs to
`C:\ProgramData\AWS\WorkloadCredentialsProvider\logs\acm_provider.log`. Service start and
stop events are also recorded in the Windows Application Event Log under the source
`AWSWorkloadCredentialsProvider-ACM`.

**Log rotation** — The provider creates a new log
file when the current file reaches 10 MB, and stores up to five archived log
files.

**AWS service logging** — When the provider
calls `ExportCertificate`, that call is recorded in AWS CloudTrail with a
user agent string containing `aws-workload-credentials-provider`. The provider's internal
operations (scheduler cycles, file writes) appear only in the local log.

You can configure logging with the `log_level` and
`log_to_file` settings. For more information, see
[Configuration reference](#acm-cert-automation-config-reference "#acm-cert-automation-config-reference").

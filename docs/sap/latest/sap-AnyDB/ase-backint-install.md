# Installation

This section provides information to help you install the AWS Backint agent using the AWS Backint for SAP ASE installer.
It also provides information to help you configure the agent, view logs, and get the current agent version.

###### Topics

- [Backint for SAP ASE Installer](#ase-backint-installer "#ase-backint-installer")
- [Verify Authenticity before Installation](#ase-backint-verify-authenticity "#ase-backint-verify-authenticity")
- [Configuration](#ase-backint-configuration "#ase-backint-configuration")

## Backint for SAP ASE Installer

AWS Backint Installer (`install-aws-backint-agent-ase`) is the recommended method for installing AWS Backint Agent for ASE on an Amazon EC2 instance running SAP ASE.

1. Download `install-aws-backint-agent-ase` from Amazon S3.

```
wget https://s3.amazonaws.com/awssap-backint-agent-ase/binary/latest/install-aws-backint-agent-ase
```

2. Verify authenticity of installer. (See section [Verify Authenticity before Installation](#ase-backint-verify-authenticity "#ase-backint-verify-authenticity"))
3. Start installation by running installer as `root`.

The Installer installs AWS Backint Agent in a central directory (`/sybase/shared/aws-backint-agent-ase`).
In addition, symbolic links are created at a database-specific location (e.g., `/sybase/AWS/lib`).
This allows multiple instances of SAP ASE running on the same Amazon EC2 instance to use AWS Backint Agent.

**Installation logs** are written to `install_aws_backint_YYYYMMDD_HHMMSS.log` in the current working directory.

### Interactive Mode

Interactive mode provides a guided installation experience.
You are asked to provide each configuration value before the installation starts.

```
./install-aws-backint-agent-ase
```

### Silent Mode

Silent mode allows for unattended installation without user interaction.
It requires a response file - either created manually, or by running the installer in interactive mode and selecting "Create Response File".

```
./install-aws-backint-agent-ase \
    --mode silent \
    --config-file install-aws-backint-agent-ase-response.rsp
```

#### Example: Response File

```
[DEFAULT]
s3_bucket = my-s3-bucket
s3_bucket_folder = my-backup-folder
s3_sse_kms_arn = arn:aws:kms:us-east-1:111122223333:key/1abcd9b9-ab12-1a2a-1abc-12345abc12a3
s3_sse_kms_enabled = True
aws_account_id = 111122223333
aws_region = us-east-1
sid = AWS
installation_directory = /sybase/shared
binary_location = aws-backint-agent-ase.rpm
verify_agent_binary = True
create_response_file = True
install_action = install
```

### Upgrade

The installer supports upgrading an existing installation of AWS Backint Agent for SAP ASE.
Follow the same steps as in the previous section.
The installer will detect that the currently installed version is lower and perform the upgrade.

In case of issues with the upgrade process, uninstall the existing installation first.

### Uninstall

In case you want to uninstall AWS Backint Agent for SAP ASE.

1. Remove the RPM package using the RPM package manager.

```
rpm -e aws-backint-agent-ase
```

2. Remove the Installation directory.

```
rm -r /sybase/shared/aws-backint-agent-ase
```

3. Remove stale symbolic links in database installation directory.

```
find <install dir>/lib -type l -xtype l -delete
```

## Verify Authenticity before Installation

Files for installing AWS Backint Agent for SAP ASE - the installer (`install-aws-backint-agent-ase`) and the RPM package (`aws-backint-agent-ase.rpm`) - support signature verification.
Use the AWS Backint public key to verify that the downloaded files are original and unmodified.

### Verify Installer

1. Download public key

```
> wget https://s3.amazonaws.com/awssap-backint-agent/binary/public-key/aws-backint-agent.gpg
```

2. Import public key into your GPG keyring

```
> gpg --import aws-backint-agent.gpg

gpg: key 1E65925B: public key "AWS Backint Agent" imported
gpg: Total number processed: 1
gpg: imported: 1 (RSA: 1)
```

Make a note of the key value, as you will need it in the next step. In the preceding example, the key value is 1E65925B. 3. Verify fingerprint

```
> gpg --fingerprint 1E65925B

pub 2048R/1E65925B 2020-03-18
Key fingerprint = BD35 7A5F 1AE9 38A0 213A 82A8 80D8 5C5E 1E65 925B
uid [ unknown] AWS Backint Agent
```

The fingerprint should be equal to the following:

```
BD35 7A5F 1AE9 38A0 213A 82A8 80D8 5C5E 1E65 925B
```

###### Note

If the fingerprint string doesn’t match, don’t install the agent.
Contact Amazon Web Services. 4. Download the signature file `install-aws-backint-agent-ase.sig` of the installer.

```
> wget https://s3.amazonaws.com/awssap-backint-agent-ase/binary/latest/install-aws-backint-agent-ase.sig
```

5. Verify installer (`install-aws-backint-agent-ase`) and signature (`install-aws-backint-agent-ase.sig`).

```
> gpg --verify \
    install-aws-backint-agent-ase.sig \
    install-aws-backint-agent-ase
```

###### Note

If the output includes the phrase BAD signature, check whether you performed the procedure correctly.
If you continue to get this response, contact Amazon Web Services and avoid using the downloaded files.

### Verify RPM package

By default, the installer verifies the signature of the RPM package automatically before installation.
Installation fails if the authenticity of the RPM package - downloaded automatically or manually - fails.

Follow the instructions below to verify the signature manually.

1. Import GPG key into RPM database.

```
> rpm --import aws-backint-agent.gpg
```

2. Verify the signature.

```
> rpm -Kv aws-backint-agent-ase.rpm

aws-backint-agent-ase.rpm:
    Header V3 RSA/SHA1 Signature, key ID 1e65925b: OK
    Header SHA1 digest: OK
    V3 RSA/SHA1 Signature, key ID 1e65925b: OK
    MD5 digest: OK
```

###### Note

If the command fails (return code != 0) or the key ID does not match the key ID of the GPG public key, do not install the RPM package.
Contact Amazon Web Services.

## Configuration

Installing AWS Backint Agent for SAP ASE with the installer creates a configuration file automatically.
The configuration file is located at `/sybase/shared/aws-backint-agent-ase/aws-backint-agent-config.yaml`.
The following tables summarize the configuration parameters added as part of the AWS Backint agent installation process.

### Default Parameters

| Parameter                | Description                                                                                                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `S3BucketAwsRegion`      | AWS Region of your Amazon S3 bucket. For example, `us-east-1``.                                                                                                                                   |
| `S3BucketName`           | Name of the Amazon S3 bucket, where you want to store your SAP ASE backup files. For example, `amzon-s3-demo-bucket`.                                                                             |
| `S3BucketFolder`         | Name of the folder in the Amazon S3 bucket, where you want to store your SAP ASE backup files. For example, `my-folder`.                                                                          |
| `S3BucketOwnerAccountID` | 12-digit AWS account ID of the Amazon S3 bucket owner. For example, `111122223333`                                                                                                                |
| `S3SseEnabled`           | Specifies whether AWS KMS encryption is enabled.                                                                                                                                                  |
| `S3SseKmsArn`            | ARN of the kms-key that AWS Backint agent can use to encrypt the backup files stored in Amazon S3. For example, `arn:aws:kms:<us-east-1>: 111122223333:key/5bfbc9b9-ab12-ab12-a123-11111xxx22xx`. |
| `LogFile`                | Location of the AWS Backint agent log file.                                                                                                                                                       | ### Additional Parameters You can add the following additional parameters to the configuration file. |
| Parameter                | Description                                                                                                                                                                                       | Default value                                                                                        | Allowed values                                                                                    |
| ---                      | ---                                                                                                                                                                                               | ---                                                                                                  | ---                                                                                               |
| `BackupObjectTags`       | Additional S3 object tags.                                                                                                                                                                        | None                                                                                                 | JSON string with the following syntax: `[{Key=string,Value=string},{Key=string,Value=string},…​]` |
| `EnableTagging`          | Enables or disables default object tagging for backups files stored in S3. Tagging helps to identify the AWS Backint version and SAP HANA version used during the backup.                         | `true`                                                                                               | `true`, `false`                                                                                   |
| `LogLevel`               | Logging level for agent logs.                                                                                                                                                                     | `info`                                                                                               | `info`, `debug`                                                                                   |
| `LogRotationFrequency`   | Log file rotation frequency.                                                                                                                                                                      | `never`                                                                                              | `minute`, `hour`, `day`, `never`                                                                  |
| `S3StorageClass`         | S3 storage class that is used for storing backups.                                                                                                                                                | `STANDARD`                                                                                           | `STANDARD`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`                                    |
| `UploadConcurrency`      | Number of Amazon S3 threads that can work in parallel during backup.                                                                                                                              | `100`                                                                                                | `1` to `200`                                                                                      |
| `UploadChannelSize`      | Number of files that can be uploaded in parallel to the S3 bucket during the backups.                                                                                                             | `10`                                                                                                 | `1` to `32`                                                                                       |
| `DownloadConcurrency`    | Number of Amazon S3 threads that can work in parallel during restore.                                                                                                                             | `100`                                                                                                | `1` to `200`                                                                                      |

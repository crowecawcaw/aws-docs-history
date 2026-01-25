# Verify the signature of the AWS Backint agent and installer for SAP HANA

The source file of AWS Backint agent (`aws-backint-agent.tar.gz`) and AWS Backint installer (`install-aws-backint-agent`) supports signature verification. You can use a public key to verify that the downloaded source file and AWS Backint installer are original and unmodified. You can find the AWS Backint installer in your `/tmp` directory or any other location where you have downloaded the installer. You can find the source file (`aws-backint-agent.tar.gz`) of AWS Backint agent under `<installation directory>/aws-backint-agent/package/`.

## Verify the signature

**Automatic signature verification**

To enable automatic signature verification during agent installation, see the parameter descriptions at [Install AWS Backint agent using AWS Backint installer — interactive mode](aws-backint-agent-s3-installing-configuring.md#aws-backint-agent-installer-interactive "aws-backint-agent-s3-installing-configuring.md#aws-backint-agent-installer-interactive") (Step 6k).

**To verify the AWS Backint agent package on a Linux server**

1. Download the public key.

```
$ wget https://s3.amazonaws.com/awssap-backint-agent/binary/public-key/aws-backint-agent.gpg
```

2. (Optional) For AWS GovCloud (US-East) or AWS GovCloud (US-West), download one of the following keys.

```
$ wget https://awssap-backint-agent-us-gov-east-1.s3.us-gov-east-1.amazonaws.com/binary/public-key/aws-backint-agent.gpg
```

```
$ wget https://awssap-backint-agent-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/binary/public-key/aws-backint-agent.gpg
```

3. Import the public key into your keyring.

```
$ gpg --import aws-backint-agent.gpg
gpg: key 1E65925B: public key "{aws} Backint Agent" imported
gpg: Total number processed: 1
gpg: imported: 1 (RSA: 1)
```

Make a note of the key value, as you will need it in the next step. In the preceding example, the key value is `1E65925B`. 4. Verify the fingerprint by running the following command.

```
$ gpg --fingerprint 1E65925B
pub 2048R/1E65925B 2020-03-18
Key fingerprint = BD35 7A5F 1AE9 38A0 213A 82A8 80D8 5C5E 1E65 925B
uid [ unknown] AWS Backint Agent
```

The fingerprint should be equal to the following:

```
BD35 7A5F 1AE9 38A0 213A 82A8 80D8 5C5E 1E65 925B
```

If the fingerprint string doesn’t match, don’t install the agent. Contact Amazon Web Services.

After you have verified the fingerprint, you can use it to verify the signature of the AWS Backint agent binary. 5. Download the signature files for the source file and the installer.

```
$ wget https://s3.amazonaws.com/awssap-backint-agent/binary/latest/aws-backint-agent.sig

$ wget https://s3.amazonaws.com/awssap-backint-agent/binary/latest/install-aws-backint-agent.sig
```

6. (Optional) For AWS GovCloud (US-East) and AWS GovCloud (US-West), download the signature files from one of the following locations.

```
$ wget https://awssap-backint-agent-us-gov-east-1.s3.us-gov-east-1.amazonaws.com/binary/latest/aws-backint-agent.sig

$ wget https://awssap-backint-agent-us-gov-east-1.s3-us-gov-east-1.amazonaws.com/binary/latest/install-aws-backint-agent.sig
```

```
$ wget https://awssap-backint-agent-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/binary/latest/aws-backint-agent.sig

$ wget https://awssap-backint-agent-us-gov-west-1.s3-us-gov-west-1.amazonaws.com/binary/latest/install-aws-backint-agent.sig
```

7. To verify the signature, run `gpg --verify` against the `aws-backint-agent.tar.gz` source file and `install-aws-backint-agent` installer.

```
$ gpg --verify aws-backint-agent.sig aws-backint-agent.tar.gz
gpg: Signature made Fri 08 May 2020 12:24:48 AM UTC using RSA key ID 1E65925B
gpg: Good signature from "AWS Backint Agent" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg: There is no indication that the signature belongs to the owner.
Primary key fingerprint: BD35 7A5F 1AE9 38A0 213A  82A8 80D8 5C5E 1E65 925B

$ gpg --verify install-aws-backint-agent.sig install-aws-backint-agent
gpg: Signature made Fri 08 May 2020 12:15:40 AM UTC using RSA key ID 1E65925B
gpg: Good signature from "AWS Backint Agent" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg: There is no indication that the signature belongs to the owner.
Primary key fingerprint: BD35 7A5F 1AE9 38A0 213A  82A8 80D8 5C5E 1E65 925B
```

If the output includes the phrase `BAD signature`, check whether you performed the procedure correctly. If you continue to get this response, contact Amazon Web Services and avoid using the downloaded files.

###### Note

A key is trusted only if you or someone you trust has signed it. If you receive a warning about trust, this doesn’t mean that the signature is invalid. Instead, it means that you have not verified the public key.

# RPM installation validation

The latest RPM version, MD5 hash validated from RPM, and SHA256 hash using sha256sum are shown below. These values, combined, can be used to validate the RPM version being used for the ground station agent.

## Latest Agent Version

### Version 1.0.3555.0

Release Date: 03/27/2024

RPM Checksums:

- SHA256: `108f3aceb00e5af549839cd766c56149397e448a6e1e1429c89a9eebb6bc0fc1`
- MD5: `65b72fa507fb0af32651adbb18d2e30f`

Changes:

- Add Agent metric for selected executable version during tasking startup.
- Add config file support for avoiding specific executable versions when other versions are available.
- Add network and routing diagnostics.
- Additional security features.
- Fix issue where some metric reporting errors were written to stdout/journal instead of log file.
- Gracefully handle network unreachable socket errors.
- Measure packet loss and latency between source and destination agents.
- Release aws-gs-datapipe version 2.0 to support new protocol features and the ability to transparently upgrade contacts to the new protocol.

## Verify the RPM

Tools that you will need to be able to verify this RPM installation are:

- [sha256sum](https://man7.org/linux/man-pages/man1/sha256sum.1.html "https://man7.org/linux/man-pages/man1/sha256sum.1.html")
- [rpm](https://man7.org/linux/man-pages/man8/rpm.8.html "https://man7.org/linux/man-pages/man8/rpm.8.html")

Both tools come by default on Amazon Linux 2. These tools will help to validate that the RPM you are using is the correct version.
First download the latest RPM from the S3 bucket (see [Download agent](installing-the-agent.md#download-agent "installing-the-agent.md#download-agent") for instructions on downloading the RPM). Once this file is downloaded, there will be a few things to check:

- Calculate the sha256sum of the RPM file. Perform the following action from the command line of the compute instance that you are using:

```

sha256sum aws-groundstation-agent.rpm

```

Take this value and compare it to the table above. This shows that the RPM file that is downloaded is a valid file to use that AWS Ground Station has vended out to customers.
If the hashes do not match, do not install the RPM, and delete it from the compute instance.

- Check the MD5 hash of the file as well, to ensure that the RPM has not been compromised.
  To do this, use the RPM command line tool by running the following command:

```

rpm -Kv ./aws-groundstation-agent.rpm

```

Validate that the MD5 hash listed here is the same as the MD5 hash of the version that is in the table above.
Once both of these hashes have been validated against this table that is listed within AWS Docs, the customer can be
ensured that the RPM that was downloaded and installed is the safe and uncompromised version of the RPM.

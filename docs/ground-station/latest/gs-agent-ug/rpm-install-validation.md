# RPM installation validation

The latest RPM version, MD5 hash validated from RPM, and SHA256 hash using sha256sum are shown below. These values, combined, can be used to validate the RPM version being used for the ground station agent.

## Latest Agent Version

### Version 1.0.4382.0

Release Date: 11/18/2025

RPM Checksums:

- SHA256: `620fd307124f1276194f2faa0104fe0549427ae18e4f5655444f8c30b919c640`
- MD5: `73e06dcad44adaccbe2ab005218abfc7`

Changes:

- Update client retry behavior when server indicates overload.

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

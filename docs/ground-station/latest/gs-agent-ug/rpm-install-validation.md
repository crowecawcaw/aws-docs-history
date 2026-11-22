

# RPM installation validation

The latest RPM version, MD5 hash validated from RPM, and SHA256 hash using sha256sum are shown below. These values, combined, can be used to validate the RPM version being used for the AWS Ground Station Agent.

## Latest Agent Version
<a name="gs-agent-releases-latest"></a>

### Version 1.0.8022.0
<a name="gs-agent-version-1-0-8022-0"></a>

Release Date: 2026-11-17

The Amazon Linux 2023 RPM has the following checksums:
+ SHA256: `1b63585d1d2032118598d8ffcd53e4fde495dd2304f23a405b446c6e43547362`
+ MD5: `18ab683256ed52498147e4bb733a02e8`

The Amazon Linux 2 RPM has the following checksums:
+ SHA256: `442c32f2bea5ce7697ffe729a237d8a74c2013aaea7e563ff9d7ebd0dea4dad9`
+ MD5: `eb3ceacfcc2932272c0bc5f272d4facf`

This version includes the following changes:
+ Support dataflow endpoints whose Elastic IP is on a secondary network interface

## Verify the RPM
<a name="verify-installation"></a>

Tools that you will need to be able to verify this RPM installation are:
+ [sha256sum](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
+ [rpm](https://man7.org/linux/man-pages/man8/rpm.8.html)

Both tools come by default on Amazon Linux 2 and Amazon Linux 2023. These tools will help to validate that the RPM you are using is the correct version. First download the latest RPM from the S3 bucket (see [Download agent](installing-the-agent.md#download-agent) for instructions on downloading the RPM). Once this file is downloaded, there will be a few things to check: 
+  Calculate the sha256sum of the RPM file. Perform the following action from the command line of the compute instance that you are using: 

  ```bash
  sha256sum aws-groundstation-agent.rpm
  ```

   Compare this value to the section of the table above that corresponds to your instance's Linux OS version. A match shows that the RPM you downloaded is a valid file that AWS Ground Station has vended out to customers. If the hashes do not match, do not install the RPM, and delete it from the compute instance. 
+  Check the MD5 hash of the file as well, to ensure that the RPM has not been compromised. To do this, use the RPM command line tool by running the following command: 

  ```bash
  rpm -qp --qf '%{SIGMD5}\n' ./aws-groundstation-agent.rpm
  ```

   Validate that the MD5 hash listed here is the same as the MD5 hash in the section of the table above that corresponds to your instance's Linux OS version. After you validate both hashes against the table in the AWS documentation, you can be confident that the RPM you downloaded and installed is the safe, uncompromised version vended by AWS Ground Station. 
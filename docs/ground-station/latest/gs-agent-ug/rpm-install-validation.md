

# RPM installation validation
<a name="rpm-install-validation"></a>

The latest RPM version, MD5 hash validated from RPM, and SHA256 hash using sha256sum are shown below. These values, combined, can be used to validate the RPM version being used for the AWS Ground Station Agent.

## Latest Agent Version
<a name="gs-agent-releases-latest"></a>

### Version 1.0.5953.0
<a name="gs-agent-version-1-0-5953-0"></a>

Release Date: 06/29/2026

AL2023 RPM Checksums:
+ SHA256: `083eaf4da2095250ab901251446c67b764a574a3cee34c7d2c6d41aa5790ae16`
+ MD5: `76fedce9de360cbb0464986214bcfbc1`

AL2 RPM Checksums:
+ SHA256: `f2905ff0da26473669ac2d3c096b04c8e423166be3e5b1dcf39912a2f6002915`
+ MD5: `c178f0d7f1ad86e0717c7fac2c6edaf2`

Changes:
+ Add support for Amazon Linux 2023

## Verify the RPM
<a name="verify-installation"></a>

Tools that you will need to be able to verify this RPM installation are:
+ [sha256sum](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
+ [rpm](https://man7.org/linux/man-pages/man8/rpm.8.html)

Both tools come by default on Amazon Linux 2 and Amazon Linux 2023. These tools will help to validate that the RPM you are using is the correct version. First download the latest RPM from the S3 bucket (see [Download agent](installing-the-agent.md#download-agent) for instructions on downloading the RPM). Once this file is downloaded, there will be a few things to check: 
+  Calculate the sha256sum of the RPM file. Perform the following action from the command line of the compute instance that you are using: 

  ```
  sha256sum aws-groundstation-agent.rpm
  ```

   Compare this value to the section of the table above that corresponds to your instance's Linux OS version. A match shows that the RPM you downloaded is a valid file that AWS Ground Station has vended out to customers. If the hashes do not match, do not install the RPM, and delete it from the compute instance. 
+  Check the MD5 hash of the file as well, to ensure that the RPM has not been compromised. To do this, use the RPM command line tool by running the following command: 

  ```
  rpm -qp --qf '%{SIGMD5}\n' ./aws-groundstation-agent.rpm
  ```

   Validate that the MD5 hash listed here is the same as the MD5 hash in the section of the table above that corresponds to your instance's Linux OS version. After you validate both hashes against the table in the AWS documentation, you can be confident that the RPM you downloaded and installed is the safe, uncompromised version vended by AWS Ground Station. 
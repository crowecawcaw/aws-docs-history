# Validating the AWS Schema Conversion Tool

installation

There are several ways you can verify the distribution file of AWS SCT. The
simplest is to compare the checksum of the file with the published checksum from AWS. As
an additional level of security, you can use the procedures following to verify the
distribution file, based on the operating system where you installed the file.

This section includes the following topics.

###### Topics

- [Verifying the checksum of the AWS SCT file](#CHAP_Installing.InstallValidation.Checksum "#CHAP_Installing.InstallValidation.Checksum")
- [Verifying the AWS SCT RPM files on Fedora](#CHAP_Installing.InstallValidation.RPM "#CHAP_Installing.InstallValidation.RPM")
- [Verifying the AWS SCT DEB files on Ubuntu](#CHAP_Installing.InstallValidation.DEB "#CHAP_Installing.InstallValidation.DEB")
- [Verifying the AWS SCT MSI file on Microsoft Windows](#CHAP_Installing.InstallValidation.MSI "#CHAP_Installing.InstallValidation.MSI")

## Verifying the checksum of the AWS SCT file

In order to detect any errors that could have been introduced when downloading or
storing the AWS SCT compressed file, you can compare the file checksum with a
value provided by AWS. AWS uses the SHA256 algorithm for the checksum.

###### To verify the AWS SCT distribution file using a checksum

1. Download the AWS SCT distribution file using the links in the Installing
   section. For more information, see [Installing AWS Schema Conversion Tool](CHAP_Installing.md "CHAP_Installing.md").
2. Download the latest checksum file, called [sha256Check.txt](https://d2fk11eyrwr7ob.cloudfront.net/sha256Check.txt "https://d2fk11eyrwr7ob.cloudfront.net/sha256Check.txt"). This file includes the checksums for the
   latest AWS SCT version. For example, the file can appear as follows:

```

Fedora   b4f5f66f91bfcc1b312e2827e960691c269a9002cd1371cf1841593f88cbb5e6
Ubuntu   4315eb666449d4fcd95932351f00399adb6c6cf64b9f30adda2eec903c54eca4
Windows  6e29679a3c53c5396a06d8d50f308981e4ec34bd0acd608874470700a0ae9a23

```

3. Run the SHA256 validation command for your operating system in the directory that contains the
   distribution file. For example, run the following command in Linux.

```
shasum -a 256 aws-schema-conversion-tool-1.0.latest.zip
```

4. Compare the results of the command with the value shown in the sha256Check.txt file. If the
   checksums match, then it is safe to run the distribution file. If the checksums don't match, then
   don't run the distribution file, and
   [contact AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Verifying the AWS SCT RPM files on Fedora

AWS provides another level of validation in addition to the distribution file
checksum. All RPM files in the distribution file are signed by an AWS private key.
The public GPG key can be viewed at [amazon.com.public.gpg-key](https://d2fk11eyrwr7ob.cloudfront.net/aws-dms-team@amazon.com.public.gpg-key "https://d2fk11eyrwr7ob.cloudfront.net/aws-dms-team@amazon.com.public.gpg-key").

###### To verify the AWS SCT RPM files on Fedora

1. Download the AWS SCT distribution file using the links in the Installing section.
2. Verify the checksum of the AWS SCT distribution file.
3. Extract the contents of the distribution file. Locate the RPM file you want to verify.
4. Download GPG public key from [amazon.com.public.gpg-key](https://d2fk11eyrwr7ob.cloudfront.net/aws-dms-team@amazon.com.public.gpg-key "https://d2fk11eyrwr7ob.cloudfront.net/aws-dms-team@amazon.com.public.gpg-key")
5. Import the public key to your RPM DB (make sure you have the appropriate permissions) by using
   the following command:

```
sudo rpm --import aws-dms-team@amazon.com.public.gpg-key
```

6. Check that the import was successful by running the following command:

```
rpm -q --qf "%{NAME}-%{VERSION}-%{RELEASE} \n %{SUMMARY} \n" gpg-pubkey-ea22abf4-5a21d30c
```

7. Check the RPM signature by running the following command:

```
rpm --checksig -v aws-schema-conversion-tool-1.0.`build number`-1.x86_64.rpm
```

## Verifying the AWS SCT DEB files on Ubuntu

AWS provides another level of validation in addition to the distribution file
checksum. All DEB files in the distribution file are signed by a GPG detached
signature.

###### To verify the AWS SCT DEB files on Ubuntu

1. Download the AWS SCT distribution file using the links in the Installing section.
2. Verifying the checksum of the AWS SCT distribution file.
3. Extract the contents of the distribution file. Locate the DEB file you want to verify.
4. Download the detached signature from [aws-schema-conversion-tool-1.0.latest.deb.asc](https://d2fk11eyrwr7ob.cloudfront.net/Ubuntu/signatures/aws-schema-conversion-tool-1.0.latest.deb.asc "https://d2fk11eyrwr7ob.cloudfront.net/Ubuntu/signatures/aws-schema-conversion-tool-1.0.latest.deb.asc").
5. Download the GPG public key from [amazon.com.public.gpg-key](https://d2fk11eyrwr7ob.cloudfront.net/aws-dms-team@amazon.com.public.gpg-key "https://d2fk11eyrwr7ob.cloudfront.net/aws-dms-team@amazon.com.public.gpg-key").
6. Import the GPG public key by running the following command:

```
gpg --import aws-dms-team@amazon.com.public.gpg-key
```

7. Verify the signature by running the following command:

```
gpg --verify aws-schema-conversion-tool-1.0.latest.deb.asc aws-schema-conversion-tool-1.0.`build number`.deb
```

## Verifying the AWS SCT MSI file on Microsoft Windows

AWS provides another level of validation in addition to the distribution file
checksum. The MSI file has a digital signature you can check to ensure it was signed
by AWS.

###### To verify the AWS SCT MSI file on Windows

1. Download the AWS SCT distribution file using the links in the Installing section.
2. Verifying the checksum of the AWS SCT distribution file.
3. Extract the contents of the distribution file. Locate the MSI file you want to verify.
4. In Windows Explorer, right-click the MSI file and select
   **Properties**.
5. Choose the **Digital Signatures** tab.
6. Verify that the digital signature is from Amazon Services LLC.

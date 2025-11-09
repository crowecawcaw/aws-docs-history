# Prerequisites for signing container

images

Before you begin signing, you need to set up an environment that bridges
AWS Signer with Amazon ECR. Complete the following steps.

###### To prepare your signing environment

1. **Prepare the AWS CLI**

Install and configure the latest version of the AWS CLI. For more
information, see [Installing or
updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the
_AWS Command Line Interface User Guide_. 2. **Prepare Amazon ECR**

Have an existing container image stored in an Amazon ECR private repository to
sign. For more information, see [Pushing an
image](../../../AmazonECR/latest/userguide/image-push.md "../../../AmazonECR/latest/userguide/image-push.md") in the _Amazon Elastic Container Registry User Guide_. 3. **Download the container-signing tools**

Two software packages need to be installed in your local environment for
you to sign images:

    * The open source supply chain security program Notation, developed
     by the [Notary
     Project](https://notaryproject.dev/ "https://notaryproject.dev/")
    * The AWS Signer plugin for Notation. You can either use our plugin binary, or our open source library.

Plugin binary
The AWS Signer installer installs both the Notation client and the AWS Signer plugin for Notation. Separate binaries are available to install only the AWS Signer plugin.

The installer includes the following.

    * Notation binary and third party license.
    * AWS Signer plugin binary and third party license.
    * Notation license.
    * Trust store set up with AWS Signer's Notation signing [root certificate](https://d2hvyiie56hcat.cloudfront.net/aws-signer-notation-root.cert "https://d2hvyiie56hcat.cloudfront.net/aws-signer-notation-root.cert").
    * GovCloud trust store and [root certificate](https://d2hvyiie56hcat.cloudfront.net/aws-us-gov-signer-notation-root.cert "https://d2hvyiie56hcat.cloudfront.net/aws-us-gov-signer-notation-root.cert"), for use in the AWS GovCloud (US) Region.
    * A configurable trust policy. For information about configuring the trust policy, see [Locally verify an image after signing](image-verification.md "image-verification.md").

The following table provides the installer and related files for each
supported operating system and architecture. You can download our latest [CHANGELOG](https://d2hvyiie56hcat.cloudfront.net/CHANGELOG "https://d2hvyiie56hcat.cloudfront.net/CHANGELOG") to see the versions of the Notation CLI and plugin included in each installer release.

| Notation binary and AWS Signer Plugin installer files | **Platform**                                                                                                                                                                                                                                             | **Architecture**                                                                                                                                                                                                                                         | Installer for Notation and AWS Signer plugin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | \*_AWS Signer_<br>• plugin binary only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Signature file |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| RPM-based Linux (e.g., Amazon Linux)                  | x86_64                                                                                                                                                                                                                                                   | [aws-signer-notation-cli_amd64.rpm](https://d2hvyiie56hcat.cloudfront.net/linux/amd64/installer/rpm/latest/aws-signer-notation-cli_amd64.rpm "https://d2hvyiie56hcat.cloudfront.net/linux/amd64/installer/rpm/latest/aws-signer-notation-cli_amd64.rpm") | [notation-aws-signer-plugin.zip](https://d2hvyiie56hcat.cloudfront.net/linux/amd64/plugin/latest/notation-aws-signer-plugin.zip "https://d2hvyiie56hcat.cloudfront.net/linux/amd64/plugin/latest/notation-aws-signer-plugin.zip")                                                                                                                                                                                                                                                                                                                                          | [aws-signer-notation-cli_amd64.rpm.sig](https://d2hvyiie56hcat.cloudfront.net/linux/amd64/installer/rpm/latest/aws-signer-notation-cli_amd64.rpm.sig "https://d2hvyiie56hcat.cloudfront.net/linux/amd64/installer/rpm/latest/aws-signer-notation-cli_amd64.rpm.sig")<br>(installer)<br>[notation-aws-signer-plugin.sig](https://d2hvyiie56hcat.cloudfront.net/linux/amd64/plugin/latest/notation-com.amazonaws.signer.notation.plugin.sig "https://d2hvyiie56hcat.cloudfront.net/linux/amd64/plugin/latest/notation-com.amazonaws.signer.notation.plugin.sig")<br>(plugin) |
| arm64                                                 | [aws-signer-notation-cli_arm64.rpm](https://d2hvyiie56hcat.cloudfront.net/linux/arm64/installer/rpm/latest/aws-signer-notation-cli_arm64.rpm "https://d2hvyiie56hcat.cloudfront.net/linux/arm64/installer/rpm/latest/aws-signer-notation-cli_arm64.rpm") | [notation-aws-signer-plugin.zip](https://d2hvyiie56hcat.cloudfront.net/linux/arm64/plugin/latest/notation-aws-signer-plugin.zip "https://d2hvyiie56hcat.cloudfront.net/linux/arm64/plugin/latest/notation-aws-signer-plugin.zip")                        | [aws-signer-notation-cli_arm64.rpm.sig](https://d2hvyiie56hcat.cloudfront.net/linux/arm64/installer/rpm/latest/aws-signer-notation-cli_arm64.rpm.sig "https://d2hvyiie56hcat.cloudfront.net/linux/arm64/installer/rpm/latest/aws-signer-notation-cli_arm64.rpm.sig")<br>(installer)<br>[notation-aws-signer-plugin.sig](https://d2hvyiie56hcat.cloudfront.net/linux/arm64/plugin/latest/notation-com.amazonaws.signer.notation.plugin.sig "https://d2hvyiie56hcat.cloudfront.net/linux/arm64/plugin/latest/notation-com.amazonaws.signer.notation.plugin.sig")<br>(plugin) |
| Debian-based Linux                                    | x86_64                                                                                                                                                                                                                                                   | [aws-signer-notation-cli_amd64.deb](https://d2hvyiie56hcat.cloudfront.net/linux/amd64/installer/deb/latest/aws-signer-notation-cli_amd64.deb "https://d2hvyiie56hcat.cloudfront.net/linux/amd64/installer/deb/latest/aws-signer-notation-cli_amd64.deb") | [notation-aws-signer-plugin.zip](https://d2hvyiie56hcat.cloudfront.net/linux/amd64/plugin/latest/notation-aws-signer-plugin.zip "https://d2hvyiie56hcat.cloudfront.net/linux/amd64/plugin/latest/notation-aws-signer-plugin.zip")                                                                                                                                                                                                                                                                                                                                          | [aws-signer-notation-cli_amd64.deb.sig](https://d2hvyiie56hcat.cloudfront.net/linux/amd64/installer/deb/latest/aws-signer-notation-cli_amd64.deb.sig "https://d2hvyiie56hcat.cloudfront.net/linux/amd64/installer/deb/latest/aws-signer-notation-cli_amd64.deb.sig")<br>(installer)<br>[notation-aws-signer-plugin.sig](https://d2hvyiie56hcat.cloudfront.net/linux/amd64/plugin/latest/notation-com.amazonaws.signer.notation.plugin.sig "https://d2hvyiie56hcat.cloudfront.net/linux/amd64/plugin/latest/notation-com.amazonaws.signer.notation.plugin.sig")<br>(plugin) |
| arm64                                                 | [aws-signer-notation-cli_arm64.deb](https://d2hvyiie56hcat.cloudfront.net/linux/arm64/installer/deb/latest/aws-signer-notation-cli_arm64.deb "https://d2hvyiie56hcat.cloudfront.net/linux/arm64/installer/deb/latest/aws-signer-notation-cli_arm64.deb") | [notation-aws-signer-plugin.zip](https://d2hvyiie56hcat.cloudfront.net/linux/arm64/plugin/latest/notation-aws-signer-plugin.zip "https://d2hvyiie56hcat.cloudfront.net/linux/arm64/plugin/latest/notation-aws-signer-plugin.zip")                        | [aws-signer-notation-cli_arm64.deb.sig](https://d2hvyiie56hcat.cloudfront.net/linux/arm64/installer/deb/latest/aws-signer-notation-cli_arm64.deb.sig "https://d2hvyiie56hcat.cloudfront.net/linux/arm64/installer/deb/latest/aws-signer-notation-cli_arm64.deb.sig")<br>[notation-aws-signer-plugin.sig](https://d2hvyiie56hcat.cloudfront.net/linux/arm64/plugin/latest/notation-com.amazonaws.signer.notation.plugin.sig "https://d2hvyiie56hcat.cloudfront.net/linux/arm64/plugin/latest/notation-com.amazonaws.signer.notation.plugin.sig")<br>(plugin)                |
| macOS                                                 | x86_64                                                                                                                                                                                                                                                   | [aws-signer-notation-cli_amd64.pkg](https://d2hvyiie56hcat.cloudfront.net/darwin/amd64/installer/latest/aws-signer-notation-cli_amd64.pkg "https://d2hvyiie56hcat.cloudfront.net/darwin/amd64/installer/latest/aws-signer-notation-cli_amd64.pkg")       | [notation-aws-signer-plugin.zip](https://d2hvyiie56hcat.cloudfront.net/darwin/amd64/plugin/latest/notation-aws-signer-plugin.zip "https://d2hvyiie56hcat.cloudfront.net/darwin/amd64/plugin/latest/notation-aws-signer-plugin.zip")                                                                                                                                                                                                                                                                                                                                        | Included in the files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| arm64                                                 | [aws-signer-notation-cli_arm64.pkg](https://d2hvyiie56hcat.cloudfront.net/darwin/arm64/installer/latest/aws-signer-notation-cli_arm64.pkg "https://d2hvyiie56hcat.cloudfront.net/darwin/arm64/installer/latest/aws-signer-notation-cli_arm64.pkg")       | [notation-aws-signer-plugin.zip](https://d2hvyiie56hcat.cloudfront.net/darwin/arm64/plugin/latest/notation-aws-signer-plugin.zip "https://d2hvyiie56hcat.cloudfront.net/darwin/arm64/plugin/latest/notation-aws-signer-plugin.zip")                      | Included in the files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Microsoft Windows                                     | x86_64                                                                                                                                                                                                                                                   | [aws-signer-notation-cli.msi](https://d2hvyiie56hcat.cloudfront.net/windows/amd64/installer/latest/aws-signer-notation-cli.msi "https://d2hvyiie56hcat.cloudfront.net/windows/amd64/installer/latest/aws-signer-notation-cli.msi")                       | [notation-aws-signer-plugin.zip](https://d2hvyiie56hcat.cloudfront.net/windows/amd64/plugin/latest/notation-aws-signer-plugin.zip "https://d2hvyiie56hcat.cloudfront.net/windows/amd64/plugin/latest/notation-aws-signer-plugin.zip")                                                                                                                                                                                                                                                                                                                                      | Validate in Explorer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

Open source library
The open source Signer plugin is available as a library for use with your toolchain to generate and verify container artifacts signatures. Access the source code and instructions to build the Signer plugin in the [Signer Notation plugin Github repository](https://github.com/aws/aws-signer-notation-plugin "https://github.com/aws/aws-signer-notation-plugin"). 4. **(Optional) Verify signed packages.**

For instructions to complete this step, select the tab for your
platform.

Linux

    1. Download the public key.



    ```
    `$` **​wget https://d2hvyiie56hcat.cloudfront.net/linux/public.key**
    ```
    2. Import the public key into your keyring. If you're using the unzip the AWS Signer plugin, first unzip downloaded file and then run command against the binary file within the zip file.



    ```
    `$`  **gpg --import public.key**
    gpg: key A3B52DA65461CF90: public key "AWS Signer Notation" imported
    gpg: Total number processed: 1
    gpg:               imported: 1
    ```

    ​Make a note of the key value, as you need it in the
     next step. In the preceding example, the key value is
     `A3B52DA65461CF90`.
    3. Verify the fingerprint by running the following
     command, replacing **key-value** with the
     value from the preceding step:



    ```
    `$`  **gpg --fingerprint key-value**
    pub   rsa3072 2023-04-24 [SC]
        E84A F8A2 A9B5 2F1F 4435  AE71 A3B5 2DA6 5461 CF90
    uid           [ unknown] AWS Signer Notation​
    ```

    The fingerprint string should be `E84A F8A2 A9B5
     2F1F 4435 AE71 A3B5 2DA6 5461 CF90`.


    If the fingerprint string doesn't match, don't run the
     installer. Contact Amazon Web Services.


    After you have verified the fingerprint, you can use
     it to verify the signature of the AWS Signer Notation
     package.
    4. Download the package signature file using
     **wget**. To determine the correct
     signature file, see the preceding table.



    ```
    `$` **​wget signature-file-link**
    ```
    5. To verify the signature, run gpg --verify:



    ```
    `$`  **gpg --verify sig-filename downloaded-filename**
    gpg: Signature made Mon May 22 16:16:34 2023 PDT
    gpg:                using RSA key A3B52DA65461CF90
    gpg: Good signature from "AWS Signer Notation" [unknown]
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    Primary key fingerprint: E84A F8A2 A9B5 2F1F 4435  AE71 A3B5 2DA6 5461 CF90​
    ```

    If the output includes the phrase *BAD signature*, check
     whether you performed the procedure correctly. If you
     continue to get this response, contact Amazon Web
     Services and avoid using the downloaded file.​


    Note the warning about *trust*. A key is trusted only if you or
     someone who you trust has signed it. This doesn't mean
     that the signature is invalid, only that you have not
     verified the public key.

Windows
To verify the signature of the MSI installer or the plugin EXE
file, using Windows PowerShell run the following command:

```
`C:\>` **​Get-AuthenticodeSignature `filename`**
```

You can also verify the signature by right-clicking on the
file in an Explorer window, choosing
**Properties**, and then choosing
**Digital Signatures**.

​You should see a result similar to the following:​

```
SignerCertificate                         Status             Path
-----------------                         ------             ----
`[40-character hexamecimal number]`         Valid              downloaded-file​​
```

MacOS

    1. To verify the signature of the PKG installer, run the
     following command. This example uses the amd64 package,
     but the signature of the arm64 package can be verified
     similarly.



    ```
    `$` **​pkgutil --check-signature ​aws-signer-notation-cli\_amd64.pkg**
    ```

    You should see a result similar to the
     following:



    ```
    ​Package "aws-signer-notation-cli_amd64.pkg":
        Status: signed by a developer certificate issued by Apple for distribution
        Notarization: trusted by the Apple notary service
        Signed with a trusted timestamp on: 2023-05-19 15:17:15 +0000
        Certificate Chain:
         1. Developer ID Installer: AMZN Mobile LLC (94KV3E626L)
             Expires: 2027-06-28 22:57:06 +0000
             SHA256 Fingerprint:
                  49 68 39 4A BA 83 3B F0 CC 5E 98 3B E7 C1 72 AC 85 97 65 18 B9 4C
                  BA 34 62 BF E9 23 76 98 C5 DA
             ------------------------------------------------------------------------
         2. Developer ID Certification Authority
             Expires: 2031-09-17 00:00:00 +0000
             SHA256 Fingerprint:
                  F1 6C D3 C5 4C 7F 83 CE A4 BF 1A 3E 6A 08 19 C8 AA A8 E4 A1 52 8F
                  D1 44 71 5F 35 06 43 D2 DF 3A
             ------------------------------------------------------------------------
         3. Apple Root CA
             Expires: 2035-02-09 21:40:36 +0000
             SHA256 Fingerprint:
                  B0 B1 73 0E CB C7 FF 45 05 14 2C 49 F1 29 5E 6E DA 6B CA ED 7E 2C
                  68 C5 BE 91 B5 A1 10 01 F0 24​
    ```
    2. To verify the signature of the AWS Signer Notation
     plugin executable, run the following command.



    ```
    `$` **​codesign -dv --verbose=4 ./notation-com.amazonaws.signer.notation.plugin**
    ```

    ​You should see a result similar to the
     following.



    ```
    Executable=/path/to/notation-com.amazonaws.signer.notation.plugin
    Identifier=notation-com.amazonaws.signer.notation.plugin_darwin_arm64
    Format=Mach-O thin (arm64)
    CodeDirectory v=20500 size=74278 flags=0x10000(runtime) hashes=2314+2 location=embedded
    VersionPlatform=1
    VersionMin=720896
    VersionSDK=720896
    Hash type=sha256 size=32
    CandidateCDHash sha256=e4000dbdf4e6243be9d290b1520d95bf9027a5e4
    CandidateCDHashFull sha256=e4000dbdf4e6243be9d290b1520d95bf9027a5e42b699a354fc39ac0f498477f
    Hash choices=sha256
    CMSDigest=e4000dbdf4e6243be9d290b1520d95bf9027a5e42b699a354fc39ac0f498477f
    CMSDigestType=2
    Executable Segment base=0
    Executable Segment limit=3571712
    Executable Segment flags=0x1
    Page size=4096Launch Constraints:None
    CDHash=e4000dbdf4e6243be9d290b1520d95bf9027a5e4
    Signature size=9070
    Authority=Developer ID Application: AMZN Mobile LLC (94KV3E626L)
    Authority=Developer ID Certification Authority
    Authority=Apple Root CATimestamp=May 19, 2023 at 7:51:07 AM
    Info.plist=not bound
    TeamIdentifier=94KV3E626L
    Runtime Version=11.0.0
    Sealed Resources=none
    Internal requirements count=1 size=220
    ```

5. **Install the packages**

For instructions to complete this step, select the tab for your
platform.

Linux (RPM)
If you downloaded an RPM package on a Linux server, change to
the directory containing the package and enter the
following:

```
`$` **​sudo rpm -U `filename`**
```

Linux (DEB)
If you downloaded a DEB package on a Linux server, change to
the directory containing the package and enter the
following:

```
`$` **​sudo dpkg -i -E `filename`**
```

Windows
Install the package with the following command.

```
`C:\>` **msiexec /i `filename`**
```

This command also works from within PowerShell. For more
information, see [Microsoft Standard Installer command-line options](https://learn.microsoft.com/en-us/windows/win32/msi/standard-installer-command-line-options "https://learn.microsoft.com/en-us/windows/win32/msi/standard-installer-command-line-options") in the Microsoft Windows documentation.

MacOS
If you downloaded a PKG package on a macOS server, change to
the directory containing the package and enter the
following:

```
`$` **​sudo installer -pkg `filename` -target /**
```

6. **Verify the package installation**

After downloading and installing the package, to verify the installation
was successful, do the following.

    1. Verify that the Notation directory structure for your operating
     system was created.
    2. Use the following command to display the Notation client
     version.



    ```
    notation version
    ```
    3. Use the following command to list the installed plugins for the
     Notation client and verify that you see the
     `com.amazonaws.signer.notation.plugin` plugin.



    ```
    notation plugin ls
    ```

## Required AWS Identity and Access Management permissions to sign and verify a container image

To sign and verify an image present in Amazon Elastic Container Registry, you need an AWS Identity and Access Management policy that allows Notation to interact with Amazon ECR and Signer.

The following is an example of a user managed policy that allows Notation to interact with Amazon ECR and Signer:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ManageRepositoryContents",
 "Effect": "Allow",
 "Action": [
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage",
 "ecr:CompleteLayerUpload",
 "ecr:DescribeRepositories",
 "ecr:UploadLayerPart",
 "ecr:InitiateLayerUpload",
 "ecr:BatchCheckLayerAvailability",
 "ecr:PutImage"
 ],
 "Resource": "arn:aws:ecr:us-east-1:`111122223333`:repository/`my-repo`"
 },
 {
 "Sid": "GetAuthorizationToken",
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SignAndRevocationCheck",
 "Effect": "Allow",
 "Action": [
 "signer:PutSigningProfile",
 "signer:SignPayload",
 "signer:GetRevocationStatus"
 ],
 "Resource": "*"
 }
 ]
}`

```

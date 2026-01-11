# AWS CloudHSM latest Client SDK release

In March 2021, AWS CloudHSM released Client SDK version 5.0.0, which introduces an
all-new Client SDK with different requirements, capabilities, and platform support.

Client SDK 5 is fully supported for production environments, and offers the same
components and level of support as Client SDK 3. For
more information, see [Compare AWS CloudHSM Client SDK component support](sdk3-compare.md "sdk3-compare.md").

###### Note

Starting CloudHSM SDK 5.17, we are updating our service level agreement to
support up to 3 prior minor versions and one year from the release date of an SDK
version. We will release new versions of the CloudHSM SDK to deliver new features
and for security, stability, performance fixes. We will disable download links for
older and unsupported versions of the CloudHSM SDK as new versions become available.

This section includes the latest version of the Client SDK. For information about previous releases, see [Previous SDK Releases](client-version-previous.md "client-version-previous.md"). For deprecated versions, see [Deprecated SDK Releases](deprecated.md "deprecated.md").

## Client SDK 5 release: Version 5.17.0

Amazon Linux 2023
Download version 5.17.0 software for Amazon Linux 2023 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.17.0-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.17.0-1.amzn2023.x86_64.rpm") (SHA256 checksum e0656d606c1f75b8ecf11df79f2d4aa17c0b68983bb20d271dabe02f7b97ca47)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.17.0-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.17.0-1.amzn2023.x86_64.rpm") (SHA256 checksum b8917abe48799035018bc044fbe2e9db8d5568ebf29663ecc12d53ec2be5efd2)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.17.0-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.17.0-1.amzn2023.x86_64.rpm") (SHA256 checksum 61e49cb0f1f9eb7bcf76f5ef36f01cf1fadfa56bf5eab94b05efdd93214c9cf7)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.17.0-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.17.0-1.amzn2023.x86_64.rpm") (SHA256 checksum 4ba2548fa27f3662c56fc140386366cfb40cde899695412c6d4731a7d0a70e43)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.17.0-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.17.0-1.amzn2023.x86_64.rpm") (SHA256 checksum 0a9de06b3f15d38f3aa02dd0288d3a9ad41f525f692f539664168b9e6b95e18d)

Download version 5.17.0 software for Amazon Linux 2023 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.17.0-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.17.0-1.amzn2023.aarch64.rpm") (SHA256 checksum 9bd40e13bf777a4651721ebe5613cf2e4f0f339679d50f06b81f7f1b73c1fef5)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.17.0-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.17.0-1.amzn2023.aarch64.rpm") (SHA256 checksum e592419bc0449664f0707281a46ebb775091386ac5b297e35ff0e4160468cbe0)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.17.0-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.17.0-1.amzn2023.aarch64.rpm") (SHA256 checksum 46358ef68388928702d780564811814aa826c143ccc0624a2a45d8995226d33e)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.17.0-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.17.0-1.amzn2023.aarch64.rpm") (SHA256 checksum db5bd1494c742a64ca3f2bc57253b17655ad38ecc27d45422965466c1caf740f)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.17.0-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.17.0-1.amzn2023.aarch64.rpm") (SHA256 checksum e3d21b4460a421058f65a597b0bb30a9fdda890363ebee107b124a1212d5a042)

Amazon Linux 2
Download version 5.17.0 software for Amazon Linux 2 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.17.0-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.17.0-1.el7.x86_64.rpm") (SHA256 checksum 17d96d5f4ad25de74fadcc7272fac825d43c496b0b7912e4d32b1ccfb67250bc)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.17.0-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.17.0-1.el7.x86_64.rpm") (SHA256 checksum 3d3de61bd16ef849e53827709b8c8bd9eaf89bd1b7d56b1a02455bca38fe1eb6)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.17.0-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.17.0-1.el7.x86_64.rpm") (SHA256 checksum 5c268313ebf16cf762619a1e75f1d44efdbd6eaf5ba4bbce67ecfe96bbed9775)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.17.0-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.17.0-1.el7.x86_64.rpm") (SHA256 checksum 43b678eff0225590cc59c02645332f4459c8161a6742e562eb95902d1bec9134)

Download version 5.17.0 software for Amazon Linux 2 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.17.0-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.17.0-1.el7.aarch64.rpm") (SHA256 checksum 7910ec55f8b106d804290b77e6d13cefb85ef79cbc728f69bb21eebeb7245c6b)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.17.0-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.17.0-1.el7.aarch64.rpm") (SHA256 checksum 399c16e0fbfa372710a83836517cfeaae0895513931427a458e7994ce91a321d)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.17.0-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.17.0-1.el7.aarch64.rpm") (SHA256 checksum 1678581e31fcfde58625ca1e3c0762c4b96095065a868a5b7f0872214e5ab9e8)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.17.0-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.17.0-1.el7.aarch64.rpm") (SHA256 checksum 52257b580d73d902e9fd29f2c334f88cabee484c7eec8af28f7b2aa7864466e7)

RHEL 10 (10.0+)
Download version 5.17.0 software for RHEL 10 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.17.0-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.17.0-1.el10.x86_64.rpm") (SHA256 checksum 037102ee2b7f9c244d647cfb06da282b99349e208d27b7b0aa80bd32e382a2d4)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.17.0-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.17.0-1.el10.x86_64.rpm") (SHA256 checksum 3d6d97df03a003bae579dabbf9abeefc1bd2fa6d799a6db01c3ef98d02145393)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.17.0-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.17.0-1.el10.x86_64.rpm") (SHA256 checksum 4e69ec89acfefc19f922c68988d4674718d49d5cda2e0a288f7f0343ebfc270c)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.17.0-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.17.0-1.el10.x86_64.rpm") (SHA256 checksum 38a67191949cc8cb0c69ef2fe4694514b2ca6af4cf5f8763bd7f6860c501675a)

Download version 5.17.0 software for RHEL 10 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.17.0-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.17.0-1.el10.aarch64.rpm") (SHA256 checksum bc383aff236d4b2a0fdbc5fd81907cf9212ad8f3cfc91fadeb6cdc14b9d3d581)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.17.0-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.17.0-1.el10.aarch64.rpm") (SHA256 checksum d9ead84f8d2e6a09044646d62fed293ca082431e5e0338bcbbfcf8acd023ecc0)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.17.0-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.17.0-1.el10.aarch64.rpm") (SHA256 checksum c61fdb5f05cf486619deb3e23ecb171ce4485bb64c891bf4480fbe6a4276c3bc)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.17.0-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.17.0-1.el10.aarch64.rpm") (SHA256 checksum fbd4387ef3fab177de8c888d98d1b24bc042d23ea2f93834dfb5ee918518f406)

RHEL 9 (9.2+)
Download version 5.17.0 software for RHEL 9 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.17.0-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.17.0-1.el9.x86_64.rpm") (SHA256 checksum 7fc68025493fc4a0bc4d3b2fd11b17da4481b6bee51fc86a40f95fe4c206aa60)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.17.0-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.17.0-1.el9.x86_64.rpm") (SHA256 checksum 3e786e9218f657c93e1bf1b54c81f0f573e39d10147cf99485da73677b0d67ae)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.17.0-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.17.0-1.el9.x86_64.rpm") (SHA256 checksum c52b366f9c6c960d697794bd7840888bc51e1ee5aa654b8d2c83ec1626797c56)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.17.0-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.17.0-1.el9.x86_64.rpm") (SHA256 checksum 427e9c68815188b59a0f9b2fd14793791d9a4ce4d3e5ddc34fce916af18a45f1)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.17.0-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.17.0-1.el9.x86_64.rpm") (SHA256 checksum 49d128639eea0e588c95281635a33b0e62837cf5a9d992e0bacb5b598a0037ed)

Download version 5.17.0 software for RHEL 9 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.17.0-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.17.0-1.el9.aarch64.rpm") (SHA256 checksum 3ae8f5068abb3d9ca75ac21b160acc7ee84c7ded6107a889602448af51d5bd82)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.17.0-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.17.0-1.el9.aarch64.rpm") (SHA256 checksum 64c5feaf86fc40e28616156f17942cc46d8ac93babdd8af59dd98a1f2e73117d)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.17.0-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.17.0-1.el9.aarch64.rpm") (SHA256 checksum 24df4296ba0ae15f6b7060ccffeca0d1a24f58d9e8da8eb6a4afa3a6a50770fd)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.17.0-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.17.0-1.el9.aarch64.rpm") (SHA256 checksum 648d7948ab8a1271d7cf0eddc2ca32e960979be481b99a1ce2ce8b9fa3a2b2ed)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.17.0-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.17.0-1.el9.aarch64.rpm") (SHA256 checksum edd1f3707aeea285a55cf24d2e2385489458a69e5d7dab4014783f5cdc232d77)

RHEL 8 (8.3+)
Download version 5.17.0 software for RHEL 8 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.17.0-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.17.0-1.el8.x86_64.rpm") (SHA256 checksum 85e070ed3273ead9698711dfc2c3e590dda1a01f99074943459ddc5ac052872d)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.17.0-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.17.0-1.el8.x86_64.rpm") (SHA256 checksum d0c8e5603f4c99d0ba547c0ba40361c15977f3349ac120d514afed59abf32c83)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.17.0-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.17.0-1.el8.x86_64.rpm") (SHA256 checksum 4567b9a236d0dfd0410863beaced6d5d4e71acb06b2b136c7c40ce6e704f3698)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.17.0-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.17.0-1.el8.x86_64.rpm") (SHA256 checksum f8a090752849fac9bf99ef67b59f571e476908dccec1285b466c25e6cc71793c)

Download version 5.17.0 software for RHEL 8 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.17.0-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.17.0-1.el8.aarch64.rpm") (SHA256 checksum 71ade413435947eb2093727cb0e7a5c5f084ca859cb38d728a8c3d23f3b49bd0)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.17.0-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.17.0-1.el8.aarch64.rpm") (SHA256 checksum 02210da06b3fd22813fce8b89b753d150c8f321df405c40dd9f0172dc03968a7)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.17.0-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.17.0-1.el8.aarch64.rpm") (SHA256 checksum 80ac5dbaad1f644d6b9551e6a1d95d4b4a51ae82d34e45593be77b1068f7c910)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.17.0-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.17.0-1.el8.aarch64.rpm") (SHA256 checksum c3c56c3b9fed1dc51761d9412007c727d3b608377a089bd637a44bc374744d5c)

Ubuntu 24.04 LTS
Download version 5.17.0 software for Ubuntu 24.04 LTS on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.17.0-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.17.0-1_u24.04_amd64.deb") (SHA256 checksum b3869a6fe9f2031cb5f36ac8d2a5a5280451159e7a68f0d6f91f98b5f0100939)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.17.0-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.17.0-1_u24.04_amd64.deb") (SHA256 checksum 3e46443a3f8425f62cec8d8ca414c4b5446b86b42012877ebe44a17303403413)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-openssl-provider_5.17.0-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-openssl-provider_5.17.0-1_u24.04_amd64.deb") (SHA256 checksum 69c2e61894e954ac1d0a785025902af5aa1922a7f6011a847f2111e153db706e)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.17.0-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.17.0-1_u24.04_amd64.deb") (SHA256 checksum 663da1a7b13a1055bb90fd7b168b69fcfb000eb91c1c3ce6062d8cc8db607fe4)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.17.0-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.17.0-1_u24.04_amd64.deb") (SHA256 checksum 0d57b4f08bd768ed595978d2a6d3fe6bbbf8398a784c66c4e30c19ecf6730b5d)

Download version 5.17.0 software for Ubuntu 24.04 LTS on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.17.0-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.17.0-1_u24.04_arm64.deb") (SHA256 checksum 94d9a36a3d3f2f04c10539713b98ddad68654c739572064e4c123005a9caf575)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.17.0-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.17.0-1_u24.04_arm64.deb") (SHA256 checksum a442950055a7051f50b4cdfa7ec347c1b207b0bbf7e159b31a3bf96896b66146)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-openssl-provider_5.17.0-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-openssl-provider_5.17.0-1_u24.04_arm64.deb") (SHA256 checksum dcc4b5a370da176a86e47683a78703a5604d6b7b49ba687377460f48c3ddff26)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.17.0-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.17.0-1_u24.04_arm64.deb") (SHA256 checksum 1fe1fa59a3e5c32edd5668604e43f7ce152473514b25ee736dfb0e9cf87c92c9)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.17.0-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.17.0-1_u24.04_arm64.deb") (SHA256 checksum 2bf2c13bf1520eaf2a45eb55aaba3334fa54da686d22d1a03005ec8f62ea8895)

Ubuntu 22.04 LTS
Download version 5.17.0 software for Ubuntu 22.04 LTS on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.17.0-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.17.0-1_u22.04_amd64.deb") (SHA256 checksum 2dc1f00952f69b59b0498e85c2f2009f80c9a2f9f28104995b0291da5f45d805)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.17.0-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.17.0-1_u22.04_amd64.deb") (SHA256 checksum df0e7ff8852a93fb4c5807317d3438ab96ffe69f19ba144d872991cbcb4172f6)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.17.0-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.17.0-1_u22.04_amd64.deb") (SHA256 checksum 77a3cc37e066ae0ad5655ddc3dd38a0513bdcbd3c9d3d780e2973ac42a75035e)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.17.0-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.17.0-1_u22.04_amd64.deb") (SHA256 checksum 88ca1614178771991649b8117ddf27ffb99c6842ee89f68e77c6df3470e6ba78)

Download version 5.17.0 software for Ubuntu 22.04 LTS on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.17.0-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.17.0-1_u22.04_arm64.deb") (SHA256 checksum 0e1f62783c16debf9188c9cf0085fe972671e5ea9bf0fc2fc3255f908885949c)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.17.0-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.17.0-1_u22.04_arm64.deb") (SHA256 checksum 109d25583e2d5ed0fe821a77098d8f2c815011f7873168e0110aeb857dc903ab)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.17.0-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.17.0-1_u22.04_arm64.deb") (SHA256 checksum 9151661a39f6394aa3ace682bd7964095ed5300244582d3f6b1f81255ebf22cf)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.17.0-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.17.0-1_u22.04_arm64.deb") (SHA256 checksum 66e408cea800a93becf378b8611595ad8cd1bf51e0ae7feebc548fe3099b477c)

Windows Server 2025
Download version 5.17.0 software for Windows Server 2025 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.0-1.msi") (SHA256 checksum 77dd4ad5da0d4a21c82ff2ea03c09a6b8c2005e27b6aba6724e4bec75606b0e7)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.0-1.msi") (SHA256 checksum c2c4766b67f02a93cca22b166e63fe6f4c71bfd9f7b45aa2da6a603d825e5c1a)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.0-1.msi") (SHA256 checksum 4feb0aeb7554ddd919eb7df301a4da537fffb0577a89a053fba802a2d3657a2a)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.0-1.msi") (SHA256 checksum 3766d4d4ab1bd7afa6b72e74bc80d8e5054481c8535f5a5c841cc320617c4e1e)

Windows Server 2022
Download version 5.17.0 software for Windows Server 2022 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.0-1.msi") (SHA256 checksum 77dd4ad5da0d4a21c82ff2ea03c09a6b8c2005e27b6aba6724e4bec75606b0e7)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.0-1.msi") (SHA256 checksum c2c4766b67f02a93cca22b166e63fe6f4c71bfd9f7b45aa2da6a603d825e5c1a)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.0-1.msi") (SHA256 checksum 4feb0aeb7554ddd919eb7df301a4da537fffb0577a89a053fba802a2d3657a2a)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.0-1.msi") (SHA256 checksum 3766d4d4ab1bd7afa6b72e74bc80d8e5054481c8535f5a5c841cc320617c4e1e)

Windows Server 2019
Download version 5.17.0 software for Windows Server 2019 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.0-1.msi") (SHA256 checksum 77dd4ad5da0d4a21c82ff2ea03c09a6b8c2005e27b6aba6724e4bec75606b0e7)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.0-1.msi") (SHA256 checksum c2c4766b67f02a93cca22b166e63fe6f4c71bfd9f7b45aa2da6a603d825e5c1a)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.0-1.msi") (SHA256 checksum 4feb0aeb7554ddd919eb7df301a4da537fffb0577a89a053fba802a2d3657a2a)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.0-1.msi") (SHA256 checksum 3766d4d4ab1bd7afa6b72e74bc80d8e5054481c8535f5a5c841cc320617c4e1e)

Windows Server 2016
Download version 5.17.0 software for Windows Server 2016 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.0-1.msi") (SHA256 checksum 77dd4ad5da0d4a21c82ff2ea03c09a6b8c2005e27b6aba6724e4bec75606b0e7)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.0-1.msi") (SHA256 checksum c2c4766b67f02a93cca22b166e63fe6f4c71bfd9f7b45aa2da6a603d825e5c1a)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.0-javadoc.jar") (SHA256 checksum a89e6d7e4e1f4049fefa64c765e97928fc54c366249f315ac6a839704e1ffba8)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.0-1.msi") (SHA256 checksum 4feb0aeb7554ddd919eb7df301a4da537fffb0577a89a053fba802a2d3657a2a)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.0-1.msi") (SHA256 checksum 3766d4d4ab1bd7afa6b72e74bc80d8e5054481c8535f5a5c841cc320617c4e1e)

Client SDK 5.17.0 introduces new features and improvements across multiple components.

###### Platform support

- Added RHEL 8 support for ARM64 architecture.

###### JCE

- Added support for OpenJDK 25 on all platforms
- Client SDK 5.17.0 is the last release to support OpenJDK 8.

###### New Features

- Introduced new OpenSSL Provider SDK for enhanced OpenSSL 3.2+ compatibility and additional cryptographic operations.
- Added Ed25519 curve support to EC key generation.
- Added support for EdDSA (Edwards-curve Digital Signature Algorithm) signing and verification in CloudHSM CLI.

###### CloudHSM CLI

- Added Ed25519 curve support to EC key generation for non-FIPS hsm2m.medium types.
- Added support for EdDSA (Edwards-curve Digital Signature Algorithm) signing and verification in CloudHSM CLI. For more information, see [Generate a signature with the HashEdDSA mechanism in
  CloudHSM CLI](cloudhsm_cli-crypto-sign-ed25519ph.md "cloudhsm_cli-crypto-sign-ed25519ph.md") and [Verify a signature signed with the HashEdDSA
  mechanism in CloudHSM CLI](cloudhsm_cli-crypto-verify-ed25519ph.md "cloudhsm_cli-crypto-verify-ed25519ph.md").

###### OpenSSL Provider

- New OpenSSL Provider SDK provides integration with OpenSSL 3.2+ Provider architecture for hsm2m.medium types.

###### Bug fixes/Improvements

- Improved retry mechanisms for cryptographic operations.

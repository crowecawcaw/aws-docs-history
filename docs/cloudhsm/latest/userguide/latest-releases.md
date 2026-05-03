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

## Client SDK 5 release: Version 5.17.1

Amazon Linux 2023
Download version 5.17.1 software for Amazon Linux 2023 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.17.1-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.17.1-1.amzn2023.x86_64.rpm") (SHA256 checksum e5d37660312c8d5b9c36a9b74555222a755276e2c1f360418c34125b2b715b97)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.17.1-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.17.1-1.amzn2023.x86_64.rpm") (SHA256 checksum 9b84d756e56f19b830adbd46aa5ac5096ae28944e34dd8dac3bd534e487d7aee)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.17.1-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.17.1-1.amzn2023.x86_64.rpm") (SHA256 checksum 5df0647ea5fe6da453bbf9a9578de9674ba93b722ec17dfe79825006211dc7a9)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.17.1-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.17.1-1.amzn2023.x86_64.rpm") (SHA256 checksum ac820e95618bf6cecf76b6ae0c5fb59198041f1d583178105a506d255d886fc9)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.17.1-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.17.1-1.amzn2023.x86_64.rpm") (SHA256 checksum 3b2f966c05690c14c325ea37cf9799bad477b2573f1077a5319d92933af9e590)

Download version 5.17.1 software for Amazon Linux 2023 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.17.1-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.17.1-1.amzn2023.aarch64.rpm") (SHA256 checksum 8cf4f7e9bed86ed15198e0870075fa01cb8243d3646ae9a1417ee3eba0cb3111)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.17.1-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.17.1-1.amzn2023.aarch64.rpm") (SHA256 checksum 831c7565caaea18c9c239b060347ec1b0e5121ec94d5bfe4cecda0fd4b1aa9ab)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.17.1-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.17.1-1.amzn2023.aarch64.rpm") (SHA256 checksum 73e91db43c98fa1eac6ce4d39f211d0dafa8445941b9f3adf77876cbeb443561)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.17.1-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.17.1-1.amzn2023.aarch64.rpm") (SHA256 checksum 1cc6bd9226ac98ebf898498f3b51b41b3ed58304f0290bd2045ab472e3bf3e14)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.17.1-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.17.1-1.amzn2023.aarch64.rpm") (SHA256 checksum d716108dfc8f0e89e082603dbd5c95379b9f593628ab30bc611c37c169fae8d0)

Amazon Linux 2
Download version 5.17.1 software for Amazon Linux 2 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.17.1-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.17.1-1.el7.x86_64.rpm") (SHA256 checksum c22875d9a81b2a5814d949b06d1467d4fbb111e67a6b29d83e961d95bdebd9e9)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.17.1-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.17.1-1.el7.x86_64.rpm") (SHA256 checksum f54d264ede8624867c3010d6b3979c51cd05a34d90a4169208400013c8de76c5)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.17.1-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.17.1-1.el7.x86_64.rpm") (SHA256 checksum c46297760a1d306541498e6a0295d7143273286dbb798c1c65bee38799b68e6b)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.17.1-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.17.1-1.el7.x86_64.rpm") (SHA256 checksum 87162212c93d8536d9247632221d855e841637a786c405eb47bc1410d62987d9)

Download version 5.17.1 software for Amazon Linux 2 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.17.1-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.17.1-1.el7.aarch64.rpm") (SHA256 checksum 0abe258732376b20730c2d2e089458e83eff4e751df8e60c0c70d3d92e75d7a4)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.17.1-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.17.1-1.el7.aarch64.rpm") (SHA256 checksum 4f8101debd678327a26246e50df10fe79663fc264fefd49deef63e036221fc0b)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.17.1-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.17.1-1.el7.aarch64.rpm") (SHA256 checksum dfc83b8f2dbee97eab98bff431c3374181a0051884abe7e9424621fcdba9c8c5)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.17.1-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.17.1-1.el7.aarch64.rpm") (SHA256 checksum bc43b221610d1c220ed402ee14bb0275ad79fb21a342639d1266579881da953a)

RHEL 10 (10.0+)
Download version 5.17.1 software for RHEL 10 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.17.1-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.17.1-1.el10.x86_64.rpm") (SHA256 checksum 11076479568454ad1083bb6a81953a73f9175f6d8626e247e1e16439a5c105ec)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.17.1-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.17.1-1.el10.x86_64.rpm") (SHA256 checksum 6c3d7a58b38ef39c7b5310958eb684feed20edf6731603a8b727b4bd978f465f)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.17.1-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.17.1-1.el10.x86_64.rpm") (SHA256 checksum 921883948344a06716d6b3b30f67708dedff550978efce6d5817b36c83e83b35)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.17.1-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.17.1-1.el10.x86_64.rpm") (SHA256 checksum 4d69481cc4e725e65811e031fe344cb178016cd268759bb910acdb14df9be413)

Download version 5.17.1 software for RHEL 10 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.17.1-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.17.1-1.el10.aarch64.rpm") (SHA256 checksum 7a20af9fbe7a9874132c1314841ef2ead0daef92ced3ba2289938a88d0ee929e)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.17.1-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.17.1-1.el10.aarch64.rpm") (SHA256 checksum e762bb21086131725e9ca13b7d25e6fcb474888ae49317e1b045ddf826a8338c)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.17.1-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.17.1-1.el10.aarch64.rpm") (SHA256 checksum c8bb96ded1abdfb54cd710fade3c91ce6030f5dc9ddeea639cc0a0cac5c26bb1)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.17.1-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.17.1-1.el10.aarch64.rpm") (SHA256 checksum d48ccaeccc9d4247f0cf4c81a6f092704630933dbc89e0b0ba9a75629fd863b7)

RHEL 9 (9.2+)
Download version 5.17.1 software for RHEL 9 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.17.1-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.17.1-1.el9.x86_64.rpm") (SHA256 checksum df4f1de8e68e363b351770dd74782d204f04d4db646c554fa96182b429006618)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.17.1-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.17.1-1.el9.x86_64.rpm") (SHA256 checksum 06d2e65adb076e65b81b51bcea34b64f718b6aa29c173eebcaf277de2c8d03ec)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.17.1-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.17.1-1.el9.x86_64.rpm") (SHA256 checksum 802e608484ab748eccdce8da0854dc668e90578d4c2bc6ede4caf4121d10171f)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.17.1-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.17.1-1.el9.x86_64.rpm") (SHA256 checksum 1a4fdfe82cc79a4de85a19d6645916b6b388c919a71a22efae7bafaba195db0f)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.17.1-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.17.1-1.el9.x86_64.rpm") (SHA256 checksum daab5b758c61f49b34b6f7e288debb121adc3d63b9652db086855d160c988570)

Download version 5.17.1 software for RHEL 9 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.17.1-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.17.1-1.el9.aarch64.rpm") (SHA256 checksum 2fe6549339b743200c6be91b8abf8017c3f67c90f7db25ffd0ab1915b91d0f78)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.17.1-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.17.1-1.el9.aarch64.rpm") (SHA256 checksum a0a964dcb817251faafcdd432e6260dff1d6e1bcdd7e7ffbd54a691cbe366b58)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.17.1-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.17.1-1.el9.aarch64.rpm") (SHA256 checksum bbcc9b3a2455328e6e7b11ff64b7e7653757960a74bfd9d6b3cc998b2a955fb2)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.17.1-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.17.1-1.el9.aarch64.rpm") (SHA256 checksum f9c74e2ededb9d2fdb7076789223c4cde7a0845b6f999b006fa741e9428195c7)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.17.1-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.17.1-1.el9.aarch64.rpm") (SHA256 checksum 0c4c1c7f4e06ba3b5b5dfe619abb0fa9d4729c87c668361fdb99b2a62f4b00fc)

RHEL 8 (8.3+)
Download version 5.17.1 software for RHEL 8 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.17.1-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.17.1-1.el8.x86_64.rpm") (SHA256 checksum 0f8465ab44f7388980b22bc1f8c6c3c3e09e809ba2712170c85db86918817803)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.17.1-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.17.1-1.el8.x86_64.rpm") (SHA256 checksum 8fe4f9fb6088d2a32e210696775d395b918ee867dede8b2152ff37d0d99cc8f3)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.17.1-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.17.1-1.el8.x86_64.rpm") (SHA256 checksum 948d37f435e7b03ec8409ee48f89c265009c7e7a76e7a18921c5ef88f3504391)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.17.1-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.17.1-1.el8.x86_64.rpm") (SHA256 checksum 2168377badf708047ee14d2bc57b9234f01ce2c9f42568dbd1185723a63eeeb8)

Download version 5.17.1 software for RHEL 8 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.17.1-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.17.1-1.el8.aarch64.rpm") (SHA256 checksum 69db8b832edba06fe055ce9772bfad645a86e5e530d20e8f14738fc7cb06a5c7)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.17.1-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.17.1-1.el8.aarch64.rpm") (SHA256 checksum ac7ad7b11e63d1fb7af57ff1e61b421aa0fccbca99ed15b0ddec1602fea2acd3)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.17.1-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.17.1-1.el8.aarch64.rpm") (SHA256 checksum 7520a95076a7a794219677489d2c764502a6dcfeea484f10059e283f1aee6975)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.17.1-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.17.1-1.el8.aarch64.rpm") (SHA256 checksum 596acc3164695a262b15edbb92eda89ffd4b8d06b91617ce91058c2d99ae2a53)

Ubuntu 24.04 LTS
Download version 5.17.1 software for Ubuntu 24.04 LTS on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.17.1-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.17.1-1_u24.04_amd64.deb") (SHA256 checksum bc3146d5dc7aabe5359c41d2bd0fd97ed4bc2f389be6a4b94423065af9d60bd0)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.17.1-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.17.1-1_u24.04_amd64.deb") (SHA256 checksum 05d6afa19949b69af4325f55d285a89255ab2c7487aba898c74cbd4ee8e30fdf)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-openssl-provider_5.17.1-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-openssl-provider_5.17.1-1_u24.04_amd64.deb") (SHA256 checksum 3deba48c356478fdbb0236ad435cee8f7f8cfe3cec1a894aea3f79d80d398cce)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.17.1-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.17.1-1_u24.04_amd64.deb") (SHA256 checksum ebacb95d8f92528e236a5342cb5c1ecbf74c228428fb4a080c0c972b697292b5)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.17.1-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.17.1-1_u24.04_amd64.deb") (SHA256 checksum 575f54610d26561bb98b69548de2f61a17b5b93ed49be13821be536d76ffdb75)

Download version 5.17.1 software for Ubuntu 24.04 LTS on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.17.1-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.17.1-1_u24.04_arm64.deb") (SHA256 checksum b0c918575e611f486902ebbcc3ee84e15217247f5577b06764cfc620660c6ec4)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.17.1-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.17.1-1_u24.04_arm64.deb") (SHA256 checksum 57f0afb66c34a91e96bef4964dd3fb487fe5b9b06d0818ee9a2c90ad60068321)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-openssl-provider_5.17.1-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-openssl-provider_5.17.1-1_u24.04_arm64.deb") (SHA256 checksum dcf5128c6913e43e0a304d0221c243fd5228f235b78fac5ffd43478bb0d96062)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.17.1-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.17.1-1_u24.04_arm64.deb") (SHA256 checksum 21d43992ace3aec9ec3711e7bd64ec716d3281f627e78a6f7a328a8e533beec4)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.17.1-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.17.1-1_u24.04_arm64.deb") (SHA256 checksum 096844ef80a7d573843682cfb3797a0c45608d004639ab0e671065f3964c06e3)

Ubuntu 22.04 LTS
Download version 5.17.1 software for Ubuntu 22.04 LTS on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.17.1-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.17.1-1_u22.04_amd64.deb") (SHA256 checksum ec8c275832f9936e698106454e930268d7f2f310faffa2b7d03c3c03c6e297e1)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.17.1-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.17.1-1_u22.04_amd64.deb") (SHA256 checksum 316c3929363ad1d764f356bbf56dff121b3bccefa5060b94c5d9d7955f828ff4)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.17.1-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.17.1-1_u22.04_amd64.deb") (SHA256 checksum 4c53b61bcdada0a684b605c0630f52b6b3bf6e9ed64f4c623f35fa4283e9770d)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.17.1-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.17.1-1_u22.04_amd64.deb") (SHA256 checksum 6b4ba5d3d06e5234b64b7c60310d5b477c2d8732fbbd3e9c60dcb56f2ef69a6e)

Download version 5.17.1 software for Ubuntu 22.04 LTS on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.17.1-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.17.1-1_u22.04_arm64.deb") (SHA256 checksum d26d10425572f0624d2205e1409b88ccc5d793bcfeef6cd26fdcb5c41f5c8129)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.17.1-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.17.1-1_u22.04_arm64.deb") (SHA256 checksum e3b6cd3e93f2645d9a23add1a514e314ad3d48a93b253e6b984577b8e502e1f0)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.17.1-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.17.1-1_u22.04_arm64.deb") (SHA256 checksum 7ab3ea04d34f92c585121b110f620b632616a5585a4ed153fbb61fedef667b06)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.17.1-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.17.1-1_u22.04_arm64.deb") (SHA256 checksum 9cf4a05ebf2bce4a0c9e57dd2eef87ba47ac05c4a303d4465cbf41536736c685)

Windows Server 2025
Download version 5.17.1 software for Windows Server 2025 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.1-1.msi") (SHA256 checksum 145ea74ff3ab70c0f5f1ccd8ced90b86f0b4f3ee029d2d9452e9b0724ae2f64e)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.1-1.msi") (SHA256 checksum 074bc0a990d51debea16e8691171c1cfc4e164795eb839be1d311858b157b0a6)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.1-1.msi") (SHA256 checksum ddc11eee7b884ddaa203ded85f36553a9a636d35bf9dd4b6557c23a167ed7c4a)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.1-1.msi") (SHA256 checksum 5bef4732d23861795a8463c3a3511e0a235a29972d584c2f65384e87ba4bb48c)

Windows Server 2022
Download version 5.17.1 software for Windows Server 2022 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.1-1.msi") (SHA256 checksum 145ea74ff3ab70c0f5f1ccd8ced90b86f0b4f3ee029d2d9452e9b0724ae2f64e)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.1-1.msi") (SHA256 checksum 074bc0a990d51debea16e8691171c1cfc4e164795eb839be1d311858b157b0a6)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.1-1.msi") (SHA256 checksum ddc11eee7b884ddaa203ded85f36553a9a636d35bf9dd4b6557c23a167ed7c4a)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.1-1.msi") (SHA256 checksum 5bef4732d23861795a8463c3a3511e0a235a29972d584c2f65384e87ba4bb48c)

Windows Server 2019
Download version 5.17.1 software for Windows Server 2019 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.1-1.msi") (SHA256 checksum 145ea74ff3ab70c0f5f1ccd8ced90b86f0b4f3ee029d2d9452e9b0724ae2f64e)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.1-1.msi") (SHA256 checksum 074bc0a990d51debea16e8691171c1cfc4e164795eb839be1d311858b157b0a6)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.1-1.msi") (SHA256 checksum ddc11eee7b884ddaa203ded85f36553a9a636d35bf9dd4b6557c23a167ed7c4a)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.1-1.msi") (SHA256 checksum 5bef4732d23861795a8463c3a3511e0a235a29972d584c2f65384e87ba4bb48c)

Windows Server 2016
Download version 5.17.1 software for Windows Server 2016 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.17.1-1.msi") (SHA256 checksum 145ea74ff3ab70c0f5f1ccd8ced90b86f0b4f3ee029d2d9452e9b0724ae2f64e)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.17.1-1.msi") (SHA256 checksum 074bc0a990d51debea16e8691171c1cfc4e164795eb839be1d311858b157b0a6)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.17.1-javadoc.jar") (SHA256 checksum 89b5c2232c1739d61813d16f6d3177984bfffb66754367883e2d7e997a363f30)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.17.1-1.msi") (SHA256 checksum ddc11eee7b884ddaa203ded85f36553a9a636d35bf9dd4b6557c23a167ed7c4a)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.1-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.17.1-1.msi") (SHA256 checksum 5bef4732d23861795a8463c3a3511e0a235a29972d584c2f65384e87ba4bb48c)

Client SDK 5.17.1 includes bug fixes and improvements.

###### JCE

- Client SDK 5.17.1 is the last release to support OpenJDK 11.

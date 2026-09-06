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

## Client SDK 5 release: Version 5.18.0

Amazon Linux 2023
Download version 5.18.0 software for Amazon Linux 2023 on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.18.0-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.18.0-1.amzn2023.x86_64.rpm") (SHA256 checksum 8d321bd3d74b7365e40107e43e5aa4680f4938513ca1c33f1c739369d54cc466)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.18.0-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.18.0-1.amzn2023.x86_64.rpm") (SHA256 checksum 107d522466e83e6f9a9d92d189271180ed60b2bf0d7343e0d46225106a485480)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.18.0-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.18.0-1.amzn2023.x86_64.rpm") (SHA256 checksum 0d6470a0083273ae1d0922ab7b8b240f929762764bd7b0c84d95f87b3c38fca4)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.18.0-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.18.0-1.amzn2023.x86_64.rpm") (SHA256 checksum 2ee2076bea49b970e1b9f6a0edee11dc9cbd139ef11a2687e4e6f54c9cc3ef66)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.18.0-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.18.0-1.amzn2023.x86_64.rpm") (SHA256 checksum 0c77a4014d77df64ea3faaf1cc8d8f67dacd8a5ca53baa0026ab0b65d4fe6b69)

Download version 5.18.0 software for Amazon Linux 2023 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.18.0-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.18.0-1.amzn2023.aarch64.rpm") (SHA256 checksum 8206a783676c2dc737872f8d536d2233e76197505b80c5bbff11690cc975d105)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.18.0-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.18.0-1.amzn2023.aarch64.rpm") (SHA256 checksum 5eb84a69a9f28218660ec6d879b86964da3402dc27ecaacf205316723346023d)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.18.0-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.18.0-1.amzn2023.aarch64.rpm") (SHA256 checksum a6cafef403e45c19faf6977906ffbf06b4d12b79ddb5fb1f26383c9d1e3dd4ec)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.18.0-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.18.0-1.amzn2023.aarch64.rpm") (SHA256 checksum 8323afdfd2f080dad51c92fe6fd1b802c7db76f6b29949d6c5349472e1377a06)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.18.0-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.18.0-1.amzn2023.aarch64.rpm") (SHA256 checksum a709088dd8857988c893475d85b9a1b3d7a3545006b119156d1e45bebe77021e)

Amazon Linux 2
Download version 5.18.0 software for Amazon Linux 2 on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.18.0-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.18.0-1.el7.x86_64.rpm") (SHA256 checksum 3d6de0aac5e9f49e96f8aace1e2515c050934f76952ae2a74b3a15952fe9b01e)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.18.0-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.18.0-1.el7.x86_64.rpm") (SHA256 checksum c68bbffc1b26926072f0b4e066c03e6f4721d36f4f2ea184efae053dd5088f30)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.18.0-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.18.0-1.el7.x86_64.rpm") (SHA256 checksum a1157f1a66a43c90ba3bd79a1dabbb2435c66f8ae50d096644aecf40a4392205)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.18.0-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.18.0-1.el7.x86_64.rpm") (SHA256 checksum f29d3ad3fb8084c2a6491003907f494876af800b3a925a000ef11702b05be306)

Download version 5.18.0 software for Amazon Linux 2 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.18.0-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.18.0-1.el7.aarch64.rpm") (SHA256 checksum 5fb27847ed54c4ec19dbe395eab417b5fe79071f3560a5e0200240bb540542e7)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.18.0-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.18.0-1.el7.aarch64.rpm") (SHA256 checksum e93c7ac45d754ba9217ed68cd9f2c09c3581128518119a3edada75c36fedd18a)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.18.0-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.18.0-1.el7.aarch64.rpm") (SHA256 checksum 19741d2bd33e9b540379878baf2917b0fe95fa14a103e3192dad0050028bb032)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.18.0-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.18.0-1.el7.aarch64.rpm") (SHA256 checksum 8e9427916230ee4b6357620c310a5463d001342a2955c436e93e314a369fbc26)

RHEL 10 (10.0+)
Download version 5.18.0 software for RHEL 10 on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.18.0-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.18.0-1.el10.x86_64.rpm") (SHA256 checksum 56c835581b68fbf6fff052f43fad93c60986c82cc74ee012dcaba25a4153ca06)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.18.0-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.18.0-1.el10.x86_64.rpm") (SHA256 checksum a06765c7e10ac46125a27ae4466464efb28d722decadb90881d6b002a7949954)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.18.0-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.18.0-1.el10.x86_64.rpm") (SHA256 checksum 86b2e64b8d5b354b2ea0e41126f2cccea1be124160621d04e7ee534d2570172b)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.18.0-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.18.0-1.el10.x86_64.rpm") (SHA256 checksum 5eabb49d6be32f2dc6e9c9a377bd0d6fc2354eb3b51412e0002fa061625ff206)

Download version 5.18.0 software for RHEL 10 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.18.0-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.18.0-1.el10.aarch64.rpm") (SHA256 checksum 96b3ae6cf52b63369fe1420ae4ed95a2bf2f42b7c1543d87894ff6014bece1ea)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.18.0-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.18.0-1.el10.aarch64.rpm") (SHA256 checksum dc6b4e852f8a079ad98fc6af11a177cd8e738ab89bd6ccee0392c25898cf3ef2)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.18.0-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.18.0-1.el10.aarch64.rpm") (SHA256 checksum 6f93577ca3dd2f5ae0980be8811753f294df193d36583f42a92d859c9a6143e2)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.18.0-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.18.0-1.el10.aarch64.rpm") (SHA256 checksum a4dd39dbdf4ffd6e589b485635e535a3d0fbf4cab815378ff7d4fa1576c3de17)

RHEL 9 (9.2+)
Download version 5.18.0 software for RHEL 9 on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.18.0-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.18.0-1.el9.x86_64.rpm") (SHA256 checksum ef2d3a0d427f6d246a69db06a07b520d98721f24fa1180af2a70a6cb90f175b8)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.18.0-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.18.0-1.el9.x86_64.rpm") (SHA256 checksum 56e67217c93bcaca96aafede8049a83018740edcaedb72cc7801350be715b28c)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.18.0-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.18.0-1.el9.x86_64.rpm") (SHA256 checksum b4fe26cc8159f77188430238660a64c6cb8ff6db21c7945ce62ba2832d3c3610)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.18.0-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.18.0-1.el9.x86_64.rpm") (SHA256 checksum 481e2cda3c26b5297f91402e80176350feccbb9f1b58001f1f577d1c800340dd)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.18.0-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.18.0-1.el9.x86_64.rpm") (SHA256 checksum d37cabf2373a9935394339f704b6f92bf183fbe8abcb2ab92deb756e0fec71ee)

Download version 5.18.0 software for RHEL 9 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.18.0-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.18.0-1.el9.aarch64.rpm") (SHA256 checksum b0d8ec4871887ad40c51e725d510137ed7311eecfc3981060eea74d99fda4ab5)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.18.0-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.18.0-1.el9.aarch64.rpm") (SHA256 checksum 475404fd30d008f952e2d07c8fc39aaeb6de200248e3cfa07711a3dbcb2d7d04)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.18.0-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.18.0-1.el9.aarch64.rpm") (SHA256 checksum 2985c6f422a2dc21578cd6f15876c147543776ba7da91db5990621543efc5ff8)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.18.0-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.18.0-1.el9.aarch64.rpm") (SHA256 checksum 45a035f5005459431a68786ea4db0184b71f8e8d5277db8b8ccbe251416b10ca)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.18.0-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.18.0-1.el9.aarch64.rpm") (SHA256 checksum 803a867e3df2f2aeb5230f6939db8ffd202991406bce2c626b987465f802fcfb)

RHEL 8 (8.3+)
Download version 5.18.0 software for RHEL 8 on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.18.0-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.18.0-1.el8.x86_64.rpm") (SHA256 checksum 912d5d2a73761801242833093472d1365cbcfc3551b1fe93743dce0cbdf8c727)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.18.0-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.18.0-1.el8.x86_64.rpm") (SHA256 checksum 70b9aedde526fed0d65114f9b4d8a9576b1ad0efe0bc271c7ef6765345ef66ce)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.18.0-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.18.0-1.el8.x86_64.rpm") (SHA256 checksum ecc9146e3ba72af288834bffe5c4a93922e9ae379f9663fac7d86ffbb36785a8)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.18.0-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.18.0-1.el8.x86_64.rpm") (SHA256 checksum 784009c529ff86f357b20c62f1680f35a4710e22d1fd40f9018dab81fa0030c7)

Download version 5.18.0 software for RHEL 8 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.18.0-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.18.0-1.el8.aarch64.rpm") (SHA256 checksum 9ee50fd41904ade515bfab6073fa2d8ba2e1e1c373116420d9125049e3bcdd1f)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.18.0-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.18.0-1.el8.aarch64.rpm") (SHA256 checksum 26ac4952f6363ba5a5fcebd45b9709343ed31d05fc5c21240b0e530520295caa)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.18.0-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.18.0-1.el8.aarch64.rpm") (SHA256 checksum ec2c5e4aa8ee0307cf393ad14a890dab5ed904aa4e0de7f7d9ec0806c243a704)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.18.0-1.el8.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.18.0-1.el8.aarch64.rpm") (SHA256 checksum edbeec5c1f8ac877fbd53f70dbe906bf69839a0493802bf9b1ef1c3c574a07e3)

Ubuntu 26.04 LTS
Download version 5.18.0 software for Ubuntu 26.04 LTS on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-pkcs11_5.18.0-1_u26.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-pkcs11_5.18.0-1_u26.04_amd64.deb") (SHA256 checksum 4b3864459b482f8d3862582b52809315b7653b8b63523f47920c3812643cbab0)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-dyn_5.18.0-1_u26.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-dyn_5.18.0-1_u26.04_amd64.deb") (SHA256 checksum 3e53d5da4ab44384b90bcdc5a4b9b120a630f407df633765414dc3146d9e6e28)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-openssl-provider_5.18.0-1_u26.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-openssl-provider_5.18.0-1_u26.04_amd64.deb") (SHA256 checksum 4967595c4ea3538f13c647469f9a7ba4583b54bb81ca761bbe1488bcfca78395)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-jce_5.18.0-1_u26.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-jce_5.18.0-1_u26.04_amd64.deb") (SHA256 checksum bc24b988be625826a18353dd0d2c2b1366e28d6d57386865bb8dc6b1c38ed794)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-cli_5.18.0-1_u26.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-cli_5.18.0-1_u26.04_amd64.deb") (SHA256 checksum 70b18fad5e3f150695a6e476c13b3e5efa29a5c0c38010522737e0ad36f4cba0)

Download version 5.18.0 software for Ubuntu 26.04 LTS on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-pkcs11_5.18.0-1_u26.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-pkcs11_5.18.0-1_u26.04_arm64.deb") (SHA256 checksum 23d562db2c6fc6a9253a66c32eb11283f7300aada9c4a714516f1dce029a731a)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-dyn_5.18.0-1_u26.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-dyn_5.18.0-1_u26.04_arm64.deb") (SHA256 checksum dfc2777e34d6016c9f39edf97553cd23591b34856bfae56cfead25a4969e9eb7)
- [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-openssl-provider_5.18.0-1_u26.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-openssl-provider_5.18.0-1_u26.04_arm64.deb") (SHA256 checksum 9f2e8ffbd92334942aea1df515c0f987c88c698acd4a74e03f7a14fe98c682be)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-jce_5.18.0-1_u26.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-jce_5.18.0-1_u26.04_arm64.deb") (SHA256 checksum c85a67409cbbbd38f54b6ac2f2ab8a67335452d42b03628681750b08bf938ebe)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-cli_5.18.0-1_u26.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-cli_5.18.0-1_u26.04_arm64.deb") (SHA256 checksum 6fa5d24febe3e3f6c8649f3bd75e2b090660cd82fbedac0e5491a726988f99bc)

Ubuntu 24.04 LTS
Download version 5.18.0 software for Ubuntu 24.04 LTS on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.18.0-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.18.0-1_u24.04_amd64.deb") (SHA256 checksum 72ab424e34ee2780ae770679180f456374d8be1b66a82aa441defa603c8ec3a7)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.18.0-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.18.0-1_u24.04_amd64.deb") (SHA256 checksum e9ebd0cada051ff21218655f1431171ddd69d219d3cdea13fd9b72ac30fb0a0c)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.18.0-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.18.0-1_u24.04_amd64.deb") (SHA256 checksum 551277453f0bf3a8e78a0e0fec31eab3341dd40adceff3225e606800e0c9c12e)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.18.0-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.18.0-1_u24.04_amd64.deb") (SHA256 checksum 28cba68e9721a1683f9a394704bd786b234cb44a8acc10dbe696aaee351a6f8d)

Download version 5.18.0 software for Ubuntu 24.04 LTS on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.18.0-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.18.0-1_u24.04_arm64.deb") (SHA256 checksum c17653c12df1448cba9f1714c6325e35d51df4015557db26b239b82cc9d50db1)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.18.0-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.18.0-1_u24.04_arm64.deb") (SHA256 checksum 253c3b8b3e40461889e5101d66f88fa7d21866ee9af1155e014890f6bb795ad1)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.18.0-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.18.0-1_u24.04_arm64.deb") (SHA256 checksum 1e79f34dbc840ec605cb85b4dcd61a01aa2490200e13c98f5021191f4a3bbb41)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.18.0-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.18.0-1_u24.04_arm64.deb") (SHA256 checksum 150a3ce22f9a2e7e6ac1b2415b94edc09c7589a64044856409071f0a55360b2d)

Ubuntu 22.04 LTS
Download version 5.18.0 software for Ubuntu 22.04 LTS on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.18.0-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.18.0-1_u22.04_amd64.deb") (SHA256 checksum 7c1f6c82edfa7ecbd98ee8e27d4fca205aacdd770ebfe962511214d511beb904)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.18.0-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.18.0-1_u22.04_amd64.deb") (SHA256 checksum 014106115154a1d47a44be7dbbeb0483b8c2ed7e676e728c1bb0d73323a94d00)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.18.0-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.18.0-1_u22.04_amd64.deb") (SHA256 checksum 0ff395b8ff58832b2b50f82066e8979329cb95ae4097748632a9b590e88e352a)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.18.0-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.18.0-1_u22.04_amd64.deb") (SHA256 checksum 8e5cc97c69bea415a272eae5b85d16566342cb581441a5061042a3998dc5600f)

Download version 5.18.0 software for Ubuntu 22.04 LTS on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.18.0-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.18.0-1_u22.04_arm64.deb") (SHA256 checksum 7c5e51bb931f54cd524d5c02487b3c2e0c26d802cf52c1d6dee8f6f1dde5513b)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.18.0-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.18.0-1_u22.04_arm64.deb") (SHA256 checksum 7a3a1b696fe1fcb34b3a3c4f4556fa89038d27165a1265458289f9b67694422a)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.18.0-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.18.0-1_u22.04_arm64.deb") (SHA256 checksum ce9740e58424e6e2f2cc98d840755e440339465da323e85049ab7dd2edc4be46)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.18.0-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.18.0-1_u22.04_arm64.deb") (SHA256 checksum 20ec9d5dd380be3f77fec871b45e1e7739b00b9438b95213666d0e3173a99d76)

Windows Server 2025
Download version 5.18.0 software for Windows Server 2025 on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.0-1.msi") (SHA256 checksum 7a6486f73ad63312ef4b09b5284185f666d68abf5c5cd23c0a234a071e1d59e6)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.0-1.msi") (SHA256 checksum 89dc221ffce8510b7b1365d5655e4b6823341986d4ecb159350e9e1e8a02e823)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.0-1.msi") (SHA256 checksum b536e61880080695dc705234eb45abef5f34bc20273ae9cdca25acf9163d86a6)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.0-1.msi") (SHA256 checksum 8dd827b51e471e08094c963b745cd6960d4d398b0ee26930981bafccaf4258a6)

Windows Server 2022
Download version 5.18.0 software for Windows Server 2022 on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.0-1.msi") (SHA256 checksum 7a6486f73ad63312ef4b09b5284185f666d68abf5c5cd23c0a234a071e1d59e6)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.0-1.msi") (SHA256 checksum 89dc221ffce8510b7b1365d5655e4b6823341986d4ecb159350e9e1e8a02e823)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.0-1.msi") (SHA256 checksum b536e61880080695dc705234eb45abef5f34bc20273ae9cdca25acf9163d86a6)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.0-1.msi") (SHA256 checksum 8dd827b51e471e08094c963b745cd6960d4d398b0ee26930981bafccaf4258a6)

Windows Server 2019
Download version 5.18.0 software for Windows Server 2019 on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.0-1.msi") (SHA256 checksum 7a6486f73ad63312ef4b09b5284185f666d68abf5c5cd23c0a234a071e1d59e6)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.0-1.msi") (SHA256 checksum 89dc221ffce8510b7b1365d5655e4b6823341986d4ecb159350e9e1e8a02e823)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.0-1.msi") (SHA256 checksum b536e61880080695dc705234eb45abef5f34bc20273ae9cdca25acf9163d86a6)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.0-1.msi") (SHA256 checksum 8dd827b51e471e08094c963b745cd6960d4d398b0ee26930981bafccaf4258a6)

Windows Server 2016
Download version 5.18.0 software for Windows Server 2016 on x86\_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.0-1.msi") (SHA256 checksum 7a6486f73ad63312ef4b09b5284185f666d68abf5c5cd23c0a234a071e1d59e6)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.0-1.msi") (SHA256 checksum 89dc221ffce8510b7b1365d5655e4b6823341986d4ecb159350e9e1e8a02e823)

  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.0-javadoc.jar") (SHA256 checksum 741a56da7358118b091ed8cdcecbccc445574688249b1d5cfba4ae5d153d16c2)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.0-1.msi") (SHA256 checksum b536e61880080695dc705234eb45abef5f34bc20273ae9cdca25acf9163d86a6)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.0-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.0-1.msi") (SHA256 checksum 8dd827b51e471e08094c963b745cd6960d4d398b0ee26930981bafccaf4258a6)

Client SDK 5.18.0 introduces new features and improvements across multiple components, including post-quantum ML-DSA signatures and EdDSA support.

###### Platform support

- Added Ubuntu 26.04 LTS support.

###### New Features

- Added support for ML-DSA (Module-Lattice-Based Digital Signature Algorithm, FIPS 204) post-quantum key generation, signing, and verification.
- Added support for EdDSA (Edwards-curve Digital Signature Algorithm) signing and verification.

###### CloudHSM CLI

- Added support for generating ML-DSA key pairs (ML-DSA-44, ML-DSA-65, and ML-DSA-87), signing, and verification. For more information, see [Generate an asymmetric ML-DSA key pair with CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair-mldsa.md "cloudhsm_cli-key-generate-asymmetric-pair-mldsa.md"), [Generate a signature with the ML-DSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-sign-mldsa.md "cloudhsm_cli-crypto-sign-mldsa.md"), and [Verify a signature signed with the ML-DSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-verify-mldsa.md "cloudhsm_cli-crypto-verify-mldsa.md").
- Added PureEdDSA (Ed25519) signing and verification, extending EdDSA support in the CloudHSM CLI. For more information, see [Generate a signature with the PureEdDSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-sign-ed25519.md "cloudhsm_cli-crypto-sign-ed25519.md") and [Verify a signature signed with the PureEdDSA mechanism in CloudHSM CLI](cloudhsm_cli-crypto-verify-ed25519.md "cloudhsm_cli-crypto-verify-ed25519.md").

###### PKCS #11 library

- Added support for ML-DSA key generation, signing, and verification, and for EdDSA (Ed25519 and Ed25519ph) signing and verification. For more information, see [Supported mechanisms for the PKCS #11 library for AWS CloudHSM Client SDK 5](pkcs11-mechanisms.md "pkcs11-mechanisms.md").

###### JCE provider

- Added support for ML-DSA key generation, signing, and verification, and for EdDSA (Ed25519 and Ed25519ph). For more information, see [Supported mechanisms for JCE provider for AWS CloudHSM Client SDK 5](java-lib-supported_5.md "java-lib-supported_5.md").

###### OpenSSL Provider

- Added support for PureEdDSA (Ed25519) key types for TLS offload on non-FIPS clusters, and ML-DSA (ML-DSA-44, ML-DSA-65, and ML-DSA-87) key types for TLS offload on both FIPS and non-FIPS clusters. For more information, see [Supported key types for OpenSSL Provider for AWS CloudHSM Client SDK 5](openssl-provider-key-types.md "openssl-provider-key-types.md") and [OpenSSL Provider Supported Mechanisms](openssl-provider-mechanisms.md "openssl-provider-mechanisms.md").
- The OpenSSL Provider now supports OpenSSL CLI operations, including certificate signing request (CSR) creation and certificate signing, for all supported key types.

###### Bug fixes/Improvements

- Resolved a known issue where the `key-reference` filter could not select session (ephemeral) keys in the CloudHSM CLI and JCE provider.
- Improved throttling handling and automatic retry behavior across the Client SDKs, along with additional bug fixes and stability improvements.

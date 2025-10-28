# AWS CloudHSM latest Client SDK release

In March 2021, AWS CloudHSM released Client SDK version 5.0.0, which introduces an
all-new Client SDK with different requirements, capabilities, and platform support.

Client SDK 5 is fully supported for production environments, and offers the same
components and level of support as Client SDK 3. For
more information, see [Compare AWS CloudHSM Client SDK component support](sdk3-compare.md "sdk3-compare.md").

This section includes the latest version of the Client SDK.

## Client SDK 5 release: Version 5.16.2

Amazon Linux 2023
Download version 5.16.2 software for Amazon Linux 2023 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.16.2-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.16.2-1.amzn2023.x86_64.rpm") (SHA256 checksum e223649cbf689afaeca445b962cceaab3c143b901ee7974a7a5360b6424c409b)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.16.2-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.16.2-1.amzn2023.x86_64.rpm") (SHA256 checksum 9b51e8b1429f22705399299c111385e9434873a1dd26dda2c70498646590148c)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.16.2-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.16.2-1.amzn2023.x86_64.rpm") (SHA256 checksum 45ec10c2e3d592fb1fe56cc9dee1d8653e3a6dfa15b8185618fd3cf66c567314)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.16.2-1.amzn2023.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.16.2-1.amzn2023.x86_64.rpm") (SHA256 checksum 8134a0e316286310eda1606b6a14e1c9fd6f0e27934a43e55e24d3094ef870a6)

Download version 5.16.2 software for Amazon Linux 2023 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.16.2-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.16.2-1.amzn2023.aarch64.rpm") (SHA256 checksum 7556c69294d0c67b359cf9995ec7047cdc90e21542d2c9d5e110e35f13c329c5)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.16.2-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.16.2-1.amzn2023.aarch64.rpm") (SHA256 checksum 6ab4f3b9731a6f26891658f5e3a0ff74255096390c42aa7f702ba07e0bd924b1)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.16.2-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.16.2-1.amzn2023.aarch64.rpm") (SHA256 checksum 98b80696762a73f3f9fbe6c3c7af0f8f9db23ba63d66d4d941690b6698019702)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.16.2-1.amzn2023.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.16.2-1.amzn2023.aarch64.rpm") (SHA256 checksum 649397606f527f330049cf7adb5ad667126dfd7f63f878f1f46b469e2f127814)

Amazon Linux 2
Download version 5.16.2 software for Amazon Linux 2 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.16.2-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.16.2-1.el7.x86_64.rpm") (SHA256 checksum 073ee736ad9c7de6e6451afdecc4d77e6ed1a63f314a7fc09373ff35986fa0fc)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.16.2-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.16.2-1.el7.x86_64.rpm") (SHA256 checksum b174fb24a15f1e22dd520ea9ac4ac14229c2adce14ac6df8901f9d3c0e7e24f6)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.16.2-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.16.2-1.el7.x86_64.rpm") (SHA256 checksum f18e42f2679ab0fb51c421965a5dd6c8fe1361442d92403d1d230bedb003b27a)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.16.2-1.el7.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.16.2-1.el7.x86_64.rpm") (SHA256 checksum 5a6c83833b60017dd494c31fd4abf3896f57177be7951674c85d0d4e909d2041)

Download version 5.16.2 software for Amazon Linux 2 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.16.2-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.16.2-1.el7.aarch64.rpm") (SHA256 checksum df2c97a27855916983f242eba05e0741335158432ac46ebbeae47c4a3b7b0bef)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.16.2-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.16.2-1.el7.aarch64.rpm") (SHA256 checksum d25456e3da39c63d9c0d4a928815f995239b146f4f0b26a8c50c742905543207)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.16.2-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.16.2-1.el7.aarch64.rpm") (SHA256 checksum 7e31734efbaae49203e57d7ad4d1e291faa5b7e16c469a3596da82a7380bceeb)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.16.2-1.el7.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.16.2-1.el7.aarch64.rpm") (SHA256 checksum b77eb1f9ff58ccc864854d7f261e331ce50836cd770efc8e8eaebb33d78c23e2)

RHEL 10 (10.0+)
Download version 5.16.2 software for RHEL 10 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.16.2-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.16.2-1.el10.x86_64.rpm") (SHA256 checksum 8044cb40c9c65ae944900c740308e68eeb0156d3b93051d60463cd3f6095ef67)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.16.2-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.16.2-1.el10.x86_64.rpm") (SHA256 checksum a1b7f110c2b15ba7ce9adee74baf1f108d85146269321991314f9153a074ca27)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.16.2-1.el10.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.16.2-1.el10.x86_64.rpm") (SHA256 checksum 3ded29fdb74537b284cf871af91dd64fce8483770141a3e4470e94fb69524621)

Download version 5.16.2 software for RHEL 10 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.16.2-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.16.2-1.el10.aarch64.rpm") (SHA256 checksum 643fa23ffea47dfb21fd326cacf99e0e45f44d767ca6198ab06023239eda5d2c)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.16.2-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.16.2-1.el10.aarch64.rpm") (SHA256 checksum e6b5c2760c60f5c82a248d36f3b47cea9b1bbb743cf1c02a1c13554b70ab87f8)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.16.2-1.el10.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.16.2-1.el10.aarch64.rpm") (SHA256 checksum a6af281ff9f429f964ac9d2babc251b4423748d2b2e6da22fc51b9fd5c59714c)

RHEL 9 (9.2+)
Download version 5.16.2 software for RHEL 9 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.16.2-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.16.2-1.el9.x86_64.rpm") (SHA256 checksum e0a44849c9cb562cf803ff182e54a35e7eee682efa2a99fdfac51a996822d126)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.16.2-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.16.2-1.el9.x86_64.rpm") (SHA256 checksum 97463a8a88239d4a81854f2a4da7e0371dbcb375a662c7eae7753c371ef3c39f)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.16.2-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.16.2-1.el9.x86_64.rpm") (SHA256 checksum 10cd4b9826451b7e9a11390cabcc7df548f5b3197e8bc87f5efe04605e503dc1)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.16.2-1.el9.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.16.2-1.el9.x86_64.rpm") (SHA256 checksum 6c7fc59dcce4d7bc0c4460ae7c793f13fcbb306924942bc6e1457f729602f76f)

Download version 5.16.2 software for RHEL 9 on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.16.2-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.16.2-1.el9.aarch64.rpm") (SHA256 checksum 7b8d3f5e2bd09f30ddc1599619c63aa4452b16e1037bf10af070c055ae48cbd7)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.16.2-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.16.2-1.el9.aarch64.rpm") (SHA256 checksum 4edb0315c050b3b0699cb244fe36b987c9fd2921999cf7519fb669354d2efe2d)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.16.2-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.16.2-1.el9.aarch64.rpm") (SHA256 checksum eae2064d9523df9f819ef4c7950a0ad15ef8bb01d8dcec062ee2558f5bebf029)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.16.2-1.el9.aarch64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.16.2-1.el9.aarch64.rpm") (SHA256 checksum f9f4073ebcde2b654b706efb1c0f99c08fe24903576e760029097b0e3c783f6a)

RHEL 8 (8.3+)
Download version 5.16.2 software for RHEL 8 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.16.2-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.16.2-1.el8.x86_64.rpm") (SHA256 checksum 9a3e023fd5ac8c444ef07bb28b96e81b467e066c9dc2da19f648f38eb04d05c9)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.16.2-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.16.2-1.el8.x86_64.rpm") (SHA256 checksum 6fc6ca58f16fe2f486f4730cd0a6029eeeebae98b3aed41fd8c605fe5c36c7a0)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.16.2-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.16.2-1.el8.x86_64.rpm") (SHA256 checksum cb6e9eccfeebca7377b1fb815c2ae306b39b271513ce73a6cd5f1dccb55eac4c)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.16.2-1.el8.x86_64.rpm "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.16.2-1.el8.x86_64.rpm") (SHA256 checksum e848f3f2221e7f6b984bd2001331f9e90f20e6d7351484e4e2f12431c00d87e5)

Ubuntu 24.04 LTS
Download version 5.16.2 software for Ubuntu 24.04 LTS on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.16.2-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.16.2-1_u24.04_amd64.deb") (SHA256 checksum d993f8c84d15cf93432b73cb37693c4ab68b3e765c35742adef3f947744b9893)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.16.2-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.16.2-1_u24.04_amd64.deb") (SHA256 checksum 055f0e4cc74ec7ead77fff3970422b4f1729e26a2cf3cc2be530f0e6a06f887e)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.16.2-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.16.2-1_u24.04_amd64.deb") (SHA256 checksum 5bd62f8f5cb3ff4ae9430020aa4f5c8a29cb635674d2400d989f512c370c755c)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.16.2-1_u24.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.16.2-1_u24.04_amd64.deb") (SHA256 checksum de263f6035cf7280a982434448aa079164050e4a09508816fd06bf000cf15f0c)

Download version 5.16.2 software for Ubuntu 24.04 LTS on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.16.2-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.16.2-1_u24.04_arm64.deb") (SHA256 checksum a6496f28f82f3e92b0acc8e3ae1fbe230a6d3ed82586e8ca6fe6d2f82c275e7c)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.16.2-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.16.2-1_u24.04_arm64.deb") (SHA256 checksum 82275d6ac2628b4291162e3609d6788b4cf01d6488a9b6a84ed8787a5a96e873)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.16.2-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.16.2-1_u24.04_arm64.deb") (SHA256 checksum 67800957c69efca0fe01623364cb3b152f2780d15624955130d507a3f591e8e5)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.16.2-1_u24.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.16.2-1_u24.04_arm64.deb") (SHA256 checksum 088f53d75250aa0ce3db7a7ba3f06ad7804b3dbeed6226683a3252890a867ac6)

Ubuntu 22.04 LTS
Download version 5.16.2 software for Ubuntu 22.04 LTS on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.16.2-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.16.2-1_u22.04_amd64.deb") (SHA256 checksum b9799ba75fb8885782283abae7f49aa76a72d27f692654dd3a415157f0ea9043)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.16.2-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.16.2-1_u22.04_amd64.deb") (SHA256 checksum 3c7675e9b7fa4bb692865559f09fc1f9fd78dadb97d8bd6b5d1fc03367d75b86)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.16.2-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.16.2-1_u22.04_amd64.deb") (SHA256 checksum 37c21821ad4d9fde9551112e8a6d7ec6b7bb62a540c0c08b6edd650d5c87b5cf)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.16.2-1_u22.04_amd64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.16.2-1_u22.04_amd64.deb") (SHA256 checksum 7d3a724892e993aebfb06ad5c3d1ef8fc650d65dff0a7de3cb9c17c089badc58)

Download version 5.16.2 software for Ubuntu 22.04 LTS on ARM64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.16.2-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.16.2-1_u22.04_arm64.deb") (SHA256 checksum 8a2b392e48b7f9021966f6c457444ddd0964f9bb85b7ecb988bc0d372bbef6c9)
- [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.16.2-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.16.2-1_u22.04_arm64.deb") (SHA256 checksum cca0736d208d59d070ced8b82181e24919f21fbf0497e5a8a2f40436e06a8dd9)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.16.2-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.16.2-1_u22.04_arm64.deb") (SHA256 checksum c12e1b9bfe1cc78ecf35892050dd06904c6a29736cc628ac1481dca4ec3e3bfe)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.16.2-1_u22.04_arm64.deb "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.16.2-1_u22.04_arm64.deb") (SHA256 checksum 586ee7663d54e76652e9f073772fcbda218dc3c6432a221d664ffbabee3590cd)

Windows Server 2025
Download version 5.16.2 software for Windows Server 2025 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.16.2-1.msi") (SHA256 checksum b5f55bc72fc994244f09e0252c7fc4a3ddf9607b20860c8718ff1d8a3db0a177)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.16.2-1.msi") (SHA256 checksum c28ea8164f277bf067f4630d433ab7090b370225116a2d594dd563dfb5f9f991)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.16.2-1.msi") (SHA256 checksum db708fc33bdc91b9ad554aa63de86a572d3ccff4ba3ab10feac9c5fd9ed79b94)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.16.2-1.msi") (SHA256 checksum c060be59673f325240bd0f1ccc9d9d97639eb7937fa323d71e223451bc0d2e19)

Windows Server 2022
Download version 5.16.2 software for Windows Server 2022 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.16.2-1.msi") (SHA256 checksum b5f55bc72fc994244f09e0252c7fc4a3ddf9607b20860c8718ff1d8a3db0a177)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.16.2-1.msi") (SHA256 checksum c28ea8164f277bf067f4630d433ab7090b370225116a2d594dd563dfb5f9f991)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.16.2-1.msi") (SHA256 checksum db708fc33bdc91b9ad554aa63de86a572d3ccff4ba3ab10feac9c5fd9ed79b94)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.16.2-1.msi") (SHA256 checksum c060be59673f325240bd0f1ccc9d9d97639eb7937fa323d71e223451bc0d2e19)

Windows Server 2019
Download version 5.16.2 software for Windows Server 2019 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.16.2-1.msi") (SHA256 checksum b5f55bc72fc994244f09e0252c7fc4a3ddf9607b20860c8718ff1d8a3db0a177)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.16.2-1.msi") (SHA256 checksum c28ea8164f277bf067f4630d433ab7090b370225116a2d594dd563dfb5f9f991)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.16.2-1.msi") (SHA256 checksum db708fc33bdc91b9ad554aa63de86a572d3ccff4ba3ab10feac9c5fd9ed79b94)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.16.2-1.msi") (SHA256 checksum c060be59673f325240bd0f1ccc9d9d97639eb7937fa323d71e223451bc0d2e19)

Windows Server 2016
Download version 5.16.2 software for Windows Server 2016 on x86_64 architecture:

- [PKCS #11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.16.2-1.msi") (SHA256 checksum b5f55bc72fc994244f09e0252c7fc4a3ddf9607b20860c8718ff1d8a3db0a177)
- [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.16.2-1.msi") (SHA256 checksum c28ea8164f277bf067f4630d433ab7090b370225116a2d594dd563dfb5f9f991)
  - [Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.16.2-javadoc.jar") (SHA256 checksum 17029e68946b83d47c8512f824599338e7315a99317e4fc33a2058cdc5512d0d)

- [CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.16.2-1.msi") (SHA256 checksum db708fc33bdc91b9ad554aa63de86a572d3ccff4ba3ab10feac9c5fd9ed79b94)
- [Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.16.2-1.msi "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.16.2-1.msi") (SHA256 checksum c060be59673f325240bd0f1ccc9d9d97639eb7937fa323d71e223451bc0d2e19)

Client SDK 5.16.2 adds support for RHEL 10 platform and removes support for Ubuntu 20.04 LTS.
Client SDK 5.16.2 also adds support for JCE Provider and KSP with new features, while delivering bug fixes and improvements across other SDKs.

###### Platform support

- Added RHEL 10 support for x86 and ARM architectures.
  - OpenSSL Engine is not supported in RHEL 10 as part of Red Hat's transition to the newer Provider-based architecture introduced in OpenSSL 3.0.

###### CloudHSM CLI

- Fixed a bug where signing with prehashed data did not clear tokens in interactive mode.
- Fixed a bug in `quorum token-sign list` that previously caused errors when three or more tokens were present.

###### JCE provider

- Added support for finding Elliptic Curve (EC) keys using ECParameters and ECPoint for hsm2m.medium types.
- Added `sharedInfo` parameter support for ECDH with X9.63 KDF.

###### PKCS #11 library

- Added support for finding Elliptic Curve (EC) keys using ECParameters and ECPoint for hsm2m.medium types.

###### Bug fixes/Improvements

- Enhanced token listing functionality to display more tokens in a single operation.
- Fixed key usage token clearing issue in CloudHSM CLI interactive mode when signing with prehashed data.
- Resolved a known issue where some HSM throttled operations on hsm2m.medium would not be automatically retried.
  Refer to [Issue: Operations can fail during backup creation](ki-hsm2m-medium.md#ki-hsm2m-medium-8 "ki-hsm2m-medium.md#ki-hsm2m-medium-8") for details.

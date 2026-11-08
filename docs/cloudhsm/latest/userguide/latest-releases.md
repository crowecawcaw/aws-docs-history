

# AWS CloudHSM latest Client SDK release
<a name="latest-releases"></a>

In March 2021, AWS CloudHSM released Client SDK version 5.0.0, which introduces an all-new Client SDK with different requirements, capabilities, and platform support. 

Client SDK 5 is fully supported for production environments, and offers the same components and level of support as Client SDK 3. For more information, see [Compare AWS CloudHSM Client SDK component support](sdk3-compare.md).

**Note**  
Starting CloudHSM SDK 5.17, we are updating our service level agreement to support up to 3 prior minor versions and one year from the release date of an SDK version. We will release new versions of the CloudHSM SDK to deliver new features and for security, stability, performance fixes. We will disable download links for older and unsupported versions of the CloudHSM SDK as new versions become available.

This section includes the latest version of the Client SDK. For information about previous releases, see [Previous SDK Releases](client-version-previous.md). For deprecated versions, see [Deprecated SDK Releases](deprecated.md).

## Client SDK 5 release: Version 5.18.1
<a name="client-version-5-18-1"></a>

------
#### [ Amazon Linux 2023 ]

Download version 5.18.1 software for Amazon Linux 2023 on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.18.1-1.amzn2023.x86_64.rpm) (SHA256 checksum a0b0c451f6f7681e05c65844f5bc5576ea0ac31c8d3e252f61c74e66ee655532) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.18.1-1.amzn2023.x86_64.rpm) (SHA256 checksum 0731667d881f80a9c5af98f81342a797c34d8e96f769a6fb40f7506436c928a7) 
+ [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.18.1-1.amzn2023.x86_64.rpm) (SHA256 checksum 14f0273c3ef991098d24d0dd8d646c845f92df737e65bc72f4c9a1c4ca06b92b) 
+ [ JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.18.1-1.amzn2023.x86_64.rpm) (SHA256 checksum 1697d9739c5079d905cc25e231a35230510c5239d304dc80bb46323e22f398fa) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.18.1-1.amzn2023.x86_64.rpm) (SHA256 checksum a04d197e87dea998cee2523d01d21db1b5244abb23344ac24ce6b86758bce34a)

Download version 5.18.1 software for Amazon Linux 2023 on ARM64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-pkcs11-5.18.1-1.amzn2023.aarch64.rpm) (SHA256 checksum afa8c577db765c4b29b916373915ec562be2436510693ab22385dcc50f3c0543) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-dyn-5.18.1-1.amzn2023.aarch64.rpm) (SHA256 checksum 42b7da584581963170f0fb53ea02dcc59ea356ff49689619e11b80fc29588d12) 
+ [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-openssl-provider-5.18.1-1.amzn2023.aarch64.rpm) (SHA256 checksum 71e2a839077ab698f5c3fe63f5aca57c6f5d0157724a65ef3a6d50648b3172ef) 
+ [ JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-jce-5.18.1-1.amzn2023.aarch64.rpm) (SHA256 checksum 04f996a5404b641fbee619f52125d0db314231c50466eb27c25f92f4f42602c1) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Amzn2023/cloudhsm-cli-5.18.1-1.amzn2023.aarch64.rpm) (SHA256 checksum 559f367a17425721ecb726d69aae534e2d6efcae97133a2b03644f63d86843b9)

------
#### [ Amazon Linux 2 ]

Download version 5.18.1 software for Amazon Linux 2 on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.18.1-1.el7.x86_64.rpm) (SHA256 checksum 7d59d824ec2179b7e963947f2e1a698af96dc9847c12663ddbd5973c7fbeba54) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.18.1-1.el7.x86_64.rpm) (SHA256 checksum 549c4b9638a0fbddebd5110311051428c2001b1625f92259e2a101532f49a485) 
+ [ JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.18.1-1.el7.x86_64.rpm) (SHA256 checksum 6bedc5cf74a74a117a17f4036d4a7295b90aea0bfa145944bfb5e2996d6fb919) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.18.1-1.el7.x86_64.rpm) (SHA256 checksum edb2ea9da4226d13a9445ee2e7d64bbdde93b377f9127d75bd17236427bb251d)

Download version 5.18.1 software for Amazon Linux 2 on ARM64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-pkcs11-5.18.1-1.el7.aarch64.rpm) (SHA256 checksum 62ac7daa6a229c85ecf0d501c46b460ff09e2a47730efcb539f2d0185df8f999) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-dyn-5.18.1-1.el7.aarch64.rpm) (SHA256 checksum a6b6db026d404b963126b983e59bdf35d2bf16415454c9ff52e9553cda916deb) 
+ [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-jce-5.18.1-1.el7.aarch64.rpm) (SHA256 checksum 80493ee52daecac103ca62bce669f2168daa17c0b68e6bc688f05c7afde9075e) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL7/cloudhsm-cli-5.18.1-1.el7.aarch64.rpm) (SHA256 checksum 837d11add1ba45b5aed47eaa5f4f36b3c5032164dd8ebc8544a81e4b0f348ae3)

------
#### [ RHEL 10 (10.0\+) ]

Download version 5.18.1 software for RHEL 10 on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.18.1-1.el10.x86_64.rpm) (SHA256 checksum 74e1e4eff3e274dde1f2e13adabb308ce97988a6bc4b83cb1df6ee3ce6215569) 
+ [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.18.1-1.el10.x86_64.rpm) (SHA256 checksum d276326ae7441fafcc986da42606429b58d706c85376cff61db1f3a81d995504) 
+ [ JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.18.1-1.el10.x86_64.rpm) (SHA256 checksum b9a3d0715eea91b3b571ab2d5baa5ff852e25fbdbfa9eac8148436b2df11f712) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.18.1-1.el10.x86_64.rpm) (SHA256 checksum 3fab44b25cfb77f963be9a87737b5ce2692268b4b96737848d930c48ee5e0337)

Download version 5.18.1 software for RHEL 10 on ARM64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-pkcs11-5.18.1-1.el10.aarch64.rpm) (SHA256 checksum 33f96eaa659d77076b33efa672570e302f092b111491980ebf518aea7eb2c8d2) 
+ [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-openssl-provider-5.18.1-1.el10.aarch64.rpm) (SHA256 checksum 2773b183fd40e43bf662fc5013c1d00a022f43e4bfe51cbec9f62358c7195f28) 
+ [ JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-jce-5.18.1-1.el10.aarch64.rpm) (SHA256 checksum a001f3061bd2ad9ca6d95beb0e273f9b94543697a0e282ed3d156fa35efd554b) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL10/cloudhsm-cli-5.18.1-1.el10.aarch64.rpm) (SHA256 checksum 4a00d86a2c91aa516340cd512d18434ef5a7bcefc77dac072d98a3558af5ad78)

------
#### [ RHEL 9 (9.2\+) ]

Download version 5.18.1 software for RHEL 9 on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.18.1-1.el9.x86_64.rpm) (SHA256 checksum 172f357b75240ed02226fd1775ae6d4f6c9e800ba83a26937ea63a5d74f8926d) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.18.1-1.el9.x86_64.rpm) (SHA256 checksum ccfbd8924c20318c97e6d3dad7b79120d661ddd37885bd6cfe3d64812887ed18) 
+ [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.18.1-1.el9.x86_64.rpm) (SHA256 checksum 3c8d0327db5a5ae8da41faa7e289908d74948018fe913ddc44a5e2db290bc358) 
+ [ JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.18.1-1.el9.x86_64.rpm) (SHA256 checksum 9a92d9d386380e22a8eca1c7e7568e0bc9139c2af78097c73ee03b95531ff987) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.18.1-1.el9.x86_64.rpm) (SHA256 checksum 125f01e9bb93886a1f6ffc32780478bd9aa60feaa85af8c241073db8b7ea7842)

Download version 5.18.1 software for RHEL 9 on ARM64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-pkcs11-5.18.1-1.el9.aarch64.rpm) (SHA256 checksum a47b507784ee6b197419ce22b8613f2449ab4292f2b4c7bb505378c73624eaab) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-dyn-5.18.1-1.el9.aarch64.rpm) (SHA256 checksum 5a38660af965396b14ab22a34f406f5980b60255c8dae32ef2d34ee8f344aebb) 
+ [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-openssl-provider-5.18.1-1.el9.aarch64.rpm) (SHA256 checksum e97c87c010655c547e372d0946828b1256b421f806a915f9acf5d74516a0b3fb) 
+ [ JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-jce-5.18.1-1.el9.aarch64.rpm) (SHA256 checksum 0abcd3408f11fe9b761ca77c826a412ff052fe5b55d6aee809b1b8362b9ff909) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL9/cloudhsm-cli-5.18.1-1.el9.aarch64.rpm) (SHA256 checksum 1be71ffa7f1b190252e96fd173dd1a80c566c4a55b77e5f4bf4973b496b63d65)

------
#### [ RHEL 8 (8.3\+) ]

Download version 5.18.1 software for RHEL 8 on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.18.1-1.el8.x86_64.rpm) (SHA256 checksum 0eaf573da77acaec72051c6b613d1642672eb7a4ad713c1357db143275017a1e) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.18.1-1.el8.x86_64.rpm) (SHA256 checksum fa94f16af1242c862138ba0080b187fefc9b32ca3a86bf7e668480c71ae9941d) 
+ [ JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.18.1-1.el8.x86_64.rpm) (SHA256 checksum 82ed7ccbbd5cf4054680aab4091ce52b70f6ce8525084d9cee123dd57bdbb553) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.18.1-1.el8.x86_64.rpm) (SHA256 checksum 5121863ebe470dcb4989eaa120c926eb2cdee362259353fc7f8a8af2d593cf78)

Download version 5.18.1 software for RHEL 8 on ARM64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-pkcs11-5.18.1-1.el8.aarch64.rpm) (SHA256 checksum d7315f60e69f58ad1fe7b7adcca468cdbf3d796e7304f2e8f2f789ef102f5027) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-dyn-5.18.1-1.el8.aarch64.rpm) (SHA256 checksum 812d6ae782083c0fe33231b00750ce610d4ad52be021c27c6b634ebbb5553da8) 
+ [ JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-jce-5.18.1-1.el8.aarch64.rpm) (SHA256 checksum a5fd30e498e5a29956801a96eac34a929e22009f5568253f096250bf630d1049) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/EL8/cloudhsm-cli-5.18.1-1.el8.aarch64.rpm) (SHA256 checksum 17368474510f9f3aa1eeaf2cc78422e7c88c084e2e32ee1967b72cb0a2c6e5b6)

------
#### [ Ubuntu 26.04 LTS ]

Download version 5.18.1 software for Ubuntu 26.04 LTS on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-pkcs11_5.18.1-1_u26.04_amd64.deb) (SHA256 checksum 1bc45ca1d62f213388f7c4e86e9044803e9b063d4c8eaf200575574de3745b33) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-dyn_5.18.1-1_u26.04_amd64.deb) (SHA256 checksum fe1bb39766154999b8b00805e54f3cca3957a71041759883c1fd21606945b2f0) 
+ [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-openssl-provider_5.18.1-1_u26.04_amd64.deb) (SHA256 checksum 06a7d6df80296494037ec134182dcb4363d3fcf3c27a5e026a9540a623b6c5d8) 
+ [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-jce_5.18.1-1_u26.04_amd64.deb) (SHA256 checksum 5ed31a6352a75574f149ac30def6e8c8f578b6847dc29397f9b27d36edc54bb5) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-cli_5.18.1-1_u26.04_amd64.deb) (SHA256 checksum d3c919e394645687e719931988a9daad282ef253e7f90e1aee5886ef04ff1d52)

Download version 5.18.1 software for Ubuntu 26.04 LTS on ARM64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-pkcs11_5.18.1-1_u26.04_arm64.deb) (SHA256 checksum 394c6e774a40e7d201de404dde7cd733c895320133f3581e4d25e4f29560fea1) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-dyn_5.18.1-1_u26.04_arm64.deb) (SHA256 checksum b68d2b55ef52df5fb460f7234b99b031d6baa468a5dd62e72291e7bb8d5e71e6) 
+ [OpenSSL Provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-openssl-provider_5.18.1-1_u26.04_arm64.deb) (SHA256 checksum bd01f72a10705ff4c1ce369b02cd5f3bc24bdf6e433ed215ab2592cd2abb586f) 
+ [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-jce_5.18.1-1_u26.04_arm64.deb) (SHA256 checksum bd3a91df4fa1bf4b0733dcdb0ccfb2b24ff3ed66358ff13167c2a4ba6b935d5b) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Resolute/cloudhsm-cli_5.18.1-1_u26.04_arm64.deb) (SHA256 checksum 1acc59c19ac3c0153098c1721597cb66930f905e707827cccd775857f78e1f95)

------
#### [ Ubuntu 24.04 LTS ]

Download version 5.18.1 software for Ubuntu 24.04 LTS on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.18.1-1_u24.04_amd64.deb) (SHA256 checksum deaf94a18ed879bc68bf064fcd73117506a28213aded31a8fd5d9878fcbf38b7) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.18.1-1_u24.04_amd64.deb) (SHA256 checksum 6a1ba5ab50477aeaf38327b0cfeb2260defd4e757981d308d8aab683a05fee79) 
+ [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.18.1-1_u24.04_amd64.deb) (SHA256 checksum 61760c8b5a6171595b47d26c49d0ea9ac54b21fa4e6cc1386f2a9e5ceb685ea5) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.18.1-1_u24.04_amd64.deb) (SHA256 checksum 58632028fc690ef588b3893513989dc705812bcf820aa69a0db3eb3a177f62c9)

Download version 5.18.1 software for Ubuntu 24.04 LTS on ARM64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-pkcs11_5.18.1-1_u24.04_arm64.deb) (SHA256 checksum fdc7a81139c30ff5b1caad3c01f6bc1d3cc7aa52907d5c4deabdf46c9cdd2974) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-dyn_5.18.1-1_u24.04_arm64.deb) (SHA256 checksum 884492016310cca8a0025964be00e1de872d5e88bcc400c209f11610be0599bc) 
+ [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-jce_5.18.1-1_u24.04_arm64.deb) (SHA256 checksum 7cc443e1c9f6ac0b6990a6058124c429b620e9068952bcf1133cd4e37f910c6c) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Noble/cloudhsm-cli_5.18.1-1_u24.04_arm64.deb) (SHA256 checksum ce8f26bdb45b2ea11855d5f50f197df2b9ffe590b87a1dbceb561a3eb258497c)

------
#### [ Ubuntu 22.04 LTS ]

Download version 5.18.1 software for Ubuntu 22.04 LTS on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.18.1-1_u22.04_amd64.deb) (SHA256 checksum 7b6eb51efdbe49bf21d059fd70d1e00cc68890e9e7ffc07c1424b22883fe1aa2) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.18.1-1_u22.04_amd64.deb) (SHA256 checksum fe410ed56aa98c07f95433af6cd0235f92d80cf67a565ec87df145ac4c34e1c8) 
+ [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.18.1-1_u22.04_amd64.deb) (SHA256 checksum 3700430b4c178f11b0043a4024d705775a81e03f9ef13ded48aff975459834db) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.18.1-1_u22.04_amd64.deb) (SHA256 checksum 404f46e949708b5a6b0fe966d3b97fb0a35b6b322c240cda7ac723543ce3be7b)

Download version 5.18.1 software for Ubuntu 22.04 LTS on ARM64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-pkcs11_5.18.1-1_u22.04_arm64.deb) (SHA256 checksum 5276bae3d2bf8b894c7e0e010d72540c5ceb60e16d114b98b23b0f2a35ebd654) 
+ [OpenSSL Dynamic Engine](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-dyn_5.18.1-1_u22.04_arm64.deb) (SHA256 checksum d48b29aac2c8b8cc600481bc74951ffddc8679c649501b491bcd6b4347286318) 
+ [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-jce_5.18.1-1_u22.04_arm64.deb) (SHA256 checksum 94f23cf5b6a92b23c170191f6d9fc2edbc3e33ad9f2c5ba0b13863e605e3d95b) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Jammy/cloudhsm-cli_5.18.1-1_u22.04_arm64.deb) (SHA256 checksum a55dd969ce43f2cfab7e8efa7aeaa062d60be3817b7d3539581200a6c1d46f65)

------
#### [ Windows Server 2025 ]

Download version 5.18.1 software for Windows Server 2025 on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.1-1.msi) (SHA256 checksum 80586fd0a02f53441a4a55a43c25df5e61fbb755613f964b56a57fb5d4cd5e19) 
+ [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.1-1.msi) (SHA256 checksum 569ba50a13a984e7d83d3023890dd06cad24db096d0f7373849917c922f5c781) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.1-1.msi) (SHA256 checksum 67c71e95c1d67dcb3f1c0d8cd2b4fca54041784c9b0fd384d7fd07f3520743d4)
+ [ Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.1-1.msi) (SHA256 checksum b059414cb725f934a3a0af2db41ffbf8ecd69e1c7c4921897bf97a085d0f3261)

------
#### [ Windows Server 2022 ]

Download version 5.18.1 software for Windows Server 2022 on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.1-1.msi) (SHA256 checksum 80586fd0a02f53441a4a55a43c25df5e61fbb755613f964b56a57fb5d4cd5e19) 
+ [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.1-1.msi) (SHA256 checksum 569ba50a13a984e7d83d3023890dd06cad24db096d0f7373849917c922f5c781) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.1-1.msi) (SHA256 checksum 67c71e95c1d67dcb3f1c0d8cd2b4fca54041784c9b0fd384d7fd07f3520743d4)
+ [ Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.1-1.msi) (SHA256 checksum b059414cb725f934a3a0af2db41ffbf8ecd69e1c7c4921897bf97a085d0f3261)

------
#### [ Windows Server 2019 ]

Download version 5.18.1 software for Windows Server 2019 on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.1-1.msi) (SHA256 checksum 80586fd0a02f53441a4a55a43c25df5e61fbb755613f964b56a57fb5d4cd5e19) 
+ [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.1-1.msi) (SHA256 checksum 569ba50a13a984e7d83d3023890dd06cad24db096d0f7373849917c922f5c781) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.1-1.msi) (SHA256 checksum 67c71e95c1d67dcb3f1c0d8cd2b4fca54041784c9b0fd384d7fd07f3520743d4)
+ [ Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.1-1.msi) (SHA256 checksum b059414cb725f934a3a0af2db41ffbf8ecd69e1c7c4921897bf97a085d0f3261)

------
#### [ Windows Server 2016 ]

Download version 5.18.1 software for Windows Server 2016 on x86\_64 architecture:
+ [PKCS \#11 library](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMPKCS11-5.18.1-1.msi) (SHA256 checksum 80586fd0a02f53441a4a55a43c25df5e61fbb755613f964b56a57fb5d4cd5e19) 
+ [JCE provider](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMJCE-5.18.1-1.msi) (SHA256 checksum 569ba50a13a984e7d83d3023890dd06cad24db096d0f7373849917c922f5c781) 
  + [ Javadocs for AWS CloudHSM](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/JCE/cloudhsm-jce-5.18.1-javadoc.jar) (SHA256 checksum a96cadadc938e2b1b9633b90751a8b0ef7cc31af1ac9cdd23ed34a8b6cba91ec)
+ [ CloudHSM CLI](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMCLI-5.18.1-1.msi) (SHA256 checksum 67c71e95c1d67dcb3f1c0d8cd2b4fca54041784c9b0fd384d7fd07f3520743d4)
+ [ Key Storage Provider (KSP)](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-5.18.1-1.msi) (SHA256 checksum b059414cb725f934a3a0af2db41ffbf8ecd69e1c7c4921897bf97a085d0f3261)

------

 Client SDK 5.18.1 includes bug fixes and improvements. 
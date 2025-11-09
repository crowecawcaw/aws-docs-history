# Release: Elastic Beanstalk supports first wave of Graviton gradual rollout on October 13, 2021

AWS Elastic Beanstalk supports first wave of Graviton gradual rollout.

**Release date:** October 13, 2021

## Changes

Elastic Beanstalk
introduced
a gradual rollout of support for Graviton instance types. This first wave of rollout is launching in the following six AWS Regions:

- US East (Ohio) – us-east-2
- US East (N. Virginia) – us-east-1
- US West (N. California) – us-west-1
- US West (Oregon) – us-west-2
- Europe (Frankfurt) – eu-central-1
- South America (São Paulo) – sa-east-1

In these
Regions,
the following platform branches now support the following Graviton instance types:

- Docker running on 64bit Amazon Linux 2
- Node.js 14 running on 64bit Amazon Linux 2
- Node.js 12 running on 64bit Amazon Linux 2
- Python 3.8 running on 64bit Amazon Linux 2
- Python 3.7 running on 64bit Amazon Linux 2
- Tomcat 8.5 with Corretto 11 running on 64bit Amazon Linux 2
- Tomcat 8.5 with Corretto 8 running on 64bit Amazon Linux 2
- PHP 8.0 running on 64bit Amazon Linux 2
- PHP 7.4 running on 64bit Amazon Linux 2
- Ruby 2.7 running on 64bit Amazon Linux 2
- Go 1 running on 64bit Amazon Linux 2

With this release, we recommend that you use the Elastic Beanstalk Console and AWS CLI for Graviton instance type configuration. Graviton instances use different OS
images than the ones that are used by x86 instances. Currently, you need to manually choose an appropriate image. When you choose a Graviton instance
type, you must also provide the image ID for your platform branch and Region.

For a list of Graviton image IDs for each supported platform branch and Region, see [Graviton image IDs for supporting platforms](#release-2021-10-13-graviton-wave1.graviton "#release-2021-10-13-graviton-wave1.graviton") on this page.

For instructions on how to create and configure environments using Graviton instances, see [Amazon EC2 instance types](../dg/using-features.managing.md#using-features.managing.ec2.instance-types "../dg/using-features.managing.md#using-features.managing.ec2.instance-types") in the
_AWS Elastic Beanstalk Developer Guide_.

## Graviton image IDs for supporting platforms

###### Elastic Beanstalk provides enhanced console support for Graviton as of November 24, 2021

Customers are no longer required to manually enter the listed custom AMIs to create a new Elastic Beanstalk environment with arm64 processor architecture.

If you created environments with the custom AMIs provided in the first wave release, we recommend that you remove the custom AMIs and upgrade to the
latest platform version. For specific instructions, see
[Recommendations for Graviton arm64 first
wave environments](../dg/using-features.managing.md#using-features.managing.ec2.graviton-wave-1 "../dg/using-features.managing.md#using-features.managing.ec2.graviton-wave-1") in the _AWS Elastic Beanstalk Developer Guide_.

The
following sections list the Graviton image IDs for each platform branch that supports Graviton instance types. The images are specific to each supporting
AWS Region.

| Platform version                                           | Graviton image ID     | x86 image ID          |
| ---------------------------------------------------------- | --------------------- | --------------------- |
| 64bit Amazon Linux 2 v3.4.7 running Docker                 | ami-0d81a697b71b7bf07 | ami-05695573c36ccc1cf |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 11 | ami-0731b0883326ddda7 | ami-0c0471aa9522b7f99 |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 8  | ami-0ca5a8ddcb8f327bd | ami-0ae56568da51f9b03 |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 12             | ami-017ff872b14a73911 | ami-09658d5c619827fa3 |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 14             | ami-005700c545676834f | ami-00308a0faa526f7d5 |
| 64bit Amazon Linux 2 v3.3.6 running Ruby 2.7               | ami-0afe1e2bc78702be8 | ami-0ef09d3e6b6e120aa |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.7             | ami-08800d7cacd2778a2 | ami-0cd04629cb8919969 |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.8             | ami-0428cd9e6e16272d8 | ami-0d2abb7aa94f07b5d |
| 64bit Amazon Linux 2 v3.3.6 running PHP 7.4                | ami-043c2fe01517fee08 | ami-0372ca355f0631dd9 |
| 64bit Amazon Linux 2 v3.3.6 running PHP 8.0                | ami-028cba9013bc637a6 | ami-0739533aa5b6a86c7 |
| 64bit Amazon Linux 2 v3.4.1 running Go 1                   | ami-0167fb079097ef915 | ami-0803c6bf11d776e3e |

| Platform version                                           | Graviton image ID     | x86 image ID          |
| ---------------------------------------------------------- | --------------------- | --------------------- |
| 64bit Amazon Linux 2 v3.4.7 running Docker                 | ami-0fbdb88ce139244bf | ami-0c4d28cfe48cc422e |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 11 | ami-00e7b90f6d15fb548 | ami-0dfbd8b3d861e8aac |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 8  | ami-0d0c9c0fa9a42b771 | ami-020f5d80a0545c8cc |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 12             | ami-0dd8668d2e8b23878 | ami-0e1ddc69db522afb7 |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 14             | ami-04fb2d6b317cf1a80 | ami-03982d1439cb6b7fb |
| 64bit Amazon Linux 2 v3.3.6 running Ruby 2.7               | ami-06d58b8cb96faf8de | ami-0f0baea233d6c0d8d |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.7             | ami-061d81a0ff2055236 | ami-0dd11e27e176aaf5b |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.8             | ami-0665cb9e7ae0326fe | ami-030060849c43d15cd |
| 64bit Amazon Linux 2 v3.3.6 running PHP 7.4                | ami-0f3cd4fdbbc4f374e | ami-041219a66d0e62231 |
| 64bit Amazon Linux 2 v3.3.6 running PHP 8.0                | ami-04de7ac2259913496 | ami-0a2aa69f60f0db690 |
| 64bit Amazon Linux 2 v3.4.1 running Go 1                   | ami-04e4857fb761845cd | ami-0684dc7c9ec0edb2a |

| Platform version                                           | Graviton image ID     | x86 image ID          |
| ---------------------------------------------------------- | --------------------- | --------------------- |
| 64bit Amazon Linux 2 v3.4.7 running Docker                 | ami-0e88c6b05c0de1dd8 | ami-0f34cb0eaed253615 |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 11 | ami-0edaedc27675ab807 | ami-0132cfc935b57cac5 |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 8  | ami-0f029c18fe886357f | ami-0cba70acabaa88266 |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 12             | ami-06f253a6a16c84cd2 | ami-01e11f55a24b5da22 |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 14             | ami-0b35d2f960c29d3d7 | ami-01b2a018cf39d149a |
| 64bit Amazon Linux 2 v3.3.6 running Ruby 2.7               | ami-0e564081ad324e3eb | ami-086da5c4ae6595c61 |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.7             | ami-08f80037e4e736432 | ami-05897a66da7d8d0df |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.8             | ami-050c462c86e96861f | ami-0ace93bfe5e1d3991 |
| 64bit Amazon Linux 2 v3.3.6 running PHP 7.4                | ami-04b54b1ed0c003aa0 | ami-0a21217b9014b2bfd |
| 64bit Amazon Linux 2 v3.3.6 running PHP 8.0                | ami-062364b89b5e487a2 | ami-0d5aab2eeaa1c6567 |
| 64bit Amazon Linux 2 v3.4.1 running Go 1                   | ami-0909c91d5269e31ea | ami-08e1ddaa6c0fea773 |

| Platform version                                           | Graviton image ID     | x86 image ID          |
| ---------------------------------------------------------- | --------------------- | --------------------- |
| 64bit Amazon Linux 2 v3.4.7 running Docker                 | ami-02b1ab520319e74be | ami-0f4f0c5c4b516f4f6 |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 11 | ami-0a697f58fcc096123 | ami-07fd7e930ba9667e2 |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 8  | ami-0a638cf33cbb3a439 | ami-0b1e94b95052802fb |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 12             | ami-03259aeb4a93b83df | ami-0e3b9fcece4ac8d81 |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 14             | ami-0122cbc939a56bdbd | ami-02a2bf9c48ae60b5d |
| 64bit Amazon Linux 2 v3.3.6 running Ruby 2.7               | ami-06ee2b1f78ad5b80d | ami-01e3a52d772a32c80 |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.7             | ami-0fb08f987f6086130 | ami-0861d9ddcd454bdba |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.8             | ami-0f8c3db10af08b1cc | ami-038f546eb9a9beb62 |
| 64bit Amazon Linux 2 v3.3.6 running PHP 7.4                | ami-045385f52d4c6b937 | ami-08ebf387cdd834b48 |
| 64bit Amazon Linux 2 v3.3.6 running PHP 8.0                | ami-0130ee3c8cd8006bd | ami-0fe2d65328bb2e51f |
| 64bit Amazon Linux 2 v3.4.1 running Go 1                   | ami-08c9eae80a8c647cc | ami-0c6f9efe848321c20 |

| Platform version                                           | Graviton image ID     | x86 image ID          |
| ---------------------------------------------------------- | --------------------- | --------------------- |
| 64bit Amazon Linux 2 v3.4.7 running Docker                 | ami-07e7185f4579f6531 | ami-0e48201b194947727 |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 11 | ami-04ce47ec8e90dcc7c | ami-0856ee4dbe31ea79d |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 8  | ami-08e963ac42a28938c | ami-04398221c977c9af7 |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 12             | ami-0652f348d4eb62f7a | ami-0d5d3d9662d218d42 |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 14             | ami-029bc449dfe2dab4c | ami-0e4c4c0cf785d4ee8 |
| 64bit Amazon Linux 2 v3.3.6 running Ruby 2.7               | ami-0c0cb62914da7c663 | ami-070aa241db40a33f4 |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.7             | ami-07590baf352a7923a | ami-037897deb0d372604 |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.8             | ami-05e126b50d5e078ed | ami-0e8e1de5f68783ffd |
| 64bit Amazon Linux 2 v3.3.6 running PHP 7.4                | ami-08ea109211334ebfe | ami-041bb03df03663aaf |
| 64bit Amazon Linux 2 v3.3.6 running PHP 8.0                | ami-0c24252abe093100f | ami-0cbbcfc94741373f9 |
| 64bit Amazon Linux 2 v3.4.1 running Go 1                   | ami-01ad97ab3f77c4fd8 | ami-0dd8585a6f115d6f2 |

| Platform version                                           | Graviton image ID     | x86 image ID          |
| ---------------------------------------------------------- | --------------------- | --------------------- |
| 64bit Amazon Linux 2 v3.4.7 running Docker                 | ami-0f2b500c362adc1be | ami-016c0cb0caadec0a0 |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 11 | ami-0f944aa28a0a20aac | ami-00d53b22a8c592f86 |
| 64bit Amazon Linux 2 v4.2.6 running Tomcat 8.5 Corretto 8  | ami-037a50f7eb6c5dacf | ami-090c2aad7de6af5ac |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 12             | ami-0ec56fe01f9796d72 | ami-06c94b163577133a9 |
| 64bit Amazon Linux 2 v5.4.6 running Node.js 14             | ami-0c94ce67d0f49de31 | ami-0cec1ff9f4db37f90 |
| 64bit Amazon Linux 2 v3.3.6 running Ruby 2.7               | ami-0a11d43311829e1ee | ami-0a32f9ba888f11b7a |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.7             | ami-043d60e607e7e56a4 | ami-0b70bb27f64210cc2 |
| 64bit Amazon Linux 2 v3.3.6 running Python 3.8             | ami-04e7ee1a17f886c89 | ami-0fabf74ee89428faa |
| 64bit Amazon Linux 2 v3.3.6 running PHP 7.4                | ami-01dfd132dd5173fd2 | ami-04287af763b491f10 |
| 64bit Amazon Linux 2 v3.3.6 running PHP 8.0                | ami-0a1a1fda7ae64a1d1 | ami-0e53b10998f375139 |
| 64bit Amazon Linux 2 v3.4.1 running Go 1                   | ami-0d997a733b63e1400 | ami-0ffb596cd1ec5457f |

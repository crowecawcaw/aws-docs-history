# How AWS CloudHSM works

This topic provides an overview of the basic concepts and architecture you use to securely encrypt data and perform cryptographic operations in HSMs. AWS CloudHSM operates in your own Amazon Virtual Private Cloud (VPC). Before you can use AWS CloudHSM,
you first create a cluster, add HSMs to it, create users and keys, and then use Client SDKs to integrate your HSMs with your application. Once this is done, you use Client SDK logs, AWS CloudTrail,
audit logs, and Amazon CloudWatch to [monitor AWS CloudHSM](get-logs.md "get-logs.md").

Learn AWS CloudHSM's basic concepts and how they work together to help protect your data.

###### Topics

- [AWS CloudHSM clusters](clusters.md "clusters.md")
- [Users in AWS CloudHSM](hsm-users.md "hsm-users.md")
- [Keys in AWS CloudHSM](whatis-hsm-keys.md "whatis-hsm-keys.md")
- [Client SDKs for AWS CloudHSM](client-tools-and-libraries.md "client-tools-and-libraries.md")
- [AWS CloudHSM cluster backups](backups.md "backups.md")
- [Supported Regions for AWS CloudHSM](regions.md "regions.md")

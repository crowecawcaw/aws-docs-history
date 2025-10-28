Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Managing CMK using AWS Management Console

This topic describes how to create and update your KMS CMKs using the AWS Management Console. To follow the procedures described in this topic, you must have permission to manage the KMS key and the Amazon MSF application. The procedures in this topic use a permissive key policy, which is for demonstration and testing purposes only. We **don't recommend** using such a permissive key policy for production workloads. For production workloads, you can use the console, but in real-life scenarios, roles, permissions, and workflows are isolated.

Before you start, create a KMS key. For information about creating a KMS key, see [Create a KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.
2. On the **Streaming applications** page, choose **Create streaming application**.
3. For **Apache Flink version**, make sure that you choose **Apache Flink 1.20**.
4. For **Encryption**, choose **Use customer managed key**.
5. If you don't have a KMS key, choose **Create an AWS KMS key**, and create a KMS key. For information about how to create the key, see [Using the AWS KMS console](../../../kms/latest/developerguide/create-symmetric-cmk.md "../../../kms/latest/developerguide/create-symmetric-cmk.md") in the _AWS Key Management Service Developer Guide_.
6. If you don't have a KMS key, choose **Create an AWS KMS key**, and create a KMS key. For information about how to create the key using console, see [Create a symmetric encryption KMS key](../../../kms/latest/developerguide/create-symmetric-cmk.md "../../../kms/latest/developerguide/create-symmetric-cmk.md").
7. Choose the key in the selector you want to use. Remember only the key with **Enabled** status is allowed.
8. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.
9. On the **Streaming applications** page, choose an application with Flink version 1.20.
10. Choose **Configure**.
11. For **Encryption**, choose **Use customer managed key**.
12. If you don't have a KMS key, choose **Create an AWS KMS key**, and create a KMS key. For information about how to create the key using console, see [Create a symmetric encryption KMS key](../../../kms/latest/developerguide/create-symmetric-cmk.md "../../../kms/latest/developerguide/create-symmetric-cmk.md").
13. Choose the key in the selector you want to use. Remember only the key with **Enabled** status is allowed.
14. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.
15. On the **Streaming applications** page, choose an application with Flink version 1.20.
16. Choose **Configure**.
17. For **Encryption**, choose **Use AWS owned key**.

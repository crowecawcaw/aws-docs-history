

# Managing CMK using AWS Management Console
<a name="manage-cmk-console"></a>

This topic describes how to create and update your KMS CMKs using the AWS Management Console. To follow the procedures described in this topic, you must have permission to manage the KMS key and the Amazon MSF application. The procedures in this topic use a permissive key policy, which is for demonstration and testing purposes only. We **don't recommend** using such a permissive key policy for production workloads. For production workloads, you can use the console, but in real-life scenarios, roles, permissions, and workflows are isolated.

Before you start, create a KMS key. For information about creating a KMS key, see [Create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.

## Create and assign KMS keys
<a name="create-assign-cmks-console"></a>

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.

1. On the **Streaming applications** page, choose **Create streaming application**.

1. For **Apache Flink version**, make sure that you choose **Apache Flink 1.20**.

1. For **Encryption**, choose **Use customer managed key**.

1. If you don't have a KMS key, choose **Create an AWS KMS key**, and create a KMS key. For information about how to create the key, see [Using the AWS KMS console](https://docs.aws.amazon.com/kms/latest/developerguide/create-symmetric-cmk.html) in the *AWS Key Management Service Developer Guide*.

1. If you don't have a KMS key, choose **Create an AWS KMS key**, and create a KMS key. For information about how to create the key using console, see [Create a symmetric encryption KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-symmetric-cmk.html).

1. Choose the key in the selector you want to use. Remember only the key with **Enabled** status is allowed.

## Update an existing application to use CMK
<a name="update-existing-cmk-console"></a>

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.

1. On the **Streaming applications** page, choose an application with Flink version 1.20.

1. Choose **Configure**.

1. For **Encryption**, choose **Use customer managed key**.

1. If you don't have a KMS key, choose **Create an AWS KMS key**, and create a KMS key. For information about how to create the key using console, see [Create a symmetric encryption KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-symmetric-cmk.html).

1. Choose the key in the selector you want to use. Remember only the key with **Enabled** status is allowed.

## Switch from CMK to an AWS owned key
<a name="revert-cmk-to-aok-console"></a>

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.

1. On the **Streaming applications** page, choose an application with Flink version 1.20.

1. Choose **Configure**.

1. For **Encryption**, choose **Use AWS owned key**.
# Your storage virtual machine (SVM) is in a `MISCONFIGURED` state

There are a number of potential causes for a Storage Virtual Machine to get into a `MISCONFIGURED` state, each with their own resolution, as follows.

## Your SVM has an offline volume

Your file system contains a volume which is in an offline state. We recommend that you keep volumes online in an ongoing basis. If you do not online this volume before
your file system’s next maintenance window, Amazon FSx will temporarily online this volume for the duration of the patching operation. To avoid this, please online or delete the volume.

To bring an offline volume back online, use the
[`volume online`](https://docs.netapp.com/us-en/ontap-cli-9141/volume-online.html "https://docs.netapp.com/us-en/ontap-cli-9141/volume-online.html")
ONTAP CLI command, as shown in the following example. If only one SVM (Vserver) exists, you do not need to specify the `-vserver` parameter.

```
`FsxID-abcdef123456::>` `volume online -volume `volume_name` -vserver `svm_name``

`Volume 'vs1:vol1' is now online.`
```

## Your SVM has an offline volume with an iSCSI LUN or an NVMe/TCP namespace

Your file system contains a volume which is in a restricted state. We recommend that you keep volumes online in an ongoing basis. If you do not online this volume before
your file system’s next maintenance window, Amazon FSx will temporarily online this volume for the duration of the patching operation. To avoid this, please online or delete the volume.

To bring an offline volume back online, use the
[`volume online`](https://docs.netapp.com/us-en/ontap-cli-9141/volume-online.html "https://docs.netapp.com/us-en/ontap-cli-9141/volume-online.html")
ONTAP CLI command, as shown in the following example. If only one SVM (Vserver) exists, you do not need to specify the `-vserver` parameter.

```
`FsxID-abcdef123456::>` `volume online -volume `volume_name` -vserver `svm_name``

`Volume 'vs1:vol1' is now online.`
```

## The AWS Secrets Manager secret or KMS key is not configured correctly

Amazon FSx can't establish a connection with your Microsoft Active Directory domain controller or controllers. This is because your AWS Secrets Manager secret or AWS KMS key is not configured correctly. For more information, see [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD-best-practices.md#bp-store-ad-creds-using-secret-manager "self-managed-AD-best-practices.md#bp-store-ad-creds-using-secret-manager").

To resolve the misconfiguration, do the following:

- Verify that the secret ARN is correct and follows the proper format: `arn:aws:secretsmanager:region:account-id:secret:secret-name-6chars`.
- Verify that the secret contains both required fields with non-empty values:
  - `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME` – Your AD service account username.
  - `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD` – Your AD service account password.

- Verify that the secret and key have a resource-based policy that grants the Amazon FSx service principal `fsx.amazonaws.com` permission to retrieve the secret value.

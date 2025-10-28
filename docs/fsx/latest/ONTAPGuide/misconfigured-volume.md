# Your volume is in a `MISCONFIGURED` state

There are a number of potential causes for an ONTAP volume to get into a `MISCONFIGURED` state, described in the following topics.

## Your volume is more than 98% full

Your file system currently contains a volume which is more than 98% full. We recommend that you do not exceed 95% utilization of your volume on an ongoing basis.
If you do not free up space in the volume before your file system’s next maintenance window, Amazon FSx will disable opportunistic locking on the volume, breaking any existing
“oplocks”. Amazon FSx will re-enable oplocks on the volume after the patching process completes. To avoid this, please reduce the volume's storage capacity utilization to below
98%. Some of the ways to achieve this include:

- Increasing the size of the volume.
- Deleting unneeded data.
- Deleting unneeded snapshots.

For more information, see [Updating storage capacity](manage-volume-capacity.md "manage-volume-capacity.md"), and
[Deleting snapshots](manually-delete-snapshots.md "manually-delete-snapshots.md").

## Your offline volume has an iSCSI LUN or an NVMe/TCP namespace

Your file system currently hosts a volume which is in an offline state, and that volume contains an iSCSI LUN, or an NVMe/TCP namespace, or both.
We recommend that you keep volumes online on an ongoing basis. If you do not online this volume before your file system’s next maintenance window,
Amazon FSx will temporarily online this volume for the duration of the patching operation. To avoid this, please online or delete the volume.

To bring an offline volume back online, use the
[`volume online`](https://docs.netapp.com/us-en/ontap-cli-9141/volume-online.html "https://docs.netapp.com/us-en/ontap-cli-9141/volume-online.html")
ONTAP CLI command, as shown in the following example. If only one SVM (Vserver) exists, you do not need to specify the `-vserver` parameter.

```
`FsxID-abcdef123456::>` `volume online -volume `volume_name` -vserver `svm_name``

`Volume 'vs1:vol1' is now online.`
```

## Your offline volume is a FlexCache origin

Your file system contains a FlexCache origin volume which is in an offline state. We recommend that you keep volumes online on an ongoing basis.
If you do not online this volume before your file system’s next maintenance window, Amazon FSx will temporarily online this volume for the duration of the
patching operation. During this time, it is possible that data will be written back to the FlexCache origin volume with data from the cache volume. To avoid
this, please online or delete the volume.

To bring an offline volume back online, use the
[`volume online`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-online.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-online.html")
ONTAP CLI command, as shown in the following example. If only one SVM (Vserver) exists, you do not need to specify the `-vserver` parameter.

```
`FsxID-abcdef123456::>` `volume online -volume `volume_name` -vserver `svm_name``

`Volume 'vs1:vol1' is now online.`
```

## Your offline volume is part of a SnapMirror relationship

Your file system currently hosts a volume that is in an offline state, and that volume is a SnapMirror source or destination.
We recommend that you keep volumes online on an ongoing basis.
If you don't online this volume before your file system’s next maintenance window, Amazon FSx will temporarily online this volume for the duration of the
patching operation and pause the SnapMirror relationship.
During this time, it's possible that data will be written to the SnapMirror destination volume with data from the SnapMirror
source volume. To avoid this, please online or delete the volume.

To bring an offline volume back online, use the
[`volume online`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-online.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-online.html")
ONTAP CLI command, as shown in the following example. If only one SVM (Vserver) exists, you do not need to specify the `-vserver` parameter.

```
`FsxID-abcdef123456::>` `volume online -volume `volume_name` -vserver `svm_name``

`Volume 'vs1:vol1' is now online.`
```

## Your restricted volume contains an iSCSI LUN or an NVMe/TCP namespace

Your file system currently hosts a volume that is in a restricted state, and that volume contains an iSCSI LUN, an NVMe/TCP namespace, or both.
We recommend that you keep volumes online on an ongoing basis. If you don't online this volume before your file system’s next maintenance window,
Amazon FSx will temporarily online this volume for the duration of the patching operation.
To avoid this, please online or delete the volume.

To bring an offline volume back online, use the
[`volume online`](https://docs.netapp.com/us-en/ontap-cli-9141/volume-online.html "https://docs.netapp.com/us-en/ontap-cli-9141/volume-online.html")
ONTAP CLI command, as shown in the following example. If only one SVM (Vserver) exists, you do not need to specify the `-vserver` parameter.

```
`FsxID-abcdef123456::>` `volume online -volume `volume_name` -vserver `svm_name``

`Volume 'vs1:vol1' is now online.`
```

## Your restricted volume is a FlexCache origin

Your file system contains a FlexCache origin volume that is in a restricted state. We recommend that you keep volumes online on an ongoing basis.
If you don't online this volume before your file system’s next maintenance window, Amazon FSx will temporarily online this volume for the duration of the
patching operation. During this time, it's possible that data will be written back to the FlexCache origin volume with data from the cache volume. To avoid
this, please online or delete the volume.

To bring an offline volume back online, use the
[`volume online`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-online.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-online.html")
ONTAP CLI command, as shown in the following example. If only one SVM (Vserver) exists, you do not need to specify the `-vserver` parameter.

```
`FsxID-abcdef123456::>` `volume online -volume `volume_name` -vserver `svm_name``

`Volume 'vs1:vol1' is now online.`
```

## Your restricted volume is part of a SnapMirror relationship

Your file system currently hosts a volume that is in a restricted state, and that volume is a SnapMirror source or destination.
We recommend that you keep volumes online on an ongoing basis.
If you don't online this volume before your file system’s next maintenance window, Amazon FSx will temporarily online this volume for the duration of the
patching operation and pause the SnapMirror relationship.
During this time, it's possible that data will be written to the SnapMirror destination volume with data from the SnapMirror
source volume. To avoid this, please online or delete the volume.

To bring an offline volume back online, use the
[`volume online`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-online.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-online.html")
ONTAP CLI command, as shown in the following example. If only one SVM (Vserver) exists, you do not need to specify the `-vserver` parameter.

```
`FsxID-abcdef123456::>` `volume online -volume `volume_name` -vserver `svm_name``

`Volume 'vs1:vol1' is now online.`
```

# Viewing offline volumes

You can't create or delete volume backups when the source volume is offline. You can use the
[`volume show`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-show.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-show.html")
ONTAP CLI command to determine a volume's current status.

```
volume show -vserver `svm-name`
```

For information about accessing the
ONTAP CLI on your file system, see [Using the NetApp ONTAP CLI](managing-resources-ontap-apps.md#netapp-ontap-cli "managing-resources-ontap-apps.md#netapp-ontap-cli").

```
`FsxIdabc12345::>` `volume show -vserver vs1`
Vserver   Volume       Aggregate    State      Type       Size  Available Used%
--------- ------------ ------------ ---------- ---- ---------- ---------- -----
vs1       vol1         aggr1        online     RW          2GB      1.9GB    5%
vs1       vol1_dr      aggr0_dp     online     DP        200GB    160.0GB   20%
vs1       vol2         aggr0        online     RW        150GB    110.3GB   26%
vs1       vol2_dr      aggr0_dp     online     DP        150GB    110.3GB   26%
vs1       vol3         aggr1        online     RW        150GB    120.0GB   20%
vs1       vol3_dr      aggr1_dp     online     DP        150GB    120.0GB   20%
vs1       vol4         aggr1        online     RW        200GB    159.8GB   20%
7 entries were displayed.
```

To bring an offline volume back online, use the
[`volume online`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-online.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-online.html")
ONTAP CLI command, as shown in the following example. If only one SVM (Vserver) exists, you do not need to specify the `-vserver` parameter.

```
`FsxID-abcdef123456::>` `volume online -volume `volume_name` -vserver `svm_name``

`Volume 'vs1:vol1' is now online.`
```

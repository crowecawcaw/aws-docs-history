# Sample configuration (crm config)

```
node 1: slxdbhost01
node 2: slxdbhost02
primitive rsc_ase_ASD_ASEDB SAPDatabase \
        params SID=ASD DBTYPE=SYB STRICT_MONITORING=TRUE \
        op start timeout=300 interval=0s \
        op stop timeout=300 interval=0s \
        op monitor timeout=60s interval=120s \
        meta target-role=Started
primitive rsc_aws_stonith_ASD stonith:external/ec2 \
        params tag=pacemaker profile=cluster pcmk_delay_max=30 \
        op start interval=0 timeout=180s \
        op stop interval=0 timeout=180s \
        op monitor interval=180s timeout=60s
primitive rsc_fs_ASD_bkp Filesystem \
        params device="svm-091efa9986c8e93c7.fs-0c3a4a5162a325aea.fsx.us-east-1.amazonaws.com:/backup" directory="/sybasebackup" fstype=nfs4 options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" \

        op start timeout=60s interval=0 \
        op stop timeout=60s interval=0 \
        op monitor interval=20s timeout=40s
primitive rsc_fs_ASD_data Filesystem \
        params device="svm-0e6e2738a9ca391ce.fs-0c3a4a5162a325aea.fsx.us-east-1.amazonaws.com:/asedata" directory="/sybase/ASD/sapdata_1" fstype=nfs4 options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=8,timeo=600,retrans=2" \
        op start timeout=60s interval=0 \
        op stop timeout=60s interval=0 \
        op monitor interval=20s timeout=40s
primitive rsc_fs_ASD_diag Filesystem \
        params device="svm-091efa9986c8e93c7.fs-0c3a4a5162a325aea.fsx.us-east-1.amazonaws.com:/sapdiag" directory="/sybase/ASD/sapdiag" fstype=nfs4 options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" \
        op start timeout=60s interval=0 \
        op stop timeout=60s interval=0 \
        op monitor interval=20s timeout=40s
primitive rsc_fs_ASD_log Filesystem \
        params device="svm-0895fe73884c12f83.fs-0c3a4a5162a325aea.fsx.us-east-1.amazonaws.com:/aselog" directory="/sybase/ASD/saplog_1" fstype=nfs4 options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" \
        op start timeout=60s interval=0 \
        op stop timeout=60s interval=0 \
        op monitor interval=20s timeout=40s
primitive rsc_fs_ASD_sap Filesystem \
        params device="svm-091efa9986c8e93c7.fs-0c3a4a5162a325aea.fsx.us-east-1.amazonaws.com:/usrsap" directory="/usr/sap" fstype=nfs4 options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" \
        op start timeout=60s interval=0 \
        op stop timeout=60s interval=0 \
        op monitor interval=20s timeout=40s
primitive rsc_fs_ASD_sybase Filesystem \
        params device="svm-091efa9986c8e93c7.fs-0c3a4a5162a325aea.fsx.us-east-1.amazonaws.com:/sybase" directory="/sybase" fstype=nfs4 options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" \
        op start timeout=60s interval=0 \
        op stop timeout=60s interval=0 \
        op monitor interval=20s timeout=40s
primitive rsc_fs_ASD_tmp Filesystem \
        params device="svm-091efa9986c8e93c7.fs-0c3a4a5162a325aea.fsx.us-east-1.amazonaws.com:/saptmp" directory="/sybase/ASD/saptmp" fstype=nfs4 options="rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2" \
        op start timeout=60s interval=0 \
        op stop timeout=60s interval=0 \
        op monitor interval=20s timeout=40s
primitive rsc_ip_SD_ASEDB aws-vpc-move-ip \
        params ip=172.16.0.29 routing_table=rtb-0b3f1d6196f45300d interface=eth0 profile=cluster \
        op start interval=0 timeout=180s \
        op stop interval=0 timeout=180s \
        op monitor interval=20s timeout=40s
group grp_ASD_ASEDB rsc_fs_ASD_sybase rsc_fs_ASD_data rsc_fs_ASD_log rsc_fs_ASD_diag rsc_fs_ASD_tmp rsc_fs_ASD_bkp rsc_fs_ASD_sap rsc_ip_SD_ASEDB rsc_ase_ASD_ASEDB
property cib-bootstrap-options: \
        maintenance-mode=false \
        stonith-enabled=true \
        stonith-action=off \
        stonith-timeout=300s \
        last-lrm-refresh=1686941627 \
        have-watchdog=false \
        dc-version="2.1.2+20211124.ada5c3b36-150400.4.9.2-2.1.2+20211124.ada5c3b36" \
        cluster-infrastructure=corosync
rsc_defaults rsc-options: \
        resource-stickiness=1 \
        migration-threshold=1
op_defaults op-options: \
        timeout=300s \
        record-pending=true
```

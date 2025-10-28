# Sample configuration (pcs config show)

The following sample configuration is based on ENSA2.

```
pcs config show
Cluster Name: rhelha
Corosync Nodes:
 rhxdbhost01 rhxdbhost02
Pacemaker Nodes:
 rhxdbhost01 rhxdbhost02

Resources:
 Group: rsc_asedb_group
  Meta Attrs: resource-stickiness=5000
  Resource: rsc_vip_asedb (class=ocf provider=heartbeat type=aws-vpc-move-ip)
   Attributes: interface=eth0 ip=172.16.0.23 routing_table=rtb-0b3f1d6196f45300d
   Operations: monitor interval=60s timeout=30s (rsc_vip_asedb-monitor-interval-60s)
               start interval=0s timeout=180s (rsc_vip_asedb-start-interval-0s)
               stop interval=0s timeout=180s (rsc_vip_asedb-stop-interval-0s)
  Resource: rsc_fs_sybase (class=ocf provider=heartbeat type=Filesystem)
   Attributes: device=svm-09794aeece44cc025.fs-04af26e8311974f41.fsx.us-east-1.amazonaws.com:/sybase directory=/sybase force_unmount=safe fstype=nfs4 options=rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2
   Operations: monitor interval=20s timeout=40s (rsc_fs_sybase-monitor-interval-20s)
               start interval=0s timeout=60s (rsc_fs_sybase-start-interval-0s)
               stop interval=0s timeout=60s (rsc_fs_sybase-stop-interval-0s)
  Resource: rsc_fs_data (class=ocf provider=heartbeat type=Filesystem)
   Attributes: device=svm-01c02d046ae5a24a2.fs-04af26e8311974f41.fsx.us-east-1.amazonaws.com:/asedata directory=/sybase/ARD/sapdata_1 force_unmount=safe fstype=nfs4 options=rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=8,timeo=600,retrans=2
   Operations: monitor interval=20s timeout=40s (rsc_fs_data-monitor-interval-20s)
               start interval=0s timeout=60s (rsc_fs_data-start-interval-0s)
               stop interval=0s timeout=60s (rsc_fs_data-stop-interval-0s)
  Resource: rsc_fs_log (class=ocf provider=heartbeat type=Filesystem)
   Attributes: device=svm-04cd525dbd0b354d2.fs-04af26e8311974f41.fsx.us-east-1.amazonaws.com:/aselog directory=/sybase/ARD/saplog_1 force_unmount=safe fstype=nfs4 options=rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2
   Operations: monitor interval=20s timeout=40s (rsc_fs_log-monitor-interval-20s)
               start interval=0s timeout=60s (rsc_fs_log-start-interval-0s)
               stop interval=0s timeout=60s (rsc_fs_log-stop-interval-0s)
  Resource: rsc_fs_sapdiag (class=ocf provider=heartbeat type=Filesystem)
   Attributes: device=svm-09794aeece44cc025.fs-04af26e8311974f41.fsx.us-east-1.amazonaws.com:/sapdiag directory=/sybase/ARD/sapdiag force_unmount=safe fstype=nfs4 options=rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2
   Operations: monitor interval=20s timeout=40s (rsc_fs_sapdiag-monitor-interval-20s)
               start interval=0s timeout=60s (rsc_fs_sapdiag-start-interval-0s)
               stop interval=0s timeout=60s (rsc_fs_sapdiag-stop-interval-0s)
  Resource: rsc_fs_saptmp (class=ocf provider=heartbeat type=Filesystem)
   Attributes: device=svm-09794aeece44cc025.fs-04af26e8311974f41.fsx.us-east-1.amazonaws.com:/saptmp directory=/sybase/ARD/saptmp force_unmount=safe fstype=nfs4 options=rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2
   Operations: monitor interval=20s timeout=40s (rsc_fs_saptmp-monitor-interval-20s)
               start interval=0s timeout=60s (rsc_fs_saptmp-start-interval-0s)
               stop interval=0s timeout=60s (rsc_fs_saptmp-stop-interval-0s)
  Resource: rsc_fs_backup (class=ocf provider=heartbeat type=Filesystem)
   Attributes: device=svm-09794aeece44cc025.fs-04af26e8311974f41.fsx.us-east-1.amazonaws.com:/backup directory=/sybasebackup force_unmount=safe fstype=nfs4 options=rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2
   Operations: monitor interval=20s timeout=40s (rsc_fs_backup-monitor-interval-20s)
               start interval=0s timeout=60s (rsc_fs_backup-start-interval-0s)
               stop interval=0s timeout=60s (rsc_fs_backup-stop-interval-0s)
  Resource: rsc_fs_usrsap (class=ocf provider=heartbeat type=Filesystem)
   Attributes: device=svm-09794aeece44cc025.fs-04af26e8311974f41.fsx.us-east-1.amazonaws.com:/usrsap directory=/usr/sap force_unmount=safe fstype=nfs4 options=rw,noatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,nconnect=2,timeo=600,retrans=2
   Operations: monitor interval=20s timeout=40s (rsc_fs_usrsap-monitor-interval-20s)
               start interval=0s timeout=60s (rsc_fs_usrsap-start-interval-0s)
               stop interval=0s timeout=60s (rsc_fs_usrsap-stop-interval-0s)
  Resource: sybaseARD (class=ocf provider=heartbeat type=SAPDatabase)
   Attributes: DBTYPE=SYB SID=ARD STRICT_MONITORING=TRUE
   Operations: methods interval=0s timeout=5s (sybaseARD-methods-interval-0s)
               monitor interval=120s timeout=60s (sybaseARD-monitor-interval-120s)
               start interval=0s timeout=300 (sybaseARD-start-interval-0s)
               stop interval=0s timeout=300 (sybaseARD-stop-interval-0s)
Stonith Devices:
 Resource: clusterfence (class=stonith type=fence_aws)
  Attributes: pcmk_delay_max=45 pcmk_host_map=rhxdbhost01:i-03939ad3f07e14e3f;rhxdbhost02:i-09f138e3a1290bfde pcmk_reboot_action=off pcmk_reboot_retries=4 pcmk_reboot_timeout=600 power_timeout=240 region=us-east-1
  Operations: monitor interval=300 timeout=60 (clusterfence-monitor-interval-300)
              start interval=0s timeout=600 (clusterfence-start-interval-0s)
Fencing Levels:
Location Constraints:
Ordering Constraints:
Colocation Constraints:
Ticket Constraints:
Alerts:
 No alerts defined
Resources Defaults:
  Meta Attrs: rsc_defaults-meta_attributes
    migration-threshold=1
Operations Defaults:
  No defaults set
Cluster Properties:
 cluster-infrastructure: corosync
 cluster-name: rhelha
 dc-version: 2.1.2-4.el8_6.7-ada5c3b36e2
 have-watchdog: false
 last-lrm-refresh: 1693394303
 maintenance-mode: false
Tags:
 No tags defined
Quorum:
  Options:
```

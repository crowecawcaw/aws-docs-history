# Sample configuration (`pcs config show`)

The following sample configuration is based on ENSA2.

```
[root@rhxhost01 cluster] pcs config show
Cluster Name: rhelha
Corosync Nodes:
 rhxhost01 rhxhost02
Pacemaker Nodes:
 rhxhost01 rhxhost02

Resources:
 Group: grp_RHX_ASCS00
  Meta Attrs: resource-stickiness=3000
  Resource: rsc_fs_RHX_ASCS00 (class=ocf provider=heartbeat type=Filesystem)
   Attributes: device=fs-0f935147fc20d5ce9.efs.ap-south-1.amazonaws.com:/RHX_ASCS00 directory=/usr/sap/RHX/ASCS00 force_unmount=safe fstype=nfs4 options=nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport
   Operations: monitor interval=20s timeout=40s (rsc_fs_RHX_ASCS00-monitor-interval-20s)
               notify interval=0s timeout=60s (rsc_fs_RHX_ASCS00-notify-interval-0s)
               start interval=0s timeout=60s (rsc_fs_RHX_ASCS00-start-interval-0s)
               stop interval=0s timeout=60s (rsc_fs_RHX_ASCS00-stop-interval-0s)
  Resource: rsc_ip_RHX_ASCS00 (class=ocf provider=heartbeat type=aws-vpc-move-ip)
   Attributes: interface=eth0 ip=172.16.30.5 routing_table=rtb-0cbb0e6fa45ac5a93,rtb-06b959bbca4d4df44
   Operations: monitor interval=20s timeout=40s (rsc_ip_RHX_ASCS00-monitor-interval-20s)
               start interval=0s timeout=180s (rsc_ip_RHX_ASCS00-start-interval-0s)
               stop interval=0s timeout=180s (rsc_ip_RHX_ASCS00-stop-interval-0s)
  Resource: rsc_sap_RHX_ASCS00 (class=ocf provider=heartbeat type=SAPInstance)
   Attributes: AUTOMATIC_RECOVER=false InstanceName=RHX_ASCS00_rhxascs START_PROFILE=/usr/sap/RHX/SYS/profile/RHX_ASCS00_rhxascs
   Meta Attrs: resource-stickiness=5000
   Operations: demote interval=0s timeout=320s (rsc_sap_RHX_ASCS00-demote-interval-0s)
               methods interval=0s timeout=5s (rsc_sap_RHX_ASCS00-methods-interval-0s)
               monitor interval=11s on-fail=restart timeout=60s (rsc_sap_RHX_ASCS00-monitor-interval-11s)
               promote interval=0s timeout=320s (rsc_sap_RHX_ASCS00-promote-interval-0s)
               reload interval=0s timeout=320s (rsc_sap_RHX_ASCS00-reload-interval-0s)
               start interval=0s timeout=600s (rsc_sap_RHX_ASCS00-start-interval-0s)
               stop interval=0s timeout=240s (rsc_sap_RHX_ASCS00-stop-interval-0s)
 Group: grp_RHX_ERS10
  Resource: rsc_fs_RHX_ERS10 (class=ocf provider=heartbeat type=Filesystem)
   Attributes: device=fs-0f935147fc20d5ce9.efs.ap-south-1.amazonaws.com:/RHX_ERS10 directory=/usr/sap/RHX/ERS10 force_unmount=safe fstype=nfs4 options=nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport
   Operations: monitor interval=20s timeout=40s (rsc_fs_RHX_ERS10-monitor-interval-20s)
               notify interval=0s timeout=60s (rsc_fs_RHX_ERS10-notify-interval-0s)
               start interval=0s timeout=60s (rsc_fs_RHX_ERS10-start-interval-0s)
               stop interval=0s timeout=60s (rsc_fs_RHX_ERS10-stop-interval-0s)
  Resource: rsc_ip_RHX_ERS10 (class=ocf provider=heartbeat type=aws-vpc-move-ip)
   Attributes: interface=eth0 ip=172.16.30.6 routing_table=rtb-0cbb0e6fa45ac5a93,rtb-06b959bbca4d4df44
   Operations: monitor interval=20s timeout=40s (rsc_ip_RHX_ERS10-monitor-interval-20s)
               start interval=0s timeout=180s (rsc_ip_RHX_ERS10-start-interval-0s)
               stop interval=0s timeout=180s (rsc_ip_RHX_ERS10-stop-interval-0s)
  Resource: rsc_sap_RHX_ERS10 (class=ocf provider=heartbeat type=SAPInstance)
   Attributes: AUTOMATIC_RECOVER=false InstanceName=RHX_ERS10_rhxers START_PROFILE=/usr/sap/RHX/SYS/profile/RHX_ERS10_rhxers
   Operations: demote interval=0s timeout=320s (rsc_sap_RHX_ERS10-demote-interval-0s)
               methods interval=0s timeout=5s (rsc_sap_RHX_ERS10-methods-interval-0s)
               monitor interval=20s on-fail=restart timeout=60s (rsc_sap_RHX_ERS10-monitor-interval-20s)
               promote interval=0s timeout=320s (rsc_sap_RHX_ERS10-promote-interval-0s)
               reload interval=0s timeout=320s (rsc_sap_RHX_ERS10-reload-interval-0s)
               start interval=0s timeout=600s (rsc_sap_RHX_ERS10-start-interval-0s)
               stop interval=0s timeout=240s (rsc_sap_RHX_ERS10-stop-interval-0s)

Stonith Devices:
 Resource: rsc_aws_stonith_RHX (class=stonith type=fence_aws)
  Attributes: pcmk_delay_max=30 pcmk_host_map=rhxhost01:i-xxxxinstidforhost1;rhxhost02:i-xxxxinstidforhost2 pcmk_reboot_action=reboot pcmk_reboot_retries=2 pcmk_reboot_timeout=300 power_timeout=240 region=us-east-1
  Operations: monitor interval=180 timeout=60 (rsc_aws_stonith_RHX-monitor-interval-180)
              start interval=0s timeout=180 (rsc_aws_stonith_RHX-start-interval-0s)
              stop interval=0s timeout=180 (rsc_aws_stonith_RHX-stop-interval-0s)
Fencing Levels:

Location Constraints:
Ordering Constraints:
  start grp_RHX_ASCS00 then stop grp_RHX_ERS10 (kind:Optional) (non-symmetrical) (id:order-grp_RHX_ASCS00-grp_RHX_ERS10-Optional)
Colocation Constraints:
  grp_RHX_ERS10 with grp_RHX_ASCS00 (score:-5000) (id:colocation-grp_RHX_ERS10-grp_RHX_ASCS00--5000)
Ticket Constraints:

Alerts:
 No alerts defined

Resources Defaults:
 migration-threshold=3
 resource-stickiness=1
Operations Defaults:
 No defaults set

Cluster Properties:
 cluster-infrastructure: corosync
 cluster-name: rhelha
 dc-version: 1.1.23-1.el7_9.1-9acf116022
 have-watchdog: false
 last-lrm-refresh: 1674393658
 maintenance-mode: false

Quorum:
  Options:
```

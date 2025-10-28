# Sample configuration (`crm config`)

The following sample configuration is based on simple mount and ENSA2.

```
node 1: slxhost01 \
        attributes standby=off
node 2: slxhost02 \
        attributes standby=off
primitive res_{aws}_STONITH stonith:external/ec2 \
        op start interval=0 timeout=180s \
        op stop interval=0 timeout=180s \
        op monitor interval=180s timeout=60s \
        params tag=pacemaker profile=cluster pcmk_delay_max=10
primitive rsc_ip_SLX_ASCS00 aws-vpc-move-ip \
        params ip=172.16.52.5 routing_table=rtb-04385ff6bcae17982 interface=eth0 profile=cluster \
        op start interval=0 timeout=180s \
        op stop interval=0 timeout=180s \
        op monitor interval=20s timeout=40s
primitive rsc_ip_SLX_ERS10 aws-vpc-move-ip \
        params ip=172.16.52.6 routing_table=rtb-04385ff6bcae17982 interface=eth0 profile=cluster \
        op start interval=0 timeout=180s \
        op stop interval=0 timeout=180s \
        op monitor interval=20s timeout=40s
primitive rsc_sap_SLX_ASCS00 SAPInstance \
        operations $id=rsc_sap_SLX_ASCS00-operations \
        op monitor interval=11s timeout=60s on-fail=restart \
        op stop interval=0 timeout=240s \
        params InstanceName=SLX_ASCS00_slxascs START_PROFILE=" /usr/sap/SLX/SYS/profile/SLX_ASCS00_slxascs" AUTOMATIC_RECOVER=false MINIMAL_PROBE=true \
        meta resource-stickiness=5000 priority=1000
primitive rsc_sap_SLX_ERS10 SAPInstance \
        operations $id=rsc_sap_SLX_ERS10-operations \
        op monitor interval=11s timeout=60s on-fail=restart \
        op stop interval=0 timeout=240s \
        params InstanceName=SLX_ERS10_slxers START_PROFILE=" /usr/sap/SLX/SYS/profile/SLX_ERS10_slxers" AUTOMATIC_RECOVER=false IS_ERS=true MINIMAL_PROBE=true
primitive rsc_sapstart_SLX_ASCS00 ocf:suse:SAPStartSrv \
        params InstanceName=SLX_ASCS00_slxascs
primitive rsc_sapstart_SLX_ERS10 ocf:suse:SAPStartSrv \
        params InstanceName=SLX_ERS10_slxers
group grp_SLX_ASCS00 rsc_ip_SLX_ASCS00 rsc_sapstart_SLX_ASCS00 rsc_sap_SLX_ASCS00 \
        meta resource-stickiness=3000
group grp_SLX_ERS10 rsc_ip_SLX_ERS10 rsc_sapstart_SLX_ERS10 rsc_sap_SLX_ERS10
colocation col_sap_SLX_separate -5000: grp_SLX_ERS10 grp_SLX_ASCS00
order ord_sap_SLX_first_start_ascs Optional: rsc_sap_SLX_ASCS00:start rsc_sap_SLX_ERS10:stop symmetrical=false
property cib-bootstrap-options: \
        maintenance-mode=false \
        stonith-enabled=true \
        stonith-action=off \
        stonith-timeout=300s \
        priority-fencing-delay=30s \
        have-watchdog=false \
        dc-version="2.0.5+20201202.ba59be712-150300.4.24.1-2.0.5+20201202.ba59be712" \
        cluster-infrastructure=corosync \
        last-lrm-refresh=1670459760
rsc_defaults rsc-options: \
        resource-stickiness=1 \
        migration-threshold=3
op_defaults op-options: \
        timeout=600s \
        record-pending=true
```

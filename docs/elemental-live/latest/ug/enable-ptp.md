# Setup: Enable precision time protocol (PTP)

If you set up SMPTE 2110 outputs in events, you must enable Precision Time Protocol
(PTP). You don't need to enable it if you only set up SMPTE 2110 inputs.

When PTP is enabled, you can view the PTP logs in
`/var/log/messages`.

###### To enable PTP

You must enable PTP on the Elemental Live appliance. Enabling PTP automatically disables the
NTP clock. And disabling PTP automatically enables the NTP clock.

1. In the Elemental Live web interface, choose **Settings**. (Don't choose
   **Input Devices** or **Routers** from the
   submenu).
2. On the **Settings** page, choose the **Network**
   tab, then choose **Hostname, DNS, & Timing Server**.
3. Select the **Enable PTP** check box, and then choose
   **Save**.

## Working with PTP

PTP provides the timing for packet pacing in Elemental Live’s SMPTE 2110 output. In line with
the SMPTE 2110 specification, PTP is used for synchronizing the streams in SMPTE 2110
outputs—it ensures that the video, audio, and ancillary data streams remain synchronized
downstream of Elemental Live.

Elemental Live is a follower that needs to sync to a boundary clock.

Elemental Live uses the Type N – Narrow sender profile of PTP. In the output video SDP
file, the line `TP=2110TPN` identifies the profile.

**The default configuration file**

When you enable PTP, Elemental Live uses PTP as defined in the configuration file. This file
is in `/etc/ptp4l.conf`.

The contents of the default PTP configuration file are shown below. You can modify
the values and add more parameters to suit your network requirements. However, note that
AWS Elemental won't be able to troubleshoot customizations that you make to the file.

**Default PTP configuration file**

```
[global]
domainNumber 127
priority1 128
priority2 128
use_syslog 1
logging_level 6
tx_timestamp_timeout 30
hybrid_e2e 0
dscp_event 46
dscp_general 46

[eth6]
logAnnounceInterval 0
announceReceiptTimeout 3
logSyncInterval -3
logMinDelayReqInterval -3
delay_mechanism E2E
network_transport UDPv4
```

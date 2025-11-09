This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Wickr Enterprise embedded cluster

requirements

Before you start to install Wickr Enterprise embedded cluster, verify that the following
requirements are met.

**Network requirements**

You will need to allow ingress to your Wickr server on the following ports:

- 443/TCP for HTTPS
- Calling TCP Proxy Only - The TCP proxy port configured for TCP Calling traffic in
  KOTS
- 16384-19999/UDP for UDP Calling traffic
- LAN Only - 30000/TCP for Accessing the KOTS Admin Console
  **System requirements**

Before installation, make sure you have either a VM (Virtual Machine) or a physical machine
running a Linux based Operating System (OS) with the following minimum resources available:

- 8 CPU cores
- 12 gigabytes (GB) of RAM
- 100 gigabytes (GB) of disk storage on the / (root) partition
  The Wickr Enterprise embedded cluster has been tested on the following Linux OS systems
  but other Linux based OS options may be suitable as well:

- Red Hat Enterprise Linux 9.5
- Amazon Linux 2023
- Rocky Linux 9.5

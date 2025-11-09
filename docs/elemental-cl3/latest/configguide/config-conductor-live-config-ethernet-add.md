# Configure Ethernet

interfaces

When you installed the software on the individual nodes in an AWS Elemental Conductor Live cluster, you
configured eth0. If you need to set up more Ethernet interfaces (network devices), read this
section. You can optionally bond Ethernet interfaces to suit your networking requirements.

**Where to perform the configuration**

Make sure you perform the configuration on the correct nodes.

| Node                          | Work on this node? |
| ----------------------------- | ------------------ |
| Primary Conductor Live node   | Yes                |
| Secondary Conductor Live node | Yes                |
| Each worker node              | Yes                |

###### Topics

- [Creating an Ethernet interface](config-conductor-live-ethernet-create.md "config-conductor-live-ethernet-create.md")
- [Modifying an Ethernet
  interface](config-conductor-live-ethernet-modify.md "config-conductor-live-ethernet-modify.md")
- [Creating or modifying a bond](config-conductor-live-config-bond-add.md "config-conductor-live-config-bond-add.md")
- [Dedicating interfaces to MPTS](config-cluster-mpts.md "config-cluster-mpts.md")

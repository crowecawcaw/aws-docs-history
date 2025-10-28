NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# VMware limitations

Application Migration Service supports VMC on AWS for agentless replication.

- Application Migration Service partially supports vMotion, Storage vMotion, and other features based on virtual
  machine migration (such as DRS and Storage DRS) subject to these limitations:
  - Migrating a virtual machine to a new ESXi host or datastore after one replication run
    ends, and before the next replication run begins, is supported as long as the vCenter
    account has sufficient permissions on the destination ESXi host, datastores, and datacenter,
    and on the virtual machine itself at the new location.
  - Migrating a virtual machine to a new ESXi host, datastore, and/or datacenter while a
    replication run is active – that is, while a virtual machine upload is in progress – is not
    supported. Cross vCenter vMotion is not supported for use with Application Migration Service.

- AWS does not provide support for migrating VMware Virtual Volumes.

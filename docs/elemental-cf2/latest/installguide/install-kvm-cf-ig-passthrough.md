This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step C: Enable CPU Passthrough

Enable CPU passthrough so that the KVM can tell what CPU you're using. The AWS Elemental software installer could fail, or jobs remain in a pending state, if passthrough isn't enabled.

###### To enable CPU passthrough

1. At the Linux command line on the KVM host, use the following command to update the virtual machine configuration file.

```
sudo virsh edit `hostname`
```

where `hostname` is the name that you gave the virtual machine when you deployed it. 2. Go to the line that defines `cpu mode` and change it to `host-passthrough`. 3. Save and exit the editor. 4. Enable passthrough on all KVMs that you deployed.

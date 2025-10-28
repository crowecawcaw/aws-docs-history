# Modify supported instance types for an existing Amazon EC2 Dedicated Host

You can modify a Dedicated Host to change the instance types that it supports. If it
currently supports a single instance type, you can modify it to support multiple
instance types within that instance family. Similarly, if it currently supports
multiple instance types, you can modify it to support a specific instance type
only.

To modify a Dedicated Host to support multiple instance types, you must first stop all
running instances on the host. The modification takes approximately 10 minutes to
complete. The Dedicated Host transitions to the `pending` state while the
modification is in progress. You can't start stopped instances or launch new
instances on the Dedicated Host while it is in the `pending` state.

To modify a Dedicated Host that supports multiple instance types to support only a single
instance type, the host must either have no running instances, or the running
instances must be of the instance type that you want the host to support. For
example, to modify a host that supports multiple instance types in the
`m5` instance family to support only `m5.large` instances,
the Dedicated Host must either have no running instances, or it must have only
`m5.large` instances running on it.

If you allocate a host for a virtualized instance type, you can't modify the
instance type to a `.metal` instance type after the host is allocated.
For example, if you allocate a host for the `m5.large` instance type, you
can't modify the instance type to `m5.metal`. Similarly, if you allocate
a host for a `.metal` instance type, you can't modify the instance type
to a virtualized instance type after the host is allocated. For example, if you
allocate a host for the `m5.metal` instance type, you can't modify the
instance type to `m5.large`.

Console

###### To modify the supported instance types for a Dedicated Host

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the Navigation pane, choose
   **Dedicated Host**.
3. Select the Dedicated Host to modify and choose
   **Actions**, **Modify
   host**.
4. Do one of the following, depending on the current
   configuration of the Dedicated Host:
   - If the Dedicated Host currently supports a specific instance
     type, **Support multiple instance
     types** is not enabled, and
     **Instance type** lists the
     supported instance type. To modify the host to support
     multiple types in the current instance family, for
     **Support multiple instance
     types**, choose
     **Enable**.

   You must first stop all instances running on the host
   before modifying it to support multiple instance
   types.
   - If the Dedicated Host currently supports multiple instance types
     in an instance family, **Enabled** is
     selected for **Support multiple instance
     types**. To modify the host to support a
     specific instance type, for **Support multiple
     instance types**, clear
     **Enable**, and then for
     **Instance type**, select the
     specific instance type to support.

   You can't change the instance family supported by the
   Dedicated Host.

5. Choose **Save**.

AWS CLI

###### To modify the supported instance types for a Dedicated Host

Use the [modify-hosts](../../../cli/latest/reference/ec2/modify-hosts.md "../../../cli/latest/reference/ec2/modify-hosts.md") command.

The following example modifies a Dedicated Host to support multiple instance
types within the `m5` instance family.

```
aws ec2 modify-hosts \
    --instance-family `m5` \
    --host-ids `h-012a3456b7890cdef`
```

The following example modifies a Dedicated Host to support
`m5.xlarge` instances only.

```
aws ec2 modify-hosts \
    --instance-type `m5.xlarge` \
    --instance-family --host-ids `h-012a3456b7890cdef`
```

PowerShell

###### To modify the supported instance types for a Dedicated Host

Use the [Edit-EC2Host](../../../powershell/latest/reference/items/Edit-EC2Host.md "../../../powershell/latest/reference/items/Edit-EC2Host.md") cmdlet.

The following example modifies a Dedicated Host to support multiple instance
types within the `m5` instance family.

```
Edit-EC2Host `
    -InstanceFamily `m5` `
    -HostId `h-012a3456b7890cdef`
```

The following example modifies a Dedicated Host to support
`m5.xlarge` instances only.

```
Edit-EC2Host `
    -InstanceType `m5.xlarge` `
    -HostId `h-012a3456b7890cdef`
```

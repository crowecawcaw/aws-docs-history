# Tenancy conversion in License Manager

You can change the tenancy of your instance to best suit your use case. You can use
the [modify-instance-placement](../../../cli/latest/reference/ec2/modify-instance-placement.md "../../../cli/latest/reference/ec2/modify-instance-placement.md") AWS CLI command to switch among the following
tenancies:

- Shared
- Dedicated Instance
- Dedicated Host
- Host resource groups
  Your account must have a Dedicated Host with available capacity to start the instance in order
  to switch to the Dedicated Host tenancy type. For more information about working with dedicated
  hosts, see [Work with Dedicated Hosts](../../../index.md "../../../index.md") in the
  _Amazon Elastic Compute Cloud User Guide_.

To move to the host resource groups tenancy type, you must have at least one host resource group in your account.
In order to launch an instance into a host resource group, the instance must have the
same set of licenses that are associated with the host resource group. For more
information, see [Host resource groups in License Manager](host-resource-groups.md "host-resource-groups.md").

###### Tenancy conversion limits

The following limits apply to tenancy conversion:

- The Linux billing code is permitted on all tenancy types.
- The Windows BYOL billing code is not permitted on Shared tenancy.
- The Windows Server license included billing code is permitted on all tenancy
  types.
- All supported SQL Server editions and SUSE (SLES)
  license included billing codes are permitted on Shared tenancy and Dedicated
  Instances. However, these billing codes are not permitted on Dedicated Hosts and
  host resource groups.
- License included billing codes other than Windows Server are not permitted on
  Dedicated Hosts and host resource groups.

###### Change the tenancy of an instance using the AWS CLI

An instance must be in the `stopped` state in order to change its
tenancy.

To stop the instance, run the following command:

```
aws ec2 stop-instances --instance-ids `<instance_id>`
```

To change an instance from any tenancy to `default` or
`dedicated` tenancy, run the following commands:

`default`

```
aws ec2 modify-instance-placement --instance-id `<instance_id>` \
  --tenancy default
```

`dedicated`

```
aws ec2 modify-instance-placement --instance-id `<instance_id>` \
  --tenancy dedicated
```

To change an instance from any tenancy to `host` tenancy with
auto-placement, run the following command:

```
aws ec2 modify-instance-placement --instance-id `<instance_id>` \
  --tenancy host --affinity default
```

To change an instance from any tenancy to `host` tenancy, targeting a
specific Dedicated Host, run the following command:

```
aws ec2 modify-instance-placement --instance-id `<instance_id>` \
  --tenancy host --affinity host --host-id `<host_id>`
```

To change an instance from any tenancy to `host` tenancy using a Host
Resource Group, run the following command:

```
aws ec2 modify-instance-placement --instance-id `<instance_id>` \
  --tenancy host --host-resource-group-arn `<host_resource_group_arn>`
```

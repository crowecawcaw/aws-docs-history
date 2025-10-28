# Get hardware information for each HSM in an

AWS CloudHSM cluster with CMU

Use the **getHSMInfo** command in the AWS CloudHSM cloudhsm_mgmt_util (CMU) to get information
about the hardware on which each hardware security module (HSM) runs, including the model,
serial number, FIPS state, memory, temperature, and the version numbers of the hardware and
firmware. The information also includes the server ID that cloudhsm_mgmt_util uses to refer to the
HSM.

Before you run any CMU command, you must start CMU and log in to the HSM. Be
sure that you log in with a user type that can run the commands you plan to
use.

If you add or delete HSMs, update the
configuration files for CMU.
Otherwise, the changes that you make might not be effective for all HSMs in the cluster.

## User type

The following types of users can run this command.

- All users. You do not have to be logged in to run this command.

## Syntax

This command has no parameters.

```
getHSMInfo
```

## Example

This example uses **getHSMInfo** to get information about the HSMs in the
cluster.

```
`aws-cloudhsm>` `getHSMInfo`
`Getting HSM Info on 3 nodes
 *** Server 0 HSM Info ***

 Label :cavium
 Model :NITROX-III CNN35XX-NFBE

 Serial Number :3.0A0101-ICM000001
 HSM Flags :0
 FIPS state :2 [FIPS mode with single factor authentication]

 Manufacturer ID :
 Device ID :10
 Class Code :100000
 System vendor ID :177D
 SubSystem ID :10


 TotalPublicMemory :560596
 FreePublicMemory :294568
 TotalPrivateMemory :0
 FreePrivateMemory :0

 Hardware Major :3
 Hardware Minor :0

 Firmware Major :2
 Firmware Minor :03

 Temperature :56 C

 Build Number :13

 Firmware ID :xxxxxxxxxxxxxxx

...`
```

## Related topics

- [info](cloudhsm_mgmt_util-info.md "cloudhsm_mgmt_util-info.md")

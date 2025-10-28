# List HSMs with CloudHSM CLI

Use the **cluster hsm-info** command in CloudHSM CLI to list the hardware
security modules (HSMs) in your AWS CloudHSM cluster. You do not need to be logged in to CloudHSM CLI
to run this command.

###### Note

If you add or delete HSMs, update the
configuration files that the AWS CloudHSM client and the command line tools use.
Otherwise, the changes that you make might not be effective on all HSMs in the
cluster.

## User type

The following types of users can run this command.

- All users. You do not need to be logged in to run this command.

## Syntax

```
`aws-cloudhsm >` `help cluster hsm-info``List info about each HSM in the cluster

Usage: cloudhsm-cli cluster hsm-info [OPTIONS]

Options:
 --cluster-id `<CLUSTER_ID>` Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
 -h, --help Print help`

```

## Example

This command lists the HSMs present in your AWS CloudHSM cluster.

```
`aws-cloudhsm >` `cluster hsm-info``{
 "error_code": 0,
 "data": {
 "hsms": [
 {
 "vendor": "Marvell Semiconductors, Inc.",
 "model": "NITROX-III CNN35XX-NFBE",
 "serial-number": "5.3G1941-ICM000590",
 "hardware-version-major": "5",
 "hardware-version-minor": "3",
 "firmware-version-major": "2",
 "firmware-version-minor": "6",
 "firmware-build-number": "16",
 "firmware-id": "CNN35XX-NFBE-FW-2.06-16"
 "fips-state": "2 [FIPS mode with single factor authentication]"
 },
 {
 "vendor": "Marvell Semiconductors, Inc.",
 "model": "NITROX-III CNN35XX-NFBE",
 "serial-number": "5.3G1941-ICM000625",
 "hardware-version-major": "5",
 "hardware-version-minor": "3",
 "firmware-version-major": "2",
 "firmware-version-minor": "6",
 "firmware-build-number": "16",
 "firmware-id": "CNN35XX-NFBE-FW-2.06-16"
 "fips-state": "2 [FIPS mode with single factor authentication]"
 },
 {
 "vendor": "Marvell Semiconductors, Inc.",
 "model": "NITROX-III CNN35XX-NFBE",
 "serial-number": "5.3G1941-ICM000663",
 "hardware-version-major": "5",
 "hardware-version-minor": "3",
 "firmware-version-major": "2",
 "firmware-version-minor": "6",
 "firmware-build-number": "16",
 "firmware-id": "CNN35XX-NFBE-FW-2.06-16"
 "fips-state": "2 [FIPS mode with single factor authentication]"
 }
 ]
 }
}`
```

The output has the following attributes:

- **Vendor**: The vendor name of the HSM.
- **Model**: The model number of the HSM.
- **Serial-number**: The serial number of the HSM. This may change due to replacements.
- **Hardware-version-major**: The major hardware version.
- **Hardware-version-minor**: The minor hardware version.
- **Firmware-version-major**: The major firmware version.
- **Firmware-version-minor**: The minor firmware version.
- **Firmware-build-number**: The firmware build number.
- **Firmware-id**: The firmware ID, which includes the major and minor versions along with the build.
- **FIPS-state**: The FIPS mode the cluster and the HSMs in it. If in FIPS mode, the output is "2 [FIPS mode with single factor authentication]."
  If in non-FIPS mode, the output is "0 [non-FIPS mode with single factor authentication]".

## Related topics

- [Activate a cluster with CloudHSM CLI](cloudhsm_cli-cluster-activate.md "cloudhsm_cli-cluster-activate.md")

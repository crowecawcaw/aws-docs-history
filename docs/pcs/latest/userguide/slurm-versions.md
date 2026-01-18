# Slurm versions in AWS PCS

SchedMD continually enhances Slurm with new capabilities, optimizations, and security
patches. SchedMD releases a new major version at [regular intervals](https://slurm.schedmd.com/upgrades.html#release_cycle "https://slurm.schedmd.com/upgrades.html#release_cycle") and plans
to support up to 3 versions at any given time.
AWS PCS is designed to automatically update the Slurm controller with patch versions.

When SchedMD ends [support](https://slurm.schedmd.com/upgrades.html#compatibility_window "https://slurm.schedmd.com/upgrades.html#compatibility_window") for a particular major version, AWS PCS designates that version as End of Life (EOL). After EOL, no new clusters can be created with that version, though existing clusters can continue running for up to 12 months without guaranteed support. AWS PCS sends advance notice if a Slurm major version is close to EOL, to
help customers know when to upgrade their clusters to a newer supported version.

We recommend you use the latest supported Slurm version to deploy your cluster, to access the
most recent advancements and improvements.

## Supported Slurm versions in AWS PCS

The following table shows the supported Slurm versions and important dates and information for each version.

| Slurm version | SchedMD release date | AWS PCS release date | AWS PCS EOL date | Minimum compatible AWS PCS agent version | Supported AWS PCS sample AMIs                                                                     |
| ------------- | -------------------- | -------------------- | ---------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 25.05         | 5/29/2025            | 10/16/2025           | 11/30/2026       | 1.0.0-1                                  | • `aws-pcs-sample_ami-amzn2-x86_64-slurm-25.05`<br>• `aws-pcs-sample_ami-amzn2-arm64-slurm-25.05` |
| 24.11         | 11/29/2024           | 5/14/2025            | 5/31/2026        | 1.0.0-1                                  | • `aws-pcs-sample_ami-amzn2-x86_64-slurm-24.11`<br>• `aws-pcs-sample_ami-amzn2-arm64-slurm-24.11` |

## Unsupported Slurm versions in AWS PCS

The following table shows Slurm versions that aren't supported in AWS PCS.

| Slurm version | SchedMD release date | AWS PCS release date | AWS PCS EOL date |
| ------------- | -------------------- | -------------------- | ---------------- |
| 24.05         | 5/30/2024            | 12/18/2024           | 11/30/2025       |
| 23.11         | 11/21/2023           | 8/28/2024            | 5/31/2025        |

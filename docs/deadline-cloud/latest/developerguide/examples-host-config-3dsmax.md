# Install Autodesk 3ds Max on Deadline Cloud Windows workers

The
[3dsmax](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/3dsmax "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/3dsmax")
host configuration scripts install 3ds Max with renderer plugins such as
V-Ray, Corona, tyFlow, and AEC plugins on Windows service-managed fleet
workers. Because 3ds Max runs only on Windows and requires administrative
access to install, the recommended approach is to install it on the worker
host through a host configuration script.

The samples repository on GitHub includes scripts for the following
version and plugin combinations:

- [3dsmax-2024](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2024.ps1 "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2024.ps1")
  — 3ds Max 2024.
- [3dsmax-2025-and-vray](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2025-and-vray.ps1 "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2025-and-vray.ps1")
  — 3ds Max 2025 with V-Ray.
- [3dsmax-2025-and-corona-13](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2025-and-corona-13.ps1 "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2025-and-corona-13.ps1")
  — 3ds Max 2025 with Chaos Corona 13.
- [3dsmax-2025-vray-and-aec-plugins](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2025-vray-and-aec-plugins.ps1 "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2025-vray-and-aec-plugins.ps1")
  — 3ds Max 2025 with V-Ray and AEC plugins.
- [3dsmax-2025-vray-and-tyflow](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2025-vray-and-tyflow.ps1 "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2025-vray-and-tyflow.ps1")
  — 3ds Max 2025 with V-Ray and tyFlow.
- [3dsmax-2027](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2027.ps1 "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2027.ps1")
  — 3ds Max 2027.
- [3dsmax-2027-and-vray](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2027-and-vray.ps1 "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2027-and-vray.ps1")
  — 3ds Max 2027 with V-Ray.
- [3dsmax-2027-and-corona-14](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2027-and-corona-14.ps1 "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2027-and-corona-14.ps1")
  — 3ds Max 2027 with Chaos Corona 14.
- [3dsmax-2027-and-vray-and-tyflow](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2027-and-vray-and-tyflow.ps1 "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2027-and-vray-and-tyflow.ps1")
  — 3ds Max 2027 with V-Ray and tyFlow.
- [3dsmax-2027-vray-and-aec-plugins](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2027-vray-and-aec-plugins.ps1 "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/host_configuration_scripts/3dsmax/3dsmax-2027-vray-and-aec-plugins.ps1")
  — 3ds Max 2027 with V-Ray and AEC plugins.
  To generate a script for a different version, renderer, or plugin
  combination, you can use the
  [Kiro](https://kiro.dev "https://kiro.dev") AI agent with the bundled
  [3dsmax-host-config
  skill](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/skills/3dsmax-host-config "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/skills/3dsmax-host-config").

Each script downloads the 3ds Max installer from an Amazon S3 bucket in
your AWS account and runs it in silent mode. Autodesk provides 3ds Max as
a `.7z` archive, which the scripts expect repackaged as
`.zip`. Each script's README includes instructions for
creating the `.zip` archive and uploading it to Amazon S3.

Your fleet IAM role needs `s3:GetObject` permission for
the installers in Amazon S3.

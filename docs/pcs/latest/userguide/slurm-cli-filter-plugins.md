# Use Slurm CLI Filter Plugins to customize job

submission in AWS PCS

AWS PCS supports Slurm CLI Filter Plugins to run custom Lua scripts that validate and modify job submission parameters on login and compute nodes. For detailed information about CLI Filter Plugins, see the [cli_filter Plugin API documentation](https://slurm.schedmd.com/cli_filter_plugins.html "https://slurm.schedmd.com/cli_filter_plugins.html") on the SchedMD website.

## Requirements

CLI Filter Plugins require Slurm version 24.11 or later and a Lua script deployed to all login and compute nodes.

###### Important

For Slurm versions 24.11 and 25.05, CLI Filter Plugins require installing Slurm using AWS PCS Slurm installer (version 24.11.6-2+ or 25.05.4-1+). For more information about installing Slurm, see [Step 3 – Install Slurm](working-with_ami_custom_install-slurm.md "working-with_ami_custom_install-slurm.md").

## Limitations and security

considerations

- **Security enforcement** – CLI Filter Plugins can be easily bypassed
  by any user and must not be used for security-critical policies. Users can disable CLI Filter Plugins by providing a custom configuration that has `CLIFilterPlugins` disabled while submitting jobs.
- **Lua implementation only** – Lua script
  implementation is supported. C implementation is not supported.

###### Topics

- [Configure Slurm CLI Filter Plugins on an
  AWS PCS cluster](slurm-cli-filter-plugins-configure.md "slurm-cli-filter-plugins-configure.md")
- [Use Amazon S3 to deploy a CLI Filter Plugin script
  in AWS PCS](slurm-cli-filter-plugins-deploy-s3.md "slurm-cli-filter-plugins-deploy-s3.md")
- [Translate a Slurm Job Submit plugin script to
  use CLI Filter Plugin in AWS PCS](slurm-cli-filter-plugins-translate.md "slurm-cli-filter-plugins-translate.md")
- [Frequently asked questions about Slurm CLI Filter
  Plugins in AWS PCS](slurm-cli-filter-plugins-faq.md "slurm-cli-filter-plugins-faq.md")
- [Troubleshooting Slurm CLI Filter Plugin
  issues in AWS PCS](slurm-cli-filter-plugins-troubleshooting.md "slurm-cli-filter-plugins-troubleshooting.md")

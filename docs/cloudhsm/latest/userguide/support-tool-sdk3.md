# AWS CloudHSM Client SDK 3 support tool

The script for the AWS CloudHSM Client SDK 3 extracts the following information:

- Operating system and its current version
- Client configuration information from
  `cloudhsm_client.cfg`,
  `cloudhsm_mgmt_util.cfg`, and
  `application.cfg` files
- Client logs from the location specific to the platform
- Cluster and HSM information by using cloudhsm_mgmt_util
- OpenSSL information
- Current client and build version
- Installer version

## Running the info tool for Client SDK 3

The script creates an output file with all the gathered information. The script creates the output file inside the `/tmp`
directory.

**Linux**: `/opt/cloudhsm/bin/client_info`

**Windows**: `C:\Program
 Files\Amazon\CloudHSM\client_info`

###### Warning

This script has a known issue for Client SDK 3 versions 3.1.0 through 3.3.1. We strongly recommend you upgrade to version 3.3.2
which includes a fix for this issue. Please refer to the [Known Issues](ki-all.md#ki-all-9 "ki-all.md#ki-all-9")
page for more information before using this tool.

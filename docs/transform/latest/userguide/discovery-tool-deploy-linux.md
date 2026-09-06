

# Deploy on Linux
<a name="discovery-tool-deploy-linux"></a>

The discovery tool is available as a standalone Linux installer for deployment on supported Linux distributions. Use this option when you want to install the discovery tool directly on an existing Linux server instead of deploying a virtual machine.

## Linux server specifications
<a name="discovery-tool-linux-server-specs"></a>
+ **RAM** – We recommend allocating at least 16 GB
+ **CPU** – We recommend allocating at least 4 cores
+ **Disks** – 35 GB minimum. For larger inventories, see [Disk sizing and management](discovery-tool-disk-sizing.md).

## Supported distributions for the installer host
<a name="discovery-tool-linux-supported-distros"></a>
+ **Amazon Linux** – Amazon Linux 2, Amazon Linux 2023
+ **Red Hat Enterprise Linux and derivatives** – RHEL 8–9, Rocky Linux 8–9, AlmaLinux 9
+ **Ubuntu** – 20.04, 22.04, 24.04
+ **Debian** – 10, 11, 12
+ **SUSE** – SLES 15 SP5

## Install the discovery tool
<a name="discovery-tool-linux-install"></a>

Download the installer script from this URL: [https://s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/AWS-Transform-discovery-tool.sh](https://s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/AWS-Transform-discovery-tool.sh)

**To install the discovery tool on Linux**

1. Download the installer script to your Linux server.

   ```
   curl -O https://s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/AWS-Transform-discovery-tool.sh
   chmod +x AWS-Transform-discovery-tool.sh
   ```

1. (Optional) Run the compatibility check to verify that your system meets the requirements.

   ```
   sudo ./AWS-Transform-discovery-tool.sh check
   ```

1. Install the discovery tool. Choose one of the following options:

   **Option 1: Install with automatic dependency installation (recommended)**

   This option automatically installs any missing system dependencies before installing the service.

   ```
   sudo ./AWS-Transform-discovery-tool.sh install --install-deps
   ```

   **Option 2: Install without automatic dependency installation**

   This option checks for missing dependencies and displays errors with manual install instructions if critical dependencies are missing. Use this option if your organization restricts automatic package installation and you prefer to manage system packages manually.

   ```
   sudo ./AWS-Transform-discovery-tool.sh install
   ```

1. Start the discovery tool service.

   ```
   sudo ./AWS-Transform-discovery-tool.sh start
   ```

1. Access the discovery tool at `https://{{ip_address}}:5000`.

To uninstall the discovery tool, run `sudo ./AWS-Transform-discovery-tool.sh uninstall`.

You can also use the following commands to manage the service:
+ `sudo ./AWS-Transform-discovery-tool.sh status` – Check whether the service is running.
+ `sudo ./AWS-Transform-discovery-tool.sh stop` – Stop the service.
+ `sudo ./AWS-Transform-discovery-tool.sh logs` – View service logs.

## System dependencies
<a name="discovery-tool-linux-dependencies"></a>

The installer checks for the following system dependencies:


| Dependency | Severity | Purpose | 
| --- | --- | --- | 
| OpenSSL | Critical | Generates the database encryption key | 
| libcrypt | Critical | Required by the Python runtime | 
| Kerberos libraries | Warning | Required for Kerberos authentication to Windows servers. Without this, NTLM and basic authentication still work. | 

Critical dependencies are required for the discovery tool to start. If they are missing and you chose Option 2 (without `--install-deps`), the installer displays an error with instructions to install them manually. Warning-level dependencies are optional — the installer warns you but proceeds with installation.

**Note**  
The installer checks system compatibility including glibc version and systemd availability. On systems with systemd 250 or later (Amazon Linux 2023, RHEL 9, Rocky 9, AlmaLinux 9, Ubuntu 24.04\+, Debian 12\+), the database encryption key is encrypted at rest using systemd-creds. On older systems, the encryption key is stored as a permission-protected file.


# Configuring EFA clients
<a name="configure-efa-clients"></a>

Use the following procedures to set up your Lustre client to access an FSx for Lustre file system via Elastic Fabric Adapter (EFA).

EFA is supported on Lustre clients running the following operating systems:
+ Amazon Linux 2023 (AL2023)
+ Red Hat Enterprise Linux (RHEL) 9.5 or newer
+ Ubuntu 22.04 or newer with kernel version 6.8\+

EFA is supported on Lustre clients listed below. For more information, see [Installing the Lustre client](install-lustre-client.md).

EFA is supported on Nitro v4 (or higher) EC2 instances that support EFA, excluding the trn2 instance family. See [Supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types) in the *Amazon EC2 User Guide*.

**Topics**
+ [Step 1: Configure an EFA-enabled security group](#configure-efa-security-group)
+ [Step 2: Install required drivers](#install-required-drivers)
+ [Step 3: Configure EFA for the Lustre client](#install-efa-on-client)
+ [Step 4: EFA interfaces](#add-efa-interfaces)

## Step 1: Configure an EFA-enabled security group
<a name="configure-efa-security-group"></a>

Before you configure your EFA client, you must ensure that the security groups for both your file system and your Lustre clients allow EFA traffic. For instructions on configuring security groups for EFA, see [EFA-enabled security groups](limit-access-security-groups.md#efa-security-groups).

## Step 2: Install required drivers
<a name="install-required-drivers"></a>

**Note**  
If you are using a [Deep Learning AMI](https://docs.aws.amazon.com/dlami/latest/devguide/what-is-dlami.html), you can skip this step as the Lustre client, EFA driver and NVIDIA GPUDirect Storage (GDS) driver are pre-installed.

### Install the Lustre client and EFA driver
<a name="install-lustre-client-efa-driver"></a>

**To quickly install the Lustre client and EFA driver**

1. Download and unzip the file containing the installation script:

   ```
   curl -O https://docs.aws.amazon.com/fsx/latest/LustreGuide/samples/install-fsx-lustre-client.zip
   unzip install-fsx-lustre-client.zip
   ```

1. Change to the `install-fsx-lustre-client` folder and run the installation script:

   ```
   cd install-fsx-lustre-client
   sudo ./bin/install-fsx-lustre-client.sh --install-lustre --install-efa
   ```

   The script automatically does the following:
   + Installs the Lustre client
   + Installs the EFA driver
   + Verifies the Lustre client and EFA driver installation

   For a list of options and usage examples you can use with the `install-fsx-lustre-client.sh` script, see the `README.md` file in the zip file.

### Install the GDS driver (optional)
<a name="install-gds-driver"></a>

This step is only required if you plan to use NVIDIA GPUDirect Storage (GDS) with FSx for Lustre.

Requirements:
+ Amazon EC2 P5, P5e, P5en, or P6-B200 instance
+ NVIDIA GDS driver version 2.24.2 or higher

**To install the NVIDIA GPUDirect Storage driver on your client instance**

1. Clone the NVIDIA GDS repository:

   ```
   git clone https://github.com/NVIDIA/gds-nvidia-fs.git
   ```

1. Build and install the driver:

   ```
   cd gds-nvidia-fs/src/
   export NVFS_MAX_PEER_DEVS=128
   export NVFS_MAX_PCI_DEPTH=16
   sudo -E make
   sudo insmod nvidia-fs.ko
   ```

## Step 3: Configure EFA for the Lustre client
<a name="install-efa-on-client"></a>

To access an FSx for Lustre file system using an EFA interface, you must install the Lustre EFA modules and configure EFA interfaces.

### Quick setup
<a name="quick-setup"></a>

**To quickly configure your Lustre client**

1. Connect to your Amazon EC2 instance.

1. Download and unzip the file containing the configuration script:

   ```
   curl -O https://docs.aws.amazon.com/fsx/latest/LustreGuide/samples/configure-efa-fsx-lustre-client.zip
   unzip configure-efa-fsx-lustre-client.zip
   ```

1. Change to the `configure-efa-fsx-lustre-client` folder and run the setup script:

   ```
   cd configure-efa-fsx-lustre-client
   # for regular IO
   sudo ./setup.sh
   
   # for NVIDIA GPUDirect Storage (GDS) IO
   sudo ./setup.sh --optimized-for-gds
   ```

   The script automatically does the following:
   + Imports Lustre modules
   + Configures TCP and EFA interfaces
   + Creates a systemd service for automatic configuration on reboot

   For a list of options and usage examples you can use with the `setup.sh` script, see the `README.md` file in the zip file.

### Managing the systemd service manually
<a name="manage-systemd-service"></a>

The systemd service file is created at /etc/systemd/system/configure-efa-fsx-lustre-client.service. The following are some helpful systemd-related commands:

```
# Check status
sudo systemctl status configure-efa-fsx-lustre-client.service

# View logs
sudo journalctl -u configure-efa-fsx-lustre-client.service
# View warnings/errors from dmesg
sudo dmesg
```

For more information, see the `README.md` file in the zip file.

### Auto-mount configuration (optional)
<a name="auto-mount-configuration"></a>

For information on automatically mounting your Amazon FSx for Lustre file system on boot, see [Mounting your Amazon FSx file system automatically](mount-fs-auto-mount-onreboot.md).

## Step 4: EFA interfaces
<a name="add-efa-interfaces"></a>

Each FSx for Lustre file system has a maximum limit of 1024 EFA connections across all client instances.

The `configure-efa-fsx-lustre-client.sh` script automatically configures EFA interfaces based on the instance type.


| Instance Type | Default Number of EFA Interfaces | 
| --- | --- | 
| p6-b300.48xlarge | 16 | 
| p6e-gb200.36xlarge | 8 | 
| p6-b200.48xlarge | 8 | 
| p5en.48xlarge | 8 | 
| p5e.48xlarge | 8 | 
| p5.48xlarge | 8 | 
| Other instances with multiple network cards | 2 | 
| Other instances with a single network card | 1 | 

Each configured EFA interface on a client instance counts as one connection against the 1024 EFA connection limit when connected to an FSx for Lustre file system.

### Managing EFA interfaces manually
<a name="manage-interfaces-manually"></a>

Instances with more EFA interfaces typically support higher throughput. You can customize the number of interfaces to optimize performance for your specific workloads, as long as you stay within the total EFA connection limit.

You can manually manage EFA interfaces using the following commands:

1. View available EFA interfaces:

   ```
   for interface in /sys/class/infiniband/*; do
       if [ ! -e "$interface/device/driver" ]; then continue; fi
       driver=$(basename "$(realpath "$interface/device/driver")")
       if [ "$driver" != "efa" ]; then continue; fi
       echo $(basename $interface)
   done
   ```

1. View currently configured interfaces:

   ```
   sudo lnetctl net show
   ```

1. Add an EFA interface:

   ```
   sudo lnetctl net add --net efa --if {{device_name}} --peer-credits 32
   ```

   Replace {{device\_name}} with an actual device name from the list in step 1.

1. Remove an EFA interface:

   ```
   sudo lnetctl net del --net efa --if {{device_name}}
   ```

   Replace {{device\_name}} with an actual device name from the list in step 2.
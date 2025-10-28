# Configuring EFA clients

Use the following procedures to set up your Lustre client to access
an FSx for Lustre file system via Elastic Fabric Adapter (EFA).

EFA is supported on Lustre clients running the following operating systems:

- Amazon Linux 2023 (AL2023)
- Red Hat Enterprise Linux (RHEL) 9.5 or newer
- Ubuntu 22.04 or newer with kernel version 6.8+
  EFA is supported on Lustre clients listed below. For more information,
  see [Installing the Lustre client](install-lustre-client.md "install-lustre-client.md").

EFA is supported on Nitro v4 (or higher) EC2 instances that support EFA, excluding the trn2 instance family.
See [Supported
instance types](../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types "../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types") in the _Amazon EC2 User Guide_.

###### Topics

- [Step 1: Install required drivers](#install-required-drivers "#install-required-drivers")
- [Step 2: Configure EFA for the Lustre client](#install-efa-on-client "#install-efa-on-client")
- [Step 3: EFA interfaces](#add-efa-interfaces "#add-efa-interfaces")

## Step 1: Install required drivers

###### Note

If you are using a [Deep Learning AMI](../../../dlami/latest/devguide/what-is-dlami.md "../../../dlami/latest/devguide/what-is-dlami.md"),
you can skip this step as both the EFA driver and NVIDIA GPUDirect Storage (GDS) driver are pre-installed.

### Install the EFA driver

Follow the instructions in
[Step 3:
Install the EFA software](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-enable "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-enable") in the _Amazon EC2 User Guide_.

### Install the GDS driver (optional)

This step is only required if you plan to use NVIDIA GPUDirect Storage (GDS) with FSx for Lustre.

Requirements:

- Amazon EC2 P5, P5e, P5en, P6-B200, or P6e-GB200 instance
- NVIDIA GDS driver version 2.24.2 or higher

###### To install the NVIDIA GPUDirect Storage driver on your client instance

1. Clone the NVIDIA GDS repository:

```
`git clone https://github.com/NVIDIA/gds-nvidia-fs.git`
```

2. Build and install the driver:

```
`cd gds-nvidia-fs/src/
export NVFS_MAX_PEER_DEVS=128
export NVFS_MAX_PCI_DEPTH=16
sudo -E make
sudo insmod nvidia-fs.ko`
```

## Step 2: Configure EFA for the Lustre client

To access an FSx for Lustre file system using an EFA interface, you must install the Lustre EFA modules and
configure EFA interfaces.

### Quick setup

###### To quickly configure your Lustre client

1. Connect to your Amazon EC2 instance.
2. Download and unzip the file containing the configuration script:

```
`curl -O https://docs.aws.amazon.com/fsx/latest/LustreGuide/samples/configure-efa-fsx-lustre-client.zip
unzip configure-efa-fsx-lustre-client.zip`
```

3. Change to the `configure-efa-fsx-lustre-client` folder and run the setup script:

```
`cd `configure-efa-fsx-lustre-client`
sudo ./setup.sh`
```

The script automatically does the following:

    * Imports Lustre modules
    * Configures TCP and EFA interfaces
    * Creates a systemd service for automatic configuration on reboot

For a list of options and usage examples you can use with the
`setup.sh` script, see the `README.md` file in the zip file.

### Managing the systemd service manually

The systemd service file is created at /etc/systemd/system/configure-efa-fsx-lustre-client.service.
The following are some helpful systemd-related commands:

```
`# Check status
sudo systemctl status configure-efa-fsx-lustre-client.service

# View logs
sudo journalctl -u configure-efa-fsx-lustre-client.service
# View warnings/errors from dmesg
sudo dmesg`
```

For more information, see the `README.md` file in the zip file.

### Auto-mount configuration (optional)

For information on automatically mounting your Amazon FSx for Lustre file system on boot,
see [Mounting your Amazon FSx file system
automatically](mount-fs-auto-mount-onreboot.md "mount-fs-auto-mount-onreboot.md").

## Step 3: EFA interfaces

Each FSx for Lustre file system has a maximum limit of 1024 EFA connections across all client instances.

The `configure-efa-fsx-lustre-client.sh` script automatically configures EFA interfaces based on the instance type.

| Instance Type                               | Default Number of EFA Interfaces |
| ------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| p6e-gb200.36xlarge                          | 8                                |
| p6-b200.48xlarge                            | 8                                |
| p5en.48xlarge                               | 8                                |
| p5e.48xlarge                                | 8                                |
| p5.48xlarge                                 | 8                                |
| Other instances with multiple network cards | 2                                |
| Other instances with a single network card  | 1                                | Each configured EFA interface on a client instance counts as one connection against the 1024 EFA connection limit when connected to an FSx for Lustre file system. ### Managing EFA interfaces manually Instances with more EFA interfaces typically support higher throughput. You can customize the number of interfaces to optimize performance for your specific workloads, as long as you stay within the total EFA connection limit. You can manually manage EFA interfaces using the following commands: 1. View available EFA devices: `` `for interface in /sys/class/infiniband/*; do if [ ! -e "$interface/device/driver" ]; then continue; fi driver=$(basename "$(realpath "$interface/device/driver")") if [ "$driver" != "efa" ]; then continue; fi echo $(basename $interface) done` `` 2. View currently configured interfaces: `` `sudo lnetctl net show` `` 3. Add an EFA interface: `` `sudo lnetctl net add --net efa --if `device_name` —peer-credits 32` `` Replace `device_name` with an actual device name from the list in step 1. 4. Remove an EFA interface: ``` `sudo lnetctl net del --net efa --if `device_name`` ``` Replace `device_name` with an actual device name from the list in step 2. |

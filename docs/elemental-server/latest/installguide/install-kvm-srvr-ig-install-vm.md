This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Step B: Deploy the VM

Perform these steps from your workstation.

1. Place the OVA file in a convenient location accessible to the VM host.
2. Start the Virtual Machine Manager client and choose **File**
   > **Create New Virtual Machine**.
3. In the **New VM** dialog, choose **Import existing
   disk image** and select **Forward**.
4. Complete the fields as described in the following table and then select
   **Forward**.

| Screen and Field                         | Action                                                      |
| ---------------------------------------- | ----------------------------------------------------------- |
| **Provide the existing storage<br>path** | Select the location where the OVA image file is<br>located. |
| **OS type**                              | Select **Linux**.                                           |
| **Version**                              | Select **CentOS 6.5**.                                      |

5. Complete the memory and CPU fields as described in the following table and
   then select **Forward**.

| Screen and Field | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Memory (RAM)** | Choose a minimum of 15259 MiB (16GB). If your physical system<br>has additional RAM available, choose more for improved performance.NoteIf you oversubscribe your memory for your virtual<br>machine and there isn't enough for the host, then<br>you might see performance degradation in the<br>AWS Elemental Server software.                                                                                                                       |
| **CPUs**         | Choose **24**.ImportantEnsure that the number of cores you select matches<br>your AWS Elemental licensing. To check the cores available with<br>your license, see the **Activations**<br>information at [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations "https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations"). |

6. Complete the installation fields as described in the following table and
   choose **Finish**.

| Screen and Field      | Action                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Name**              | Type a descriptive name for the VM. This will be the hostname<br>that you use to access AWS Elemental Server. |
| **Network selection** | Use this section to configure your system according to your<br>network setup.                                 |

The OVA is installed and the VM is created. 7. Before proceeding, take a snapshot of the VM, as described in the CentOS 7
online help. 8. Repeat these steps to install the OVA on all of the VM instances.

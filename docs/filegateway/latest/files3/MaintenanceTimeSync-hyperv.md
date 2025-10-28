# Synchronize VM time with Hyper-V or Linux KVM

host time

For a gateway deployed on VMware ESXi, setting the hypervisor host time and synchronizing
the virtual machine time to the host is sufficient to avoid time drift. For more
information, see [Synchronize VM time with VMware host
time](GettingStartedSyncVMTime-common.md "GettingStartedSyncVMTime-common.md"). For a gateway deployed on Microsoft
Hyper-V or Linux KVM, we recommend that you periodically check the virtual machine time
using the procedure described following.

###### To view and synchronize the time of a hypervisor gateway virtual machine to a Network

Time Protocol (NTP) server

1. Log in to your gateway's local console:
   - For more information on logging in to the Microsoft Hyper-V local console,
     see [Access the Gateway Local Console
     with Microsoft Hyper-V](accessing-local-console.md#MaintenanceConsoleWindowHyperV-common "accessing-local-console.md#MaintenanceConsoleWindowHyperV-common").
   - For more information on logging in to the local console for Linux
     Kernel-based Virtual Machine (KVM), see [Accessing the Gateway Local Console
     with Linux KVM](accessing-local-console.md#MaintenanceConsoleWindowKVM-common "accessing-local-console.md#MaintenanceConsoleWindowKVM-common").

2. On the **Storage Gateway Configuration** main menu screen, enter the
   corresponding numeral to select **System Time Management**.
3. On the **System Time Management** menu screen, enter the
   corresponding numeral to select **View and Synchronize System
   Time**.

The gateway local console displays the current system time and compares it with
the time reported by the NTP server, then reports the exact discrepancy between the
two times in seconds. 4. If the time discrepancy is greater than 60 seconds, enter `y`
to synchronize the system time with NTP time. Otherwise, enter
`n`.

Time synchronization might take a few moments.

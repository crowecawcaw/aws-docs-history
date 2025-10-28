# Switching to Legacy on a

SuperMicro

To switch the boot mode from UEFI back to BIOS (Legacy mode), you can use the IPMI
interface, or you can work when directly connected to the server.

## Install Java

applet

Decide if you want to use the IPMI management console, or if you plan to
connect directly to the server. If you want to use the console, decide if you
want to use the Java remote console applet to access the console, or if you want
to use HTML5.

If you want to use the Java remote console applet, you might need to install
it. See [Step 1: Install Java
applet](migrate-topic-uefi-supermicro.md#migrate-topic-uefi-supermicro-applet "migrate-topic-uefi-supermicro.md#migrate-topic-uefi-supermicro-applet").

## Change the mode to

BIOS

This procedure is nearly identical to the procedure for [switching to UEFI](migrate-topic-uefi-supermicro.md "migrate-topic-uefi-supermicro.md"). You change
the same fields on the **Setup Utility** screen, but you
specify either `Legacy` or `Disabled`.

1. From the IPMI management console, sign in to the server as the
   _elemental_ user.
2. Reboot the system:

```
[elemental@hostname sudo reboot
```

The system starts to reboot. The window size might change as the
system is rebooting. 3. While the system is rebooting, repeatedly press the **Delete** key on the keyboard (or the **del** button on the virtual keyboard). The
**Setup Utility** screen appears.

You can use these keys to work on the screen:

    * The arrow keys
    * Enter to select
    * ESC to return to the previous screen.

4. On the main menu, choose **Advanced**.
5. In **sSATA Configuration**, change the following line
   to **Legacy**:
   - **sSATA RAID Option ROM/UEFI Driver**

6. In **PCIe/PCI/PnP Configuration**, change the
   following lines to **Legacy**:
   - **AOC-URN2-14GXS-SLOT1 PCI-E 3.0 X8
     OPROM**
   - **RSC-RIUW-EBR SLOT1 PCI-E X8 OPROM**
   - **RSC-RIUW-2E16 SLOT1 PCI-E X16
     OPROM**
   - **RSC-RIUW-2E16 SLOT2 PCI-E X16
     OPROM**
   - **Onboard LAN OPROM Type**
   - **Onboard Video OPROM**

7. Still in **PCIe/PCI/PnP Configuration**, change the
   following lines to **Disabled:**
   - **Onboard LAN NVMe1 OPROM**
   - **Onboard LAN NVMe2 OPROM**

8. Select **F4**. On the **Save &
   Exit** dialog, choose **Yes**.

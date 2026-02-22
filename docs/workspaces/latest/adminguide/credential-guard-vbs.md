# Credential Guard / Virtualization-Based Security (VBS)

Windows WorkSpaces can utilize Credential Guard and Virtualization-Based Security (VBS) to provide hardware-based isolation and protect credentials within the operating system.
You can disable Credential Guard or VBS through Group Policy settings.

###### Important

Disabling VBS reduces the security posture of your Windows WorkSpace. Only disable
VBS if required for specific performance or compatibility needs.

**Security implications of disabling VBS**

- **Reduced kernel-level protection** – The OS kernel becomes more vulnerable to malicious code.
- **Increased risk of credential theft** – Attackers may more easily extract credentials from the lsass.exe process.
- **Disabled code integrity checks** – Hypervisor-Enforced Code Integrity (HVCI) will not function, allowing unsigned drivers to run in kernel mode.
- **Increased vulnerability to exploits** – The system becomes more susceptible to attacks that could result in full system compromise.
- **Loss of advanced security features** – Features such as Windows Defender Credential Guard and System Guard cannot operate as intended.

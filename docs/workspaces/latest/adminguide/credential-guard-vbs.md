

# Credential Guard / Virtualization-Based Security (VBS)
<a name="credential-guard-vbs"></a>

Windows WorkSpaces can utilize Credential Guard and Virtualization-Based Security (VBS) to provide hardware-based isolation and protect credentials within the operating system. You can disable Credential Guard or VBS through Group Policy settings.

**Note**  
When you enable nested virtualization on a Windows WorkSpace, Credential Guard and VBS are automatically disabled. This is required because nested virtualization uses the hardware virtualization extensions that VBS relies on. If you need both Credential Guard and nested virtualization, they cannot be enabled on the same WorkSpace simultaneously. For more information, see [Nested virtualization for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/nested-virtualization.html) and [Use nested virtualization to run hypervisors in Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html).

**Important**  
Disabling VBS reduces the security posture of your Windows WorkSpace. Only disable VBS if required for specific performance or compatibility needs.

**Security implications of disabling VBS**
+ **Reduced kernel-level protection** – The OS kernel becomes more vulnerable to malicious code.
+ **Increased risk of credential theft** – Attackers may more easily extract credentials from the lsass.exe process.
+ **Disabled code integrity checks** – Hypervisor-Enforced Code Integrity (HVCI) will not function, allowing unsigned drivers to run in kernel mode.
+ **Increased vulnerability to exploits** – The system becomes more susceptible to attacks that could result in full system compromise.
+ **Loss of advanced security features** – Features such as Windows Defender Credential Guard and System Guard cannot operate as intended.
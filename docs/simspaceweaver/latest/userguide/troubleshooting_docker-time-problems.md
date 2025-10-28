End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Problems related to time when

using Docker

If you are using Docker and you receive time-related errors while
running scripts from the SimSpace Weaver app SDK, the cause could be that your
Docker virtual machine clock is incorrect. This can happen if your
computer was running Docker and then resumes from sleep or
hibernation.

###### Solutions to try

- Restart Docker.
- Disable and then re-enable time synchronization in **Windows PowerShell**:

```
Get-VMIntegrationService -VMName DockerDesktopVM -Name "Time Synchronization" | Disable-VMIntegrationService
Get-VMIntegrationService -VMName DockerDesktopVM -Name "Time Synchronization" | Enable-VMIntegrationService
```

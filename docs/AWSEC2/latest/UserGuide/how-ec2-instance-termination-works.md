# How instance termination

works

When you terminate an instance, changes are registered at the operating system (OS)
level of the instance, some resources are lost, and some resources persist.

The following diagram shows what is lost and what persists when an Amazon EC2 instance is
terminated. When an instance terminates, the data on any instance store volumes and the
data stored in the instance RAM is erased. Any Elastic IP addresses associated with the
instance are detached. For Amazon EBS root volumes and data volumes, the outcome depends on
the **Delete on termination** setting of each volume.

![The IP addresses, RAM, instance store volumes, and EBS root volume are lost when an instance is terminated.](images/terminate-instance.png)

## Considerations

- **Data persistence**
  - Instance store volumes: All data is permanently deleted when the
    instance terminates.
  - EBS root volume:
    - When attached at launch, deleted by default when the
      instance terminates.
    - When attached after launch, persists by default when the
      instance terminates.

  - EBS data volumes:
    - When attached at launch using the console: Persists by
      default when the instance terminates.
    - When attached at launch using the CLI: Deleted by default
      when the instance terminates.
    - When attached after launch using the console or CLI:
      Persists by default when the instance terminates.

    ###### Note

    Any volumes that are not deleted on instance
    termination continue to incur charges. You can change
    the setting so that a volume is deleted or persists on
    instance termination. For more information, see [Preserve data when an instance is
    terminated](preserving-volumes-on-termination.md "preserving-volumes-on-termination.md").

- **Protection against accidental
  termination**
  - To prevent an instance from being accidentally terminated by
    someone, [enable
    termination protection](Using_ChangingDisableAPITermination.md "Using_ChangingDisableAPITermination.md").
  - To control whether an instance stops or terminates when shutdown
    is initiated from the instance, change the [instance initiated shutdown behavior](Using_ChangingInstanceInitiatedShutdownBehavior.md "Using_ChangingInstanceInitiatedShutdownBehavior.md").

- **Shutdown scripts** – If you run a
  script on instance termination, your instance might have an abnormal
  termination because we have no way of ensuring that shutdown scripts run.
  Amazon EC2 attempts to cleanly shut down an instance and run any system shutdown
  scripts; however, certain events (such as hardware failure) may prevent
  these system shutdown scripts from running.
- **Bare metal instances** – x86 bare
  metal instances don't support cooperative shutdown.

## What happens when you terminate an

instance

###### Changes registered at the OS level

- The API request sends a button press event to the guest.
- Various system services are stopped as a result of the button press event.
  Graceful shutdown of the system is provided by **systemd**
  (Linux) or the System process (Windows). Graceful shutdown is triggered by
  the ACPI shutdown button press event from the hypervisor.
- ACPI shutdown is initiated.
- The instance shuts down after the graceful shutdown process exits. There
  is no configurable OS shutdown time. The instance remains visible in the
  console for a short time, then the entry is automatically deleted.

###### Resources lost

- Data stored on the instance store volumes.
- EBS root volume if the `DeleteOnTermination` attribute is set to
  `true`.
- EBS data volumes (attached at launch or after) if the `DeleteOnTermination`
  attribute is set to `true`.

###### Resources that persist

- EBS root volume if the `DeleteOnTermination` attribute is set to
  `false`.
- EBS data volumes (attached at launch or after) if the `DeleteOnTermination`
  attribute is set to `false`.

## Test application response to instance

termination

You can use AWS Fault Injection Service to test how your application responds when your instance is
terminated. For more information, see the [AWS Fault Injection Service User Guide](../../../fis/latest/userguide/what-is.md "../../../fis/latest/userguide/what-is.md").

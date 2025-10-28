# Working with Tape Gateway storage

resources

The topics in this section describe how to manage the storage resources associated
with your Tape Gateway, such as the physical disks attached to a gateway's virtual host
platform, the Amazon EBS volumes attached to a gateway's Amazon EC2 instance, your virtual tape
library devices such as medium changers, and the tapes in your virtual tape
libraries.

**Topics**

- [Removing Disks from Your Gateway](add-remove-disks.md "add-remove-disks.md") - Learn
  about what to do if you need to remove a disk from the virtual host platform for
  your gateway, for example if you have a failed disk.
- [Managing Amazon EBS volumes on Amazon EC2
  gateways](GatewayInstanceStorage-common.md "GatewayInstanceStorage-common.md") - Learn about how you can
  increase or reduce the quanity of Amazon EBS volumes that are allocated for use as
  upload buffer or cache storage for a gateway that is hosted on an Amazon EC2
  instance.
- [Working with VTL Devices](resource_vtl-devices.md "resource_vtl-devices.md") -
  Learn about how to manage your virtual tape library devices, including how to
  select a medium changer for a Tape Gateway, how to update the device driver for
  a medium changer, and how to display barcodes for tapes in Microsoft System
  Center Data Protection Manager.
- [Managing tapes in your virtual tape
  library](managing-virtual-tapes-vtl.md "managing-virtual-tapes-vtl.md") - Learn about how to manage the
  tapes and virtual tape libraries associated with your Tape Gateway, including
  how to manually archive tapes and cancel tape archival that is in
  progress.

# Add storage to a virtual computer in Lightsail for Research

Complete the following steps to attach a disk to a virtual computer in Lightsail for Research. You can
attach up to 15 disks to a virtual computer. When you attach a disk to your virtual
computer using the Lightsail for Research console, it is automatically formatted and mounted by the
service. This process takes a few minutes, so you should confirm that the disk has
reached a **Mounted** mounting status before you start using it. By
default, Lightsail for Research mounts disks to the
`/home/lightsail-user/`<disk-name>` directory; where`<disk-name>`` is the name
you gave your disk.

###### Important

Before you can attach a disk to a virtual computer, the virtual computer must be
in a _Running_ state. If you attach a disk to a virtual computer
while it’s in a _Stopped_ state, the disk will be attached but
fail to mount. If the disk's **Mount status** is
_Failed_, you must detach the disk then reattach it when the
virtual computer is in a _Running_ state.

1. Sign in to the [Lightsail for Research console](https://lfr.console.aws.amazon.com/ls/research "https://lfr.console.aws.amazon.com/ls/research").
2. Choose **Virtual computers** in the navigation pane.
3. Choose the computer to attach the disk to.
4. Choose the **Storage** tab.
5. Choose **Attach disk**.
6. Select the name of the disk to attach to the computer.
7. Choose **Attach**.

# Control your desktop state

To control your desktop's state:

1. Choose **Actions**.

![Virtual desktops](images/res-virtualdesktops.png) 2. Choose **Virtual Desktop State**. You have four
states to select from:

    * **Stop**


    A stopped session will not suffer data loss, and you can restart a
     stopped session at any time.
    * **Reboot**


    Reboots current session.
    * **Terminate**


    Permanently ends a session. Terminating a session may cause data loss
     if you are using ephemeral storage. You should backup your data to the
     RES filesystem before terminating.
    * **Hibernate**


    Your desktop state will be saved in memory. When you restart the desktop,
     your applications will resume but any remote connections may be lost.
     Not all instances support hibernation, and the option is only available
     if it was enabled during instance creation. To verify if your instance
     supports this state, see [Hibernation
     prerequisites](../../../AWSEC2/latest/UserGuide/hibernating-prerequisites.md "../../../AWSEC2/latest/UserGuide/hibernating-prerequisites.md").

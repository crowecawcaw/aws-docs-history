

# Control your desktop state
<a name="control-desktop-state"></a>

To control your desktop's state:

1. Choose **Actions**.   
![Virtual desktops](http://docs.aws.amazon.com/res/latest/ug/images/res-virtualdesktops.png)

1. Choose **Virtual Desktop State**. You have four states to select from:
   + **Stop**

     Stopping a session does not cause data loss, and you can restart a stopped session at any time.
   + **Reboot**

     Reboots current session.
   + **Terminate**

     Permanently ends a session. Terminating a session may cause data loss if you are using ephemeral storage. Back up your data to the RES filesystem before terminating.
   + **Hibernate**

     Your desktop state is saved to disk. When you restart the desktop, your applications resume but any remote connections may be lost. Not all instances support hibernation, and the option is only available if it was enabled during instance creation. To verify if your instance supports this state, see [Hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html). 
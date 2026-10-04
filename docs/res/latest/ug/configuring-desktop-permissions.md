

End of development notice: AWS is discontinuing development of Research and Engineering Studio on AWS (RES). 2026.09 is the final release, supported through September 30, 2027. RES remains open source and keeps running in your account. For more information, see [RES end of support](res-end-of-support.md).

# Configuring Desktop Permissions
<a name="configuring-desktop-permissions"></a>

Administrators can toggle **Desktop permissions** on or off to globally manage the VDI functionality of all session owners. All of these permissions, or a subset, can be used to create **Desktop sharing profiles** that determine which actions the users with whom a desktop is shared can perform. If any desktop permission is disabled, this will automatically disable the corresponding permissions in the **Desktop sharing profiles**. These permissions will be labeled as "Disabled Globally". Even if the administrator enables this desktop permission again, the permission in the desktop sharing profile will remain disabled until the administrator manually enables it.

![environment boundaries](https://docs.aws.amazon.com/res/latest/ug/images/permission-policy-environment-boundaries.png)

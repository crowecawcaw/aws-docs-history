

End of development notice: AWS is discontinuing development of Research and Engineering Studio on AWS (RES). 2026.09 is the final release, supported through September 30, 2027. RES remains open source and keeps running in your account. For more information, see [RES end of support](res-end-of-support.md).

# Desktop settings
<a name="desktop-settings"></a>

You can use the Desktop Settings page to configure resources associated with virtual desktops.

![Desktop settings](https://docs.aws.amazon.com/res/latest/ug/images/res-virtual-desktop-settings.png)


**General**

The **General** tab provides access to settings such as:

**QUIC**  
Enables QUIC in favor of TCP as the default streaming protocol for all your virtual desktops.

**Default DCV Session Type**  
The default DCV Session Type used for all virtual desktops. This setting will not apply to previously created desktops. This will only apply in cases where the Instance Type and Operating System supports either Virtual or Console Session types.  
**Virtual session type deprecated**  
Starting with the 2026.06 release, the *Virtual* session type is no longer supported. All sessions now use the *Console* session type. If your configuration or automation specifies the Virtual session type, update it to use Console.

**Default Allowed Sessions Per User Per Project**  
The default value for the allowed number of VDI sessions per user per project.

**DCV Session Token Expiration**  
The duration for which a DCV session token remains valid. When a token expires, users must re-download the DCV connection file from the web portal to continue accessing their virtual desktop session. The available options are:  
+ 1,440 minutes (1 day)
+ 10,080 minutes (7 days)
+ 43,200 minutes (30 days)

![DCV session token expiration setting in Desktop Settings](https://docs.aws.amazon.com/res/latest/ug/images/dcv-settings-form.png)


**Server**

The **Server** tab provides access to settings such as:

**DCV session idle timeout**  
The time after which the DCV session will be automatically disconnected. This does not change the state of the desktop session, it only closes the session from either the DCV client or the web browser.

**Idle timeout warning**  
The time after which an idle warning will be provided to the client.

**CPU utilization threshold**  
The CPU utilization to be considered idle.

**Max root volume size**  
The default size of the root volume on virtual desktop sessions.

**Allowed instance types**  
The list of instance families and sizes that can be launched for this RES environment. Instance family and instance size combinations are both accepted. For example, if you specify 'm7a', all sizes of the m7a family will be available to launch as VDI sessions. If you specify 'm7a.24xlarge', only m7a.24xlarge will be available to launch as a VDI session. This list affects all projects in the environment.

**Smart retry**  
Enables RES to automatically select the instance type and subnet at launch time for all virtual desktops. RES tries multiple instance type and subnet combinations from the software stack's allowed instance types until one has capacity. When this setting is enabled, the instance type and subnet cannot be set on the session request. Smart retry applies only when launching new virtual desktops and does not apply when resuming existing desktops. To manually update the instance type of a virtual desktop after launch, first disable smart retry.

![Desktop settings](https://docs.aws.amazon.com/res/latest/ug/images/res-virtual-desktop-settings2.png)

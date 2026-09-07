

# Bundles and images for WorkSpaces Pools
<a name="pools-images"></a>

**Note**  
After careful consideration, we decided to end support for Amazon WorkSpaces Pools, effective December 31, 2027. Amazon WorkSpaces Pools will no longer accept new customers beginning July 31, 2026. As an existing customer, you can continue to use the service as normal until December 31, 2027. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see [Amazon WorkSpaces Pools end of support](wsp-pools-end-of-support.md).

A *WorkSpace bundle* is a combination of an operating system, and storage, compute, and software resources. When you launch a WorkSpace, you select the bundle that meets your needs. The default bundles available for WorkSpaces are called *public bundles*. For more information about the various public bundles available for WorkSpaces, see [Amazon WorkSpaces Bundles](https://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles).

If you've launched a Windows WorkSpace and have customized it, you can create a custom image from that WorkSpace for use with WorkSpaces Pool. Linux are not supported in WorkSpaces Pool.

A *custom image* contains only the OS, software, and settings for the WorkSpace. A *custom bundle* is a combination of both that custom image and the hardware from which a WorkSpace can be launched.

After you create a custom image, you can build a custom bundle that combines the custom WorkSpace image and the underlying compute and storage configuration that you select. You can then specify this custom bundle when you create new WorkSpaces Pools to ensure that the new WorkSpaces in the pool have the same consistent configuration (hardware and software).

If you need to perform software updates or to install additional software on your WorkSpaces, you can update your custom bundle and use it to rebuild your WorkSpaces.

WorkSpaces Pools supports several different operating systems (OS), streaming protocols, and bundles. The following table provides information about the licensing, streaming protocols, and bundles that are supported by each OS.


| Operating System | Licenses | Streaming protocols | Supported bundles | Lifecycle policy / retirement date | 
| --- | --- | --- | --- | --- | 
| Windows Server 2019 | Included | DCV | Value, Standard, Performance, Power, PowerPro | [January 9, 2029](https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2019) | 
| Windows Server 2022 | Included | DCV | Standard, Performance, Power, PowerPro, Graphics.G4dn, GraphicsPro.G4dn | [October 14, 2031](https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2022) | 

**Note**  
Operating system versions that are no longer supported by the vender are not guaranteed to work and are not supported by AWS support.

**Topics**
+ [Bundle options for WorkSpaces Pools](pools-custom-images-bundles.md)
+ [Create a custom image and bundle for WorkSpaces Pools](pools-images-custom-image.md)
+ [Manage custom images and bundles for WorkSpaces Pools](pools-images-managing.md)
+ [Use session scripts to manage your users' streaming experience](pools-images-session-scripts.md)
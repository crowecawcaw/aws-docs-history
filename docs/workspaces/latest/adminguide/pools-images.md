# Bundles and images for WorkSpaces Pools

A _WorkSpace bundle_ is a combination of an operating system, and
storage, compute, and software resources. When you launch a WorkSpace, you select the bundle
that meets your needs. The default bundles available for WorkSpaces are called _public bundles_. For more information about the various public
bundles available for WorkSpaces, see [Amazon WorkSpaces Bundles](https://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles "https://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles").

If you've launched a Windows WorkSpace and have customized it, you can create a custom
image from that WorkSpace for use with WorkSpaces Pool. Linux are not supported in
WorkSpaces Pool.

A _custom image_ contains only the OS, software, and settings for the
WorkSpace. A _custom bundle_ is a combination of both that
custom image and the hardware from which a WorkSpace can be launched.

After you create a custom image, you can build a custom bundle that combines the custom
WorkSpace image and the underlying compute and storage configuration that you select. You
can then specify this custom bundle when you create new WorkSpaces Pools to ensure that the new
WorkSpaces in the pool have the same consistent configuration (hardware and software).

If you need to perform software updates or to install additional software on your WorkSpaces,
you can update your custom bundle and use it to rebuild your WorkSpaces.

WorkSpaces Pools supports several different operating systems (OS), streaming protocols, and
bundles. The following table provides information about the licensing, streaming protocols,
and bundles that are supported by each OS.

| Operating System    | Licenses | Streaming protocols | Supported bundles                                                                    | Lifecycle policy / retirement date                                                                                                                                      |
| ------------------- | -------- | ------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows Server 2019 | Included | DCV                 | Value, Standard, Performance, Power, PowerPro                                        | [January 9, 2029](https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2019 "https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2019")  |
| Windows Server 2022 | Included | DCV                 | Standard, Performance, Power, PowerPro, Graphics.g6, Graphics.G4dn, GraphicsPro.G4dn | [October 14, 2031](https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2022 "https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2022") |

###### Note

- Operating system versions that are no longer supported by the vender are not
  guaranteed to work and are not supported by AWS support.

###### Topics

- [Bundle options for WorkSpaces Pools](pools-custom-images-bundles.md "pools-custom-images-bundles.md")
- [Create a custom image and bundle for
  WorkSpaces Pools](pools-images-custom-image.md "pools-images-custom-image.md")
- [Manage custom images and bundles for
  WorkSpaces Pools](pools-images-managing.md "pools-images-managing.md")
- [Use session scripts to manage your
  users' streaming experience](pools-images-session-scripts.md "pools-images-session-scripts.md")

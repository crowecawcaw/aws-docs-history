# Optimizing the Launch Performance of Your Applications in Amazon AppStream 2.0

When you create an image, AppStream 2.0 requires that you optimize the launch performance of your applications for your users' streaming sessions. When your applications are opened during this process, make sure that they use the initial components required by your users. Doing so ensures that these components are captured by the optimization process. In some cases, not all of the files required for the optimizations are detected. Examples of such files would be plug-ins or components that aren't opened in the image builder. To ensure that all of the files needed for your application are captured, you can include them in the optimization manifest. Adding files to the optimization manifest may increase the time it takes for fleet instances to be created and made available for users. Doing so, however, reduces the time it takes for the application to be launched the first time on the fleet instance.

To optimize all the files in a folder, open PowerShell and use the following
PowerShell command:

```
`dir -path` "`C:\Path\To\Folder\To\Optimize`" `-Recurse -ErrorAction SilentlyContinue | %{$_.FullName} | Out-File "C:\ProgramData\Amazon\Photon\Prewarm\PrewarmManifest.txt" -encoding UTF8 -append`
```

By default, Image Assistant replaces the application optimization manifest each time
the Image Assistant **Optimize** step runs. You must run the
PowerShell command to optimize all files in a folder:

- Each time after the **Optimize** step runs.
- Before you choose **Disconnect and create image** on the Image Assistant
  **Review** page.
  Alternatively, you can specify the optimization manifest on a per-application basis by
  using the Image Assistant command line interface (CLI) operations. When you specify the optimization manifest by using the Image Assistant CLI operations, AppStream 2.0 merges the specified application optimization manifest with the files identified by the Image Assistant **Optimize** step. For more
  information, see [Create Your Amazon AppStream 2.0 Image Programmatically by Using the Image Assistant CLI Operations](programmatically-create-image.md "programmatically-create-image.md").

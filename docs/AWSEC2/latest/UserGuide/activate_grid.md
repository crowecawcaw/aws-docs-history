# Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances

To activate the GRID Virtual Applications on GPU-based instances that have NVIDIA GPUs (NVIDIA GRID Virtual
Workstation is enabled by default), you must define the product type for the driver. The process that
you use depends on the operating system of your instance.

###### To activate GRID Virtual Applications on your Linux instances

1. Create the `/etc/nvidia/gridd.conf` file from the provided
   template file.

```
`[ec2-user ~]$` sudo cp /etc/nvidia/gridd.conf.template /etc/nvidia/gridd.conf
```

2. Open the `/etc/nvidia/gridd.conf` file in your favorite
   text editor.
3. Find the `FeatureType` line, and set it equal to `0`.
   Then add a line with `IgnoreSP=TRUE`.

```
FeatureType=0 IgnoreSP=TRUE
```

4. Save the file and exit.
5. Reboot the instance to pick up the new configuration.

```
`[ec2-user ~]$` sudo reboot
```

###### To activate GRID Virtual Applications on your Windows instances

1. Run **regedit.exe** to open the registry editor.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\NVIDIA
Corporation\Global\GridLicensing`.
3. Open the context (right-click) menu on the right pane and choose
   **New**, **DWORD**.
4. For **Name**, enter **FeatureType** and type
   `Enter`.
5. Open the context (right-click) menu on **FeatureType** and
   choose **Modify**.
6. For **Value data**, enter `0` for NVIDIA GRID
   Virtual Applications and choose **OK**.
7. Open the context (right-click) menu on the right pane and choose
   **New**, **DWORD**.
8. For **Name**, enter **IgnoreSP** and type
   `Enter`.
9. Open the context (right-click) menu on **IgnoreSP** and
   choose **Modify**.
10. For **Value data**, type `1` and choose
    **OK**.
11. Close the registry editor.

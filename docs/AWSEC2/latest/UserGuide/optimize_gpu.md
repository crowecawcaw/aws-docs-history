# Optimize GPU settings on Amazon EC2 instances

There are several GPU setting optimizations that you can perform to achieve the best
performance on NVIDIA GPU instances. With some of
these instance types, the NVIDIA driver uses an autoboost feature, which varies the GPU
clock speeds. By disabling autoboost and setting the GPU clock speeds to their maximum
frequency, you can consistently achieve the maximum performance with your GPU instances.

1. Configure the GPU settings to be persistent. This command can take several
   minutes to run.

```
`[ec2-user ~]$` sudo nvidia-persistenced
```

2. [G3, and P2 instances only] Disable the autoboost feature for all GPUs on
   the instance.

```
`[ec2-user ~]$` sudo nvidia-smi --auto-boost-default=0
```

3. Set all GPU clock speeds to their maximum frequency. Use the memory and
   graphics clock speeds specified in the following commands.

Some versions of the NVIDIA driver do not support setting the application
clock speed, and display the error `"Setting applications clocks is not
 supported for GPU..."`, which you can ignore.

    * G3 instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `2505,1177`
    ```
    * G4dn instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `5001,1590`
    ```
    * G5 instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `6250,1710`
    ```
    * G6, G6f, Gr6, and Gr6f instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `6251,2040`
    ```
    * G6e instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `9001,2520`
    ```
    * G7e instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `12481,2430`
    ```
    * P2 instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `2505,875`
    ```
    * P3 and P3dn instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `877,1530`
    ```
    * P4d instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `1215,1410`
    ```
    * P4de instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `1593,1410`
    ```
    * P5 instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `2619,1980`
    ```
    * P5e and P5en instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `3201,1980`
    ```
    * P6-B200 instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `3996,1965`
    ```
    * P6-B300 instances:



    ```
    `[ec2-user ~]$` sudo nvidia-smi -ac `3996,2032`
    ```

1. Open a PowerShell window and navigate to the NVIDIA installation
   folder.

```
`PS C:\>` cd "C:\Windows\System32\DriverStore\FileRepository\nvgridsw_aws.inf_*\"
```

2. [G3, and P2 instances only] Disable the autoboost feature for all GPUs on
   the instance.

```
`PS C:\>` .\nvidia-smi --auto-boost-default=0
```

3. Set all GPU clock speeds to their maximum frequency. Use the memory and
   graphics clock speeds specified in the following commands.

Some versions of the NVIDIA driver do not support setting the application
clock speed, and display the error `"Setting applications clocks is not
 supported for GPU..."`, which you can ignore.

    * G3 instances:



    ```
    `PS C:\>` .\nvidia-smi -ac "`2505,1177`"
    ```
    * G4dn instances:



    ```
    `PS C:\>` .\nvidia-smi -ac "`5001,1590`"
    ```
    * G5 instances:



    ```
    `PS C:\>` .\nvidia-smi -ac "`6250,1710`"
    ```
    * G6, G6f, Gr6, and Gr6f instances:



    ```
    `PS C:\>` .\nvidia-smi -ac "`6251,2040`"
    ```
    * G6e instances:



    ```
    `PS C:\>` .\nvidia-smi -ac "`9001,2520`"
    ```
    * P2 instances:



    ```
    `PS C:\>` .\nvidia-smi -ac "`2505,875`"
    ```
    * P3 and P3dn instances:



    ```
    `PS C:\>` .\nvidia-smi -ac "`877,1530`"
    ```

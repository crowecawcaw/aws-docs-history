# Lustre file system and client kernel compatibility

We highly recommend using the Lustre version for your FSx for Lustre file system that is compatible
with the Linux kernel versions of your client instances.

| Operating system  | OS version | Minimum kernel version | Maximum kernel version | Lustre client version | Lustre file system version |
| ----------------- | ---------- | ---------------------- | ---------------------- | --------------------- | -------------------------- | -------- | -------- |
|                   |            |                        |                        |                       | **2.10**                   | **2.12** | **2.15** |
| Amazon Linux 2023 | 6.12       | \*                     | \*                     | 2.15                  | no                         | yes      | yes      |
|                   | 6.1        | 6.1.79-99.167          | 6.1.79-99.167+         | 2.15                  | no                         | yes      | yes      |
| Amazon Linux 2    | 5.10       | 5.10.144-127.601       | 5.10.144-127.601+      | 2.12                  | yes                        | yes      | yes      |
|                   |            |                        | <5.10.144-127.601      | 2.10                  | yes                        | yes      | no       |
|                   | 5.4        | 5.4.214-120.368        | 5.4.214-120.368+       | 2.12                  | yes                        | yes      | yes      |
|                   |            |                        | <5.4.214-120.368       | 2.10                  | yes                        | yes      | no       |
|                   | 4.14       | 4.14.294-220.533       | 4.14.294-220.533+      | 2.12                  | yes                        | yes      | yes      |
|                   |            |                        | <4.14.294-220.533      | 2.10                  | yes                        | yes      | no       |

| Operating system | OS version | Minimum kernel version | Maximum kernel version | Lustre client version | Lustre file system version |
| ---------------- | ---------- | ---------------------- | ---------------------- | --------------------- | -------------------------- | -------- | -------- |
|                  |            |                        |                        |                       | **2.10**                   | **2.12** | **2.15** |
| Ubuntu           | 24         | 6.14.0-1012            | 6.14.0\*               | 2.15                  | no                         | yes      | yes      |
|                  |            | 6.8.0-1024             | 6.8.0\*                | 2.15                  | no                         | yes      | yes      |
|                  | 22         | 6.8.0-1017             | 6.8.0\*                | 2.15                  | no                         | yes      | yes      |
|                  |            | 6.5.0-1023             | 6.5.0\*                | 2.15                  | no                         | yes      | yes      |
|                  |            | 6.2.0-1017             | 6.2.0\*                | 2.15                  | no                         | yes      | yes      |
|                  |            | 5.15.0-1015-aws        | 5.15.0-1051-aws        | 2.12                  | yes                        | yes      | yes      |
|                  | 20         | 5.15.0-1015-aws        | 5.15.0\*               | 2.12                  | yes                        | yes      | yes      |
|                  |            | 5.4.0-1011-aws         | 5.13.0-1031-aws        | 2.10                  | yes                        | yes      | no       |

| Operating system        | OS version | Architecture | Minimum kernel version | Maximum kernel version | Lustre client version | Lustre file system version |
| ----------------------- | ---------- | ------------ | ---------------------- | ---------------------- | --------------------- | -------------------------- | -------- | -------- |
|                         |            |              |                        |                        |                       | **2.10**                   | **2.12** | **2.15** |
| RHEL/Rocky Linux        | 9.6        | Arm + x86    | 5.14.0-570.12.1        | 5.14.0-570\*           | 2.15                  | no                         | yes      | yes      |
|                         | 9.5        | Arm + x86    | 5.14.0-503.19.1        | 5.14.0-503\*           | 2.15                  | no                         | yes      | yes      |
|                         | 9.4        | Arm + x86    | 5.14.0-427.13.1        | 5.14.0-427\*           | 2.15                  | no                         | yes      | yes      |
|                         | 9.3        | Arm + x86    | 5.14.0-362.18.1        | 5.14.0-362.18.1        | 2.15                  | no                         | yes      | yes      |
|                         | 9.0        | Arm + x86    | 5.14.0-70.13.1         | 5.14.0-70.30.1         | 2.15                  | no                         | yes      | yes      |
| RHEL/CentOS/Rocky Linux | 8.10       | Arm + x86    | 4.18.0-553             | 4.18.0-553\*           | 2.12                  | yes                        | yes      | yes      |
|                         | 8.9        | Arm + x86    | 4.18.0-513\*           | 4.18.0-513\*           | 2.12                  | yes                        | yes      | yes      |
|                         | 8.8        | Arm + x86    | 4.18.0-477\*           | 4.18.0-477\*           | 2.12                  | yes                        | yes      | yes      |
|                         | 8.7        | Arm + x86    | 4.18.0-425\*           | 4.18.0-425\*           | 2.12                  | yes                        | yes      | yes      |
|                         | 8.6        | Arm + x86    | 4.18.0-372\*           | 4.18.0-372\*           | 2.12                  | yes                        | yes      | yes      |
|                         | 8.5        | Arm + x86    | 4.18.0-348\*           | 4.18.0-348\*           | 2.12                  | yes                        | yes      | yes      |
|                         | 8.4        | Arm + x86    | 4.18.0-305\*           | 4.18.0-305\*           | 2.12                  | yes                        | yes      | yes      |
| RHEL/CentOS             | 8.3        | Arm + x86    | 4.18.0-240\*           | 4.18.0-240\*           | 2.10                  | yes                        | yes      | no       |
|                         | 8.2        | Arm + x86    | 4.18.0-193\*           | 4.18.0-193\*           | 2.10                  | yes                        | yes      | no       |
|                         | 7.9        | x86          | 3.10.0-1160\*          | 3.10.0-1160\*          | 2.12                  | yes                        | yes      | yes      |
|                         | 7.8        | x86          | 3.10.0-1127\*          | 3.10.0-1127\*          | 2.10                  | yes                        | yes      | no       |
|                         | 7.7        | x86          | 3.10.0-1062\*          | 3.10.0-1062\*          | 2.10                  | yes                        | yes      | no       |
| CentOS                  | 7.9        | Arm          | 4.18.0-193\*           | 4.18.0-193\*           | 2.12                  | yes                        | yes      | yes      |
|                         | 7.8        | Arm          | 4.18.0-147\*           | 4.18.0-147\*           | 2.12                  | yes                        | yes      | yes      |

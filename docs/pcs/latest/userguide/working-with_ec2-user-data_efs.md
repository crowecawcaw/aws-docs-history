# Example: Use an EFS file system as a shared home directory for AWS PCS

Provide this script as the value of `"userData"` in your launch template. For
more information, see [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md "working-with_ec2-user-data.md").

This example extends the example EFS mount in [Using network file systems with AWS PCS](working-with_file-systems.md "working-with_file-systems.md") to implement a shared home directory. The
contents of /home are backed up before the EFS file system is mounted. The contents are then
quickly copied into place on the shared storage after the mount completes.

Replace the following values in this script with your own details:

- `/mount-point-directory` – The path on an instance
  where you want to mount the EFS file system.
- `filesystem-id` – The file system ID for the EFS
  file system.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

packages:
  - amazon-efs-utils

runcmd:
  - mkdir -p /tmp/home
  - rsync -a /home/ /tmp/home
  - echo "`filesystem-id`:/ `/mount-point-directory` efs tls,_netdev" >> /etc/fstab
  - mount -a -t efs defaults
  - rsync -a --ignore-existing /tmp/home/ /home
  - rm -rf /tmp/home/

--==MYBOUNDARY==--
```

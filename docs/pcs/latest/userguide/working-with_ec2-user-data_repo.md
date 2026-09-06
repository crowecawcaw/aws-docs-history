

# Example: Install software for AWS PCS from a package repository
<a name="working-with_ec2-user-data_repo"></a>

 Provide this script as the value of `"userData"` in your launch template. For more information, see [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md). 

This script uses **cloud-config** to install software packages on node group instances at launch. For more information, see the [User data formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html) in the *cloud-init documentation*. This example installs `curl` and `llvm`.

**Note**  
Your instances must be able to connect to their configured package repositories.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

packages:
- python3-devel
- rust
- golang

--==MYBOUNDARY==--
```
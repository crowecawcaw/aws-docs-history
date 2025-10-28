# Known issues for Amazon EC2 instances running Amazon Linux 2 with AWS CloudHSM

The following issues impact AWS CloudHSM and Amazon EC2 instances that are running on Amazon Linux 2.

## Issue: Amazon Linux 2 version 2018.07 uses an updated `ncurses`

package (version 6) that is currently incompatible with the AWS CloudHSM SDKs

You see the following
error returned upon running the AWS CloudHSM [cloudhsm_mgmt_util](cloudhsm_mgmt_util.md "cloudhsm_mgmt_util.md") or [key_mgmt_util](key_mgmt_util.md "key_mgmt_util.md"):

```
/opt/cloudhsm/bin/cloudhsm_mgmt_util: `error while loading shared libraries: libncurses.so.5: cannot open shared object file: No such file or directory`
```

- **Impact:** Instances running on Amazon Linux 2 version 2018.07 will
  be unable to use _all_ AWS CloudHSM utilities.
- **Workaround:** Issue the following command on your Amazon Linux 2
  EC2 instances to install the supported `ncurses` package (version
  5):

```
sudo yum update && yum install ncurses-compat-libs
```

- **Resolution status:** This issue has been resolved in the
  AWS CloudHSM client 1.1.2 release. You
  must upgrade to this client to benefit from the fix.

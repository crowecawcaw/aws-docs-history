# Example: Set global environment variables for AWS PCS

Provide this script as the value of `"userData"` in your launch template. For more information, see [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md "working-with_ec2-user-data.md").

The following example uses `/etc/profile.d` to set global variables on node group instances.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/x-shellscript; charset="us-ascii"

#!/bin/bash
touch /etc/profile.d/awspcs-userdata-vars.sh
echo MY_GLOBAL_VAR1=100 >> /etc/profile.d/awspcs-userdata-vars.sh
echo MY_GLOBAL_VAR2=abc >> /etc/profile.d/awspcs-userdata-vars.sh

--==MYBOUNDARY==--
```

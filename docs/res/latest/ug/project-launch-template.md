

# Add a launch template
<a name="project-launch-template"></a>

When creating or editing a project, you can add launch templates using the **Advanced Options** within the project configuration. Launch templates provide additional configurations, such as security groups, IAM policies, and launch scripts to all VDI instances within the project. 

## Add policies
<a name="add-policies"></a>

You can add an IAM policy to control VDI access for all instances deployed under your project. To onboard a policy, tag the policy with the following key-value pair:

```
res:Resource/vdi-host-policy
```

For more information on IAM roles, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Add security groups
<a name="add-security-groups"></a>

You can add a security group to control the egress and ingress data for all VDI instances under your project. To onboard a security group, tag the security group with the following key-value pair:

```
res:Resource/vdi-security-group
```

For more information on security groups, see [Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the *Amazon VPC User Guide*.

### Add launch scripts
<a name="project-launch-scripts"></a>

You can add launch scripts that will initiate on all VDI sessions within your project. RES supports script initiation for Linux and Windows. For script initiation, you can choose either:

**Run Script When VDI Starts**  
This option initiates the script at the beginning of a VDI instance before any RES configurations or installations run.

**Run Script when VDI is Configured**  
This option initiates the script after RES configurations complete.

Scripts support the following options:


| Script configuration | Example | 
| --- | --- | 
| S3 URI | s3://bucketname/script.sh | 
| HTTPS URL | https://sample.samplecontent.com/sample | 
| Local file | file:///user/scripts/example.sh | 

All custom scripts that are hosted on a S3 buckets need to be provisioned with the following tag:

```
res:EnvironmentName/{{<res-environment>}}
```

For **Arguments**, provide any arguments separated by a comma.

![Example of a project configuration](http://docs.aws.amazon.com/res/latest/ug/images/res-projectconfigexample.png)


Example templates for launch scripts.

------
#### [ Linux ]

```
#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
#  with the License. A copy of the License is located at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions
#  and limitations under the License.

#!/bin/bash

echo "start_script.sh running" >> /test_scripts
echo "All arguments: $@" >> /test_scripts
echo "Argument count: $#" >> /test_scripts
echo "Argument 1, $1" >> /test_scripts
echo "Argument 2, $2" >> /test_scripts
echo "end of start_script.sh" >> /test_scripts
```

------
#### [ Windows ]

```
#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
#  with the License. A copy of the License is located at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions
#  and limitations under the License.

#!pwsh

Write-Output "configure_script.ps1 running" | Out-File -Append -FilePath "/test_scripts"
Write-Output "All arguments: $args" | Out-File -Append -FilePath "/test_scripts"
Write-Output "Argument count: $($args.Count)" | Out-File -Append -FilePath "/test_scripts"
Write-Output "Argument 1, $($args[0])" | Out-File -Append -FilePath "/test_scripts"
Write-Output "Argument 2, $($args[1])" | Out-File -Append -FilePath "/test_scripts"
Write-Output "end of configure_script.ps1" | Out-File -Append -FilePath "/test_scripts"
```

------
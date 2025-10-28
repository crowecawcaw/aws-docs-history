# Known Issues

- [Known Issues 2024.x](#res-troubleshooting-known-issues-2024x "#res-troubleshooting-known-issues-2024x")
  - [(2024.12 and 2024.12.01)
    Regex failure when registering a new Cognito user](#res-troubleshooting-known-issues-2024x-regex-failure-cognito "#res-troubleshooting-known-issues-2024x-regex-failure-cognito")
  - [(2024.12.01 and earlier)
    Invalid bad cert error when connecting to VDI using a custom domain](#res-troubleshooting-known-issues-2024x-invalid-bad-cert "#res-troubleshooting-known-issues-2024x-invalid-bad-cert")
  - [(2024.12 and 2024.12.01)
    Active Directory users cannot SSH to Bastion Host](#res-troubleshooting-known-issues-2024x-ad-users-cannot-ssh "#res-troubleshooting-known-issues-2024x-ad-users-cannot-ssh")
  - [(2024.10) VDI
    auto stop broken for RES environments deployed in isolated VPCs](#res-troubleshooting-known-issues-2024x-vdi-auto-stop-broken "#res-troubleshooting-known-issues-2024x-vdi-auto-stop-broken")
  - [(2024.10 and earlier) Failure to launch
    VDI for Graphic enhanced instance types](#res-troubleshooting-known-issues-2024x-fail-to-launch-vdi "#res-troubleshooting-known-issues-2024x-fail-to-launch-vdi")
  - [(2024.08) Preparing
    Infrastructure AMI Failure](#res-troubleshooting-known-issues-2024x-prep-infra-ami-fail "#res-troubleshooting-known-issues-2024x-prep-infra-ami-fail")
  - [(2024.08)
    Virtual desktops fail to mount read/write Amazon S3 bucket with root bucket ARN and custom
    prefixing](#res-troubleshooting-known-issues-2024x-vdi-fails-to-mount-s3 "#res-troubleshooting-known-issues-2024x-vdi-fails-to-mount-s3")
  - [(2024.06) Apply
    snapshot fails when the AD group name contains spaces](#res-troubleshooting-known-issues-2024x-apply-snapshot-fails "#res-troubleshooting-known-issues-2024x-apply-snapshot-fails")
  - [(2024.06 and earlier)
    Group members not synced to RES during AD sync](#res-troubleshooting-known-issues-2024x-group-not-synced "#res-troubleshooting-known-issues-2024x-group-not-synced")
  - [(2024.06 and earlier)
    CVE-2024-6387, RegreSSHion, Security Vulnerability in RHEL9 and Ubuntu VDIs](#res-troubleshooting-known-issues-2024x-regresshion "#res-troubleshooting-known-issues-2024x-regresshion")
  - [(2024.04-2024.04.02)
    Provided IAM Permission Boundary not attached to the VDI instances' role](#res-troubleshooting-known-issues-2024x-iam-boundary "#res-troubleshooting-known-issues-2024x-iam-boundary")
  - [(2024.04.02 and earlier)
    Windows NVIDIA instances in ap-southeast-2 (Sydney) fail to launch](#res-troubleshooting-known-issues-2024x-nvidia-instances "#res-troubleshooting-known-issues-2024x-nvidia-instances")
  - [(2024.04 and 2024.04.01)
    RES delete failure in GovCloud](#res-troubleshooting-known-issues-2024x-delete-fail "#res-troubleshooting-known-issues-2024x-delete-fail")
  - [(2024.04 - 2024.04.02)
    Linux virtual desktop may be stuck in the "RESUMING" status on reboot](#res-troubleshooting-known-issues-2024x-linux-stuck-resuming "#res-troubleshooting-known-issues-2024x-linux-stuck-resuming")
  - [(2024.04.02 and earlier)
    Fails to sync AD users whose SAMAccountName attribute includes capital letters or special
    characters](#res-troubleshooting-known-issues-2024x-samaccountname "#res-troubleshooting-known-issues-2024x-samaccountname")
  - [(2024.04.02 and earlier)
    Private key for accessing the bastion host is invalid](#res-troubleshooting-known-issues-2024x-private-key "#res-troubleshooting-known-issues-2024x-private-key")

## Known Issues 2024.x

........................

### (2024.12 and 2024.12.01)

Regex failure when registering a new Cognito user

**Bug description**

If you attempt to register AWS Cognito users through the web portal who have email prefixes
that contain ".", such as `<firstname>.<lastname>@<company>.com`,
this will result in an error stating that the Cognito username does not match the defined
regex pattern.

![Invalid parameters error](images/res-invalid-parameters-regex.png)

This error is caused by RES auto-generating usernames from the user's email prefix. However,
usernames with "." are not valid users for VDIs in certain Linux distributions supported by RES.
This fix removes any "." in the email prefix when generating a username so that the username will
be valid on RES Linux VDIs.

**Affected versions**

RES versions 2024.12 and 2024.12.01

**Mitigation**

1. Run the following commands to download `patch.py` and
   `cognito_sign_up_email_fix.patch` for version 2024.12 or
   `cognito_sign_up_email_fix.patch` for version 2024.12.01,
   replacing `<output-directory>` with the directory where you
   want to download the patch script and patch file, and
   `<environment-name>` with the name of your RES environment:
   1. The patch applies to RES 2024.12 and 2024.12.01.
   2. The patch script requires [AWS CLI v2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"), Python 3.9.16 or above, and [Boto3](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/").
   3. Configure the AWS CLI for the account and region where RES is deployed,
      and make sure that you have S3 permissions to write to the bucket created by
      RES.

```
OUTPUT_DIRECTORY=<output-directory>
ENVIRONMENT_NAME=<environment-name>
RES_VERSION=<res-version> # either 2024.12 or 2024.12.01

mkdir -p ${OUTPUT_DIRECTORY}
curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/${RES_VERSION}/patch_scripts/patch.py --output ${OUTPUT_DIRECTORY}/patch.py
curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/${RES_VERSION}/patch_scripts/patches/cognito_sign_up_email_fix.patch --output ${OUTPUT_DIRECTORY}/cognito_sign_up_email_fix.patch
```

2. Navigate to the directory where the patch script and patch file were downloaded.
   Run the following patch command:

```
python3 ${OUTPUT_DIRECTORY}/patch.py --environment-name ${ENVIRONMENT_NAME} --res-version ${RES_VERSION} --module cluster-manager --patch ${OUTPUT_DIRECTORY}/cognito_sign_up_email_fix.patch

```

3. Restart the Cluster Manager instance for your environment. You may also terminate
   the instance from the Amazon EC2 Management Console.

```
INSTANCE_ID=$(aws ec2 describe-instances \
    --filters \
    Name=tag:Name,Values=${ENVIRONMENT_NAME}-cluster-manager \
    Name=tag:res:EnvironmentName,Values=${ENVIRONMENT_NAME}\
    --query "Reservations[0].Instances[0].InstanceId" \
    --output text)

aws ec2 terminate-instances --instance-ids ${INSTANCE_ID}
```

4. Verify the Cluster Manager instance status by checking the activity of the auto
   scaling group starting with the name `<RES-EnvironmentName>-cluster-manager-asg`.
   Wait until the new instance is launched successfully.

........................

### (2024.12.01 and earlier)

Invalid bad cert error when connecting to VDI using a custom domain

**Bug description**

When you deploy the [External Resources recipe](create-external-resources.md "create-external-resources.md")
and RES with a custom portal domain name, CertificateRenewalNode fails to refresh the TLS
certificate for VDI connection with the following error in `/var/log/user-data.log`:

```
{
  "type": "urn:ietf:params:acme:error:unauthorized",
  "detail": "Error finalizing order :: OCSP must-staple extension is no longer available: see https://letsencrypt.org/2024/12/05/ending-ocsp",
  "status": 403
}
```

As a result, you will encounter an error that states `net::ERR_CERT_DATE_INVALID`
(Chrome) or `Error code: SSL_ERROR_BAD_CERT_DOMAIN` (FireFox) when you connect to your
VDIs in the RES web portal.

**Affected versions**

2024.12.01 and earlier

**Mitigation**

1. Navigate to the EC2 console. If there is an instance named `CertificateRenewalNode-`,
   terminate the instance.
2. Navigate to the Lambda console. Open the source code of the Lambda function named
   `-CertificateRenewalLambda-`. Identify the line staring with
   `./acme.sh --issue --dns dns_aws --ocsp-must-staple --keylength 4096`
   and remove the `--ocsp-must-staple` argument.
3. Select **Deploy** and wait for the code change to take effect.
4. To manually trigger the Lambda function: go to the **Test** tab and
   then select **Test**. No additional input is required. This should create
   a certificate EC2 instance that updates the Certificate and PrivateKey secrets in Secret
   Manager. The instance will be terminated automatically once the secrets are updated.
5. Terminate the existing dcv-gateway instance: `<env-name>-vdc-gateway`
   and wait for the auto scaling group to automatically deploy a new one.

**Error details**

Let's Encrypt is ending OCSP Support in 2025. Starting from January 30, 2025, OCSP Must-Staple
requests will fail unless the requesting account has previously issued a certificate that contains
the OCSP Must Staple extension. Check [https://letsencrypt.org/2024/12/05/ending-ocsp/](https://letsencrypt.org/2024/12/05/ending-ocsp/ "https://letsencrypt.org/2024/12/05/ending-ocsp/") for more details.

........................

### (2024.12 and 2024.12.01)

Active Directory users cannot SSH to Bastion Host

**Bug description**

Active Directory users receive a permission denied error when they connect to the Bastion Host
following the instructions from the RES web portal.

The Python application that runs on the Bastion Host fails to launch the SSSD service due to a
missing environment variable. As a result, AD users are unknown to the operating system and cannot
log in.

**Affected versions**

2024.12 and 2024.12.01

**Mitigation**

1. Connect to the Bastion Host instance from the EC2 console.
2. Edit `/etc/environment` and add
   `environment_name=<res-environment-name>` as a new line under
   IDEA_CLUSTER_NAME.
3. Run the following commands on the instance:

```
source /etc/environment
sudo service supervisord restart
sudo systemctl restart supervisord
```

4. Try to connect to the Bastion Host again following the instructions from the
   RES web portal.

........................

### (2024.10) VDI

auto stop broken for RES environments deployed in isolated VPCs

**Bug description**

With the 2024.10 RES release, VDI auto stop was added for VDIs that are at idle for a certain
period of time. This setting can be configured in Desktop Settings → Server → Session.

VDI auto stop is currently not supported for RES environments deployed in isolated VPCs.

**Affected versions**

2024.10

**Mitigation**

We are currently working on a fix that will be included in a future release. However, it
is still possible to manually stop VDIs in RES environments deployed in isolated VPCs.

........................

### (2024.10 and earlier) Failure to launch

VDI for Graphic enhanced instance types

**Bug description**

When an Amazon Linux 2 - x86_64, RHEL 8 - x86_64, or RHEL 9 x86_64 VDI is launched on a
graphic enhanced instance type (g4, g5), the instance will get stuck in the provisioning
state. This means the instance will never get to the "Ready" state and be available for
connection.

This happens because the X Server does not properly instantiate on the instances. After
you apply this patch we also suggest you increase the root volume size of your software
stacks for graphics instances to 50gb to ensure there is sufficient space for installing
all dependencies.

**Affected versions**

All RES versions 2024.10 or earlier.

**Mitigation**

1. Download [patch.py](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.10/patch_scripts/patch.py "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.10/patch_scripts/patch.py") and [graphic_enhanced_instance_types_fix.patch](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.10/patch_scripts/patches/graphic_enhanced_instance_types_fix.patch "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.10/patch_scripts/patches/graphic_enhanced_instance_types_fix.patch") by replacing
   `<output-directory>` with the directory where you want to download
   the patch script and patch file and `<environment-name>` with the
   name of your RES environment in the command below:
   1. The patch only applies to RES 2024.10.
   2. The patch script requires AWS CLI v2, Python 3.9.16 or above, and
      Boto3.
   3. Configure the AWS CLI for the account and region where RES is deployed,
      and make sure that you have S3 permissions to write to the bucket created by
      RES.

```
OUTPUT_DIRECTORY=<output-directory>
ENVIRONMENT_NAME=<environment-name>

mkdir -p ${OUTPUT_DIRECTORY}
curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.10/patch_scripts/patch.py --output ${OUTPUT_DIRECTORY}/patch.py
curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.10/patch_scripts/patches/graphic_enhanced_instance_types_fix.patch --output ${OUTPUT_DIRECTORY}/graphic_enhanced_instance_types_fix.patch
```

2. Navigate to the directory where the patch script and patch file were downloaded.
   Run the following patch command:

```
python3 ${OUTPUT_DIRECTORY}/patch.py --environment-name ${ENVIRONMENT_NAME} --res-version 2024.10 --module virtual-desktop-controller --patch ${OUTPUT_DIRECTORY}/graphic_enhanced_instance_types_fix.patch
```

3. To terminate the Virtual Desktop Controller (vdc-controller) instance for your environment,
   run the following commands, replacing the name of your RES environment where shown.

```
INSTANCE_ID=$(aws ec2 describe-instances \
    --filters \
    Name=tag:Name,Values=${ENVIRONMENT_NAME}-vdc-controller \
    Name=tag:res:EnvironmentName,Values=${ENVIRONMENT_NAME}\
    --query "Reservations[0].Instances[0].InstanceId" \
    --output text)

aws ec2 terminate-instances --instance-ids ${INSTANCE_ID}
```

4. Launch a new instance after the target group starting with the name
   `<RES-EnvironmentName>-vdc-ext` becomes healthy. We recommend any
   new software stacks you register for graphics instances have at least 50GB storage.

........................

### (2024.08) Preparing

Infrastructure AMI Failure

**Bug description**

When you prepare AMIs using EC2 Image Builder according to the directions listed in the
[Prerequisites Documentation](prerequisites.md#private-vpc "prerequisites.md#private-vpc"), the building process fails
with the following error message:

```
CmdExecution: [ERROR] Command execution has resulted in an error
```

This is due to errors in the dependencies file that is provided in the documentation.

**Affected versions**

2024.08

**Mitigation**

_Create new EC2 Image Builder resources:_

(Follow these steps if you have never prepared AMIs for RES instances)

1. Download the updated [res-installation-scripts.tar.gz](samples/res-installation-scripts.md "samples/res-installation-scripts.md") file.
2. Follow the steps listed under _Prepare Amazon Machine Images (AMIs)_
   on the [Prerequisites](prerequisites.md#private-vpc "prerequisites.md#private-vpc") page.

_Reusing previous EC2 Image Builder resources:_

(Follow these steps if you have prepared AMIs for RES instances)

1. Download the updated [res-installation-scripts.tar.gz](samples/res-installation-scripts.md "samples/res-installation-scripts.md") file.
2. Navigate to EC2 Image Builder → Components → Click on the Component created
   for preparing RES AMIs.
3. Note the S3 location listed under Content → DownloadRESInstallScripts step → inputs →
   source.
4. The S3 location found above contains the dependencies file that was previously
   used, replace this file with the file downloaded in the first step.

........................

### (2024.08)

Virtual desktops fail to mount read/write Amazon S3 bucket with root bucket ARN and custom
prefixing

**Bug description**

Research and Engineering Studio 2024.08 fails to mount read/write S3 buckets on to a virtual desktop infrastructure
(VDI) instance when using a root bucket ARN (that is, `arn:aws:s3:::example-bucket`)
and a custom prefix (project name or project name and user name).

Bucket configurations that are **not affected** by this
issue include:

- read-only buckets
- read/write buckets with a prefix as part of the bucket ARN (that is,
  `arn:aws:s3:::example-bucket/example-folder-prefix`) and custom prefixing
  (project name or project name and user name)
- read/write buckets with a root bucket ARN, but no custom prefixing

After you provision a VDI instance, the specified mount directory for that S3 bucket
will not have the bucket mounted. Although the mount directory on the VDI will be present,
the directory will be empty and will not contain the current contents of the bucket. When
you write a file to the directory using the terminal, the error `Permission denied, 
 unable to write a file` will be thrown and the file contents will not be uploaded
to the corresponding S3 bucket.

**Affected versions**

2024.08

**Mitigation**

1. To download the patch script and patch file (`patch.py`
   and `s3_mount_custom_prefix_fix.patch`), run the following
   command, replacing `<output-directory>` with the directory where
   you want to download the patch script and patch file and `<environment-name>`
   with the name of your RES environment:
   1. The patch only applies to RES 2024.08.
   2. The patch script requires [AWS CLI
      v2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"), Python 3.9.16 or above, and [Boto3](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/").
   3. Configure the AWS CLI for the account and region where RES is
      deployed, and make sure that you have Amazon S3 permissions to write to
      the bucket created by RES.

```
OUTPUT_DIRECTORY=<output-directory>
ENVIRONMENT_NAME=<environment-name>

mkdir -p ${OUTPUT_DIRECTORY}
curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.08/patch_scripts/patch.py --output ${OUTPUT_DIRECTORY}/patch.py
curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.08/patch_scripts/patches/s3_mount_custom_prefix_fix.patch --output ${OUTPUT_DIRECTORY}/s3_mount_custom_prefix_fix.patch
```

2. Navigate to the directory where the patch script and patch file are downloaded.
   Run the following patch command:

```
python3 ${OUTPUT_DIRECTORY}/patch.py --environment-name ${ENVIRONMENT_NAME} --res-version 2024.08 --module virtual-desktop-controller --patch ${OUTPUT_DIRECTORY}/s3_mount_custom_prefix_fix.patch

```

3. To terminate the Virtual Desktop Controller (vdc-controller) instance for your
   environment, run the following commands. (You already set the `ENVIRONMENT_NAME`
   variable to the name of your RES environment in the first step.)

```
INSTANCE_ID=$(aws ec2 describe-instances \
    --filters \
    Name=tag:Name,Values=${ENVIRONMENT_NAME}-vdc-controller \
    Name=tag:res:EnvironmentName,Values=${ENVIRONMENT_NAME}\
    --query "Reservations[0].Instances[0].InstanceId" \
    --output text)

aws ec2 terminate-instances --instance-ids ${INSTANCE_ID}
```

###### Note

For private VPC setups, if you haven't already done so, for the
`<RES-EnvironmentName>-vdc-custom-credential-broker-lambda`
function make sure to add the `Environment variable` with name
`AWS_STS_REGIONAL_ENDPOINTS` and value of `regional`.
See [Amazon S3 bucket prerequisites for isolated VPC deployments](S3-buckets-prereqs.md "S3-buckets-prereqs.md")
for more information. 4. After the target group starting with the name
``<RES-EnvironmentName>`-vdc-ext` becomes
healthy, new VDIs will need to be launched that will have the read/write S3 buckets
with root bucket ARN and custom prefixing mounted correctly.

........................

### (2024.06) Apply

snapshot fails when the AD group name contains spaces

**Issue**

RES 2024.06 fails to apply snapshots from prior versions if the AD groups contain spaces
in their names.

The cluster-manager CloudWatch logs (under the `/<environment-name>/cluster-manager`
log group) will include the following error during AD sync:

```
[apply-snapshot] authz.role-assignments/<Group name with spaces>:group#<projectID>:project FAILED_APPLY because: [INVALID_PARAMS] Actor key doesn't match the regex pattern ^[a-zA-Z0-9_.][a-zA-Z0-9_.-]{1,20}:(user|group)$
```

The error results from RES only accepting group names that meet the following requirements:

- It can only contain lowercase and uppercase ASCII letters, digits, dash(-),
  period (.), and underscore (\_)
- A dash (-) is not allowed as the first character
- It cannot contain spaces.

**Affected versions**

2024.06

**Mitigation**

1. To download the patch script and patch file
   ([patch.py](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patch.py "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patch.py") and
   [groupname_regex.patch](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patches/groupname_regex.patch "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patches/groupname_regex.patch")), run the following command, replacing
   `<output-directory>` with the directory where you want to put
   the files, and `<environment-name>` with the name of your RES
   environment:
   1. The patch only applies to RES 2024.06
   2. The patch script requires
      [AWS CLI v2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"), Python 3.9.16 or above, and
      [Boto3](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/").
   3. Configure the AWS CLI for the account and region where RES is deployed,
      and make sure that you have S3 permissions to write to the bucket created
      by RES:

   ```
   OUTPUT_DIRECTORY=`<output-directory>`
   ENVIRONMENT_NAME=`<environment-name>`

   mkdir -p ${OUTPUT_DIRECTORY}
   curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patch.py --output ${OUTPUT_DIRECTORY}/patch.py
   curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patches/groupname_regex.patch --output ${OUTPUT_DIRECTORY}/groupname_regex.patch
   ```

2. Navigate to the directory where the patch script and patch file are downloaded.
   Run the following patch command:

```
python3 patch.py --environment-name ${ENVIRONMENT_NAME} --res-version 2024.06 --module cluster-manager --patch ${OUTPUT_DIRECTORY}/groupname_regex.patch
```

3. To restart the Cluster Manager instance for your environment, run the following
   commands: You may also terminate the instance from the Amazon EC2 Management Console.

```
INSTANCE_ID=$(aws ec2 describe-instances \
    --filters \
    Name=tag:Name,Values=${ENVIRONMENT_NAME}-cluster-manager \
    Name=tag:res:EnvironmentName,Values=${ENVIRONMENT_NAME}\
    --query "Reservations[0].Instances[0].InstanceId" \
    --output text)

aws ec2 terminate-instances --instance-ids ${INSTANCE_ID}
```

###### Note

The patch allows AD group names to contain lower case and uppercase ASCII letters,
digits, dash(-), period (.), underscore (\_), and spaces with a total length between 1 and
30, inclusive.

........................

### (2024.06 and earlier)

Group members not synced to RES during AD sync

**Bug description**

Group members will not properly sync to RES if the GroupOU differs from the UserOU.

RES creates an ldapsearch filter when attempting to sync users from an AD group. The current
filter incorrectly utilizes the UserOU parameter instead of the GroupOU parameter. The result
is that the search fails to return any users. This behavior only occurs in instances where
the UsersOU and GroupOU differ.

**Affected versions**

All RES versions 2024.06 or earlier

**Mitigation**

Follow these steps to resolve the issue:

1. To download the patch.py script and group_member_sync_bug_fix.patch file, run
   the following commands, replacing `<output-directory>` with the
   local directory where you'd like to download the files, and `<res_version>`
   with the version of RES you want to patch:

###### Note

    * The patch script requires [AWS CLI v2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"),
     Python 3.9.16 or above, and [Boto3](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/").
    * Configure the AWS CLI for the account and region where RES is deployed,
     and make sure that you have S3 permissions to write to the bucket created by
     RES.
    * The patch only supports RES versions 2024.04.02 and 2024.06. If you are
     using 2024.04 or 2024.04.01, you can follow the steps listed in
     [Minor version updates](update-the-product.md#minor-version-updates "update-the-product.md#minor-version-updates")
     to first update your environment to 2024.04.02 prior to applying the patch.




    	+ RES Version: RES 2024.04.02


    	Patch download link:
    	 [2024.04.02\_group\_member\_sync\_bug\_fix.patch](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patches/2024.04.02_group_member_sync_bug_fix.patch "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patches/2024.04.02_group_member_sync_bug_fix.patch")
    	+ RES Version: RES 2024.06


    	Patch download link:
    	 [2024.06\_group\_member\_sync\_bug\_fix.patch](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patches/2024.06_group_member_sync_bug_fix.patch "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patches/2024.06_group_member_sync_bug_fix.patch")

```
OUTPUT_DIRECTORY=`<output-directory>`
RES_VERSION=`<res_version>`
mkdir -p ${OUTPUT_DIRECTORY}

curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/${RES_VERSION}/patch_scripts/patch.py --output ${OUTPUT_DIRECTORY}/patch.py

curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/${RES_VERSION}/patch_scripts/patches/${RES_VERSION}_group_member_sync_bug_fix.patch --output ${OUTPUT_DIRECTORY}/${RES_VERSION}_group_member_sync_bug_fix.patch
```

2. Navigate to the directory where the patch script and patch file are downloaded.
   Run the following patch command, replacing `<environment-name>`
   with the name of your RES environment:

```
cd ${OUTPUT_DIRECTORY}
ENVIRONMENT_NAME=`<environment-name>`

python3 patch.py --environment-name ${ENVIRONMENT_NAME} --res-version ${RES_VERSION} --module cluster-manager --patch $PWD/${RES_VERSION}_group_member_sync_bug_fix.patch
```

3. To restart the cluster-manager instance for your environment, run the following
   commands:

```
INSTANCE_ID=$(aws ec2 describe-instances \
    --filters \
    Name=tag:Name,Values=${ENVIRONMENT_NAME}-cluster-manager \
    Name=tag:res:EnvironmentName,Values=${ENVIRONMENT_NAME}\
    --query "Reservations[0].Instances[0].InstanceId" \
    --output text)

aws ec2 terminate-instances --instance-ids ${INSTANCE_ID}
```

........................

### (2024.06 and earlier)

CVE-2024-6387, RegreSSHion, Security Vulnerability in RHEL9 and Ubuntu VDIs

**Bug description**

[CVE-2024-6387](https://nvd.nist.gov/vuln/detail/CVE-2024-6387 "https://nvd.nist.gov/vuln/detail/CVE-2024-6387"), dubbed
regreSSHion, has been identified in the OpenSSH server. This vulnerability enables remote,
unauthenticated attackers to execute arbitrary code on the target server, presenting a
severe risk to systems that utilize OpenSSH for secure communications.

For RES, the standard configuration is to go through the bastion host to SSH into virtual
desktops, and the bastion host is unaffected by this vulnerability. However, the default AMI
(Amazon Machine Image) we provide for RHEL9 and Ubuntu2024 VDIs (Virtual Desktop Infrastructure)
in **ALL** RES versions utilizes an OpenSSH version which is
vulnerable to the security threat.

This means that existing RHEL9 and Ubuntu2024 VDIs could be exploitable, but the attacker
would require access to the bastion host.

More details about the issue can found
[here](https://vulcan.io/blog/cve-2024-6387-how-to-fix-regresshion-vulnerability/ "https://vulcan.io/blog/cve-2024-6387-how-to-fix-regresshion-vulnerability/").

**Affected versions**

All RES versions 2024.06 or earlier.

**Mitigation**

Both RHEL9 and Ubuntu have released patches for OpenSSH which fixes the security vulnerability.
These can be pulled using the platform’s respective package manager.

If you have existing RHEL9 or Ubuntu VDIs, we recommend following the
**PATCH EXISTING VDIs** instructions below. To patch future VDIs,
we recommend following the **PATCH FUTURE VDIs** instructions.
These instructions describe how to run a script to apply the platform update on your VDIs.

###### PATCH EXISTING VDIs

1. Run the following command which will patch all existing Ubuntu and RHEL9 VDIs:
   1. The patch script requires [AWS CLI v2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
   2. Configure the AWS CLI for the account and region where RES is deployed,
      and make sure that you have AWS Systems Manager permissions to send a
      Systems Manager Run Command.

   ```
   aws ssm send-command \
       --document-name "AWS-RunRemoteScript" \
       --targets "Key=tag:res:NodeType,Values=virtual-desktop-dcv-host" \
       --parameters '{"sourceType":["S3"],"sourceInfo":["{\"path\":\"https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/scripts/patch_openssh.sh\"}"],"commandLine":["bash patch_openssh.sh"]}'
   ```

2. You can verify the script ran successfully on the [Run Command page](https://console.aws.amazon.com/systems-manager/run-command "https://console.aws.amazon.com/systems-manager/run-command"). Click on the
   **Command History** tab, select the most recent Command ID,
   and verify that all instance IDs have a SUCCESS message.

###### PATCH FUTURE VDIs

1. To download the patch script and patch file
   ([patch.py](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patch.py "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patch.py") and
   [update_openssh.patch](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patches/update_openssh.patch "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patches/update_openssh.patch")) run the following commands, replacing
   `<output-directory>` with the directory where you want to download
   the files, and `<environment-name>` with the name of your RES
   environment:

###### Note

    * The patch only applies to RES 2024.06.
    * The patch script requires [AWS CLI v2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")),
     Python 3.9.16 or above, and
     [Boto3](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/").
    * Configure your copy of the AWS CLI for the account and region where
     RES is deployed, and make sure that you have S3 permissions to write to
     the bucket created by RES.

```
OUTPUT_DIRECTORY=`<output-directory>`
ENVIRONMENT_NAME=`<environment-name>`

curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patch.py --output ${OUTPUT_DIRECTORY}/patch.py

curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.06/patch_scripts/patches/update_openssh.patch --output ${OUTPUT_DIRECTORY}/update_openssh.patch
```

2. Run the following patch command:

```
python3 ${OUTPUT_DIRECTORY}/patch.py --environment-name ${ENVIRONMENT_NAME} --res-version 2024.06 --module virtual-desktop-controller --patch ${OUTPUT_DIRECTORY}/update_openssh.patch
```

3. Restart the VDC Controller instance for your environment with the following
   commands:

```
INSTANCE_ID=$(aws ec2 describe-instances \
    --filters \
    Name=tag:Name,Values=${ENVIRONMENT_NAME}-vdc-controller \
    Name=tag:res:EnvironmentName,Values=${ENVIRONMENT_NAME}\
    --query "Reservations[0].Instances[0].InstanceId" \
    --output text)

aws ec2 terminate-instances --instance-ids ${INSTANCE_ID}
```

###### Important

Patching future VDIs is only supported on RES versions 2024.06 and later.
To patch future VDIs in RES environments with versions earlier than 2024.06, first upgrade
the RES environment to 2024.06 using the instructions at: [Major version updates](update-the-product.md#major-version-update "update-the-product.md#major-version-update").

........................

### (2024.04-2024.04.02)

Provided IAM Permission Boundary not attached to the VDI instances' role

**The issue**

Virtual desktop sessions are not properly inheriting their project’s permission boundary
configuration. This is a result of the permissions boundary defined by the IAMPermissionBoundary
parameter not being properly assigned to a project during that project’s creation.

**Affected versions**

2024.04 - 2024.04.02

**Mitigation**

Follow these steps to allow VDIs to properly inherit the permissions boundary assigned to
a project:

1. To download the patch script and patch file
   ([patch.py](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patch.py "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patch.py") and
   [vdi_host_role_permission_boundary.patch](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patches/vdi_host_role_permission_boundary.patch "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patches/vdi_host_role_permission_boundary.patch")), run the following command,
   replacing `<output-directory>` with the local directory where
   you'd like to put the files:
   1. The patch only applies to RES 2024.04.02. If you are on version
      2024.04 or 2024.04.01, you can follow [the steps listed in the public document for minor version updates](update-the-product.md#minor-version-updates "update-the-product.md#minor-version-updates")
      to update your environment to 2024.04.02.
   2. The patch script requires [AWS CLI v2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")),
      Python 3.9.16 or above, and
      [Boto3](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/").
   3. Configure the AWS CLI for the account and region where RES is deployed,
      and make sure that you have S3 permissions to write to the bucket created
      by RES.

```
OUTPUT_DIRECTORY=`<output-directory>`

curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patch.py --output ${OUTPUT_DIRECTORY}/patch.py

curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patches/vdi_host_role_permission_boundary.patch --output ${OUTPUT_DIRECTORY}/vdi_host_role_permission_boundary.patch
```

2. Navigate to the directory where the patch script and patch file are downloaded.
   Run the following patch command, replacing `<environment-name>`
   with the name of your RES environment:

```
python3 patch.py --environment-name `<environment-name>` --res-version 2024.04.02 --module cluster-manager --patch vdi_host_role_permission_boundary.patch
```

3. Restart the cluster-manager instance in your environment by running this command,
   replacing `<environment-name>` with the name of your RES environment.
   You may also terminate the instance from the Amazon EC2 Management Console.

```
ENVIRONMENT_NAME=`<environment-name>`

INSTANCE_ID=$(aws ec2 describe-instances \
    --filters \
    Name=tag:Name,Values=${ENVIRONMENT_NAME}-cluster-manager \
    Name=tag:res:EnvironmentName,Values=${ENVIRONMENT_NAME}\
    --query "Reservations[0].Instances[0].InstanceId" \
    --output text)

aws ec2 terminate-instances --instance-ids ${INSTANCE_ID}
```

........................

### (2024.04.02 and earlier)

Windows NVIDIA instances in ap-southeast-2 (Sydney) fail to launch

**The issue**

Amazon Machine Images (AMIs) are used to spin up virtual desktops (VDIs) in RES with
specific configurations. Each AMI has an associated ID that differs per region. The AMI
ID configured in RES to launch Windows Nvidia instances in ap-southeast-2 (Sydney) is
currently incorrect.

AMI-ID `ami-0e190f8939a996caf` for this type of instance configuration is
incorrectly listed in ap-southeast-2 (Sydney). AMI ID `ami-027cf6e71e2e442f4`
should be used instead.

Users will get the following error when trying to launch an instance with the default
`ami-0e190f8939a996caf` AMI.

```
An error occured (InvalidAMIID.NotFound) when calling the RunInstances operation: The image id ‘[ami-0e190f8939a996caf]’ does not exist
```

Steps to reproduce the bug, including an example configuration file:

- Deploy RES in the ap-southeast-2 region.
- Launch an instance using Windows-NVIDIA default software stack (AMI ID
  `ami-0e190f8939a996caf`).

**Affected versions**

All RES versions 2024.04.02 or earlier are impacted

**Mitigation**

The following mitigation has been tested on RES version 2024.01.01:

- Register a new software stack with the following settings
  - AMI ID: `ami-027cf6e71e2e442f4`
  - Operating System: Windows
  - GPU Manufacturer: NVIDIA
  - Min. Storage Size (GB): 30
  - Min. RAM (GB): 4

- Use this software stack to launch Windows-NVIDIA instances

........................

### (2024.04 and 2024.04.01)

RES delete failure in GovCloud

**The issue**

During the RES delete workflow the `UnprotectCognitoUserPool` Lambda inactivates
Deletion Protection for Cognito User Pools that will later be deleted. The Lambda execution is
started by the `InstallerStateMachine`.

Because of default AWS CLI version differences between Commercial and GovCloud regions,
the `update_user_pool` call in the Lambda will fail in GovCloud regions.

Customers will get the following error when trying to delete RES in GovCloud regions:

```
Parameter validation failed: Unknown parameter in input: \"DeletionProtection\", must be one of: UserPoolId, Policies, LambdaConfig, AutoVerifiedAttributes, SmsVerificationMessage, EmailVerificationMessage, EmailVerificationSubject, VerificationMessageTemplate, SmsAuthenticationMessage, MfaConfiguration, DeviceConfiguration, EmailConfiguration, SmsConfiguration, UserPoolTags, AdminCreateUserConfig, UserPoolAddOns, AccountRecoverySetting
```

Steps to reproduce the bug:

- Deploy RES in a GovCloud region
- Delete the RES stack

**Affected versions**

RES version 2024.04 and 2024.04.01

**Mitigation**

The following mitigation has been tested on RES version 2024.04:

- Open the `UnprotectCognitoUserPool` Lambda
  - Naming convention:
    ``<env-name>`-InstallerTasksUnprotectCognitoUserPool-...`

- **Runtime Settings** -> **Edit** -> Select
  **Runtime** `Python 3.11` -> **Save**.
- Open CloudFormation.
- Delete RES stack -> leave Retain Installer Resource UNCHECKED ->
  **Delete**.

........................

### (2024.04 - 2024.04.02)

Linux virtual desktop may be stuck in the "RESUMING" status on reboot

**The issue**

Linux virtual desktops can get stuck in "RESUMING" status when restarting after a manual
or scheduled stop.

After the instance is rebooted, the AWS Systems Manager doesn't run any remote commands to
create a new DCV session and the following log message is missing in the vdc-controller CloudWatch
logs (under the `/<environment-name>/vdc/controller` CloudWatch log group):

```
Handling message of type DCV_HOST_REBOOT_COMPLETE_EVENT
```

**Affected versions**

2024.04 - 2024.04.02

**Mitigation**

To recover the virtual desktops that are stuck in the "RESUMING" state:

1. SSH into the problem instance from the EC2 console.
2. Run the following commands on the instance:

```
sudo su -
/bin/bash /root/bootstrap/latest/virtual-desktop-host-linux/configure_post_reboot.sh
sudo reboot
```

3. Wait for the instance to reboot.

To prevent new virtual desktops from running into the same issue:

1. To download the patch script and patch file
   ([patch.py](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patch.py "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patch.py") and
   [vdi_stuck_in_resuming_status.patch](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patches/vdi_stuck_in_resuming_status.patch "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patches/vdi_stuck_in_resuming_status.patch")), run the following command, replacing
   `<output-directory>` with the directory where you want to put
   the files:

###### Note

    * The patch only applies to RES 2024.04.02.
    * The patch script requires [AWS CLI v2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"),
     Python 3.9.16 or above, and
     [Boto3](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/").
    * Configure the AWS CLI for the account and region where RES is deployed,
     and make sure that you have S3 permissions to write to the bucket created
     by RES.

```
OUTPUT_DIRECTORY=`<output-directory>`

curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patch.py --output ${OUTPUT_DIRECTORY}/patch.py

curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patches/vdi_stuck_in_resuming_status.patch --output ${OUTPUT_DIRECTORY}/vdi_stuck_in_resuming_status.patch
```

2. Navigate to the directory where the patch script and patch file are downloaded.
   Run the following patch command, replacing `<environment-name>`
   with the name of your RES environment and `<aws-region>` with
   the region where RES is deployed:

```
python3 patch.py --environment-name `<environment-name>` --res-version 2024.04.02 --module virtual-desktop-controller --patch vdi_stuck_in_resuming_status.patch --region `<aws-region>`
```

3. To restart the VDC Controller instance for your environment, run the following
   commands, replacing `<environment-name>` with the name of your
   RES environment:

```
ENVIRONMENT_NAME=`<environment-name>`

INSTANCE_ID=$(aws ec2 describe-instances \
    --filters \
    Name=tag:Name,Values=${ENVIRONMENT_NAME}-vdc-controller \
    Name=tag:res:EnvironmentName,Values=${ENVIRONMENT_NAME}\
    --query "Reservations[0].Instances[0].InstanceId" \
    --output text)

aws ec2 terminate-instances --instance-ids ${INSTANCE_ID}
```

........................

### (2024.04.02 and earlier)

Fails to sync AD users whose SAMAccountName attribute includes capital letters or special
characters

**The issue**

RES fails to sync AD users after SSO is set up for at least two hours (two AD sync cycles).
The cluster-manager CloudWatch logs (under the `/<environment-name>/cluster-manager`
log group) include the following error during AD sync:

```
Error: [INVALID_PARAMS] Invalid params: user.username must match regex: ^(?=.{3,20}$)(?![_.])(?!.*[_.]{2})[a-z0-9._]+(?<![_.])$
```

The error results from RES only accepting a SAMAccount username that meets the following
requirements:

- It can only contain lower case ASCII letters, digits, period (.), underscore (\_).
- A period or underscore is not allowed as the first or last character.
- It cannot contain two continuous periods or underscores (e.g. .., \_\_, .\_, \_.).

**Affected versions**

2024.04.02 and earlier

**Mitigation**

1. To download the patch script and patch file
   ([patch.py](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patch.py "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patch.py") and
   [samaccountname_regex.patch](https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patches/samaccountname_regex.patch "https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patches/samaccountname_regex.patch")), run the following command, replacing
   `<output-directory>` with the directory where you want to put the
   files:

###### Note

    * The patch only applies to RES 2024.04.02.
    * The patch script requires [AWS CLI v2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"),
     Python 3.9.16 or above, and
     [Boto3](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/").
    * Configure the AWS CLI for the account and region where RES is deployed,
     and make sure that you have S3 permissions to write to the bucket created
     by RES.

```
OUTPUT_DIRECTORY=`<output-directory>`

curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patch.py --output ${OUTPUT_DIRECTORY}/patch.py

curl https://research-engineering-studio-us-east-1.s3.amazonaws.com/releases/2024.04.02/patch_scripts/patches/samaccountname_regex.patch --output ${OUTPUT_DIRECTORY}/samaccountname_regex.patch
```

2. Navigate to the directory where the patch script and patch file are downloaded.
   Run the following patch command, replacing `<environment-name>`
   with the name of your RES environment:

```
python3 patch.py --environment-name `<environment-name>` --res-version 2024.04.02 --module cluster-manager --patch samaccountname_regex.patch
```

3. To restart the Cluster Manager instance for your environment, run the following
   commands, replacing `<environment-name>` with the name
   of your RES environment. You may also terminate the instance from the Amazon EC2
   Management Console.

```
ENVIRONMENT_NAME=`<environment-name>`

INSTANCE_ID=$(aws ec2 describe-instances \
    --filters \
    Name=tag:Name,Values=${ENVIRONMENT_NAME}-cluster-manager \
    Name=tag:res:EnvironmentName,Values=${ENVIRONMENT_NAME}\
    --query "Reservations[0].Instances[0].InstanceId" \
    --output text)

aws ec2 terminate-instances --instance-ids ${INSTANCE_ID}
```

........................

### (2024.04.02 and earlier)

Private key for accessing the bastion host is invalid

**The issue**

When a user downloads the private key to access the bastion host from the RES web portal,
the key is not well formatted– multiple lines are downloaded as a single line, which
makes the key invalid. The user will get the following error when they attempt to access the
bastion host with the downloaded key:

```
Load key "`<downloaded-ssh-key-path>`": error in libcrypto
`<user-name>`@`<bastion-host-public-ip>`: Permission denied (publickey,gssapi-keyex,gssapi-with-mic)
```

**Affected versions**

2024.04.02 and earlier

**Mitigation**

We recommend using Chrome to download the keys, as this browser is unaffected.

Alternatively, the key file can be reformatted by creating a new line after
`-----BEGIN PRIVATE KEY-----` and another new line just before
`-----END PRIVATE KEY-----`.

........................

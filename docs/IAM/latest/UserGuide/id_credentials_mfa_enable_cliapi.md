# Assign MFA devices

in the AWS CLI or AWS API

You can use AWS CLI commands or AWS API operations to enable a virtual MFA device for an
IAM user. You cannot enable an MFA device for the AWS account root user with the AWS CLI, AWS API, Tools for Windows PowerShell,
or any other command line tool. However, you can use the AWS Management Console to enable an MFA device for
the root user.

When you enable an MFA device from the AWS Management Console, the console performs multiple steps for
you. If you instead create a virtual device using the AWS CLI, Tools for Windows PowerShell, or AWS API, then you must
perform the steps manually and in the correct order. For example, to create a virtual MFA
device, you must create the IAM object and extract the code as either a string or a QR code
graphic. Then you must sync the device and associate it with an IAM user. See the **Examples** section of [New-IAMVirtualMFADevice](../../../powershell/latest/reference/Index.md "../../../powershell/latest/reference/Index.md") for more details. For a physical device, you skip the
creation step and go directly to syncing the device and associating it with the user.

You can attach tags to your IAM resources, including virtual MFA devices, to identify,
organize, and control access to them. You can tag virtual MFA devices only when you use the
AWS CLI or AWS API.

An IAM user using the SDK or CLI can enable an additional MFA device by calling [`EnableMFADevice`](../APIReference/API_EnableMFADevice.md "../APIReference/API_EnableMFADevice.md") or deactivate an existing MFA device by calling [`DeactivateMFADevice`](../APIReference/API_DeactivateMFADevice.md "../APIReference/API_DeactivateMFADevice.md"). To do this successfully, they must first call
[`GetSessionToken`](../../../STS/latest/APIReference/API_GetSessionToken.md "../../../STS/latest/APIReference/API_GetSessionToken.md") and submit MFA codes with an existing MFA device. This
call returns temporary security credentials that can then be used to sign API operations that
require MFA authentication. For an example request and response, see [`GetSessionToken`—temporary credentials for users in untrusted
environments](id_credentials_temp_request.md#api_getsessiontoken "id_credentials_temp_request.md#api_getsessiontoken").

###### To create the virtual device entity in IAM to represent a virtual MFA device

These commands provide an ARN for the device that is used in place of a serial number in
many of the following commands.

- AWS CLI: [`aws iam create-virtual-mfa-device`](../../../cli/latest/reference/iam/create-virtual-mfa-device.md "../../../cli/latest/reference/iam/create-virtual-mfa-device.md")
- AWS API: [`CreateVirtualMFADevice`](../APIReference/API_CreateVirtualMFADevice.md "../APIReference/API_CreateVirtualMFADevice.md")

###### To enable an MFA device for use with AWS

These commands synchronize the device with AWS and associate it with a user. If the
device is virtual, use the ARN of the virtual device as the serial number.

###### Important

Submit your request immediately after generating the authentication codes. If you generate
the codes and then wait too long to submit the request, the MFA device successfully associates
with the user but the MFA device becomes out of sync. This happens because time-based one-time
passwords (TOTP) expire after a short period of time. If this happens, you can resynchronize
the device using the commands described below.

- AWS CLI: [`aws
iam enable-mfa-device`](../../../cli/latest/reference/iam/enable-mfa-device.md "../../../cli/latest/reference/iam/enable-mfa-device.md")
- AWS API: [`EnableMFADevice`](../APIReference/API_EnableMFADevice.md "../APIReference/API_EnableMFADevice.md")

###### To deactivate a device

Use these commands to disassociate the device from the user and deactivate it. If the
device is virtual, use the ARN of the virtual device as the serial number. You must also
separately delete the virtual device entity.

- AWS CLI: [`aws iam deactivate-mfa-device`](../../../cli/latest/reference/iam/deactivate-mfa-device.md "../../../cli/latest/reference/iam/deactivate-mfa-device.md")
- AWS API: [`DeactivateMFADevice`](../APIReference/API_DeactivateMFADevice.md "../APIReference/API_DeactivateMFADevice.md")

###### To list virtual MFA device entities

Use these commands to list virtual MFA device entities.

- AWS CLI: [`aws iam list-virtual-mfa-devices`](../../../cli/latest/reference/iam/list-virtual-mfa-devices.md "../../../cli/latest/reference/iam/list-virtual-mfa-devices.md")
- AWS API: [`ListVirtualMFADevices`](../APIReference/API_ListVirtualMFADevices.md "../APIReference/API_ListVirtualMFADevices.md")

###### To tag a virtual MFA device

Use these commands to tag a virtual MFA device.

- AWS CLI: [`aws iam
tag-mfa-device`](../../../cli/latest/reference/iam/tag-mfa-device.md "../../../cli/latest/reference/iam/tag-mfa-device.md")
- AWS API: [`TagMFADevice`](../APIReference/API_TagMFADevice.md "../APIReference/API_TagMFADevice.md")

###### To list tags for a virtual MFA device

Use these commands to list the tags attached to a virtual MFA device.

- AWS CLI: [`aws iam list-mfa-device-tags`](../../../cli/latest/reference/iam/list-mfa-device-tags.md "../../../cli/latest/reference/iam/list-mfa-device-tags.md")
- AWS API: [`ListMFADeviceTags`](../APIReference/API_ListMFADeviceTags.md "../APIReference/API_ListMFADeviceTags.md")

###### To untag a virtual MFA device

Use these commands to remove tags attached to a virtual MFA device.

- AWS CLI: [`aws
iam untag-mfa-device`](../../../cli/latest/reference/iam/untag-mfa-device.md "../../../cli/latest/reference/iam/untag-mfa-device.md")
- AWS API: [`UntagMFADevice`](../APIReference/API_UntagMFADevice.md "../APIReference/API_UntagMFADevice.md")

###### To resynchronize an MFA device

Use these commands if the device is generating codes that are not accepted by AWS. If
the device is virtual, use the ARN of the virtual device as the serial number.

- AWS CLI: [`aws
iam resync-mfa-device`](../../../cli/latest/reference/iam/resync-mfa-device.md "../../../cli/latest/reference/iam/resync-mfa-device.md")
- AWS API: [`ResyncMFADevice`](../APIReference/API_ResyncMFADevice.md "../APIReference/API_ResyncMFADevice.md")

###### To delete a virtual MFA device entity in IAM

After the device is disassociated from the user, you can delete the device entity.

- AWS CLI: [`aws iam delete-virtual-mfa-device`](../../../cli/latest/reference/iam/delete-virtual-mfa-device.md "../../../cli/latest/reference/iam/delete-virtual-mfa-device.md")
- AWS API: [`DeleteVirtualMFADevice`](../APIReference/API_DeleteVirtualMFADevice.md "../APIReference/API_DeleteVirtualMFADevice.md")

###### To recover a virtual MFA device that is lost or not working

Sometimes, a user's device that hosts the virtual MFA app is lost, replaced, or not
working. When this happens, the user can't recover it on their own. The user must contact
an administrator to deactivate the device. For more information, see [Recover an MFA protected identity in
IAM](id_credentials_mfa_lost-or-broken.md "id_credentials_mfa_lost-or-broken.md").

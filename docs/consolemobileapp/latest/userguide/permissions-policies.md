

# IAM permissions for listing mobile devices as delivery channels
<a name="permissions-policies"></a>

The AWS Console Mobile Application supports push notifications via [AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is.html). If you enable push notifications, the Console Mobile Application collects your device nickname (if applicable) to help identify your device. You can manage your mobile device’s push notifications from the AWS User Notifications console by adding your device as a delivery channel. Delivery channels allow you to receive and view notifications in locations other than the AWS Management Console. You can remove your device as a delivery channel at any time.

You must have access to the `ListDeviceIdentities` and `GetDeviceIdentity` API actions to view your mobile device in the AWS User Notifications Console. The following sample policies show how to allow or deny permissions to these actions.

For more information about delivery channels, see [Managing delivery channels](https://docs.aws.amazon.com/notifications/latest/userguide/managing-delivery-channels.html) in the *AWS User Notifications User Guide*.

## Sample ListDeviceIdentities IAM policies
<a name="_sample_listdeviceidentities_iam_policies"></a>

### Allow ListDeviceIdentities
<a name="_allow_listdeviceidentities"></a>

You can attach the following policy to your IAM identities. This policy allows access to `ListDeviceIdentities`.

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "consoleapp:ListDeviceIdentities"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

### Deny ListDeviceIdentities
<a name="_deny_listdeviceidentities"></a>

You can attach the following policy to your IAM identities. This policy denies access to `ListDeviceIdentities`.

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "consoleapp:ListDeviceIdentities"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

## Sample GetDeviceIdentity IAM policies
<a name="_sample_getdeviceidentity_iam_policies"></a>

### Allow GetDeviceIdentity
<a name="_allow_getdeviceidentity"></a>

This policy allows a specific resource access to `GetDeviceIdentity`.

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "consoleapp:GetDeviceIdentity"
            ],
            "Resource": [
                "arn:aws:consoleapp::123456789012:device/2FQVtmveB13WEXAMPL3D3V1D/identity/AIDACKCEVSQ6C2EXAMPLE"
            ]
        }
    ]
}
```

### Deny GetDeviceIdentity
<a name="_deny_getdeviceidentity"></a>

This policy denies a specific resource access to `GetDeviceIdentity`.

```
{
"Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "consoleapp:GetDeviceIdentity"
            ],
            "Resource": [
                "arn:aws:consoleapp::123456789012:device/2FQVtmveB13WEXAMPL3D3V1D/identity/AIDACKCEVSQ6C2EXAMPLE"
            ]
        }
    ]
}
```

The following shows an example of the denial response:

```
{"message": "User: arn:aws:iam::123456789012:user/testUser-readOnly is not authorized to perform: consoleapp:GetDeviceIdentity on resource: arn:aws:consoleapp::123456789012:device/2FQVtmveB13WEXAMPL3D3V1D/identity/123456789012 with an explicit deny"}
```
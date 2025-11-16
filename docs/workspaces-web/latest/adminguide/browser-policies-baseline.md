# Editing the baseline browser policy in Amazon WorkSpaces Secure Browser

In order to deliver the service, WorkSpaces Secure Browser applies a baseline browser policy to all portals.
This baseline policy is applied in addition to those you specify from the console view or JSON
upload. The following is the list of policies applied by the service in JSON format:

```

{
    "chromePolicies":
    {
        "DefaultDownloadDirectory": {
            "value": "/home/as2-streaming-user/MyFiles/TemporaryFiles"
        },
        "DownloadDirectory": {
            "value": "/home/as2-streaming-user/MyFiles/TemporaryFiles"
        },
        "DownloadRestrictions": {
            "value": 1
        },
        "URLBlocklist": {
            "value": [
                "file://",
                "http://169.254.169.254",
                "http://[fd00:ec2::254]",
            ]
        },
        "URLAllowlist": {
            "value": [
                "file:///home/as2-streaming-user/MyFiles/TemporaryFiles",
                "file:///opt/appstream/tmp/TemporaryFiles",
            ]
        }
    }
}
```

Customers can't make changes to the following policies:

- `DefaultDownloadDirectory` – This policy can't be edited. The service
  overwrites any changes to this policy.
- `DownloadDirectory` – This policy can't be edited. The service
  overwrites any changes to this policy.
  The baseline `URLAllowlist` and `URLBlocklist` policies can't be overwritten. Note that the JSON browser policy file that is associated with your web portal will not contain these baseline policies. To see a full list of all applied policies and their values, navigate to "chrome://policy" from within a remote browsing session.

Customers can update the following policies for their web portal:

- `DownloadRestrictions` – The default is set to `1` to
  prevent downloads identified as malicious by Chrome Safe Browsing. For more information, see
  [Prevent users from
  downloading harmful files](https://support.google.com/chrome/a/answer/7579271 "https://support.google.com/chrome/a/answer/7579271"). You can set the value from `0` to
  `4`.

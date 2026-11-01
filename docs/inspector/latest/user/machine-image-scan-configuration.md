

# Configuring machine image scanning
<a name="machine-image-scan-configuration"></a>

 Your scan configuration determines which of the machine images that your account owns are in scope. It has three parts, which Amazon Inspector applies in this order: 

1.  **Scan eligibility windows** – How recently a machine image must have been created, or had an instance launched from it, to be in scope. For more information, see [Setting scan eligibility windows](#machine-image-eligibility-windows). 

1.  **Exclusion options** – Whether to exclude copied machine images and backup machine images. To exclude other individual machine images, use an exclusion tag in exclusion mode. For more information, see [Excluding copied and backup machine images](#machine-image-exclusions). 

1.  **Scan mode** – Whether Amazon Inspector scans every eligible image except the ones you tag (exclusion mode), or only the ones you tag (inclusion mode). For more information, see [Managing machine image scan mode](#machine-image-scan-mode). 

 A machine image is in scope only if it satisfies all three parts. Amazon Inspector excludes a machine image if any exclusion condition applies. 

 You configure machine image scanning by using the [UpdateConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateConfiguration.html) API operation, or from the machine image scanning settings under **General settings** in the Amazon Inspector console. To view your current configuration, use the [GetConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetConfiguration.html) API operation. Amazon Inspector applies default values for every setting when you activate machine image scanning for an account. The default configuration is the following: 
+ **Created within** and **Last launched within** – 14 days each.
+ Exclusion options – Copied machine images and backup machine images are excluded.
+ Scan mode – Exclusion mode (`SCAN_ALL`), with no exclusion tag.

**Note**  
 If you're the delegated administrator for an organization, your machine image scan configuration propagates to all member accounts in your organization that have machine image scanning activated. Member accounts can't configure machine image scanning for themselves. If a member account calls UpdateConfiguration, Amazon Inspector returns an `AccessDeniedException`. For more information, see [Managing multiple accounts in Amazon Inspector with AWS Organizations](managing-multiple-accounts.md). 

**Topics**
+ [Setting scan eligibility windows](#machine-image-eligibility-windows)
+ [Excluding copied and backup machine images](#machine-image-exclusions)
+ [Managing machine image scan mode](#machine-image-scan-mode)
+ [How Amazon Inspector applies a configuration change](#machine-image-reconciliation)
+ [Configuring machine image scan settings](#machine-image-scan-configuration-proc)

## Setting scan eligibility windows
<a name="machine-image-eligibility-windows"></a>

 Scan eligibility windows determine how long Amazon Inspector continues to monitor a machine image. Amazon Inspector provides two independent windows: 

**Created within**  
 A machine image is eligible if you created it within this window. 

**Last launched within**  
 A machine image is eligible if you launched an EC2 instance from it within this window. 

 A machine image is eligible if *either* window is satisfied. This means an older machine image stays in scope as long as you're still launching instances from it, and a newly created image is in scope even if you haven't launched an instance from it yet. 

 The following durations are available for each window: 
+ 7 days
+ 14 days (default)
+ 30 days
+ 60 days
+ 90 days
+ 180 days

 When a machine image falls outside both windows, Amazon Inspector stops monitoring it and closes its findings. A deprecated image stays eligible for rescans as long as it satisfies either window. Amazon Inspector checks your images against the windows once a day. As a result, a change in scope can take up to 24 hours to take effect. 

**Important**  
 Lengthening a scan eligibility window increases the number of machine images that Amazon Inspector scans, which increases your Amazon Inspector costs. Amazon Inspector meters machine image scanning per scan. For more information, see [Monitoring Usage and Cost in Amazon Inspector](usage.md) and [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/). 

## Excluding copied and backup machine images
<a name="machine-image-exclusions"></a>

 You can exclude two categories of machine image from scanning. These exclusions apply in both scan modes. Amazon Inspector applies them before your scan mode tag filter. To exclude other individual images, add an exclusion tag to them and use exclusion (`SCAN_ALL`) mode. For more information, see [Managing machine image scan mode](#machine-image-scan-mode). 

**Copied machine images**  
 Excludes machine images that are copies of other images. Amazon Inspector identifies a copy from the description that Amazon EC2 adds to the copied image and its snapshots. Use this option when you already scan the image in the source account and don't want to pay to scan the copy too. It's turned on by default. 

**Backup machine images**  
 Excludes machine images that Amazon Data Lifecycle Manager or AWS Backup created. Amazon Inspector identifies these images by the tags that AWS applies to them: `aws:dlm:lifecycle-policy-id` or `aws:backup:source-resource`. Use this option when you don't want automated backup images to increase your scan volume. It's turned on by default. For more information about Data Lifecycle Manager, see [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) in the *Amazon Elastic Compute Cloud User Guide*. 

**Note**  
 You're not charged for excluded machine images. 

## Managing machine image scan mode
<a name="machine-image-scan-mode"></a>

 The scan mode determines which of your eligible machine images Amazon Inspector keeps in scope. It also sets whether the tag you configure adds images to that scope or removes them. Amazon Inspector scans continuously in both modes, and supports the following modes. 

**Exclusion mode** (`SCAN_ALL`) – default  
 Amazon Inspector continuously scans every eligible machine image except the ones that carry the tag you configure. In this mode, the tag is an *exclusion* tag. Use this mode when you want broad coverage and only need to opt specific images out. 

**Inclusion mode** (`TARGET_SCANNING`)  
 Amazon Inspector continuously scans only the eligible machine images that carry the tag you configure, and excludes all others. In this mode, the tag is an *inclusion* tag. Use this mode when you want to limit scanning to a targeted subset of your images, such as production images only. 

 You choose the tag that Amazon Inspector matches on, so you can reuse a tag that's already part of your tagging strategy. Note the following about the tag: 
+  A tag is required for inclusion (`TARGET_SCANNING`) mode. If you set this mode without a tag, Amazon Inspector returns a `ValidationException`. In exclusion (`SCAN_ALL`) mode, a tag is optional. If you don't provide one, Amazon Inspector scans every eligible machine image. 
+  You can configure one tag. If you provide more than one, Amazon Inspector returns a `ValidationException`. 
+  A tag value is optional. If you specify a key without a value, Amazon Inspector matches any machine image that has that key, regardless of its value. If you specify both a key and a value, Amazon Inspector matches only machine images that have that exact key-value pair. 

 For information about adding tags to a machine image, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon Elastic Compute Cloud User Guide*. 

 When you add or remove the configured tag on a machine image, Amazon Inspector re-evaluates that image. In exclusion (`SCAN_ALL`) mode, adding the tag removes the image from your scanning scope, and removing the tag brings it back in. In inclusion (`TARGET_SCANNING`) mode, adding the tag brings the image into scope, and removing the tag removes it. In both modes, the exclusion options still apply, so an image that you tag for inclusion stays out of scope if it's also a copied or backup image that you chose to exclude. 

**Important**  
 Before you switch from exclusion mode to inclusion mode, tag the machine images that you want Amazon Inspector to keep scanning. When you switch modes, Amazon Inspector immediately removes every untagged image from your scanning scope and closes the findings for those images. 

## How Amazon Inspector applies a configuration change
<a name="machine-image-reconciliation"></a>

 When you change your scan configuration, Amazon Inspector re-evaluates every machine image in the account right away. Amazon Inspector then does the following: 
+  Starts scanning machine images that the change brought into scope. 
+  Stops monitoring machine images that the change removed from scope, and closes the findings for those images. 

 Amazon Inspector processes one configuration change for an account at a time. If you call UpdateConfiguration while Amazon Inspector is still applying a previous change, Amazon Inspector returns a `ValidationException`. Retry the request after the previous change finishes. If you submit a configuration that matches your current configuration, Amazon Inspector treats the request as a no-op. 

 Separately from configuration changes, Amazon Inspector re-evaluates your machine images against your scan eligibility windows once a day. For more information, see [Setting scan eligibility windows](#machine-image-eligibility-windows). 

**Note**  
 If you're the delegated administrator for an organization, Amazon Inspector applies your change to your own account and then propagates it to each member account that has machine image scanning activated. Each member account is re-evaluated independently, so the change can take effect at different times across your organization. 

## Configuring machine image scan settings
<a name="machine-image-scan-configuration-proc"></a>

 The following procedure describes how to configure machine image scanning. To complete this procedure for a multi-account environment, follow these steps while signed in as the Amazon Inspector delegated administrator. 

------
#### [ Console ]

**To configure machine image scanning**

1.  Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home). 

1.  Select the AWS Region where you want to configure machine image scanning. 

1.  From the navigation pane, choose **General settings**, and then choose **Machine image scanning settings**. 

1.  Under **Scan eligibility**, choose a duration for **Created within** and a duration for **Last launched within**. 

1.  Under **Scan mode**, choose **Exclusion mode** or **Inclusion mode**, and then enter the tag key and optional tag value that Amazon Inspector matches on. A tag is required for **Inclusion mode**. (Optional) Select or clear **Exclude copied machine images** and **Exclude backup machine images**; both are selected by default. 

1.  Choose **Save**. 

1.  (Recommended) Repeat these steps in each AWS Region where you activated machine image scanning. 

------
#### [ API ]

 Run the [UpdateConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateConfiguration.html) API operation. In the request, provide an `amiConfiguration` object. Any field that you omit keeps its current value. 

 The following example continuously scans all eligible machine images except the ones tagged with `InspectorExclude=true`, and excludes copied machine images. 

```
{
    "amiConfiguration": {
        "createdWithin": "180_DAYS",
        "lastLaunchedWithin": "90_DAYS",
        "scanModeConfiguration": {
            "scanMode": "SCAN_ALL",
            "tags": [
                {
                    "key": "InspectorExclude",
                    "value": "true"
                }
            ],
            "excludeCopiedAmis": true,
            "excludeBackupDlmAmis": false
        }
    }
}
```

 The following example continuously scans only the eligible machine images that have the `InspectorScan` tag key, regardless of the tag value, and excludes backup machine images. 

```
{
    "amiConfiguration": {
        "scanModeConfiguration": {
            "scanMode": "TARGET_SCANNING",
            "tags": [
                {
                    "key": "InspectorScan"
                }
            ],
            "excludeCopiedAmis": false,
            "excludeBackupDlmAmis": true
        }
    }
}
```

------
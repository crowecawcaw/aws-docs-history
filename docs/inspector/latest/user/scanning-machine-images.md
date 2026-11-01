

# Scanning machine images with Amazon Inspector
<a name="scanning-machine-images"></a>

 Amazon Inspector scans the machine images that your account owns for operating system and programming language package vulnerabilities. A machine image is an Amazon Machine Image (AMI) that you use to launch EC2 instances. When Amazon Inspector detects a vulnerability in a machine image, it produces a **Package Vulnerability** type finding with a **Resource type** of `MACHINE_IMAGE`. Scanning your machine images lets you find and remediate vulnerabilities before you use an image to launch instances. 

 For each machine image, Amazon Inspector collects a software inventory from all of the Amazon EBS snapshots that back the image, and then evaluates that inventory against vulnerability data that Amazon Inspector sources from more than 50 data feeds. Because Amazon Inspector reads the snapshots that back an image, you don't need to launch an instance from a machine image for Amazon Inspector to scan it. 

 By default, machine image scanning is continuous. When you activate machine image scanning for an account, Amazon Inspector discovers the machine images that your account owns, scans all of the eligible ones, and then keeps monitoring them for as long as they remain in scope. Amazon Inspector scans new machine images as you create, copy, register, or enable them, and rescans in-scope images whenever Amazon Inspector adds a new common vulnerabilities and exposures (CVE) item to its database that's relevant to that image. You don't need to request a rescan. 

 Exclusion mode, which scans all eligible machine images except the ones you tag for exclusion, is the default scan mode. If you only want Amazon Inspector to scan a targeted subset of your machine images, you can change the scan mode to inclusion mode and tag the images you want scanned. Amazon Inspector scans continuously in either mode; the scan mode controls which images are in scope, not how often Amazon Inspector scans them. For more information, see [Managing machine image scan mode](machine-image-scan-configuration.md#machine-image-scan-mode). 

 If you don't want continuous scanning, you can scan a single machine image on demand instead. An on-demand scan is a one-time scan that you request for a specific machine image, and it doesn't require you to activate Amazon Inspector. On-demand scans ignore your machine image scan configuration, and Amazon Inspector delivers the results only through Amazon EventBridge. For more information, see [Running on-demand machine image scans with Amazon Inspector](machine-image-on-demand.md). 

 For information about how to activate machine image scanning, see [Activating a scan type](activate-scans.md). For information about how to control which machine images Amazon Inspector scans, see [Configuring machine image scanning](machine-image-scan-configuration.md). For information about how to view findings, see [Viewing Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-locating-analyzing.html). 

**Note**  
 Amazon Inspector only scans machine images that your account owns. Amazon Inspector doesn't scan a machine image that is not owned by you. To scan a shared or public machine image, copy it into your own account first. Copying an image creates new snapshots in your account, and Amazon Inspector scans the copy. 

**Note**  
 Machine image scanning is available in the commercial AWS Regions. Continuous machine image scanning and on-demand machine image scans aren't available in the AWS GovCloud (US) Regions or the China Regions. For more information, see [Region-specific feature availability](inspector_regions.md#ins-regional-feature-availability). 

**Topics**
+ [Eligible machine images](#machine-image-eligible)
+ [Scan behaviors for machine image scanning](#machine-image-scan-behavior)
+ [Configuring machine image scanning](machine-image-scan-configuration.md)
+ [Running on-demand machine image scans with Amazon Inspector](machine-image-on-demand.md)

## Eligible machine images
<a name="machine-image-eligible"></a>

 Amazon Inspector scans a machine image if the image meets all of the following conditions: 
+  Your account owns the machine image and the Amazon EBS snapshots that back it. 
+  The machine image is backed by Amazon EBS and has a state of `available`. 
+  The machine image runs a supported operating system. For more information, see [Supported operating systems: machine image scanning](supported.md#supported-os-ami). 
+  The machine image runs a single operating system. Amazon Inspector doesn't support scanning machine images that contain multiple operating systems. 
+  The snapshots that back the machine image use one of the following file system formats: 
  + `ext3`
  + `ext4`
  + `ntfs`
  + `xfs`
**Note**  
 Amazon Inspector doesn't support Logical Volume Manager (LVM). If any snapshot that backs the machine image uses an LVM volume, Amazon Inspector can't scan the image and reports a scan status of `UNSUPPORTED_OS`. 
+  The machine image is within your scan eligibility windows, and it's in scope based on your scan mode and exclusion options. For more information, see [Configuring machine image scanning](machine-image-scan-configuration.md). 

**Note**  
 If Amazon Inspector can't scan a machine image, Amazon Inspector reports a terminal scan status for the image, such as `UNSUPPORTED_OS` or `STORAGE_LIMIT_EXCEEDED`. For more information, see [Scan status values for machine images](#machine-image-scan-status). 

## Scan behaviors for machine image scanning
<a name="machine-image-scan-behavior"></a>

 When you first activate machine image scanning, Amazon Inspector discovers the machine images that your account owns and scans the images that are within your scan eligibility windows. Amazon Inspector then continues to monitor each in-scope image. 

 Amazon Inspector initiates a new scan of a machine image in the following situations: 
+ Whenever you create, copy, or register a machine image.
+ Whenever you enable a machine image that Amazon Inspector hasn't previously scanned.
+ Whenever Amazon Inspector adds a new CVE item to its database, and that CVE is relevant to a machine image that's in scope.
+ Whenever you change your scan configuration in a way that brings a machine image into scope. For more information, see [How Amazon Inspector applies a configuration change](machine-image-scan-configuration.md#machine-image-reconciliation).

 Amazon Inspector keeps your scanning scope current by monitoring Amazon EC2 machine image lifecycle events. The following table describes how Amazon Inspector responds to each event. 


**How Amazon Inspector responds to Amazon EC2 machine image lifecycle events**  

| Event | Amazon Inspector behavior | 
| --- | --- | 
| CreateImage | Amazon Inspector scans the new machine image and all of the snapshots that back it. | 
| CopyImage | Amazon Inspector treats the copy as a new machine image and scans it, because copying an image creates new snapshots in your account. You can exclude copied images from scanning. For more information, see [Excluding copied and backup machine images](machine-image-scan-configuration.md#machine-image-exclusions). | 
| RegisterImage | Amazon Inspector treats the registered machine image as a new image and scans it, along with all of the snapshots that back it. | 
| EnableImage | If Amazon Inspector previously scanned the machine image, Amazon Inspector doesn't rescan it. Otherwise, Amazon Inspector treats the image as a new image and scans it. | 
| DisableImage | Amazon Inspector takes no action. Disabling a machine image only prevents Amazon EC2 from launching instances from it, and the image still exists in your account. | 
| DeregisterImage | Amazon Inspector removes the machine image from your scanning scope, because the image no longer exists in your account. | 
| Tag change events | Amazon Inspector re-evaluates the machine image against your scan mode. Depending on your scan mode, adding or removing the configured tag either brings the image into scope or removes it. For more information, see [Managing machine image scan mode](machine-image-scan-configuration.md#machine-image-scan-mode). | 

 You can check when Amazon Inspector last scanned a machine image for vulnerabilities from the **Machine images** tab on the **Account management** page, or by using the [ListCoverage](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCoverage.html) API operation. 

### Scan status values for machine images
<a name="machine-image-scan-status"></a>

 The following table lists the scan status values that Amazon Inspector reports for a machine image. 


**Machine image scan status values**  

| Status | Description | 
| --- | --- | 
| PENDING\_INITIAL\_SCAN | Amazon Inspector discovered the machine image and is collecting a software inventory from its snapshots. | 
| ACTIVE | Amazon Inspector scanned the machine image and continues to monitor it for new CVEs while the image remains in scope. | 
| ACCESS\_DENIED | Amazon Inspector couldn't access the machine image or the snapshots that back it. This can occur if a resource policy or a AWS KMS key policy prevents Amazon Inspector from reading the snapshot data. | 
| UNSUPPORTED\_OS | The operating system of the machine image isn't supported for scanning, or one or more of the snapshots that back the image uses a configuration that Amazon Inspector can't read, such as Logical Volume Manager (LVM). For more information, see [Supported operating systems: machine image scanning](supported.md#supported-os-ami). | 
| COLLECTION\_TIME\_LIMIT\_EXCEEDED | Amazon Inspector timed out while collecting the software inventory from the snapshots that back the machine image. | 
| STORAGE\_LIMIT\_EXCEEDED | The combined size of the snapshots that back the machine image exceeds the limit that Amazon Inspector supports for scanning. | 
| INTERNAL\_ERROR | Amazon Inspector encountered an internal error while scanning the machine image. Amazon Inspector retries the scan automatically. | 
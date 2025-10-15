# Reviewing bucket access using IAM Access Analyzer for S3

IAM Access Analyzer for S3 provides external access findings for your S3 general purpose buckets that are configured to allow access to anyone on the
 internet (public) or other AWS accounts, including AWS accounts outside of your organization. For
 each bucket that's shared publicly or with other AWS accounts, you receive findings into the source and level of shared access. 
 For example, IAM Access Analyzer for S3 might show that a bucket has read or write access
 provided through a bucket access control list (ACL), a bucket policy, a Multi-Region Access Point policy, or an access point
 policy. With these findings, you can take immediate and precise corrective action to
 restore your bucket access to what you intended. 

The Amazon S3 console presents an **External access summary** in the S3 console next to your list of general purpose buckets. 
 In the summary, you can click on the active findings for each AWS Region to see the details of the finding in
 the IAM Access Analyzer for S3 page. External acces findings in **External access summary** are automatically updated once every 24 hours.

When reviewing a bucket that allows public access, on the IAM Access Analyzer for S3 page, you can block all public access to the
 bucket with a single click. We recommend that you block all public access to your buckets unless
 you require public access to support a specific use case. Before you block all public
 access, ensure that your applications will continue to work correctly without public access.
 For more information, see [Blocking public access to your Amazon S3
 storage](access-control-block-public-access.md "access-control-block-public-access.md").

You can also drill down into bucket-level permission settings to configure granular levels
 of access. For specific and verified use cases that require public access, such as static
 website hosting, public downloads, or cross-account sharing, you can acknowledge and record
 your intent for the bucket to remain public or shared by archiving the findings for the
 bucket. You can revisit and modify these bucket configurations at any time. You can also
 download your findings as a CSV report for auditing purposes.

IAM Access Analyzer for S3 is available at no extra cost on the Amazon S3 console. IAM Access Analyzer for S3 is powered by
 AWS Identity and Access Management (IAM) IAM Access Analyzer. To use IAM Access Analyzer for S3 in the Amazon S3 console, you must visit the IAM
 console and create an external access analyzer on a per-Region basis.

For more information about IAM Access Analyzer, see [What is IAM Access Analyzer?](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html") in the
 *IAM User Guide*. For more information about IAM Access Analyzer for S3, review the
 following sections.

###### Important


* IAM Access Analyzer for S3 requires an account-level analyzer in each AWS Region where you have buckets. To use IAM Access Analyzer for S3, you must visit
 IAM Access Analyzer and create an analyzer that has an account as the zone of trust.
 For more information, see [Enabling IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#access-analyzer-enabling "https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#access-analyzer-enabling") in *IAM User Guide*.
* IAM Access Analyzer for S3 doesn't analyze the access point policy that's attached to cross-account access points. This
 behavior occurs because the access point and its policy are outside the zone of
 trust, that is, the account. Buckets that delegate access to a cross-account access point are
 listed under **Buckets with public access** if you haven't
 applied the `RestrictPublicBuckets` block public access setting to
 the bucket or account. When you apply the `RestrictPublicBuckets`
 block public access setting, the bucket is reported under **Buckets with
 access from other AWS accounts — including third-party
 AWS accounts**.
* When a bucket policy or bucket ACL is added or modified, IAM Access Analyzer generates and
 updates findings based on the change within 30 minutes. Findings related to
 account level block public access settings might not be generated or updated for
 up to 6 hours after you change the settings. Findings related to Multi-Region Access Points might
 not be generated or updated for up to six hours after the Multi-Region Access Point is created,
 deleted, or you change its policy.
###### Topics

* [Reviewing a global summary of policies that grant external access to buckets](#external-access-summary "#external-access-summary")
* [Information provided by IAM Access Analyzer for S3](#access-analyzer-information-s3 "#access-analyzer-information-s3")
* [Blocking all public
 access](#blocking-public-access-access-analyzer "#blocking-public-access-access-analyzer")
* [Reviewing and changing bucket access](#changing-bucket-access "#changing-bucket-access")
* [Archiving bucket findings](#archiving-buckets "#archiving-buckets")
* [Activating an archived bucket finding](#activating-buckets "#activating-buckets")
* [Viewing finding details](#viewing-finding-details "#viewing-finding-details")
* [Downloading an IAM Access Analyzer for S3 report](#downloading-bucket-report-s3 "#downloading-bucket-report-s3")

## Reviewing a global summary of policies that grant external access to buckets


You can use the **External access summary** to view a global summary of policies that grant external access to buckets across your 
 AWS account directly from the S3 console. This summary helps you identify Amazon S3 general purpose buckets in any AWS Region that allow public access or access from 
 other AWS accounts without needing to inspect policies in each AWS Region individually.


### Enabling external access summary and IAM Access Analyzer for S3


To use the **External access summary** and IAM Access Analyzer for S3, you must complete the following prerequisite steps.


1. Grant the required permissions. For more information, see [Permissions Required to use IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#access-analyzer-permissions "https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#access-analyzer-permissions") in the
 *IAM User Guide*.
2. Visit IAM to create an account-level analyzer for each Region where you want to use IAM Access Analyzer.


You can do this by creating an analyzer that has an account as the zone of trust in the IAM console or by using the AWS CLI or AWS SDKs. For more 
 information, see [Enabling IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#access-analyzer-enabling "https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#access-analyzer-enabling") in *IAM User Guide*.

### Viewing buckets that allow external access


The **External access summary** displays findings and errors for external access that are provided by IAM Access Analyzer for S3 for general purpose buckets. 
 Archived findings and findings for unused access are not included in the summary but can be viewed in the IAM console or IAM Access Analyzer for S3. For more information, see [View the IAM Access Analyzer findings dashboard](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-dashboard.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-dashboard.html") in the IAM User Guide.


###### Note

The **External access summary** only includes findings for external access analyzers for each of your AWS accounts, not your AWS Organization.


1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation panel, choose **General purpose buckets**.
3. Expand the **External access summary**. The console displays active public and cross-account access findings.


###### Note

If S3 experiences an issue loading bucket details, refresh the general purpose buckets list or view findings in IAM Access Analyzer for S3. For more information, see [Reviewing bucket access using IAM Access Analyzer for S3](access-analyzer.md "access-analyzer.md").
4. To view a list of findings or errors for an AWS Region, choose the link to the Region. The IAM Access Analyzer for S3 page displays names of buckets that can be accessed publicly 
 or by other AWS accounts. For more information, see [Information provided by IAM Access Analyzer for S3](#access-analyzer-information-s3 "#access-analyzer-information-s3").

### Updating access controls for buckets that allow external access


1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation panel, choose **General purpose buckets**.
3. Expand the **External access summary**. The console displays active findings for buckets that can be accessed publicly or by other AWS accounts.


###### Note

If S3 experiences an issue loading bucket details, refresh the general purpose buckets list or view findings in IAM Access Analyzer for S3. For more information, see [Reviewing bucket access using IAM Access Analyzer for S3](access-analyzer.md "access-analyzer.md").
4. To view a list of findings or errors for an AWS Region, choose the link to the Region. The IAM Access Analyzer for S3 displays active findings for buckets that can be accessed publicly or by other AWS accounts.


###### Note

External acces findings in **External access summary** are automatically updated once every 24 hours.
5. To block all public access for a bucket, see [Blocking all public
 access](#blocking-public-access-access-analyzer "#blocking-public-access-access-analyzer"). 
 To change the bucket access, see [Reviewing and changing bucket access](#changing-bucket-access "#changing-bucket-access").

## Information provided by IAM Access Analyzer for S3


IAM Access Analyzer for S3 provides findings for buckets that can be accessed outside your AWS account. Buckets that are listed under **Public access findings**
 can be accessed by anyone on the internet. If IAM Access Analyzer for S3 identifies public buckets, you
 also see a warning at the top of the page that shows you the number of public buckets in
 your Region. Buckets listed under **Cross-account access findings** are shared
 conditionally with other AWS accounts, including accounts outside of your
 organization. 


For each bucket, IAM Access Analyzer for S3 provides the following information:



* **Bucket name**
* **Shared through** ‐ How the bucket is
 shared—through a bucket policy, a bucket ACL, a Multi-Region Access Point policy, or an access point
 policy. Multi-Region Access Points and cross-account access points are reflected under access points. A bucket can be
 shared through both policies and ACLs. If you want to find and review the source
 for your bucket access, you can use the information in this column as a starting
 point for taking immediate and precise corrective action.
* **Status** ‐ The status of the bucket
 finding. IAM Access Analyzer for S3 displays findings for all public and shared buckets. 




	+ **Active** ‐ Finding has not been
	 reviewed.
	+ **Archived** ‐ Finding has been
	 reviewed and confirmed as intended.
	+ **All** ‐ All findings for buckets
	 that are public or shared with other AWS accounts, including AWS accounts outside of your organization.
* **Access level** ‐ Access permissions
 granted for the bucket:




	+ **List** ‐ List resources.
	+ **Read** ‐ Read but not edit
	 resource contents and attributes.
	+ **Write** ‐ Create, delete, or
	 modify resources.
	+ **Permissions** ‐ Grant or modify
	 resource permissions.
	+ **Tagging** ‐ Update tags associated
	 with the resource.
* **External principal** ‐ The AWS account outside of your organization with access to the bucket.
* **Resources control policy (RCP) restriction** ‐ The resource control policy (RCP) that applies to the bucket, if applicable. 
 For more information, see [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html").

## Blocking all public
 access


If you want to block all access to a bucket in a single click, you can use the
 **Block all public access** button in IAM Access Analyzer for S3. When you block all
 public access to a bucket, no public access is granted. We recommend that you block all
 public access to your buckets unless you require public access to support a specific and
 verified use case. Before you block all public access, ensure that your applications
 will continue to work correctly without public access.


If you don't want to block all public access to your bucket, you can edit your block
 public access settings on the Amazon S3 console to configure granular levels of access to
 your buckets. For more information, see [Blocking public access to your Amazon S3
 storage](access-control-block-public-access.md "access-control-block-public-access.md").


In rare cases, IAM Access Analyzer for S3 and Amazon S3 block public access evaluation might differ on
 whether a bucket is public. This behavior occurs because Amazon S3 block public access
 performs validation on the existence of actions in addition to evaluating public access.
 Suppose that the bucket policy contains an `Action` statement that allows
 public access for an action that isn't supported by Amazon S3 (for example,
 `s3:NotASupportedAction`). In this case, Amazon S3 block public access
 evaluates the bucket as public because such a statement could potentially make the
 bucket public if the action later becomes supported. In cases where Amazon S3 block public
 access and IAM Access Analyzer for S3 differ in their evaluations, we recommend reviewing the bucket
 policy and removing any unsupported actions.


###### To block all public access to a bucket using IAM Access Analyzer for S3

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane on the left, under **Dashboards**,
 choose **Access analyzer for S3**.
3. In IAM Access Analyzer for S3, choose a bucket.
4. Choose **Block all public access**.
5. To confirm your intent to block all public access to the bucket, in
 **Block all public access (bucket settings)**, enter
 `confirm`.


Amazon S3 blocks all public access to your bucket. The status of the bucket finding
 updates to **resolved**, and the bucket disappears from the
 IAM Access Analyzer for S3 listing. If you want to review resolved buckets, open IAM Access Analyzer on
 the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

## Reviewing and changing bucket access


If you did not intend to grant access to the public or other AWS accounts, including
 accounts outside of your organization, you can modify the bucket ACL, bucket policy, the
 Multi-Region Access Point policy, or the access point policy to remove the access to the bucket. The
 **Shared through** column shows all sources of bucket access:
 bucket policy, bucket ACL, and/or access point policy. Multi-Region Access Points and cross-account access points are reflected
 under access points.


###### To review and change a bucket policy, a bucket ACL, a Multi-Region Access Point, or an access point
 policy

1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Access analyzer for
 S3**.
3. To see whether public access or shared access is granted through a bucket
 policy, a bucket ACL, a Multi-Region Access Point policy, or an access point policy, look in the **Shared
 through** column.
4. Under **Buckets**, choose the name of the bucket with the
 bucket policy, bucket ACL, Multi-Region Access Point policy, or access point policy that you want to change or
 review.
5. If you want to change or view a bucket ACL:


	1. Choose **Permissions**.
	2. Choose **Access Control List**.
	3. Review your bucket ACL, and make changes as required.
	
	
	For more information, see [Configuring ACLs](managing-acls.md "managing-acls.md").
6. If you want to change or review a bucket policy:


	1. Choose **Permissions**.
	2. Choose **Bucket Policy**.
	3. Review or change your bucket policy as required.
	
	
	For more information, see [Adding a bucket policy by using the Amazon S3 console](add-bucket-policy.md "add-bucket-policy.md").
7. If you want to change or view a Multi-Region Access Point policy:


	1. Choose **Multi-Region Access Point**.
	2. Choose the Multi-Region Access Point name.
	3. Review or change your Multi-Region Access Point policy as required.
	
	
	For more information, see [Permissions](MultiRegionAccessPointPermissions.md "MultiRegionAccessPointPermissions.md").
8. If you want to review or change an access point policy:


	1. Choose **Access Points for general purpose buckets** or **Access Points for directory buckets**.
	2. Choose the access point name.
	3. Review or change access as required. 
	
	
	For more information, see [Managing your Amazon S3 access points for general purpose buckets](access-points-manage.md "access-points-manage.md").If you edit or remove a bucket ACL, a bucket policy, or an access point policy
 to remove public or shared access, the status for the bucket findings updates to
 resolved. The resolved bucket findings disappear from the IAM Access Analyzer for S3 listing, but
 you can view them in IAM Access Analyzer.

## Archiving bucket findings


If a bucket grants access to the public or other AWS accounts, including accounts
 outside of your organization, to support a specific use case (for example, a static
 website, public downloads, or cross-account sharing), you can archive the finding for
 the bucket. When you archive bucket findings, you acknowledge and record your intent for
 the bucket to remain public or shared. Archived bucket findings remain in your IAM Access Analyzer for S3
 listing so that you always know which buckets are public or shared.


###### To archive bucket findings in IAM Access Analyzer for S3

1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **IAM Access Analyzer for S3**.
3. In IAM Access Analyzer for S3, choose an active bucket.
4. To acknowledge your intent for this bucket to be accessed by the public or
 other AWS accounts, including accounts outside of your organization, choose
 **Archive**.
5. Enter `confirm`, and choose
 **Archive**.

## Activating an archived bucket finding


After you archive findings, you can always revisit them and change their status back
 to active, indicating that the bucket requires another review. 


###### To activate an archived bucket finding in IAM Access Analyzer for S3

1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Access analyzer for
 S3**.
3. Choose the archived bucket findings.
4. Choose **Mark as active**.

## Viewing finding details


If you need to see more information about a finding, you can open the bucket finding
 details in IAM Access Analyzer on the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").


###### To view finding details in IAM Access Analyzer for S3

1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Access analyzer for
 S3**.
3. In IAM Access Analyzer for S3, choose a bucket.
4. Choose **View details**.


The finding details open in IAM Access Analyzer on the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

## Downloading an IAM Access Analyzer for S3 report


You can download your bucket findings as a CSV report that you can use for auditing
 purposes. The report includes the same information that you see in IAM Access Analyzer for S3 on the Amazon S3
 console.


###### To download a report

1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane on the left, choose **Access analyzer for
 S3**.
3. In the Region filter, choose the Region.


IAM Access Analyzer for S3 updates to shows buckets for the chosen Region.
4. Choose **Download report**.


A CSV report is generated and saved to your computer.

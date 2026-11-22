

# Grant access to Resolutions

 **Resolutions** appears in the Connect Customer admin website navigation only for users whose security profile includes Work plan permissions. Grant access to the operations managers who own your standard operating procedures (SOPs) and will author Work plans. 

## Assign the AWS managed security profile (recommended)
<a name="resolutions-grant-access-assign-the-aws-managed-security-profile-recommended"></a>

 Your instance includes an AWS managed security profile that has the permissions needed to author Work plans. Because AWS manages the profile, it stays aligned with Resolutions as new permissions are added. A profile that you build by hand can fall behind. 

**To assign the security profile**

1.  In the Connect Customer admin website, choose **Users**, and then choose **User management**. 

1. Select the user.

1.  Assign the **ResolutionsUser** security profile, and then choose **Save**. 

 After you save, **Resolutions** appears in the navigation pane for that person. 

## Build a custom security profile
<a name="resolutions-grant-access-build-a-custom-security-profile"></a>

 If your organization requires a custom profile, for example to combine authoring with other duties or to narrow access, grant the following permissions. 


| Permission group | Permissions | 
| --- | --- | 
| Work plans | View, Create, Edit, Publish, Delete | 
| Contact flows | View, Create, Edit, Publish, Delete | 
| Contact flow modules | View | 
| Task templates | View, Create, Edit, Delete | 
| Case fields | View, Create, Edit | 
| Case templates | View, Create, Edit | 
| Information extraction, definitions | View, Create, Edit, Delete | 
| Information extraction, results | View | 
| Queues | View, Create, Edit, Enable and disable | 
| Connect assistant | View | 
| Metrics | Access metrics | 

 Resolutions creates flows, flow modules, Task templates, Case fields, Case templates, and information extraction definitions on the author's behalf when it generates a Work plan. If the author's profile is missing any of these permissions, generation fails partway through. 

 For more information about security profiles, see [Security profiles for Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html). 

## Grant Cases permissions to specialists
<a name="resolutions-grant-access-grant-cases-permissions-to-specialists"></a>

 Work plan authors need nothing extra for Cases. The AWS managed profile already includes the Case field and Case template permissions that authoring requires. 

 Specialists who work on the Resolutions Cases that a Work plan creates need Cases permissions on their own security profile. 
+  At minimum, **View** and **Edit** on Cases. 
+  Customer Profiles permissions, because every Case is linked to a customer profile. 
+  **View** on queues, quick connects, and users, so that Case ownership and comment authors display correctly. 

 For more information, see [Security profile permissions for Cases](assign-security-profile-cases.md). 

## Verify access
<a name="resolutions-grant-access-verify-access"></a>

 Sign in as a user who has the profile and confirm that **Resolutions** appears in the navigation. If it doesn't, check the Work plans permissions first. Those permissions control the navigation entry. 
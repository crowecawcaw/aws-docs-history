

# Manage Work plans and versions

 The **Resolutions** page lists every Work plan on your instance with its description, the number of Case templates it's associated with, and its creation date. Choose a Work plan to open it. 

## Work plan page
<a name="resolutions-manage-work-plans-work-plan-page"></a>

 The Work plan page shows one version at a time. Choose a version from the **Work plan version** list. The page has two tabs. 
+  **Version details** shows an overview of the version, its Phases and Steps, and the Case fields it uses. 
+  **Associated templates** lists the Case templates that use this version. 

### Overview
<a name="resolutions-manage-work-plans-overview"></a>

 The **Overview** section of the **Version details** tab shows the following. 


| Field | Description | 
| --- | --- | 
| Version name |  The version, such as V1. The Default label marks the default version.  | 
| Status | Published after you publish the version. | 
| Source version | The version this one was cloned from, if any. | 
| Work plan flow | The flow that runs the version's Phases and Steps. | 
| Information extraction flow |  The flow that extracts data from customer messages into Case fields. Add this flow to your inbound contact flow.  | 
| Version ARN | The Amazon Resource Name of the version. | 

### Case fields
<a name="resolutions-manage-work-plans-case-fields"></a>

 The **Version details** tab also lists the Case fields that the version uses. 

![The Case fields section lists 21 fields, such as applicantId and approvedLoanAmount, each of type Text in the Custom namespace.](https://docs.aws.amazon.com/connect/latest/adminguide/images/resolutions-case-fields.png)


## Versions
<a name="resolutions-manage-work-plans-versions"></a>

 Each time you publish, Resolutions creates an immutable version. You can't change a published version's configuration. 

**To change a published Work plan**

1. Open the Work plan and choose the version to start from.

1.  Choose **Work plan version actions**, and then clone the version. 

1.  Make your changes on the configuration page, generate flows, and publish. 

1.  Update your inbound contact flow to transfer to the new version's information extraction flow. See [When you publish a new version](resolutions-start-work-plan.md#resolutions-start-work-plan-when-you-publish-a-new-version). 

 A version can be associated with more than one Case template. A Case template is associated with at most one version at a time. For how this affects the version that a Resolutions Case runs, see [Which Work plan version a Resolutions Case runs](resolutions-start-work-plan.md#resolutions-start-work-plan-which-work-plan-version-a-resolutions-case-runs). 

## Analytics
<a name="resolutions-manage-work-plans-analytics"></a>

 After you publish, choose **View analytics** to monitor Resolutions Case progress through the Work plan. Resolutions reports progress by Phase. 

## Delete a Work plan
<a name="resolutions-manage-work-plans-delete-a-work-plan"></a>

 To delete a Work plan, choose **Work plan actions**, and then choose the delete option. 
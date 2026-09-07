

# Service context checklist
<a name="service-context-checklist"></a>

We recommend that you work through this checklist to prepare the service context prior to running your Government Lens review in AWS Well-Architected Tool. The review is performed in your AWS account so that you can record it as a milestone, save it, and use it to track your remediations and progress after the review. The completion of the review produces a detailed report and it's up to you to assess and perform risk remediation activities. 


|  | ID | Priority | Service Context | 
| --- | --- | --- | --- | 
| ☐ | C1 | Required | Clearly identify the service or system you want to review, which might include one or more end-user facing process flows. The term *service* is used in this context throughout the Government Lens review.  | 
| ☐ | C2 | Recommended | AWS recommends that all individual process flows have a review using the Well-Architected Framework lens prior to running a Government Lens review of the *service* as a whole. This helps verify that the individual flows meet the AWS best technical practices, which are then complemented by the service review done against the government context. | 
| ☐ | C3 | Required | Schedule at least three hours for the Gov Lens review (which could be spread over 2–3 shorter sessions, if desired). Invite the relevant AWS account executive and the customer product owners to participate in the entire Government Lens review session. | 
| ☐ | C4 | Recommended |  +  Enterprise risk representatives —for the last operational excellence pillar question, and the security and reliability pillar questions. <br />+  Security personnel —for the security and reliability pillar questions. <br />+  Relevant policy and program owners, frontline staff representatives (who understand the context of end users), and business and policy owners —for the reliability pillar and service outcomes for government questions.   | 

## Using the Government Lens in AWS WA Tool
<a name="using-the-government-lens"></a>

A common request from our customers has been to enable them to run a *self service* Government Lens review in the AWS Well-Architected Tool (AWS WA Tool). 

The Government Lens is available as a custom lens for the [AWS Well-Architected Tool](https://console.aws.amazon.com/wellarchitected/) in the AWS Management Console. Custom lenses, such as the Government Lens, are defined in a JSON file and allow you to tailor your workload reviews to particular technologies, help you meet governance needs, and extend the guidance already provided by the Well-Architected Framework and the AWS lenses.

**To add the Government Lens to the AWS Well-Architected Tool:**

1. Download the Government Lens JSON file provided by your Technical Account Manager (TAM), Solutions Architect (SA), or Support. This file is used in Step 5.

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.

1. Choose **Create custom lens**.

1. Choose **Choose file** and select the JSON file you downloaded in Step 1.

1. (Optional) In the **Tags** section, add any tags you want to associate with the Government Lens.

1. Choose **Submit & Preview** to preview the Government Lens, or **Submit** to create the lens without previewing.

   If you choose to **Submit & Preview**, you can select **Next** to navigate through the Government Lens preview, or select **Exit Preview** to go back to **Custom lenses**.

1. Select the Government Lens and choose **Publish lens**.

1. In the **Version name** box, enter a unique identifier for the version change. This value can be up to 32 characters and must only contain alphanumeric characters and periods (".").

1. Choose **Publish custom lens**.

   After the Government Lens has been published, it's in **PUBLISHED** status.

The Government Lens can now be applied to workloads in your AWS account, and shared with other AWS accounts and users. If your account is managed by AWS Organizations, you can share the lens with all accounts in the organization or in an OU without having to enumerate each account.

As you work through the service context checklist, risks can be identified and comments can be captured. A workload report is available in PDF format for sharing with stakeholders to document risks and future recommendations. Open risks can be managed and assigned in the tool and periodic milestone reviews can be performed.

For more information on using the AWS WA Tool, custom lenses, reports, and the risk dashboard, see the [AWS Well-Architected Tool User Guide](https://docs.aws.amazon.com/wellarchitected/latest/userguide/getting-started.html).
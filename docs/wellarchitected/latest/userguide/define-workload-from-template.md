# Defining a workload from a template in AWS WA Tool

You can define a workload from a review template that you created or a review template
that has been shared with you. You cannot define a new workload from a review template
that has been deleted, and if the review template contains an outdated version of a
lens, you must upgrade the review template before you can define a new workload from it.
For information on how to upgrade a review template, see [Upgrading a lens in AWS WA Tool](lenses-upgrading.md "lenses-upgrading.md").

###### Note

To define a workload from a review template, you must have IAM permissions to create a
workload enabled:`wellarchitected:CreateWorkload`, as well as the
following review template permissions:
`wellarchitected:GetReviewTemplate`,
`wellarchitected:GetReviewTemplateAnswer`,
`wellarchitected:ListReviewTemplateAnswers`, and
`wellarchitected:GetReviewTemplateLensReview`. For more information
about IAM permissions, see the [AWS Identity and Access Management User Guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").

###### To define a workload from a review template

1. Select **Review templates** in the left navigation pane.
2. Select the name of the review template you want to define a workload from.
3. Choose **Define workload from template**.

###### Note

You can also choose **Define from review template** from the **Define workload** dropdown on the **Workloads** page. 4. On the **Select review template** step, select the review template card, and choose **Next**. 5. On the **Specify properties** step, fill out required fields for the workload
properties, and choose **Next**. For more detail, see [Defining a workload in AWS WA Tool](define-workload.md "define-workload.md"). 6. (Optional) On the **Apply Profile** step, associate a
profile with the workload by selecting an existing profile, searching
for the profile name, or choosing **Create profile** to [create a profile](creating-a-profile.md "creating-a-profile.md"). Choose
**Next**.

[Well-Architected profiles](profiles.md "profiles.md") and review templates
can be used in tandem. The questions that are pre-filled in your review template
remain answered in the workload, and the questions are prioritized based on your
profile. 7. (Optional) On the **Apply lenses** step, you may choose to apply additional lenses from **Custom lenses** or **Lens catalog** that were not already applied to the review template. 8. Choose **Define workload**.

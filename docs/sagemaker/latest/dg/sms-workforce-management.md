

# Workforces
<a name="sms-workforce-management"></a>

**Amazon Mechanical Turk service closure**  
Amazon Mechanical Turk will permanently close on September 30, 2026. If you currently use the MTurk workforce option, we recommend that you review your affected workflows and transition to an alternative workforce option before September 30, 2026.

A *workforce* is the group of workers that you have selected to label your dataset. You can choose either the Amazon Mechanical Turk workforce, a vendor-managed workforce, or you can create your own private workforce to label or review your dataset. Whichever workforce type you choose, Amazon SageMaker AI takes care of sending tasks to workers. 

When you use a private workforce, you also create *work teams*, a group of workers from your workforce that are assigned to specific *jobs*— [Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html) labeling jobs or [Amazon Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html) human review tasks. You can have multiple work teams and can assign one or more work teams to each job.

You can use Amazon Cognito or your own private OpenID Connect (OIDC) Identity Provider (IdP) to manage your private workforce and work teams. For more information about the permissions required to manage your workforce this way, see [Permissions required to use the Amazon SageMaker Ground Truth console](security_iam_id-based-policy-examples.md#groundtruth-console-policy).

**Topics**
+ [Using the Amazon Mechanical Turk Workforce](sms-workforce-management-public.md)
+ [Subscribe to vendor workforces](sms-workforce-management-vendor.md)
+ [Private workforce](sms-workforce-private.md)
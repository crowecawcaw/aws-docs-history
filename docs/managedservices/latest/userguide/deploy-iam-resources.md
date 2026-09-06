

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Deploying IAM resources in AMS Advanced
<a name="deploy-iam-resources"></a>

AMS deploys IAM resources in your multi-account landing zone (MALZ) Application and single-account landing zone (SALZ) accounts in two ways:
+ Automated IAM Provisioning: This capability in AMS lets you submit create, update, or delete change types for IAM role or policy provisioning, without operator review, and with IAM and AMS validation checks run automatically.

  This capability must be explicitly enabled with the Management \| Managed account \| AMS Automated IAM Provisioning with read-write permissions \| [Enable (managed automation)](https://docs.aws.amazon.com/managedservices/latest/ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-enable-review-required.html) change type (ct-1706xvvk6j9hf). To learn more, see [Automated IAM Provisioning AMS](auto-iam-provisioning.md). After AMS Automated IAM Provisioning is enabled, you have access to Create, Update, and Delete change types to manage your IAM resources.
+ managed automation IAM change type: This change type, Deployment \| Advanced stack components \| Identity and Access Management (IAM) \| [Create entity or policy (managed automation)](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-advanced-identity-and-access-management-iam-create-entity-or-policy-review-required.html) (ct-3dpd8mdd9jn1r), requires an AMS operator review, which can sometimes take a few days to complete if clarifications are needed.

**Note**  
Whichever method is used, an IAM role is provisioned to the relevant account or accounts and, after the role is provisioned, you must onboard the role in your federation solution.
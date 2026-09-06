

# Customization triggers
<a name="aft-customization-triggers"></a>

Account Factory for Terraform (AFT) customization triggers automate the re-execution of account and global customizations when accounts move between organizational units (OUs). As your organization evolves, accounts frequently transition between OUs to reflect changes in team ownership, compliance requirements, or workload classification. Without customization triggers, each move requires manual intervention to re-apply the customizations that align with the account's new organizational context.

With customization triggers enabled, AFT detects OU changes and automatically invokes your customization pipelines for the affected accounts. This ensures that accounts always run the customizations appropriate to their current OU placement, reducing operational overhead and minimizing the risk of configuration drift. For example, when an account moves from a Development OU to a Production OU, customization triggers can automatically apply production-specific security controls and compliance policies without manual intervention.

**Important**  
Accounts updated through the Auto Enroll feature in AWS Control Tower landing zone do not emit the `UpdateManagedAccount` lifecycle event. Customization triggers do not fire for those operations. If you rely on Auto Enroll to bring accounts under AWS Control Tower management, you must re-invoke customizations manually for those accounts.
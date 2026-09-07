

# Best Practice 4.2 – Regularly perform patch management for software currency
<a name="best-practice-4-2"></a>

Perform regular patch management to gain features, address issues, and remain compliant with governance. Consider patches at the operating system, database and SAP application layer. Understand whether your patching process will be to patch your existing servers, or provision and patch a new server. Automate patch management to reduce errors caused by manual processes, reduce the level of effort to patch and reduce the application downtime required for major SAP, database, and kernel patching.

 **Suggestion 4.2.1 - Implement SAP patch management procedures to regularly review SAP Security Notes and newly released patches** 

Consider patches at the operating system, database and SAP application layer.
+  AWS Documentation: [AWS Security Bulletins](https://aws.amazon.com/security/security-bulletins/?card-body.sort-by=item.additionalFields.bulletinDateSort&card-body.sort-order=desc) 
+  SAP Documentation: [SAP EarlyWatch Alert](https://support.sap.com/en/offerings-programs/support-services/earlywatch-alert.html) 
+  SAP Documentation: [SAP Security News](https://support.sap.com/en/my-support/knowledge-base/security-notes-news.html) 


| Operating System | Guidance | 
| --- | --- | 
| SUSE Linux Enterprise Server |  [SUSE Update Advisories](https://www.suse.com/support/update/)  | 
| Red Hat Enterprise Linux |  [Red Hat Security Advisories](https://access.redhat.com/security/security-updates/#/)[Red Hat Customer Portal](https://access.redhat.com/articles/amazon-web-services-access) (Sign in with AWS)  | 
| Microsoft Windows |  [Microsoft Security Alerts](https://www.microsoft.com/en-us/msrc/technical-security-notifications)  | 
| Oracle Enterprise Linux |  [Oracle Security Alerts](https://www.oracle.com/security-alerts/)  | 

 For further discussion on this item see [Security]: [Best Practice 6.2 - Build and protect the operating system](best-practice-6-2.md). 

 **Suggestion 4.2.2 - Consider automated tools to align and automate patches across your SAP landscape** 

 Tools such as AWS Systems Manager and OpsWorks can assist you to align, plan, test, and deploy patching across your SAP workload. Consider an automated approach to patching to minimize effort and maintenance windows.
+  AWS Documentation: [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html?ref=wellarchitected) 
+  SAP Lens [Security]: [Best Practice 6.2 - Build and protect the operating system.](best-practice-6-2.md) 
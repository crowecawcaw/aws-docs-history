# Security best practices for AWS CloudShell

The following best practices are general guidelines and don’t represent a complete security
 solution. Because these best practices might not be appropriate or sufficient for your
 environment, we recommend
 that you treat them as helpful considerations instead of prescriptions.


###### Some security best practices for AWS CloudShell


* Use IAM permissions and policies to control access to AWS CloudShell and ensure users can perform
 only those actions
 (for example,
 downloading and uploading
 files)
 required by their role. For more information, see
 
 [Managing AWS CloudShell access and usage with IAM
 policies](sec-auth-with-identities.md "sec-auth-with-identities.md").
* Don't include sensitive data in your IAM entities such as users, roles, or session
 names.
* Keep Safe Paste feature enabled to catch potential security risks in text you've copied from
 external sources. Safe Paste is enabled by default. For more
 information about
 using safe paste for multiline text, see [Using Safe Paste
 for multiline text](customizing-cshell.md#safe-paste-enable "customizing-cshell.md#safe-paste-enable").
* Be familiar with the [Shared Security Responsibility Model](https://docs.aws.amazon.com/whitepapers/latest/aws-overview-security-processes/shared-security-responsibility-model.html "https://docs.aws.amazon.com/whitepapers/latest/aws-overview-security-processes/shared-security-responsibility-model.html")  if you
 install
 third-party applications to the compute environment of AWS CloudShell.
* Prepare rollback mechanisms before editing shell scripts that affect the user's shell
 experience. For more
 information about
 modifying the default shell environment, see [Modifying your
 shell with scripts](vm-specs.md#modifying-shell-scripts "vm-specs.md#modifying-shell-scripts").
* Store your code securely in a version control
 system.

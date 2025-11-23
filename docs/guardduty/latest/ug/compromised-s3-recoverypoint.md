# Remediating a potentially compromised S3 Recovery Point

When GuardDuty generates an Execution:S3/MaliciousFile!RecoveryPoint finding type, it indicates that malware has
been detected in an S3 Recovery Point Backup resource. Perform the following steps to remediate the potentially compromised recovery point:

1. **Identify the potentially compromised S3 Recovery Point**
   1. A GuardDuty finding for S3 recovery points will list the affected recovery point ARN, backup vault name, and associated malware scan details in the finding details.
   2. Review recovery point details:

   ```
   aws backup describe-recovery-point --backup-vault-name `021345abcdef6789` --recovery-point-arn `arn:aws:backup:us-east-1:123456789012:recovery-point:abcdef01234567890`
   ```

2. **Restrict access to the compromised resources**
   - Review and modify backup vault access policies to restrict recovery point access and suspend any automated restore jobs that might use this recovery point.
     If your environment uses resource tagging, tag the recovery point appropriately to indicate it's under investigation and consider pausing scheduled backups if necessary.

   Example:

   ```
   aws backup tag-resource —resource-arn `arn:aws:backup:us-east-1:111122223333:recovery-point:abcdef01234567890` —tags `Investigation=Malware,DoNotDelete=True`
   ```

   For additional details see: [tag-resource CLI Command Reference](../../../cli/latest/reference/backup/tag-resource.md "../../../cli/latest/reference/backup/tag-resource.md")

3. **Take remediation action**
   - Before proceeding with deletion, ensure you have identified all dependencies and have proper backups if needed.

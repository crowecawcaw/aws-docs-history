# Remediating a potentially compromised EC2 Recovery Point

When GuardDuty generates an Execution:EC2/MaliciousFile!RecoveryPoint finding type, it indicates that malware has
been detected in an EC2 Recovery Point Backup resource. Perform the following steps to remediate the potentially compromised recovery point:

1. **Identify the potentially compromised EC2 Recovery Point**
   1. A GuardDuty finding for EC2 Recovery Point will list its Amazon Resource Name (ARN), and associated malware scan details in the finding details:

   ```
   aws backup describe-recovery-point --backup-vault-name `021345abcdef6789` --recovery-point-arn "`arn:aws:backup:us-east-1:111122223333:recovery-point:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
   ```

   2. Review recovery details to look for source image:

   ```
   aws backup get-recovery-point-restore-metadata --backup-vault-name `021345abcdef6789` --recovery-point-arn "`arn:aws:backup:us-east-1:111122223333:recovery-point:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
   ```

2. **Restrict access to the compromised resources**
   - Review and modify backup vault access policies to restrict recovery point access and suspend any automated restore jobs that might use this recovery point. If your environment uses resource tagging, tag the recovery point appropriately to indicate it's under investigation and consider pausing scheduled backups if necessary.

   Example:

   `aws backup tag-resource -—resource-arn arn:aws:backup:us-east-1:111122223333:recovery-point:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 -—tags Investigation=Malware,DoNotDelete=True`

3. **Take remediation action**
   - Before proceeding with deletion, ensure you have identified all dependencies and have proper backups if needed.

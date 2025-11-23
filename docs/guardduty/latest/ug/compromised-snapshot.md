# Remediating a potentially compromised EBS Snapshot

When GuardDuty generates an Execution:EC2/MaliciousFile!Snapshot finding type, it indicates that malware has
been detected in an Amazon EBS snapshot. Perform the following steps to remediate the potentially compromised snapshot:

1. **Identify the potentially compromised snapshot**
   1. Identify the potentially compromised snapshot.
      A GuardDuty finding for an EBS snapshot will list the affected snapshot ID, its Amazon Resource Name (ARN),
      and associated malware scan details in the finding details.
   2. Review recovery point details using the following command:

   ```
   aws backup describe-recovery-point —backup-vault-name `021345abcdef6789` —recovery-point-arn `"arn:aws:ec2:us-east-1::snapshot/snap-abcdef01234567890"`
   ```

2. **Restrict access the compromised snapshot**

Review and modify backup vault access policies to restrict recovery point access and suspend any automated restore jobs that might use this snapshot.

    1. Review current sharing permissions:


    ```
    aws ec2 describe-snapshot-attribute --snapshot-id `snap-abcdef01234567890` --attribute createVolumePermission
    ```
    2. Remove specific account access:


    ```
    aws ec2 modify-snapshot-attribute --snapshot-id `snap-abcdef01234567890` --attribute createVolumePermission --operation-type remove --user-ids `111122223333`
    ```
    3. For additional CLI options, see [modify-snapshot-attribute CLI documentation](../../../cli/latest/reference/ec2/modify-snapshot-attribute.md "../../../cli/latest/reference/ec2/modify-snapshot-attribute.md").

3. **Take remediation action**
   - Before proceeding with deletion, ensure you have identified all dependencies and have proper backups if needed.

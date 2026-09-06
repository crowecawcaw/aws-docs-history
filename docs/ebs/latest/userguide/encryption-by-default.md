

# Enable Amazon EBS encryption by default
<a name="encryption-by-default"></a>

You can configure your AWS account to enforce the encryption of the new EBS volumes and snapshot copies that you create. For example, Amazon EBS encrypts the EBS volumes created when you launch an instance and the snapshots that you copy from an unencrypted snapshot. For examples of transitioning from unencrypted to encrypted EBS resources, see [Encrypt unencrypted resources](ebs-encryption.md#encrypt-unencrypted).

Encryption by default has no effect on existing EBS volumes or snapshots.

**Considerations**
+ Encryption by default is a Region-specific setting. If you enable it for a Region, you cannot disable it for individual volumes or snapshots in that Region.
+ Amazon EBS encryption by default is supported on all [ current generation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#current-gen-instances) and [ previous generation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#previous-gen-instances) instance types.
+ If you copy a snapshot and encrypt it to a new KMS key, a complete (non-incremental) copy is created. This results in additional storage costs.

------
#### [ Console ]

**To enable encryption by default for a Region**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. From the navigation bar, select the Region.

1. From the navigation pane, select **Settings**, and then select the **Data protection and security** tab.

1. In the **EBS encryption** section, choose **Manage**.

1. Select **Enable**. You keep the AWS managed key with the alias `aws/ebs` created on your behalf as the default encryption key, or choose a symmetric customer managed encryption key.

1. Choose **Update EBS encryption**.

------
#### [ AWS CLI ]

**To view the encryption by default setting**

Use the [get-ebs-encryption-by-default](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ebs-encryption-by-default.html) command.
+ For a specific Region

  ```
  aws ec2 get-ebs-encryption-by-default --region {{region}}
  ```
+ For all Regions in your account

  ```
  echo -e "Region      \t Encrypt \t Key"; \
  echo -e "----------- \t ------- \t -------" ; \
  for region in $(aws ec2 describe-regions --region us-east-1 --query "Regions[*].[RegionName]" --output text);
  do
      default=$(aws ec2 get-ebs-encryption-by-default --region $region --query "{Encryption_By_Default:EbsEncryptionByDefault}" --output text); 
      kms_key=$(aws ec2 get-ebs-default-kms-key-id --region $region | jq '.KmsKeyId'); 
      echo -e "$region \t $default \t\t $kms_key"; 
  done
  ```

**To enable encryption by default**

Use the [enable-ebs-encryption-by-default](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-ebs-encryption-by-default.html) command.
+ For a specific Region

  ```
  aws ec2 enable-ebs-encryption-by-default --region {{region}}
  ```
+ For all Regions in your account

  ```
  echo -e "Region      \t Encrypt \t Key"; \
  echo -e "----------- \t ------- \t -------" ; \
  for region in $(aws ec2 describe-regions --region us-east-1 --query "Regions[*].[RegionName]" --output text); 
  do
      default=$(aws ec2 enable-ebs-encryption-by-default --region $region --query "{Encryption_By_Default:EbsEncryptionByDefault}" --output text); 
      kms_key=$(aws ec2 get-ebs-default-kms-key-id --region $region | jq '.KmsKeyId'); 
      echo -e "$region \t $default \t\t $kms_key"; 
  done
  ```

**To disable encryption by default**

Use the [disable-ebs-encryption-by-default](https://docs.aws.amazon.com/cli/latest/reference/ec2/disable-ebs-encryption-by-default.html) command.
+ For a specific Region

  ```
  aws ec2 disable-ebs-encryption-by-default --region {{region}}
  ```
+ For all Regions in your account

  ```
  echo -e "Region      \t Encrypt \t Key"; \
  echo -e "----------- \t ------- \t -------" ; \
  for region in $(aws ec2 describe-regions --region us-east-1 --query "Regions[*].[RegionName]" --output text); 
  do
      default=$(aws ec2 disable-ebs-encryption-by-default --region $region --query "{Encryption_By_Default:EbsEncryptionByDefault}" --output text); 
      kms_key=$(aws ec2 get-ebs-default-kms-key-id --region $region | jq '.KmsKeyId'); 
      echo -e "$region \t $default \t\t $kms_key"; 
  done
  ```

------
#### [ PowerShell ]

**To view the encryption by default setting**

Use the [Get-EC2EbsEncryptionByDefault](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2EbsEncryptionByDefault.html) cmdlet.
+ For a specific Region

  ```
  Get-EC2EbsEncryptionByDefault -Region {{region}}
  ```
+ For all Regions in your account

  ```
  (Get-EC2Region).RegionName |
      ForEach-Object {
      [PSCustomObject]@{ 
          Region                    = $_
          EC2EbsEncryptionByDefault = Get-EC2EbsEncryptionByDefault -Region $_
          EC2EbsDefaultKmsKeyId     = Get-EC2EbsDefaultKmsKeyId -Region $_ 
      } } |
      Format-Table -AutoSize
  ```

**To enable encryption by default**

Use the [Enable-EC2EbsEncryptionByDefault](https://docs.aws.amazon.com/powershell/latest/reference/items/Enable-EC2EbsEncryptionByDefault.html) cmdlet.
+ For a specific Region

  ```
  Enable-EC2EbsEncryptionByDefault -Region {{region}}
  ```
+ For all Regions in your account

  ```
  (Get-EC2Region).RegionName |
      ForEach-Object { 
      [PSCustomObject]@{
          Region                    = $_
          EC2EbsEncryptionByDefault = Enable-EC2EbsEncryptionByDefault -Region $_
          EC2EbsDefaultKmsKeyId     = Get-EC2EbsDefaultKmsKeyId -Region $_ 
      } } |
      Format-Table -AutoSize
  ```

**To disable encryption by default**

Use the [Disable-EC2EbsEncryptionByDefault](https://docs.aws.amazon.com/powershell/latest/reference/items/Disable-EC2EbsEncryptionByDefault.html) cmdlet.
+ For a specific Region

  ```
  Disable-EC2EbsEncryptionByDefault -Region {{region}}
  ```
+ For all Regions in your account

  ```
  (Get-EC2Region).RegionName |
      ForEach-Object { 
      [PSCustomObject]@{
          Region                    = $_
          EC2EbsEncryptionByDefault = Disable-EC2EbsEncryptionByDefault -Region $_
          EC2EbsDefaultKmsKeyId     = Get-EC2EbsDefaultKmsKeyId -Region $_ 
      } } |
      Format-Table -AutoSize
  ```

------

You can't change the KMS key that is associated with an existing snapshot or encrypted volume. However, you can associate a different KMS key during a snapshot copy operation so that the resulting copied snapshot is encrypted by the new KMS key.
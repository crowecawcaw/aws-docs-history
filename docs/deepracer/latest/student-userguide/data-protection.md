# Data protection in AWS DeepRacer Student

The following sections explain what data is captured by AWS DeepRacer Student, and where AWS DeepRacer Student uses data encryption to protect your data.

When you create a AWS DeepRacer Student account you also create an AWS Player account. Resources created in your AWS DeepRacer Student account are stored in your AWS Player account. For more details about AWS Player accounts, see [What are AWS Player accounts?](setting-up.md "setting-up.md") in the _AWS DeepRacer Student User Guide_.

###### Topics

- [Captured data in the AWS DeepRacer Student portal](#captured-data "#captured-data")
- [Encryption at rest in AWS DeepRacer Student portal](#encryption-rest "#encryption-rest")
- [Encryption in transit in AWS DeepRacer Student portal](#encryption-transit "#encryption-transit")

## Captured data in the AWS DeepRacer Student portal

To use the AWS DeepRacer Student portal, the required data is stored in your AWS Player account. The data captured in the AWS DeepRacer Student portal is not used to help improve the service.

###### Captured data in AWS DeepRacer Student.

The following is a summary of data created in AWS DeepRacer Student and stored in your AWS Player account.

- Your email address and password used to register your account.
- Your racer name
- Your standing on the Student League leaderboard
- Your trained models
- Reward function code

## Encryption at rest in AWS DeepRacer Student portal

Data captured by AWS DeepRacer Student portal is encrypted by default.

AWS Player accounts use Amazon Cognito to encrypt and store the email and password used to login to AWS DeepRacer Student. For more information, see [Data Protection in Amazon Cognito](../../../cognito/latest/developerguide/data-protection.md "../../../cognito/latest/developerguide/data-protection.md").

All other data captured in AWS DeepRacer Student is encrypted at rest in the cloud using AWS owned keys through AWS Key Management Service with AES-GCM and using keys of size 256-bits. This data is stored and encrypted in Amazon Simple Storage Service (S3) and Amazon DynamoDB.

## Encryption in transit in AWS DeepRacer Student portal

Your registered and authorized email addresses are encrypted with client-side encryption. All other [data captured in AWS DeepRacer Student](#captured-data "#captured-data") is copied out of your account and processed in an internal AWS system. By default, AWS DeepRacer Student uses secure connections over HTTPS to encrypt data in transit.

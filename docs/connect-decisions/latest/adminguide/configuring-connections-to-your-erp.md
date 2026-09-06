

# Configuring Connections to your ERP
<a name="configuring-connections-to-your-erp"></a>

 To enable Amazon Connect Decisions to perform operations on your behalf in your Enterprise Resource Planning (ERP) system, you must configure a Connection that specifies the necessary connection parameters and the credentials Amazon Connect Decisions should use during the operation. 

**Supported ERP systems:**
+ SAP S/4HANA

## Configure the Credentials in Secrets Manager
<a name="configuring-connections-to-your-erp-configure-credentials"></a>

1.  Using your account, use [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/) to [Create an Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) 
   +  When entering the credentials in Secrets Manager, replace the placeholder values below (`<username>` and `<password>`) with the actual username and password that Amazon Connect Decisions should use 
   +  If using the console, choose `Other type of secret` for the `Secret Type` 
   +  If entering the details through the `Key/value pairs` tab in the console, enter 2 pairs: 
     + Key: `username`; Value: `<{{username}}>`
     + Key: `password`; Value: `<{{password}}>`
   +  If using the `Plaintext` tab to enter the secret in the console, enter a JSON object with the two pairs: 

     ```
     {
           "Username": "<{{username}}>",
           "Password": "<{{password}}>"
         }
     ```

1.  Encrypt your secret with an AWS KMS Key, take note of the Key's id, as you will need it in subsequent steps 

1.  Once your secret is created, take note of its Amazon Resource Name (ARN), as you will need it in subsequent steps 
   +  e.g.: `arn:aws:secretsmanager:<Region>:<AccountId>:secret:<SecretName>-<SixRandomCharacters>` 

## Configure permissions on the KMS Key
<a name="configuring-connections-to-your-erp-configure-kms-permissions"></a>

 You need to provide the permissions necessary for Amazon Connect Decisions to access and use it. 

1.  Update your KMS policy to allow Amazon Connect Decisions to access your key through the instance role 
   +  Note: Replace `<YourAccountNumber>` and `<YourInstanceID>` with your AWS account and Amazon Connect Decisions Instance ID. 

   ```
   {
           "Sid": "Allow Amazon Connect Decisions to access the AWS KMS Key",
           "Effect": "Allow",
           "Principal": {
              "Service": "scn.amazonaws.com",
               "AWS": "arn:aws:iam::{{YourAccountNumber}}:role/service-role/scn-instance-role-{{YourInstanceID}}"
           },
           "Action": [
              "kms:DescribeKey",
              "kms:CreateGrant",
               "kms:Encrypt",
               "kms:Decrypt",
               "kms:GenerateDataKey",
              "kms:GenerateDataKeyWithoutPlaintext"
           ],
           "Resource": "*"
       }
   ```

1.  Update the inline policy for your instance role to grant permission on the key 
   +  Note: Replace `<YourSecretArn>`, `<YourAccountNumber>` and `<YourInstanceID>` with your Secret ARN, AWS account and AWS Supply Chain Instance ID. 

   ```
   {
           "Version": "2012-10-17",		 	 	 
           "Statement": [
               {
                   "Sid": "Statement1",
                   "Effect": "Allow",
                   "Action": "secretsmanager:*",
                   "Resource": "{{YourSecretArn}}"
               },
               {
                   "Sid": "AllowKmsForSecretsManager",
                   "Effect": "Allow",
                   "Action": [
                       "kms:Decrypt",
                       "kms:DescribeKey"
                   ],
                   "Resource": "arn:aws:kms:us-east-1:{{YourAccountNumber}}:key/{{YourKeyId}}"
               }
           ]
       }
   ```

## Update the Secrets Manager resource policy for your Secret
<a name="configuring-connections-to-your-erp-update-secrets-manager-policy"></a>

1.  Update the Secrets Manager resource Policy for your Secret 
   +  Note: Replace `<YourSecretArn>` with the ARN of your Secret 

   ```
   {
          "Version":"2012-10-17",		 	 	 
          "Statement":[
             {
                "Effect":"Allow",
                "Principal":{
                   "Service":"scn.amazonaws.com"
                },
                "Action":[
                   "secretsmanager:GetSecretValue",
                   "secretsmanager:DescribeSecret"
                ],
                "Resource":"{{YourSecretArn}}"
             }
          ]
       }
   ```

## Configure the Amazon Connect Decisions Connection
<a name="configuring-connections-to-your-erp-configure-connection"></a>

1.  In your instance of Amazon Connect Decisions, navigate to the Data Management page 

1.  Select the `Connections` tab 

1.  Click the `Create Connection` button 

1.  In the `Create Connector` page, click the `Select` button on the row for `SAP S/4HANA` connector type 

1.  In the `Configure SAP S/4HANA API Connector` page enter the necessary information: 
   + `Connection Name`: unique connection name
   +  `API Endpoint URL`: the OData API endpoint URL of your SAP S/4HANA instance (e.g.: `https://<hostname>:<port>`) 
   +  `Client Number`: the 3-digit SAP client number (e.g.: `100`) 
   +  `Secret ARN`: the Amazon Resource Name (ARN) of the secret in Secrets Manager where the credentials to be used by Amazon Connect Decisions are stored 

1.  Click on the `Create Connector` button 
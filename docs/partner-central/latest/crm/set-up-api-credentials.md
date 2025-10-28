# Set up named credentials

To upgrade to the Partner Central API, you first set up named credentials. The CRM connector uses your Salesforce
organization credentials to authenticate with Partner Central.

###### To set up credentials

1. Sign in to Salesforce as a system administrator.
2. Under **Named credentials**,
   choose **New earlier**.
3. In the **New named credential**
   form, enter the values from the following table.

| Field                                 | Value                                                           |
| ------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Label**                             | AWS Partner Central API                                         |
| **URL**                               | https://partnercentral-selling.us-east-1.api.aws                |
| **Identity type**                     | Named Principal                                                 |
| **Authentication protocol**           | AWS signature version 4                                         |
| **AWS access key ID**                 | Cloud-Ops provides the ID during the prerequisite steps         |
| **AWS secret access key**             | Cloud-Ops provides the access key during the prerequisite steps |
| **AWS Region**                        | us-east-1                                                       |
| **AWS service**                       | partnercentral-selling                                          |
| **Generate authorization header**     | checked                                                         |
| **Allow merge fields in HTTP header** | checked                                                         |
| **Allow merge fields in HTTP body**   | unchecked                                                       | 4. Choose **Save**. 5. Return to the **AWSGuided setup** page. In the **Authentication details** section, choose **Review** and confirm the credentials. |

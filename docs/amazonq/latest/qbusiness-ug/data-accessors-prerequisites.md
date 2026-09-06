

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Prerequisites
<a name="data-accessors-prerequisites"></a>

To add an ISV as a data accessor, complete the following prerequisites:

1. [Get started with Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/getting-started.html)

1. [Create an Identity and Access Management (IAM) Identity Center-integrated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html) (IAM Federated application environments are not supported at this time).

1. Set up the retriever and connect your data sources. For a complete list of data source connectors (see [supported connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connectors-list.html)). You need the relevant credentials from each connector that you want to retrieve data from. For more information, see [Creating a retriever for an Amazon Q Business application environment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html) and [Connecting Amazon Q Business data sources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-sources.html).

1. If you are using a customer managed key in your Amazon Q Business Application, you must set your key policy to allow the ISV principal access to the KMS key with the following policy:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Id": "isv-key-consolepolicy",
       "Statement": [
           {
               "Sid": "EnableIAMUserPermissions",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::111122223333:role/{{isv-role}}"
               },
               "Action": "kms:Decrypt",
               "Resource": "arn:aws:kms:us-east-1:111122223333:key/{{key-id}}",
               "Condition": {
                   "StringLike": {
                       "kms:ViaService": [
                           "qbusiness.us-east-1.amazonaws.com"
                       ]
                   }
               }
           }
       ]
   }
   ```

------
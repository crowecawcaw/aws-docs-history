# Creating
 a presigned URL for Amazon S3 objects using
 CloudShell

This tutorial shows you how to create a presigned URL to share an Amazon S3 object with others.
 Because object owners specify their own security credentials when sharing, anyone who receives
 the presigned URL can access the object for a limited time.


## Prerequisites



* An IAM user with access permissions provided by the **AWSCloudShellFullAccess** policy.
* For the IAM permissions that are required to create a presigned URL, see [Share an object with others](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html") in
 the *Amazon Simple Storage Service User Guide*.

## Step 1: Create an IAM role to grant
 access to Amazon S3 bucket


This step describes how to create an IAM role to grant
 access to Amazon S3 bucket.


1. To get your IAM details that can be shared, call the `get-caller-identity`
 command from AWS CloudShell.



```
aws sts get-caller-identity
```

If the call is successful, the command line displays a response similar to the
 following.



```
{
    "Account": "123456789012", 
    "UserId": "AROAXXOZUUOTTWDCVIDZ2:redirect_session", 
    "Arn": "arn:aws:sts::531421766567:assumed-role/Feder08/redirect_session"
}
```
2. Take the user information that you obtained in the previous step, and add it to an AWS CloudFormation
 template. This template creates an IAM role. This role grants your collaborator
 least-privilege permissions for the shared resources.



```
Resources:
  CollaboratorRole:
    Type: AWS::IAM::Role
    Properties: 
      AssumeRolePolicyDocument: 
        Version: 2012-10-17		 	 	 
        Statement: 
          - Effect: Allow
            Principal:
              AWS: "arn:aws:iam::531421766567:role/Feder08"
            Action: "sts:AssumeRole"
      Description: Role used by my collaborators
      MaxSessionDuration: 7200
  CollaboratorPolicy:
    Type: AWS::IAM::Policy
    Properties: 
      PolicyDocument: 
        Version: 2012-10-17		 	 	 
        Statement:
          - Effect: Allow
            Action:
              - 's3:*'
            Resource: 'arn:aws:s3:::<YOUR_BUCKET_FOR_FILE_TRANSFER>'
            Condition:
              StringEquals:
                s3:prefix:
                 - "myfolder/*"
      PolicyName: S3ReadSpecificFolder
      Roles: 
        - !Ref CollaboratorRole
Outputs:
  CollaboratorRoleArn:
    Description: Arn for the Collaborator's Role
    Value: !GetAtt CollaboratorRole.Arn

```
3. Save the AWS CloudFormation template in a file that's named `template.yaml`.
4. Use the template to deploy the stack and create the IAM role by calling the
 `deploy` command.


```
aws cloudformation deploy --template-file ./template.yaml --stack-name CollaboratorRole --capabilities CAPABILITY_IAM
```

## Generate the presigned URL


This step describes how to generate the presigned URL.


1. Using your editor in AWS CloudShell, add the following code. This code creates a URL that provides
 federated users with direct access to the AWS Management Console.



```
import urllib, json, sys
import requests
import boto3
import os

def main():
  sts_client = boto3.client('sts')
  assume_role_response = sts_client.assume_role(
      RoleArn=os.environ.get(ROLE_ARN),
      RoleSessionName="collaborator-session"
  )
  credentials = assume_role_response['Credentials']
  url_credentials = {}
  url_credentials['sessionId'] = credentials.get('AccessKeyId')
  url_credentials['sessionKey'] = credentials.get('SecretAccessKey')
  url_credentials['sessionToken'] = credentials.get('SessionToken')
  json_string_with_temp_credentials = json.dumps(url_credentials)
  print(f"json string {json_string_with_temp_credentials}")

  request_parameters = f"?Action=getSigninToken&Session={urllib.parse.quote(json_string_with_temp_credentials)}"
  request_url = "https://signin.aws.amazon.com/federation" + request_parameters
  r = requests.get(request_url)
  signin_token = json.loads(r.text)
  request_parameters = "?Action=login" 
  request_parameters += "&Issuer=Example.org" 
  request_parameters += "&Destination=" + urllib.parse.quote("https://us-west-2.console.aws.amazon.com/cloudshell")
  request_parameters += "&SigninToken=" + signin_token["SigninToken"]
  request_url = "https://signin.aws.amazon.com/federation" + request_parameters

  # Send final URL to stdout
  print (request_url)

if __name__ == "__main__":
  main()

```
2. Save the code in a file called `share.py`.
3. Run the following from the command line to retrieve the Amazon Resource Name (ARN) of the
 IAM role from AWS CloudFormation. Then, use it in the Python script to obtain
 temporary security credentials.



```
ROLE_ARN=$(aws cloudformation describe-stacks --stack-name CollaboratorRole --query "Stacks[*].Outputs[?OutputKey=='CollaboratorRoleArn'].OutputValue" --output text) python3 ./share.py 
```

The script returns a URL that a collaborator can click to take them to AWS CloudShell in
 AWS Management Console. The collaborator has full control over the `myfolder/`
 folder in the Amazon S3 bucket for the next 3,600 seconds (1 hour). The credentials expire
 after an hour. After this time, the collaborator can no longer access the bucket.



# Integrate your identity provider (IdP) with a Connect Customer Global Resiliency SAML sign in endpoint
<a name="integrate-idp"></a>

To enable your agents to sign in once and be logged into both AWS Regions to process contacts from the current active Region, you need to configure IAM settings to use the global sign in SAML endpoint. 

## Before you begin
<a name="before-idp"></a>

You must enable SAML for your Connect Customer instance to use Connect Customer Global Resiliency. For information about getting started with IAM federation, see [Enabling SAML 2.0 federated users to access the AWS Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html). 

## Important things to know
<a name="important-integrate-idp"></a>
+ Agent failover is only supported when using the global sign-in endpoint.
+ To perform the steps in this topic, you'll need your instance ID. For instructions about how to find it, see [Find your Connect Customer instance ID or ARN](find-instance-arn.md).
+ You will also need to know the source Region of your Connect Customer instances. For instructions about how to find it, see [How to find the source Region of your Connect Customer instances](create-replica-connect-instance.md#how-to-find-source-region-of-instances). 
+ If you are embedding your Connect application within an iframe, you must make sure that your domain is present in the list of Approved Origins in both your source and replica instance in order for global sign-in to work.

  To configure Approved Origins at the instance level, follow the steps in [Use an allowlist for integrated applications in Connect Customer](app-integration.md).
+ Agents must exist in *both* your source and replica Connect Customer instances and have the same username as the role session name from your identity provider (IdP). Otherwise, you will receive a `UserNotOnboardedException` exception and risk losing agent redundancy capabilities between your instances.
+ You must associate agents to a traffic distribution group before agents attempt to sign in. Otherwise agent sign-in will fail with a `ResourceNotFoundException`. For information about how to setup your traffic distribution groups and associate agents to them, see [Associate agents to Connect Customer instances across multiple AWS Regions](associate-agents-across-regions.md).
+ When your agents federate into Connect Customer with the new SAML sign-in URL, Connect Customer Global Resiliency always attempts to log the agent into both your source and replica Regions / instances, no matter how `SignInConfig` is configured in your traffic distribution group. You can verify this by checking CloudTrail logs. 
+ The `SignInConfig` distribution in your default traffic distribution group only determines which AWS Region is used to help sign-in. Regardless of how your `SignInConfig` distribution is configured, Connect Customer always attempts to sign in agents to both Regions of your Connect Customer instance.
+ After replicating a Connect Customer instance, only one SAML sign-in endpoint is generated for your instances. This endpoint always contains the source AWS Region in the URL. 
+ You don't need to configure a relay state when using the personalized SAML sign-in URL with Connect Customer Global Resiliency.

## How to integrate your identity provider
<a name="howto-integrate-idp"></a>

1. When you create a replica of your Connect Customer instance using the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API, a personalized SAML sign-in URL is generated for your Connect Customer instances. The URL is generated in the following format: 

   `https://{{instance-id}}.{{source-region}}.sign-in.connect.aws/saml`

   1. {{instance-id}} is the instance ID for either instance in your instance group. The instance ID is identical in the source and replica Regions.

   1. {{source-region}} corresponds to the source AWS Region in which the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API was called.

1. Add the following trust policy to your IAM Federation role. Use the URL for the global sign-in SAML endpoint as shown in the following example.

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement":[
         {
            "Effect":"Allow",
            "Principal":{
               "Federated":[
                 "arn:aws:iam::{{111122223333}}:saml-provider/{{MySAMLProvider}}"
               ]
            },
            "Action":"sts:AssumeRoleWithSAML",
            "Condition":{
               "StringLike":{
                  "SAML:aud":[
                     "https://instance-id.source-region.sign-in.connect.aws/saml*"
                  ]
               }
            }
         }
      ]
   }
   ```

------
**Note**  
`saml-provider-arn` is the identity provider resource created in IAM.

1. Grant access to `connect:GetFederationToken` for your `InstanceId` on your IAM Federation role. For example:

------
#### [ JSON ]

****  

   ```
   {
   "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "GetFederationTokenAccess",
               "Effect": "Allow",
               "Action": "connect:GetFederationToken",
               "Resource": "*",
               "Condition": {
                   "StringEquals": {
                       "connect:InstanceId": "{{your-instance-id}}"
                   }
               }
           }
       ]
   }
   ```

------

1. Add an attribute mapping to your identity provider application using the following attribute and value strings.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/integrate-idp.html)

1. Configure the Assertion Consumer Service (ACS) URL of your identity provider to point to your personalized SAML sign-in URL. Use the following example for the ACS URL:

   ```
   https://{{instance-id}}.{{source-region}}.sign-in.connect.aws/saml?&instanceId={{instance-id}}&accountId={{your AWS account ID}}&role={{saml-federation-role}}&idp={{your SAML IDP}}&destination={{optional-destination}}
   ```

1. Set following fields in the URL parameters:
   + `instanceId`: The identifier of your Connect Customer instance. For instructions about how to find your instance ID, see [Find your Connect Customer instance ID or ARN](find-instance-arn.md).
   + `accountId`: The AWS account ID where the Connect Customer instances are located.
   + `role`: Set to the name or Amazon Resource Name (ARN) of the SAML role used for Connect Customer federation.
   + `idp`: Set to the name or Amazon Resource Name (ARN) of the SAML identity provider in IAM.
   + `destination`: Set to the optional path where agents will land in the instance after signing in (for example: `/agent-app-v2`).
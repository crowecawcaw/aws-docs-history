# Integrate your identity provider (IdP) with an

Amazon Connect Global Resiliency SAML sign in endpoint

To enable your agents to sign in once and be logged into both AWS Regions to
process contacts from the current active Region, you need to configure IAM
settings to use the global sign in SAML endpoint.

## Before you begin

You must enable SAML for your Amazon Connect instance to use Amazon Connect Global
Resiliency. For information about getting started with IAM federation, see
[Enabling SAML 2.0 federated users to access the AWS Management
Console](../../../IAM/latest/UserGuide/id_roles_providers_enable-console-saml.md "../../../IAM/latest/UserGuide/id_roles_providers_enable-console-saml.md").

## Important things to know

- To perform the steps in this topic, you'll need your instance ID.
  For instructions about how to find it, see [Find your Amazon Connect instance ID or ARN](find-instance-arn.md "find-instance-arn.md").
- You will also need to know the source Region of your Amazon Connect
  instances. For instructions about how to find it, see [How to find the source
  Region of your Amazon Connect instances](create-replica-connect-instance.md#how-to-find-source-region-of-instances "create-replica-connect-instance.md#how-to-find-source-region-of-instances").
- If you are embedding your Connect application within an iframe,
  you must ensure that your domain is present in the list of Approved
  Origins in both your source and replica instance in order for global
  sign-in to work.

To configure Approved Origins at the instance level, follow the
steps in [Use an allowlist for integrated applications in
Amazon Connect](app-integration.md "app-integration.md").

- Agents must be created already in _both_ your
  source and replica Amazon Connect instances and have the same username as the
  role session name from your identity provider (IdP). Otherwise, you
  will receive a `UserNotOnboardedException` exception and
  risk losing agent redundancy capabilities between your
  instances.
- You must associate agents to a traffic distribution group before
  agents attempt to sign in. Otherwise agent sign-in will fail with a
  `ResourceNotFoundException`. For information about
  how to setup your traffic distribution groups and associate agents
  to them, see [Associate agents to Amazon Connect
  instances across multiple AWS Regions](associate-agents-across-regions.md "associate-agents-across-regions.md").
- When your agents federate into Amazon Connect with the new SAML sign-in
  URL, Amazon Connect Global Resiliency always attempts to log the agent into
  both your source and replica Regions / instances, no matter how
  `SignInConfig` is configured in your traffic distribution group. You can
  verify this by checking CloudTrail logs.
- The `SignInConfig` distribution in your default traffic distribution group
  only determines which AWS Region is used to
  facilitate sign-in. Regardless of how your `SignInConfig`
  distribution is configured, Amazon Connect always attempts to sign in agents
  to both Regions of your Amazon Connect instance.
- After replicating an Amazon Connect instance, only one SAML sign-in
  endpoint is generated for your instances. This endpoint always
  contains the source AWS Region in the URL.
- You don't need to configure a relay state when using the
  personalized SAML sign-in URL with Amazon Connect Global Resiliency.

## How to integrate your identity

provider

1. When you create a replica of your Amazon Connect instance using the [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") API, a personalized SAML sign-in URL
   is generated for your Amazon Connect instances. The URL is generated in the
   following format:

`https://`instance-id`.`source-region`.sign-in.connect.aws/saml`

    1. `instance-id` is the instance ID
     for either instance in your instance group. The instance ID
     is identical in the source and replica Regions.
    2. `source-region` corresponds to
     the source AWS Region in which the [ReplicateInstance](../APIReference/API_ReplicateInstance.md "../APIReference/API_ReplicateInstance.md") API was called.

2. Add the following trust policy to your IAM Federation role. Use
   the URL for the global sign-in SAML endpoint as shown in the
   following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Federated":[
 "arn:aws:iam::`111122223333`:saml-provider/`MySAMLProvider`"
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
}`

```

###### Note

`saml-provider-arn` is the identity provider
resource created in IAM. 3. Grant access to `connect:GetFederationToken` for your
`InstanceId` on your IAM Federation role. For
example:

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetFederationTokenAccess",
 "Effect": "Allow",
 "Action": "connect:GetFederationToken",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "connect:InstanceId": "`your-instance-id`"
 }
 }
 }
 ]
}`

```

4. Add an attribute mapping to your identity provider application
   using the following attribute and value strings.

| Attribute                                   | Value                                   |
| ------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| https://aws.amazon.com/SAML/Attributes/Role | `saml-role-arn`,`identity-provider-arn` | 5. Configure the Assertion Consumer Service (ACS) URL of your identity provider to point to your personalized SAML sign-in URL. Use the following example for the ACS URL: `` https://`instance-id`.`source-region`.sign-in.connect.aws/saml?&instanceId=`instance-id`&accountId=`your AWS account ID`&role=`saml-federation-role`&idp=`your SAML IDP`&destination=`optional-destination` `` 6. Set following fields in the URL parameters: <br>• `instanceId`: The identifier of your Amazon Connect instance. For instructions about how to find your instance ID, see [Find your Amazon Connect instance ID or ARN](find-instance-arn.md "find-instance-arn.md"). <br>• `accountId`: The AWS account ID where the Amazon Connect instances are located. <br>• `role`: Set to the name or Amazon Resource Name (ARN) of the SAML role used for Amazon Connect federation. <br>• `idp`: Set to the name or Amazon Resource Name (ARN) of the SAML identity provider in IAM. <br>• `destination`: Set to the optional path where agents will land in the instance after signing in (for example: `/agent-app-v2`). |

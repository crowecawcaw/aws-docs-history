**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# IAM role for retrieving recommendations

from Amazon Personalize

You can configure Amazon Pinpoint to retrieve recommendation data from an Amazon Personalize solution
that's been deployed as an Amazon Personalize campaign. You can use this data to send personalized
recommendations to message recipients based on each recipient's attributes and behavior. To
learn more, see [Machine learning models](../userguide/ml-models.md "../userguide/ml-models.md") in
the _Amazon Pinpoint User Guide_.

Before you can retrieve recommendation data from an Amazon Personalize campaign, you have to create an
AWS Identity and Access Management (IAM) role that allows Amazon Pinpoint to retrieve the data from the campaign. Amazon Pinpoint can
create this role for you automatically when you use the console to set up a recommender
model in Amazon Pinpoint. Or, you can create this role manually.

To create the role manually, use the IAM API to complete the following steps:

1. Create an IAM policy that allows an entity (in this case, Amazon Pinpoint) to retrieve
   recommendation data from an Amazon Personalize campaign.
2. Create an IAM role and attach the IAM policy to it.
   This topic explains how to complete these steps by using the AWS Command Line Interface (AWS CLI). It assumes
   that you've already created the Amazon Personalize solution and deployed it
   as an Amazon Personalize campaign. For information about creating and
   deploying a campaign, see [Creating a
   campaign](../../../personalize/latest/dg/campaigns.md "../../../personalize/latest/dg/campaigns.md") in the _Amazon Personalize Developer Guide_.

This topic also assumes that you've already installed and configured the AWS CLI. For
information about setting up the AWS CLI, see [Installing
the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the _AWS Command Line Interface User Guide_.

## Step 1: Create the IAM

policy

An IAM policy defines permissions for an entity, such as an identity or resource. To
create a role that allows Amazon Pinpoint to retrieve recommendation data from an Amazon Personalize campaign,
you first have to create an IAM policy for the role. This policy needs to allow Amazon Pinpoint
to:

- Retrieve configuration information for the solution that's deployed by the
  campaign (`DescribeSolution`).
- Check the status of the campaign (`DescribeCampaign`).
- Retrieve recommendation data from the campaign
  (`GetRecommendations`).

In the following procedure, the example policy allows this access for a particular
Amazon Personalize solution that was deployed by a particular Amazon Personalize campaign.

###### To create the IAM policy

1. In a text editor, create a new file. Paste the following code into the
   file:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RetrieveRecommendationsOneCampaign",
 "Effect": "Allow",
 "Action": [
 "personalize:DescribeSolution",
 "personalize:DescribeCampaign",
 "personalize:GetRecommendations"
 ],
 "Resource": [
 "arn:aws:personalize:`us-east-1`:`111122223333`:solution/`solutionId`",
 "arn:aws:personalize:`us-east-1`:`111122223333`:campaign/`campaignId`"
 ]
 }
 ]
}`

```

In the preceding example, replace the `italicized`
text with your information:

    * `region` – The name of the AWS
     Region that hosts the Amazon Personalize solution and campaign.
    * `accountId` – Your AWS account
     ID.
    * `solutionId` – The unique resource ID
     for the Amazon Personalize solution that's deployed by the campaign.
    * `campaignId` – The unique resource ID
     for the Amazon Personalize campaign to retrieve recommendation data from.

2. When you finish, save the file as
   `RetrieveRecommendationsPolicy.json`.
3. By using the command line interface, navigate to the directory where you saved
   the `RetrieveRecommendationsPolicy.json` file.
4. Enter the following command to create a policy and name it
   `RetrieveRecommendationsPolicy`. To use a different name, change
   `RetrieveRecommendationsPolicy` to the name that
   you want.

```
aws iam create-policy --policy-name `RetrieveRecommendationsPolicy` --policy-document file://RetrieveRecommendationsPolicy.json
```

###### Note

If you receive a message that your account isn't authorized to perform the
`CreatePolicy` operation, you need to attach a policy to your
user that lets you create new IAM policies and roles for your
account. For more information, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#attach-managed-policy-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#attach-managed-policy-console") in the
_IAM User Guide_. 5. Copy the Amazon Resource Name (ARN) of the policy
(`arn:aws:iam::123456789012:policy/RetrieveRecommendationsPolicy`
in the preceding example). You need this ARN to create the IAM role in the
next section.

## Step 2: Create the IAM

role

After you create the IAM policy, you can create an IAM role and attach the policy
to it.

Each IAM role contains a _trust policy_, which is a set of rules
that specifies which entities are allowed to assume the role. In this section, you
create a trust policy that allows Amazon Pinpoint to assume the role. Next, you create the role
itself. Then, you attach the policy to the role.

###### To create the IAM role

1. In a text editor, create a new file. Paste the following code into the
   file:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "pinpoint.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "AWS:SourceArn": "arn:aws:mobiletargeting:`us-east-1`:`444455556666`:apps/*"
 }
 }
 }
 ]
}`

```

2. Save the file as `RecommendationsTrustPolicy.json`.
3. By using the command line interface, navigate to the directory where you saved
   the `RecommendationsTrustPolicy.json` file.
4. Enter the following command to create a new role and name it
   `PinpointRoleforPersonalize`. To use a different name, change
   `PinpointRoleforPersonalize` to the name that you
   want.

```
aws iam create-role --role-name `PinpointRoleforPersonalize` --assume-role-policy-document file://RecommendationsTrustPolicy.json
```

5. Enter the following command to attach the policy that you created in the
   previous section to the role that you just created:

```
`aws iam attach-role-policy --policy-arn `arn:aws:iam::123456789012:policy/RetrieveRecommendationsPolicy` --role-name `PinpointRoleforPersonalize``
```

In the preceding command, replace
`arn:aws:iam::123456789012:policy/RetrieveRecommendationsPolicy`
with the ARN of the policy that you created in the previous section. Also,
replace `PinpointRoleforPersonalize` with the name of
the role that you specified in step 4, if you specified a different name for the
role.

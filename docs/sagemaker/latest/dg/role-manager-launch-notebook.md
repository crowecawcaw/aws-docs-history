# Launch Studio Classic

Use your persona-focused roles to launch Studio Classic. If you are an administrator, you
can give your users access to Studio Classic and have them assume their persona role either
directly through the AWS Management Console or through the AWS IAM Identity Center.

## Launch Studio Classic with

AWS Management Console

For data scientists or other users to assume their given persona through the
AWS Management Console, they require a console role to get to the Studio Classic environment.

You cannot use Amazon SageMaker Role Manager to create a role that grants permissions to the AWS Management Console.
However, after creating a service role in the role manager, you can go to the IAM
console to edit the role and add a user access role. The following is an example of
a role that provides user access to the AWS Management Console:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DescribeCurrentDomain",
 "Effect": "Allow",
 "Action": "sagemaker:DescribeDomain",
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:domain/<STUDIO-DOMAIN-ID>"
 },
 {
 "Sid": "RemoveErrorMessagesFromConsole",
 "Effect": "Allow",
 "Action": [
 "servicecatalog:ListAcceptedPortfolioShares",
 "sagemaker:GetSagemakerServicecatalogPortfolioStatus",
 "sagemaker:ListModels",
 "sagemaker:ListTrainingJobs",
 "servicecatalog:ListPrincipalsForPortfolio",
 "sagemaker:ListNotebookInstances",
 "sagemaker:ListEndpoints"
 ],
 "Resource": "*"
 },
 {
 "Sid": "RequiredForAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListDomains",
 "sagemaker:ListUserProfiles"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CreatePresignedURLForAccessToDomain",
 "Effect": "Allow",
 "Action": "sagemaker:CreatePresignedDomainUrl",
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:user-profile/<STUDIO-DOMAIN-ID>/<PERSONA_NAME>"
 }
 ]
}`

```

In the Studio Classic control panel, choose **Add User** to create a
new user. In the **General Settings** section, give your user a
name and set the **Default execution role** for the user to be the
role that you created using Amazon SageMaker Role Manager.

On the next screen, choose the appropriate Jupyter Lab version, and whether to
turn on SageMaker JumpStart and SageMaker AI Project templates. Then choose
**Next**. On the SageMaker Canvas settings page, choose whether to turn on
SageMaker Canvas support, and additionally whether to allow for timeseries forecasting in
SageMaker Canvas. Then choose **Submit**.

Your new user should now be visible in the Studio Classic control panel. To test this
user, choose **Studio** from the **Launch app**
dropdown list in the same row as the user’s name.

## Launch Studio Classic

with IAM Identity Center

To assign IAM Identity Center users to execution roles, the user must first
exist in the IAM Identity Center directory. For more information, see [Manage
identities in IAM Identity Center](../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md "../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md") in the _AWS IAM Identity Center_.

###### Note

Your IAM Identity Center Authentication directory and Studio Classic domain
must be in the same AWS Region.

1. To assign IAM Identity Center users to your Studio Classic domain,
   choose **Assign users and Groups** in the Studio Classic
   control panel. On the **Assign users and groups** screen
   select your data scientist user, and then choose **Assign Users and
   Groups**.
2. After the user is added to the Studio Classic control panel, choose the user
   to open the user details screen.
3. On the **User details** screen, choose
   **Edit**.
4. On the **Edit user profile** screen, under
   **General settings**, modify the **Default
   execution role** to match the user execution role you’ve
   created for your data scientists.
5. Choose **Next** through the rest of the settings pages,
   and choose **Submit** to save your changes.

When your data scientist or other user logs into the IAM Identity Center portal,
they see a tile for this Studio Classic domain. Choosing that tile logs them into
Studio Classic with their assigned user execution role.

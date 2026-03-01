# Setting up Storage Browser for S3

To connect end users with Amazon S3 _locations_, you must first set up an authentication and
authorization method. There are three methods to set up an authentication and authorization
method with Storage Browser:

- [Method 1: Managing data access for your customers and third party partners](#setup-storagebrowser-method1 "#setup-storagebrowser-method1")
- [Method 2: Managing data access for your IAM principals for your AWS account](#setup-storagebrowser-method2 "#setup-storagebrowser-method2")
- [Method 3: Managing data access at scale](#setup-storagebrowser-method3 "#setup-storagebrowser-method3")

## Method 1: Managing data access for your customers and third party partners

With this method, you can use [AWS Amplify
Auth](https://docs.amplify.aws/react/build-a-backend/auth/set-up-auth/ "https://docs.amplify.aws/react/build-a-backend/auth/set-up-auth/") to manage access control and security for files. This method is ideal when
you want to connect your customers or third party partners with data in S3. With this
option, your customers can authenticate using social or enterprise identity
providers.

You provide IAM credentials to your end users and third party partners using AWS Amplify
Auth with an S3 bucket that’s configured to use Amplify Storage. AWS Amplify Auth is built
on [Amazon Cognito](../../../cognito/latest/developerguide/what-is-amazon-cognito.md "../../../cognito/latest/developerguide/what-is-amazon-cognito.md"), a fully
managed customer identity and access management service where you can authenticate and
authorize users from a built-in user directory or enterprise directory, or from consumer
identity providers. The Amplify authorization model defines which prefixes the current
authenticated user can access. For more information about how to set up authorization for
AWS Amplify, see [Set up
storage](https://docs.amplify.aws/react/build-a-backend/storage/set-up-storage/ "https://docs.amplify.aws/react/build-a-backend/storage/set-up-storage/").

To initialize the component with the Amplify authentication and storage methods, add the
following code snippet to your web application:

```
import {
  createAmplifyAuthAdapter,
  createStorageBrowser,
} from '@aws-amplify/ui-react-storage/browser';
import "@aws-amplify/ui-react-storage/styles.css";

import config from './amplify_outputs.json';

Amplify.configure(config);

export const { StorageBrowser } = createStorageBrowser({
  config: createAmplifyAuthAdapter(),
});
```

## Method 2: Managing data access for your IAM principals for your AWS account

If you want to manage access for your IAM principals or your AWS account directly,
you can create an IAM role that has permissions to invoke the [GetDataAccess](../API/API_control_GetDataAccess.md "../API/API_control_GetDataAccess.md") S3 API operation. To set this up, you must create an
S3 Access Grants instance to map out permissions for S3 general purpose buckets and prefixes to the specified IAM
identities. The Storage Browser component (which must be called on the client side after obtaining the IAM credentials) will then invoke the [ListCallerAccessGrants](../API/API_control_ListCallerAccessGrants.md "../API/API_control_ListCallerAccessGrants.md") S3 API operation to fetch the available grants to the
identity requester and populate the locations in the component. After you obtain the
`s3:GetDataAccess` permission, those credentials are then used by the Storage
Browser component to request data access to S3.

```
import {
  createManagedAuthAdapter,
  createStorageBrowser,
} from '@aws-amplify/ui-react-storage/browser';
import "@aws-amplify/ui-react-storage/styles.css";

export const { StorageBrowser } = createStorageBrowser({
  config: createManagedAuthAdapter({
    credentialsProvider: async (options?: { forceRefresh?: boolean }) => {
      // return your credentials object
      return {
        credentials: {
          accessKeyId: 'my-access-key-id',
          secretAccessKey: 'my-secret-access-key',
          sessionToken: 'my-session-token',
          expiration: new Date()
        },
      }
    },
    // AWS `region` and `accountId`
    region: '',
    accountId: '',
    // call `onAuthStateChange` when end user auth state changes
    // to clear sensitive data from the `StorageBrowser` state
    registerAuthListener: (onAuthStateChange) => {},
  })
});
```

## Method 3: Managing data access at scale

If you want to associate an [S3 Access Grants](access-grants.md "access-grants.md") instance to your IAM
Identity Center for a more scalable solution (such as providing data access to your whole
company), you can request data from Amazon S3 on behalf of the current authenticated user. For
example, you can grant user groups in your corporate directory access to your data in S3.
This approach allows you to centrally manage S3 Access Grants permissions for your users and groups,
including the ones hosted on external providers such as Microsoft Entra, Okta, and
others.

When using this method, the [integration with the
IAM Identity Center](../../../singlesignon/latest/userguide/trustedidentitypropagation.md "../../../singlesignon/latest/userguide/trustedidentitypropagation.md") allows you to use existing user directories. Another benefit
of an IAM Identity Center trusted identity propagation is that each [AWS CloudTrail data event for Amazon S3](enable-cloudtrail-logging-for-s3.md "enable-cloudtrail-logging-for-s3.md") contains a direct reference to the end user identity
that accessed the S3 data.

If you have an application that supports OAuth 2.0 and your users need access from these
applications to AWS services, we recommend that you use trusted identity propagation. With
trusted identity propagation, a user can sign in to an application, and that application can
pass the user’s identity in any requests that access data in AWS services. This
application interacts with IAM Identity Center on behalf of any authenticated users. For
more information, see [Using trusted identity propagation with customer managed applications](../../../singlesignon/latest/userguide/trustedidentitypropagation-using-customermanagedapps-setup.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-using-customermanagedapps-setup.md").

[Trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md") is an AWS IAM Identity Center feature that administrators of connected AWS services can use to grant and audit access to service data. Access to this data is based on user attributes such as group associations. Setting up trusted identity propagation requires collaboration between the administrators of connected AWS services and the IAM Identity Center administrators. For more information, see [Prerequisites and considerations](../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overall-prerequisites.md").

### Setup

To set up Storage Browser authentication in the AWS Management Console using [S3 Access Grants](access-grants.md "access-grants.md")
and [IAM Identity
Center trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation.md "../../../singlesignon/latest/userguide/trustedidentitypropagation.md"), your applications must request data from
Amazon S3 on behalf of the current authenticated user. With this approach, you can give users
or groups of users from your corporate directory direct access to your S3 buckets,
prefixes, or objects. This means that your application won’t need to map any users to an
IAM principal.

The following workflow outlines the steps for setting up Storage Browser for S3, using IAM
Identity Center and S3 Access Grants:

| Steps | Description                                                                                                                                                                                                                                                                                                                                                       |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | [Enable IAM Identity Center for your AWS Organizations](#enable-iam-idc-org "#enable-iam-idc-org")                                                                                                                                                                                                                                                                |
| 2     | [Configure AWS Identity and Access Management Identity Center federation](#configure-iam-idc "#configure-iam-idc")                                                                                                                                                                                                                                                |
| 3     | [Add a trusted token issuer in the AWS Identity and Access Management Identity Center console](#add-trusted-token-issuer-idc "#add-trusted-token-issuer-idc")<br>The trusted token issuer represents your external identity provider (IdP)<br>within IAM Identity Center, enabling it to recognize identity tokens for your<br>application’s authenticated users. |
| 4     | [Create an IAM role for the bootstrap application and identity bearer](#create-iam-role-bootstrap "#create-iam-role-bootstrap")                                                                                                                                                                                                                                   |
| 5     | [Create and configure your application in IAM Identity Center](#create-app-iam-idc "#create-app-iam-idc")<br>This application interacts with IAM Identity Center on behalf of<br>authenticated users.                                                                                                                                                             |
| 6     | [Add S3 Access Grants as a trusted application for identity propagation](#add-s3-ag-app "#add-s3-ag-app")<br>This step connects your application to S3 Access Grants, so that it can make requests<br>to S3 Access Grants on behalf of authenticated users.                                                                                                       |
| 7     | [Create a grant to a user or group](#create-grant-user-group "#create-grant-user-group")<br>This step syncs users from AWS Identity and Access Management Identity Center with the System for<br>Cross-domain Identity Management (SCIM). SCIM keeps your IAM Identity Center<br>identities in sync with identities from your identity provider (IdP).            |
| 8     | [Create your Storage Browser for S3 component](#create-storage-browser-component "#create-storage-browser-component")                                                                                                                                                                                                                                             |

### Enable IAM Identity Center for your AWS Organizations

To enable IAM Identity Center for your AWS Organizations, perform the following steps:

1. Sign in to the AWS Management Console, using one of these methods:
   1. \***\*New to AWS (root user)**
      –\*\* Sign in as the account owner by choosing Root user and
      entering your AWS account email address. On the next page, enter your
      password.
   2. \***\*Already using AWS (IAM
      credentials)** –\*\* Sign in using your IAM
      credentials with administrative permissions.

2. Open the [IAM Identity
   Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
3. Under **Enable IAM Identity Center**, choose
   **Enable**.

###### Note

IAM Identity Center requires the setup of AWS Organizations. If you haven't set up an
organization, you can choose to have AWS create one for you. Choose
**Create AWS organization** to complete this process. 4. Choose **Enable with AWS Organizations**. 5. Choose **Continue**. 6. (Optional) Add any tags that you want to associate with this organization
instance. 7. (Optional) Configure the delegated administration.

###### Note

If you’re using a multi-account environment, we recommend that you configure
delegated administration. With delegated administration, you can limit the number of
people who require access to the management account in AWS Organizations. For more
information, see [Delegated
administration](../../../singlesignon/latest/userguide/delegated-admin.md "../../../singlesignon/latest/userguide/delegated-admin.md"). 8. Choose **Save**.

AWS Organizations automatically sends a verification email to the address that is associated
with your management account. There might be a delay before you receive the verification
email. Make sure to verify your email address within 24 hours, before your verification
email expires.

### Configure AWS Identity and Access Management Identity Center federation

To use Storage Browser for S3 with corporate directory users, you must configure IAM
Identity Center to use an external identity provider (IdP). You can use the preferred
identity provider of your choice. However, be aware that each identity provider uses
different configuration settings. For tutorials on using different external identity
providers, see [IAM Identity Center source
tutorials](../../../singlesignon/latest/userguide/tutorials.md "../../../singlesignon/latest/userguide/tutorials.md").

###### Note

Make sure to record the issuer URL and the audience attributes of the identity
provider that you’ve configured because you will need to refer to it in later steps. If
you don’t have the required access or permissions to configure an IdP, you might need to
contact the administrator of the external IdP to obtain them.

### Add a trusted token issuer in the AWS Identity and Access Management Identity Center console

The trusted token issuer represents your external identity provider in the AWS Identity and Access Management
Identity Center, and recognizes tokens for your application’s authenticated users. The
account owner of the IAM Identity Center instance in your AWS Organizations must perform these
steps. These steps can be done either in the IAM Identity Center console, or
programmatically.

To add a trusted token issuer in the AWS Identity and Access Management Identity Center console, perform the
following steps:

1. Open the [IAM Identity
   Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Settings**.
3. Choose the **Authentication** tab.
4. Navigate to the **Trusted token issuers** section, and fill out
   the following details:
   1. Under **Issuer URL**, enter the URL of the external IdP that
      serves as the trusted token issuer. You might need to contact the administrator of
      the external IdP to obtain this information. For more information, see [Using applications with a trusted token issuer](../../../singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.md "../../../singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.md").
   2. Under **Trusted token issuer name**, enter a name for the
      trusted token issuer. This name will appear in the list of trusted token issuers
      that you can select in _Step 8_, when an application resource is configured for
      identity propagation.

5. Update your **Map attributes** to your preferred application
   attribute, where each identity provider attribute is mapped to an IAM Identity
   Center attribute. For example, you might want to [map the
   application attribute](../../../singlesignon/latest/userguide/mapawsssoattributestoapp.md "../../../singlesignon/latest/userguide/mapawsssoattributestoapp.md")
   `email` to the IAM Identity Center user attribute `email`. To
   see the list of allowed user attributes in IAM Identity Center, see the table in
   [Attribute mappings
   for AWS Managed Microsoft AD directory](../../../singlesignon/latest/userguide/attributemappingsconcept.md "../../../singlesignon/latest/userguide/attributemappingsconcept.md").
6. (Optional) If you want to add a resource tag, enter the key and value pair. To add
   multiple resource tags, choose **Add new tag** to generate a new
   entry and enter the key and value pairs.
7. Choose **Create trusted token issuer**.
8. After you finish creating the trusted token issuer, contact the application
   administrator to let them know the name of the trusted token issuer, so that they can
   confirm that the trusted token issuer is visible in the applicable console.
9. Make sure the application administrator selects this trusted token issuer in the
   applicable console to enable user access to the application from applications that are
   configured for trusted identity propagation.

### Create an IAM role for the `bootstrap` application and `identity bearer`

To ensure that the `bootstrap` application and `identity bearer`
users can properly work with each other, make sure to [create two IAM
roles](../../../managedservices/latest/onboardingguide/create-iam-role.md "../../../managedservices/latest/onboardingguide/create-iam-role.md"). One IAM role is required for the `bootstrap` application and
the other IAM role must be used for the identity bearer, or end users who are accessing
the web application that requests access through S3 Access Grants. The `bootstrap`
application receives the token issued by the identity provider and invokes the
`CreateTokenWithIAM` API, exchanging this token with the one
issued by the Identity Center.

Create an IAM role, such as `bootstrap-role`, with permissions such as
the following. The following example IAM policy gives permissions to the
`bootstrap-role` to perform the token exchange:

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Action": [
            "sso-oauth:CreateTokenWithIAM",
        ],
        "Resource": "arn:${`Partition`}:sso::${`AccountId`}:application/${`InstanceId`}/${`ApplicationId`}",
        "Effect": "Allow"
    },
    {
        "Action": [
            "sts:AssumeRole",
            "sts:SetContext"
        ],
        "Resource": "arn:aws:iam::${`AccountId`}:role/`identity-bearer-role`",
        "Effect": "Allow"
    }]
}
```

Then, create a second IAM role (such as `identity-bearer-role`), which
the identity broker uses to generate the IAM credentials. The IAM credentials returned
from the identity broker to the web application are used by the Storage Browser for S3 component
to allow access to S3 data:

```
{
    "Action": [
        "s3:GetDataAccess",
        "s3:ListCallerAccessGrants",
    ],
    "Resource": "arn:${`Partition`}:s3:${`Region`}:${`Account`}:access-grants/default",
    "Effect": "Allow"
}
```

This IAM role (`identity-bearer-role`) must use a trust policy with the
following statement:

```
{
   "Effect": "Allow",
   "Principal": {
      "AWS": "arn:${`Partition`}:iam::${`Account`}:role/${`RoleNameWithPath`}"
   },
   "Action": [
       "sts:AssumeRole",
       "sts:SetContext"
   ]
}
```

### Create and configure your application in IAM Identity Center

###### Note

Before you begin, make sure that you’ve created the required IAM roles from the
previous step. You’ll need to specify one of these IAM roles in this step.

To create and configure a customer managed application in AWS IAM Identity Center,
perform the following steps:

1. Open the [IAM Identity
   Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Applications**.
3. Choose the **Customer managed** tab.
4. Choose **Add application**.
5. On the **Select application type** page, under **Setup
   preference**, choose **I have an application I want to set
   up**.
6. Under **Application type**, choose **OAuth
   2.0**.
7. Choose **Next**. The **Specify application**
   page is displayed.
8. Under the **Application name and description**section, enter a
   **Display name** for the application, such as
   `storage-browser-oauth`.
9. Enter a **Description**. The application description appears in
   the IAM Identity Center console and API requests, but not in the AWS access
   portal.
10. Under **User and group assignment method**, choose **Do
    not require assignments**. This option allows all authorized IAM Identity
    Center users and groups access to this application.
11. Under **AWS access portal**, enter an application URL where
    users can access the application.
12. (Optional) If you want to add a resource tag, enter the key and value pair. To add
    multiple resource tags, choose **Add new tag** to generate a new
    entry and enter the key and value pairs.
13. Choose **Next**. The **Specify authentication
    page** displays.
14. Under **Authentication with trusted token issuer**, use the
    checkbox to select the trusted token issuer that you previously created.
15. Under **Configure selected trusted token issuers**, enter the
    [aud claim](../../../singlesignon/latest/userguide/trusted-token-issuer-configuration-settings.md#trusted-token-issuer-aud-claim "../../../singlesignon/latest/userguide/trusted-token-issuer-configuration-settings.md#trusted-token-issuer-aud-claim"). The **aud claim** identifies the audience of
    the JSON Web Token (JWT), and it is the name by which the trusted token issuer
    identifies this application.

###### Note

You might need to contact the administrator of the external IdP to obtain this
information. 16. Choose **Next**. The **Specify authentication
credentials** page displays. 17. Under **Configuration method**, choose **Enter one or
more IAM roles**. 18. Under **Enter IAM roles**, add the [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") or Amazon Resource Name
(ARN) for the identity bearer token. You must enter the IAM role that you created from
the previous step for the identity broker application (for example,
`bootstrap-role`). 19. Choose **Next**. 20. On the **Review and configure** page, review the details of your
application configuration. If you need to modify any of the settings, choose
**Edit** for the section that you want to edit and make your
changes to. 21. Choose **Submit**. The details page of the application that you
just added is displayed.

After you’ve set up your applications, your users can access your applications from
within their AWS access portal based on the [permission sets that you’ve created](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") and the [user
access that you’ve assigned](../../../singlesignon/latest/userguide/get-started-assign-account-access-user.md "../../../singlesignon/latest/userguide/get-started-assign-account-access-user.md").

### Add S3 Access Grants as a trusted application for identity propagation

After you set up your customer managed application, you must specify S3 Access Grants for
identity propagation. S3 Access Grants vends credentials for users to access Amazon S3 data. When you sign in to your customer
managed application, S3 Access Grants will pass your user identity to the trusted application.

**Prerequisite:** Make sure that you’ve set up S3 Access Grants (such
as [creating an S3 Access Grants
instance](access-grants-instance-create.md "access-grants-instance-create.md") and [registering a
location](access-grants-location-register.md "access-grants-location-register.md")) before following these steps. For more information, see [Getting started with S3 Access Grants](access-grants-get-started.md "access-grants-get-started.md").

To add S3 Access Grants for identity propagation to your customer managed application, perform
the following steps:

1. Open the [IAM Identity
   Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Applications**.
3. Choose the **Customer managed** tab.
4. In the **Customer managed applications** list, select the OAuth
   2.0 application for which you want to initiate access requests. This is the
   application that your users will sign in to.
5. On the **Details** page, under **Trusted applications for
   identity propagation**, choose **Specify trusted
   applications**.
6. Under Setup type, select Individual applications and specify access, and then
   choose **Next**.
7. On the **Select service** page, choose
   **S3 Access Grants**. S3 Access Grants has applications that you can use to define your
   own web application for trusted identity propagation.
8. Choose **Next**. You'll select your applications in the next
   step.
9. On the **Select applications** page, choose **Individual
   applications**, select the checkbox for each application that can receive
   requests for access, and then choose **Next**.
10. On the **Configure access** page, under **Configuration
    method**, choose either of the following:
    - **Select access per application –** Select
      this option to configure different access levels for each application. Choose the
      application for which you want to configure the access level, and then choose
      **Edit access**. In **Level of access to
      apply**, change the access levels as needed, and then choose
      **Save changes**.
    - \***\*Apply same level of access to all
      applications** –\*\* Select this option if you don't
      need to configure access levels on a per-application basis.

11. Choose **Next**.
12. On the **Review configuration** page, review the choices that you
    made.

###### Note

You’ll want to make sure the `s3:access_grants:read_write` permission
is granted for your users. This permission allows your users to retrieve credentials
to access Amazon S3. Make sure to use either the IAM policy you created previously, or
S3 Access Grants, to limit access to write operations. 13. To make changes, choose **Edit** for the configuration section
that you want to make changes to. Then, make the required changes and choose
**Save changes**. 14. Choose **Trust applications** to add the trusted application for
identity propagation.

### Create a grant to a user or group

In this step, you use IAM Identity Center to provision your users. You can use SCIM
for [automated or manual
provisioning of users and groups](../../../singlesignon/latest/userguide/provision-automatically.md "../../../singlesignon/latest/userguide/provision-automatically.md"). SCIM keeps your IAM Identity Center
identities in sync with identities from your identity provider (IdP). This includes any
provisioning, updates, and deprovisioning of users between your IdP and IAM Identity
Center.

###### Note

This step is required because when S3 Access Grants is used with IAM Identity Center, local
IAM Identity Center users aren’t used. Instead, users must be synchronized from the
identity provider with IAM Identity Center.

To synchronize users from your identity provider with IAM Identity Center, perform
the following steps:

1. [Enable automatic
   provisioning](../../../singlesignon/latest/userguide/how-to-with-scim.md "../../../singlesignon/latest/userguide/how-to-with-scim.md").
2. [Generate an access token](../../../singlesignon/latest/userguide/generate-token.md "../../../singlesignon/latest/userguide/generate-token.md").

For examples of how to set up the identity provider with IAM Identity Center for
your specific use case, see
[IAM
Identity Center Identity source tutorials](../../../singlesignon/latest/userguide/tutorials.md "../../../singlesignon/latest/userguide/tutorials.md").

### Create your Storage Browser for S3 component

After you’ve set up your IAM Identity Center instance and created grants in S3 Access Grants,
open your React application. In the React application, use
`createManagedAuthAdapter` to set up the authorization rules. You must
provide a credentials provider to return the credentials you acquired from IAM Identity
Center. You can then call `createStorageBrowser` to initialize the
Storage Browser for S3 component:

```
import {
    createManagedAuthAdapter,
    createStorageBrowser,
} from '@aws-amplify/ui-react-storage/browser';
import '@aws-amplify/ui-react-storage/styles.css';

export const { StorageBrowser } = createStorageBrowser({
   config: createManagedAuthAdapter({
    credentialsProvider: async (options?: { forceRefresh?: boolean }) => {
      // return your credentials object
      return {
        credentials: {
          accessKeyId: '`my-access-key-id`',
          secretAccessKey: '`my-secret-access-key`',
          sessionToken: '`my-session-token`',
          expiration: new Date(),
        },
      }
    },
    // AWS `region` and `accountId` of the S3 Access Grants Instance.
    region: '',
    accountId: '',
    // call `onAuthStateChange` when end user auth state changes
    // to clear sensitive data from the `StorageBrowser` state
    registerAuthListener: (onAuthStateChange) => {},
  })
});
```

Then, create a mechanism to exchange the JSON web tokens (JWTs) from your web
application with the IAM credentials from IAM Identity Center. For more information
about how to exchange the JWT, see the following resources:

- [How to develop a user-facing data application with IAM Identity Center and
  S3 Access Grants](https://aws.amazon.com/blogs/storage/how-to-develop-a-user-facing-data-application-with-iam-identity-center-and-s3-access-grants-part-2/ "https://aws.amazon.com/blogs/storage/how-to-develop-a-user-facing-data-application-with-iam-identity-center-and-s3-access-grants-part-2/") post in _AWS Storage Blog_
- [Scaling data access with S3 Access Grants](https://aws.amazon.com/blogs/storage/scaling-data-access-with-amazon-s3-access-grants/ "https://aws.amazon.com/blogs/storage/scaling-data-access-with-amazon-s3-access-grants/") post in _AWS Storage
  Blog_
- [S3 Access Grants workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/77b0af63-6ad2-4c94-bfc0-270eb9358c7a/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/77b0af63-6ad2-4c94-bfc0-270eb9358c7a/en-US") on _AWS workshop studio_
- [S3 Access Grants workshop](https://github.com/aws-samples/s3-access-grants-workshop "https://github.com/aws-samples/s3-access-grants-workshop") on _GitHub_

Then, set up an API endpoint to handle requests for fetching credentials. To validate
the JSON web token (JWT) exchange, perform the following steps:

1. Retrieve the JSON web token from the authorization header for incoming
   requests.
2. Validate the token using the public keys from the specified JSON web key set
   (JWKS) URL.
3. Verify the token's expiration, issuer, subject, and audience claims.

To exchange the identity provider’s JSON web token with AWS IAM credentials,
perform the following steps:

###### Tip

Make sure to avoid logging any sensitive information. We recommend that you use
error handling controls for missing authorization, expired tokens, and other exceptions.
For more information, see the [Implementing AWS Lambda error handling patterns](https://aws.amazon.com/blogs/compute/implementing-aws-lambda-error-handling-patterns/ "https://aws.amazon.com/blogs/compute/implementing-aws-lambda-error-handling-patterns/") post in _AWS Compute
Blog_.

1. Verify that the required **Permission** and
   **Scope** parameters are provided in the request.
2. Use the [CreateTokenWithIAM](../../../singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.md "../../../singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.md") API to exchange the JSON web token for an IAM Identity
   Center token.

###### Note

After the IdP JSON web token is used, it can’t be used again. A new token must
be used to exchange with IAM Identity Center. 3. Use the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API operation
to assume a transient role using the IAM Identity Center token. Make sure to use the
identity bearer role, also known as the role that carries the identity context (for
example, `identity-bearer-role`) to request the
credentials. 4. Return the IAM credentials to the web application.

###### Note

Make sure that you’ve set up a proper logging mechanism. Responses are returned
in a standardized JSON format with an appropriate HTTP status code.

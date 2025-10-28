# IAM Identity Center Trusted Identity Propagation Support for OpenSearch

You can now use your centrally configured AWS IAM Identity Center principals (users and groups) via
[Trusted
Identity Propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md") to access Amazon OpenSearch Service domains through [OpenSearch Service applications](application.md "application.md") . In order to enable IAM Identity Center support for
OpenSearch, you will need to enable use of IAM Identity Center To learn more on how to do this, see
[What is
IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md"). See [How to associate OpenSearch domain as
datasource in OpenSearch applications?](application.md "application.md") for details.

You can configure IAM Identity Center by using the OpenSearch Service console, the AWS Command Line Interface (AWS CLI), or the AWS
SDKs.

###### Note

IAM Identity Center principals are not supported through [Dashboards
(co-located with cluster)](dashboards.md "dashboards.md"). They are only supported through [Centralized OpenSearch user interface (Dashboards)](application.md "application.md").

## Considerations

Before you use IAM Identity Center with Amazon OpenSearch Service you must consider the following:

- IAM Identity Center is enabled in the account.
- IAM Identity Center is available in your [Region](opensearch-ui-endpoints-quotas.md "opensearch-ui-endpoints-quotas.md").
- The OpenSearch domain version is 1.3 or later.
- [Fine Grained Access Control](fgac.md "fgac.md") is enabled on the
  domain.
- Domain is in the same Region as IAM Identity Center instance.
- Domain and [OpenSearch application](application.md "application.md") belong
  to the same AWS account.

## Modifying the domain access policy

Before you configure IAM Identity Center, you must update the domain access policy or the
permissions of the IAM role configured in OpenSearch applications for Trusted Identity
Propagation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/OpenSearchRole"
 },
 "Action": "es:ESHttp*",
 "Resource": "arn:aws:es:`us-east-1`:`111122223333`:domain/example-domain/*"
 }
 ]
}`

```

## Configuring IAM Identity Center authentication and

authorization (Console)

You can enable IAM Identity Center authentication and authorization during the domain creation
process or by updating an existing domain. The set-up steps vary slightly depending on
which option you choose.

The following steps explain how to configure an existing domain for IAM Identity Center
authentication and authorization in the Amazon OpenSearch Service console:

1. Under **Domain configuration**, navigate to
   **Security Configuration**, choose Edit and
   navigate to IAM Identity Center Authentication section and select **Enable API access authenticated with IAM Identity Center**.
2. Select the SubjectKey and Roles key as follows.
   - **Subject key** - choose one of UserId
     (default), UserName and Email to use corresponding attribute as
     principal accessing the domain.
   - **Roles key** - choose one of GroupId
     (default) and GroupName to use corresponding attribute values as backend
     role for [fine-grained-access-control](fgac.md "fgac.md") for all
     the groups associated with the IdC principal.

After you've made your changes, save your domain.

## Configuring fine-grained access control

Once you have enabled IAM Identity Center option on your OpenSearch domain, you can configure
access to IAM Identity Center principals by [creating role mapping to the
backend role](fgac.md#fgac-mapping "fgac.md#fgac-mapping"). The backend role value for
the principal is based on the IdC principal’s group membership and the RolesKey
configuration of GroupId or GroupName.

###### Note

Amazon OpenSearch Service can support up to **100 groups** for a
single user. If you try to use more than the number of allowed instances, you will
experience inconsistency with your fine-grained-access-control authorization
processing and receive a 403error message.

## Configuring IAM Identity Center authentication and authorization

(CLI)

```

	 aws opensearch update-domain-config \
	     --domain-name `my-domain` \
	     --identity-center-options '{"EnabledAPIAccess": `true`, "IdentityCenterInstanceARN": "`instance arn`",  "SubjectKey": "`UserId/UserName/UserEmail`" , "RolesKey": "`GroupId/GroupName`"}'

```

## Disabling IAM Identity Center authentication on the

domain

To disable IAM Identity Center on your OpenSearch domain:

1. Choose the domain, **Actions**, and **Edit security
   configuration**.
2. Uncheck **Enable API access authenticated with
   IAM Identity Center**.
3. Choose **Save changes**.
4. After the domain finishes processing, remove [role
   mappings](fgac.md "fgac.md") added for IdC principals

To disable IAM Identity Center through CLI, you can use following

```

	 aws opensearch update-domain-config \
	     --domain-name `my-domain` \
	     --identity-center-options '{"EnabledAPIAccess": `false`}'

```

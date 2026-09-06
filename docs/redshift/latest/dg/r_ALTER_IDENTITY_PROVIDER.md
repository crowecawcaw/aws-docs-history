

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ALTER IDENTITY PROVIDER
<a name="r_ALTER_IDENTITY_PROVIDER"></a>

Alters an identity provider to assign new parameters and values. When you run this command, all previously set parameter values are deleted before the new values are assigned. Only a superuser can alter an identity provider.

## Syntax
<a name="r_ALTER_IDENTITY_PROVIDER-synopsis"></a>

```
ALTER IDENTITY PROVIDER identity_provider_name
[PARAMETERS parameter_string]
[NAMESPACE namespace]
[IAM_ROLE iam_role]
[AUTO_CREATE_ROLES
    [ TRUE [ { INCLUDE | EXCLUDE } GROUPS LIKE filter_pattern] |
      FALSE
    ]
[DISABLE | ENABLE]
```

## Parameters
<a name="r_ALTER_IDENTITY_PROVIDER-parameters"></a>

 *identity\_provider\_name*   
Name of the new identity provider. For more information about valid names, see [Names and identifiers](r_names.md).

 *parameter\_string*   
A string containing a properly formatted JSON object that contains parameters and values required for the specific identity provider.

 *namespace*   
The organization namespace.

 *iam\_role*   
The IAM role that provides permissions for the connection to IAM Identity Center. This parameter is applicable only when the identity-provider type is AWSIDC.

 *auto\_create\_roles*   
Enables or disables the auto-create role feature. If the value is TRUE, Amazon Redshift enables the auto-create role feature. If the value is FALSE, Amazon Redshift disables the auto-create role feature. If the value for this parameter isn't specified, Amazon Redshift determines the value using the following logic:   
+  If `AUTO_CREATE_ROLES` is provided but the value isn't specified, the value is set to TRUE. 
+  If `AUTO_CREATE_ROLES` isn't provided and the identity provider is AWSIDC, the value is set to FALSE. 
+  If `AUTO_CREATE_ROLES` isn't provided and the identity provider is Azure, the value is set to TRUE. 
To include groups, specify `INCLUDE`. The default is empty, which means include all groups if `AUTO_CREATE_ROLES` is on.  
To exclude groups, specify `EXCLUDE`. The default is empty, which means do not exclude any groups if `AUTO_CREATE_ROLES` is on.

 *filter\_pattern*   
A valid UTF-8 character expression with a pattern to match group names. The LIKE option performs a case-sensitive match that supports the following pattern-matching metacharacters:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_IDENTITY_PROVIDER.html)
If *filter\_pattern* does not contain metacharacters, then the pattern only represents the string itself; in that case LIKE acts the same as the equals operator.   
*filter\_pattern* supports the following characters:  
+  Uppercase and lowercase alphabetic characters (A-Z and a-z) 
+  Numerals (0-9) 
+  The following special characters: 

  ```
  _ % ^ * + ? { } , $
  ```

 *DISABLE or ENABLE*   
Turns an identity provider on or off. The default is ENABLE.

## Examples
<a name="r_ALTER_IDENTITY_PROVIDER-examples"></a>

The following example alters an identity provider named *oauth\_standard*. It applies specifically to when Microsoft Azure AD is the identity provider.

```
ALTER IDENTITY PROVIDER oauth_standard
PARAMETERS '{"issuer":"https://sts.windows.net/2sdfdsf-d475-420d-b5ac-667adad7c702/",
"client_id":"87f4aa26-78b7-410e-bf29-57b39929ef9a",
"client_secret":"BUAH~ewrqewrqwerUUY^%tHe1oNZShoiU7",
"audience":["https://analysis.windows.net/powerbi/connector/AmazonRedshift"]
}'
```

The following sample shows how to set the identity-provider namespace. This can apply to Microsoft Azure AD, if it follows a statement like the previous sample, or to another identity provider. It can also apply to a case where you connect an existing Amazon Redshift provisioned cluster or Amazon Redshift Serverless workgroup to IAM Identity Center, if you have a connection set up through a managed application.

```
ALTER IDENTITY PROVIDER "my-redshift-idc-application"
NAMESPACE 'MYCO';
```

The following sample sets the IAM role and works in the use case for configuring Redshift integration with IAM Identity Center.

```
ALTER IDENTITY PROVIDER "my-redshift-idc-application"
IAM_ROLE 'arn:aws:iam::123456789012:role/myadministratorrole';
```

For more information about setting up a connection to IAM Identity Center from Redshift, see [Connect Redshift with IAM Identity Center to give users a single sign-on experience](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect.html).

**Disabling an identity provider**

The following sample statement shows how to disable an identity provider. When it's disabled, federated users from the identity provider can't login to the cluster until it's enabled again.

```
ALTER IDENTITY PROVIDER "redshift-idc-app" DISABLE;
```
# Distribution tenant customizations

When using a multi-tenant distribution, your distribution tenants inherit the multi-tenant distribution configuration. However, you
can customize some settings at the distribution tenant level.

You can customize the following:

- **Parameters** – Parameters are key-value pairs that you
  can use for the origin domain or origin paths. See [How parameters work with distribution tenants](#tenant-customize-parameters "#tenant-customize-parameters").
- **AWS WAF web ACL (V2)** – You can specify a separate web
  ACL for the distribution tenant, which will _override_ the web ACL used for
  the multi-tenant distribution. You can also disable this setting for a specific distribution tenant, which
  means the distribution tenant won't inherit the web ACL protections from the multi-tenant distribution. For
  more information, see [AWS WAF web ACL](DownloadDistValuesGeneral.md#DownloadDistValuesWAFWebACL "DownloadDistValuesGeneral.md#DownloadDistValuesWAFWebACL").
- **Geographic restrictions** – Geographic restrictions that
  you specify for a distribution tenant will _override_ any geographic
  restrictions for the multi-tenant distribution. For example, if you block Germany (DE) in your
  multi-tenant distribution, all associated distribution tenants will also block DE. However, if you allow DE
  for a specific distribution tenant, that distribution tenant settings will override the settings for the
  multi-tenant distribution. For more information, see [Restrict the geographic distribution of your content](georestrictions.md "georestrictions.md").
- **Invalidation paths** – Specify the file paths to the
  content that you want to invalidate for the distribution tenant. For more information, see
  [Invalidate files](Invalidation_Requests.md "Invalidation_Requests.md").
- **Custom TLS certificates** – AWS Certificate Manager (ACM)
  certificates that you specify for distribution tenants are supplemental to the certificate
  provided in the multi-tenant distribution. However, if the same domain is covered by both the
  multi-tenant distribution and distribution tenant certificates, then the tenant certificate is used. For more
  information, see [Request certificates for your
  CloudFront distribution tenant](managed-cloudfront-certificates.md "managed-cloudfront-certificates.md").
- **Domain names** – You must specify at least one domain
  name per distribution tenant.

## How parameters work with distribution tenants

A parameter is a key-value pair that you can use for placeholder values. Define the
parameters that you want to use in your multi-tenant distribution and specify whether they're
required.

When you define parameters in your multi-tenant distribution, you choose whether those parameters are
required to be entered at the distribution tenant level.

- If you define the parameters as _required_ in the
  multi-tenant distribution, then they must be entered at the distribution tenant level. (They are not
  inherited).
- If the parameters are _not required_, then you can provide
  a default value in the multi-tenant distribution that is inherited by the distribution tenant.

You can use parameters in the following properties:

- Origin domain name
- Origin path

In the multi-tenant distribution, you can define up to two parameters for each of the preceding
properties.

## Example parameters

See the following examples for using parameters for the domain name and origin
path.

**Domain name parameters**

In the multi-tenant distribution configuration, you can define a parameter for the origin domain name
like the following examples:

###### Amazon S3

- `{{`parameter1`}}.amzn-s3-demo-logging-bucket.s3.us-east-1.amazonaws.com`
- `{{`parameter1`}}–amzn-s3-demo-logging-bucket.s3.us-east-1.amazonaws.com`

###### Custom origins

- `{{`parameter1`}}.lambda-url.us-east-1.on.aws`
- `{{`parameter1`}}.mediapackagev2.ap-south-1.amazonaws.com`

When you create a distribution tenant, specify the value to use for
`parameter1`.

```
"Parameters": [
  {
    "Name": "parameter1",
    "Value": "mycompany-website"
  }
]

```

Using the previous examples specified in the multi-tenant distribution, the origin domain name for
the distribution tenant resolves to the following:

- ``mycompany-website`.amzn-s3-demo-bucket3.s3.us-east-1.amazonaws.com`
- ``mycompany-website`–amzn-s3-demo-bucket3.s3.us-east-1.amazonaws.com`
- ``mycompany-website`.lambda-url.us-east-1.on.aws`
- ``mycompany-website`.mediapackagev2.ap-south-1.amazonaws.com`

**Origin path parameters**

Similarly, you can define parameters for the origin path in the multi-tenant distribution like the
following examples:

- `/{{``parameter2``}}`
- `/{{``parameter2``}}/test`
- `/public/{{``parameter2``}}/test`
- `/search?name={{``parameter2``}}`

When you create a distribution tenant, specify the value to use for
`parameter2`.

```
"Parameters": [
  {
    "Name": "parameter2",
    "Value": "myBrand"
  }
]

```

Using the previous examples specified in the multi-tenant distribution, the origin path for the
distribution tenant resolves to the following:

- `/`myBrand``
- `/`myBrand`/test`
- `/public/`myBrand`/test`
- `/search?name=`myBrand``

###### Example

You want to create multiple websites (tenants) for your customers, and you need to
ensure that each distribution tenant resource uses the correct values.

1. You create a multi-tenant distribution and include two parameters for the distribution tenant
   configuration.
2. For the origin domain name, you create a parameter named
   `customer-name` and specify that it's required.
   You enter the parameter before the S3 bucket, so that it appears as:

`{{`customer-name`}}.amzn-s3-demo-bucket3.s3.us-east-1.amazonaws.com`. 3. For origin path, you create a second parameter named
`my-theme`, and specify that it's optional,
with a default value of `basic`. Your origin path
appears as: `/{{`my-theme`}}` 4. When you create a distribution tenant:

    * For domain name, you must specify a value for
     `customer-name`, because it's marked as
     required in the multi-tenant distribution.
    * For origin path, you can optionally specify a value for
     `my-theme` or use the default
     value.

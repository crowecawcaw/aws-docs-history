# Create cache policies

You can use a cache policy to improve your cache hit ratio by controlling the values
(URL query strings, HTTP headers, and cookies) that are included in the cache key. You
can create a cache policy in the CloudFront console, with the AWS Command Line Interface (AWS CLI), or with the
CloudFront API.

After you create a cache policy, you attach it to one or more cache behaviors in a
CloudFront distribution.

Console

###### To create a cache policy (console)

1. Sign in to the AWS Management Console and open the
   **Policies** page in the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home?#/policies](https://console.aws.amazon.com/cloudfront/v4/home?#/policies "https://console.aws.amazon.com/cloudfront/v4/home?#/policies").
2. Choose **Create cache policy**.
3. Choose the desired setting for this cache policy. For more
   information, see [Understand cache policies](cache-key-understand-cache-policy.md "cache-key-understand-cache-policy.md").
4. When finished, choose **Create**.

After you create a cache policy, you can attach it to a cache
behavior.

###### To attach a cache policy to an existing distribution (console)

1. Open the **Distributions** page in the CloudFront
   console at [https://console.aws.amazon.com/cloudfront/v4/home#/distributions](https://console.aws.amazon.com/cloudfront/v4/home#/distributions "https://console.aws.amazon.com/cloudfront/v4/home#/distributions").
2. Choose the distribution to update, then choose the
   **Behaviors** tab.
3. Choose the cache behavior to update, then choose
   **Edit**.

Or, to create a new cache behavior, choose **Create
behavior**. 4. In the **Cache key and origin requests** section,
make sure that **Cache policy and origin request
policy** is chosen. 5. For **Cache policy**, choose the cache policy to
attach to this cache behavior. 6. At the bottom of the page, choose **Save
changes**.

###### To attach a cache policy to a new distribution (console)

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose **Create distribution**.
3. In the **Cache key and origin requests** section,
   make sure that **Cache policy and origin request
   policy** is chosen.
4. For **Cache policy**, choose the cache policy to
   attach to this distribution's default cache behavior.
5. Choose the desired settings for the origin, default cache
   behavior, and other distribution settings. For more information, see
   [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").
6. When finished, choose **Create
   distribution**.

CLI
To create a cache policy with the AWS Command Line Interface (AWS CLI), use the **aws
cloudfront create-cache-policy** command. You can use an input
file to provide the command's input parameters, rather than specifying each
individual parameter as command line input.

###### To create a cache policy (CLI with input file)

1. Use the following command to create a file named
   `cache-policy.yaml` that contains all of the
   input parameters for the **create-cache-policy**
   command.

```

aws cloudfront create-cache-policy --generate-cli-skeleton yaml-input > cache-policy.yaml
```

2. Open the file named `cache-policy.yaml` that
   you just created. Edit the file to specify the cache policy settings
   that you want, then save the file. You can remove optional fields
   from the file, but don't remove the required fields.

For more information about the cache policy settings, see [Understand cache policies](cache-key-understand-cache-policy.md "cache-key-understand-cache-policy.md"). 3. Use the following command to create the cache policy using input
parameters from the `cache-policy.yaml`
file.

```

aws cloudfront create-cache-policy --cli-input-yaml file://cache-policy.yaml
```

Make note of the `Id` value in the command's output.
This is the cache policy ID, and you need it to attach the cache
policy to a CloudFront distribution's cache behavior.

###### To attach a cache policy to an existing distribution (CLI with input file)

1. Use the following command to save the distribution configuration
   for the CloudFront distribution that you want to update. Replace
   `distribution_ID` with the
   distribution's ID.

```

aws cloudfront get-distribution-config --id `distribution_ID` --output yaml > dist-config.yaml
```

2.  Open the file named `dist-config.yaml` that you
    just created. Edit the file, making the following changes to each
    cache behavior that you are updating to use a cache policy.

        * In the cache behavior, add a field named
         `CachePolicyId`. For the field's value, use
         the cache policy ID that you noted after creating the
         policy.
        * Remove the `MinTTL`, `MaxTTL`,
         `DefaultTTL`, and
         `ForwardedValues` fields from the cache
         behavior. These settings are specified in the cache policy,
         so you can't include these fields and a cache policy in the
         same cache behavior.
        * Rename the `ETag` field to
         `IfMatch`, but don't change the field's
         value.

    Save the file when finished.

3.  Use the following command to update the distribution to use the
    cache policy. Replace `distribution_ID`
    with the distribution's ID.

```

aws cloudfront update-distribution --id `distribution_ID` --cli-input-yaml file://dist-config.yaml
```

###### To attach a cache policy to a new distribution (CLI with input file)

1. Use the following command to create a file named
   `distribution.yaml` that contains all of the
   input parameters for the **create-distribution**
   command.

```

aws cloudfront create-distribution --generate-cli-skeleton yaml-input > distribution.yaml
```

2. Open the file named `distribution.yaml` that
   you just created. In the default cache behavior, in the
   `CachePolicyId` field, enter the cache policy ID that
   you noted after creating the policy. Continue editing the file to
   specify the distribution settings that you want, then save the file
   when finished.

For more information about the distribution settings, see [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md"). 3. Use the following command to create the distribution using input
parameters from the `distribution.yaml`
file.

```

aws cloudfront create-distribution --cli-input-yaml file://distribution.yaml
```

API
To create a cache policy with the CloudFront API, use [CreateCachePolicy](../../../cloudfront/latest/APIReference/API_CreateCachePolicy.md "../../../cloudfront/latest/APIReference/API_CreateCachePolicy.md"). For more information about the fields that
you specify in this API call, see [Understand cache policies](cache-key-understand-cache-policy.md "cache-key-understand-cache-policy.md") and the API
reference documentation for your AWS SDK or other API client.

After you create a cache policy, you can attach it to a cache behavior,
using one of the following API calls:

- To attach it to a cache behavior in an existing distribution, use
  [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md").
- To attach it to a cache behavior in a new distribution, use [CreateDistribution](../../../cloudfront/latest/APIReference/API_CreateDistribution.md "../../../cloudfront/latest/APIReference/API_CreateDistribution.md").

For both of these API calls, provide the cache policy's ID in the
`CachePolicyId` field, inside a cache behavior. For more
information about the other fields that you specify in these API calls, see
[All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md") and the API reference
documentation for your AWS SDK or other API client.

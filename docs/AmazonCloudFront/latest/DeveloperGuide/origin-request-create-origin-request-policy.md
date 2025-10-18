# Create origin request
 policies

You can use an origin request policy to control the values (URL query strings, HTTP
 headers, and cookies) that are included in requests that CloudFront sends to your origin. You
 can create an origin request policy in the CloudFront console, with the AWS Command Line Interface (AWS CLI), or
 with the CloudFront API.

After you create an origin request policy, you attach it to one or more cache
 behaviors in a CloudFront distribution.

Origin request policies are not required. When a cache behavior does not have an
 origin request policy attached, the origin request includes all the values that are
 specified in the [cache policy](cache-key-understand-cache-policy.md "cache-key-understand-cache-policy.md"),
 but nothing more.

###### Note

To use an origin request policy, the cache behavior must also use a [cache policy](controlling-the-cache-key.md "controlling-the-cache-key.md"). You cannot use an origin
 request policy in a cache behavior without a cache policy.


Console
###### To create an origin request policy (console)

1. Sign in to the AWS Management Console and open the
 **Policies** page in the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home?#/policies](https://console.aws.amazon.com/cloudfront/v4/home?#/policies "https://console.aws.amazon.com/cloudfront/v4/home?#/policies").
2. Choose **Origin request**, then choose
 **Create origin request policy**.
3. Choose the desired setting for this origin request policy. For
 more information, see [Understand origin
 request policies](origin-request-understand-origin-request-policy.md "origin-request-understand-origin-request-policy.md").
4. When finished, choose **Create**.

After you create an origin request policy, you can attach it to a cache
 behavior.


###### To attach an origin request policy to an existing distribution
 (console)

1. Open the **Distributions** page in the CloudFront console
 at [https://console.aws.amazon.com/cloudfront/v4/home#/distributions](https://console.aws.amazon.com/cloudfront/v4/home#/distributions "https://console.aws.amazon.com/cloudfront/v4/home#/distributions").
2. Choose the distribution to update, then choose the
 **Behaviors** tab.
3. Choose the cache behavior to update, then choose
 **Edit**.


Or, to create a new cache behavior, choose **Create
 behavior**.
4. In the **Cache key and origin requests** section,
 make sure that **Cache policy and origin request
 policy** is chosen.
5. For **Origin request policy**, choose the origin
 request policy to attach to this cache behavior.
6. At the bottom of the page, choose **Save
 changes**.

###### To attach an origin request policy to a new distribution
 (console)

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose **Create distribution**.
3. In the **Cache key and origin requests** section,
 make sure that **Cache policy and origin request
 policy** is chosen.
4. For **Origin request policy**, choose the origin
 request policy to attach to this distribution's default cache
 behavior.
5. Choose the desired settings for the origin, default cache
 behavior, and other distribution settings. For more information, see
 [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").
6. When finished, choose **Create
 distribution**.


CLI
To create an origin request policy with the AWS Command Line Interface (AWS CLI), use the
 **aws cloudfront create-origin-request-policy** command. You can
 use an input file to provide the command's input parameters, rather than
 specifying each individual parameter as command line input.


###### To create an origin request policy (CLI with input file)

1. Use the following command to create a file named
 `origin-request-policy.yaml` that contains all of the
 input parameters for the **create-origin-request-policy**
 command.



```

aws cloudfront create-origin-request-policy --generate-cli-skeleton yaml-input > origin-request-policy.yaml
```
2. Open the file named `origin-request-policy.yaml`
 that you just created. Edit the file to specify the origin request
 policy settings that you want, then save the file. You can remove
 optional fields from the file, but don't remove the required
 fields.


For more information about the origin request policy settings, see
 [Understand origin
 request policies](origin-request-understand-origin-request-policy.md "origin-request-understand-origin-request-policy.md").
3. Use the following command to create the origin request policy using
 input parameters from the
 `origin-request-policy.yaml` file.



```

aws cloudfront create-origin-request-policy --cli-input-yaml file://origin-request-policy.yaml
```

Make note of the `Id` value in the command's output. This
 is the origin request policy ID, and you need it to attach the origin
 request policy to a CloudFront distribution's cache behavior.

###### To attach an origin request policy to an existing distribution (CLI with
 input file)

1. Use the following command to save the distribution configuration for
 the CloudFront distribution that you want to update. Replace
 `distribution_ID` with the distribution's
 ID.



```

aws cloudfront get-distribution-config --id `distribution_ID` --output yaml > dist-config.yaml
```
2. Open the file named `dist-config.yaml` that you
 just created. Edit the file, making the following changes to each cache
 behavior that you are updating to use an origin request policy.




	* In the cache behavior, add a field named
	 `OriginRequestPolicyId`. For the field's value, use
	 the origin request policy ID that you noted after creating the
	 policy.
	* Rename the `ETag` field to `IfMatch`,
	 but don't change the field's value.
Save the file when finished.
3. Use the following command to update the distribution to use the origin
 request policy. Replace `distribution_ID` with
 the distribution's ID.



```

aws cloudfront update-distribution --id `distribution_ID` --cli-input-yaml file://dist-config.yaml
```

###### To attach an origin request policy to a new distribution (CLI with
 input file)

1. Use the following command to create a file named
 `distribution.yaml` that contains all of the input
 parameters for the **create-distribution**
 command.



```

aws cloudfront create-distribution --generate-cli-skeleton yaml-input > distribution.yaml
```
2. Open the file named `distribution.yaml` that you
 just created. In the default cache behavior, in the
 `OriginRequestPolicyId` field, enter the origin request
 policy ID that you noted after creating the policy. Continue editing the
 file to specify the distribution settings that you want, then save the
 file when finished.


For more information about the distribution settings, see [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").
3. Use the following command to create the distribution using input
 parameters from the `distribution.yaml` file.



```

aws cloudfront create-distribution --cli-input-yaml file://distribution.yaml
```


API
To create an origin request policy with the CloudFront API, use [CreateOriginRequestPolicy](../../../cloudfront/latest/APIReference/API_CreateOriginRequestPolicy.md "../../../cloudfront/latest/APIReference/API_CreateOriginRequestPolicy.md"). For more information about the fields
 that you specify in this API call, see [Understand origin
 request policies](origin-request-understand-origin-request-policy.md "origin-request-understand-origin-request-policy.md") and the
 API reference documentation for your AWS SDK or other API client.


After you create an origin request policy, you can attach it to a cache
 behavior, using one of the following API calls:



* To attach it to a cache behavior in an existing distribution, use
 [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md").
* To attach it to a cache behavior in a new distribution, use [CreateDistribution](../../../cloudfront/latest/APIReference/API_CreateDistribution.md "../../../cloudfront/latest/APIReference/API_CreateDistribution.md").

For both of these API calls, provide the origin request policy's ID in the
 `OriginRequestPolicyId` field, inside a cache behavior. For more
 information about the other fields that you specify in these API calls, see
 [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md") and the API reference
 documentation for your AWS SDK or other API client.

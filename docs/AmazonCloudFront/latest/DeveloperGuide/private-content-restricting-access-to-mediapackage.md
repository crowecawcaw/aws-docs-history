# Restrict access to an
 AWS Elemental MediaPackage v2 origin

CloudFront provides *origin access control* (OAC) for restricting
 access to a MediaPackage v2 origin.

###### Note

CloudFront OAC only supports MediaPackage v2. MediaPackage v1 isn't supported.

###### Topics

* [Creating a new OAC](#create-oac-overview-mediapackage "#create-oac-overview-mediapackage")
* [Advanced settings for origin access
 control](#oac-advanced-settings-mediapackage "#oac-advanced-settings-mediapackage")

## Creating a new OAC


Complete the steps described in the following topics to set up a new OAC in CloudFront.


###### Topics

* [Prerequisites](#oac-prerequisites-mediapackage "#oac-prerequisites-mediapackage")
* [Grant CloudFront permission to access the
 MediaPackage v2 origin](#oac-permission-to-access-mediapackage "#oac-permission-to-access-mediapackage")
* [Creating the OAC](#create-oac-mediapackage "#create-oac-mediapackage")

### Prerequisites


Before you create and set up OAC, you must have a CloudFront distribution with a MediaPackage v2
 origin. For more information, see [Use a MediaStore container or a MediaPackage channel](DownloadDistS3AndCustomOrigins.md#concept_AWS_Media "DownloadDistS3AndCustomOrigins.md#concept_AWS_Media").


### Grant CloudFront permission to access the
 MediaPackage v2 origin


Before you create an OAC or set it up in a CloudFront distribution, make sure that CloudFront has
 permission to access the MediaPackage v2 origin. Do this after you create a CloudFront distribution, but
 before you add the OAC to the MediaPackage v2 origin in the distribution configuration.


Use an IAM policy to allow the CloudFront service principal
 (`cloudfront.amazonaws.com`) to access the origin. The `Condition`
 element in the policy allows CloudFront to access the MediaPackage v2 origin *only*
 when the request is on behalf of the CloudFront distribution that contains the MediaPackage v2 origin.
 This is the distribution with the MediaPackage v2 origin that you want to add OAC to.


###### Example : IAM policy that allows read-only access for a CloudFront distribution with OAC
 enabled

The following policy allows the CloudFront distribution
 (``E1PDK09ESKHJWT``) access to the MediaPackage v2
 origin. The origin is the ARN specified for the `Resource` element.


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "AllowCloudFrontServicePrincipal",
 "Effect": "Allow",
 "Principal": {"Service": "cloudfront.amazonaws.com"},
 "Action": "mediapackagev2:GetObject",
 "Resource": "arn:aws:mediapackagev2:us-east-1:123456789012:channelGroup/`channel-group-name`/channel/`channel-name`/originEndpoint/`origin_endpoint_name`",
 "Condition": {
 "StringEquals": {"AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/`E1PDK09ESKHJWT`"}
 }
 }
 ]
}`

```





###### Notes


* If you enabled the MQAR feature and origin access control (OAC), add the `mediapackagev2:GetHeadObject` action to the IAM policy. MQAR requires this permission to send `HEAD` requests to the MediaPackage v2 origin. For more information about MQAR, see [Media quality-aware resiliency](media-quality-score.md "media-quality-score.md").
* If you create a distribution that doesn't have permission to your MediaPackage v2 origin,
 you can choose **Copy policy** from the CloudFront console and then choose
 **Update endpoint permissions**. You can then attach the copied
 permission to the endpoint. For more information, see [Endpoint policy fields](https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints-policy.html "https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints-policy.html") in the *AWS Elemental MediaPackage User Guide*.

### Creating the OAC


To create an OAC, you can use the AWS Management Console, AWS CloudFormation, the AWS CLI, or the CloudFront API.



Console
###### To create an OAC

1. Sign in to the AWS Management Console and open the CloudFront console at
 [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Origin access**.
3. Choose **Create control setting**.
4. On the **Create new OAC** form, do the following:


	1. Enter a **Name** and (optionally) a
	 **Description** for the OAC.
	2. For **Signing behavior**, we recommend that you leave the
	 default setting (**Sign requests (recommended)**). For more
	 information, see [Advanced settings for origin access
	 control](#oac-advanced-settings-mediapackage "#oac-advanced-settings-mediapackage").
5. For **Origin type**, choose **MediaPackage V2**.
6. Choose **Create**.


###### Tip

After you create the OAC, make note of the **Name**. You
 need this in the following procedure.

###### To add an OAC to a MediaPackage v2 origin in a distribution

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose a distribution with a MediaPackage V2 origin that you want to add the OAC to,
 then choose the **Origins** tab.
3. Select the MediaPackage v2 origin that you want to add the OAC to, then choose
 **Edit**.
4. Select **HTTPS only** for your origin's
 **Protocol**.
5. From the **Origin access control** dropdown, choose the OAC
 name that you want to use.
6. Choose **Save changes**.

The distribution starts deploying to all of the CloudFront edge locations. When an edge
 location receives the new configuration, it signs all requests that it sends to the
 MediaPackage v2 origin.



CloudFormation
To create an OAC with AWS CloudFormation, use the
 `AWS::CloudFront::OriginAccessControl` resource type. The following
 example shows the AWS CloudFormation template syntax, in YAML format, for creating an OAC.



```
Type: AWS::CloudFront::OriginAccessControl
Properties: 
  OriginAccessControlConfig: 
      Description: An optional description for the origin access control
      Name: ExampleOAC
      OriginAccessControlOriginType: mediapackagev2
      SigningBehavior: always
      SigningProtocol: sigv4
```

For more information, see [AWS::CloudFront::OriginAccessControl](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originaccesscontrol.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originaccesscontrol.md") in the *AWS CloudFormation User Guide*.



CLI
To create an origin access control with the AWS Command Line Interface (AWS CLI), use the
 **aws cloudfront create-origin-access-control** command. You can use
 an input file to provide the input parameters for the command, rather than specifying
 each individual parameter as command line input.


###### To create an origin access control (CLI with input file)

1. Use the following command to create a file that's named
 `origin-access-control.yaml`. This file contains all of the
 input parameters for the **create-origin-access-control**
 command.



```

aws cloudfront create-origin-access-control --generate-cli-skeleton yaml-input > origin-access-control.yaml
```
2. Open the `origin-access-control.yaml` file that you just
 created. Edit the file to add a name for the OAC, a description (optional), and
 change the `SigningBehavior` to `always`. Then save the
 file.


For information about other OAC settings, see [Advanced settings for origin access
 control](#oac-advanced-settings-mediapackage "#oac-advanced-settings-mediapackage").
3. Use the following command to create the origin access control using the input
 parameters from the `origin-access-control.yaml` file.



```

aws cloudfront create-origin-access-control --cli-input-yaml file://origin-access-control.yaml
```

Make note of the `Id` value in the command output. You need it to
 add the OAC to a MediaPackage v2 origin in a CloudFront distribution.

###### To attach an OAC to a MediaPackage v2 origin in an existing distribution (CLI with
 input file)

1. Use the following command to save the distribution configuration for the CloudFront
 distribution that you want to add the OAC to. The distribution must have a MediaPackage
 v2 origin.



```

aws cloudfront get-distribution-config --id `<CloudFront distribution ID>` --output yaml > dist-config.yaml
```
2. Open the file that's named `dist-config.yaml` that you just
 created. Edit the file, making the following changes:




	* In the `Origins` object, add the OAC's ID to the field that's
	 named `OriginAccessControlId`.
	* Remove the value from the field that's named
	 `OriginAccessIdentity`, if one exists.
	* Rename the `ETag` field to `IfMatch`, but don't
	 change the field's value.
Save the file when finished.
3. Use the following command to update the distribution to use the origin access
 control.



```

aws cloudfront update-distribution --id `<CloudFront distribution ID>` --cli-input-yaml file://dist-config.yaml
```

The distribution starts deploying to all of the CloudFront edge locations. When an edge
 location receives the new configuration, it signs all requests that it sends to the
 MediaPackage v2 origin.



API
To create an OAC with the CloudFront API, use [CreateOriginAccessControl](../../../cloudfront/latest/APIReference/API_CreateOriginAccessControl.md "../../../cloudfront/latest/APIReference/API_CreateOriginAccessControl.md"). For more information about the fields that you
 specify in this API call, see the API reference documentation for your AWS SDK or
 other API client.


After you create an OAC you can attach it to a MediaPackage v2 origin in a distribution,
 using one of the following API calls:



* To attach it to an existing distribution, use [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md").
* To attach it to a new distribution, use [CreateDistribution](../../../cloudfront/latest/APIReference/API_CreateDistribution.md "../../../cloudfront/latest/APIReference/API_CreateDistribution.md").

For both of these API calls, provide the OAC ID in the
 `OriginAccessControlId` field, inside an origin. For more information
 about the other fields that you specify in these API calls, see [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md") and the API reference
 documentation for your AWS SDK or other API client.




## Advanced settings for origin access
 control


The CloudFront OAC feature includes advanced settings that are intended only for specific use
 cases. Use the recommended settings unless you have a specific need for the advanced
 settings.


OAC contains a setting named **Signing behavior** (in the console), or
 `SigningBehavior` (in the API, CLI, and AWS CloudFormation). This setting provides the
 following options:




**Always sign origin requests (recommended setting)**

We recommend using this setting, named **Sign requests
 (recommended)** in the console, or `always` in the API, CLI, and
 AWS CloudFormation. With this setting, CloudFront always signs all requests that it sends to the MediaPackage v2
 origin.



**Never sign origin requests**

This setting is named **Do not sign requests** in the console, or
 `never` in the API, CLI, and AWS CloudFormation. Use this setting to turn off OAC for
 all origins in all distributions that use this OAC. This can save time and effort
 compared to removing an OAC from all origins and distributions that use it, one by one.
 With this setting, CloudFront doesn't sign any requests that it sends to the MediaPackage v2
 origin.


###### Warning

To use this setting, the MediaPackage v2 origin must be publicly accessible. If you use
 this setting with a MediaPackage v2 origin that's not publicly accessible, CloudFront can't access
 the origin. The MediaPackage v2 origin returns errors to CloudFront and CloudFront passes those errors on
 to viewers. For more information, see the example MediaPackage v2 policy for [Policies and Permissions in MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/policies-permissions.html "https://docs.aws.amazon.com/mediapackage/latest/userguide/policies-permissions.html") in the *AWS Elemental MediaPackage User
 Guide*.



**Don't override the viewer (client) `Authorization` header**

This setting is named **Do not override authorization header** in
 the console, or `no-override` in the API, CLI, and AWS CloudFormation. Use this setting
 when you want CloudFront to sign origin requests only when the corresponding viewer request
 does not include an `Authorization` header. With this setting, CloudFront passes on
 the `Authorization` header from the viewer request when one is present, but
 signs the origin request (adding its own `Authorization` header) when the
 viewer request doesn't include an `Authorization` header.


###### Warning

To pass along the `Authorization` header from the viewer request, you
 *must* add the `Authorization` header to
 a [cache policy](controlling-the-cache-key.md "controlling-the-cache-key.md") for all cache
 behaviors that use MediaPackage v2 origins associated with this origin access control.

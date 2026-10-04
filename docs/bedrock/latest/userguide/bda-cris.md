

# Cross Region support required for Bedrock Data Automation
<a name="bda-cris"></a>

BDA requires users to use cross Region inference support when processing files. With cross-Region inference, Amazon Bedrock Data Automation will automatically select the optimal Region within your geography (as shown in the table below) to process your inference request, maximizing available compute resources and model availability, and providing the best customer experience. If you use the global inference profile, BDA can select any commercial AWS Region. There's no additional cost for using cross-Region inference. Unless you select the global inference profile, cross-Region inference requests are kept within the AWS Regions that are part of the geography where the data originally resides. For example, a request made within the US is kept within the AWS Regions in the US. Although the data remains stored only in the source Region, when using cross-Region inference, your requests and output results may move outside of your primary Region. All data will be encrypted while transmitted across Amazon's secure network. 

In addition to geographic inference profiles, BDA also offers a **global inference profile** (`global.data-automation-v1`). When you use the global profile, BDA might route your inference requests to **any commercial AWS Region globally** where the model is available. This profile is opt-in only. You must explicitly reference the global profile ARN in your IAM policy to use it. If you have data residency requirements, continue using the following geographic profiles, which restrict routing to Regions within your geography. The global inference profile is currently available only for requests made in Asia Pacific (Singapore), where it is the only supported inference profile.

The following table includes the ARNs for different inference profiles. Replace account id with the account id you're using.


| Source Region | Amazon Resource Name (ARN) | Supported Regions | 
| --- | --- | --- | 
| US East (N. Virginia) | arn:aws:bedrock:us-east-1:{{account id}}:data-automation-profile/us.data-automation-v1 | us-east-1<br />us-east-2<br />us-west-1<br />us-west-2 | 
| US West (Oregon) | arn:aws:bedrock:us-west-2:{{account id}}:data-automation-profile/us.data-automation-v1 | us-east-1<br />us-east-2<br />us-west-1<br />us-west-2 | 
| US East (Ohio) | arn:aws:bedrock:us-east-2:{{account id}}:data-automation-profile/us.data-automation-v1 | us-east-1<br />us-east-2<br />us-west-1<br />us-west-2 | 
| Canada (Central) | arn:aws:bedrock:ca-central-1:{{account id}}:data-automation-profile/na.data-automation-v1 | ca-central-1<br />ca-west-1<br />us-east-1<br />us-east-2<br />us-west-2 | 
| Europe (Frankfurt) | arn:aws:bedrock:eu-central-1:{{account id}}:data-automation-profile/eu.data-automation-v1 | eu-central-1<br />eu-north-1<br />eu-south-1<br />eu-south-2<br />eu-west-1<br />eu-west-3 | 
| Europe (Ireland) | arn:aws:bedrock:eu-west-1:{{account id}}:data-automation-profile/eu.data-automation-v1 | eu-central-1<br />eu-north-1<br />eu-south-1<br />eu-south-2<br />eu-west-1<br />eu-west-3 | 
| Europe (London) | arn:aws:bedrock:eu-west-2:{{account id}}:data-automation-profile/eu.data-automation-v1 | eu-west-2 | 
| Europe (Spain) | arn:aws:bedrock:eu-south-2:{{account id}}:data-automation-profile/eu.data-automation-v1 | eu-central-1<br />eu-north-1<br />eu-south-1<br />eu-south-2<br />eu-west-1<br />eu-west-3 | 
| Asia Pacific (Mumbai) | arn:aws:bedrock:ap-south-1:{{account id}}:data-automation-profile/apac.data-automation-v1 | ap-northeast-1<br />ap-northeast-2<br />ap-northeast-3<br />ap-south-1<br />ap-south-2<br />ap-southeast-1<br />ap-southeast-2<br />ap-southeast-4 | 
| Asia Pacific (Singapore) | arn:aws:bedrock:ap-southeast-1:{{account id}}:data-automation-profile/global.data-automation-v1 | All commercial AWS Regions where the model is available | 
| Asia Pacific (Sydney) | arn:aws:bedrock:ap-southeast-2:{{account id}}:data-automation-profile/apac.data-automation-v1 | ap-northeast-1<br />ap-northeast-2<br />ap-northeast-3<br />ap-south-1<br />ap-south-2<br />ap-southeast-1<br />ap-southeast-2<br />ap-southeast-4 | 
| Asia Pacific (Tokyo) | arn:aws:bedrock:ap-northeast-1:{{account id}}:data-automation-profile/apac.data-automation-v1 | ap-northeast-1<br />ap-northeast-2<br />ap-northeast-3<br />ap-south-1<br />ap-south-2<br />ap-southeast-1<br />ap-southeast-2<br />ap-southeast-3<br />ap-southeast-4<br />ap-southeast-5 | 
| AWS GovCloud (US-West) | arn:aws-us-gov:bedrock:us-gov-west-1:{{account id}}:data-automation-profile/us-gov.data-automation-v1 | us-gov-west-1 | 

Below is an example IAM policy for processing documents with CRIS enabled for `us-east-1` or `us-west-2`.

```
{"Effect": "Allow",
 "Action": ["bedrock:InvokeDataAutomationAsync"],
 "Resource": [
  "arn:aws:bedrock:us-east-1:{{account_id}}:data-automation-profile/us.data-automation-v1",
  "arn:aws:bedrock:us-east-2:{{account_id}}:data-automation-profile/us.data-automation-v1",
  "arn:aws:bedrock:us-west-1:{{account_id}}:data-automation-profile/us.data-automation-v1",
  "arn:aws:bedrock:us-west-2:{{account_id}}:data-automation-profile/us.data-automation-v1"]}
```

The following example shows an IAM policy for processing documents with the global inference profile in Asia Pacific (Singapore) (`ap-southeast-1`).

```
{
  ...
  "Effect": "Allow",
  "Action": ["bedrock:InvokeDataAutomationAsync"],
  "Resource": ["arn:aws:bedrock:ap-southeast-1:{{account_id}}:data-automation-profile/global.data-automation-v1"],
  ...
}
```

**Global cross-Region inference**  
By adding this policy, you explicitly enable global cross-Region inference. Your requests and results might be processed in any commercial AWS Region. To restrict inference to a specific geography, use the corresponding geographic profile ARN instead. Geographic inference profiles aren't available for requests made in Asia Pacific (Singapore).

## Troubleshooting
<a name="bda-cris-troubleshooting"></a>

**Error:**

```
ValidationException: The provided DataAutomationProfile ARN is invalid.
```

**Cause:**

This error occurs when the inference profile ARN in your IAM policy references `global.data-automation-v1` in a Region that does not support the global profile. Common scenarios:
+ **New users** — Configured the wrong profile ARN for their Region.
+ **If you're already using a geographic profile** — No action needed if you continue using your current geographic profile. However, if you attempt to switch to `global.data-automation-v1` in a Region where it is not yet supported, you will encounter this error. Continue using your geographic profile until global support is available in your Region.

**Resolution:**

Verify the profile ARN in your IAM policy matches a supported profile for your Region:
+ If your Region supports the global profile, check for typos in the ARN.
+ If your Region does not support the global profile, use the geographic profile for your Region instead (for example, `us.data-automation-v1` or `eu.data-automation-v1`). For supported Regions and profile ARNs, see the table in [Cross Region support required for Bedrock Data Automation](#bda-cris).

**Existing customers unaffected**  
Existing customers using geographic profiles are not affected by the introduction of the global profile. This error only applies when explicitly referencing `global.data-automation-v1`.
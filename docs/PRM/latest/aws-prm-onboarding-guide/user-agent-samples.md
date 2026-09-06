

# Implementation Samples
<a name="user-agent-samples"></a>

This section provides code samples for implementing User Agent strings across different programming languages and AWS SDKs. Each sample demonstrates how to configure the User Agent string format `APN_1.1/pc_<YOUR-PRODUCT-CODE>$` for AWS services.

**Note**  
Replace the example product code `5ugbbrmu7ud3u5hsipfzug61p` with your actual AWS Marketplace product code retrieved from the AWS Marketplace Management Portal.

## Python (boto3)
<a name="python-sample"></a>

```
import boto3
from botocore.config import Config

UA_STRING = "APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$"

# Create a config object with the custom user agent
session_config = Config(user_agent=UA_STRING)

# EC2 client
ec2 = boto3.client('ec2', config=session_config)

# S3 client
s3 = boto3.client('s3', config=session_config)
```

## Java (AWS SDK v2)
<a name="java-sample"></a>

```
import software.amazon.awssdk.core.client.config.ClientOverrideConfiguration;
import software.amazon.awssdk.core.client.config.SdkAdvancedClientOption;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.s3.S3Client;

public class AwsCustomUserAgentExample {
    private static final String UA_STRING = "APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$";
    private static final Region REGION = Region.US_WEST_2;

    public static void main(String[] args) {
        ClientOverrideConfiguration overrideConfig = ClientOverrideConfiguration.builder()
            .putAdvancedOption(SdkAdvancedClientOption.USER_AGENT_PREFIX, UA_STRING)
            .build();

        Ec2Client ec2 = Ec2Client.builder()
            .region(REGION)
            .overrideConfiguration(overrideConfig)
            .build();

        S3Client s3 = S3Client.builder()
            .region(REGION)
            .overrideConfiguration(overrideConfig)
            .build();
    }
}
```

## .NET (AWS SDK)
<a name="dotnet-sample"></a>

```
using Amazon;
using Amazon.S3;
using Amazon.Runtime;

class Program
{
    static void Main(string[] args)
    {
        AWSConfigs.UseAlternateUserAgentHeader = true;
        string UA_STRING = "APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$";

        var s3Config = new AmazonS3Config
        {
            RegionEndpoint = RegionEndpoint.USEast2,
        };
        var s3Client = new AmazonS3Client(s3Config);

        s3Client.BeforeRequestEvent += delegate (object sender, RequestEventArgs e)
        {
            if (e is WebServiceRequestEventArgs args)
            {
                args.Headers["User-Agent"] = UA_STRING;
            }
        };
    }
}
```

## Node.js (AWS SDK v3)
<a name="nodejs-sample"></a>

```
const { EC2Client } = require("@aws-sdk/client-ec2");
const { S3Client } = require("@aws-sdk/client-s3");

const PRODUCT_CODE = "5ugbbrmu7ud3u5hsipfzug61p";
const REGION = "us-west-2";

function addPRMUserAgent(client, productCode) {
    client.middlewareStack.add(
        (next) => async (args) => {
            if (!args.request.headers) args.request.headers = {};
            const existing = args.request.headers["User-Agent"] || "";
            const prmUAString = `APN_1.1/pc_${productCode}$`;
            args.request.headers["User-Agent"] = existing 
                ? `${existing} ${prmUAString}`
                : prmUAString;
            return next(args);
        },
        { step: "finalizeRequest", name: "prmUserAgent" }
    );
    return client;
}

const ec2Client = addPRMUserAgent(new EC2Client({ region: REGION }), PRODUCT_CODE);
const s3Client = addPRMUserAgent(new S3Client({ region: REGION }), PRODUCT_CODE);
```

## Go (AWS SDK v2)
<a name="go-sample"></a>

```
package main

import (
    "context"
    "net/http"

    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/s3"
)

const UA_STRING = "APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$"

type PRMUserAgentTransport struct {
    Transport http.RoundTripper
}

func (t *PRMUserAgentTransport) RoundTrip(req *http.Request) (*http.Response, error) {
    req.Header.Set("User-Agent", UA_STRING)
    return t.Transport.RoundTrip(req)
}

func main() {
    cfg, _ := config.LoadDefaultConfig(context.TODO(),
        config.WithRegion("us-east-2"),
        config.WithHTTPClient(&http.Client{
            Transport: &PRMUserAgentTransport{
                Transport: http.DefaultTransport,
            },
        }),
    )
    s3Client := s3.NewFromConfig(cfg)
    _ = s3Client
}
```

## Ruby (AWS SDK v3)
<a name="ruby-sample"></a>

```
require 'aws-sdk-ec2'
require 'aws-sdk-s3'

UA_STRING = 'APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$'
REGION = 'us-west-2'

Aws.config.update({
  region: REGION,
  user_agent_suffix: UA_STRING
})

ec2_client = Aws::EC2::Client.new
s3_client = Aws::S3::Client.new
```

## Terraform
<a name="terraform-user-agent-sample"></a>

The Terraform AWS provider supports three ways to inject custom User Agent information:


| Method | Scope | Recommended | 
| --- | --- | --- | 
| provider\_meta user\_agent argument | Declaring module only | Yes | 
| user\_agent provider argument | Provider block | No | 
| TF\_APPEND\_USER\_AGENT env var | Global (all API calls) | No | 

`provider_meta` is scoped to the declaring module only, ensuring correct attribution without collision when multiple partner modules are used in the same Terraform configuration.

**Prerequisites:** Terraform >= 1.0 and AWS provider **>= 6.27.0** (or AWSCC provider **>= 1.67.0**).

In your module's `terraform` block, add the `provider_meta "aws"` block with the PRM User Agent string:

```
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 6.27.0"
    }
  }

  provider_meta "aws" {
    user_agent = [
      "APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$",
    ]
  }
}
```

Replace `5ugbbrmu7ud3u5hsipfzug61p` with your actual product code. The `$` is a required end delimiter, do not omit it.

**Important**  
User Agent attribution requires ongoing API or CLI interaction with AWS resources. Terraform typically interacts with resources only during `plan`, `apply`, and `destroy` operations. If the partner solution provisions static, long-running resources with limited ongoing API activity, consider using [tag-based attribution with Terraform](automated-tagging.md#terraform-tagging) instead.

**Note**  
Do not declare a `provider "aws" {}` block in your module. The provider configuration should be controlled by the root module (the customer). Your module should only use `provider_meta`.  
`provider_meta` user-agent does **not** inherit to child modules. If your module calls other modules that also need attribution, each module must declare its own `provider_meta`.  
If both provider-level `user_agent` and `provider_meta` are present, the provider-level User Agent appears first in the header, followed by `provider_meta`.
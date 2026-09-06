

# Setting up a friendly URL for OpenSearch UI applications (self-service)
<a name="application-custom-domain"></a>

OpenSearch UI applications have auto-generated URLs like `https://application-{{name}}-{{id}}.{{Region}}.opensearch.amazonaws.com`. These URLs are long and difficult to remember. You can set up a friendly URL (such as `https://prod.example.com`). This URL redirects to your application, so you can access dashboards directly without navigating through the AWS Management Console.

## How it works
<a name="application-custom-domain-overview"></a>

This solution uses CloudFront to redirect requests from your friendly URL to your OpenSearch UI application endpoint. The architecture consists of the following components:
+ **ACM certificate** – Provides HTTPS encryption for your friendly URL.
+ **CloudFront KeyValueStore** – Stores the mapping between subdomain names and application URLs.
+ **CloudFront function** – Reads the KeyValueStore and returns a 302 redirect to the correct application URL.
+ **CloudFront distribution** – Serves your friendly URL with TLS and routes requests through the function.
+ **Route 53 DNS record** – Points your friendly URL to the CloudFront distribution.

When you visit your friendly URL (for example, `https://prod.example.com`), the CloudFront function looks up the corresponding application URL and redirects your browser to it. The application handles authentication directly.

## Prerequisites
<a name="application-custom-domain-prerequisites"></a>
+ One or more OpenSearch UI applications with their endpoint URLs.
+ A domain name that you own (for example, `example.com`).
+ A public hosted zone in Route 53 for your domain. If you don't have one, for more information, see [Setting up without Route 53 (manual configuration)](#application-custom-domain-without-route53).
+ An Amazon S3 bucket to store your application URL mappings file.

## Deploy using AWS CloudFormation
<a name="application-custom-domain-deploy-cfn"></a>

Use the following procedure to deploy the friendly URL redirect infrastructure with a CloudFormation template.

**To set up a friendly URL for your OpenSearch UI applications**

1. Create a JSON file that maps your friendly names to application URLs. Each key becomes a subdomain (for example, key `prod` becomes `https://prod.example.com`).

   ```
   {
     "data": [
       {"key": "prod", "value": "https://application-prod-abc123.us-west-2.opensearch.amazonaws.com"},
       {"key": "staging", "value": "https://application-staging-def456.us-east-1.opensearch.amazonaws.com"},
       {"key": "analytics", "value": "https://application-analytics-ghi789.eu-west-1.opensearch.amazonaws.com"}
     ]
   }
   ```

   Save this file as `opensearch-ui-friendly-url-app-mappings-v1.json`. The `v1` suffix identifies this as the first version of your mappings. You increment this version when you update your mappings.

1. Upload the mappings file to an Amazon S3 bucket in your account:

   ```
   aws s3 cp opensearch-ui-friendly-url-app-mappings-v1.json \
     s3://{{your-bucket-name}}/opensearch-ui-friendly-url-app-mappings-v1.json
   ```

1. Grant CloudFront permission to read the mappings file by adding a bucket policy. Replace {{your-bucket-name}} and {{your-account-id}} with your values:

   ```
   aws s3api put-bucket-policy \
     --bucket {{your-bucket-name}} \
     --policy '{
       "Version": "2012-10-17",
       "Statement": [{
         "Sid": "AllowCloudFrontKVSImport",
         "Effect": "Allow",
         "Principal": {"Service": "cloudfront.amazonaws.com"},
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::{{your-bucket-name}}/*",
         "Condition": {"StringEquals": {"aws:SourceAccount": "{{your-account-id}}"}}
       }]
     }'
   ```
**Note**  
This bucket policy allows CloudFront to read the mappings file during KeyValueStore creation. Without it, stack deployment fails with a "SourceARN is inaccessible" error.

1. Deploy the CloudFormation stack using one of the following options:

   **Option 1: Launch Stack (recommended)**

   Copy the following URL and paste it into your browser to open the AWS CloudFormation quick-create page with the template pre-loaded. Fill in the parameters and choose **Create stack**.

   ```
   https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://opensearch-ui-quickstart-sample-cfn-templates.s3.us-west-2.amazonaws.com/opensearch-ui-friendly-url/main.yaml&stackName=opensearch-ui-friendly-url&param_MappingsVersion=v1
   ```

   **Option 2: AWS CLI**

   Replace the placeholder values with your own:

   ```
   aws cloudformation create-stack \
     --stack-name opensearch-ui-friendly-url \
     --template-url https://opensearch-ui-quickstart-sample-cfn-templates.s3.us-west-2.amazonaws.com/opensearch-ui-friendly-url/main.yaml \
     --parameters \
       ParameterKey=DomainName,ParameterValue={{your-domain.com}} \
       ParameterKey=HostedZoneId,ParameterValue={{Z0123456789ABCDEFG}} \
       ParameterKey=MappingsBucket,ParameterValue={{your-bucket-name}} \
       ParameterKey=MappingsKey,ParameterValue=opensearch-ui-friendly-url-app-mappings-v1.json \
       ParameterKey=MappingsVersion,ParameterValue=v1 \
     --region us-east-1
   ```

1. If you used the AWS CLI (Option 2), deploy the stack in the `us-east-1` Region. CloudFront requires ACM certificates to be in `us-east-1`. Your OpenSearch UI applications can be in any [Supported Regions and quotas for OpenSearch UI](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/opensearch-ui-endpoints-quotas.html).

1. Wait for the stack to complete (approximately 15 minutes). You can monitor progress:

   ```
   aws cloudformation wait stack-create-complete \
     --stack-name opensearch-ui-friendly-url \
     --region us-east-1
   ```

1. Test the redirect. Open your browser and navigate to `https://{{prod}}.{{your-domain.com}}`. You should be redirected to your OpenSearch UI application.

   You can also verify with `curl`:

   ```
   curl -I https://{{prod}}.{{your-domain.com}}
   # Expected: HTTP/2 302
   # location: https://application-prod-abc123.us-west-2.opensearch.amazonaws.com
   ```

### CloudFormation template source
<a name="application-custom-domain-template-source"></a>

The following is the full CloudFormation template used by the Launch Stack link and CLI command above. You can also download it directly from `https://opensearch-ui-quickstart-sample-cfn-templates.s3.us-west-2.amazonaws.com/opensearch-ui-friendly-url/main.yaml`.

```
AWSTemplateFormatVersion: '2010-09-09'
Metadata:
  TemplateVersion: '1.0.0'
  LastUpdated: '2026-08-05'
  Author: 'OpenSearch UI Team'
Description: >
  OpenSearch UI Friendly URL - Creates a CloudFront distribution with a CloudFront Function
  that redirects friendly subdomain URLs to OpenSearch Application endpoints.
  Deploy this template in us-east-1 (required for ACM certificates used with CloudFront).

Parameters:
  DomainName:
    Type: String
    Description: "Your domain name (e.g., example.com or subdomain.example.com)"
    AllowedPattern: "^[a-zA-Z0-9][a-zA-Z0-9-]*(\\.[a-zA-Z0-9][a-zA-Z0-9-]*)+$"
  HostedZoneId:
    Type: AWS::Route53::HostedZone::Id
    Description: "Route 53 Hosted Zone ID for your domain"
  MappingsBucket:
    Type: String
    Description: "S3 bucket name containing your app mappings JSON file"
  MappingsKey:
    Type: String
    Description: "S3 key (path) to your app mappings JSON file"
    Default: "opensearch-ui-friendly-url-app-mappings.json"
  MappingsVersion:
    Type: String
    Description: "Version identifier for your mappings (change this when updating mappings, e.g., v1, v2, v3)"
    Default: "v1"
    AllowedPattern: "^[a-zA-Z0-9-]+$"

Resources:
  # 1. Wildcard TLS Certificate (DNS validated via Route 53)
  Certificate:
    Type: AWS::CertificateManager::Certificate
    Properties:
      DomainName: !Sub "*.${DomainName}"
      ValidationMethod: DNS
      DomainValidationOptions:
        - DomainName: !Sub "*.${DomainName}"
          HostedZoneId: !Ref HostedZoneId

  # 2. CloudFront KeyValueStore with S3 import for app mappings
  AppMappingStore:
    Type: AWS::CloudFront::KeyValueStore
    Properties:
      Name: !Sub "${AWS::StackName}-kvs-${MappingsVersion}"
      Comment: !Sub "OpenSearch UI app mappings ${MappingsVersion} for ${DomainName}"
      ImportSource:
        SourceType: S3
        SourceArn: !Sub "arn:aws:s3:::${MappingsBucket}/${MappingsKey}"

  # 3. CloudFront Function (reads KVS, returns 302 redirect)
  RedirectFunction:
    Type: AWS::CloudFront::Function
    Properties:
      Name: !Sub "${AWS::StackName}-fn"
      AutoPublish: true
      FunctionConfig:
        Comment: !Sub "Redirects friendly URLs to OpenSearch Application endpoints (${MappingsVersion})"
        Runtime: cloudfront-js-2.0
        KeyValueStoreAssociations:
          - KeyValueStoreARN: !GetAtt AppMappingStore.Arn
      FunctionCode: !Sub |
        import cf from 'cloudfront';

        const kvsHandle = cf.kvs("${AppMappingStore.Id}");

        async function handler(event) {
          var request = event.request;
          var host = request.headers.host.value;
          
          // Extract subdomain prefix (e.g., "app1" from "app1.example.com")
          var subdomain = host.split('.')[0];
          
          try {
            var targetUrl = await kvsHandle.get(subdomain);
            return {
              statusCode: 302,
              statusDescription: 'Found',
              headers: {
                'location': { value: targetUrl },
                'cache-control': { value: 'no-cache, no-store, must-revalidate' }
              }
            };
          } catch (e) {
            // Key not found - return 404
            return {
              statusCode: 404,
              statusDescription: 'Not Found',
              headers: {
                'content-type': { value: 'text/html' }
              },
              body: {
                encoding: 'text',
                data: '<html><body><h1>Application Not Found</h1><p>No OpenSearch application is mapped to the requested subdomain.</p></body></html>'
              }
            };
          }
        }

  # 4. CloudFront Distribution
  Distribution:
    Type: AWS::CloudFront::Distribution
    DependsOn: Certificate
    Properties:
      DistributionConfig:
        Enabled: true
        Comment: !Sub "OpenSearch UI Friendly URL for ${DomainName}"
        Aliases:
          - !Sub "*.${DomainName}"
        ViewerCertificate:
          AcmCertificateArn: !Ref Certificate
          SslSupportMethod: sni-only
          MinimumProtocolVersion: TLSv1.2_2021
        DefaultCacheBehavior:
          ViewerProtocolPolicy: redirect-to-https
          AllowedMethods:
            - GET
            - HEAD
          CachedMethods:
            - GET
            - HEAD
          CachePolicyId: "4135ea2d-6df8-44a3-9df3-4b5a84be39ad"  # AWS managed CachingDisabled policy
          TargetOriginId: dummy-origin
          FunctionAssociations:
            - EventType: viewer-request
              FunctionARN: !GetAtt RedirectFunction.FunctionMetadata.FunctionARN
        Origins:
          - Id: dummy-origin
            DomainName: "example.com"
            CustomOriginConfig:
              OriginProtocolPolicy: https-only
        HttpVersion: http2and3
        IPV6Enabled: true
        PriceClass: PriceClass_All

  # 5. Wildcard DNS record pointing to CloudFront
  WildcardDnsRecord:
    Type: AWS::Route53::RecordSet
    Properties:
      HostedZoneId: !Ref HostedZoneId
      Name: !Sub "*.${DomainName}"
      Type: A
      AliasTarget:
        HostedZoneId: Z2FDTNDATAQYW2  # CloudFront's fixed hosted zone ID (constant for all distributions)
        DNSName: !GetAtt Distribution.DomainName
        EvaluateTargetHealth: false

Outputs:
  CloudFrontDomain:
    Description: "CloudFront distribution domain name"
    Value: !GetAtt Distribution.DomainName
  CertificateArn:
    Description: "ACM Certificate ARN"
    Value: !Ref Certificate
  KeyValueStoreArn:
    Description: "CloudFront KeyValueStore ARN"
    Value: !GetAtt AppMappingStore.Arn
  ExampleUrl:
    Description: "Example friendly URL"
    Value: !Sub "https://prod.${DomainName}"
  MappingsFileLocation:
    Description: "S3 location of your app mappings file"
    Value: !Sub "s3://${MappingsBucket}/${MappingsKey}"
  CurrentMappingsVersion:
    Description: "Current mappings version deployed"
    Value: !Ref MappingsVersion
  TemplateVersion:
    Description: "Template version and last updated date"
    Value: "1.0.0 (2026-08-05)"
```

### Adding or removing applications
<a name="application-custom-domain-add-apps"></a>

To add, update, or remove application mappings, create a new version of your S3 mappings file and update the stack with the new version. The versioned approach keeps your S3 file as the source of truth and allows you to roll forward to new configurations or roll back to previous versions at any time.

1. Edit your mappings file to add or remove entries. Save it with an incremented version suffix (for example, `opensearch-ui-friendly-url-app-mappings-v2.json`).

1. Upload the new version to S3:

   ```
   aws s3 cp opensearch-ui-friendly-url-app-mappings-v2.json \
     s3://{{your-bucket-name}}/opensearch-ui-friendly-url-app-mappings-v2.json
   ```

1. Update the stack with the new `MappingsKey` and `MappingsVersion`:

   **Using the console:** Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your stack, choose **Update**, select **Use current template**, then update the `MappingsKey` and `MappingsVersion` parameters with the new values.

   **Using the AWS CLI:**

   ```
   aws cloudformation update-stack \
     --stack-name opensearch-ui-friendly-url \
     --use-previous-template \
     --parameters \
       ParameterKey=DomainName,UsePreviousValue=true \
       ParameterKey=HostedZoneId,UsePreviousValue=true \
       ParameterKey=MappingsBucket,UsePreviousValue=true \
       ParameterKey=MappingsKey,ParameterValue=opensearch-ui-friendly-url-app-mappings-v2.json \
       ParameterKey=MappingsVersion,ParameterValue=v2 \
     --region us-east-1
   ```

**Important**  
You must change the `MappingsVersion` parameter each time you update mappings. The version drives the KeyValueStore name, which triggers CloudFormation to replace the KeyValueStore with the updated data. Keep the `MappingsKey` file name and `MappingsVersion` in sync (for example, `...-v2.json` with `MappingsVersion=v2`) for clarity.

To roll back to a previous version, update the stack pointing to the earlier file and version.

**Using the console:** Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), select your stack, choose **Update**, select **Use current template**, then set `MappingsKey` and `MappingsVersion` back to the previous values (for example, `v1`).

**Using the AWS CLI:**

```
aws cloudformation update-stack \
  --stack-name opensearch-ui-friendly-url \
  --use-previous-template \
  --parameters \
    ParameterKey=DomainName,UsePreviousValue=true \
    ParameterKey=HostedZoneId,UsePreviousValue=true \
    ParameterKey=MappingsBucket,UsePreviousValue=true \
    ParameterKey=MappingsKey,ParameterValue=opensearch-ui-friendly-url-app-mappings-v1.json \
    ParameterKey=MappingsVersion,ParameterValue=v1 \
  --region us-east-1
```

This versioned approach gives you full control to roll forward or roll back your application mappings as needed, while keeping your S3 files as the definitive record of each configuration version.

## Setting up without Route 53 (manual configuration)
<a name="application-custom-domain-without-route53"></a>

If your domain is managed by a DNS provider other than Route 53, you can set up friendly URL redirects manually in the AWS Management Console. This approach does not use Amazon S3 for mappings — you manage key-value pairs directly in the CloudFront console.

**To set up a friendly URL redirect without Route 53**

1. 

**Request a certificate in ACM**

   1. Open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/) in the `us-east-1` Region.

   1. Choose **Request certificate**.

   1. For **Domain name**, enter `*.{{your-domain.com}}` (wildcard certificate).

   1. For **Validation method**, choose **DNS validation**.

   1. Choose **Request**.

   1. On the certificate details page, note the CNAME record name and value under **Domain validation**. Create this CNAME record at your DNS provider to validate domain ownership.

   1. Wait for the certificate status to change to **Issued** (typically 5 to 30 minutes after DNS record creation).

1. 

**Create a CloudFront KeyValueStore**

   1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/](https://console.aws.amazon.com/cloudfront/).

   1. In the navigation pane, choose **Functions**. Then choose the **KeyValueStores** tab.

   1. Choose **Create KeyValueStore**.

   1. Enter a name (for example, `opensearch-ui-friendly-url-app-mappings-store`).

   1. Choose **Create**.

   1. After creation, choose **Edit** to add key-value pairs. For each application, add a key (the subdomain name, such as `prod`) and a value (the full OpenSearch UI application URL).

1. 

**Create a CloudFront function**

   1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/](https://console.aws.amazon.com/cloudfront/).

   1. In the navigation pane, choose **Functions**.

   1. On the **Functions** tab, choose **Create function**.

   1. Enter a name for the function (for example, `opensearch-ui-friendly-url-redirect-function`).

   1. For **Runtime**, choose **cloudfront-js-2.0**.

   1. Replace the function code with the following:

      ```
      import cf from 'cloudfront';
      
      const kvsHandle = cf.kvs("{{YOUR_KVS_ID}}");
      
      async function handler(event) {
        var request = event.request;
        var host = request.headers.host.value;
        var subdomain = host.split('.')[0];
      
        try {
          var targetUrl = await kvsHandle.get(subdomain);
          return {
            statusCode: 302,
            statusDescription: 'Found',
            headers: {
              'location': { value: targetUrl },
              'cache-control': { value: 'no-cache, no-store, must-revalidate' }
            }
          };
        } catch (e) {
          return {
            statusCode: 404,
            statusDescription: 'Not Found',
            headers: { 'content-type': { value: 'text/html' } },
            body: {
              encoding: 'text',
              data: '<html><body><h1>Application Not Found</h1><p>No OpenSearch application is mapped to the requested subdomain.</p></body></html>'
            }
          };
        }
      }
      ```

      Replace {{YOUR\_KVS\_ID}} with the ID of the KeyValueStore you created (visible on the KeyValueStore details page).

   1. In **KeyValueStore associations**, associate the KeyValueStore you created.

   1. Choose **Save changes** and then **Publish function**.

1. 

**Create a CloudFront distribution**

   1. In the CloudFront console, choose **Create distribution**.

   1. For **Origin domain**, enter any valid domain (for example, `example.com`). The origin is never contacted because the function returns a response before reaching it.

   1. Under **Default cache behavior**, for **Viewer protocol policy**, choose **Redirect HTTP to HTTPS**.

   1. For **Cache policy**, choose **CachingDisabled**.

   1. Under **Function associations**, for **Viewer request**, select your CloudFront function.

   1. Under **Settings**, for **Alternate domain names (CNAMEs)**, enter `*.{{your-domain.com}}`.

   1. For **Custom SSL certificate**, select the certificate you created in ACM.

   1. Choose **Create distribution**.

   1. Note the distribution domain name (for example, `d1234abcdef8.cloudfront.net`).

1. 

**Configure DNS at your provider**

   At your DNS provider, create a CNAME record that points `*.{{your-domain.com}}` to your CloudFront distribution domain name (for example, `d1234abcdef8.cloudfront.net`).
**Note**  
Some DNS providers don't support wildcard CNAME records. In that case, create individual CNAME records for each subdomain you want to use (for example, `prod.your-domain.com`, `staging.your-domain.com`).

### Adding application mappings manually
<a name="application-custom-domain-manual-add-apps"></a>

To add new application mappings after the initial manual setup:

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/](https://console.aws.amazon.com/cloudfront/).

1. In the navigation pane, choose **Functions**. Then choose the **KeyValueStores** tab.

1. Choose your KeyValueStore name (for example, `opensearch-ui-friendly-url-app-mappings-store`).

1. Choose **Edit**.

1. Choose **Add pair**. Enter the subdomain name as the key and the full OpenSearch UI application URL as the value.

1. Choose **Save changes**.

The new friendly URL is available immediately after saving.

## Cleaning up
<a name="application-custom-domain-cleanup"></a>

To remove the friendly URL redirect infrastructure, run the following command:

```
aws cloudformation delete-stack \
  --stack-name opensearch-ui-friendly-url \
  --region us-east-1
```

This command removes the CloudFront distribution, function, KeyValueStore, ACM certificate, and DNS record. It does not affect your OpenSearch UI applications.

## Troubleshooting
<a name="application-custom-domain-troubleshooting"></a>

ACM certificate stays in `Pending validation`  
Ensure your domain's DNS is properly delegated to Route 53 (or that you created the validation CNAME at your DNS provider). Use `dig {{your-domain}} NS` to verify the nameservers.

Browser shows certificate error  
Verify the ACM certificate covers your domain as a wildcard (`*.your-domain.com`). The certificate must be in the `us-east-1` Region.

404 Application Not Found  
The subdomain you're trying to access doesn't have a mapping in the KeyValueStore. Verify the key exists in your mappings file and confirm that you updated the stack (or added the pair manually) after your last change.

CloudFront distribution shows `Deploying` status for more than 15 minutes  
CloudFront distributions can take up to 15 minutes to deploy globally. If the deployment takes longer, check the CloudFront console for error details.

SourceARN is inaccessible error during stack creation  
Ensure the S3 bucket policy grants `cloudfront.amazonaws.com` permission to read the mappings file. Also verify the IAM role deploying the stack has `s3:GetObject`, `s3:HeadObject`, and `s3:GetBucketLocation` permissions on the bucket.
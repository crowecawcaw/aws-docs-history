

# Manual Implementation
<a name="user-agent-implementation"></a>

Follow these steps to implement User Agent strings in your regular AWS API/CLI calls for Partner Revenue Measurement:

1. [Retrieve your product code from AWS Marketplace Management Portal](product-code-retrieval.md).

1. Create the User Agent string using the format `APN_1.1/pc_<YOUR-PRODUCT-CODE>$`. Replace `<YOUR-PRODUCT-CODE>` with your actual alphanumeric product code. The `$` symbol marks the end delimiter.

1. Update your AWS SDK configuration to include the User Agent string. For complete implementation examples across different programming languages, see [User Agent Implementation Samples](user-agent-samples.md). For automated methods, see [Automated User Agent](automated-user-agent.md).

   Basic example for AWS CLI:

   ```
   # Set user-agent string for AWS CLI
   export AWS_SDK_UA_APP_ID="APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$"
   
   # Example EC2 API call with user-agent
   aws ec2 run-instances --image-id ami-0abcdef1234567890 --instance-type t2.micro --region us-east-1
   ```
**Note**  
Replace `5ugbbrmu7ud3u5hsipfzug61p` with your actual AWS Marketplace product code.

1. Test your implementation using AWS CloudTrail to verify the User Agent string is included:

   ```
   # Check CloudTrail logs for user-agent string
   aws logs filter-log-events \
     --log-group-name CloudTrail/YourLogGroup \
     --filter-pattern "APN_1.1" \
     --start-time 1640995200000
   ```

   Look for the `userAgent` field in CloudTrail events to confirm your User Agent string is being sent with API calls.

1. Deploy to production and contact your AWS partner management team or [APN Support](https://partnercentral.awspartner.com/partnercentral2/s/support) (Partner Central login required) with your deployment details for validation.

   Example CloudTrail event showing User Agent string:

   ```
   {
     "eventTime": "2025-01-14T21:21:54Z",
     "eventName": "RunInstances",
     "eventSource": "ec2.amazonaws.com",
     "userAgent": "APN_1.1/pc_5ugbbrmu7ud3u5hsipfzug61p$ aws-cli/2.0.0",
     "sourceIPAddress": "203.0.113.12",
     "resources": [
       {
         "accountId": "123456789123",
         "type": "AWS::EC2::Instance"
       }
     ]
   }
   ```

**Note**  
User Agent strings must be implemented consistently across all regular AWS API/CLI calls to ensure accurate revenue attribution. For multi-region deployments, ensure the User Agent string is included in regular AWS API/CLI calls across all regions where your solution operates.

**Note**  
Partner Revenue Measurement is intended to measure production workloads. Dev/test/staging environments can be used for validating your implementation before rolling out to production.

**Important**  
User Agent based attribution is evaluated monthly. Your partner solution must make at least one regular AWS API/CLI call per resource per month for continued attribution. If no calls are made on a resource in a given month, that resource does not contribute to revenue attribution for that month.  
In scenarios where your partner solution does not make frequent regular AWS API/CLI calls, you can make non-mutating, read-only calls (such as `Describe*` operations) to demonstrate continued interaction between your partner solution and the AWS resource. Refer to the [included services](user-agent-included-services.md) for supported API actions.

## Infrastructure as Code Limitations
<a name="ua-iac-limitations"></a>

**AWS CloudFormation / AWS CDK:** CloudFormation does not support custom User Agent strings natively. When CloudFormation creates resources, it makes regular AWS API/CLI calls using its own service principal, and you cannot control the User Agent string in those calls. Use [Resource Tagging](resource-tagging.md) for CloudFormation-deployed resources instead. If your CloudFormation template includes Custom Resources (Lambda-backed), the Lambda function code can include a User Agent string via the SDK approach.

**Terraform:** Terraform supports User Agent attribution via `provider_meta` with the `user_agent` argument (AWS provider **>= 6.27.0** or AWSCC provider **>= 1.67.0**). This is scoped to the declaring module only, ensuring correct attribution without collision across multiple partner modules. See [Terraform Implementation Sample](user-agent-samples.md#terraform-user-agent-sample) for full details.


# User Agent String
<a name="user-agent-string"></a>

This guide provides step-by-step instructions for AWS Partners to implement User Agent strings for Partner Revenue Measurement revenue attribution using AWS APIs and SDKs.

**Note**  
If you have an AMI product listed on AWS Marketplace that uses services beyond Amazon EC2, or an ML product that uses services beyond Amazon SageMaker AI, AWS recommends integrating a User Agent string to receive additional revenue attribution for your product.

**Note**  
**Required Format:** `APN_1.1/pc_<YOUR-PRODUCT-CODE>$`  
The User Agent string format must be included in all regular AWS API/CLI calls made by your solution. Where `<YOUR-PRODUCT-CODE>` is your alphanumeric product code from AWS Marketplace and `$` is the required end delimiter.

**Note**  
For revenue attribution, your product must conduct at least one API operation on an AWS Resource Name (ARN) per month. If no API operations are performed on a resource in a given month, that resource does not contribute to revenue attribution for that month.
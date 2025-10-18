# Get started with a standard distribution (AWS CLI)

The procedures in this section show you how to use the AWS CLI with CloudFront to set up a basic configuration that involves the following:


* Creating an Amazon S3 bucket to use as your distribution origin.
* Storing the original versions of your objects in the S3
 bucket.
* Using origin access control (OAC) to send authenticated requests to your Amazon S3 origin. OAC sends requests through CloudFront to prevent viewers from accessing your S3 bucket directly. For more information about OAC, see [Restrict access to an Amazon S3
 origin](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md").
* Using the CloudFront domain name in URLs for your objects (for example,
 `https://d111111abcdef8.cloudfront.net/index.html`).
* Keeping your objects in CloudFront edge locations for the default duration of 24 hours
 (the minimum duration is 0 seconds).
Most of these options are customizable. For information about how to customize your
 CloudFront distribution options, see [Create a distribution](distribution-web-creating-console.md "distribution-web-creating-console.md").

## Prerequisites


Before you begin, make sure that you’ve completed the steps in [Set up your AWS account](setting-up-cloudfront.md "setting-up-cloudfront.md").


Install the AWS CLI and configure it with your credentials. For more information, see [Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html") in the *AWS CLI User Guide*.



## Create an Amazon S3 bucket


An Amazon S3 bucket is a container for files (objects) or folders. CloudFront can distribute
 almost any type of file for you when an S3 bucket is the source. For example, CloudFront
 can distribute text, images, and videos. There is no maximum for the amount of data
 that you can store on Amazon S3.


For this tutorial, you create an S3 bucket and upload an
 HTML file that you will use to create a basic
 webpage.



```
aws s3 mb s3://`amzn-s3-demo-bucket`/ --region `us-east-1`

```

Replace `amzn-s3-demo-bucket` with a globally unique bucket name. For the AWS Region, we recommend choosing a Region
 that is geographically close to you. This reduces latency and
 costs, but choosing a different Region works, too. For example, you might do this to
 address regulatory requirements.


## Upload the content to the bucket


For this tutorial, download and extract the sample content files for a basic "Hello World" webpage.



```
# Create a temporary directory
mkdir -p ~/cloudfront-demo

# Download the sample Hello World files
curl -o ~/cloudfront-demo/hello-world-html.zip https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/samples/hello-world-html.zip

# Extract the zip file
unzip ~/cloudfront-demo/hello-world-html.zip -d ~/cloudfront-demo/hello-world
```

This creates a directory with an `index.html` file and a `css` folder. Upload these files to your S3 bucket.



```
aws s3 cp ~/cloudfront-demo/hello-world/ s3://`amzn-s3-demo-bucket`/ --recursive
```

## Create an Origin Access Control (OAC)


For this tutorial, you will create an origin access control (OAC). OAC helps you securely send authenticated requests to your Amazon S3 origin. For more information about OAC, see [Restrict access to an Amazon S3
 origin](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md").



```
aws cloudfront create-origin-access-control \
    --origin-access-control-config Name="`oac-for-s3`",SigningProtocol=sigv4,SigningBehavior=always,OriginAccessControlOriginType=s3
```

Save the OAC ID from the output as an environment variable. Replace the example value with your own OAC ID. You will use this in the next step.



```
OAC_ID="`E1ABCD2EFGHIJ`"
```

## Create a standard distribution


Create a distribution configuration file named `distribution-config.json`. Replace the example bucket name with your bucket name for the `Id`, `DomainName`, and `TargetOriginId` values.



```
cat > distribution-config.json << EOF
{
    "CallerReference": "cli-example-$(date +%s)",
    "Origins": {
        "Quantity": 1,
        "Items": [
            {
                "Id": "S3-`amzn-s3-demo-bucket`",
                "DomainName": "`amzn-s3-demo-bucket`.s3.amazonaws.com",
                "S3OriginConfig": {
                    "OriginAccessIdentity": ""
                },
                "OriginAccessControlId": "$OAC_ID"
            }
        ]
    },
    "DefaultCacheBehavior": {
        "TargetOriginId": "S3-`amzn-s3-demo-bucket`",
        "ViewerProtocolPolicy": "redirect-to-https",
        "AllowedMethods": {
            "Quantity": 2,
            "Items": ["GET", "HEAD"],
            "CachedMethods": {
                "Quantity": 2,
                "Items": ["GET", "HEAD"]
            }
        },
        "DefaultTTL": 86400,
        "MinTTL": 0,
        "MaxTTL": 31536000,
        "Compress": true,
        "ForwardedValues": {
            "QueryString": false,
            "Cookies": {
                "Forward": "none"
            }
        }
    },
    "Comment": "CloudFront distribution for S3 bucket",
    "Enabled": true
}
EOF

```

Create the standard distribution.



```
aws cloudfront create-distribution --distribution-config file://distribution-config.json

```

Save the distribution ID and domain name from the output as environment variables. Replace the example values with your own. You'll use these later in this tutorial.



```
DISTRIBUTION_ID="`EABCD1234XMPL`"
DOMAIN_NAME="`d111111abcdef8.cloudfront.net`"
```

Before using the distribution and S3 bucket from this tutorial in a production
 environment, make sure to configure it to meet your specific needs. For information
 about configuring access in a production environment, see [Configure secure access and restrict access to
 content](SecurityAndPrivateContent.md "SecurityAndPrivateContent.md").


## Update your S3 bucket policy


Update your S3 bucket policy to allow CloudFront to access the objects. Replace the example bucket name with your bucket name.



```
# Get your AWS account ID
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

# Create the bucket policy
cat > bucket-policy.json << EOF
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCloudFrontServicePrincipal",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceArn": "arn:aws:cloudfront::$ACCOUNT_ID:distribution/$DISTRIBUTION_ID"
                }
            }
        }
    ]
}
EOF

# Apply the bucket policy
aws s3api put-bucket-policy \
    --bucket `amzn-s3-demo-bucket` \
    --policy file://bucket-policy.json

```

## Confirm distribution deployment


After you create your distribution, it will take some time to finish deploying. When the distribution status changes from `InProgress` to `Deployed`, proceed to the next step.



```
aws cloudfront get-distribution --id $DISTRIBUTION_ID --query 'Distribution.Status'

```

Alternatively, you can use the `wait` command to wait for distribution deployment.



```
aws cloudfront wait distribution-deployed --id $DISTRIBUTION_ID
```

## Access your content through CloudFront


To access your content through CloudFront, combine the domain name for your CloudFront
 distribution with the main page for your content. Replace the example CloudFront domain name with your own.



```
https://`d111111abcdef8.cloudfront.net`/index.html
```

If you followed the previous steps and created the HTML file, you should see a webpage that says **Hello world!**.


When you upload more content to this S3 bucket, you can access the content through
 CloudFront by combining the CloudFront distribution domain name with the path to the object in
 the S3 bucket. For example, if you upload a new file named
 `new-page.html` to the root of your S3 bucket, the URL looks
 like this:


`https://d111111abcdef8.cloudfront.net/new-page.html`.


## Clean up


If you created your distribution and S3 bucket only as a learning exercise, delete
 them so that you no longer accrue charges. Disable and delete the distribution first.


###### To disable and delete a standard distribution (AWS CLI)

1. First, disable the distribution.



```
# Get the current configuration and ETag
ETAG=$(aws cloudfront get-distribution-config --id $DISTRIBUTION_ID --query 'ETag' --output text)

# Create a modified configuration with Enabled=false
aws cloudfront get-distribution-config --id $DISTRIBUTION_ID | \
jq '.DistributionConfig.Enabled = false' > temp_disabled_config.json

# Update the distribution to disable it
aws cloudfront update-distribution \
    --id $DISTRIBUTION_ID \
    --distribution-config file://<(jq '.DistributionConfig' temp_disabled_config.json) \
    --if-match $ETAG

```
2. Wait for the distribution to be disabled.



```
aws cloudfront wait distribution-deployed --id $DISTRIBUTION_ID

```
3. Delete the distribution.



```
# Get the current ETag
ETAG=$(aws cloudfront get-distribution-config --id $DISTRIBUTION_ID --query 'ETag' --output text)

# Delete the distribution
aws cloudfront delete-distribution --id $DISTRIBUTION_ID --if-match $ETAG
```

###### To delete an S3 bucket (AWS CLI)

* Delete the S3 bucket and its contents. Replace the example bucket name with your own.



```
# Delete the bucket contents
aws s3 rm s3://`amzn-s3-demo-bucket` --recursive

# Delete the bucket
aws s3 rb s3://`amzn-s3-demo-bucket`

```

To clean up the local files created for this tutorial, run the following commands:



```
# Clean up local files
rm -f distribution-config.json bucket-policy.json temp_disabled_config.json
rm -rf ~/cloudfront-demo
```

Optionally, you can delete the OAC that you created for this tutorial.



```
# Get the OAC ETag
OAC_ETAG=$(aws cloudfront get-origin-access-control --id $OAC_ID --query 'ETag' --output text)

# Delete the OAC
aws cloudfront delete-origin-access-control --id $OAC_ID --if-match $OAC_ETAG
```

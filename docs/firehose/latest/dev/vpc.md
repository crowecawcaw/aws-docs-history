# Using Amazon Data Firehose with AWS PrivateLink

You can use an interface VPC endpoint (AWS PrivateLink) to access Amazon Data Firehose from
your VPC without requiring an Internet Gateway or NAT Gateway. Interface VPC endpoints don't
require an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Interface
VPC endpoints are powered by AWS PrivateLink, an AWS technology that enables private
communication between AWS services using an elastic network interface with private IPs in
your Amazon VPC. For more information, see [Amazon Virtual Private Cloud](../../../AmazonVPC/latest/UserGuide/VPC_Introduction.md "../../../AmazonVPC/latest/UserGuide/VPC_Introduction.md").

## Using interface VPC endpoints (AWS

PrivateLink) for Firehose

To get started, create an interface VPC endpoint in order for your Amazon Data Firehose traffic from
your Amazon VPC resources to start flowing through the interface VPC endpoint. When you
create an endpoint, you can attach an endpoint policy to it that controls access to
Amazon Data Firehose. For more about using policies to control access from a VPC endpoint to Amazon Data Firehose, see
[Controlling Access to Services with VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md").

The following example shows how you can set up an AWS Lambda function in a VPC and
create a VPC endpoint to allow the function to communicate securely with the Amazon Data Firehose
service. In this example, you use a policy that allows the Lambda function to list the
Firehose streams in the current Region but not to describe any Firehose stream.

###### Create a VPC endpoint

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the VPC Dashboard choose **Endpoints**.
3. Choose **Create Endpoint**.
4. In the list of service names, choose
   `com.amazonaws.`your_region`.kinesis-firehose`.
5. Choose the VPC and one or more subnets in which to create the endpoint.
6. Choose one or more security groups to associate with the endpoint.
7. For **Policy**, choose **Custom** and paste
   the following policy:

```
{
    "Statement": [
        {
            "Sid": "Allow-only-specific-PrivateAPIs",
            "Principal": "*",
            "Action": [
                "firehose:ListDeliveryStreams"
            ],
            "Effect": "Allow",
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "Allow-only-specific-PrivateAPIs",
            "Principal": "*",
            "Action": [
                "firehose:DescribeDeliveryStream"
            ],
            "Effect": "Deny",
            "Resource": [
                "*"
            ]
        }
    ]
}
```

8. Choose **Create endpoint**.

###### Create an IAM role to use with the Lambda function

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left pane, chose **Roles** and then choose
   **Create role**.
3. Under **Select type of trusted entity**, leave the default
   selection **AWS service**.
4. Under **Choose the service that will use this role**, choose
   **Lambda**.
5. Choose **Next: Permissions**.
6. In the list of policies, search for and add the two policies named
   `AWSLambdaVPCAccessExecutionRole` and
   `AmazonDataFirehoseReadOnlyAccess`.

###### Important

This is an example. You might need stricter policies for your production
environment. 7. Choose **Next: Tags**. You don't need to add tags for the
purpose of this exercise. Choose **Next: Review**. 8. Enter a name for the role, then choose **Create
role**.

###### Create a Lambda function inside the VPC

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**.
3. Choose **Author from scratch**.
4. Enter a name for the function, then set **Runtime** to
   `Python 3.9` or higher.
5. Under **Permissions**, expand **Choose or create an
   execution role**.
6. In the **Execution role** list, choose **Use an
   existing role**.
7. In the **Existing role** list, choose the role you created
   above.
8. Choose **Create function**.
9. Under **Function code**, paste the following code.

```
    import json
    import boto3
    import os
    from botocore.exceptions import ClientError

    def lambda_handler(event, context):
        REGION = os.environ['AWS_REGION']
        client = boto3.client(
            'firehose',
            REGION

        )
        print("Calling list_delivery_streams with ListDeliveryStreams allowed policy.")
        delivery_stream_request = client.list_delivery_streams()
        print("Successfully returned list_delivery_streams request %s." % (
            delivery_stream_request
        ))
        describe_access_denied = False
        try:
            print("Calling describe_delivery_stream with DescribeDeliveryStream denied policy.")
            delivery_stream_info = client.describe_delivery_stream(DeliveryStreamName='test-describe-denied')
        except ClientError as e:
            error_code = e.response['Error']['Code']
            print ("Caught %s." % (error_code))
            if error_code == 'AccessDeniedException':
                describe_access_denied = True

        if not describe_access_denied:
            raise
        else:
            print("Access denied test succeeded.")
```

10. Under **Basic settings**, set the timeout to 1 minute.
11. Under **Network**, choose the VPC where you created the
    endpoint above, then choose the subnets and security group that you associated
    with the endpoint when you created it.
12. Near the top of the page, choose **Save**.
13. Choose **Test**.
14. Enter an event name, then choose **Create**.
15. Choose **Test** again. This causes the function to run.
    After the execution result appears, expand **Details** and
    compare the log output to the function code. Successful results show a list of
    the Firehose streams in the Region, as well as the following output:

`Calling describe_delivery_stream.`

`AccessDeniedException`

`Access denied test succeeded.`

## Supported AWS Regions

Interface VPC endpoints are currently supported within the following regions.

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Thailand)
- Asia Pacific (Tokyo)
- Asia Pacific (Hong Kong)
- Canada (Central)
- Canada West (Calgary)
- China (Beijing)
- China (Ningxia)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Mexico (Central)
- South America (São Paulo)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)
- Europe (Spain)
- Middle East (UAE)
- Asia Pacific (Jakarta)
- Asia Pacific (Osaka)
- Israel (Tel Aviv)
- Asia Pacific (Malaysia)

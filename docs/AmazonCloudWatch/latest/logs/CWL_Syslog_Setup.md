

# Setting up syslog ingestion
<a name="CWL_Syslog_Setup"></a>

This section walks you through the steps to set up syslog ingestion into CloudWatch Logs. You will create a VPC endpoint for the syslog service, a log group to receive the messages, a resource policy to authorize the syslog service, and a syslog configuration that routes traffic from your VPC endpoint to your log group.

You can perform all of these steps using the AWS Management Console, the AWS CLI, or the AWS SDKs. The following instructions provide both console and AWS CLI examples.

## Prerequisites
<a name="CWL_Syslog_Setup_Prerequisites"></a>

The IAM identity (user or role) that you use to set up syslog ingestion must have permissions to create VPC endpoints, log groups, resource policies, and syslog configurations. The following example policy shows the minimum required permissions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:PutResourcePolicy",
        "logs:DeleteResourcePolicy",
        "logs:PutSyslogConfiguration",
        "logs:ListSyslogConfigurations",
        "logs:DeleteSyslogConfiguration"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateVpc",
        "ec2:ModifyVpcAttribute",
        "ec2:CreateSubnet",
        "ec2:CreateSecurityGroup",
        "ec2:AuthorizeSecurityGroupIngress",
        "ec2:CreateVpcEndpoint",
        "ec2:ModifyVpcEndpoint",
        "ec2:DescribeVpcEndpoints"
      ],
      "Resource": "*"
    }
  ]
}
```

**Note**  
If you already have a VPC, subnet, and security group, you only need the `ec2:CreateVpcEndpoint`, `ec2:ModifyVpcEndpoint`, and `ec2:DescribeVpcEndpoints` permissions for the EC2 actions.

## Step 1: Create or identify a VPC
<a name="CWL_Syslog_Setup_VPC"></a>

You need a VPC that is reachable from your on-premises network (via VPN or Direct Connect) where your syslog-generating devices reside. If you already have a VPC connected to your data center, skip this step and use your existing VPC and subnet IDs.

------
#### [ Console ]

**To create a VPC (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Your VPCs**, then choose **Create VPC**.

1. For **Resources to create**, choose **VPC only**.

1. For **IPv4 CIDR block**, enter `10.0.0.0/16` (or a CIDR that does not conflict with your on-premises network).

1. Choose **Create VPC**.

1. Select the newly created VPC, choose **Actions**, **Edit VPC settings**. Enable both **DNS resolution** and **DNS hostnames**, then choose **Save**.

1. Create a subnet for the VPC endpoint:

   1. In the navigation pane, choose **Subnets**, then choose **Create subnet**.

   1. For **VPC ID**, select the VPC you created.

   1. For **Availability Zone**, choose an Availability Zone.

   1. For **IPv4 subnet CIDR block**, enter `10.0.1.0/24`.

   1. Choose **Create subnet**.

------
#### [ AWS CLI ]

```
REGION=us-east-1

# Create VPC
VPC_ID=$(aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --region $REGION \
  --query 'Vpc.VpcId' --output text)

aws ec2 modify-vpc-attribute --vpc-id $VPC_ID --enable-dns-support --region $REGION
aws ec2 modify-vpc-attribute --vpc-id $VPC_ID --enable-dns-hostnames --region $REGION

# Create a subnet for the VPC endpoint
SUBNET_ID=$(aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.1.0/24 \
  --availability-zone ${REGION}a \
  --region $REGION \
  --query 'Subnet.SubnetId' --output text)

echo "VPC: $VPC_ID, Subnet: $SUBNET_ID"
```

------

**Note**  
The VPC endpoint creates an elastic network interface (ENI) with a private IP in your subnet. Your on-premises devices reach this IP via your VPN or Direct Connect connection. Ensure your network routing allows traffic from your devices to the subnet CIDR.

## Step 2: Create a security group
<a name="CWL_Syslog_Setup_SG"></a>

Create a security group for the VPC endpoint that allows inbound syslog traffic from your VPC. This controls which resources can send syslog to the endpoint.

------
#### [ Console ]

**To create a security group (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security groups**, then choose **Create security group**.

1. For **Security group name**, enter `syslog-vpce-sg`.

1. For **Description**, enter `Allow syslog traffic to VPC endpoint`.

1. For **VPC**, select the VPC you created or identified in Step 1.

1. In the **Inbound rules** section, choose **Add rule** and add the following rules:
   + **Rule 1:** Type = **Custom TCP**, Port range = `6514`, Source = `10.0.0.0/16` (your VPC CIDR)
   + **Rule 2:** Type = **Custom TCP**, Port range = `1514`, Source = `10.0.0.0/16`
   + **Rule 3:** Type = **Custom UDP**, Port range = `514`, Source = `10.0.0.0/16`

1. Choose **Create security group**.

------
#### [ AWS CLI ]

```
VPCE_SG_ID=$(aws ec2 create-security-group \
  --group-name syslog-vpce-sg \
  --description "Allow syslog traffic to VPC endpoint" \
  --vpc-id $VPC_ID \
  --region $REGION \
  --query 'GroupId' --output text)

# Allow TCP+TLS (port 6514), TCP plaintext (port 1514), and UDP (port 514)
aws ec2 authorize-security-group-ingress --group-id $VPCE_SG_ID \
  --protocol tcp --port 6514 --cidr 10.0.0.0/16 --region $REGION
aws ec2 authorize-security-group-ingress --group-id $VPCE_SG_ID \
  --protocol tcp --port 1514 --cidr 10.0.0.0/16 --region $REGION
aws ec2 authorize-security-group-ingress --group-id $VPCE_SG_ID \
  --protocol udp --port 514 --cidr 10.0.0.0/16 --region $REGION
```

------

**Tip**  
If you only plan to use one protocol (for example, TCP\+TLS on port 6514), you only need to open that port in the security group.

## Step 3: Create the VPC endpoint
<a name="CWL_Syslog_Setup_VPCE"></a>

Create an interface VPC endpoint pointing to the syslog AWS PrivateLink service. This gives your VPC a private entry point to the CloudWatch Logs syslog service.

**Note**  
You can specify multiple subnet IDs across different Availability Zones when creating the endpoint. The endpoint creates an ENI in each subnet, providing higher availability without needing separate VPC endpoints per Availability Zone. A single VPC endpoint with subnets in multiple Availability Zones is sufficient.

------
#### [ Console ]

**To create the VPC endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**, then choose **Create endpoint**.

1. For **Name tag**, enter a name for the endpoint (for example, `syslog-vpce`).

1. For **Service category**, choose **AWS services**.

1. In the **Services** search field, enter `syslog-logs` and select the service `com.amazonaws.{{Region}}.syslog-logs`.

1. For **VPC**, select the VPC you created or identified in Step 1.

1. In the **Subnets** section, select one or more Availability Zones and choose the subnets where you want to create the endpoint network interfaces.

1. For **Security groups**, select the security group you created in Step 2 (`syslog-vpce-sg`).

1. (Optional) If you want to restrict what traffic is allowed through the endpoint, configure a VPC endpoint policy. For more information, see [VPC endpoint policies for syslog](CWL_Syslog_VPCEndpointPolicies.md).

1. Choose **Create endpoint**.

1. After the endpoint state changes to **Available**, select the endpoint and note the **DNS names** value. This is the address your syslog devices will send to.

------
#### [ AWS CLI ]

```
VPCE_ID=$(aws ec2 create-vpc-endpoint \
  --vpc-id $VPC_ID \
  --service-name com.amazonaws.${REGION}.syslog-logs \
  --vpc-endpoint-type Interface \
  --subnet-ids $SUBNET_ID \
  --security-group-ids $VPCE_SG_ID \
  --region $REGION \
  --query 'VpcEndpoint.VpcEndpointId' --output text)

echo "VPC Endpoint: $VPCE_ID"
```

Wait for the endpoint to become available (approximately 60 seconds), then retrieve the DNS name:

```
VPCE_DNS=$(aws ec2 describe-vpc-endpoints --vpc-endpoint-ids $VPCE_ID \
  --region $REGION --query 'VpcEndpoints[0].DnsEntries[0].DnsName' --output text)

echo "Endpoint DNS: $VPCE_DNS"
```

Save the `VPCE_DNS` value – you'll configure your syslog devices to send to this address.

------

## Step 4: Create a log group
<a name="CWL_Syslog_Setup_LogGroup"></a>

Create the CloudWatch Logs log group where your syslog messages will be delivered. You can use any log group name. We recommend using a `/syslog/` prefix for organizational clarity.

------
#### [ Console ]

**To create a log group (console)**

1. Open the CloudWatch Logs console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, under **Log Management**, choose **Log groups**.

1. Choose **Create log group**.

1. For **Log group name**, enter `/syslog/my-devices`.

1. (Optional) Configure retention settings and encryption as needed.

1. Choose **Create**.

------
#### [ AWS CLI ]

```
aws logs create-log-group \
  --log-group-name /syslog/my-devices \
  --region $REGION
```

------

You do not need to create a log stream. The syslog service automatically creates a log stream named `{{VPCE_ID}}_Syslog_{{Region}}` (for example, `vpce-0abc123def456_Syslog_us-east-1`) when the first message is delivered.

## Step 5: Add a resource policy
<a name="CWL_Syslog_Setup_ResourcePolicy"></a>

The CloudWatch Logs syslog service writes to your log group using the `syslog.logs.amazonaws.com` Service Principal. You must grant it permission via a resource policy on your log group. The `aws:SourceArn` condition ensures only traffic from your specific VPC endpoint can write to this log group.

```
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

aws logs put-resource-policy \
  --policy-name syslog-ingestion \
  --policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "syslog.logs.amazonaws.com"
      },
      "Action": [
        "logs:PutLogEvents",
        "logs:CreateLogStream"
      ],
      "Resource": "arn:aws:logs:'$REGION':'$ACCOUNT_ID':log-group:/syslog/my-devices:*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "'$ACCOUNT_ID'"
        },
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:ec2:'$REGION':'$ACCOUNT_ID':vpc-endpoint/'$VPCE_ID'"
        }
      }
    }
  ]
}' \
  --region $REGION
```

The conditions in the resource policy provide the following protections:
+ `aws:SourceAccount` – Prevents confused deputy attacks. Only your account's traffic is accepted.
+ `aws:SourceArn` – Scopes access to a specific VPC endpoint. If you have multiple VPC endpoints, add each one as a separate ARN in the condition.

To allow multiple VPC endpoints to write to the same log group, use the `ArnLike` condition operator with a wildcard:

```
"ArnLike": {
    "aws:SourceArn": "arn:aws:ec2:us-east-1:123456789012:vpc-endpoint/*"
}
```

## Step 6: Create the syslog configuration
<a name="CWL_Syslog_Setup_Config"></a>

This step tells the CloudWatch Logs syslog service that traffic arriving from your VPC endpoint should be routed to your log group. Without this configuration, traffic from your endpoint is rejected.

------
#### [ Console ]

**To create the syslog configuration (console)**

1. Open the CloudWatch Logs console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, under **Log Management**, choose **Log groups**.

1. Choose the log group you created in Step 4 (for example, `/syslog/my-devices`).

1. In the log group details, locate the **Syslog Ingestion** section.

1. Choose **Configure**.

1. From the VPC endpoint dropdown, select the VPC endpoint you created in Step 3.

1. Choose **Create**.

------
#### [ AWS CLI ]

```
aws logs put-syslog-configuration \
  --log-group-identifier /syslog/my-devices \
  --vpc-endpoint-id $VPCE_ID \
  --region $REGION
```

Verify the configuration:

```
aws logs list-syslog-configurations \
  --log-group-identifier /syslog/my-devices \
  --region $REGION
```

------

Your syslog ingestion pipeline is now active. Any syslog messages sent to the VPC endpoint will be delivered to the `/syslog/my-devices` log group.

## Step 7: Verify delivery and field extraction
<a name="CWL_Syslog_Setup_Verify"></a>

Send a test message from any EC2 host or device that can reach the VPC endpoint, then use CloudWatch Log Analytics to verify that the message was delivered and that structured fields were extracted correctly. Messages typically appear within 10–20 seconds.

**Send a test message (TCP plaintext):**

```
echo "<134>1 $(date -u +%Y-%m-%dT%H:%M:%SZ) myhost myapp 1234 - - Hello from syslog" | \
  nc $VPCE_DNS 1514
```

**Verify delivery and extracted fields:**

------
#### [ Console ]

**To verify delivery using Log Analytics (console)**

1. Open the CloudWatch Logs console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, under **Logs**, choose **Log Analytics**.

1. In the log group selector, choose your log group (for example, `/syslog/my-devices`).

1. Enter the following query and choose **Run query**:

   ```
   fields @timestamp, facility, severity, hostname, appName, procId, message
   | sort @timestamp desc
   | limit 10
   ```

1. Verify that your test message appears and that the extracted fields are populated correctly. For the test message above, you should see `facility` = `local0`, `severity` = `info`, `hostname` = `myhost`, `appName` = `myapp`, and `procId` = `1234`.

------
#### [ AWS CLI ]

Start a Log Analytics query to verify delivery and field extraction:

```
QUERY_ID=$(aws logs start-query \
  --log-group-name /syslog/my-devices \
  --start-time $(date -d '5 minutes ago' +%s 2>/dev/null || echo $(date -v-5M +%s)) \
  --end-time $(date +%s) \
  --query-string 'fields @timestamp, facility, severity, hostname, appName, procId, message | sort @timestamp desc | limit 10' \
  --region $REGION \
  --query 'queryId' --output text)

# Wait a few seconds for the query to complete, then retrieve results
aws logs get-query-results \
  --query-id $QUERY_ID \
  --region $REGION
```

Verify that your test message appears and that the extracted fields are populated correctly. For the test message above, you should see `facility` = `local0`, `severity` = `info`, `hostname` = `myhost`, `appName` = `myapp`, and `procId` = `1234`.

------


# Accelerate onboarding prerequisites
<a name="acc-gs-prereqs"></a>

Before you start the onboarding process, it is important to understand the technical dependencies that Accelerate components rely on.

**Note**  
To use AMS Accelerate, you must be on one of the two supported Support plans: Enterprise On-Ramp or Enterprise. The Developer and Business plans are not eligible for qualifying for AMS Accelerate. To learn more about the different plans, see [Compare Support Plans](https://aws.amazon.com/premiumsupport/plans/).

## AMS Accelerate VPC endpoints
<a name="acc-vpc-endpoints"></a>

A VPC endpoint enables private connections between your VPC and supported AWS services and VPC endpoint services powered by AWS. If you need to filter outbound internet connectivity, configure the following VPC service endpoints to ensure that AMS Accelerate has connectivity with its service dependencies.

**Note**  
In the following list, {{region}} represents the identifier for an AWS Region, for example `us-east-2` for the US East (Ohio) Region.

```
com.amazonaws.{{region}}.logs
com.amazonaws.{{region}}.monitoring
com.amazonaws.{{region}}.ec2
com.amazonaws.{{region}}.ec2messages
com.amazonaws.{{region}}.ssm
com.amazonaws.{{region}}.ssmmessages
com.amazonaws.{{region}}.s3
com.amazonaws.{{region}}.events
```

For information about how to configure AWS VPC endpoints, see [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html). 

**Note**  
If you are creating VPC endpoints in your account for all of the above mentioned services, then see this [sample CloudFormation template](https://maxis-file-service-prod-dub.dub.proxy.amazon.com/issues/d2db9efe-7f92-4e17-98c6-1522449f43aa/attachments/d0469f4d1fadfa88580a640666f0886bdef5dccfc6272104ab4ca37c3c7a1eb4_f317b3ec-e76b-43cc-8ca2-847f0671d445). You can update this template and remove or add VPC endpoints definition as per your use-case.

## Outbound internet connectivity in Accelerate
<a name="acc-gs-prereqs-ob"></a>

1. Download [`egressMgmt.zip`](samples/egressMgmt.zip).

1. Open the **`ams-egress.json`** file.

1. Find the URLs under the JSON properties:
   + `WindowsPatching`
   + `RedHatPatching`
   + `AmazonLinuxPatching`
   + `EPELRepository`

1. Allow access to these URLs.

## Testing outbound connectivity in Accelerate
<a name="acc-gs-prereqs-ob-test"></a>

Test outbound connectivity using one of the following methods.

**Note**  
Before running the script/command, replace the red {{region}} with your Region identifier, for example, `us-east-1`.

**Windows PowerShell script**

```
$region = '{{region}}'
@('logs', 'monitoring', 'ec2', 'ec2messages', 'ssm', 'ssmmessages', 's3', 'events') |
    ForEach-Object {
        Test-NetConnection ("$_.$region.amazonaws.com") -Port 443
    } |
    Format-Table ComputerName, RemotePort, RemoteAddress, PingSucceeded, TcpTestSucceeded -AutoSize
```

**Linux command**

```
region='{{region}}'
for endpoint in logs monitoring ec2 ec2messages ssm ssmmessages s3 events; do
    nc -zv "$endpoint.$region.amazonaws.com" 443
done
```

## Amazon EC2 Systems Manager in Accelerate
<a name="acc-gs-prereqs-sysman"></a>

You must install the AWS Systems Manager Agent (SSM Agent) on all of the EC2 instances you want AMS to manage. You also need to add the [ bucket permissions](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-minimum-s3-permissions.html#ssm-agent-minimum-s3-permissions-required) that SSM Agent requires. For an overview that includes Amazon EC2, see [Step 3. Onboarding AMS features with default policies](acc-get-feature-config.md).

## IAM in Accelerate
<a name="acc-gs-prereqs-iam"></a>

To allow your users to read and configure AMS Accelerate capabilities, like accessing the AMS console or configuring backups, you must grant explicit permissions in AWS Identity and Access Management (IAM) to perform those actions. For example IAM policies, see [Permissions to use AMS features](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-access-customer.html).
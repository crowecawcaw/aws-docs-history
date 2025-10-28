# Accelerate onboarding prerequisites

Before you start the onboarding process, it is important to understand the technical dependencies that Accelerate components rely on.

###### Note

To use AMS Accelerate, you must be on one of the two supported Support plans: Enterprise On-Ramp or Enterprise. The Developer and Business plans are not
eligible for qualifying for AMS Accelerate. To learn more about the different plans, see
[Compare Support Plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/").

## AMS Accelerate VPC endpoints

A VPC endpoint enables private connections between your VPC and supported AWS services and VPC endpoint services
powered by AWS. If you need to filter outbound internet connectivity, configure the following VPC service endpoints to
ensure that AMS Accelerate has connectivity with its service dependencies.

###### Note

In the following list, `region` represents the identifier for an AWS Region, for example `us-east-2` for the
US East (Ohio) Region.

```
com.amazonaws.`region`.logs
com.amazonaws.`region`.monitoring
com.amazonaws.`region`.ec2
com.amazonaws.`region`.ec2messages
com.amazonaws.`region`.ssm
com.amazonaws.`region`.ssmmessages
com.amazonaws.`region`.s3
com.amazonaws.`region`.events
```

For information about how to configure AWS VPC endpoints, see
[VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints.md "../../../vpc/latest/privatelink/vpc-endpoints.md").

###### Note

If you are creating VPC endpoints in your account for all of the above mentioned services,
then see this [sample AWS CloudFormation template](https://maxis-file-service-prod-dub.dub.proxy.amazon.com/issues/d2db9efe-7f92-4e17-98c6-1522449f43aa/attachments/d0469f4d1fadfa88580a640666f0886bdef5dccfc6272104ab4ca37c3c7a1eb4_f317b3ec-e76b-43cc-8ca2-847f0671d445 "https://maxis-file-service-prod-dub.dub.proxy.amazon.com/issues/d2db9efe-7f92-4e17-98c6-1522449f43aa/attachments/d0469f4d1fadfa88580a640666f0886bdef5dccfc6272104ab4ca37c3c7a1eb4_f317b3ec-e76b-43cc-8ca2-847f0671d445"). You can update this template and remove or add VPC endpoints
definition as per your use-case.

## Outbound internet connectivity in Accelerate

1. Download [`egressMgmt.zip`](samples/egressMgmt.md "samples/egressMgmt.md").
2. Open the **`ams-egress.json`** file.
3. Find the URLs under the JSON properties:
   - `WindowsPatching`
   - `RedHatPatching`
   - `AmazonLinuxPatching`
   - `EPELRepository`

4. Allow access to these URLs.

## Testing outbound connectivity in Accelerate

Test outbound connectivity using one of the following methods.

###### Note

Before running the script/command, replace the red `region` with your
Region identifier, for example, `us-east-1`.

**Windows PowerShell script**

```
$region = '`region`'
@('logs','monitoring','ec2','ec2messages','ssm','ssmmessages','s3','events') | `
ForEach-Object { `
Test-NetConnection ("$_" + '.' + "$region" + '.amazonaws.com') -Port 443 } | `
Format-Table ComputerName,RemotePort,RemoteAddress,PingSucceeded,TcpTestSucceeded -AutoSize
```

**Linux command**

```
for endpoint in logs monitoring ec2 ec2messages ssm ssmmessages s3 events; do nc -zv $endpoint.`region`.amazonaws.com 443; done
```

## Amazon EC2 Systems Manager in Accelerate

You must install the AWS Systems Manager Agent (SSM Agent) on all of the EC2 instances
you want AMS to manage. You also need to add the [bucket permissions](../../../systems-manager/latest/userguide/ssm-agent-minimum-s3-permissions.md#ssm-agent-minimum-s3-permissions-required "../../../systems-manager/latest/userguide/ssm-agent-minimum-s3-permissions.md#ssm-agent-minimum-s3-permissions-required") that SSM Agent requires. For an overview that
includes Amazon EC2, see [Step 3. Onboarding AMS features with default policies](acc-get-feature-config.md "acc-get-feature-config.md").

## IAM in Accelerate

To allow your users to read and configure AMS Accelerate capabilities, like accessing the AMS console or configuring backups,
you must grant explicit permissions in AWS Identity and Access Management (IAM) to perform those actions. For example IAM policies, see
[Permissions to use AMS features](acc-access-customer.md "acc-access-customer.md").

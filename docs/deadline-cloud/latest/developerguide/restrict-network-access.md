

# Restrict farm access to your network
<a name="restrict-network-access"></a>

Every request to your farm goes through the Deadline Cloud APIs. The monitor, the AWS CLI, the submitters, and the AWS Management Console all call the APIs with temporary credentials, so the network boundary belongs on the API calls. The monitor URL is reachable from any location on the internet and holds no farm data. For more information, see [Access to the monitor web application](security-data-flow.md#security-data-flow-monitor).

Add a network condition to the IAM policies of the credentials that your people use:
+ The monitor gets its credentials from the monitor role. So do the AWS CLI and the submitters when they use the profile that the Deadline Cloud monitor creates. Add a custom policy to the monitor role. For more information, see [Adding permissions for advanced workflows](security-iam-service-roles.md#adding-monitor-permissions).
+ The AWS Management Console and pipeline scripts use their own IAM roles or users. Add the condition to those policies, or to the permission sets that you assign for AWS Management Console access in IAM Identity Center.

## Allow only your IP ranges
<a name="restrict-network-access-ip"></a>

An `aws:SourceIp` condition limits requests to the public addresses that you list. List the addresses that your studio sends traffic from. Include your office ranges, your VPN exit addresses, and the NAT gateway addresses of any VPC where your workstations run.

The following policy denies Deadline Cloud requests from any other address. Attach it to the monitor role, alongside the managed policies that the role already has.

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "deadline:*",
      "Resource": "*",
      "Condition": {
        "NotIpAddress": {
          "aws:SourceIp": [
            "{{203.0.113.0/24}}",
            "{{198.51.100.10/32}}"
          ]
        },
        "BoolIfExists": {
          "aws:ViaAWSService": "false"
        }
      }
    }
  ]
}
```

The policy covers your files as well as your farm. Job attachments and job logs need queue role credentials. The monitor, the AWS CLI, and the submitters get those credentials by calling `AssumeQueueRoleForUser`. The deny blocks the call from any address that you didn't list.

If you sign in from an address that you didn't list, you still reach the sign-in page. The monitor then reports errors instead of showing farm data. An allow can't override a deny, so verify your ranges before you attach the policy.

**Important**  
The preceding policy also denies requests that arrive through an Deadline Cloud interface endpoint. Endpoint traffic carries `aws:VpcSourceIp` instead of `aws:SourceIp`, and a `NotIpAddress` condition on an absent key matches, so the deny applies. If your people reach Deadline Cloud through an interface endpoint, use the VPC form in the next section. To allow both paths, put both keys in the same condition block. The deny then applies only when neither key matches. Test the policy from both networks before you roll it out.

For more information about the keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

## Allow access only from your VPC
<a name="restrict-network-access-vpc"></a>

To require that people work from hosts in a VPC, such as virtual workstations, combine three pieces:

1. Run the monitor, the AWS CLI, and the submitters on hosts in the VPC.

1. Create an interface endpoint in the VPC for the Deadline Cloud management endpoint. Add Amazon S3 and CloudWatch Logs endpoints if your people upload job attachments and read job logs. Enable private DNS so that the client tools use the endpoints without extra configuration. For more information, see [Access AWS Deadline Cloud using an interface endpoint (AWS PrivateLink)](vpc-interface-endpoints.md).

1. Attach a policy to the monitor role that denies requests from outside the VPC. The VPC keys hold strings, so the condition operator is `StringNotEquals` rather than `NotIpAddress`.

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "deadline:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:SourceVpc": "{{vpc-0123456789abcdef0}}"
        },
        "BoolIfExists": {
          "aws:ViaAWSService": "false"
        }
      }
    }
  ]
}
```

To name individual endpoints instead of the whole VPC, use `aws:SourceVpce` with your endpoint IDs. To name address ranges inside the VPC, use `aws:VpcSourceIp` with `NotIpAddress`.

The monitor web application, the IAM Identity Center portal, and AWS Sign-In have no interface endpoints. The browser on the host therefore needs outbound access to the sign-in domains listed in [Restricted network environments](network-connectivity.md). You can route that traffic through a NAT gateway or a web proxy that allows only those domains. Farm data doesn't travel over the sign-in path.

## Keep worker access working
<a name="restrict-network-access-workers"></a>

Your workers share the queue role with your people. A worker uses queue role credentials to read inputs and write outputs while it runs a job. The monitor and the AWS CLI use the same role when someone uploads inputs or downloads outputs. Restrict the monitor role, and leave the queue role and the fleet role without a network condition.

Service-managed fleet workers run on the AWS network, so their addresses aren't in your ranges and their requests don't come through your endpoints. A network condition on the queue role, the fleet role, or the bucket policy of the job attachments bucket denies those requests. Jobs then fail. A bucket policy condition works only if all of your fleets are customer-managed and run in your VPC. In that case, list both your workstation endpoint and your fleet endpoint in an `aws:SourceVpce` condition.

Queue role credentials carry no network condition of their own. Someone who obtains them from an address that you allow can use them from anywhere until they expire. The condition on the monitor role controls who gets credentials, rather than every request that uses them.
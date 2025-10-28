# Prerequisite – Creating

an Amazon VPC endpoint

Before you can install the GuardDuty security agent, you must create an Amazon Virtual Private Cloud (Amazon VPC)
endpoint. This will help GuardDuty receive the runtime events of your Amazon EKS resources.

###### Note

There is no additional cost for the usage of the VPC endpoint.

Choose a preferred access method to create an Amazon VPC endpoint.

Console

###### To create a VPC endpoint

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Virtual private
   cloud**, choose **Endpoints**.
3. Choose **Create Endpoint**.
4. On the **Create endpoint** page, for
   **Service category**, choose **Other
   endpoint services**.
5. For **Service name**, enter
   `com.amazonaws.`us-east-1`.guardduty-data`.

Make sure to replace `us-east-1` with the
correct Region. This must be the same Region as the EKS cluster that
belongs to your AWS account ID. 6. Choose **Verify service**. 7. After the service name is successfully verified, choose the
**VPC** where your cluster resides. Add the
following policy to restrict VPC endpoint usage to specified account
only. With the organization `Condition` provided below
this policy, you can update the following policy to restrict access
to your endpoint. To provide VPC endpoint support to specific
account IDs in your organization, see [Organization condition to restrict access to your endpoint](#gdu-shared-vpc-endpoint-org "#gdu-shared-vpc-endpoint-org").

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "*",
 "Resource": "*",
 "Effect": "Allow",
 "Principal": "*"
 },
 {
 "Condition": {
 "StringNotEquals": {
 "aws:PrincipalAccount": "`111122223333`"
 }
 },
 "Action": "*",
 "Resource": "*",
 "Effect": "Deny",
 "Principal": "*"
 }
 ]
}`

```

The `aws:PrincipalAccount` account ID must match the
account containing the VPC and VPC endpoint. The following list
shows how to share the VPC endpoint with other AWS account
IDs:

###### Organization condition to restrict access to your

endpoint

    * To specify multiple accounts to access the VPC endpoint,
     replace `"aws:PrincipalAccount":
     "`111122223333`"`
     with the following:



    ```
    "aws:PrincipalAccount": [
              "`666666666666`",
              "`555555555555`"
        ]
    ```
    * To allow all the members from an organization to access
     the VPC endpoint, replace `"aws:PrincipalAccount":
     "`111122223333`"`
     with the following:



    ```
    "aws:PrincipalOrgID": "`o-abcdef0123`"
    ```
    * To restrict accessing a resource to an organization ID,
     add your `ResourceOrgID` to the policy.


    For more information, see [ResourceOrgID](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourceorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourceorgid").



    ```
    "aws:ResourceOrgID": "`o-abcdef0123`"
    ```

8. Under **Additional settings**, choose
   **Enable DNS name**.
9. Under **Subnets**, choose the subnets in which
   your cluster resides.
10. Under **Security groups**, choose a security
    group that has the in-bound port 443 enabled from your VPC (or your
    EKS cluster). If you don't already have a security group that has an
    in-bound port 443 enabled, [Create a security group](../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#creating-security-group "../../../AWSEC2/latest/UserGuide/working-with-security-groups.md#creating-security-group").

If there is an issue while restricting the in-bound permissions to
your VPC (or instance), you can the in-bound 443 port from any IP
address `(0.0.0.0/0)`. However, GuardDuty recommends using IP
addresses that matches the CIDR block for your VPC. For more
information, see [VPC CIDR
blocks](../../../vpc/latest/userguide/vpc-cidr-blocks.md "../../../vpc/latest/userguide/vpc-cidr-blocks.md") in the
_Amazon VPC User Guide_.

API/CLI

###### To create a VPC endpoint

- Invoke [CreateVpcEndpoint](../../../AWSEC2/latest/APIReference/API_CreateVpcEndpoint.md "../../../AWSEC2/latest/APIReference/API_CreateVpcEndpoint.md").
- Use the following values for the parameters:
  - For **Service name**, enter
    `com.amazonaws.`us-east-1`.guardduty-data`.

  Make sure to replace `us-east-1`
  with the correct Region. This must be the same Region as the
  EKS cluster that belongs to your AWS account ID.
  - For [DNSOptions](../../../AWSEC2/latest/APIReference/API_DnsOptions.md "../../../AWSEC2/latest/APIReference/API_DnsOptions.md"), enable private DNS option by
    setting it to `true`.

- For AWS Command Line Interface, see [create-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html").

After you have followed the steps, see [Validating VPC
endpoint configuration](validate-vpc-endpoint-config-runtime-monitoring.md "validate-vpc-endpoint-config-runtime-monitoring.md") to ensure that the VPC
endpoint was set up correctly.

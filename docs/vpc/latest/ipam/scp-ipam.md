

# Enforce IPAM use for VPC creation with SCPs
<a name="scp-ipam"></a>

**Note**  
 This section is only applicable to you if you've enabled IPAM to integrate with AWS Organizations. For more information, see [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md).

This section describes how to create a service control policy in AWS Organizations that requires members in your organization to use IPAM when they create a VPC. Service control policies (SCPs) are a type of organization policy that enable you to manage permissions in your organization. For more information, see [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.

## Enforce IPAM when creating VPCs
<a name="scp-ipam-enforce-scen-1"></a>

Follow the steps in this section to require members in your organization to use IPAM when creating VPCs.

**To create an SCP and restrict VPC creation to IPAM**

1. Follow the steps in [Create a service control policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_create.html#create-an-scp) in the *AWS Organizations User Guide* and enter the following text in the JSON editor:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [{
          "Effect": "Deny",
           "Action": ["ec2:CreateVpc", "ec2:AssociateVpcCidrBlock"],
           "Resource": "arn:aws:ec2:*:*:vpc/*",
           "Condition": {
               "Null": {
                   "ec2:Ipv4IpamPoolId": "true"
               }
           }
        }]
   }
   ```

------

1. Attach the policy to one or more organizational units in your organization. For more information, see [Attach policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_attach.html) and [Detach policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_detach.html) in the *AWS Organizations User Guide*.

## Enforce an IPAM pool when creating VPCs
<a name="scp-ipam-enforce-scen-2"></a>

Follow the steps in this section to require members in your organization to use a specific IPAM pool when creating VPCs.

**To create an SCP and restrict VPC creation to an IPAM pool**

1. Follow the steps in [Create a service control policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_create.html#create-an-scp) in the *AWS Organizations User Guide* and enter the following text in the JSON editor:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [{
           "Effect": "Deny",
           "Action": ["ec2:CreateVpc", "ec2:AssociateVpcCidrBlock"],
           "Resource": "arn:aws:ec2:*:*:vpc/*",
           "Condition": {
               "StringNotEquals": {
                   "ec2:Ipv4IpamPoolId": "ipam-pool-0123456789abcdefg"
               }
             }
       }]
   }
   ```

------

1. Change the `ipam-pool-0123456789abcdefg` example value to the IPv4 pool ID you would like to restrict users to.

1. Attach the policy to one or more organizational units in your organization. For more information, see [Attach policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_attach.html) and [Detach policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_detach.html) in the *AWS Organizations User Guide*.

## Enforce IPAM for all but a given list of OUs
<a name="scp-ipam-enforce-scen-3"></a>

Follow the steps in this section to enforce IPAM for all but a given list of Organizational Units (OUs). The policy described in this section requires OUs in the organization except for the OUs that you specify in `aws:PrincipalOrgPaths` to use IPAM to create and expand VPCs. The listed OUs can either use IPAM when creating VPCs or specify an IP address range manually.

**To create an SCP and enforce IPAM for all but a given list of OUs**

1. Follow the steps in [Create a service control policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_create.html#create-an-scp) in the *AWS Organizations User Guide* and enter the following text in the JSON editor:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [{
   	"Effect": "Deny",
   	    "Action": ["ec2:CreateVpc", "ec2:AssociateVpcCidrBlock"],
   	    "Resource": "arn:aws:ec2:*:*:vpc/*",
   	    "Condition": {
   	        "Null": {
   		      "ec2:Ipv4IpamPoolId": "true"
                   },
   	        "ForAnyValue:StringNotLike": {
   	            "aws:PrincipalOrgPaths": [
   	                "o-a1b2c3d4e5/r-ab12/ou-ab12-11111111/ou-ab12-22222222/",
   	                "o-a1b2c3d4e5/r-ab12/ou-ab13-22222222/ou-ab13-33333333/"
   	            ]
                   }
               }
        }]
   }
   ```

------

1. Remove the example values (like `o-a1b2c3d4e5/r-ab12/ou-ab12-11111111/ou-ab12-22222222/`) and add the AWS Organizations entity paths of the OUs that you want to have the option (but not require) to use IPAM. For more information about entity path, see [Understand the AWS Organizations entity path](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_last-accessed-viewing-orgs-entity-path) and [aws:PrincipalOrgPaths](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalorgpaths) in the *IAM User Guide*.

1. Attach the policy to your organization root. For more information, see [Attach policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_attach.html) and [Detach policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_detach.html) in the *AWS Organizations User Guide*.


# Trusted resources
<a name="trusted-resources"></a>

With AWS Management Console Private Access, you can restrict which resources users access through the AWS Management Console to those that belong to your AWS organization. These policies layer on top of the principal-based restrictions described in [Trusted identities](trusted-identities.md); they further limit which resources the allowed principals can reach after signing in.
+ **AWS Management Console VPC endpoint policies** – Use the `aws:ResourceOrgID` or `aws:ResourceAccount` condition keys. `aws:ResourceOrgID` restricts access to resources in a specific AWS organization. `aws:ResourceAccount` restricts access to resources in a specific AWS account.

**Note**  
The following examples are reference policies for illustration only. For production environments, use the comprehensive data perimeter policy examples in the [aws-samples/data-perimeter-policy-examples](https://github.com/aws-samples/data-perimeter-policy-examples) repository, such as the [resource perimeter SCP](https://github.com/aws-samples/data-perimeter-policy-examples/blob/main/service_control_policies/resource_perimeter_scp.json).

**Example: Allow access only to resources in your organization**  
This AWS Management Console VPC endpoint policy uses `aws:ResourceOrgID` to allow access only to resources in the specified AWS organization.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceOrgID": "o-xxxxxxxxxxx"
        }
      }
    }
  ]
}
```

------

**Example: Allow access only to resources in specific accounts**  
This AWS Management Console VPC endpoint policy uses `aws:ResourceAccount` to allow access only to resources in a specific list of AWS accounts.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": [ "111122223333", "222233334444" ]
        }
      }
    }
  ]
}
```

------
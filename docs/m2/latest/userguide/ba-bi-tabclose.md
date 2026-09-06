

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Troubleshooting: AWS Transform for mainframe refactor does not open from the console
<a name="ba-bi-tabclose"></a>

This page describes how you can resolve AWS Transform for mainframe refactor page not opening from the AWS Mainframe Modernization console.
+ Engine: AWS Transform for mainframe
+ Component: AWS Transform for mainframe refactor

When you try to access AWS Transform for mainframe refactor from the AWS Mainframe Modernization console, it doesn't open and the new tab is closed immediately.

## Common cause
<a name="ba-bi-tabclose-cause"></a>

The role you are using to access AWS Transform for mainframe refactor does not have sufficient permissions.

## Resolution
<a name="ba-bi-tabclose-resolution"></a>

Attach an IAM policy to the role to allow it to access AWS Transform for mainframe refactor. Make sure the policy includes at least the following permissions.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "m2:GetSignedBluinsightsUrl"
            ],
            "Resource": "*"
            }
    ]
}
```

------

Make sure to replace `region` and `account` with the correct AWS Region and AWS account.
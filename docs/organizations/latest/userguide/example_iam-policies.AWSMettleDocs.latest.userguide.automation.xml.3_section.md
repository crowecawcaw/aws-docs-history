

# Policy to grant full access to Compute Optimizer Automation for standalone AWS accounts
<a name="example_iam-policies.AWSMettleDocs.latest.userguide.automation.xml.3_section"></a>

The following code example shows how to This permission-based policy grant full access to Compute Optimizer Automation for standalone AWS accounts

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
               "aco-automation:*",
            "ec2:DescribeVolumes"
            ],
            "Resource": "*"
        }
    ]
}
```

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Organizations with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.
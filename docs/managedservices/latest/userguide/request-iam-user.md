

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Restrict permissions with IAM role policy statements
<a name="request-iam-user"></a>

AMS uses an IAM role to set user permissions through your federation service.

**Single-Account Landing Zone AMS**: See [SALZ: Default IAM User Roles](https://docs.aws.amazon.com/managedservices/latest/userguide/defaults-user-role.html#json-default-role).

**Multi-Account Landing Zone AMS**: See [MALZ: Default IAM User Roles](https://docs.aws.amazon.com/managedservices/latest/userguide/defaults-user-role.html#json-default-role-malz).

An IAM role is an IAM entity that defines a set of permissions for making AWS service requests. IAM roles are not associated with a specific user or group. Instead, trusted entities assume roles, such as IAM users, applications, or AWS services such as Amazon EC2. For more information, see [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).

You can scope down the desired policy for a user assuming the AMS IAM user role by using the AWS Security Token Service (STS) API operation [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) by passing a more restrictive IAM policy under the `Policy` request field.

Example policy statements that you can use to restrict CT access are provided next.

Using your configured Active Directory (AD) groups, and the AWS Security Token Service (STS) API operation [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html), you can set permissions for certain users or groups, including restricting access to certain change types (CTs). You can use the policy statements shown below to restrict CT access in various ways.

AMS change type statement in the default IAM instance profile that allows access to all AMS API calls (amscm and amsskms) and all change types:

```
{
    "Sid": "AWSManagedServicesFullAccess",
    "Effect": "Allow",
    "Action": [
        "amscm:*",
        "amsskms:*"
    ],
    "Resource": [
        "*"
    ]
}
```

1. Statement to allow access and all actions for only two specified CTs, where "Action" is the AMS API operations (either `amscm` or `amsskms`), and "Resource" represents existing change type IDs and version number:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "amscm:*",
               "Resource": [
                   "arn:aws:amscm:*:*:changetype/{{ct-ID1:1.0}}",
                   "arn:aws:amscm:*:*:changetype/{{ct-ID2:1.0}}"
               ]
           }
       ]
   }
   ```

------

1. Statement to allow access for CreateRfc, UpdateRfc, and SubmitRfc on only two specified CTs:

1. Statement to allow access for CreateRfc, UpdateRfc, and SubmitRfc on all available CTs:

1. Statement to deny access for all actions on restricted CT and allow on other CTs:
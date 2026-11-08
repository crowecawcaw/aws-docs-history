

# An OpenSearch UI application remains in the Creating state
<a name="application-troubleshooting-creating"></a>

An OpenSearch UI application usually becomes active within a few minutes. In some cases it can remain in the Creating state for longer. Before you investigate, compare the elapsed time against the following expected durations.


| Scenario | Expected creation time | 
| --- | --- | 
| An application with public domains | 2–5 minutes | 
| An application with VPC domains | 5–10 minutes | 
| An application with multiple data sources | 5–15 minutes | 
| An application with cross-account data sources | 10–20 minutes | 
| The first application in a new AWS Region | 5–10 minutes | 

If the application has been in the Creating state for less than 20 minutes, it might still be provisioning normally, especially when VPC domains are involved.

## Checking the application status
<a name="application-troubleshooting-creating-status"></a>

**To check the application status in the console**

1. Open the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/home).

1. On the navigation menu, choose **OpenSearch UI (Dashboards)**.

1. Find your application in the list and review the **Status** column.

To check the status with the AWS CLI, run the following command:

```
aws opensearch get-application \
    --id {{application-id}} \
    --region {{region}}
```

Review the `status` field in the response.

## Cause: insufficient IAM permissions
<a name="application-troubleshooting-creating-permissions"></a>

Missing IAM permissions are the most common cause. The application remains in the Creating state for more than 20 minutes, the console shows no error message, and AWS CloudTrail records `AccessDenied` events.

Confirm that the principal creating the application has the following permissions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "es:CreateApplication",
                "es:GetApplication",
                "es:UpdateApplication",
                "es:ListApplications",
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": "*"
        }
    ]
}
```

**Important**  
The `iam:CreateServiceLinkedRole` permission is required. OpenSearch UI creates a service-linked role on first use, and if this permission is missing, you cannot create the application, and the console does not report an error.

## Cause: a problem with the service-linked role
<a name="application-troubleshooting-creating-slr"></a>

OpenSearch UI uses the `AWSServiceRoleForAmazonOpenSearchService` service-linked role to manage resources on your behalf. If OpenSearch UI cannot create that role, application creation fails. This typically affects the first application in an account, and AWS CloudTrail records `CreateServiceLinkedRole` failures.

Check whether the role exists:

```
aws iam get-role \
    --role-name AWSServiceRoleForAmazonOpenSearchService
```

If the role does not exist, create it:

```
aws iam create-service-linked-role \
    --aws-service-name opensearchservice.amazonaws.com
```

**Important**  
Don't delete the service-linked role in order to recreate it. The role is account-wide, and every Amazon OpenSearch Service resource in the account depends on it, including domains and serverless collections. IAM refuses to delete a service-linked role while any resource still depends on it, and deleting it can disrupt the other resources that use it.

If the role exists but the problem persists, confirm that your IAM principal has `iam:CreateServiceLinkedRole`, and then open an AWS Support case.

## Cause: VPC endpoint provisioning delays
<a name="application-troubleshooting-creating-vpc"></a>

When an application includes VPC-based data sources, OpenSearch UI must create VPC endpoints, which takes longer than associating public domains. Allow up to 20 minutes.

While you wait, confirm that VPC endpoint access is authorized:

```
aws opensearch list-vpc-endpoint-access \
    --domain-name {{domain-name}}
```

Also confirm that the security group of the domain allows inbound traffic on TCP port 443. For more information, see [Resolving VPC connectivity problems in OpenSearch UI](application-troubleshooting-vpc.md).

## Cause: an associated domain is not active
<a name="application-troubleshooting-creating-datasource"></a>

If an associated domain is itself creating, processing, or upgrading, application creation can stop while it waits. Check the status of every associated domain:

```
aws opensearch describe-domain \
    --domain-name {{domain-name}} \
    --region {{region}}
```

Wait until all domains are active before you create the application. Alternatively, create the application without data sources and add them after it becomes active:

```
aws opensearch create-application \
    --name {{application-name}} \
    --region {{region}}

aws opensearch update-application \
    --id {{application-id}} \
    --data-sources '[{"dataSourceArn":"arn:aws:es:{{region}}:{{account-id}}:domain/{{domain-name}}"}]'
```

## Cause: a service control policy denies the request
<a name="application-troubleshooting-creating-scp"></a>

A service control policy in AWS Organizations can deny the permissions that application creation requires, even when the IAM policy allows them. In this case the IAM permissions appear correct, the application still does not finish, and AWS CloudTrail records an `AccessDenied` event that cites a service control policy.

Review the service control policies that apply to the account, confirm that they allow `es:CreateApplication` and `iam:CreateServiceLinkedRole`, and work with your organization administrator to add an exception if one is required.

## Cause: the application quota is reached
<a name="application-troubleshooting-creating-quota"></a>

Each AWS Region limits the number of OpenSearch UI applications that you can create. Check how many applications already exist:

```
aws opensearch list-applications --region {{region}}
```

If you have reached the quota, request an increase in the Service Quotas console. For the current quota, see [OpenSearch UI endpoints and quotas](opensearch-ui-endpoints-quotas.md). OpenSearch UI must also be available in the AWS Region where you are creating the application.

## Using the diagnostic checklist
<a name="application-troubleshooting-creating-checklist"></a>

1. Confirm how long the application has been in the Creating state. If it is less than 20 minutes, wait.

1. Check AWS CloudTrail for `AccessDenied` or other error events.

1. Verify the IAM permissions, especially `iam:CreateServiceLinkedRole`.

1. Confirm that every associated domain is active.

1. Confirm VPC endpoint authorization, if you use VPC domains.

1. Confirm that you have not reached the application quota.

1. Review service control policies, if the account belongs to an organization.

If the application has been in the Creating state for more than 30 minutes and you have checked each item, delete the application, wait five minutes for cleanup, resolve the problem that you identified, and create a new application. Deleting an application that never became active does not delete saved objects or workspace data, because none were created.

```
aws opensearch delete-application \
    --id {{application-id}} \
    --region {{region}}
```
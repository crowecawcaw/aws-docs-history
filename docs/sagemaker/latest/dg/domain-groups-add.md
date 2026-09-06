

# Add groups and users
<a name="domain-groups-add"></a>

The following sections show how to add groups and users to a domain from the SageMaker AI console or AWS CLI. 

**Note**  
If the domain was created before October 1st, 2023, you can only add groups and users to the domain from the SageMaker AI console.

## SageMaker AI console
<a name="domain-groups-add-console"></a>

 Complete the following procedure to add groups and users to your domain from the SageMaker AI console. 

1.  On the **Groups** tab, choose **Assign users and groups**. 

1.  On the **Assign users and groups** page, select the users and groups that you want to add. 

1.  Choose **Assign users and groups**. 

## AWS CLI
<a name="domain-groups-add-cli"></a>

 Complete the following procedure to add groups and users to your domain from the AWS CLI. 

1. Fetch the `SingleSignOnApplicationArn` of the domain with a call to [describe-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-domain.html). `SingleSignOnApplicationArn` is the ARN of the application managed in IAM Identity Center.

   ```
   aws sagemaker describe-domain \
   --region {{region}} \
   --domain-id {{domain-id}}
   ```

1. Associate the user or group with the domain. To accomplish this, pass the `SingleSignOnApplicationArn` value returned from the [describe-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-domain.html) command as the `application-arn` parameter in a call to [create-application-assignment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-application-assignment.html).You must also pass the type and ID of the entity to associate.

   ```
   aws sso-admin create-application-assignment \
   --application-arn {{application-arn}} \
   --principal-id {{principal-id}} \
   --principal-type {{principal-type}}
   ```
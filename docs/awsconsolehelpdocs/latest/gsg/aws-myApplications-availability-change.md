

# myApplications availability change
<a name="aws-myApplications-availability-change"></a>

myApplications no longer allows creation of new applications or updates of existing applications. Existing users may continue to access and view their previously created applications. AWS will continue to address critical security patches and operational issues. No new features, integrations, or regional expansions will be released.

## Alternative solutions
<a name="myApp-availability-alternatives"></a>

We recommend using **AWS Resource Groups** – Tag-based collections of related AWS resources, available across the Console, CLI, and SDK. Suitable for customers who need a lightweight way to group and view resources. [Learn more](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html).

## Migration steps
<a name="myApp-availability-migration"></a>

No action is required. Resources you previously associated with myApplications retain the `awsApplication` tag and remain accessible through tools like AWS Resource Groups. You can use this tag to locate and group your resources:
+ Tag key: `awsApplication`
+ Tag value: `arn:aws:resource-groups:{{us-east-1}}:{{123456789012}}:group/{{applicationName}}/{{UniqueIdentifier}}`

If you have additional questions, contact [AWS Support](https://aws.amazon.com/support).
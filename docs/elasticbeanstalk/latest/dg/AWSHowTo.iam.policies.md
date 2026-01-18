# Resources and conditions for Elastic Beanstalk actions

This section describes the resources and conditions that you can use in policy statements to
grant permissions that allow specific Elastic Beanstalk actions to be performed on specific Elastic Beanstalk
resources.

Conditions enable you to specify permissions to resources that the action needs to complete.
For example, when you can call the `CreateEnvironment` action, you must also specify
the application version to deploy as well as the application that contains that application
name. When you set permissions for the `CreateEnvironment` action, you specify the
application and application version that you want the action to act upon by using the
`InApplication` and `FromApplicationVersion` conditions.

In addition, you can specify the environment configuration with a solution stack
(`FromSolutionStack`) or a configuration template
(`FromConfigurationTemplate`). The following policy statement allows the
`CreateEnvironment` action to create an environment with the name
`myenv` (specified by `Resource`) in the application
`My App` (specified by the `InApplication` condition) using
the application version `My Version` (`FromApplicationVersion`)
with a `32bit Amazon Linux running Tomcat 7` configuration
(`FromSolutionStack`):

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticbeanstalk:CreateEnvironment"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"
 ],
 "Condition": {
 "StringEquals": {
 "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"],
 "elasticbeanstalk:FromApplicationVersion": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"],
 "elasticbeanstalk:FromSolutionStack": ["arn:aws:elasticbeanstalk:us-east-2::solutionstack/32bit Amazon Linux running Tomcat 7"]
 }
 }
 }
 ]
}`

```

###### Note

Most condition keys mentioned in this topic are specific to Elastic Beanstalk, and their names contain the `elasticbeanstalk:` prefix. For brevity, we
omit this prefix from the condition key names when we mention them in the following sections. For example, we mention `InApplication` instead
of its full name `elasticbeanstalk:InApplication`.

In contrast, we mention a few condition keys used across AWS services, and we include their `aws:` prefix to highlight the
exception.

Policy examples always show full condition key names, including the prefix.

###### Sections

- [Policy information for Elastic Beanstalk
  actions](#AWSHowTo.iam.policies.actions.table "#AWSHowTo.iam.policies.actions.table")
- [Condition keys for Elastic Beanstalk actions](#AWSHowTo.iam.policies.conditions "#AWSHowTo.iam.policies.conditions")

## Policy information for Elastic Beanstalk

actions

The following table lists all Elastic Beanstalk actions, the resource that each action acts upon, and
the additional contextual information that can be provided using conditions.

Policy information for Elastic Beanstalk actions, including resources, conditions, examples, and
dependencies| Resource | Conditions | Example statement |
| --- | --- | --- |
| **Action:\*<br>• [`AbortEnvironmentUpdate`](../api/API_AbortEnvironmentUpdate.md "../api/API_AbortEnvironmentUpdate.md") |
| `application`<br>`environment` | `aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows a user to abort environment update operations on<br>environments in an application named`My App`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:AbortEnvironmentUpdate"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:_<br>• [`CheckDNSAvailability`](../api/API_CheckDNSAvailability.md "../api/API_CheckDNSAvailability.md") |
| `"_"` | N/A | ```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:CheckDNSAvailability"<br>],<br>"Effect": "Allow",<br>"Resource": "_"<br>}<br>]<br>}`<br>``` |
| \*\*Action:_<br>• [`ComposeEnvironments`](../api/API_ComposeEnvironments.md "../api/API_ComposeEnvironments.md") |
| `application` | `aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows a user to compose environments that belong to an<br>application named `My App`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:ComposeEnvironments"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/*"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`CreateApplication`](../api/API_CreateApplication.md "../api/API_CreateApplication.md") |
| `application` | `aws:RequestTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | This example allows the `CreateApplication` action to create<br>applications whose names begin with `DivA`:<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:CreateApplication"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:application/DivA*"<br>]<br>}<br>]<br>}`<br>`` |
| **Action:*<br>• [`CreateApplicationVersion`](../api/API_CreateApplicationVersion.md "../api/API_CreateApplicationVersion.md") |
| `applicationversion` | `InApplication`<br>`aws:RequestTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | This example allows the`CreateApplicationVersion` action to create<br>application versions with any name (`*`) in the application<br>`My App`:<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:CreateApplicationVersion"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/*"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br>}<br>}<br>}<br>]<br>}`<br>``` |
| **Action:_<br>• [`CreateConfigurationTemplate`](../api/API_CreateConfigurationTemplate.md "../api/API_CreateConfigurationTemplate.md") |
| `configurationtemplate` | `InApplication`<br>`FromApplication`<br>`FromApplicationVersion`<br>`FromConfigurationTemplate`<br>`FromEnvironment`<br>`FromSolutionStack`<br>`aws:RequestTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`CreateConfigurationTemplate`action<br>to create configuration templates whose name begins with`My<br>Template` (`My Template_`) in the application `My<br>App`:<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:CreateConfigurationTemplate"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:configurationtemplate/My App/My Template*"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"],<br>"elasticbeanstalk:FromSolutionStack": ["arn:aws:elasticbeanstalk:us-east-2::solutionstack/32bit Amazon Linux running Tomcat 7"]<br>}<br>}<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`CreateEnvironment`](../api/API_CreateEnvironment.md "../api/API_CreateEnvironment.md") |
| `environment`|`InApplication`<br>`FromApplicationVersion`<br>`FromConfigurationTemplate`<br>`FromSolutionStack`<br>`aws:RequestTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`CreateEnvironment`action to create<br>an environment whose name is`myenv` in the application<br>`My App`and using the solution stack`32bit Amazon<br>Linux running Tomcat 7`:<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:CreateEnvironment"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"],<br>"elasticbeanstalk:FromApplicationVersion": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"],<br>"elasticbeanstalk:FromSolutionStack": ["arn:aws:elasticbeanstalk:us-east-2::solutionstack/32bit Amazon Linux running Tomcat 7"]<br>}<br>}<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`CreatePlatformVersion`](../api/API_CreatePlatformVersion.md "../api/API_CreatePlatformVersion.md") |
| `platform`|`aws:RequestTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | This example allows the`CreatePlatformVersion`action to create<br>platform versions targeting the`us-east-2`region, whose names begin with`us-east-2*`:<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:CreatePlatformVersion"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:platform/us-east-2*_"<br>]<br>}<br>]<br>}`<br>``` |
| \*\*Action:_<br>• [`CreateStorageLocation`](../api/API_CreateStorageLocation.md "../api/API_CreateStorageLocation.md") |
| `"*"` | N/A | ``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:CreateStorageLocation"<br>],<br>"Effect": "Allow",<br>"Resource": "*"<br>}<br>]<br>}`<br>`` |
| **Action:\*<br>• [`DeleteApplication`](../api/API_DeleteApplication.md "../api/API_DeleteApplication.md") |
| `application` | `aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`DeleteApplication`action to delete<br>the application`My App`:<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:DeleteApplication"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:_<br>• [`DeleteApplicationVersion`](../api/API_DeleteApplicationVersion.md "../api/API_DeleteApplicationVersion.md") |
| `applicationversion` | `InApplication`<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`DeleteApplicationVersion`action to<br>delete an application version whose name is`My Version`in the<br>application`My App`:<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:DeleteApplicationVersion"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br>}<br>}<br>}<br>]<br>}`<br>``` |
| \*\*Action:_<br>• [`DeleteConfigurationTemplate`](../api/API_DeleteConfigurationTemplate.md "../api/API_DeleteConfigurationTemplate.md") |
| `configurationtemplate` | `InApplication` (Optional)<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `DeleteConfigurationTemplate` action<br>to delete a configuration template whose name is `My Template`<br>in the application `My App`. Specifying the application name as<br>a condition is optional.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:DeleteConfigurationTemplate"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:configurationtemplate/My App/My Template"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`DeleteEnvironmentConfiguration`](../api/API_DeleteEnvironmentConfiguration.md "../api/API_DeleteEnvironmentConfiguration.md") |
| `environment` | `InApplication` (Optional) | The following policy allows the `DeleteEnvironmentConfiguration`<br>action to delete a draft configuration for the environment<br>`myenv` in the application `My App`.<br>Specifying the application name as a condition is optional.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:DeleteEnvironmentConfiguration"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`DeletePlatformVersion`](../api/API_DeletePlatformVersion.md "../api/API_DeletePlatformVersion.md") |
| `platform` | `aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `DeletePlatformVersion` action to delete<br>platform versions targeting the `us-east-2` region, whose names begin with `us-east-2_`:<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:DeletePlatformVersion"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:platform/us-east-2_*"<br>]<br>}<br>]<br>}`<br>`` |
| **Action:\*<br>• [`DescribeApplications`](../api/API_DescribeApplications.md "../api/API_DescribeApplications.md") |
| `application` | `aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`DescribeApplications` action to<br>describe the application My App.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:DescribeApplications"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:_<br>• [`DescribeApplicationVersions`](../api/API_DescribeApplicationVersions.md "../api/API_DescribeApplicationVersions.md") |
| `applicationversion` | `InApplication` (Optional)<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`DescribeApplicationVersions`action<br>to describe the application version`My Version`in the<br>application`My App`. Specifying the application name as a<br>condition is optional.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:DescribeApplicationVersions"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"<br>]<br>}<br>]<br>}`<br>``` |
| \*\*Action:_<br>• [`DescribeConfigurationOptions`](../api/API_DescribeConfigurationOptions.md "../api/API_DescribeConfigurationOptions.md") |
| `environment`<br>`configurationtemplate`<br>`solutionstack` | `InApplication` (Optional)<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `DescribeConfigurationOptions` action<br>to describe the configuration options for the environment<br>`myenv` in the application `My App`.<br>Specifying the application name as a condition is optional.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": "elasticbeanstalk:DescribeConfigurationOptions",<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`DescribeConfigurationSettings`](../api/API_DescribeConfigurationSettings.md "../api/API_DescribeConfigurationSettings.md") |
| `environment`<br>`configurationtemplate` | `InApplication` (Optional)<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `DescribeConfigurationSettings`<br>action to describe the configuration settings for the environment<br>`myenv` in the application `My App`.<br>Specifying the application name as a condition is optional.<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": "elasticbeanstalk:DescribeConfigurationSettings",<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>]<br>}<br>]<br>}`<br>`` |
| **Action:\*<br>• [`DescribeEnvironmentHealth`](../api/API_DescribeEnvironmentHealth.md "../api/API_DescribeEnvironmentHealth.md") |
| `environment` | `aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows use of`DescribeEnvironmentHealth` to<br>retrieve health information for an environment named<br>`myenv`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": "elasticbeanstalk:DescribeEnvironmentHealth",<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:_<br>• [`DescribeEnvironmentResources`](../api/API_DescribeEnvironmentResources.md "../api/API_DescribeEnvironmentResources.md") |
| `environment` | `InApplication` (Optional)<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`DescribeEnvironmentResources`action<br>to return list of AWS resources for the environment`myenv`in<br>the application`My App`. Specifying the application name as a<br>condition is optional.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": "elasticbeanstalk:DescribeEnvironmentResources",<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>]<br>}<br>]<br>}`<br>``` |
| \*\*Action:_<br>• [`DescribeEnvironments`](../api/API_DescribeEnvironments.md "../api/API_DescribeEnvironments.md") |
| `environment` | `InApplication` (Optional)<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `DescribeEnvironments` action to<br>describe the environments `myenv` and<br>`myotherenv` in the application `My<br>App`. Specifying the application name as a condition is optional.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": "elasticbeanstalk:DescribeEnvironments",<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv",<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App2/myotherenv"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`DescribeEvents`](../api/API_DescribeEvents.md "../api/API_DescribeEvents.md") |
| `application`<br>`applicationversion`<br>`configurationtemplate`<br>`environment` | `InApplication`<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `DescribeEvents` action to list event<br>descriptions for the environment `myenv` and the application<br>version `My Version` in the application `My<br>App`.<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": "elasticbeanstalk:DescribeEvents",<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv",<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br>}<br>}<br>}<br>]<br>}`<br>`` |
| **Action:\*<br>• [`DescribeInstancesHealth`](../api/API_DescribeInstancesHealth.md "../api/API_DescribeInstancesHealth.md") |
| `environment` | N/A | The following policy allows use of `DescribeInstancesHealth` to<br>retrieve health information for instances in an environment named<br>`myenv`.<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": "elasticbeanstalk:DescribeInstancesHealth",<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>]<br>}<br>]<br>}`<br>`` |
| **Action:_<br>• [`DescribePlatformVersion`](../api/API_DescribePlatformVersion.md "../api/API_DescribePlatformVersion.md") |
| `platform` | `aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`DescribePlatformVersion`action to describe<br>platform versions targeting the`us-east-2`region, whose names begin with`us-east-2*`:<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:DescribePlatformVersion"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:platform/us-east-2*_"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`ListAvailableSolutionStacks`](../api/API_ListAvailableSolutionStacks.md "../api/API_ListAvailableSolutionStacks.md") |
| `solutionstack`| N/A | The following policy allows the`ListAvailableSolutionStacks`action<br>to return only the solution stack`32bit Amazon Linux running Tomcat<br>7`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:ListAvailableSolutionStacks"<br>],<br>"Effect": "Allow",<br>"Resource": "arn:aws:elasticbeanstalk:us-east-2::solutionstack/32bit Amazon Linux running Tomcat 7"<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`ListPlatformVersions`](../api/API_ListPlatformVersions.md "../api/API_ListPlatformVersions.md") |
| `platform`|`aws:RequestTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | This example allows the`CreatePlatformVersion`action to create<br>platform versions targeting the`us-east-2`region, whose names begin with`us-east-2*`:<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:ListPlatformVersions"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:platform/us-east-2*_"<br>]<br>}<br>]<br>}`<br>``` |
| \*\*Action:_<br>• [`ListTagsForResource`](../api/API_ListTagsForResource.md "../api/API_ListTagsForResource.md") |
| `application`<br>`applicationversion`<br>`configurationtemplate`<br>`environment`<br>`platform` | `aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `ListTagsForResource` action to list tags of existing resources only if they have a tag named<br>`stage` with the value `test`:<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:ListTagsForResource"<br>],<br>"Effect": "Allow",<br>"Resource": "*",<br>"Condition": {<br>"StringEquals": {<br>"aws:ResourceTag/stage": ["test"]<br>}<br>}<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`RebuildEnvironment`](../api/API_RebuildEnvironment.md "../api/API_RebuildEnvironment.md") |
| `environment` | `InApplication`<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `RebuildEnvironment` action to<br>rebuild the environment `myenv` in the application<br>`My App`.<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:RebuildEnvironment"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br>}<br>}<br>}<br>]<br>}`<br>`` |
| **Action:\*<br>• [`RequestEnvironmentInfo`](../api/API_RequestEnvironmentInfo.md "../api/API_RequestEnvironmentInfo.md") |
| `environment` | `InApplication`<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`RequestEnvironmentInfo`action to<br>compile information about the environment`myenv`in the<br>application`My App`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:RequestEnvironmentInfo"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br>}<br>}<br>}<br>]<br>}`<br>``` |
| **Action:_<br>• [`RestartAppServer`](../api/API_RestartAppServer.md "../api/API_RestartAppServer.md") |
| `environment` | `InApplication` | The following policy allows the `RestartAppServer` action to restart<br>the application container server for the environment `myenv` in<br>the application `My App`.<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:RestartAppServer"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br>}<br>}<br>}<br>]<br>}`<br>`` |
| \*\*Action:_<br>• [`RetrieveEnvironmentInfo`](../api/API_RetrieveEnvironmentInfo.md "../api/API_RetrieveEnvironmentInfo.md") |
| `environment` | `InApplication`<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `RetrieveEnvironmentInfo` action to<br>retrieve the compiled information for the environment `myenv`<br>in the application `My App`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:RetrieveEnvironmentInfo"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br>}<br>}<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`SwapEnvironmentCNAMEs`](../api/API_SwapEnvironmentCNAMEs.md "../api/API_SwapEnvironmentCNAMEs.md") |
| `environment` | `InApplication` (Optional)<br>`FromEnvironment` (Optional) | The following policy allows the `SwapEnvironmentCNAMEs` action to<br>swap the CNAMEs for the environments `mysrcenv` and<br>`mydestenv`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:SwapEnvironmentCNAMEs"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/mysrcenv",<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/mydestenv"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`TerminateEnvironment`](../api/API_TerminateEnvironment.md "../api/API_TerminateEnvironment.md") |
| `environment` | `InApplication`<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `TerminateEnvironment` action to<br>terminate the environment `myenv` in the application<br>`My App`.<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:TerminateEnvironment"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br>}<br>}<br>}<br>]<br>}`<br>`` |
| **Action:\*<br>• [UpdateApplication](../api/API_UpdateApplication.md "../api/API_UpdateApplication.md") |
| `application` | `aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`UpdateApplication`action to update<br>properties of the application`My App`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:UpdateApplication"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"<br>]<br>}<br>]<br>}`<br>``` |
| **Action:_<br>• [UpdateApplicationResourceLifecycle](../api/API_UpdateApplicationResourceLifecycle.md "../api/API_UpdateApplicationResourceLifecycle.md") |
| `application` | `aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`UpdateApplicationResourceLifecycle`action to update<br>lifecycle settings of the application`My App`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:UpdateApplicationResourceLifecycle"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"<br>]<br>}<br>]<br>}`<br>``` |
| \*\*Action:_<br>• [`UpdateApplicationVersion`](../api/API_UpdateApplicationVersion.md "../api/API_UpdateApplicationVersion.md") |
| `applicationversion` | `InApplication`<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `UpdateApplicationVersion` action to<br>update the properties of the application version `My Version`<br>in the application `My App`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:UpdateApplicationVersion"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br>}<br>}<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`UpdateConfigurationTemplate`](../api/API_UpdateConfigurationTemplate.md "../api/API_UpdateConfigurationTemplate.md") |
| `configurationtemplate` | `InApplication`<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The following policy allows the `UpdateConfigurationTemplate` action<br>to update the properties or options of the configuration template `My<br>Template` in the application `My App`.<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:UpdateConfigurationTemplate"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:configurationtemplate/My App/My Template"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br>}<br>}<br>}<br>]<br>}`<br>`` |
| **Action:\*<br>• [`UpdateEnvironment`](../api/API_UpdateEnvironment.md "../api/API_UpdateEnvironment.md") |
| `environment` | `InApplication`<br>`FromApplicationVersion`<br>`FromConfigurationTemplate`<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`UpdateEnvironment`action to update<br>the environment`myenv`in the application`My<br>App`by deploying the application version`My<br>Version`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:UpdateEnvironment"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"],<br>"elasticbeanstalk:FromApplicationVersion": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"]<br>}<br>}<br>}<br>]<br>}`<br>``` |
| **Action:_<br>• [`UpdateTagsForResource`](../api/API_UpdateTagsForResource.md "../api/API_UpdateTagsForResource.md") – `AddTags` |
| `application`<br>`applicationversion`<br>`configurationtemplate`<br>`environment`<br>`platform` | `aws:ResourceTag/`key-name`` (Optional)<br>`aws:RequestTag/`key-name`` (Optional)<br>`aws:TagKeys` (Optional) | The `AddTags` action is one of two virtual actions associated with the [`UpdateTagsForResource`](../api/API_UpdateTagsForResource.md "../api/API_UpdateTagsForResource.md") API.<br>The following policy allows the `AddTags` action to modify tags of existing resources only if they have a tag named<br>`stage` with the value `test`:<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:AddTags"<br>],<br>"Effect": "Allow",<br>"Resource": "_",<br>"Condition": {<br>"StringEquals": {<br>"aws:ResourceTag/stage": ["test"]<br>}<br>}<br>}<br>]<br>}`<br>``` |
| **Action:*<br>• [`UpdateTagsForResource`](../api/API_UpdateTagsForResource.md "../api/API_UpdateTagsForResource.md") – `RemoveTags`|
|`application`<br>`applicationversion`<br>`configurationtemplate`<br>`environment`<br>`platform`|`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The`RemoveTags` action is one of two virtual actions associated with the [`UpdateTagsForResource`](../api/API_UpdateTagsForResource.md "../api/API_UpdateTagsForResource.md") API.<br>The following policy denies the `RemoveTags`action to request the removal of a tag named`stage` from existing<br>resources:<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:RemoveTags"<br>],<br>"Effect": "Deny",<br>"Resource": "_",<br>"Condition": {<br>"ForAnyValue:StringEquals": {<br>"aws:TagKeys": ["stage"]<br>}<br>}<br>}<br>]<br>}`<br>``` |
| \*\*Action:_<br>• [`ValidateConfigurationSettings`](../api/API_ValidateConfigurationSettings.md "../api/API_ValidateConfigurationSettings.md") |
| `template`<br>`environment` | `InApplication`<br>`aws:ResourceTag/`key-name`` (Optional)<br>`aws:TagKeys`(Optional) | The following policy allows the`ValidateConfigurationSettings`<br>action to validates configuration settings against the environment<br>`myenv`in the application`My<br>App`.<br>```<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Action": [<br>"elasticbeanstalk:ValidateConfigurationSettings"<br>],<br>"Effect": "Allow",<br>"Resource": [<br>"arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br>],<br>"Condition": {<br>"StringEquals": {<br>"elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br>}<br>}<br>}<br>]<br>}`<br>``` |

## Condition keys for Elastic Beanstalk actions

Keys enable you to specify conditions that express dependencies, restrict permissions, or
specify constraints on the input parameters for an action. Elastic Beanstalk supports the following
keys.

`InApplication`

Specifies the application that contains the resource that the action operates
on.

The following example allows the `UpdateApplicationVersion` action to
update the properties of the application version `My Version`. The
`InApplication` condition specifies `My App` as the
container for `My Version`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticbeanstalk:UpdateApplicationVersion"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"
 ],
 "Condition": {
 "StringEquals": {
 "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]
 }
 }
 }
 ]
}`

```

`FromApplicationVersion`

Specifies an application version as a dependency or a constraint on an input
parameter.

The following example allows the `UpdateEnvironment` action to update the
environment `myenv` in the application `My
 App`. The `FromApplicationVersion` condition constrains the
`VersionLabel` parameter to allow only the application version
`My Version` to update the environment.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticbeanstalk:UpdateEnvironment"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"
 ],
 "Condition": {
 "StringEquals": {
 "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"],
 "elasticbeanstalk:FromApplicationVersion": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"]
 }
 }
 }
 ]
}`

```

`FromConfigurationTemplate`

Specifies a configuration template as a dependency or a constraint on an input
parameter.

The following example allows the `UpdateEnvironment` action to update the
environment `myenv` in the application `My
 App`. The `FromConfigurationTemplate` condition constrains the
`TemplateName` parameter to allow only the configuration template
`My Template` to update the environment.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticbeanstalk:UpdateEnvironment"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"
 ],
 "Condition": {
 "StringEquals": {
 "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"],
 "elasticbeanstalk:FromConfigurationTemplate": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:configurationtemplate/My App/My Template"]
 }
 }
 }
 ]
}`

```

`FromEnvironment`

Specifies an environment as a dependency or a constraint on an input
parameter.

The following example allows the `SwapEnvironmentCNAMEs` action to swap
the CNAMEs in `My App` for all environments whose names begin with
`mysrcenv` and `mydestenv` but not those
environments whose names begin with `mysrcenvPROD*` and
`mydestenvPROD*`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticbeanstalk:SwapEnvironmentCNAMEs"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/mysrcenv*",
 "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/mydestenv*"
 ],
 "Condition": {
 "ArnNotLike": {
 "elasticbeanstalk:FromEnvironment": [
 "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/mysrcenvPROD*",
 "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/mydestenvPROD*"
 ]
 }
 }
 }
 ]
}`

```

`FromSolutionStack`

Specifies a solution stack as a dependency or a constraint on an input
parameter.

The following policy allows the `CreateConfigurationTemplate` action to
create configuration templates whose name begins with `My Template`
(`My Template*`) in the application `My App`. The
`FromSolutionStack` condition constrains the `solutionstack`
parameter to allow only the solution stack `32bit Amazon Linux running Tomcat
 7` as the input value for that parameter.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "elasticbeanstalk:CreateConfigurationTemplate"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticbeanstalk:us-east-2:123456789012:configurationtemplate/My App/My Template*"
 ],
 "Condition": {
 "StringEquals": {
 "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"],
 "elasticbeanstalk:FromSolutionStack": ["arn:aws:elasticbeanstalk:us-east-2::solutionstack/32bit Amazon Linux running Tomcat 7"]
 }
 }
 }
 ]
}`

```

`aws:ResourceTag/`key-name``
`aws:RequestTag/`key-name``
`aws:TagKeys`

Specify tag-based conditions. For details, see [Using tags to control access to Elastic Beanstalk resources](AWSHowTo.iam.policies.md "AWSHowTo.iam.policies.md").

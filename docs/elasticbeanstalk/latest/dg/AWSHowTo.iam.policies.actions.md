

# Resources and conditions for Elastic Beanstalk actions
<a name="AWSHowTo.iam.policies.actions"></a>

This section describes the resources and conditions that you can use in policy statements to grant permissions that allow specific Elastic Beanstalk actions to be performed on specific Elastic Beanstalk resources.

Conditions enable you to specify permissions to resources that the action needs to complete. For example, when you can call the `CreateEnvironment` action, you must also specify the application version to deploy as well as the application that contains that application name. When you set permissions for the `CreateEnvironment` action, you specify the application and application version that you want the action to act upon by using the `InApplication` and `FromApplicationVersion` conditions. 

In addition, you can specify the environment configuration with a solution stack (`FromSolutionStack`) or a configuration template (`FromConfigurationTemplate`). The following policy statement allows the `CreateEnvironment` action to create an environment with the name **myenv** (specified by `Resource`) in the application **My App** (specified by the `InApplication` condition) using the application version **My Version** (`FromApplicationVersion`) with a **32bit Amazon Linux running Tomcat 7** configuration (`FromSolutionStack`):

------
#### [ JSON ]

****  

```
{
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
}
```

------

**Note**  
Most condition keys mentioned in this topic are specific to Elastic Beanstalk, and their names contain the `elasticbeanstalk:` prefix. For brevity, we omit this prefix from the condition key names when we mention them in the following sections. For example, we mention `InApplication` instead of its full name `elasticbeanstalk:InApplication`.  
In contrast, we mention a few condition keys used across AWS services, and we include their `aws:` prefix to highlight the exception.  
Policy examples always show full condition key names, including the prefix.

**Topics**
+ [Policy information for Elastic Beanstalk actions](#AWSHowTo.iam.policies.actions.table)
+ [Condition keys for Elastic Beanstalk actions](#AWSHowTo.iam.policies.conditions)

## Policy information for Elastic Beanstalk actions
<a name="AWSHowTo.iam.policies.actions.table"></a>

The following table lists all Elastic Beanstalk actions, the resource that each action acts upon, and the additional contextual information that can be provided using conditions.


**Policy information for Elastic Beanstalk actions, including resources, conditions, examples, and dependencies**  

<table>
<thead>
  <tr><th>Resource</th><th>Conditions</th><th>Example statement</th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_AbortEnvironmentUpdate.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_AbortEnvironmentUpdate.html</a></td></tr>
  <tr><td><code>application</code><br /><code>environment</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows a user to abort environment update operations on environments in an application named <code>My App</code>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:AbortEnvironmentUpdate"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CheckDNSAvailability.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CheckDNSAvailability.html</a></td></tr>
  <tr><td><code>"*"</code></td><td>N/A</td><td> <b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:CheckDNSAvailability"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": "*"<br />    }<br />  ]<br />}<br /></pre>  </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ComposeEnvironments.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ComposeEnvironments.html</a></td></tr>
  <tr><td><code>application</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows a user to compose environments that belong to an application named <code>My App</code>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:ComposeEnvironments"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/*"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplication.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplication.html</a></td></tr>
  <tr><td><code>application</code></td><td><code>aws:RequestTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>This example allows the <code>CreateApplication</code> action to create applications whose names begin with <b>DivA</b>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:CreateApplication"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:application/DivA*"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplicationVersion.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplicationVersion.html</a></td></tr>
  <tr><td><code>applicationversion</code></td><td><code>InApplication</code><br /><code>aws:RequestTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>This example allows the <code>CreateApplicationVersion</code> action to create application versions with any name (<b>*</b>) in the application <b>My App</b>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:CreateApplicationVersion"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/*"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateConfigurationTemplate.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateConfigurationTemplate.html</a></td></tr>
  <tr><td><code>configurationtemplate</code></td><td><code>InApplication</code><br /><code>FromApplication</code><br /><code>FromApplicationVersion</code><br /><code>FromConfigurationTemplate</code><br /><code>FromEnvironment</code><br /><code>FromSolutionStack</code><br /><code>aws:RequestTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>CreateConfigurationTemplate</code> action to create configuration templates whose name begins with <b>My Template</b> (<code>My Template*</code>) in the application <b>My App</b>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:CreateConfigurationTemplate"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:configurationtemplate/My App/My Template*"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"],<br />          "elasticbeanstalk:FromSolutionStack": ["arn:aws:elasticbeanstalk:us-east-2::solutionstack/32bit Amazon Linux running Tomcat 7"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateEnvironment.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateEnvironment.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>InApplication</code><br /><code>FromApplicationVersion</code><br /><code>FromConfigurationTemplate</code><br /><code>FromSolutionStack</code><br /><code>aws:RequestTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>CreateEnvironment</code> action to create an environment whose name is <b>myenv</b> in the application <b>My App</b> and using the solution stack <b>32bit Amazon Linux running Tomcat 7</b>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:CreateEnvironment"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"],<br />          "elasticbeanstalk:FromApplicationVersion": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"],<br />          "elasticbeanstalk:FromSolutionStack": ["arn:aws:elasticbeanstalk:us-east-2::solutionstack/32bit Amazon Linux running Tomcat 7"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreatePlatformVersion.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreatePlatformVersion.html</a></td></tr>
  <tr><td><code>platform</code></td><td><code>aws:RequestTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>This example allows the <code>CreatePlatformVersion</code> action to create platform versions targeting the <code>us-east-2</code> region, whose names begin with <b>us-east-2_</b>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:CreatePlatformVersion"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:platform/us-east-2_*"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateStorageLocation.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateStorageLocation.html</a></td></tr>
  <tr><td><code>"*"</code></td><td>N/A</td><td> <b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:CreateStorageLocation"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": "*"<br />    }<br />  ]<br />}<br /></pre>  </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteApplication.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteApplication.html</a></td></tr>
  <tr><td><code>application</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DeleteApplication</code> action to delete the application <b>My App</b>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:DeleteApplication"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteApplicationVersion.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteApplicationVersion.html</a></td></tr>
  <tr><td><code>applicationversion</code></td><td><code>InApplication</code><br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DeleteApplicationVersion</code> action to delete an application version whose name is <b>My Version</b> in the application <b>My App</b>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:DeleteApplicationVersion"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br />        }<br />      }        <br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteConfigurationTemplate.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteConfigurationTemplate.html</a></td></tr>
  <tr><td><code>configurationtemplate</code></td><td><code>InApplication</code> (Optional)<br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DeleteConfigurationTemplate</code> action to delete a configuration template whose name is <b>My Template</b> in the application <b>My App</b>. Specifying the application name as a condition is optional.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:DeleteConfigurationTemplate"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:configurationtemplate/My App/My Template"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteEnvironmentConfiguration.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteEnvironmentConfiguration.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>InApplication</code> (Optional)</td><td>The following policy allows the <code>DeleteEnvironmentConfiguration</code> action to delete a draft configuration for the environment <b>myenv</b> in the application <b>My App</b>. Specifying the application name as a condition is optional.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:DeleteEnvironmentConfiguration"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeletePlatformVersion.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeletePlatformVersion.html</a></td></tr>
  <tr><td><code>platform</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DeletePlatformVersion</code> action to delete platform versions targeting the <code>us-east-2</code> region, whose names begin with <b>us-east-2_</b>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:DeletePlatformVersion"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:platform/us-east-2_*"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplications.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplications.html</a></td></tr>
  <tr><td><code>application</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DescribeApplications</code> action to describe the application My App.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:DescribeApplications"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplicationVersions.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplicationVersions.html</a></td></tr>
  <tr><td><code>applicationversion</code></td><td><code>InApplication</code> (Optional)<br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DescribeApplicationVersions</code> action to describe the application version <b>My Version</b> in the application <b>My App</b>. Specifying the application name as a condition is optional.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:DescribeApplicationVersions"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationOptions.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationOptions.html</a></td></tr>
  <tr><td><code>environment</code><br /><code>configurationtemplate</code><br /><code>solutionstack</code></td><td><code>InApplication</code> (Optional)<br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DescribeConfigurationOptions</code> action to describe the configuration options for the environment <b>myenv</b> in the application <b>My App</b>. Specifying the application name as a condition is optional.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": "elasticbeanstalk:DescribeConfigurationOptions",<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationSettings.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationSettings.html</a></td></tr>
  <tr><td><code>environment</code><br /><code>configurationtemplate</code></td><td><code>InApplication</code> (Optional)<br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DescribeConfigurationSettings</code> action to describe the configuration settings for the environment <b>myenv</b> in the application <b>My App</b>. Specifying the application name as a condition is optional.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": "elasticbeanstalk:DescribeConfigurationSettings",<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentHealth.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentHealth.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows use of <code>DescribeEnvironmentHealth</code> to retrieve health information for an environment named <b>myenv</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": "elasticbeanstalk:DescribeEnvironmentHealth",<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentResources.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentResources.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>InApplication</code> (Optional)<br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DescribeEnvironmentResources</code> action to return list of AWS resources for the environment <b>myenv</b> in the application <b>My App</b>. Specifying the application name as a condition is optional.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": "elasticbeanstalk:DescribeEnvironmentResources",<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>InApplication</code> (Optional)<br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DescribeEnvironments</code> action to describe the environments <b>myenv</b> and <b>myotherenv</b> in the application <b>My App</b>. Specifying the application name as a condition is optional.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": "elasticbeanstalk:DescribeEnvironments",<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv",<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App2/myotherenv"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEvents.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEvents.html</a></td></tr>
  <tr><td><code>application</code><br /><code>applicationversion</code><br /><code>configurationtemplate</code><br /><code>environment</code></td><td><code>InApplication</code><br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DescribeEvents</code> action to list event descriptions for the environment <b>myenv</b> and the application version <b>My Version</b> in the application <b>My App</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": "elasticbeanstalk:DescribeEvents",<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv",<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeInstancesHealth.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeInstancesHealth.html</a></td></tr>
  <tr><td><code>environment</code></td><td>N/A</td><td>The following policy allows use of <code>DescribeInstancesHealth</code> to retrieve health information for instances in an environment named <b>myenv</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": "elasticbeanstalk:DescribeInstancesHealth",<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribePlatformVersion.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribePlatformVersion.html</a></td></tr>
  <tr><td><code>platform</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>DescribePlatformVersion</code> action to describe platform versions targeting the <code>us-east-2</code> region, whose names begin with <b>us-east-2_</b>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:DescribePlatformVersion"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:platform/us-east-2_*"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html</a></td></tr>
  <tr><td><code>solutionstack</code></td><td>N/A</td><td>The following policy allows the <code>ListAvailableSolutionStacks</code> action to return only the solution stack <b>32bit Amazon Linux running Tomcat 7</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:ListAvailableSolutionStacks"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": "arn:aws:elasticbeanstalk:us-east-2::solutionstack/32bit Amazon Linux running Tomcat 7"<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformVersions.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformVersions.html</a></td></tr>
  <tr><td><code>platform</code></td><td><code>aws:RequestTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>This example allows the <code>CreatePlatformVersion</code> action to create platform versions targeting the <code>us-east-2</code> region, whose names begin with <b>us-east-2_</b>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:ListPlatformVersions"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:platform/us-east-2_*"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListTagsForResource.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListTagsForResource.html</a></td></tr>
  <tr><td><code>application</code><br /><code>applicationversion</code><br /><code>configurationtemplate</code><br /><code>environment</code><br /><code>platform</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>ListTagsForResource</code> action to list tags of existing resources only if they have a tag named <code>stage</code> with the value <code>test</code>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:ListTagsForResource"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": "*",<br />      "Condition": {<br />        "StringEquals": {<br />          "aws:ResourceTag/stage": ["test"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RebuildEnvironment.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RebuildEnvironment.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>InApplication</code><br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>RebuildEnvironment</code> action to rebuild the environment <b>myenv</b> in the application <b>My App</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:RebuildEnvironment"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RequestEnvironmentInfo.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RequestEnvironmentInfo.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>InApplication</code><br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>RequestEnvironmentInfo</code> action to compile information about the environment <b>myenv</b> in the application <b>My App</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:RequestEnvironmentInfo"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RestartAppServer.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RestartAppServer.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>InApplication</code></td><td>The following policy allows the <code>RestartAppServer</code> action to restart the application container server for the environment <b>myenv</b> in the application <b>My App</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:RestartAppServer"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RetrieveEnvironmentInfo.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RetrieveEnvironmentInfo.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>InApplication</code><br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>RetrieveEnvironmentInfo</code> action to retrieve the compiled information for the environment <b>myenv</b> in the application <b>My App</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:RetrieveEnvironmentInfo"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SwapEnvironmentCNAMEs.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SwapEnvironmentCNAMEs.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>InApplication</code> (Optional)<br /><code>FromEnvironment</code> (Optional)</td><td>The following policy allows the <code>SwapEnvironmentCNAMEs</code> action to swap the CNAMEs for the environments <b>mysrcenv</b> and <b>mydestenv</b>. <b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:SwapEnvironmentCNAMEs"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/mysrcenv",<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/mydestenv"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_TerminateEnvironment.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_TerminateEnvironment.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>InApplication</code><br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>TerminateEnvironment</code> action to terminate the environment <b>myenv</b> in the application <b>My App</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:TerminateEnvironment"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplication.html">UpdateApplication</a></td></tr>
  <tr><td><code>application</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>UpdateApplication</code> action to update properties of the application <b>My App</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:UpdateApplication"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplicationResourceLifecycle.html">UpdateApplicationResourceLifecycle</a></td></tr>
  <tr><td><code>application</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>UpdateApplicationResourceLifecycle</code> action to update lifecycle settings of the application <b>My App</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:UpdateApplicationResourceLifecycle"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"<br />      ]<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplicationVersion.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplicationVersion.html</a></td></tr>
  <tr><td><code>applicationversion</code></td><td><code>InApplication</code><br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>UpdateApplicationVersion</code> action to update the properties of the application version <b>My Version</b> in the application <b>My App</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:UpdateApplicationVersion"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateConfigurationTemplate.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateConfigurationTemplate.html</a></td></tr>
  <tr><td><code>configurationtemplate</code></td><td><code>InApplication</code><br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>UpdateConfigurationTemplate</code> action to update the properties or options of the configuration template <b>My Template</b> in the application <b>My App</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:UpdateConfigurationTemplate"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:configurationtemplate/My App/My Template"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateEnvironment.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateEnvironment.html</a></td></tr>
  <tr><td><code>environment</code></td><td><code>InApplication</code><br /><code>FromApplicationVersion</code><br /><code>FromConfigurationTemplate</code><br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>UpdateEnvironment</code> action to update the environment <b>myenv</b> in the application <b>My App</b> by deploying the application version <b>My Version</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:UpdateEnvironment"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"],<br />          "elasticbeanstalk:FromApplicationVersion": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:applicationversion/My App/My Version"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html</a> – <code>AddTags</code></td></tr>
  <tr><td><code>application</code><br /><code>applicationversion</code><br /><code>configurationtemplate</code><br /><code>environment</code><br /><code>platform</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:RequestTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The <code>AddTags</code> action is one of two virtual actions associated with the <a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html</a> API.<br />The following policy allows the <code>AddTags</code> action to modify tags of existing resources only if they have a tag named <code>stage</code> with the value <code>test</code>:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:AddTags"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": "*",<br />      "Condition": {<br />        "StringEquals": {<br />          "aws:ResourceTag/stage": ["test"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html</a> – <code>RemoveTags</code></td></tr>
  <tr><td><code>application</code><br /><code>applicationversion</code><br /><code>configurationtemplate</code><br /><code>environment</code><br /><code>platform</code></td><td><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The <code>RemoveTags</code> action is one of two virtual actions associated with the <a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html</a> API.<br />The following policy denies the <code>RemoveTags</code> action to request the removal of a tag named <code>stage</code> from existing resources:<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:RemoveTags"<br />      ],<br />      "Effect": "Deny",<br />      "Resource": "*",<br />      "Condition": {<br />        "ForAnyValue:StringEquals": {<br />          "aws:TagKeys": ["stage"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
  <tr><td colspan="3"><b>Action: </b><a href="http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ValidateConfigurationSettings.html">http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ValidateConfigurationSettings.html</a></td></tr>
  <tr><td><code>template</code><br /><code>environment</code></td><td><code>InApplication</code><br /><code>aws:ResourceTag/key-name</code> (Optional)<br /><code>aws:TagKeys</code> (Optional)</td><td>The following policy allows the <code>ValidateConfigurationSettings</code> action to validates configuration settings against the environment <b>myenv</b> in the application <b>My App</b>.<b></b><br /> <pre>{<br />  "Version":"2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Action": [<br />        "elasticbeanstalk:ValidateConfigurationSettings"<br />      ],<br />      "Effect": "Allow",<br />      "Resource": [<br />        "arn:aws:elasticbeanstalk:us-east-2:123456789012:environment/My App/myenv"<br />      ],<br />      "Condition": {<br />        "StringEquals": {<br />          "elasticbeanstalk:InApplication": ["arn:aws:elasticbeanstalk:us-east-2:123456789012:application/My App"]<br />        }<br />      }<br />    }<br />  ]<br />}<br /></pre> </td></tr>
</tbody>
</table>


## Condition keys for Elastic Beanstalk actions
<a name="AWSHowTo.iam.policies.conditions"></a>

Keys enable you to specify conditions that express dependencies, restrict permissions, or specify constraints on the input parameters for an action. Elastic Beanstalk supports the following keys.

`InApplication`  
Specifies the application that contains the resource that the action operates on.  
The following example allows the `UpdateApplicationVersion` action to update the properties of the application version **My Version**. The `InApplication` condition specifies **My App** as the container for **My Version**.    
****  

```
{
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
}
```

`FromApplicationVersion`  
Specifies an application version as a dependency or a constraint on an input parameter.  
The following example allows the `UpdateEnvironment` action to update the environment **myenv** in the application **My App**. The `FromApplicationVersion` condition constrains the `VersionLabel` parameter to allow only the application version **My Version** to update the environment.    
****  

```
{
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
}
```

`FromConfigurationTemplate`  
Specifies a configuration template as a dependency or a constraint on an input parameter.  
The following example allows the `UpdateEnvironment` action to update the environment **myenv** in the application **My App**. The `FromConfigurationTemplate` condition constrains the `TemplateName` parameter to allow only the configuration template **My Template** to update the environment.    
****  

```
{
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
}
```

`FromEnvironment`  
Specifies an environment as a dependency or a constraint on an input parameter.  
The following example allows the `SwapEnvironmentCNAMEs` action to swap the CNAMEs in **My App** for all environments whose names begin with **mysrcenv** and **mydestenv** but not those environments whose names begin with **mysrcenvPROD\*** and **mydestenvPROD\***.     
****  

```
{
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
}
```

`FromSolutionStack`  
Specifies a solution stack as a dependency or a constraint on an input parameter.  
The following policy allows the `CreateConfigurationTemplate` action to create configuration templates whose name begins with **My Template** (`My Template*`) in the application **My App**. The `FromSolutionStack` condition constrains the `solutionstack` parameter to allow only the solution stack **32bit Amazon Linux running Tomcat 7** as the input value for that parameter.    
****  

```
{
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
}
```

`aws:ResourceTag/{{key-name}}``aws:RequestTag/{{key-name}}``aws:TagKeys`  
Specify tag-based conditions. For details, see [Using tags to control access to Elastic Beanstalk resources](AWSHowTo.iam.policies.access-tags.md).
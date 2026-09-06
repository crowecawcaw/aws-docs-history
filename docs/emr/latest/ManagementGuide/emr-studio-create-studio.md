

# Create an EMR Studio
<a name="emr-studio-create-studio"></a>

You can create an EMR Studio for your team with the Amazon EMR console or the AWS CLI. Creating a Studio instance is part of setting up Amazon EMR Studio.

**Prerequisites**

Before you create a Studio, make sure you've completed the previous tasks in [Set up an EMR Studio](emr-studio-set-up.md).

To create a Studio using the AWS CLI, you should have the latest version installed. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**Important**  
Deactivate proxy management tools such as FoxyProxy or SwitchyOmega in the browser before you create a Studio. Active proxies can result in a **Network Failure ** error message when you choose **Create Studio**.

 Amazon EMR provides you with a simple console experience to create a Studio, so you can quickly get started with the default settings. to run interactive workloads or batch jobs with the default settings. Creating a EMR Studio also creates an EMR Serverless application ready for your interactive jobs.

If you want full control over your Studio's settings, you can choose **Custom**, which lets you configure all of the additional settings. 

------
#### [ Interactive workloads ]

**To create a EMR Studio for interactive workloads**

1. Open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr).

1. Under **EMR Studio** on the left navigation, choose **Getting started**. You can also create a new Studio from the **Studios** page.

1. Amazon EMR provides default settings for you if you're creating a EMR Studio for interactive workloads, but you can edit these settings. Configurable settings include the EMR Studio's name, the S3 location for your Workspace, the service role to use, the Workspace(s) you want to use, EMR Serverless application name, and the associated runtime role.

1. Choose **Create Studio and launch Workspace** to finish and navigate to the **Studios** page. Your new Studio appears in the list with details such as **Studio name**, **Creation date**, and **Studio access URL**. Your Workspace opens in a new tab in your browser.

------
#### [ Batch jobs ]

**To create a EMR Studio for interactive workloads**

1. Open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr).

1. Under **EMR Studio** on the left navigation, choose **Getting started**. You can also create a new Studio from the **Studios** page.

1. Amazon EMR provides default settings for you if you're creating a EMR Studio for batch jobs, but you can edit these settings. Configurable settings include the EMR Studio's name, EMR Serverless application name, and the associated runtime role.

1. Choose **Create Studio and launch Workspace** to finish and navigate to the **Studios** page. Your new Studio appears in the list with details such as **Studio name**, **Creation date**, and **Studio access URL**. Your EMR Studio opens in a new tab in your browser.

------
#### [ Custom settings ]

**To create a EMR Studio with custom settings**

1. Open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr).

1. Under **EMR Studio** on the left navigation, choose **Getting started**. You can also create a new Studio from the **Studios** page.

1. Choose **Create a Studio** to open the **Create a Studio** page.

1. Enter a **Studio name**.

1. Choose to create a new S3 bucket or use an existing location.

1. Choose the Workspace to add to the Studio. You can add up to 3 Workspaces.

1. Under **Authentication**, choose an authentication mode for the Studio and provide information according to the following table. To learn more about authentication for EMR Studio, see [Choose an authentication mode for Amazon EMR Studio](emr-studio-authentication.md).    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-studio.html)

1. For VPC, choose an Amazon Virtual Private Cloud (**VPC**) for the Studio from the dropdown list.

1. Under **Subnets**, select a maximum of five subnets in your VPC to associate with the Studio. You have the option to add more subnets after you create the Studio.

1. For **Security groups**, choose either the default security groups or custom security groups. For more information, see [Define security groups to control EMR Studio network traffic](emr-studio-security-groups.md).    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-studio.html)

1. Add tags to your Studio and other resources. For more information about tags, see [Tag clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html).

1. Choose **Create Studio and launch Workspace** to finish and navigate to the **Studios** page. Your new Studio appears in the list with details such as **Studio name**, **Creation date**, and **Studio access URL**.

After you create a Studio, follow the instructions in [Assign a user or group to an EMR Studio](emr-studio-manage-users.md#emr-studio-assign-users-groups).

------
#### [ CLI ]

**Note**  
Linux line continuation characters (\\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

**Example – Create an EMR Studio that uses IAM for authentication**  
The following example AWS CLI command creates an EMR Studio with IAM authentication mode. When you use IAM authentication or federation for the Studio, you don't specify a `--user-role`.   
To let federated users log in using the Studio URL and credentials for your identity provider (IdP), specify your `--idp-auth-url` and `--idp-relay-state-parameter-name`. For a list of IdP authentication URLs and RelayState names, see [Identity provider RelayState parameters and authentication URLs](#emr-studio-idp-reference-table).  

```
aws emr create-studio \
--name {{<example-studio-name>}} \
--auth-mode IAM \
--vpc-id {{<example-vpc-id>}} \
--subnet-ids {{<subnet-id-1> <subnet-id-2>... <subnet-id-5> }} \
--service-role {{<example-studio-service-role-name>}} \
--user-role {{studio-user-role-name}} \
--workspace-security-group-id {{<example-workspace-sg-id>}} \
--engine-security-group-id {{<example-engine-sg-id>}} \
--default-s3-location {{<example-s3-location>}} \
--idp-auth-url {{<https://EXAMPLE/login/>}} \
--idp-relay-state-parameter-name {{<example-RelayState>}}
```

**Example – Create an EMR Studio that uses Identity Center for authentication**  
The following AWS CLI example command creates an EMR Studio that uses IAM Identity Center authentication mode. When you use IAM Identity Center authentication, you must specify a `--user-role`.   
For more information about IAM Identity Center authentication mode, see [Set up IAM Identity Center authentication mode for Amazon EMR Studio](emr-studio-authentication.md#emr-studio-enable-sso).  

```
aws emr create-studio \
--name {{<example-studio-name>}} \
--auth-mode SSO \
--vpc-id {{<example-vpc-id>}} \
--subnet-ids {{<subnet-id-1> <subnet-id-2>... <subnet-id-5> }} \
--service-role {{<example-studio-service-role-name>}} \
--user-role {{<example-studio-user-role-name>}} \
--workspace-security-group-id {{<example-workspace-sg-id>}} \
--engine-security-group-id {{<example-engine-sg-id>}} \
--default-s3-location {{<example-s3-location>}}
--trusted-identity-propagation-enabled \
--idc-user-assignment OPTIONAL \
--idc-instance-arn {{<iam-identity-center-instance-arn>}}
```

**Example – CLI output for `aws emr create-studio`**  
The following is an example of the output that appears after you create a Studio.  

```
{
    StudioId: "es-123XXXXXXXXX",
    Url: "https://es-123XXXXXXXXX.emrstudio-prod.us-east-1.amazonaws.com"
}
```

For more information about the `create-studio` command, see [*AWS CLI Command Reference*](https://docs.aws.amazon.com/cli/latest/reference/emr/create-studio.html).

------

## Identity provider RelayState parameters and authentication URLs
<a name="emr-studio-idp-reference-table"></a>

When you use IAM federation, and you want users to log in using your Studio URL and credentials for your identity provider (IdP), you can specify your **Identity provider (IdP) login URL** and **RelayState** parameter name when you [Create an EMR Studio](#emr-studio-create-studio).

The following table shows the standard authentication URL and RelayState parameter name for some popular identity providers.


| Identity provider | Parameter | Authentication URL | 
| --- | --- | --- | 
| Auth0 | RelayState | https://{{<sub\_domain>}}.auth0.com/samlp/{{<app\_id>}} | 
| Google accounts | RelayState | https://accounts.google.com/o/saml2/initsso?idpid={{<idp\_id>}}&spid={{<sp\_id>}}&forceauthn=false | 
| Microsoft Azure | RelayState | https://myapps.microsoft.com/signin/{{<app\_name>}}/{{<app\_id>}}?tenantId={{<tenant\_id>}} | 
| Okta | RelayState | https://{{<sub\_domain>}}.okta.com/app/{{<app\_name>}}/{{<app\_id>}}/sso/saml | 
| PingFederate | TargetResource | https://{{<host>}}/idp/{{<idp\_id>}}/startSSO.ping?PartnerSpId={{<sp\_id>}} | 
| PingOne | TargetResource | https://sso.connect.pingidentity.com/sso/sp/initsso?saasid={{<app\_id>}}&idpid={{<idp\_id>}} | 
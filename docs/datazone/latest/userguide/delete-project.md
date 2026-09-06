

# Delete project
<a name="delete-project"></a>

In Amazon DataZone, projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and/or consuming data assets in the Amazon DataZone catalog. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md). 

The act of deleting a project is final. Deletion irrevocably deletes the project’s contents, including data sources, environments, assets, glossaries, and metadata forms. Amazon DataZone revokes grants Amazon DataZone has placed on managed assets via Lake Formation and Amazon Redshift. Deleting a project does not delete non-Amazon DataZone AWS resources that Amazon DataZone may have helped you create. If you no longer need these AWS resources, delete them in their respective AWS service and account.

To delete an Amazon DataZone project, you must be an owner of the project.

To delete an existing project, complete the following steps. 

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on (SSO) or your AWS credentials. An IAM principal can navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and sign in with the AWS account where the domain was created, then choose **Open data portal**.

1. Choose **Browse projects** from the top navigation pane.

1. Choose the project that you want to delete. If you don't see it in the list of projects, you can search for it by specifying the project name in the **Find project** field. 

1. Expand **Actions** and choose **Delete project**.

   Review the informational warnings about the potential impact of deleting the project.

1. If you accept the warnings, then type in the confirmation text, and choose **Delete**.

**Important**  
Deleting a project is an irrevocable action that cannot be undone by you or by AWS.

**Note**  
When you or your domain users create an environment in a project, Amazon DataZone creates AWS resources in your domain or associated accounts to provide you and your domain users with functionality. Below is the list of AWS resources that Amazon DataZone may create for a project, along with the default name. Deleting a project does not delete any of these AWS resources in your AWS accounts.  
IAM roles: datazone\_usr\_<environmentId>.
Glue databases: (1) <environmentName>\_pub\_db-\*, (2) <environmentName>\_sub\_db-\*. If there was already an existing database of this name, Amazon DataZone will add the environment ID.
Athena workgroups: <environmentName>-\*. If there was already an existing workgroup of this name, Amazon DataZone will add the environment ID.
CloudWatch log group: datazone\_<environmentId>
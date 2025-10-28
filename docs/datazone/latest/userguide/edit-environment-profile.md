# Edit an environment profile

In Amazon DataZone, an environment proﬁle is a template that you can use to create
environments. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md"). To edit an existing environment profiles in an
Amazon DataZone domain, you must belong to an Amazon DataZone project.

###### To edit an environment profile

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Within the data portal, choose **Browse projects** and select
   the project in which you want to edit the environment profile.
3. Navigate to the **Environments** tab within the project, then
   choose **Environment profiles**, and then choose the
   environment profile that you want to edit.

If you are editing a Data Warehouse environment profile, you can only edit the
name and the description of an existing environment profile.

If you are editing a Data Lake environment profile, you can edit the name and
the description of the profile and you can also edit the projects that are
authorized to use this profile to create environments and you can edit
databases. To edit these settings, do the following:

    * In the **Authorized projects** section, specify the
     projects that can use the environment profile with the built-in Data
     Lake environment profile for creating environments. By default, all
     projects within the domain can use the data lake blueprint in the
     account to create environment profiles. To keep this default setting,
     choose **All projects**. However, you can restrict this
     by assigning projects to the blueprint. To do so, choose
     **Authorized projects** only and then specify
     projects that can use this project profile to create
     environments.
    * In the **Databases** section, either choose
     **Any database** to enable publishing from any
     database within the AWS account and region where the environment is
     created or choose Only default database to enable publishing from only
     the default publishing database that is created with the
     environment.

When you complete your edits, choose **Edit environment
profile**.

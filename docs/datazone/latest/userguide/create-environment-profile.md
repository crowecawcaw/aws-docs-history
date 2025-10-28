# Create an environment profile

In Amazon DataZone, an environment proﬁle is a template that you can use to create
environments. The purpose of an environment profile is to simplify environment creation
by embedding placement information such as AWS account and region within the profiles.
For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md"). To create environment profiles in an Amazon DataZone
domain, you must belong to an Amazon DataZone project. All environment profiles are owned by
projects and can be used by all authorized users, from any project, to create new
environments.

###### To create an environment profile

1.  Navigate to the Amazon DataZone data portal using the data portal URL and log in
    using your SSO or AWS credentials. If you’re an Amazon DataZone administrator, you
    can obtain the data portal URL by accessing the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") in the AWS account where
    the Amazon DataZone domain was created.
2.  Within the data portal, choose **Browse projects** and select
    the project in which you want to create the environment profile.
3.  Navigate to the **Environments** tab within the project, then
    choose **Create environment profile**.
4.  Configure the following fields:
    - **Name** – The name for your environment
      profile.
    - **Description** – (Optional) A description for
      your environment profile.
    - **Owner Project** - The project where the profile is
      being created is selected by default in this field.
    - **Blueprint** – The blueprint for which this
      profile is created. You can choose one of the default Amazon DataZone
      blueprints (Data Lake or Data
      Warehouse).

    If you specified the Data Warehouse blueprint, do the
    following:

        + Provide a parameter set. To select an existing parameter set
         choose the option **Choose a parameter set**.
         If you want to enter your own parameters, choose **Enter
         my own**.
        + If you choose to select an existing parameter, then do the
         following:




        	- Select an AWS account from the drop down.
        	- Select a parameter set from the dropdown.
        + If you choose to enter your own parameters, do the
         following:




        	- Provide the AWS parameters by selecting the AWS
        	 Account and Region from the dropdown.
        	- Provide Redshift Data Wareshoue parameters:




        		* Select either Amazon Redshift cluster or
        		 Amazon Redshift Serverless
        		* Enter the AWS Secret ARN that holds the
        		 credentials to the selected Amazon Redshift
        		 cluster or Amazon Redshift Serverless workgroup.
        		 The AWS secret must be tagged with the domain Id
        		 and Project Id where you are creating the
        		 environment profile.




        			+ `AmazonDataZoneDomain:
        			 [Domain_ID]`
        			+ `AmazonDataZoneProject:
        			 [Project_ID]`
        		* Enter the name of Amazon Redshift cluster or
        		 Amazon Redshift Serverless workgroup.
        		* Enter the name of the database within the
        		 selected Amazon Redshift cluster or Amazon
        		 Redshift Serverless workgroup.
        	- In the **Authorized projects**
        	 section, specify the projects that can use the
        	 environment profile for creating environments. By
        	 default, all projects within the domain can use the
        	 environment profiles in the account to create
        	 environments. To keep this default setting, choose
        	 **All projects**. However, you can
        	 restrict this by assigning authorized projects to the
        	 environment. To do so, choose **Authorized
        	 projects only** and then specify projects
        	 that can use this project profile to create
        	 environments.
        	- In the **Publishing** section, either
        	 choose one of the following options:




        		* **Publish from any schema**:
        		 If you choose this option, environments created
        		 using this environment profile can be used to
        		 publish from any schema within database selected
        		 in the Redshift parameters provided above. Users
        		 of the environment created using this environment
        		 profiles can also provide their own Amazon
        		 Redshift parameters to publish from any schema
        		 within the AWS account and region selected in
        		 the environment profile.
        		* **Publish from only default
        		 environment schema**: If you choose this
        		 option, environments created using this can be
        		 used to publish only from the default schema
        		 created by Amazon DataZone for that environment. Users
        		 of the environment created using this environment
        		 profiles cannot provide their own Amazon Redshift
        		 parameters.
        		* **Don’t allow publishing**:
        		 If you choose this option, environments created
        		 using this environment profile can only be used
        		 for subscribing and consumption of data.
        		 Environments cannot be used to publish any data at
        		 all.

    If you specified the Data Lake blueprint, do the following:

        + In the **AWS account parameters** section,
         specify the AWS account number and the AWS account region
         where the potential environments will be created.
        + In the **Authorized projects** section,
         specify the projects that can use the environment profile with
         the built-in Data Lake environment profile for creating
         environments. By default, all projects within the domain can use
         the data lake blueprint in the account to create environment
         profiles. To keep this default setting, choose **All
         projects**. However, you can restrict this by
         assigning projects to the blueprint. To do so, choose
         **Authorized projects** only and then
         specify projects that can use this project profile to create
         environments.
        + In the **Databases** section, either choose
         **Any database** to enable publishing from
         any database within the AWS account and region where the
         environment is created or choose Only default database to enable
         publishing from only the default publishing database that is
         created with the environment.

5.  Choose **Create environment profile**.

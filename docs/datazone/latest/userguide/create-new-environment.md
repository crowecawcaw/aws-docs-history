# Create a new environment

In Amazon DataZone projects, environments are collections of configured resources (for
example, an Amazon S3 bucket, an AWS Glue database, or an Amazon Athena workgroup),
with a given set of IAM principals (environment user roles) with assigned owner or
contributor permissions who can operate on those resources. For more information, see
[Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

Any Amazon DataZone user with the required permissions to access the data portal can create
an Amazon DataZone environment within a project.

To create a new environment, complete the following steps.

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Browse all projects** and select the project in
   which you want to create a new environment.
3. Choose **Create environment**, specify values for the
   following fields, and then choose **Create
   environment**:
   - **Name** – the environment name
   - **Description** – a description of the
     environment
   - **Environment proﬁle** – choose an existing
     environment profile or create a new one. An environment proﬁle is a
     template that you can use to create environments. For more information,
     see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

   Once you've selected the environment profile, under the
   **Parameters** section, specify the values for the
   fields that are part of this environment profile.

# Converting a Lake Formation resource to a hybrid resource

In cases where you're currently using Lake Formation permissions for your Data Catalog databases and
tables, you can edit the location registration properties to enable hybrid access mode. This
allows you to provide new principals access to the same resources using IAM permission
policies for Amazon S3 and AWS Glue actions without interrupting existing Lake Formation permissions.

Scenario description - The following steps assume that you’ve a data location
registered with Lake Formation, and you've set up permissions for principals on databases, tables, or
columns pointing to that location. If the location was registered with a service linked
role, you can’t update the location parameters and enable hybrid access mode.
The `IAMAllowedPrincipals` group by default has Super permissions on the database and all its tables.

###### Important

Don’t update a location registration to hybrid access mode without opting in the principals
that are accessing data in this location.

###### Enabling hybrid access mode for a data location registered with Lake Formation

1. ###### Warning

We don't recommend converting a Lake Formation managed data location to hybrid access mode to avoid
interrupting the permission policies of other existing users or workloads.

Opt in the existing principals who have Lake Formation permissions.

    1. List and review the permissions you’ve granted to principals on catalogs,
     databases and tables. For more information, see [Viewing database and table permissions in Lake Formation](viewing-permissions.md "viewing-permissions.md").
    2. Choose **Hybrid access mode** under
     **Permissions** from the left navigation bar, and choose
     **Add**.
    3. On the **Add principals and resources** page, choose the
     catalogs, databases, and tables from the Amazon S3 data location that you want to use in
     hybrid access mode. Choose the principals that already have Lake Formation permissions.
    4. Choose **Add** to opt in the principals to use Lake Formation permissions in hybrid access mode.

2. Update the Amazon S3 bucket/prefix registration by choosing **Hybrid access mode** option.

Console

    1. Sign in to the Lake Formation console as the data lake administrator.
    2. In the navigation pane, under **Register and Ingest**, choose **Data lake locations**.
    3. Select a location, and on the **Actions**menu, choose **Edit**.
    4. Choose **Hybrid access mode**.
    5. Choose **Save**.
    6. Under Data Catalog, select the database or table and grant `Super` or
     `All` permissions to the virtual group called
     `IAMAllowedPrincipals`.
    7. Verify that your existing Lake Formation users' access is not interrupted when you
     updated the location registration properties. Sign in to Athena console as a
     Lake Formation principal and run a sample query on a table that is pointing to the
     updated location.


    Similarly, verify the access of AWS Glue users who are using IAM permissions
     policies to access the database and tables.

AWS CLI
Following is an example for registering a data location with Lake Formation with
HybridAccessEnabled:true/false. Default value for the
`HybridAccessEnabled` parameter is false. Replace Amazon S3 path, role name, and AWS account id with valid values.

```
aws lakeformation update-resource --cli-input-json file://`file path`
json:
{
    "ResourceArn": "arn:aws:s3:::`<s3-path>`",
    "RoleArn": "arn:aws:iam::`<123456789012>`:role/`<test>`",
    "HybridAccessEnabled": true
}

```

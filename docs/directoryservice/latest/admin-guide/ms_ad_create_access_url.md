# Creating an access URL for AWS Managed Microsoft AD

An access URL is used with AWS applications and services, such as Amazon WorkDocs, to
reach a login page that is associated with your directory. You
can create an access URL for your directory by performing the following steps.

###### Considerations

- The URL must be unique globally.
- The access URL can only be configured from the Primary Region when using Multi-Region
  directories.
- Once you create an application access URL for this directory, it cannot be changed. After
  an access URL is created, it cannot be used by others. If you delete your directory, the
  access URL is also deleted and can then be used by any other account.

###### To create an access URL

1. In the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/") navigation pane, select
   **Directories**.
2. On the **Directories** page, choose your directory ID.
3. On the **Directory details** page, do one of the
   following:
   - If you have multiple Regions showing under **Multi-Region
     replication**, select the Primary Region and then choose the
     **Application management** tab. For more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
   - If you do not have any regions showing under **Multi-Region
     replication**, choose the **Application management**
     tab.

4. In the **Application access URL** section, if an access URL has not
   been assigned to the directory, the **Create** button is displayed. Enter a
   directory alias and choose **Create**. If an **Entity Already
   Exists** error is returned, the specified directory alias has already been
   allocated. Choose another alias and repeat this procedure.

Your access URL is displayed in the format
`<alias>`.awsapps.com. By default, this URL will take you to
the sign-in page for WorkDocs.

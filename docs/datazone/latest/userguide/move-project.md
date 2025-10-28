# Move project to a different domain unit

In Amazon DataZone, projects enable a group of users to collaborate on various business use
cases that involve publishing, discovering, subscribing to, and consuming data assets in
the Amazon DataZone catalog. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

To move an Amazon DataZone project to a different domain unit, you must meet the following
requirements:

- You must have a policy grant for Project creation in the domain unit to which
  you are moving the project.
- All members of the project must have Project membership permissions in the
  domain unit to which you are moving the project.
- You must be a Domain Unit Owner in the domain unit to which you're moving the
  project.
- You must be the owner of the project.
  To move an existing project to a different domian unit, complete the following steps.

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Browse projects**.
3. Choose the project that you want to move. If you don't readily see it in the
   list of projects, you can search for it by specifying the project name in the
   **Find project** field.
4. Expand **Actions** and choose **Move
   project**.
5. Specify the domain unit under which you want to move this project and then
   choose **Move**.

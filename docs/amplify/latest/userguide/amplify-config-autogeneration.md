# Automatic build-time generation of

Amplify config (Gen 1 apps only)

###### Note

The information in this section is for Gen 1 apps only. If you want to automatically
deploy infrastructure and application code changes from feature branches for a Gen 2
app, see [Fullstack branch deployments](https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/branch-deployments/ "https://docs.amplify.aws/nextjs/deploy-and-host/fullstack-branching/branch-deployments/") in the _Amplify docs_

Amplify supports the automatic build-time generation of the Amplify config
`aws-exports.js` file for Gen 1 apps. By turning off full stack CI/CD
deployments, you enable your app to autogenerate the `aws-exports.js` file and
ensure that updates are not made to your backend at build-time.

###### To autogenerate `aws-exports.js` at build-time

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app to edit.
3. Choose the **Hosting environments** tab.
4. Locate the branch to edit and choose **Edit**.

![The location of the Edit link for a branch in the Amplify console.](images/amplify_edit_backend_alternate.png) 5. On the **Edit target backend** page, uncheck **Enable
full-stack continuous deployments (CI/CD)** to turn off full-stack CI/CD
for this backend.

![The location of the checkbox to turn off CI/CD in the Amplify console.](images/amplify_turnoff_CICD.png) 6. Select an existing service role to give Amplify the permissions it requires to
make changes to your app backend. If you need to create a service role, choose
**Create new role**. For more information about creating a
service role, see [Adding a service role with permissions to deploy
backend resources](amplify-service-role.md "amplify-service-role.md"). 7. Choose **Save**. Amplify applies these changes the next time
you build the app.

# Create a CodeDeploy Application

The CodeDeploy application is simply a name or container used by AWS CodeDeploy to ensure that the correct revision, deployment configuration, and
deployment group are referenced during a deployment. The deployment configuration, in this case, is the WordPress bundle that you previously created.

REQUIRED DATA:

- `VpcId`: The VPC that you are using, this should be the same as the previously used VPC.
- `CodeDeployApplicationName`: Must be unique in the account. Look at the CodeDeploy Console to check for existing application names.

1. Create the CodeDeploy Application for WordPress

On the **Create RFC** page, select the category **Deployment**,
subcategory **Applications**, item **CodeDeploy application** and operation **Create** from the RFC CT
pick list. Choose **Basic** and set the values as shown. Click **Submit** when finished.

```
**Subject**:                      CD-WP-App-RFC
**CodeDeployApplicationName**:    `WordPress`
**VpcId**:                        `VPC_ID`
**Name**:                         WP-CD-App
```

2. Click **Submit** when finished.

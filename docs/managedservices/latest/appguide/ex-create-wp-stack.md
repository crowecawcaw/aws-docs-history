# CLI Tutorial: Deploying a Tier and Tie WordPress Website

This section describes how to deploy a high availability (HA) WordPress site into an AMS environment using the AMS CLI.
This set of instructions includes an example of creating the necessary WordPress CodeDeploy-compatible package (e.g. zip) file.

###### Note

This deployment walkthrough is designed for use with an AMZN Linux environment.

The essential variable parameters are notated as `replaceable`; however, you may want to modify other parameters to suit your situation.

Summary of tasks and required RFCs:

1. Create the infrastructure:
   1. [Create an RDS Stack (CLI)](ex-WP-stack-rds-create.md "ex-WP-stack-rds-create.md")
   2. Create a load balancer
   3. Create an Auto scaling group and tie it to the load balancer
   4. Create an S3 bucket for CodeDeploy applications

2. Create a WordPress application bundle (does not require an RFC)
3. Deploy the WordPress application bundle with CodeDeploy:
   1. Create a CodeDeploy application
   2. Create a CodeDeploy deployment group
   3. Upload your WordPress application bundle to the S3 bucket (does not require an RFC)
   4. Deploy the CodeDeploy application

4. Validate the deployment
5. Tear down the deployment
   Follow all steps at the command line from your authenticated account.

## Creating an RFC using the CLI

For detailed information on creating RFCs, see
[Creating RFCs](../userguide/create-rfcs.md "../userguide/create-rfcs.md"); for an explanation of common RFC parameters, see
[RFC common parameters](../userguide/rfc-common-params.md "../userguide/rfc-common-params.md") .

## Create a WordPress Application Bundle for CodeDeploy

This section provides an example of creating an application deployment bundle.

1. Download WordPress, extract the files and create a ./scripts directory.

Linux command:

```
wget https://github.com/WordPress/WordPress/archive/master.zip
```

Windows: Paste `https://github.com/WordPress/WordPress/archive/master.zip` into a browser window and download the zip file.

Create a temporary directory in which to assemble the package.

Linux:

```
mkdir /tmp/WordPress
```

Windows: Create a "WordPress" directory, you will use the directory path later. 2. Extract the WordPress source to the "WordPress" directory and create a ./scripts directory.

Linux:

```
unzip master.zip -d /tmp/WordPress_Temp
cp -paf /tmp/WordPress_Temp/WordPress-master/* /tmp/WordPress
rm -rf /tmp/WordPress_Temp
rm -f master
cd /tmp/WordPress
mkdir scripts
```

Windows: Go to the "WordPress" directory that you created and create a "scripts" directory there.

If you are in a Windows environment, be sure to set the break type for the script files to Unix (LF). In Notepad ++, this is an option at the bottom
right of the window. 3. Create the CodeDeploy **appspec.yml** file, in the WordPress directory (if
copying the example, check the indentation, each space counts). IMPORTANT: Ensure that
the "source" path is correct for copying the WordPress files (in this case, in your
WordPress directory) to the expected destination (/var/www/html/WordPress). In the
example, the appspec.yml file is in the directory with the WordPress files, so only "/"
is needed. Also, even if you used a RHEL AMI for your Auto Scaling group, leave the "os:
linux" line as-is. Example appspec.yml file:

```
version: 0.0
os: linux
files:
  - source: /
    destination: /var/www/html/WordPress
hooks:
  BeforeInstall:
    - location: scripts/install_dependencies.sh
      timeout: 300
      runas: root
  AfterInstall:
    - location: scripts/config_wordpress.sh
      timeout: 300
      runas: root
  ApplicationStart:
    - location: scripts/start_server.sh
      timeout: 300
      runas: root
  ApplicationStop:
    - location: scripts/stop_server.sh
      timeout: 300
      runas: root
```

4. Create bash file scripts in the WordPress ./scripts directory.

First, create `config_wordpress.sh` with the following content (if you prefer, you can edit the wp-config.php file directly).

###### Note

Replace `DBName` with the value given in the HA Stack RFC (for example, `wordpress`).

Replace `DB_MasterUsername` with the `MasterUsername` value given in the HA Stack RFC (for example, `admin`).

Replace `DB_MasterUserPassword` with the `MasterUserPassword` value given in the HA Stack RFC (for example, `p4ssw0rd`).

Replace `DB_ENDPOINT` with the endpoint DNS name in the execution outputs of the HA Stack RFC (for example,
`srt1cz23n45sfg.clgvd67uvydk.us-east-1.rds.amazonaws.com`). You can find this with the [GetRfc](../ApiReference-cm/API_GetRfc.md "../ApiReference-cm/API_GetRfc.md") operation (CLI: get-rfc --rfc-id RFC_ID) or in the AMS
Console RFC details page for the HA Stack RFC that you previously submitted.

```
#!/bin/bash
chmod -R 755 /var/www/html/WordPress
cp /var/www/html/WordPress/wp-config-sample.php /var/www/html/WordPress/wp-config.php
cd /var/www/html/WordPress
sed -i "s/database_name_here/`DBName`/g" wp-config.php
sed -i "s/username_here/`DB_MasterUsername`/g" wp-config.php
sed -i "s/password_here/`DB_MasterUserPassword`/g" wp-config.php
sed -i "s/localhost/`DB_ENDPOINT`/g" wp-config.php
```

5. In the same directory create `install_dependencies.sh` with the following content:

```
#!/bin/bash
yum install -y php
yum install -y php-mysql
yum install -y mysql
service httpd restart
```

###### Note

HTTPS is installed as part of the user data at launch in order to allow health checks to work from the start. 6. In the same directory create `start_server.sh` with the following content:

    * For Amazon Linux instances, use this:



    ```
    #!/bin/bash
    service httpd start
    ```
    * For RHEL instances, use this (the extra commands are policies that allow SELINUX to accept WordPress):



    ```
    #!/bin/bash
    setsebool -P  httpd_can_network_connect_db 1
    setsebool -P  httpd_can_network_connect 1
    chcon -t httpd_sys_rw_content_t /var/www/html/WordPress/wp-content -R
    restorecon -Rv /var/www/html
    service httpd start
    ```

7. In the same directory create `stop_server.sh` with the following content:

```
#!/bin/bash
service httpd stop
```

8. Create the zip bundle.

Linux:

```
$ cd /tmp/WordPress
$ zip -r wordpress.zip .
```

Windows: Go to your "WordPress" directory and select all of the files and create a zip file, be sure to name it wordpress.zip.

## Deploy the WordPress Application Bundle with CodeDeploy

The CodeDeploy is an AWS deployment service that automates application deployments to Amazon EC2 instances. This part of the process involves creating a
CodeDeploy application, creating a CodeDeploy deployment group, and then deploying the application using CodeDeploy.

### Create a CodeDeploy Application

The CodeDeploy application is simply a name or container used by AWS CodeDeploy to ensure that the correct revision, deployment configuration, and
deployment group are referenced during a deployment. The deployment configuration, in this case, is the WordPress bundle that you previously created.

REQUIRED DATA:

- `VpcId`: The VPC that you are using, this should be the same as the previously used VPC.
- `CodeDeployApplicationName`: Must be unique in the account. Look at the CodeDeploy Console to check for existing application names.
- `ChangeTypeId` and `ChangeTypeVersion`: The change type ID for this walkthrough is `ct-0ah3gwb9seqk2`,
  to find out the latest version, run this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value=ct-0ah3gwb9seqk2
```

1. Output the execution parameters JSON schema for the CodeDeploy application CT to a file in your current folder; example names it CreateCDAppParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-0ah3gwb9seqk2" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateCDAppParams.json
```

2. Modify and save the JSON file as follows; you can delete and replace the contents.

```
{
"Description":                      "`Create WordPress CodeDeploy App`",
"VpcId":                            "`VPC_ID`",
"StackTemplateId":                  "stm-sft6rv00000000000",
"Name":                             "`WordPressCDApp`",
"TimeoutInMinutes":                 60,
"Parameters":   {
    "CodeDeployApplicationName":    "`WordPressCDApp`"
    }
}
```

3. Output the JSON template for CreateRfc to a file in your current folder; example names it CreateCDAppRfc.json.

```
aws amscm create-rfc --generate-cli-skeleton > CreateCDAppRfc.json
```

4. Modify and save the JSON file as follows; you can delete and replace the contents. Note that
   `RequestedStartTime` and `RequestedEndTime` are now optional; excluding them causes the RFC
   to be executed as soon as it is approved (which usually happens automatically). Tosubmit a "scheduled" RFC, add those values.

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-0ah3gwb9seqk2",
"Title":                "`CD-App-For-WP-Stack-RFC`"
}
```

5. Create the RFC, specifying the CreateCDAppRfc file and the execution parameters file:

```
aws amscm create-rfc --cli-input-json file://CreateCDAppRfc.json --execution-parameters file://CreateCDAppParams.json
```

You receive the RFC ID of the new RFC in the response. Save the ID for subsequent steps. 6. Submit the RFC:

```
`aws amscm submit-rfc --rfc-id `RFC_ID``
```

If the RFC succeeds, you receive no output. 7. Submit the RFC:

```
`aws amscm get-rfc --rfc-id `RFC_ID``
```

### Create a CodeDeploy Deployment Group

Create the CodeDeploy deployment group.

A CodeDeploy deployment group defines a set of individual instances targeted for a deployment.

REQUIRED DATA:

- `VpcId`: The VPC that you are using, this should be the same as the previously used VPC.
- `CodeDeployApplicationName`: Use the value you previously created.
- `CodeDeployAutoScalingGroups`: Use the name of the Auto Scaling group that you created previously.
- `CodeDeployDeploymentGroupName`: A name for the deployment group. This name must be unique for each application associated with the deployment group.
- `CodeDeployServiceRoleArn`: Use the formula given in the example.
- `ChangeTypeId` and `ChangeTypeVersion`: The change type ID for this walkthrough is `ct-2gd0u847qd9d2`,
  to find out the latest version, run this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value=ct-2gd0u847qd9d2
```

1. Output the execution parameters JSON schema to a file in your current folder; example names it CreateCDDepGroupParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-2gd0u847qd9d2" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateCDDepGroupParams.json
```

2. Modify and save the JSON file as follows; you can delete and replace the contents.

```
{
"Description":                      "`CreateWPCDDeploymentGroup`",
"VpcId":                            "`VPC_ID`",
"StackTemplateId":                  "stm-sp9lrk00000000000",
"Name":                             "`WordPressCDAppGroup`",
"TimeoutInMinutes":                 60,
"Parameters":   {
    "CodeDeployApplicationName":        "`WordPressCDApp`",
    "CodeDeployAutoScalingGroups":      ["`ASG_NAME`"],
    "CodeDeployDeploymentConfigName":   "CodeDeployDefault.HalfAtATime",
    "CodeDeployDeploymentGroupName":    "`UNIQUE_CDDepGroupNAME`",
    "CodeDeployServiceRoleArn":         "arn:aws:iam::`ACCOUNT_ID`:role/aws-codedeploy-role"
    }
}
```

3. Output the JSON template for CreateRfc to a file in your current folder; example names it CreateCDDepGroupRfc.json.

```
aws amscm create-rfc --generate-cli-skeleton > CreateCDDepGroupRfc.json
```

4. Modify and save the JSON file as follows; you can delete and replace the contents. Note that
   `RequestedStartTime` and `RequestedEndTime` are now optional; excluding them causes the RFC
   to be executed as soon as it is approved (which usually happens automatically). To submit a "scheduled" RFC, add those values.

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-2gd0u847qd9d2",
"Title":                "`CD-Dep-Group-For-WP-Stack-RFC`"
}
```

5. Create the RFC, specifying the CreateCDDepGroupRfc file and the execution parameters file:

```
aws amscm create-rfc --cli-input-json file://CreateCDDepGroupRfc.json --execution-parameters file://CreateCDDepGroupParams.json
```

You receive the RFC ID of the new RFC in the response. Save the ID for subsequent steps. 6. Submit the RFC:

```
aws amscm submit-rfc --rfc-id `RFC_ID`
```

If the RFC succeeds, you receive no output. 7. Check the RFC status:

```
aws amscm get-rfc --rfc-id `RFC_ID`
```

### Upload the WordPress Application

You automatically have access to any S3 bucket instance that you create. You can access it through your Bastions
(see [Accessing Instances](../userguide/using-bastions.md "../userguide/using-bastions.md")), or through the S3 console, and upload the CodeDeploy bundle.
The bundle needs to be in place in order to continue deploying the stack. The example uses the bucket name previously created.

```
aws s3 cp wordpress/wordpress.zip s3://ACCOUNT_ID-codedeploy-bundles/
```

### Deploy the WordPress Application with CodeDeploy

Deploy the CodeDeploy application.

Once you have your CodeDeploy application bundle and deployment group, use this RFC to deploy the application.

REQUIRED DATA:

- `VPC-ID`: The VPC you are using, this should be the same as the previously used VPC.
- `CodeDeployApplicationName`: Use the name for the CodeDeploy application that you previously created.
- `CodeDeployDeploymentGroupName`: Use the name of the CodeDeploy deployment group that you created previously.
- `S3Location` (where you uploaded the application bundle): `S3Bucket`: The BucketName that you previously created,
  `S3BundleType` and `S3Key`: The type of, and name of, the bundle that you put on your S3 store.
- `ChangeTypeId` and `ChangeTypeVersion`: The change type ID for this walkthrough is `ct-2edc3sd1sqmrb`,
  to find out the latest version, run this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value=ct-2edc3sd1sqmrb
```

1. Output the execution parameters JSON schema for the CodeDeploy application deployment CT to a file in your current folder; example names it DeployCDAppParams.json.

```
aws amscm get-change-type-version --change-type-id "ct-2edc3sd1sqmrb" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > DeployCDAppParams.json
```

2. Modify the JSON file as follows; you can delete and replace the contents. For `S3Bucket`, use the
   `BucketName` that you previously created.

```
{
"Description":                      "`Deploy WordPress CodeDeploy Application`",
"VpcId":                            "`VPC_ID`",
"Name":                             "`WP CodeDeploy Deployment Group`",
"TimeoutInMinutes":                 60,
"Parameters":   {
    "CodeDeployApplicationName":        "`WordPressCDApp`",
    "CodeDeployDeploymentGroupName":    "`WordPressCDDepGroup`",
    "CodeDeployIgnoreApplicationStopFailures": `false`,
    "CodeDeployRevision": {
      "RevisionType": "`S3`",
      "S3Location": {
        "S3Bucket": "`ACCOUNT_ID.BUCKET_NAME`",
        "S3BundleType": "`zip`",
        "S3Key": "wordpress.`zip`" }
        }
    }
}
```

3. Output the JSON template for CreateRfc to a file in your current folder; example names it DeployCDAppRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > DeployCDAppRfc.json
```

4. Modify and save the DeployCDAppRfc.json file; you can delete and replace the contents.

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-2edc3sd1sqmrb",
"Title":                "`CD-Deploy-For-WP-Stack-RFC`",
"RequestedStartTime":   "`2017-04-28T22:45:00Z`",
"RequestedEndTime":     "`2017-04-28T22:45:00Z`"
}
```

5. Create the RFC, specifying the execution parameters file and the DeployCDAppRfc file:

```
aws amscm create-rfc --cli-input-json file://DeployCDAppRfc.json  --execution-parameters file://DeployCDAppParams.json
```

You receive the RfcId of the new RFC in the response. Save the ID for subsequent steps. 6. Submit the RFC:

```
aws amscm submit-rfc --rfc-id `RFC_ID`
```

If the RFC succeeds, you receive no output.

## Validate the Application Deployment

Navigate to the endpoint (ELB CName) of the previously created load balancer, with the WordPress deployed path: /WordPress. For example:

```
http://stack-`ID-FOR-ELB`.us-east-1.elb.amazonaws.com/WordPress
```

## Tear Down the Application Deployment

To tear down the deployment, you submit the Delete Stack CT against the RDS database stack, the application load balancer, the Auto Scaling group, the S3 bucket, and
the Code Deploy application and group--six RFCs in all. Additionally, you can submit a service request for the RDS snapshots to be deleted
(they are deleted automatically after ten days, but they do cost a small amount while there). Gather the stack IDs for all and then follow these steps.

This walkthrough provides an example of using the AMS console to delete an S3 stack; this procedure applies to deleting any stack using the AMS console.

###### Note

If deleting an S3 bucket, it must be emptied of objects first.

REQUIRED DATA:

- `StackId`: The stack to use. You can find this by looking at the AMS Console **Stacks** page, available through a link in the left nav.
  Using the AMS SKMS API/CLI, run the For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. operation (`list-stack-summaries` in the CLI).
- The change type ID for this walkthrough is `ct-0q0bic0ywqk6c`, the version is "1.0", to find out the latest version, run this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value=ct-0q0bic0ywqk6c
```

_INLINE CREATE_:

- Issue the create RFC command with execution parameters provided inline (escape quotes when providing execution parameters inline). E

```
aws amscm create-rfc --change-type-id "ct-0q0bic0ywqk6c" --change-type-version "1.0" --title "Delete My Stack" --execution-parameters "{\"StackId\":\"`STACK_ID`\"}"

```

- Submit the RFC using the RFC ID returned in the create RFC operation. Until submitted, the RFC remains in the `Editing` state and is not acted on.

```
aws amscm submit-rfc --rfc-id `RFC_ID`
```

- Monitor the RFC status and view execution output:

```
aws amscm get-rfc --rfc-id `RFC_ID`
```

_TEMPLATE CREATE_:

1. Output the RFC template to a file in your current folder; example names it DeleteStackRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > DeleteStackRfc.json
```

2. Modify and save the DeleteStackRfc.json file. Since deleting a stack has only one execution parameter, the execution parameters can be in the
   DeleteStackRfc.json file itself (there is no need to create a separate JSON file with execution parameters).

The internal quotation marks in the ExecutionParameters JSON extension must be escaped with a backslash (\). Example without start and end time:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-0q0bic0ywqk6c",
"Title":                "`Delete-My-Stack-RFC`"
"ExecutionParameters":  "{
        \"StackId\":\"`STACK_ID`\"}"
}
```

3. Create the RFC:

```
aws amscm create-rfc --cli-input-json file://DeleteStackRfc.json
```

You receive the RfcId of the new RFC in the response. For example:

```
{
"RfcId": "daaa1867-ffc5-1473-192a-842f6b326102"
}
```

Save the ID for subsequent steps. 4. Submit the RFC:

```
aws amscm submit-rfc --rfc-id `RFC_ID`
```

If the RFC succeeds, you receive no confirmation at the command line. 5. To monitor the status of the request and to view Execution Output:

```
aws amscm get-rfc --rfc-id `RFC_ID` --query "Rfc.{Status:Status.Name,Exec:ExecutionOutput}" --output table
```

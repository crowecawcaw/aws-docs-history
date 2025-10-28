# Tutorial: Create a pipeline that builds and

tests your Android app with AWS Device Farm

You can use AWS CodePipeline to configure a continuous integration flow in which your app is built
and tested each time a commit is pushed. This tutorial shows how to create and configure a
pipeline to build and test your Android app with source code in a GitHub repository. The
pipeline detects the arrival of a new GitHub commit and then uses [CodeBuild](../../../codebuild/latest/userguide/welcome.md "../../../codebuild/latest/userguide/welcome.md") to build the app and [Device Farm](../../../devicefarm/latest/developerguide/welcome.md "../../../devicefarm/latest/developerguide/welcome.md") to test it.

###### Important

As part of creating a pipeline in the console, an S3 artifact bucket will be used by CodePipeline
for artifacts. (This is different from the bucket used for an S3 source action.) If the S3
artifact bucket is in a different account from the account for your pipeline, make sure that
the S3 artifact bucket is owned by AWS accounts that are safe and will be dependable.

###### Important

Many of the actions you add to your pipeline in this procedure involve AWS resources that you need to create before you create the pipeline. AWS resources for your source actions must always be created in the same AWS Region
where you create your pipeline. For example, if you create your pipeline in the US East (Ohio)
Region, your CodeCommit repository must be in the US East (Ohio) Region.

You can add cross-region actions when you create your pipeline. AWS resources for cross-region actions must be in the same AWS Region where you plan to execute the action.
For more information, see [Add a cross-Region action in CodePipeline](actions-create-cross-region.md "actions-create-cross-region.md").

You can try this out using your existing Android app and test definitions, or you can use
the [sample
app and test definitions provided by Device Farm](https://github.com/aws-samples/aws-device-farm-sample-app-for-android "https://github.com/aws-samples/aws-device-farm-sample-app-for-android").

###### Note

**Before you begin**

1. Sign in to the AWS Device Farm console and choose **Create a new
   project**.
2. Choose your project. In the browser, copy the URL of your new project. The URL contains
   the project ID.
3. Copy and retain this project ID. You use it when you create your pipeline in
   CodePipeline.

Here is an example URL for a project. To extract the project ID, copy the value after
`projects/`. In this example, the project ID is
`eec4905f-98f8-40aa-9afc-4c1cfexample`.

```
https://<region-URL>/devicefarm/home?region=us-west-2#/projects/eec4905f-98f8-40aa-9afc-4c1cfexample/runs
```

## Configure CodePipeline to use your Device Farm tests

1. Add and commit a file called [`buildspec.yml`](../../../codebuild/latest/userguide/build-spec-ref.md "../../../codebuild/latest/userguide/build-spec-ref.md") in the root of your app code, and push it
   to your repository. CodeBuild uses this file to perform commands and access artifacts required
   to build your app.

```
version: 0.2

phases:
  build:
    commands:
      - chmod +x ./gradlew
      - ./gradlew assembleDebug
artifacts:
  files:
     - './android/app/build/outputs/**/*.apk'
  discard-paths: yes
```

2. (Optional) If you [use Calabash or
   Appium to test your app](../../../devicefarm/latest/developerguide/test-types-intro.md "../../../devicefarm/latest/developerguide/test-types-intro.md"), add the test definition file to your repository. In a
   later step, you can configure Device Farm to use the definitions to carry out your test suite.

If you use Device Farm built-in tests, you can skip this step. 3. To create your pipeline and add a source stage, do the following:

    1. Sign in to the AWS Management Console and open the CodePipeline console at
     [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
    2. On the **Welcome** page, **Getting started**
     page, or the **Pipelines** page, choose **Create
     pipeline**.
    3. On the **Step 1: Choose creation option** page, under
     **Creation options**, choose the **Build custom
     pipeline** option. Choose **Next**.
    4. On the **Step 2: Choose pipeline settings** page, in
     **Pipeline name**, enter the name for your pipeline.
    5. CodePipeline provides V1 and V2 type pipelines, which differ in characteristics and
     price. The V2 type is the only type you can choose in the console. For more
     information, see [pipeline
     types](pipeline-types-planning.md "pipeline-types-planning.md"). For information about pricing for CodePipeline, see [Pricing](https://aws.amazon.com/codepipeline/pricing/ "https://aws.amazon.com/codepipeline/pricing/").
    6. In **Service role**, leave **New service role**
     selected, and leave **Role name** unchanged. You can also choose to
     use an existing service role, if you have one.


    ###### Note

    If you use a CodePipeline service role that was created before July 2018, you need to
     add permissions for Device Farm. To do this, open the IAM console, find the role, and
     then add the following permissions to the role's policy. For more information, see
     [Add permissions to the CodePipeline
     service role](how-to-custom-role.md#how-to-update-role-new-services "how-to-custom-role.md#how-to-update-role-new-services").


    ```
    {
         "Effect": "Allow",
         "Action": [
            "devicefarm:ListProjects",
            "devicefarm:ListDevicePools",
            "devicefarm:GetRun",
            "devicefarm:GetUpload",
            "devicefarm:CreateUpload",
            "devicefarm:ScheduleRun"
         ],
         "Resource": "*"
    }
    ```
    7. Leave the settings under **Advanced settings** at their defaults,
     and then choose **Next**.
    8. On the **Step 3: Add source stage** page, in **Source
     provider**, choose **GitHub (via GitHub App)**.
    9. Under **Connection**, choose an existing connection or create a
     new one. To create or manage a connection for your GitHub source action, see [GitHub connections](connections-github.md "connections-github.md").
    10. In **Repository**, choose the source repository.
    11. In **Branch**, choose the branch that you want to use.
    12. Leave the remaining defaults for the source action. Choose
     **Next**.

4. In **Step 4: Add build stage**, add a build stage:
   1. In **Build provider**, choose **Other build
      providers**, and then choose **AWS CodeBuild**. Allow
      **Region** to default to the pipeline Region.
   2. Choose **Create project**.
   3. In **Project name**, enter a name for this build project.
   4. In **Environment image**, choose **Managed
      image**. For **Operating system**, choose
      **Ubuntu**.
   5. For **Runtime**, choose **Standard**. For
      **Image**, choose
      **aws/codebuild/standard:5.0**.

   CodeBuild uses this OS image, which has Android Studio installed, to build your
   app. 6. For **Service role**, choose your existing CodeBuild service role or
   create a new one. 7. For **Build specifications**, choose **Use a buildspec
   file**. 8. Choose **Continue to CodePipeline**. This returns to the CodePipeline
   console and creates a CodeBuild project that uses the `buildspec.yml`
   in your repository for configuration. The build project uses a service role to manage
   AWS service permissions. This step might take a couple of minutes. 9. Choose **Next**.

5. In **Step 5: Add test stage**, choose **Skip test
   stage**, and then accept the warning message by choosing
   **Skip** again.

Choose **Next**. 6. On the **Step 6: Add deploy stage** page, choose **Skip
deploy stage**, and then accept the warning message by choosing
**Skip** again. Choose **Next**. 7. On **Step 7: Review**, choose **Create pipeline**.
You should see a diagram that shows the source and build stages. 8. Add a Device Farm test action to your pipeline:

    1. In the upper right, choose **Edit**.
    2. At the bottom of the diagram, choose **+ Add stage**. In
     **Stage name**, enter a name, such as
     `Test`.
    3. Choose **+ Add action group**.
    4. In **Action name**, enter a name.
    5. In **Action provider**, choose **AWS Device
     Farm**. Allow **Region** to default to the pipeline
     Region.
    6. In **Input artifacts**, choose the input artifact that matches
     the output artifact of the stage that comes before the test stage, such as
     `BuildArtifact`.


    In the AWS CodePipeline console, you can find the name of the output artifact for each
     stage by hovering over the information icon in the pipeline diagram. If your pipeline
     tests your app directly from the **Source** stage, choose
     **SourceArtifact**. If the pipeline includes a
     **Build** stage, choose **BuildArtifact**.
    7. In **ProjectId**, enter your Device Farm project ID. Use the steps at
     the start of this tutorial to retrieve your project ID.
    8. In **DevicePoolArn**, enter the ARN for the device pool. To get
     the available device pool ARNs for the project, including the ARN for Top Devices, use
     the AWS CLI to enter the following command:



    ```
    aws devicefarm list-device-pools --arn arn:aws:devicefarm:us-west-2:`account_ID`:project:`project_ID`
    ```
    9. In **AppType**, enter **Android**.


    The following is a list of valid values for **AppType**:




    	* **iOS**
    	* **Android**
    	* **Web**
    10. In **App**, enter the path of the compiled app package. The path
     is relative to the root of the input artifact for the test stage. Typically, this path
     is similar to `app-release.apk`.
    11. In **TestType**, enter your type of test, and then in
     **Test**, enter the path of the test definition file. The path is
     relative to the root of the input artifact for your test.


    The following is a list of valid values for **TestType**:




    	* **APPIUM\_JAVA\_JUNIT**
    	* **APPIUM\_JAVA\_TESTNG**
    	* **APPIUM\_NODE**
    	* **APPIUM\_RUBY**
    	* **APPIUM\_PYTHON**
    	* **APPIUM\_WEB\_JAVA\_JUNIT**
    	* **APPIUM\_WEB\_JAVA\_TESTNG**
    	* **APPIUM\_WEB\_NODE**
    	* **APPIUM\_WEB\_RUBY**
    	* **APPIUM\_WEB\_PYTHON**
    	* **BUILTIN\_FUZZ**
    	* **INSTRUMENTATION**
    	* **XCTEST**
    	* **XCTEST\_UI**
    ###### Note

    Custom environment nodes are not supported.
    12. In the remaining fields, provide the configuration that is appropriate for your
     test and application type.
    13. (Optional) In **Advanced**, provide configuration information for
     your test run.
    14. Choose **Save**.
    15. On the stage you are editing, choose **Done**. In the AWS CodePipeline
     pane, choose **Save**, and then choose **Save** on
     the warning message.
    16. To submit your changes and start a pipeline build, choose **Release
     change**, and then choose **Release**.



# Integrating AWS Device Farm in a CodePipeline test stage
<a name="codepipeline"></a>

 You can use [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/) to incorporate mobile app tests configured in Device Farm into an AWS-managed automated release pipeline. You can configure your pipeline to run tests on demand, on a schedule, or as part of a continuous integration flow.

The following diagram shows the continuous integration flow in which an Android app is built and tested each time a push is committed to its repository. To create this pipeline configuration, see the [Tutorial: Build and Test an Android App When Pushed to GitHub](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-codebuild-devicefarm.html). 

![Continuos integration setup for building and testing Android source code from a GitHub repository on each push.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-push-build-test.png)




|  |  |  |  |  | 
| --- |--- |--- |--- |--- |
| 1. Configure | 2. Add definitions | 3. Push | 4. Build and test | 5. Report | 
| Configure pipeline resources | Add build and test definitions to your package | Push a package to your repository |  App build and test of build output artifact kicked off automatically | View test results | 

To learn how to configure a pipeline that continually tests a compiled app (such as an iOS `.ipa` or Android `.apk` file) as its source, see [Tutorial: Test an iOS App Each Time You Upload an .ipa File to an Amazon S3 Bucket](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-codebuild-devicefarm-S3.html). 

## Configure CodePipeline to use your Device Farm tests
<a name="codepipeline-configure-tests"></a>

 In these steps, we assume that you have [configured a Device Farm project](how-to-create-project.md) and [created a pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/getting-started-codepipeline.html). The pipeline should be configured with a test stage that receives an [input artifact](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html#welcome-introducing-artifacts) that contains your test definition and compiled app package files. The test stage input artifact can be the output artifact of either a source or build stage configured in your pipeline. 

**To configure a Device Farm test run as an CodePipeline test action**

1. Sign in to the AWS Management Console and open the CodePipeline console at [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/).

1. Choose the pipeline for your app release.

1. On the test stage panel, choose the pencil icon, and then choose **Action**.

1. On the **Add action** panel, for **Action category**, choose **Test**.

1. In **Action name**, enter a name. 

1. In **Test provider**, choose **AWS Device Farm**.  
![Add a Device Farm test action to your pipeline.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-add-action.png)

1. In **Project name**, choose your existing Device Farm project or choose **Create a new project**. 

1. In **Device pool**, choose your existing device pool or choose **Create a new device pool**. If you create a device pool, you need to select a set of test devices.

1. In **App type**, choose the platform for your app.  
![Configure CodePipeline to use Device Farm as a test provider for stages of your pipeline.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-choose-test-provider.png)

1. In **App file path**, enter the path of the compiled app package. The path is relative to the root of the input artifact for your test.

1. In **Test type**, do one of the following: 
   + If you're using one of the built-in Device Farm tests, choose the type of test configured in your Device Farm project.
   + If you aren't using one of the Device Farm built-in tests, in the **Test file path**, enter the path of the test definition file. The path is relative to the root of the input artifact for your test.  
![Device Farm test types.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-test-type.png)

1. In the remaining fields, provide the configuration that is appropriate for your test and application type.

1. (Optional) In **Advanced**, provide detailed configuration for your test run.  
![Advanced AWS Device Farm configurations.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-advanced.png)

1. In **Input artifacts**, choose the input artifact that matches the output artifact of the stage that comes before the test stage in the pipeline.   
![Advanced AWS Device Farm configurations.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-input-artifact.png)

    In the CodePipeline console, you can find the name of the output artifact for each stage by hovering over the information icon in the pipeline diagram. If your pipeline tests your app directly from the **Source** stage, choose **MyApp**. If your pipeline includes a **Build** stage, choose **MyAppBuild**.  
![Advanced AWS Device Farm configurations.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/codepipeline-output-artifact.png)

1. At the bottom of the panel, choose **Add Action**.

1. In the CodePipeline pane, choose **Save pipeline change**, and then choose **Save change**.

1. To submit your changes and start a pipeline build, choose **Release change**, and then choose **Release**.
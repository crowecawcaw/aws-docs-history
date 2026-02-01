# Create a build with

files in Amazon S3

You can store your build files in Amazon S3 and upload them to Amazon GameLift Servers from there. When
you create you build, you specify the S3 bucket location, and Amazon GameLift Servers retrieves the
build files directly from Amazon S3.

###### To create a build resource

1. **Store your build files in Amazon S3.** Create a
   .zip file containing the packaged build files and upload it to an S3 bucket
   in your AWS account. Take note of the bucket label and the file name,
   you'll need these when creating an Amazon GameLift Servers build.
2. **Give Amazon GameLift Servers access to your build files.**
   Create an IAM role by following the instructions in [Access a
   game build file in Amazon S3](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-storage-loc "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-storage-loc"). After you've created the role, take note of the new role's Amazon
   Resource Name (ARN), you'll need this when creating a build.
3. **Create a build.** Use the Amazon GameLift Servers console or
   the AWS CLI to create a new build record. You must have the
   `PassRole` permission, as described in [IAM permission examples for Amazon GameLift Servers](gamelift-iam-policy-examples.md "gamelift-iam-policy-examples.md").

Console

1. In the [Amazon GameLift Servers
   console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), in the navigation pane, choose
   **Hosting**,
   **Builds**.
2. On the **Builds** page, choose
   **Create build**.
3. On the **Create build** page, under
   **Build settings**, do the
   following:
   1. For **Name**, enter a script
      name.
   2. For **Version**, enter a version.
      Because you can update the content of a build, version
      data can help you track updates.
   3. For **Operating system (OS)**, choose
      the OS of your game server build. You can't update this
      value later.
   4. For **Game server build**, enter the
      **S3 URI** of the build object that
      you uploaded to Amazon S3, and choose the **Object
      version**. If you don't remember the Amazon S3
      URI and object version, choose **Browse
      S3** and search for the build
      object.
   5. For **IAM role**, choose the role
      that you created that gives Amazon GameLift Servers access to your S3
      bucket and build object.

4. (Optional) Under **Tags**, add tags to the
   build by entering **Key** and
   **Value** pairs.
5. Choose **Create**.

Amazon GameLift Servers assigns an ID to the new build and uploads the
designated .zip file. You can view the new build, including the
status, on the **Builds** page.

AWS CLI
To define the new build and upload your server build files, use
the [`create-build`](../../../cli/latest/reference/gamelift/create-build.md "../../../cli/latest/reference/gamelift/create-build.md") command.

1. Open a command line window and switch to a directory where you
   can use the AWS CLI.
2. Enter the following **create-build**
   command:

```
aws gamelift create-build \
    --name `user-defined name of build` \
    --server-sdk-version `server SDK for Amazon GameLift Servers version` \
    --operating-system `supported OS` \
    --build-version `user-defined build number` \
    --storage-location "Bucket"=`S3 bucket label`,"Key"=`Build .zip file name`,"RoleArn"=`Access role ARN`} \
    --region `region name`
```

    * **name** – A descriptive name
     for the new build.
    * **server-sdk-version** – The
     version of the server SDK for Amazon GameLift Servers you used to integrate
     your game server with Amazon GameLift Servers. If you don't provide a
     value, Amazon GameLift Servers uses the default value
     `4.0.2`.
    * **operating-system** – The game
     server build's runtime environment. You must specify an
     OS value. You can't update this later.
    * **build-version** – The version
     details for the build files. This information can be
     useful because each new version of your game server
     requires a new build resource.
    * **storage-location**




    	+ **Bucket** – The name of
    	 the S3 bucket that contains your build. For
    	 example, "my\_build\_files".
    	+ **Key** – The name of
    	 the .zip file that contains your build files. For
    	 example, "my\_game\_build\_7.0.1, 7.0.2".
    	+ **RoleARN** – The ARN
    	 assigned to the IAM role that you created. For
    	 example,
    	 "arn:aws:iam::111122223333:role/GameLiftAccess".
    	 For an example policy, see [Access a
    	 game build file in Amazon S3](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-storage-loc "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-storage-loc").
    * **region** – Create the build in
     the AWS Region where you plan to deploy fleets. If
     you're deploying your game in multiple Regions, create a
     build in each Region.


    ###### Note

    We recommend checking your current default Region
     using the [`configure get`](../../../cli/latest/reference/configure/get.md "../../../cli/latest/reference/configure/get.md") command. To change your default
     Region, use the [`configure set`](../../../cli/latest/reference/configure/set.md "../../../cli/latest/reference/configure/set.md")
     command.

_Example_

```
aws gamelift create-build \
 --operating-system WINDOWS\_2022 \
    --storage-location "Bucket"="my_game_build_files","Key"="mygame_build_101.zip","RoleArn"="arn:aws:iam::111122223333:role/gamelift" \
    --name "My Game Nightly Build" \
    --build-version "build 101" \
    --region us-west-2
```

3. To view the new build, use the [`describe-build`](../../../cli/latest/reference/gamelift/describe-build.md "../../../cli/latest/reference/gamelift/describe-build.md") command.

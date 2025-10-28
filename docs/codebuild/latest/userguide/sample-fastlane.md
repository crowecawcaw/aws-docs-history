# Tutorial: Apple code signing with Fastlane in CodeBuild using

S3 for certificate storage

[fastlane](https://docs.fastlane.tools/ "https://docs.fastlane.tools/") is a popular open source
automation tool to automate beta deployments and releases for your iOS and Android apps. It
handles all tedious tasks, like generating screenshots, dealing with code signing, and
releasing your application.

## Prerequisites

To complete this tutorial, you must first have set up the following:

- An AWS account
- An [Apple Developer account](https://developer.apple.com/ "https://developer.apple.com/")
- An S3 bucket for storing certificates
- fastlane installed in your project - [Guide](https://docs.fastlane.tools/getting-started/ios/setup/ "https://docs.fastlane.tools/getting-started/ios/setup/")
  to install fastlane

## Step 1: Set up Fastlane

Match with S3 on your local machine

[Fastlane Match](https://docs.fastlane.tools/actions/match/ "https://docs.fastlane.tools/actions/match/") is one
of the [Fastlane tools](https://fastlane.tools/ "https://fastlane.tools/"), and it allows for
seamless configuration for code signing in both your local development environment and
on CodeBuild. Fastlane Match stores all of your code signing certificates and provisioning
profiles in a Git repository/S3 Bucket/Google Cloud Storage, and downloads and installs
the necessary certificates and profiles when required.

In this example configuration, you will set up and use an Amazon S3 bucket for storage.

######

1. Initialize match in your project:

```
fastlane match init
```

2. When prompted, choose S3 as the storage mode.
3. Update your `*Matchfile*` to use S3:

```
storage_mode("s3")
   s3_bucket("your-s3-bucket-name")
   s3_region("your-aws-region")
   type("appstore") # The default type, can be: appstore, adhoc, enterprise or development

```

## Step 2: Set up your

Fastfile

Create or update your `Fastfile` with the following lane.

On CodeBuild, Fastlane Match will need to be run every time you build and sign your app.
The easiest way to do this is to add the `match` action to the lane which
builds your app.

```
default_platform(:ios)

platform :ios do
  before_all do
    setup_ci
  end

  desc "Build and sign the app"
  lane :build do
    match(type: "appstore", readonly: true)
    gym(
      scheme: "YourScheme",
      export_method: "app-store"
    )
  end
end
```

###### Note

Make sure to add `setup_ci` to the `before_all` section in
`Fastfile` for the match action to work correctly. This ensures that
a temporary Fastlane keychain with the appropriate permissions is used. Without
using this you may see build failures or inconsistent results.

## Step 3: Run the `fastlane match` command to generate respective

certificates and profiles

The fastlane match command for the given type (i.e., development, appstore, adhoc,
enterprise) will generate the certificate and profile if not available in remote store.
The certificates and profiles will be stored in S3 by fastlane.

```
bundle exec fastlane match appstore
```

The command execution will be interactive and fastlane will ask to set pass phrase for
decrypting the certificates.

## Step 4: Create the application file for your project

Create or add the application file as appropriate for your project.

######

1. Create or add the [Gymfile](http://docs.fastlane.tools/actions/gym/#gymfile "http://docs.fastlane.tools/actions/gym/#gymfile"), [Appfile](http://docs.fastlane.tools/advanced/Appfile/ "http://docs.fastlane.tools/advanced/Appfile/"), [Snapfile](http://docs.fastlane.tools/actions/snapshot/#snapfile "http://docs.fastlane.tools/actions/snapshot/#snapfile"), [Deliverfile](http://docs.fastlane.tools/actions/deliver/#editing-the-deliverfile "http://docs.fastlane.tools/actions/deliver/#editing-the-deliverfile") based on your project build requirements.
2. Commit the changes to your remote repository

## Step 5: Create environment variables in Secrets Manager

Create two secrets for storing the fastlane session cookie and matching pass phrase.
For more information about creating secrets in Secrets Manager, see [Create an AWS Secrets Manager
secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md").

######

1. Access your fastlane session cookie as follows.
   1. Secret key - `FASTLANE_SESSION`
   2. Secret value - session cookie generated from running the following
      command on your local machine.

   ###### Note

   This value is available after authentication in a local file:
   `~/.fastlane/spaceship/my_appleid_username/cookie`.

   ```
   fastlane spaceauth -u <apple account>
   ```

2. Fastlane Match pass phrase - To enable Fastlane Match to decrypt the
   certificates and profiles stored in the S3 bucket, it is necessary to add the
   encryption passphrase that you configured in the Match setup step to the CodeBuild
   project’s environment variables.
   1. Secret key - `MATCH_PASSWORD`
   2. Secret value - `<match passphrase to decrypt
certificates>`. The passphrase is set while generating
      the certificates in Step 3.

###### Note

While creating the above secrets in Secrets Manager, remember to give a secret name with the
following prefix: `/CodeBuild/`

## Step 6: Create a compute fleet

Create the compute fleet for your project.

######

1. In the console, go to CodeBuild and create a new compute fleet.
2. Choose "macOS" as the operating system and select an appropriate compute type
   and image.

## Step 7: Create a project in CodeBuild

Create your project in CodeBuild.

######

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. Create a build project. For information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console")
   and [Run a build (console)](run-build-console.md "run-build-console.md").
3. Set up your source provider (such as GitHub, CodeCommit). This is iOS project
   source repository and not certificates repository.
4. In **Environment**:
   - Choose **Reserved Capacity**.
   - For **Fleet**, select the fleet created above.
   - Provide the name of the service role that CodeBuild will create for
     you.
   - Provide the below environment variables.
     - Name: `MATCH_PASSWORD`, Value:
       `<secrets arn>`, Type: Secrets
       Manager (Secrets ARN created in step 5 for
       MATCH_PASSWORD)
     - Name: `FASTLANE_SESSION`, Value:
       `<secrets arn>`, Type: Secrets
       Manager (Secrets ARN created in Step 5 for
       FASTLANE_SESSION)

5. In **Buildspec**, add the following:

```
version: 0.2

phases:
  install:
    commands:
      - gem install bundler
      - bundle install
  build:
    commands:
      - echo "Building and signing the app..."
      - bundle exec fastlane build
  post_build:
    commands:
      - echo "Build completed on date"

artifacts:
  files:
    - '*/.ipa'
  name: app-$(date +%Y-%m-%d)
```

## Step 8: Configure IAM role

Once the project is created, ensure your CodeBuild project's service role has permissions
to access the S3 bucket containing the certificates. Add the following policy to the
role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3:::your-s3-bucket-name"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": "arn:aws:s3:::your-s3-bucket-name/*"
 }
 ]
}`

```

## Step 9: Run the build

Run the build. You can review the build status and logs in CodeBuild.

Once the job is completed, you will be able to view the log of the job.

## Troubleshooting

- If you encounter issues with certificate fetching, ensure your IAM
  permissions are set up correctly for S3 access.
- If you encounter issues with certificate decrypting, ensure you set correct
  passphrase in MATCH_PASSWORD environment variable.
- For code signing issues, verify that your Apple Developer account has the
  necessary certificates and profiles, and that the bundle identifier in your
  Xcode project matches the one in your provisioning profile.

## Security considerations

The following are security considerations for this tutorial.

- Ensure your S3 bucket has appropriate security settings, including encryption
  at rest. In particular, make sure the bucket has no public access and restrict
  access to only CodeBuild and the system that needs to have an access.
- Consider using AWS Secrets Manager for storing sensitive information like the
  MATCH_PASSWORD and FASTLANE_SESSION.

This sample provides a setup for iOS code signing with Fastlane in CodeBuild using Amazon
S3 for certificate storage. You may need to adjust some steps based on your specific
project requirements and CodeBuild environment. This approach leverages AWS services for
enhanced security and integration within the AWS ecosystem.

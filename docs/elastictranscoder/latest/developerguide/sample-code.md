End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# AWS SDK Sample Code

This section contains sample code that shows how to use the AWS SDKs for Java,
Ruby, PHP, and Python to perform the following operations:

- Create an HLS playlist in Amazon Elastic Transcoder
- Create a job in Elastic Transcoder
- Poll an Amazon Simple Queue Service (Amazon SQS) queue
- Parse a notification from the Amazon Simple Notification Service (Amazon SNS)
- Handle the notification from Amazon SNS
  These operations represent Elastic Transcoder best practices.
  Polling an Amazon SQS queue allows for long polling, which scales more efficiently than
  regular polling, and setting up Amazon SNS notifications allows Elastic Transcoder to deliver
  messages to the Amazon SQS queue.

The sample code shows how to transcode for HLS (HTTP Live Streaming) and
how to handle the Amazon SNS notification once it has been removed from the Amazon SQS queue.

If you are using a language for which an SDK exists, we recommend that you use the SDK
rather than try to work your way through the APIs. You'll find that using the SDKs makes
authentication simpler, integrates easily with your development environment, and
provides easy access to related commands.

###### Topics

- [Background for AWS SDK Sample Code](#sample-intro "#sample-intro")
- [Setting Up Your Environment](#env-setup "#env-setup")
- [Java Samples](#java-sample "#java-sample")
- [Ruby Samples](#ruby-sample "#ruby-sample")
- [PHP Samples](#php-sample "#php-sample")
- [Python Samples](#python-sample "#python-sample")

## Background for AWS SDK Sample Code

### HTTP Live Streaming (HLS)

You use HTTP Live Streaming (HLS) outputs in order to deliver adaptive-bit rate
content to HLS-enabled players. Examples of HLS-enabled devices are Android
4+ devices, iOS devices, desktop media players such as QuickTime or VLC, and
browser players such as jwplayer. Adaptive bit rate allows you to automatically
adjust the quality of delivered content based on the quality of the client
connection.

### Notifications

If you poll the Elastic Transcoder's `ReadJob` API to track job status,
you need to continuously call `ReadJob` on every submitted job. This methodology
cannot scale as the number of transcode jobs increases. To solve this problem,
Elastic Transcoder can publish notifications to Amazon SNS which provides an event-driven
mechanism for tracking job status.

Each Elastic Transcoder notification is sent as a JSON object in the `Message`
field. Because notifications are themselves sent in JSON format, you need to escape the Elastic Transcoder
notification in the message string. For information
about the format and content of Elastic Transcoder notifications, see the
[Notifications](notifications.md "notifications.md") section.

When you are writing custom code to handle job status notifications, follow these
best practices:

- **Handlers must be idempotent.** It is possible that a notification
  will be delivered more than once.
- **Handlers must support out of order notifications.**
  It is possible that notifications will be delivered out of order.
- **Handlers must be able to process a notification for any job.**
  There is no way to guarantee that a notification for a particular job will
  be delivered to a particular worker.
- **Handlers should be short operations.** All of the messages must be
  handled and deleted before the visibility timeout. If the visibility
  timeout is 15 seconds and a maximum of 5 messages will be returned from
  Amazon SQS, each message must be handled and deleted from the queue in less than
  3 seconds. If handling takes longer than this, unprocessed messages will
  time out and be delivered to a different worker.

For Java, Python, and Ruby, we recommend that you consume notifications by polling an
Amazon SQS queue that is subscribed to your notification topic. Since Amazon SQS uses a
long-poll mechanism, polling the Amazon SQS queue gives a scalable method for consuming
job notifications. Amazon SQS also simplifies availability and scaling for when hosts
fail or during times of high load, and generally requires no special ACL setup.

For PHP running in Apache, we recommend that you subscribe your endpoint directly to
the Amazon SNS topic. This requires that your endpoint be publicly available since Amazon SNS will need
to be able to push notifications directly to you.

## Setting Up Your Environment

To run the sample code, you need to have an AWS environment set up. This section
walks you through the setup process, and shows how to create the AWS resources
that Elastic Transcoder needs in order to work optimally.

###### Topics

- [Setting up your Java environment](#env-java "#env-java")
- [Setting up your Ruby environment](#env-ruby "#env-ruby")
- [Setting up your PHP environment](#env-php "#env-php")
- [Setting up your Python environment](#env-python "#env-python")

### Setting up your Java environment

This section walks you through setting up your Java environment.

###### Topics

- [Setting up the AWS SDK for Java](#java-sdk "#java-sdk")
- [Creating Amazon S3 input and output buckets](#java-s3 "#java-s3")
- [Creating an Amazon SNS topic to receive job status notifications](#java-sns "#java-sns")
- [Creating an Amazon SQS queue to poll for job status notifications](#java-sqs "#java-sqs")
- [Subscribing your Amazon SQS queue to your Amazon SNS topic](#java-sqs-subscribe "#java-sqs-subscribe")
- [Creating an Elastic Transcoder pipeline](#java-pipeline "#java-pipeline")
- [Creating an Amazon CloudFront distribution to deliver content in a scalable manner](#java-cloudfront "#java-cloudfront")
- [Modifying the Amazon S3 bucket policy](#java-s3-policy "#java-s3-policy")

The sample code makes two major assumptions:

- Samples are written to work with Java version 1.6 or higher.
- Samples are run using Eclipse with the AWS Toolkit for Eclipse.

#### Setting up the AWS SDK for Java

These samples assume you are using the AWS Toolkit for Eclipse. You
need both the [AWS SDK for Java](http://aws.amazon.com/sdkforjava/ "http://aws.amazon.com/sdkforjava/")
and the following Jackson JSON processor JAR files:

- Jackson Core
- Jackson Databind
- Jackson Annotations

The Jackson JSON processor handles job status notifications.

Alternatively, if you are using Maven to manage your dependencies, you can
add the following snippets to your `pom.xml` file:

Version property:

```
    <jackson-2-version>2.2.3</jackson-2-version>
```

Dependencies:

```
    <dependency>
        <groupId>com.amazonaws</groupId>
        <artifactId>aws-java-sdk</artifactId>
        <version>LATEST</version>
    </dependency>

    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-core</artifactId>
        <version>${jackson-2-version}</version>
    </dependency>

    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-annotations</artifactId>
        <version>${jackson-2-version}</version>
    </dependency>

    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
        <version>${jackson-2-version}</version>
    </dependency>
```

For more information, see the [AWS
SDK for Java Documentation](https://aws.amazon.com/documentation/sdkforjava/ "https://aws.amazon.com/documentation/sdkforjava/").

#### Creating Amazon S3 input and output buckets

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/home "https://console.aws.amazon.com/s3/home").
2. In the console, click **Create Bucket**.
3. In the **Bucket Name** field, enter the desired name for your input bucket.
4. Still in the Amazon S3 console, click **Create Bucket** again.
5. In the **Bucket Name** field, enter the desired name for your output bucket.

#### Creating an Amazon SNS topic to receive job status notifications

1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the console, click **Create and Add** and select **Create New Topic**.
3. In the **Topic Name** field, enter `ets-sample-topic` and then click **Create Topic**.
4. Record the ARN of `ets-sample-topic`.

#### Creating an Amazon SQS queue to poll for job status notifications

1. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/home "https://console.aws.amazon.com/sqs/home").
2. In the console, click **Create New Queue**.
3. In the **Queue Name** field, enter `ets-sample-queue` and then click **Create Queue**.
4. Record the Amazon SQS queue URL.

#### Subscribing your Amazon SQS queue to your Amazon SNS topic

1. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/home "https://console.aws.amazon.com/sqs/home").
2. In the console, select **ets-sample-queue** from the list of queues.
3. Under **Queue Actions**, select **Subscribe Queue to Amazon SNS Topic**.
4. Under **Choose a Topic**, select **ets-sample-topic** and then click **Subscribe**.

You should see a confirmation that your queue has been successfully subscribed to your topic.

#### Creating an Elastic Transcoder pipeline

1. Open the [Amazon Elastic Transcoder console](https://console.aws.amazon.com/elastictranscoder/home "https://console.aws.amazon.com/elastictranscoder/home").
2. In the console, click **Create New Pipeline**.
3. In the **Pipeline Name** field, enter `ets-sample-pipeline`.
4. In the **Input Bucket** field, enter the name of your input bucket.
5. Leave **IAM Role** as `Console Default Role`.
6. In **Configure Amazon S3 Bucket for Transcoded Files and Playlists**, enter the name of your output bucket.
7. Still in **Configure Amazon S3 Bucket for Transcoded Files and Playlists**, select the **standard storage class**.
8. Expand the **Notifications** drop-down menu.
9. For all four event types, select **Use an existing SNS topic**,
   and under **Select a Topic**, select `ets-sample-topic`.
10. Click **Create Pipeline**.
11. Record the Elastic Transcoder pipeline ID.

#### Creating an Amazon CloudFront distribution to deliver content in a scalable manner

1. Open the [Amazon CloudFront console](https://console.aws.amazon.com/cloudfront/home "https://console.aws.amazon.com/cloudfront/home").
2. In the navigation pane of the console, expand **Private Content**
   and then click **Origin Access Identity**.
3. Click **Create Origin Access Identity**.
4. Click **Create**.
5. Record the Amazon S3 canonical user ID that is generated when you create your origin access identity.
6. In the navigation pane, click **Distribution**.
7. Click **Create Distribution**.
8. Select **Web** and then click **Continue**.
9. Under **Origin Settings**, enter your Amazon S3 output bucket as the **Origin Domain Name**.
10. In the **Origin ID** field, enter `S3-transcoder-sample-output`.
11. For **Restrict Bucket Access**, select **Yes**.
12. Click **Create Distribution**, and record the domain name of the distribution.

#### Modifying the Amazon S3 bucket policy

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/home "https://console.aws.amazon.com/s3/home").
2. Next to the output bucket, click the **magnifying glass icon** to
   bring up the bucket properties.
3. Expand **Permissions** and click **Add bucket policy**.
4. Enter the following policy statement, replacing **CloudFront-oai-s3-canonical-user-id**
   with `your recorded Amazon S3 canonical user ID` and **s3-output-bucket-name**
   with `the name of your output bucket`.
5. Click **Save**.

```
{
  "Version":"2012-10-17",
  "Id":"PolicyForCloudFrontPrivateContent",
  "Statement":[{
     "Sid":" Granting CloudFront OAI access to private content",
     "Effect":"Allow",
     "Principal":{ "CanonicalUser":"<CloudFront-oai-s3-canonical-user-id>" },
     "Action":"s3:GetObject",
     "Resource":"arn:aws:s3:::<s3-output-bucket-name>/*"
   }]
}

```

Skip to the [Java Samples](#java-sample "#java-sample").

### Setting up your Ruby environment

This section walks you through setting up your Ruby environment.

###### Topics

- [Setting up the AWS SDK for Ruby](#ruby-sdk "#ruby-sdk")
- [Creating Amazon S3 input and output buckets](#ruby-s3 "#ruby-s3")
- [Creating an Amazon SNS topic to receive job status notifications](#ruby-sns "#ruby-sns")
- [Creating an Amazon SQS queue to poll for job status notifications](#ruby-sqs "#ruby-sqs")
- [Subscribing your Amazon SQS queue to your Amazon SNS topic](#ruby-sqs-subscribe "#ruby-sqs-subscribe")
- [Creating an Elastic Transcoder pipeline](#ruby-pipeline "#ruby-pipeline")
- [Creating an Amazon CloudFront distribution to deliver content in a scalable manner](#ruby-cloudfront "#ruby-cloudfront")
- [Modifying the Amazon S3 bucket policy](#ruby-s3-policy "#ruby-s3-policy")

The sample code makes one major assumption:

- Samples are written to be compatible with Ruby version 1.9.

#### Setting up the AWS SDK for Ruby

The AWS SDK for Ruby is available [here](http://aws.amazon.com/sdkforruby/ "http://aws.amazon.com/sdkforruby/").
You can install it easily using Ruby gems with the following command:

```
gem install aws-sdk
```

For more information, see the [AWS
SDK for Ruby Documentation](https://aws.amazon.com/documentation/sdkforruby/ "https://aws.amazon.com/documentation/sdkforruby/").

#### Creating Amazon S3 input and output buckets

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/home "https://console.aws.amazon.com/s3/home").
2. In the console, click **Create Bucket**.
3. In the **Bucket Name** field, enter the desired name for your input bucket.
4. Still in the Amazon S3 console, click **Create Bucket** again.
5. In the **Bucket Name** field, enter the desired name for your output bucket.

#### Creating an Amazon SNS topic to receive job status notifications

1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the console, click **Create and Add** and select **Create New Topic**.
3. In the **Topic Name** field, enter `ets-sample-topic` and then click **Create Topic**.
4. Record the ARN of `ets-sample-topic`.

#### Creating an Amazon SQS queue to poll for job status notifications

1. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/home "https://console.aws.amazon.com/sqs/home").
2. In the console, click **Create New Queue**.
3. In the **Queue Name** field, enter `ets-sample-queue` and then click **Create Queue**.
4. Record the Amazon SQS queue URL.

#### Subscribing your Amazon SQS queue to your Amazon SNS topic

1. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/home "https://console.aws.amazon.com/sqs/home").
2. In the console, select **ets-sample-queue** from the list of queues.
3. Under **Queue Actions**, select **Subscribe Queue to Amazon SNS Topic**.
4. Under **Choose a Topic**, select **ets-sample-topic** and then click **Subscribe**.

You should see a confirmation that your queue has been successfully subscribed to your topic.

#### Creating an Elastic Transcoder pipeline

1. Open the [Amazon Elastic Transcoder console](https://console.aws.amazon.com/elastictranscoder/home "https://console.aws.amazon.com/elastictranscoder/home").
2. In the console, click **Create New Pipeline**.
3. In the **Pipeline Name** field, enter `ets-sample-pipeline`.
4. In the **Input Bucket** field, enter the name of your input bucket.
5. Leave **IAM Role** as `Console Default Role`.
6. In **Configure Amazon S3 Bucket for Transcoded Files and Playlists**, enter the name of your output bucket.
7. Still in **Configure Amazon S3 Bucket for Transcoded Files and Playlists**, select the **standard storage class**.
8. Expand the **Notifications** drop-down menu.
9. For all four event types, select **Use an existing SNS topic**,
   and under **Select a Topic**, select `ets-sample-topic`.
10. Click **Create Pipeline**.
11. Record the Elastic Transcoder pipeline ID.

#### Creating an Amazon CloudFront distribution to deliver content in a scalable manner

1. Open the [Amazon CloudFront console](https://console.aws.amazon.com/cloudfront/home "https://console.aws.amazon.com/cloudfront/home").
2. In the navigation pane of the console, expand **Private Content**
   and then click **Origin Access Identity**.
3. Click **Create Origin Access Identity**.
4. Click **Create**.
5. Record the Amazon S3 canonical user ID that is generated when you create your origin access identity.
6. In the navigation pane, click **Distribution**.
7. Click **Create Distribution**.
8. Select **Web** and then click **Continue**.
9. Under **Origin Settings**, enter your Amazon S3 output bucket as the **Origin Domain Name**.
10. In the **Origin ID** field, enter `S3-transcoder-sample-output`.
11. For **Restrict Bucket Access**, select **Yes**.
12. Click **Create Distribution**, and record the domain name of the distribution.

#### Modifying the Amazon S3 bucket policy

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/home "https://console.aws.amazon.com/s3/home").
2. Next to the output bucket, click the **magnifying glass icon** to
   bring up the bucket properties.
3. Expand **Permissions** and click **Add bucket policy**.
4. Enter the following policy statement, replacing **CloudFront-oai-s3-canonical-user-id**
   with `your recorded Amazon S3 canonical user ID` and **s3-output-bucket-name**
   with `the name of your output bucket`.
5. Click **Save**.

```
{
  "Version":"2012-10-17",
  "Id":"PolicyForCloudFrontPrivateContent",
  "Statement":[{
     "Sid":" Granting CloudFront OAI access to private content",
     "Effect":"Allow",
     "Principal":{ "CanonicalUser":"<CloudFront-oai-s3-canonical-user-id>" },
     "Action":"s3:GetObject",
     "Resource":"arn:aws:s3:::<s3-output-bucket-name>/*"
   }]
}

```

Skip to the [Ruby Samples](#ruby-sample "#ruby-sample").

### Setting up your PHP environment

This section walks you through setting up your PHP environment.

###### Topics

- [Installing the sample code](#php-install "#php-install")
- [Setting up the AWS SDK for PHP](#php-sdk "#php-sdk")
- [Creating Amazon S3 input and output buckets](#php-s3 "#php-s3")
- [Creating Amazon SNS topic to receive job status notifications](#php-sns "#php-sns")
- [Subscribing your server to Amazon SNS](#php-sns-sub "#php-sns-sub")
- [Creating an Elastic Transcoder pipeline](#php-pipeline "#php-pipeline")
- [Creating Amazon CloudFront distribution to deliver content in a scalable manner](#php-cloudfront "#php-cloudfront")
- [Modifying the Amazon S3 bucket policy](#php-s3-policy "#php-s3-policy")

The sample code makes three major assumptions:

- PHP samples are run inside an Apache server.
- Apache server must be able to take input from the internet to receive Amazon SNS notifications.
- Samples are written to work with PHP version 5.4 or higher.

#### Installing the sample code

To use the PHP sample code, you must first download and install it.

- Download the sample code:
  - [HLS Sample Code](samples/phphls.md "samples/phphls.md").
  - [Notification Sample Code](samples/phpnotification.md "samples/phpnotification.md").

- Unzip the sample code.
- Place the code under your Apache server's DocumentRoot.
- Remove the downloaded sample code .zip file.
- Update the path to your AWS SDK Installation.

###### Note

In `HlsJobCreationSample.php` and `JobStatusNotificationsSample.php`, you need to
update the path to your `autoload.php`. If you use the phar installation, you
can use the path to the `aws.phar` file that you downloaded, which includes
all necessary dependencies.

#### Setting up the AWS SDK for PHP

You can find the AWS SDK for PHP [here](http://aws.amazon.com/sdkforphp/ "http://aws.amazon.com/sdkforphp/").
For this tutorial, we recommend the phar installation; however,
long-term projects are better managed using composer.

For more information, see the [AWS
SDK for PHP Documentation](https://aws.amazon.com/documentation/sdkforphp/ "https://aws.amazon.com/documentation/sdkforphp/").

#### Creating Amazon S3 input and output buckets

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/home "https://console.aws.amazon.com/s3/home").
2. In the console, click **Create Bucket**.
3. In the **Bucket Name** field, enter the desired name for your input bucket.
4. Still in the Amazon S3 console, click **Create Bucket** again.
5. In the **Bucket Name** field, enter the desired name for your output bucket.

#### Creating Amazon SNS topic to receive job status notifications

1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the console, click **Create and Add** and select **Create New Topic**.
3. In the **Topic Name** field, enter `ets-sample-topic` and then click **Create Topic**.
4. Record the ARN of `ets-sample-topic`.

#### Subscribing your server to Amazon SNS

1. Verify that the PHP sample code has been installed.
2. Open the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
3. Under **AdditionalActions**, click **Create Subscription**.
4. Select HTTP or HTTPS based on your server's configuration.
5. In **Endpoint**, enter the endpoint of your server. The path of the endpoint
   should point to `JobStatusNotificationsSampleNotificationHandler.php`.
6. Click **Subscribe**. This sends a subscription request to your PHP endpoint.

The PHP sample code automatically handles the subscription request and confirms
a subscription. The subscription request and response are written to `/tmp/subscribe_requests.txt`.

#### Creating an Elastic Transcoder pipeline

1. Open the [Amazon Elastic Transcoder console](https://console.aws.amazon.com/elastictranscoder/home "https://console.aws.amazon.com/elastictranscoder/home").
2. In the console, click **Create New Pipeline**.
3. In the **Pipeline Name** field, enter `ets-sample-pipeline`.
4. In the **Input Bucket** field, enter the name of your input bucket.
5. Leave **IAM Role** as `Console Default Role`.
6. In **Configure Amazon S3 Bucket for Transcoded Files and Playlists**, enter the name of your output bucket.
7. Still in **Configure Amazon S3 Bucket for Transcoded Files and Playlists**, select the **standard storage class**.
8. Expand the **Notifications** drop-down menu.
9. For all four event types, select **Use an existing SNS topic**,
   and under **Select a Topic**, select `ets-sample-topic`.
10. Click **Create Pipeline**.
11. Record the Elastic Transcoder pipeline ID.

#### Creating Amazon CloudFront distribution to deliver content in a scalable manner

1. Open the [Amazon CloudFront console](https://console.aws.amazon.com/cloudfront/home "https://console.aws.amazon.com/cloudfront/home").
2. In the navigation pane of the console, expand **Private Content**
   and then click **Origin Access Identity**.
3. Click **Create Origin Access Identity**.
4. Click **Create**.
5. Record the Amazon S3 canonical user ID that is generated when you create your origin access identity.
6. In the navigation pane, click **Distribution**.
7. Click **Create Distribution**.
8. Select **Web** and then click **Continue**.
9. Under **Origin Settings**, enter your Amazon S3 output bucket as the **Origin Domain Name**.
10. In the **Origin ID** field, enter `S3-transcoder-sample-output`.
11. For **Restrict Bucket Access**, select **Yes**.
12. Click **Create Distribution**, and record the domain name of the distribution.

#### Modifying the Amazon S3 bucket policy

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/home "https://console.aws.amazon.com/s3/home").
2. Next to the output bucket, click the **magnifying glass icon** to
   bring up the bucket properties.
3. Expand **Permissions** and click **Add bucket policy**.
4. Enter the following policy statement, replacing **CloudFront-oai-s3-canonical-user-id**
   with `your recorded Amazon S3 canonical user ID` and **s3-output-bucket-name**
   with `the name of your output bucket`.
5. Click **Save**.

```
{
  "Version":"2012-10-17",
  "Id":"PolicyForCloudFrontPrivateContent",
  "Statement":[{
     "Sid":" Granting CloudFront OAI access to private content",
     "Effect":"Allow",
     "Principal":{ "CanonicalUser":"<CloudFront-oai-s3-canonical-user-id>" },
     "Action":"s3:GetObject",
     "Resource":"arn:aws:s3:::<s3-output-bucket-name>/*"
   }]
}

```

Skip to the [PHP Samples](#php-sample "#php-sample").

### Setting up your Python environment

This section walks you through setting up your Python environment.

###### Topics

- [Setting up the AWS SDK for Python](#python-sdk "#python-sdk")
- [Creating Amazon S3 input and output buckets](#python-s3 "#python-s3")
- [Creating Amazon SNS topic to receive job status notifications](#python-sns "#python-sns")
- [Creating Amazon SQS queue to poll for job status notifications](#python-sqs "#python-sqs")
- [Subscribing your Amazon SQS queue to your Amazon SNS topic](#python-sqs-subscribe "#python-sqs-subscribe")
- [Creating an Elastic Transcoder pipeline](#python-pipeline "#python-pipeline")
- [Creating Amazon CloudFront distribution to deliver content in a scalable manner](#python-cloudfront "#python-cloudfront")
- [Modifying the Amazon S3 bucket policy](#python-s3-policy "#python-s3-policy")

It makes one major assumption:

- Samples are written to be compatible with Python version 2.7.

#### Setting up the AWS SDK for Python

You can find the AWS SDK for Python [here](http://aws.amazon.com/sdkforpython/ "http://aws.amazon.com/sdkforpython/").
You can also install it easily by using PIP with the following command:

```
pip-2.7 install boto
```

For more information, see the [AWS
SDK for Python Documentation](http://docs.pythonboto.org/en/latest/ "http://docs.pythonboto.org/en/latest/").

#### Creating Amazon S3 input and output buckets

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/home "https://console.aws.amazon.com/s3/home").
2. In the console, click **Create Bucket**.
3. In the **Bucket Name** field, enter the desired name for your input bucket.
4. Still in the Amazon S3 console, click **Create Bucket** again.
5. In the **Bucket Name** field, enter the desired name for your output bucket.

#### Creating Amazon SNS topic to receive job status notifications

1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the console, click **Create and Add** and select **Create New Topic**.
3. In the **Topic Name** field, enter `ets-sample-topic` and then click **Create Topic**.
4. Record the ARN of `ets-sample-topic`.

#### Creating Amazon SQS queue to poll for job status notifications

1. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/home "https://console.aws.amazon.com/sqs/home").
2. In the console, click **Create New Queue**.
3. In the **Queue Name** field, enter `ets-sample-queue` and then click **Create Queue**.
4. Record the Amazon SQS queue URL.

#### Subscribing your Amazon SQS queue to your Amazon SNS topic

1. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/home "https://console.aws.amazon.com/sqs/home").
2. In the console, select **ets-sample-queue** from the list of queues.
3. Under **Queue Actions**, select **Subscribe Queue to Amazon SNS Topic**.
4. Under **Choose a Topic**, select **ets-sample-topic** and then click **Subscribe**.

You should see a confirmation that your queue has been successfully subscribed to your topic.

#### Creating an Elastic Transcoder pipeline

1. Open the [Amazon Elastic Transcoder console](https://console.aws.amazon.com/elastictranscoder/home "https://console.aws.amazon.com/elastictranscoder/home").
2. In the console, click **Create New Pipeline**.
3. In the **Pipeline Name** field, enter `ets-sample-pipeline`.
4. In the **Input Bucket** field, enter the name of your input bucket.
5. Leave **IAM Role** as `Console Default Role`.
6. In **Configure Amazon S3 Bucket for Transcoded Files and Playlists**, enter the name of your output bucket.
7. Still in **Configure Amazon S3 Bucket for Transcoded Files and Playlists**, select the **standard storage class**.
8. Expand the **Notifications** drop-down menu.
9. For all four event types, select **Use an existing SNS topic**,
   and under **Select a Topic**, select `ets-sample-topic`.
10. Click **Create Pipeline**.
11. Record the Elastic Transcoder pipeline ID.

#### Creating Amazon CloudFront distribution to deliver content in a scalable manner

1. Open the [Amazon CloudFront console](https://console.aws.amazon.com/cloudfront/home "https://console.aws.amazon.com/cloudfront/home").
2. In the navigation pane of the console, expand **Private Content**
   and then click **Origin Access Identity**.
3. Click **Create Origin Access Identity**.
4. Click **Create**.
5. Record the Amazon S3 canonical user ID that is generated when you create your origin access identity.
6. In the navigation pane, click **Distribution**.
7. Click **Create Distribution**.
8. Select **Web** and then click **Continue**.
9. Under **Origin Settings**, enter your Amazon S3 output bucket as the **Origin Domain Name**.
10. In the **Origin ID** field, enter `S3-transcoder-sample-output`.
11. For **Restrict Bucket Access**, select **Yes**.
12. Click **Create Distribution**, and record the domain name of the distribution.

#### Modifying the Amazon S3 bucket policy

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/home "https://console.aws.amazon.com/s3/home").
2. Next to the output bucket, click the **magnifying glass icon** to
   bring up the bucket properties.
3. Expand **Permissions** and click **Add bucket policy**.
4. Enter the following policy statement, replacing **CloudFront-oai-s3-canonical-user-id**
   with `your recorded Amazon S3 canonical user ID` and **s3-output-bucket-name**
   with `the name of your output bucket`.
5. Click **Save**.

```
{
  "Version":"2012-10-17",
  "Id":"PolicyForCloudFrontPrivateContent",
  "Statement":[{
     "Sid":" Granting CloudFront OAI access to private content",
     "Effect":"Allow",
     "Principal":{ "CanonicalUser":"<CloudFront-oai-s3-canonical-user-id>" },
     "Action":"s3:GetObject",
     "Resource":"arn:aws:s3:::<s3-output-bucket-name>/*"
   }]
}

```

Skip to the [Python Samples](#python-sample "#python-sample").

## Java Samples

All Java samples make two assumptions:

- Samples are written to work with Java version 1.6 or higher.
- Samples are run using Eclipse with the AWS Toolkit for Eclipse.

### HLS Samples

###### Topics

- [Java HLS Sample Download](#java-hls-link "#java-hls-link")
- [Sample Code Pieces](#java-hls-list "#java-hls-list")
- [Tasks](#java-hls-tasklist "#java-hls-tasklist")

This sample shows you how to create an HLS job and an HLS playlist file that
can be used to play an adaptive bit rate stream.

#### Java HLS Sample Download

You can download the sample code [here](samples/javasamples.md "samples/javasamples.md").

#### Sample Code Pieces

The Java code sample includes:

- The class `HlsJobCreationSample`

#### Tasks

To run the sample, follow these steps:

1. Set up your environment according to these instructions:
   [Setting up your Java environment](#env-java "#env-java")
2. Download the sample code.
3. In Eclipse, open `com/amazonaws/services/elastictranscoder/samples/HlsJobCreationSample.java`.
4. Replace PIPELINE_ID and INPUT_KEY with the appropriate values.
5. Run the samples in Eclipse.

### Notification Samples

###### Topics

- [Example of Notification Syntax](#java-notification-example "#java-notification-example")
- [Java Notification Sample Download](#java-link "#java-link")
- [Sample Code Pieces](#java-list "#java-list")
- [Tasks](#java-tasklist "#java-tasklist")

#### Example of Notification Syntax

```
{
   "Type" : "Notification",
   "MessageId" : "341527b6-9081-5f3d-b933-6c8472c3be40",
   "TopicArn" : "arn:aws:sns:us-east-1:123456789012:ets-sample-topic",
   "Subject" : "Amazon Elastic Transcoder has scheduled job 1387847681009
      -abcdef for transcoding.",
   "Message" : "{\n  \"state\" : \"PROGRESSING\",\n
      \"version\" : \"2012-09-25\",\n  \"jobId\" : \"1387847681009-abcdef\",
      \n \"pipelineId\" : \"1387847629327-fedcba\",\n  \"input\" : {\n
      \"key\" : \"input/example/key.mp4\",\n \"frameRate\" : \"auto\",\n
      \"resolution\" : \"auto\",\n  \"aspectRatio\" : \"auto\",\n
      \"interlaced\" : \"auto\",\n  \"container\" : \"auto\"\n  },\n
      \"outputKeyPrefix\" : \"elastic-transcoder-samples/\",\n
      \"outputs\" : [ {\n \"id\" : \"1\",\n \"presetId\" :
      \"1351620000001-000020\",\n \"key\" : \"output/example/key.mp4\",\n
      \"thumbnailPattern\" : \"\",\n \"rotate\" : \"auto\",\n \"status\" :
      \"Progressing\"\n  } ]\n}",
   "Timestamp" : "2013-12-24T01:14:42.493Z",
   "SignatureVersion" : "1",
   "Signature" : "ElSqJW3ZksCPViYGTayI/p+LjdF2HB42iJlIJRJ+jWzWwygXdiJXvZXl94qhd/tLln1lxPqijjivb5RWu7n5yzdZwbod6lpLwyZ2TfWM6dZt57OzsG3GbdTxgqwVsztVSyWCYhcV8f+CrT3IQrfrU3Me/SRYVUqrSUXXsu4Ls7A2q9mosG7v0Sn+3Z1rAa9+Rf6QmkfAg05UX0sLyA+I2hFqTu5oAGDK4Cm6FHuIwV+oYJXNBbGWuS7tD6mRNwrYvPBlUvBLXx9m3CbqSXv5Yoj39vglv+1djtaLA3GpwX+B1hHx8QT373lgmmsmGDRWhSQretpOTWDYb81PV2K0bg==",
   "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-e372f8ca30337fdb084e8ac449342c77.pem",
   "UnsubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=
      Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789012:ets-
      sample-topic:b3ec47e5-e1f0-401f-a0a5-98c7fe405c2b"
 }
```

#### Java Notification Sample Download

You can download the sample code [here](samples/javasamples.md "samples/javasamples.md").

#### Sample Code Pieces

The Java code sample includes:

- The class `Notification`: To consume notifications from Java, we
  use the Jackson JSON library to deserialize job status notifications
  into POJOs. The `Notification` class models the message we get back from
  the Amazon SQS queue.
- The class `JobStatusNotification`: The `JobStatusNotification` class
  models an Elastic Transcoder notification.
- The class `SqsQueueNotificationWorker`: The `SqsQueueNotificationWorker`
  class can be started in a separate thread to poll Amazon SQS and handle job
  status notifications. This class receives messages, calls all
  registered handlers for each notification received, and deletes the
  message from the queue.
- The interface `JobStatusNotificationHandler`: The
  `JobStatusNotificationHandler` interface can be implemented to allow custom
  handling for notifications.
- The class `JobStatusNotificationsSample`: The
  `JobStatusNotificationsSample` class creates a job and waits for it to
  complete. When the job goes into a terminal state, the queue worker
  shuts down and the application exits.

#### Tasks

To run the sample, follow these steps:

1. Set up your environment according to these instructions:
   [Setting up your Java environment](#env-java "#env-java").
2. Download the sample code.
3. Unzip the sample code into your JAVA project's source directory.
4. Open `com/amazonaws/services/elastictranscoder/samples/JobStatusNotificationsSample.java` in Eclipse.
5. Replace PIPELINE_ID, SQS_QUEUE_URL, and INPUT_KEY with the appropriate values.
6. Run the sample in Eclipse.

## Ruby Samples

All Ruby samples make one major assumption:

- Samples are written to be compatible with Ruby version 1.9.

### HLS Samples

###### Topics

- [Ruby HLS Sample Download](#ruby-hls-link "#ruby-hls-link")
- [Sample Code Pieces](#ruby-hls-list "#ruby-hls-list")
- [Tasks](#ruby-hls-tasklist "#ruby-hls-tasklist")

This sample shows you how to create an HLS job and an HLS playlist file that
can be used to play an adaptive bit rate stream.

#### Ruby HLS Sample Download

You can download the sample code
[here](samples/rubyhls.md "samples/rubyhls.md").

#### Sample Code Pieces

The Ruby sample code includes:

- The `HlsJobCreationSample.rb` file

#### Tasks

To run the sample, follow these steps:

1. Set up your environment according to these instructions:
   [Setting up your Ruby environment](#env-ruby "#env-ruby")
2. Download the sample code.
3. Unzip the sample code into your Ruby project's source directory.
4. Edit `HlsJobCreationSample.rb` and replace
   pipeline_id and input_key with the appropriate values.
5. From a terminal, navigate to the directory where you unzipped the sample code and run:

```
$ruby HlsJobCreationSample.rb
```

### Notification Samples

###### Topics

- [Example of Notification Syntax](#ruby-notification-example "#ruby-notification-example")
- [Ruby Notification Sample Download](#ruby-link "#ruby-link")
- [Sample Code Pieces](#ruby-list "#ruby-list")
- [Tasks](#ruby-tasklist "#ruby-tasklist")

#### Example of Notification Syntax

```
{
   "Type" : "Notification",
   "MessageId" : "341527b6-9081-5f3d-b933-6c8472c3be40",
   "TopicArn" : "arn:aws:sns:us-east-1:123456789012:ets-sample-topic",
   "Subject" : "Amazon Elastic Transcoder has scheduled job 1387847681009
      -abcdef for transcoding.",
   "Message" : "{\n  \"state\" : \"PROGRESSING\",\n
      \"version\" : \"2012-09-25\",\n  \"jobId\" : \"1387847681009-abcdef\",
      \n \"pipelineId\" : \"1387847629327-fedcba\",\n  \"input\" : {\n
      \"key\" : \"input/example/key.mp4\",\n \"frameRate\" : \"auto\",\n
      \"resolution\" : \"auto\",\n  \"aspectRatio\" : \"auto\",\n
      \"interlaced\" : \"auto\",\n  \"container\" : \"auto\"\n  },\n
      \"outputKeyPrefix\" : \"elastic-transcoder-samples/\",\n
      \"outputs\" : [ {\n \"id\" : \"1\",\n \"presetId\" :
      \"1351620000001-000020\",\n \"key\" : \"output/example/key.mp4\",\n
      \"thumbnailPattern\" : \"\",\n \"rotate\" : \"auto\",\n \"status\" :
      \"Progressing\"\n  } ]\n}",
   "Timestamp" : "2013-12-24T01:14:42.493Z",
   "SignatureVersion" : "1",
   "Signature" : "ElSqJW3ZksCPViYGTayI/p+LjdF2HB42iJlIJRJ+jWzWwygXdiJXvZXl94qhd/tLln1lxPqijjivb5RWu7n5yzdZwbod6lpLwyZ2TfWM6dZt57OzsG3GbdTxgqwVsztVSyWCYhcV8f+CrT3IQrfrU3Me/SRYVUqrSUXXsu4Ls7A2q9mosG7v0Sn+3Z1rAa9+Rf6QmkfAg05UX0sLyA+I2hFqTu5oAGDK4Cm6FHuIwV+oYJXNBbGWuS7tD6mRNwrYvPBlUvBLXx9m3CbqSXv5Yoj39vglv+1djtaLA3GpwX+B1hHx8QT373lgmmsmGDRWhSQretpOTWDYb81PV2K0bg==",
   "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-e372f8ca30337fdb084e8ac449342c77.pem",
   "UnsubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=
      Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789012:ets-
      sample-topic:b3ec47e5-e1f0-401f-a0a5-98c7fe405c2b"
 }
```

#### Ruby Notification Sample Download

You can download the sample code [here](samples/rubynotification.md "samples/rubynotification.md").

#### Sample Code Pieces

The Ruby sample code includes:

- The class `SqsQueueNotificationWorker`: The `SqsQueueNotificationWorker`
  class polls Amazon SQS for notifications, calls all registered handlers for
  each notification, and deletes the message from the queue. Note that the
  worker runs in a separate thread. If the Ruby implementation used has
  "green" threads, then only a single thread runs at a time (no true
  multiprocessing).
- The script `JobStatusNotificationsSample.rb`: This script creates
  an Elastic Transcoder job, starts an Amazon SQS worker and waits for the job to
  complete. The provided handler tells the Amazon SQS worker to stop when the
  created job's processing is complete. Handling notifications is done by
  calling the add_handlers method and providing a Proc or lambda as a handler
  that takes a single argument. For each notification received, all
  registered handlers are called with the notification provided as the input
  argument to the handler.

#### Tasks

To run the sample, follow these steps:

1. Set up your environment according to these instructions:
   [Setting up your Ruby environment](#env-ruby "#env-ruby")
2. Download the sample code.
3. Unzip the sample code into your Ruby project's source directory.
4. Edit `JobStatusNotificationsSample.rb` and
   replace pipeline_id, sqs_queue_url, and input_key with the appropriate values.
5. From a terminal, navigate to the directory where you unzipped the sample code and run:

```
$ruby JobStatusNotificationsSample.rb
```

## PHP Samples

All PHP samples make three major assumptions:

- PHP samples are run inside an Apache server.
- Apache server must be able to take input from the Internet to receive Amazon SNS notifications.
- Samples are written to work with PHP version 5.4 or higher.

### HLS Samples

###### Topics

- [PHP HLS Sample Download](#php-hls-link "#php-hls-link")
- [Sample Code Pieces](#php-hls-list "#php-hls-list")
- [Tasks](#php-hls-tasklist "#php-hls-tasklist")

This sample shows you how to create an HLS job and an HLS playlist file that
can be used to play an adaptive bit rate stream.

#### PHP HLS Sample Download

You can download the sample code
[here](samples/phphls.md "samples/phphls.md").

#### Sample Code Pieces

The PHP sample code includes:

- The `HlsJobCreationSample.php` file

#### Tasks

To run the sample, follow these steps:

1. Set up your environment according to these instructions:
   [Setting up your PHP environment](#env-php "#env-php")
2. Download the sample code.
3. In your browser, load the page http://<your-endpoint>/transcoder-samples/HlsJobCreationSample.php.
4. Fill in the pipeline ID and input key and submit the form to create a job.

### Notification Samples

###### Topics

- [Example of Notification Syntax](#php-notification-example "#php-notification-example")
- [PHP Notification Sample Download](#php-link "#php-link")
- [Sample Code Pieces](#php-list "#php-list")
- [Tasks](#php-tasklist "#php-tasklist")

#### Example of Notification Syntax

```
{
   "Type" : "Notification",
   "MessageId" : "341527b6-9081-5f3d-b933-6c8472c3be40",
   "TopicArn" : "arn:aws:sns:us-east-1:123456789012:ets-sample-topic",
   "Subject" : "Amazon Elastic Transcoder has scheduled job 1387847681009
      -abcdef for transcoding.",
   "Message" : "{\n  \"state\" : \"PROGRESSING\",\n
      \"version\" : \"2012-09-25\",\n  \"jobId\" : \"1387847681009-abcdef\",
      \n \"pipelineId\" : \"1387847629327-fedcba\",\n  \"input\" : {\n
      \"key\" : \"input/example/key.mp4\",\n \"frameRate\" : \"auto\",\n
      \"resolution\" : \"auto\",\n  \"aspectRatio\" : \"auto\",\n
      \"interlaced\" : \"auto\",\n  \"container\" : \"auto\"\n  },\n
      \"outputKeyPrefix\" : \"elastic-transcoder-samples/\",\n
      \"outputs\" : [ {\n \"id\" : \"1\",\n \"presetId\" :
      \"1351620000001-000020\",\n \"key\" : \"output/example/key.mp4\",\n
      \"thumbnailPattern\" : \"\",\n \"rotate\" : \"auto\",\n \"status\" :
      \"Progressing\"\n  } ]\n}",
   "Timestamp" : "2013-12-24T01:14:42.493Z",
   "SignatureVersion" : "1",
   "Signature" : "ElSqJW3ZksCPViYGTayI/p+LjdF2HB42iJlIJRJ+jWzWwygXdiJXvZXl94qhd/tLln1lxPqijjivb5RWu7n5yzdZwbod6lpLwyZ2TfWM6dZt57OzsG3GbdTxgqwVsztVSyWCYhcV8f+CrT3IQrfrU3Me/SRYVUqrSUXXsu4Ls7A2q9mosG7v0Sn+3Z1rAa9+Rf6QmkfAg05UX0sLyA+I2hFqTu5oAGDK4Cm6FHuIwV+oYJXNBbGWuS7tD6mRNwrYvPBlUvBLXx9m3CbqSXv5Yoj39vglv+1djtaLA3GpwX+B1hHx8QT373lgmmsmGDRWhSQretpOTWDYb81PV2K0bg==",
   "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-e372f8ca30337fdb084e8ac449342c77.pem",
   "UnsubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=
      Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789012:ets-
      sample-topic:b3ec47e5-e1f0-401f-a0a5-98c7fe405c2b"
 }
```

#### PHP Notification Sample Download

You can download the sample code [here](samples/phpnotification.md "samples/phpnotification.md").

#### Sample Code Pieces

The PHP sample code includes:

- The file `JobStatusNotificationsSampleNotificationHandler.php`: When
  a notification is POSTed to your server, the notification handler
  writes the status back to a file under /tmp/<job-id>.
- The file `JobStatusNotificationsSample.php`: Once the notification
  handler writes the status back to a file under /tmp/<job-id>,
  `JobStatusNotificationsSample.php` loads the /tmp/<job-id> status
  file specified by the Id in the query string given to it.

#### Tasks

To run the sample, follow these steps:

1. Set up your environment according to these instructions:
   [Setting up your PHP environment](#env-php "#env-php")
2. Download the sample code.
3. Unzip the sample code into your PHP project's source directory.
4. In your browser, load the page http://<your-endpoint>/transcoder-samples/JobStatusNotificationsSample.php.
5. Fill in the pipeline ID and input key you wish to transcode and press the **Create Job** button.

## Python Samples

All Python samples make one major assumption:

- Samples are written to be compatible with Python version 2.7.

### HLS Samples

###### Topics

- [Python HLS Sample Download](#python-hls-link "#python-hls-link")
- [Sample Code Pieces](#python-hls-list "#python-hls-list")
- [Tasks](#python-hls-tasklist "#python-hls-tasklist")

This sample shows you how to create an HLS job and an HLS playlist file that
can be used to play an adaptive bit rate stream.

#### Python HLS Sample Download

You can download the sample code
[here](samples/pythonhls.md "samples/pythonhls.md").

#### Sample Code Pieces

The Python sample code includes:

- The `HlsJobCreationSample.py` file

#### Tasks

To run the sample, follow these steps:

1. Set up your environment according to these instructions:
   [Setting up your Python environment](#env-python "#env-python")
2. Download the sample code.
3. Unzip the sample code.
4. Edit `HlsJobCreationSample.py` and replace pipeline_id and input_key with the appropriate values.
5. From a terminal, navigate to the directory where you unzipped the sample code and run:

```
$python HlsJobCreationSample.py
```

### Notification Samples

###### Topics

- [Example of Notification Syntax](#python-notification-example "#python-notification-example")
- [Python Notification Sample Download](#python-link "#python-link")
- [Sample Code Pieces](#python-list "#python-list")
- [Tasks](#python-tasklist "#python-tasklist")

#### Example of Notification Syntax

```
{
   "Type" : "Notification",
   "MessageId" : "341527b6-9081-5f3d-b933-6c8472c3be40",
   "TopicArn" : "arn:aws:sns:us-east-1:123456789012:ets-sample-topic",
   "Subject" : "Amazon Elastic Transcoder has scheduled job 1387847681009
      -abcdef for transcoding.",
   "Message" : "{\n  \"state\" : \"PROGRESSING\",\n
      \"version\" : \"2012-09-25\",\n  \"jobId\" : \"1387847681009-abcdef\",
      \n \"pipelineId\" : \"1387847629327-fedcba\",\n  \"input\" : {\n
      \"key\" : \"input/example/key.mp4\",\n \"frameRate\" : \"auto\",\n
      \"resolution\" : \"auto\",\n  \"aspectRatio\" : \"auto\",\n
      \"interlaced\" : \"auto\",\n  \"container\" : \"auto\"\n  },\n
      \"outputKeyPrefix\" : \"elastic-transcoder-samples/\",\n
      \"outputs\" : [ {\n \"id\" : \"1\",\n \"presetId\" :
      \"1351620000001-000020\",\n \"key\" : \"output/example/key.mp4\",\n
      \"thumbnailPattern\" : \"\",\n \"rotate\" : \"auto\",\n \"status\" :
      \"Progressing\"\n  } ]\n}",
   "Timestamp" : "2013-12-24T01:14:42.493Z",
   "SignatureVersion" : "1",
   "Signature" : "ElSqJW3ZksCPViYGTayI/p+LjdF2HB42iJlIJRJ+jWzWwygXdiJXvZXl94qhd/tLln1lxPqijjivb5RWu7n5yzdZwbod6lpLwyZ2TfWM6dZt57OzsG3GbdTxgqwVsztVSyWCYhcV8f+CrT3IQrfrU3Me/SRYVUqrSUXXsu4Ls7A2q9mosG7v0Sn+3Z1rAa9+Rf6QmkfAg05UX0sLyA+I2hFqTu5oAGDK4Cm6FHuIwV+oYJXNBbGWuS7tD6mRNwrYvPBlUvBLXx9m3CbqSXv5Yoj39vglv+1djtaLA3GpwX+B1hHx8QT373lgmmsmGDRWhSQretpOTWDYb81PV2K0bg==",
   "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-e372f8ca30337fdb084e8ac449342c77.pem",
   "UnsubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=
      Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789012:ets-
      sample-topic:b3ec47e5-e1f0-401f-a0a5-98c7fe405c2b"
 }
```

#### Python Notification Sample Download

You can download the sample code [here](samples/pythonnotification.md "samples/pythonnotification.md").

#### Sample Code Pieces

The Python sample code includes:

- The class `SqsQueueNotificationWorker.py`: The
  `SqsQueueNotificationWorker` class polls Amazon SQS and
  handles notifications in a separate process. This allows for true
  multiprocessing in Python.
  This class receives messages, calls all registered handlers for each
  notification received, and deletes the message from the queue. This class
  also includes the definition for the `JobStatusNotificationHandler` class,
  which is provided to give a framework for handling Elastic Transcoder
  notifications. This class can be extended and the handle method overwritten
  to provide custom job handling. Note that this does not follow Pythons
  standards of duck typing, but does give a formal definition of handlers
  for the purposes of this sample.
- The script `JobStatusNotificationSample.py`: The
  `JobStatusNotificationSample.py` script creates a job in Elastic Transcoder
  and waits for it to complete. When the job completes, it
  stops the queue polling process and exits. Cross-process synchronization using the
  multiprocessing value object is necessary, because the handler runs in a
  separate process from the queue it polls.

#### Tasks

To run the sample, follow these steps:

1. Set up your environment according to these instructions:
   [Setting up your Python environment](#env-python "#env-python")
2. Download the sample code.
3. Unzip the sample code to a local folder.
4. Edit `JobStatusNotificationsSample.py` and replace
   pipeline_id, sqs_queue_url, and input_key with the appropriate values.
5. From a terminal, navigate to the directory where you unzipped the sample code and run:

```
$python JobStatusNotificationsSample.py
```

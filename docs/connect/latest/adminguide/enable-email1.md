

# Enable email for your Connect Customer instance
<a name="enable-email1"></a>

This topic is for administrators who have access to the Connect Customer console. It explains how to enable email for your instance using the Connect Customer admin website. For a list of the APIs to enable email programmatically, see [APIs to enable email](#apis-email-setup2). 

When you enable email, you get an auto-generated email domain. Optionally, you can also use custom domains.
+ **Connect Customer email domain**. The email domain is *{{instance-alias}}.email.connect.aws*.
  +  You can use this domain for testing.
  + Or, you can use this email domain to integrate with Connect Customer and start receiving emails into Connect Customer. For example, if you have an email address such as *support@example.com* you can forward email into Connect Customer by using *support@example.email.connect.aws*.
+ **Custom domains**. You can specify up to 5 custom domains that have been [onboarded to Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#just-verify-domain-proc).

## Step 1: Move Amazon SES into production mode
<a name="move-ses-production"></a>

Connect Customer uses Amazon SES for sending and receiving emails. If you have a new Amazon SES instance, you need to take it out of sandbox mode. For instructions, see [Request production access (Moving out of the Amazon SES sandbox)](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html) in the *Amazon SES Developer Guide*. 

After you move Amazon SES into production mode, if you already enabled email when you created your Connect Customer instance, skip to these topics:
+ [(Optional) Step 3: Use your own custom email domains](#use-custom-email)
+ [Step 5: Configure a CORS policy on your attachments bucket](#config-email-attachments-cors1)

## Step 2: Get a default Connect Customer email domain
<a name="get-email-domain"></a>

These steps only apply if you already created a Connect Customer instance but didn't enable email. Complete these steps to get a default email domain from Connect Customer.

1. In the Connect Customer console, on the left navigation menu, choose **Email**, and then choose **Create service role**. This role needs to be created only once for your account. It allows Amazon SES to route emails to Connect Customer.

1.  Choose **Add Domain** as shown in the following image.  
![The Manage email page, the Add domain button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-aws-console1.png)

1. In the **Add email domain** box, choose **Connect Customer email domain**, as shown in the following image. When you choose this option, the name of the domain is auto-generated: *{{instance-alias}}.email.connect.aws*. You cannot change this email address.  
![The Add email domain box, the Connect Customer email domain option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-add-email-domain.png)

## (Optional) Step 3: Use your own custom email domains
<a name="use-custom-email"></a>

You can import up to five custom domains that have been [onboarded to Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#just-verify-domain-proc).

1. In the Connect Customer console, on the left navigation menu, choose **Email**, and then choose **Add Domain** as shown in the following image.  
![The Email channel on the Connect Customer console.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-aws-console.png)

1. Choose **Use custom email domain**. Use the dropdown box to choose custom domains that have been [verified by Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#just-verify-domain-proc).  
![The Use custom email domain option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-add-custom-domain.png)

## Step 4: Enable email and create an Amazon S3 bucket for storing email and attachments
<a name="enable-email-buckets"></a>

These steps apply only if you already created a Connect Customer instance but didn't enable email.

You need to update your **Data storage** settings to enable the email channel and specify the Amazon S3 bucket where email messages and attachments are to be stored. Email requires two Amazon S3 bucket pointers. They can be to the same Amazon S3 bucket or two different buckets.

**Important**  
If you choose **Enable Attachments sharing** for your instance, you must create an Amazon S3 bucket and [configure a CORS policy on your attachments bucket](#config-email-attachments-cors1), as described in this topic. If you don't do this, **the email channel will not work for your instance**.

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. On the instances page, choose the instance alias. The instance alias is also your **instance name**, which appears in your Connect Customer URL. The following image shows the **Connect Customer virtual contact center instances** page, with a box around the instance alias.  
![The Connect Customer virtual contact center instances page, the instance alias.](http://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)

1. On the left navigation menu, choose **Data storage**, **Email messages**, **Edit**, **Enable exporting email messages to S3**, and then choose **Save**. 

1. Complete the **Email messages** page to create or select an S3 bucket where email messages are stored. The following image shows an example of a completed page.   
![The Data storage menu option, the Email messages page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-messages-export-to-s3.png)

1.  If you want to allow email attachments, choose **Attachments** as well. The following image shows these options.

The following image of the **Data storage** page shows the Amazon S3 bucket for email messages and attachments. 

![The Amazon S3 bucket to store emails and attachments.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-s3-bucket.png)


## Step 5: Configure a CORS policy on your attachments bucket
<a name="config-email-attachments-cors1"></a>

To allow customers and agents to upload and download files, update your cross-origin resource sharing (CORS) policy to allow `PUT` and `GET` requests for the Amazon S3 bucket you are using for attachments. This is more secure than enabling public read/write on your Amazon S3 bucket, which we don't recommend.

**To configure CORS on the attachments bucket**

1. Find the name of the Amazon S3 bucket for storing attachments: 

   1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

   1. In the Connect Customer console, choose **Data storage**, and locate the Amazon S3 bucket name. 

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the Amazon S3 console, select your Amazon S3 bucket. 

1. Choose the **Permissions** tab, and then scroll down to the **Cross-origin resource sharing (CORS)** section.

1. Add a CORS policy that has one of the following rules on your attachments bucket. For example CORS policies, see [Cross-origin resource sharing: Use-case scenarios](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html#example-scenarios-cors) in the *Amazon S3 Developer Guide*.
   + Option 1: List the endpoints from where attachments will be sent and received, such as the name of your business web site. This rule allows cross-origin PUT and GET requests from your website (for example, http://www.example1.com).

     Your CORS policy might look similar to the following example:

     ```
     [
         {
             "AllowedHeaders": [
                 "*"
             ],
             "AllowedMethods": [
                 "PUT",
                 "GET"
             ],
             "AllowedOrigins": [
                 "*.my.connect.aws",
                 "*.awsapps.com"
             ],
             "ExposeHeaders": []
         }
     ]
     ```
   + Option 2: Add the `*` wildcard to `AllowedOrigin`. This rule allows cross-origin PUT and GET requests from all origins, so you don't have to list your endpoints.

     Your CORS policy might look similar to the following example:

     ```
     [
         {                               
             "AllowedMethods": [
                 "PUT",
                 "GET"            
             ],
             "AllowedOrigins": [   
                 "*" 
                 ],
            "AllowedHeaders": [
                 "*"
                 ]
         }    
     ]
     ```

## Next steps
<a name="next-steps-email-setup3"></a>
+ [Set up attachment scanning in Connect Customer](setup-attachment-scanning.md): This topic is for developers who are familiar with Lambda. You can configure Connect Customer to scan email attachments by using your preferred scanning application.

## APIs to enable email
<a name="apis-email-setup2"></a>

Use the following APIs to enable email programmatically:
+ [CreateIntegrationAssociation](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html)
+ [AssociateInstanceStorageConfig](https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateInstanceStorageConfig.html)
+ [DescribeInstanceStorageConfig](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeInstanceStorageConfig.html)
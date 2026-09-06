

# Set up your Connect Customer instance
<a name="tutorial1-set-up-your-instance"></a>

You can have multiple instances of Connect Customer. Each instance contains all the resources related to your contact center, such as phone numbers, agent accounts, and queues.

In this tutorial, you open Connect Customer, create an instance of Connect Customer, and claim a phone number that you can use for testing.

**Topics**
+ [Step 1: Launch Connect Customer](#tutorial1-login-aws)
+ [Step 2: Create an instance](#tutorial1-create-instance)
+ [Step 3: Claim a phone number for your instance](#tutorial1-claim-phone-number)

## Step 1: Launch Connect Customer
<a name="tutorial1-login-aws"></a>

This step walks you through finding Connect Customer in the AWS console, and opening the Connect Customer console. 

1. Log in to the [AWS Management Console](https://console.aws.amazon.com/console) (https://console.aws.amazon.com/console) using your AWS account. 

1. In the AWS Management Console, at the top of the page, choose the **Services** drop-down menu.  
![The AWS Management console, the services dropdown menu.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-access-services.png)

1. In the search box, type **Connect Customer**.  
![The search box, Connect Customer in the dropdown list of results.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-access-services2.png)

1. Choose **Connect Customer**. 

   If this is the first time you've been to the Connect Customer console, you'll see the following Welcome page.   
![The Connect Customer welcome page, the get started button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-amazon-connect-getting-started.png)

1. Choose **Get started**. 

**Congratulations\!** You found and accessed Connect Customer. You can use these same steps to search for and launch any AWS service.

Go to [Step 2: Create an instance](#tutorial1-create-instance).

## Step 2: Create an instance
<a name="tutorial1-create-instance"></a>

1. On the **Connect Customer virtual contact center instances** page, choose **Add an instance**.

1. On the **Set identity** page, in the **Access URL** box, type a unique name for your instance. For example, the following image shows **mytest10089** as a name. Choose a different name for your instance. Then choose **Next**.  
![The set identity page, the Access URL box.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-name-instance.png)

1. On the **Add administrator** page, add a new administrator account for Connect Customer. Use this account to log in to your instance later using the unique access URL. Choose **Next**.  
![The add administrator page, the username and password boxes.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-create-admin.png)

   1. The user name will be your Connect Customer login. It's case sensitive.

   1. The password must be between 8-64 characters, and must contain at least one uppercase letter, one lowercase letter, and one number.

1. On the **Set telephony** page, accept the default settings to allow incoming and outgoing calls. Choose **Next**.   
![The set telephony page, telephony options section.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-telephony-defaults.png)

1. On the **Data storage** page, accept the default settings and choose **Next**.   
![The default settings for storing data and flow logs, enable customer profiles option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-data-storage.png)

1. On the **Review and create** page, choose **Create instance**.  
![The review and create page, the create instance button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-review-create-instance.png)

1. After the instance is created, choose **Get started**.  
![The Connect Customer instances page, the Getting started button in the top right corner.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-done-created-instance.png)

1. On the **Welcome to Connect Customer** page, choose **Skip for now**.  
![The Welcome to Connect Customer page, the Skip for now link.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-skip-for-now.png)

1. You're now on the Connect Customer dashboard. Your instance name (also called an **alias**) displays in the URL. On the left is the navigation menu.  
![The Connect Customer dashboard page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-dashboard.png)

   1. Your instance alias is located in the first part of the URL.

   1. The navigation menu.

Congratulations\! You set up your instance and now you're on the Connect Customer dashboard. Go to [Step 3: Claim a phone number for your instance](#tutorial1-claim-phone-number).

## Step 3: Claim a phone number for your instance
<a name="tutorial1-claim-phone-number"></a>

In this step, you set up a phone number so that you can experiment with Connect Customer.

1. On the Connect Customer navigation menu, choose **Channels**, **Phone numbers**.   
![The Connect Customer navigation menu, channels icon, phone numbers option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-routing-phone-numbers.png)

1. On the right side of the **Manage Phone numbers** page, choose **Claim a number**.  
![The Manage phone numbers page, the Claim a number button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-claim-a-number-button.png)

1. Select the **DID (Direct Inward Dialing)** tab. Use the drop-down arrow to choose your country/region. If you're in the US, you can specify the area code you want for your number, and only available numbers with that area code will be displayed. When numbers are returned, choose one.   
![The Claim phone number page, DID (Direct Inward Dialing) tab.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-claim-number.png)

1. Write down the phone number. You call it later in this tutorial.

1. In the **Description** box, type this note: **this number is for testing**.  
![The Description box, the flow IVR dropdown menu.](http://docs.aws.amazon.com/connect/latest/adminguide/images/tutorial1-claim-number2.png)

1. In the **Flow / IVR** box, choose the drop-down arrow, and then choose **Sample inbound flow (first contact experience)**.

1. Choose **Save**.

**Congratulations\!** You set up your instance and claimed a phone number. Now you're ready to experience how chat and voice work in Connect Customer. Go to [Test the sample voice and chat experience in Connect Customer](tutorial1-explore-voice-and-chat.md).
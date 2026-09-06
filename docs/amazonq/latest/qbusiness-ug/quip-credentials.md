

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Retrieving Quip credentials
<a name="quip-credentials"></a>

Before you connect Quip to Amazon Q, you need to create and retrieve the Quip credentials you will use to connect Quip to Amazon Q. 

The following procedure gives you an overview of how to configure Quip for connecting with Amazon Q by creating a API access token.

**Configuring Quip authentication for Amazon Q**

1. Log in to your Quip account using a web browser of your choice and sign into your Quip workspace.
**Note**  
To configure Quip for Amazon Q, you must be an admin user in the Quip account.

1. From the browser URL, note your Quip domain name. You will need this both to connect to Amazon Q and also to generate an API access token.  
![Screenshot of the Quip interface showing the account settings menu where users can access developer tools to generate an API token.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/quip-1.png)

1. In a text editor of your choice, copy and paste the following: `https://{{domain}}/dev/token`. Then, replace {{domain}} with the Quip domain you copied in the last step. Copy the URL.

1. Open a new browser window and paste the formatted URL you created in the last step. Quip will return an API access token in your browser window.  
![Screenshot of the Quip developer token page showing the generated personal access token that needs to be copied for API authentication.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/quip-2.png)

You now have the Quip domain name and Quip API access token you need to connect to Amazon Q.
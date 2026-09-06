

# Removing the delegated administrator account in Security Hub
<a name="securityhub-v2-remove-da"></a>

 You can remove the delegated administrator account in the Security Hub console at any time. However, this action removes the delegated administrator from both Security Hub and Security Hub CSPM. We recommend only performing this action when you have confirmed this operation with your security account. 

**Note**  
 If you are using an account other than the organization management account as the Security Hub CSPM delegated administrator, removing it through either the Security Hub CSPM console or the AWS Organizations API also removes it from Security Hub.   
 Similarly, if you remove the Security Hub delegated administrator through either the Security Hub Console or AWS Organizations API, it is also removed from Security Hub CSPM. When the delegated administrator is removed from Security Hub CSPM, Central Configuration automatically opts out. 

**To remove the delegated administrator account**

1.  Sign in to your AWS account with your organization management account credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **General**. 

1.  In **Delegated administrator**, choose **Remove delegated administrator**. In the confirmation dialog box, enter *remove*, and choose **Remove**. 
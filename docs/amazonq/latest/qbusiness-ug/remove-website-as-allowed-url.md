

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Remove your website as an allowed URL
<a name="remove-website-as-allowed-url"></a>

To remove a website(s) from list of allowed websites, you can use the Amazon Q Business console or the Amazon Q Business API.

## Using the console
<a name="remove-website-as-allowed-url-console"></a>

1. Sign in to the [Amazon Amazon Q Console](https://console.aws.amazon.com/amazonq/business/).

1. Choose **Applications**, then select the name of your application from the list.

1. From the left navigation, choose **Amazon Q embedded** under the **Enhancements** section.

1. On the main page, select the website that you want to remove and choose **Remove** and confirm your choice.

## Using the AWS CLI
<a name="remove-website-as-allowed-url-cli"></a>

To remove the website from the list of allowed websites, you will need to use the `get-web-experience` operation to get a list of all your allowed website URLs `origins` and remove the website that you no longer want to work with Amazon Q embedded and resubmit the rest of the URLs using the `update-web-experience` operation. Otherwise, all your other allowed websites will also be removed.

```
 aws qbusiness get-web-experience \
  --application-id application-id \
  --web-experience-id web-experience-id \  
                    
aws qbusiness update-web-experience \
  --application-id application-id \
  --web-experience-id web-experience-id \
  --origins {{origins}}
```

**Note**  
You will need to remove the `<iframe>` element from that website as it will no longer work.
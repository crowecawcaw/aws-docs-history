# Remove your website as an allowed URL

To remove a website(s) from list of allowed websites, you can use the Amazon Q Business console or the Amazon Q Business API.

1. Sign in to the [Amazon
   Amazon Q Console](https://console.aws.amazon.com/amazonq/business/ "https://console.aws.amazon.com/amazonq/business/").
2. Choose **Applications**, then select the name of your
   application from the list.
3. From the left navigation, choose **Amazon Q
   embedded** under the **Enhancements**
   section.
4. On the main page, select the website that you want to remove and
   choose **Remove** and confirm your choice.
   To remove the website from the list of allowed websites, you will need to use
   the `get-web-experience` operation to get a list of all your allowed
   website URLs `origins` and remove the website that you no longer want
   to work with Amazon Q embedded and resubmit the rest of the URLs
   using the `update-web-experience` operation. Otherwise, all your
   other allowed websites will also be removed.

```

 aws qbusiness get-web-experience \
  --application-id application-id \
  --web-experience-id web-experience-id \

aws qbusiness update-web-experience \
  --application-id application-id \
  --web-experience-id web-experience-id \
  --origins `origins`

```

###### Note

You will need to remove the `<iframe>` element from that website
as it will no longer work.

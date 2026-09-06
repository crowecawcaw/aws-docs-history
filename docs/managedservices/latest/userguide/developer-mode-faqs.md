

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Before you begin with AMS Developer mode
<a name="developer-mode-faqs"></a>

Before implementing Developer mode, there are a few things you should know.

AMS Advanced cannot manage existing stacks or resources in a DevMode account that were created outside of the AMS Advanced change management process through requests for change (RFCs). However, while the account is in DevMode, AMS Advanced continues to manage resources provisioned through the AMS Advanced change management process with RFCs.

You cannot start with a DevMode account and later covert it to an AMS Advanced-managed application account.
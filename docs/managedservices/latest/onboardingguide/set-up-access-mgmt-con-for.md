

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Configure the Conditional Forwarder
<a name="set-up-access-mgmt-con-for"></a>

1. In the AD **DNS Manager -> Create a New Conditional Forwarder**, under **DNS Domain:** Use the domain name AMS supplied to you; for example, *A523434123.amazonaws.com* (change this to the domain name selected in the onboarding questionnaire.

1. Under **IP addresses of the master servers:** Add the AMS-supplied IP addresses. Make sure there isn't a connection problem by validating both addresses.

1. Select **Store this conditional forwarder in Active Directory and replicate as follows: All DNS servers in this domain** and press **OK**.
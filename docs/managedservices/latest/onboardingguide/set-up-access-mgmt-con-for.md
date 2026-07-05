End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# Configure the Conditional Forwarder

1. In the AD **DNS Manager -> Create a New Conditional Forwarder**, under
   **DNS Domain:** Use the domain name AMS supplied to you; for example,
   _A523434123.amazonaws.com_ (change this to the domain name selected in the onboarding questionnaire.
2. Under **IP addresses of the master servers:** Add the AMS-supplied IP addresses. Make sure
   there isn't a connection problem by validating both addresses.
3. Select **Store this conditional forwarder in Active Directory and replicate as follows: All DNS servers in this domain** and press
   **OK**.

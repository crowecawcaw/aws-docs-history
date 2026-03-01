AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Editing Agentless Collector settings

You configured the collector when you first set up Application Discovery Service Agentless Collector
(Agentless Collector) as described in [Configuring Agentless Collector](agentless-collector-gs-configure.md "agentless-collector-gs-configure.md"). The following procedure
describes how to edit Agentless Collector configuration settings.

###### To edit the collector configuration settings

- Choose the **Edit collector settings** button on the
  Agentless Collector dashboard.

On the **Edit collector settings** page, perform the
following:

    1. For **Collector name**, enter a name to identify the
     collector. The name can contain
     spaces but it cannot contain special characters.
    2. Under **Destination AWS account for discovery
     data**, enter the AWS access key and secret key for the
     AWS account to specify as the destination account to receive the data
     discovered by the collector. For information about the requirements for
     the IAM user, see [Deploying Application Discovery Service Agentless Collector](agentless-collector-deploying.md#agentless-collector-gs-iam-user "agentless-collector-deploying.md#agentless-collector-gs-iam-user").


    	1. For **AWS access-key**, enter the access
    	 key of the AWS account IAM user that you're specifying as
    	 the destination account.
    	2. For **AWS secret-key**, enter the secret
    	 key of the AWS account IAM user that you're specifying as
    	 the destination account.
    3. Under **Agentless Collector password**,
     change the password to use to authenticate access to the
     Agentless Collector.


    	1. For **Agentless Collector
    	 password**, enter a password to use to authenticate
    	 access to the Agentless Collector.
    	2. For **Re-enter Agentless Collector
    	 password**, for verification enter the password
    	 again.
    4. Choose **Save configurations**.

Next, you'll see [The Agentless Collector dashboard](agentless-collector-dashboard.md "agentless-collector-dashboard.md").

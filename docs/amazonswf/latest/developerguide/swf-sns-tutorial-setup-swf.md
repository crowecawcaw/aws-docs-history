# Subscription Workflow Tutorial Part 1: Using Amazon SWF

with the AWS SDK for Ruby

###### Topics

- [Include the AWS SDK for Ruby](#include-the-sdk-for-ruby "#include-the-sdk-for-ruby")
- [Configuring the AWS Session](#configuring-the-aws-session "#configuring-the-aws-session")
- [Registering an Amazon SWF Domain](#registering-swf-domain "#registering-swf-domain")
- [Next Steps](#next-steps "#next-steps")

## Include the AWS SDK for Ruby

Begin by creating a file called `utils.rb`. The code in this file will obtain,
or create if necessary, the Amazon SWF domain used by both the workflow and activities code and
will provide a place to put code that is common to all of our classes.

First, we need to include the `aws-sdk-v1` library in our code, so that we can
use the features provided by the SDK for Ruby.

```
require 'aws-sdk-v1'
```

This gives us access to the AWS namespace, which provides the ability to set global
session-related values, such as your AWS credentials and region, and also provides access to
the AWS service APIs.

## Configuring the AWS Session

We'll configure the AWS Session by setting our AWS credentials (which are needed for
accessing AWS services) and the AWS region to use.

There are a number of ways to [set AWS credentials
in the AWS SDK for Ruby](../../../AWSRubySDK/latest/index.md#Basic_Configuration "../../../AWSRubySDK/latest/index.md#Basic_Configuration"): by setting them in environment variables (AWS_ACCESS_KEY_ID
and AWS_SECRET_ACCESS_KEY) or by setting them with [`AWS.config`](../../../AWSRubySDK/latest/AWS.md#config-class_method "../../../AWSRubySDK/latest/AWS.md#config-class_method").
We'll use the latter method, loading them from a YAML configuration file, called
`aws-config.txt`, that looks like this.

```
---
:access_key_id: REPLACE_WITH_ACCESS_KEY_ID
:secret_access_key: REPLACE_WITH_SECRET_ACCESS_KEY
```

Create this file now, replacing the strings beginning with
_REPLACE_WITH\__ with your AWS access key ID and secret access key. For
information about your AWS access keys, see [How Do I Get Security Credentials?](../../../general/latest/gr/getting-aws-sec-creds.md "../../../general/latest/gr/getting-aws-sec-creds.md") in
the _Amazon Web Services General Reference_.

We also need to set the AWS region to use. Because we'll be using the [Short Message Service (SMS)](http://en.wikipedia.org/wiki/Short_Message_Service "http://en.wikipedia.org/wiki/Short_Message_Service")
to send text messages to the user's phone with Amazon SNS, we need to make sure that we're using
region supported by Amazon SNS. See [Supported
Regions and Countries](../../../sns/latest/dg/sms_supported-countries.md "../../../sns/latest/dg/sms_supported-countries.md") in the Amazon Simple Notification Service Developer Guide.

###### Note

If you don't have access to **us-east-1**, or don't care
about running the demo with SMS messaging enabled, feel free to use any region you wish to.
You can remove the SMS functionality from the sample and use email as the sole endpoint to
subscribe to the Amazon SNS topic.

For more information about sending SMS messages, see [Sending and Receiving SMS Notifications Using
Amazon SNS](../../../sns/latest/dg/SMSMessages.md "../../../sns/latest/dg/SMSMessages.md") in the _Amazon Simple Notification Service Developer Guide_.

We'll now add some code to `utils.rb` to load the config file, get the user's
credentials, then provide both the credentials and region to [`AWS.config`](../../../AWSRubySDK/latest/AWS.md#config-class_method "../../../AWSRubySDK/latest/AWS.md#config-class_method").

```
require 'yaml'

# Load the user's credentials from a file, if it exists.
begin
  config_file = File.open('aws-config.txt') { |f| f.read }
rescue
  puts "No config file! Hope you set your AWS credentials in the environment..."
end

if config_file.nil?
  options = { }
else
  options = YAML.load(config_file)
end

# SMS Messaging (which can be used by Amazon SNS) is available only in the
# `us-east-1` region.
$SMS_REGION = 'us-east-1'
options[:region] = $SMS_REGION

# Now, set the options
AWS.config = options
```

## Registering an Amazon SWF Domain

To use Amazon SWF, you need to set up a _domain_: a named entity that will
hold your workflows and activities. You can have many Amazon SWF domains registered, but they must
all have unique names within your AWS account, and workflows can't interact across domains:
All of the workflows and activities for your application must be in the same domain to
interact with one another.

Because we'll be using the same domain throughout our application, we'll create a function
in `utils.rb` called `init_domain`, that will retrieve the Amazon SWF domain
named _SWFSampleDomain_.

Once you have registered a domain, you can reuse it for many workflow executions. However,
_it is an error to try to register a domain that already exists_, so our
code will first check to see if the domain exists, and will use the existing domain if it can
be found. If the domain can't be found, we'll create it.

To work with Amazon SWF domains in the SDK for Ruby, use [AWS::SimpleWorkflow.domains](../../../AWSRubySDK/latest/AWS/SimpleWorkflow.md#domains-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow.md#domains-instance_method"), which returns a [DomainCollection](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DomainCollection.md "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DomainCollection.md") that can be used to both enumerate and register domains:

- To check to see if a domain is already registered, you can look at the list provided
  by [AWS::Simpleworkflow.domains.registered](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DomainCollection.md#registered-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DomainCollection.md#registered-instance_method").
- To register a new domain, use [AWS::Simpleworkflow.domains.register](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DomainCollection.md#register-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/DomainCollection.md#register-instance_method").

Here is the code for `init_domain` in `utils.rb`.

```
# Registers the domain that the workflow will run in.
def init_domain
  domain_name = 'SWFSampleDomain'
  domain = nil
  swf = AWS::SimpleWorkflow.new

  # First, check to see if the domain already exists and is registered.
  swf.domains.registered.each do | d |
    if(d.name == domain_name)
      domain = d
      break
    end
  end

  if domain.nil?
    # Register the domain for one day.
    domain = swf.domains.create(
      domain_name, 1, { :description => "#{domain_name} domain" })
  end

  return domain
end
```

## Next Steps

Next, you will create the workflow and starter code in [Subscription Workflow Tutorial Part 2: Implementing the Workflow](swf-sns-tutorial-implementing-workflow.md "swf-sns-tutorial-implementing-workflow.md").

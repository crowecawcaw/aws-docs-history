# Subscription Workflow Tutorial Part 3: Implementing the Activities

We'll now implement each of the activities in our workflow, beginning with a base class that provides some
common features for the activity code.

###### Topics

- [Defining a Basic Activity Type](#defining-a-basic-activity-type "#defining-a-basic-activity-type")
- [Defining GetContactActivity](#defining-getcontactactivity "#defining-getcontactactivity")
- [Defining SubscribeTopicActivity](#defining-subscribetopicactivity "#defining-subscribetopicactivity")
- [Defining WaitForConfirmationActivity](#defining-waitforconfirmationactivity "#defining-waitforconfirmationactivity")
- [Defining SendResultActivity](#defining-sendresultactivity "#defining-sendresultactivity")
- [Next Steps](#implementing-activities-next-steps "#implementing-activities-next-steps")

## Defining a Basic Activity Type

When designing the workflow, we identified the following activities:

- `get_contact_activity`
- `subscribe_topic_activity`
- `wait_for_confirmation_activity`
- `send_result_activity`

We'll implement each of these activities now. Because our activities will share some features, let's do a
little groundwork and create some common code they can share. We'll call it **BasicActivity**, and define it in a new file called `basic_activity.rb`.

As with the other source files, we'll include `utils.rb` to access the
`init_domain` function to set up the sample domain.

```
   require_relative 'utils.rb'
```

Next, we'll declare the basic activity class and some common data that we'll be interested in for each
activity. We'll save the activity's [AWS::SimpleWorkflow::ActivityType](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/ActivityType.md "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/ActivityType.md") instance,
_name_, and _results_ in attributes of the class.

```
   class BasicActivity

     attr_accessor :activity_type
     attr_accessor :name
     attr_accessor :results
```

These attributes access instance data that's defined in the class' `initialize` method,
which takes an activity _name_, and an optional _version_ and map of
_options_ to be used when registering the activity with Amazon SWF.

```
     def initialize(name, version = 'v1', options = nil)

       @activity_type = nil
       @name = name
       @results = nil

       # get the domain to use for activity tasks.
       @domain = init_domain

       # Check to see if this activity type already exists.
       @domain.activity_types.each do | a |
         if (a.name == @name) && (a.version == version)
           @activity_type = a
         end
       end

       if @activity_type.nil?
         # If no options were specified, use some reasonable defaults.
         if options.nil?
           options = {
             # All timeouts are in seconds.
             :default_task_heartbeat_timeout => 900,
             :default_task_schedule_to_start_timeout => 120,
             :default_task_schedule_to_close_timeout => 3800,
             :default_task_start_to_close_timeout => 3600 }
         end
         @activity_type = @domain.activity_types.register(@name, version, options)
       end
     end
```

As with workflow type registration, if an activity type is already registered, we can retrieve it by looking
at the domain's [activity_types](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/Domain.md#activity_types-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/Domain.md#activity_types-instance_method")
collection. If the activity can't be found, it will be registered.

Also, as with workflow types, you can set _default options_ that are stored with your
activity type when you register it.

The last thing our basic activity gets is a consistent way to run it. We'll define a
`do_activity` method that takes an activity task. As shown, we can use the passed-in activity task
to receive data via its `input` instance attribute.

```
     def do_activity(task)
       @results = task.input # may be nil
       return true
     end
   end
```

That wraps up the **BasicActivity** class. Now we'll use it to make defining
our activities simple and consistent.

## Defining GetContactActivity

The first activity that is run during a workflow execution is `get_contact_activity`, which
retrieves the user's Amazon SNS topic subscription information.

Create a new file called `get_contact_activity.rb`, and require both
`yaml`, which we'll use to prepare a string for passing to Amazon SWF, and
`basic_activity.rb`, which we'll use as the basis for this **GetContactActivity** class.

```
   require 'yaml'
   require_relative 'basic_activity.rb'

   # **GetContactActivity** provides a prompt for the user to enter contact
   # information. When the user successfully enters contact information, the
   # activity is complete.
   class GetContactActivity < BasicActivity
```

Because we put the activity registration code in **BasicActivity**, the
`initialize` method for **GetContactActivity** is pretty simple. We
simply call the base class constructor with the activity name, `get_contact_activity`. This is all
that is required to register our activity.

```
     # initialize the activity
     def initialize
       super('get_contact_activity')
     end
```

We'll now define the `do_activity` method, which prompts for the user's email
and/or phone number.

```
     def do_activity(task)
       puts ""
       puts "Please enter either an email address or SMS message (mobile phone) number to"
       puts "receive SNS notifications. You can also enter both to use both address types."
       puts ""
       puts "If you enter a phone number, it must be able to receive SMS messages, and must"
       puts "be 11 digits (such as 12065550101 to represent the number 1-206-555-0101)."

       input_confirmed = false
       while !input_confirmed
         puts ""
         print "Email: "
         email = $stdin.gets.strip

         print "Phone: "
         phone = $stdin.gets.strip

         puts ""
         if (email == '') && (phone == '')
           print "You provided no subscription information. Quit? (y/n)"
            confirmation = $stdin.gets.strip.downcase
            if confirmation == 'y'
              return false
            end
         else
            puts "You entered:"
            puts "  email: #{email}"
            puts "  phone: #{phone}"
            print "\nIs this correct? (y/n): "
            confirmation = $stdin.gets.strip.downcase
            if confirmation == 'y'
              input_confirmed = true
            end
         end
       end

       # make sure that @results is a single string. YAML makes this easy.
       @results = { :email => email, :sms => phone }.to_yaml
       return true
     end
   end
```

At the end of `do_activity`, we take the email and phone number retrieved from the user,
place it in a map and then use `to_yaml` to convert the entire map to a YAML string. There's an
important reason for this: any results that you pass to Amazon SWF when you complete an activity must be
_string data only_. Ruby's ability to easily convert objects to YAML strings and then back again
into objects is, thankfully, well-suited for this purpose.

That's the end of the `get_contact_activity` implementation. This data will be used next in
the `subscribe_topic_activity` implementation.

## Defining SubscribeTopicActivity

We'll now delve into Amazon SNS and create an activity that uses the information generated by
`get_contact_activity` to subscribe the user to an Amazon SNS topic.

Create a new file called `subscribe_topic_activity.rb`, add the same requirements that we
used for `get_contact_activity`, declare your class, and provide its `initialize`
method.

```
   require 'yaml'
   require_relative 'basic_activity.rb'

   # **SubscribeTopicActivity** sends an SMS / email message to the user, asking for
   # confirmation.  When this action has been taken, the activity is complete.
   class SubscribeTopicActivity < BasicActivity

     def initialize
       super('subscribe_topic_activity')
     end
```

Now that we have the code in place to get the activity set up and registered, we will add some code
to create an Amazon SNS topic. To do so, we'll use the [AWS::SNS::Client](../../../AWSRubySDK/latest/AWS/SNS/Client.md "../../../AWSRubySDK/latest/AWS/SNS/Client.md") object's [create_topic](../../../AWSRubySDK/latest/AWS/SNS/Client.md#create_topic-instance_method "../../../AWSRubySDK/latest/AWS/SNS/Client.md#create_topic-instance_method")
method.

Add the `create_topic` method to your class, which takes a passed-in Amazon SNS client object.

```
     def create_topic(sns_client)
       topic_arn = sns_client.create_topic(:name => 'SWF_Sample_Topic')[:topic_arn]

       if topic_arn != nil
         # For an SMS notification, setting `DisplayName` is *required*. Note that
         # only the *first 10 characters* of the DisplayName will be shown on the
         # SMS message sent to the user, so choose your DisplayName wisely!
         sns_client.set_topic_attributes( {
           :topic_arn => topic_arn,
           :attribute_name => 'DisplayName',
           :attribute_value => 'SWFSample' } )
       else
         @results = {
           :reason => "Couldn't create SNS topic", :detail => "" }.to_yaml
         return nil
       end

       return topic_arn
     end
```

Once we have the topic's Amazon Resource Name (ARN), we can use it with the Amazon SNS client's [set_topic_attributes](../../../AWSRubySDK/latest/AWS/SNS/Client.md#set_topic_attributes-instance_method "../../../AWSRubySDK/latest/AWS/SNS/Client.md#set_topic_attributes-instance_method") method to
set the topic's _DisplayName_, which is required for sending SMS messages with Amazon SNS.

Lastly, we'll define the `do_activity` method. We'll start by collecting any data that was
passed via the `input` option when the activity was scheduled. As previously mentioned, this must
be passed as a string, which we created using `to_yaml`. When retrieving it, we'll use
`YAML.load` to turn the data into Ruby objects.

Here's the beginning of `do_activity`, in which we retrieve the input data.

```
     def do_activity(task)
       activity_data = {
         :topic_arn => nil,
         :email => { :endpoint => nil, :subscription_arn => nil },
         :sms => { :endpoint => nil, :subscription_arn => nil },
       }

       if task.input != nil
         input = YAML.load(task.input)
         activity_data[:email][:endpoint] = input[:email]
         activity_data[:sms][:endpoint] = input[:sms]
       else
         @results = { :reason => "Didn't receive any input!", :detail => "" }.to_yaml
         puts("  #{@results.inspect}")
         return false
       end

       # Create an SNS client. This is used to interact with the service. Set the
       # region to $SMS_REGION, which is a region that supports SMS notifications
       # (defined in the file `utils.rb`).
       sns_client = AWS::SNS::Client.new(
         :config => AWS.config.with(:region => $SMS_REGION))
```

If we didn't receive any input, there isn't much to do, so we'll just fail the activity.

Assuming that everything is fine, however, we'll continue filling in our `do_activity`
method, get an Amazon SNS client with the AWS SDK for Ruby, and pass it to our `create_topic` method to
create the Amazon SNS topic.

```
       # Create the topic and get the ARN
       activity_data[:topic_arn] = create_topic(sns_client)

       if activity_data[:topic_arn].nil?
         return false
       end
```

There are a couple of things worth noting here:

- We use [`AWS.config.with`](../../../AWSRubySDK/latest/AWS/Core/Configuration.md#with-instance_method "../../../AWSRubySDK/latest/AWS/Core/Configuration.md#with-instance_method") to set the region
  for our Amazon SNS client. Because we want to send SMS messages, we use the SMS-enabled region that we declared in
  `utils.rb`.
- We save the topic's ARN in our `activity_data` map. This is part of the data that will
  be passed to the _next_ activity in our workflow.

Finally, this activity subscribes the user to the Amazon SNS topic, using the passed-in endpoints (email and SMS).
We don't require the user to enter _both_ endpoints, but we do need at least one.

```
       # Subscribe the user to the topic, using either or both endpoints.
       [:email, :sms].each do | x |
         ep = activity_data[x][:endpoint]
         # don't try to subscribe an empty endpoint
         if (ep != nil && ep != "")
           response = sns_client.subscribe( {
             :topic_arn => activity_data[:topic_arn],
             :protocol => x.to_s, :endpoint => ep } )
           activity_data[x][:subscription_arn] = response[:subscription_arn]
         end
       end
```

[AWS::SNS::Client.subscribe](../../../AWSRubySDK/latest/AWS/SNS/Client.md#subscribe-instance_method "../../../AWSRubySDK/latest/AWS/SNS/Client.md#subscribe-instance_method")
takes the topic ARN, the _protocol_ (which, cleverly, we disguised as the
`activity_data` map key for the corresponding endpoint).

Finally, we re-package the information for the next activity in YAML format, so that we can send it back to
Amazon SWF.

```
       # if at least one subscription arn is set, consider this a success.
       if (activity_data[:email][:subscription_arn] != nil) or (activity_data[:sms][:subscription_arn] != nil)
         @results = activity_data.to_yaml
       else
         @results = { :reason => "Couldn't subscribe to SNS topic", :detail => "" }.to_yaml
         puts("  #{@results.inspect}")
         return false
       end
       return true
     end
   end
```

That completes the implementation of the `subscribe_topic_activity`. Next, we'll define
`wait_for_confirmation_activity`.

## Defining WaitForConfirmationActivity

Once a user is subscribed to an Amazon SNS topic, he or she will still need to confirm the subscription request.
In this case, we'll be waiting for the user to confirm by either email or an SMS message.

The activity that waits for the user to confirm the subscription is called
`wait_for_confirmation_activity`, and we'll define it here. To begin, create a new file called
`wait_for_confirmation_activity.rb` and set it up as we've set up the previous activities.

```
   require 'yaml'
   require_relative 'basic_activity.rb'

   # **WaitForConfirmationActivity** waits for the user to confirm the SNS
   # subscription.  When this action has been taken, the activity is complete. It
   # might also time out...
   class WaitForConfirmationActivity < BasicActivity

     # Initialize the class
     def initialize
       super('wait_for_confirmation_activity')
     end
```

Next, we'll begin defining the `do_activity` method and retrieve any input data into a local
variable called `subscription_data`.

```
     def do_activity(task)
       if task.input.nil?
         @results = { :reason => "Didn't receive any input!", :detail => "" }.to_yaml
         return false
       end

       subscription_data = YAML.load(task.input)
```

Now that we have the topic ARN, we can retrieve the topic by creating a new instance of [AWS::SNS::Topic](../../../AWSRubySDK/latest/AWS/SNS/Topic.md "../../../AWSRubySDK/latest/AWS/SNS/Topic.md") and pass it the ARN.

```
       topic = AWS::SNS::Topic.new(subscription_data[:topic_arn])

       if topic.nil?
         @results = {
           :reason => "Couldn't get SWF topic ARN",
           :detail => "Topic ARN: #{topic.arn}" }.to_yaml
         return false
       end
```

Now, we'll check the topic to see if the user has confirmed the subscription using one of the endpoints.
We'll only require that one endpoint has been confirmed to consider the activity a success.

An Amazon SNS topic maintains a list of the [subscriptions](../../../AWSRubySDK/latest/AWS/SNS/Topic.md#subscriptions-instance_method "../../../AWSRubySDK/latest/AWS/SNS/Topic.md#subscriptions-instance_method") for that topic, and we
can check whether or not the user has confirmed a particular subscription by checking to see if the subscription's
ARN is set to anything other than `PendingConfirmation`.

```
       # loop until we get some indication that a subscription was confirmed.
       subscription_confirmed = false
       while(!subscription_confirmed)
         topic.subscriptions.each do | sub |
           if subscription_data[sub.protocol.to_sym][:endpoint] == sub.endpoint
             # this is one of the endpoints we're interested in. Is it subscribed?
             if sub.arn != 'PendingConfirmation'
               subscription_data[sub.protocol.to_sym][:subscription_arn] = sub.arn
               puts "Topic subscription confirmed for (#{sub.protocol}: #{sub.endpoint})"
               @results = subscription_data.to_yaml
               return true
             else
               puts "Topic subscription still pending for (#{sub.protocol}: #{sub.endpoint})"
             end
           end
         end
```

If we get an ARN for the subscription, we'll save it in the activity's result data, convert it to YAML, and
return true from `do_activity`, which signals that the activity completed successfully.

Because waiting for a subscription to be confirmed might take a while, we'll occasionally call
`record_heartbeat` on the activity task. This signals to Amazon SWF that the activity is still
processing, and can also be used to provide updates about the progress of the activity (if you are doing something,
like processing files, that you can report progress for).

```
         task.record_heartbeat!(
           { :details => "#{topic.num_subscriptions_confirmed} confirmed, #{topic.num_subscriptions_pending} pending" })
         # sleep a bit.
         sleep(4.0)
       end
```

This ends our `while` loop. If we somehow get out of the while loop without success, we'll
report failure and finish the `do_activity` method.

```
       if (subscription_confirmed == false)
         @results = {
           :reason => "No subscriptions could be confirmed",
           :detail => "#{topic.num_subscriptions_confirmed} confirmed, #{topic.num_subscriptions_pending} pending" }.to_yaml
         return false
       end
     end
   end
```

That ends the implementation of `wait_for_confirmation_activity`. We have only one more
activity to define: `send_result_activity`.

## Defining SendResultActivity

If the workflow has progressed this far, we've successfully subscribed the user to an Amazon SNS topic and the
user has confirmed the subscription.

Our last activity, `send_result_activity`, sends the user a confirmation of the successful
topic subscription, using the topic that the user subscribed to and the endpoint that the user confirmed the
subscription with.

Create a new file called `send_result_activity.rb` and set it up as we've set up all the
activities so far.

```
   require 'yaml'
   require_relative 'basic_activity.rb'

   # **SendResultActivity** sends the result of the activity to the screen, and, if
   # the user successfully registered using SNS, to the user using the SNS contact
   # information collected.
   class SendResultActivity < BasicActivity

     def initialize
       super('send_result_activity')
     end
```

Our `do_activity` method begins similarly, as well, getting the input data from the
workflow, converting it from YAML, and then using the topic ARN to create an [AWS::SNS::Topic](../../../AWSRubySDK/latest/AWS/SNS/Topic.md "../../../AWSRubySDK/latest/AWS/SNS/Topic.md") instance.

```
     def do_activity(task)
       if task.input.nil?
         @results = { :reason => "Didn't receive any input!", :detail => "" }
         return false
       end

       input = YAML.load(task.input)

       # get the topic, so we publish a message to it.
       topic = AWS::SNS::Topic.new(input[:topic_arn])

       if topic.nil?
         @results = {
           :reason => "Couldn't get SWF topic",
           :detail => "Topic ARN: #{topic.arn}" }
         return false
       end
```

Once we have the topic, we'll [publish](../../../AWSRubySDK/latest/AWS/SNS/Topic.md#publish-instance_method "../../../AWSRubySDK/latest/AWS/SNS/Topic.md#publish-instance_method") a
message to it (and echo it to the screen, as well).

```
       @results = "Thanks, you've successfully confirmed registration, and your workflow is complete!"

       # send the message via SNS, and also print it on the screen.
       topic.publish(@results)
       puts(@results)

       return true
     end
   end
```

Publishing to an Amazon SNS topic sends the message that you supply to _all_ of the subscribed
and confirmed endpoints that exist for that topic. So, if the user confirmed with _both_ an
email and an SMS number, he or she will receive two confirmation messages, one at each endpoint.

## Next Steps

This completes the implementation of `send_result_activity`. Now, you will tie all these
activities together in an activity application that handles the activity tasks and can launch activities in
response, in [Subscription Workflow Tutorial Part 4: Implementing the Activities Task Poller](swf-sns-tutorial-implementing-activities-poller.md "swf-sns-tutorial-implementing-activities-poller.md").

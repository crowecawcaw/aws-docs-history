# Subscription Workflow Tutorial Part 4: Implementing the Activities Task Poller

In Amazon SWF, activity tasks for a running workflow execution appear on the _activity task
list_, which is provided when you schedule an activity in the workflow.

We'll implement a basic activity poller to handle these tasks for our workflow, and use it to launch our
activities when Amazon SWF places a task on the activity task list to start the activity.

To begin, create a new file called `swf_sns_activities.rb`. We'll use it to:

- Instantiate the activity classes that we created.
- Register each activity with Amazon SWF.
- Poll for activities and call `do_activity` for each activity when its name appears on
  the activity task list.
  In `swf_sns_activities.rb`, add the following statements to require each of the activity classes we defined.

```
require_relative 'get_contact_activity.rb'
require_relative 'subscribe_topic_activity.rb'
require_relative 'wait_for_confirmation_activity.rb'
require_relative 'send_result_activity.rb'
```

Now, we'll create the class and provide some initialization code.

```
class ActivitiesPoller

  def initialize(domain, workflowId)
    @domain = domain
    @workflowId = workflowId
    @activities = {}

    # These are the activities we'll run
    activity_list = [
      GetContactActivity,
      SubscribeTopicActivity,
      WaitForConfirmationActivity,
      SendResultActivity ]

    activity_list.each do | activity_class |
      activity_obj = activity_class.new
      puts "** initialized and registered activity: #{activity_obj.name}"
      # add it to the hash
      @activities[activity_obj.name.to_sym] = activity_obj
    end
  end
```

In addition to saving the passed in _domain_ and _task list_, this code
instantiates each of the activity classes we created. Because each class registers its associated activity (refer to
`basic_activity.rb` if you need to review that code), this is enough to let Amazon SWF know about all of
the activities we'll be running.

For each activity instantiated, we store it on a map using the activity name (such as
`get_contact_activity`) as the key, so we can easily look these up in the activity poller code,
which we'll define next.

Create a new method called `poll_for_activities` and call [poll](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/ActivityTaskCollection.md#poll-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/ActivityTaskCollection.md#poll-instance_method") on the [activity_tasks](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/Domain.md#activity_tasks-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/Domain.md#activity_tasks-instance_method") held by the
domain to get activity tasks.

```
  def poll_for_activities
    @domain.activity_tasks.poll(@workflowId) do | task |
      activity_name = task.activity_type.name
```

We can get the activity name from the task's [activity_type](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/ActivityTask.md#activity_type-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/ActivityTask.md#activity_type-instance_method") member.
Next, we'll use the activity name associated with this task to look up the class to run
`do_activity` on, passing it the task (which includes any input data that should be transferred to
the activity).

```
      # find the task on the activities list, and run it.
      if @activities.key?(activity_name.to_sym)
        activity = @activities[activity_name.to_sym]
        puts "** Starting activity task: #{activity_name}"
        if activity.do_activity(task)
          puts "++ Activity task completed: #{activity_name}"
          task.complete!({ :result => activity.results })
          # if this is the final activity, stop polling.
          if activity_name == 'send_result_activity'
             return true
          end
        else
          puts "-- Activity task failed: #{activity_name}"
          task.fail!(
            { :reason => activity.results[:reason],
              :details => activity.results[:detail] } )
        end
      else
        puts "couldn't find key in @activities list: #{activity_name}"
        puts "contents: #{@activities.keys}"
      end
    end
  end
end
```

The code just waits for `do_activity` to complete, and then calls either [complete!](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/ActivityTask.md#complete!-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/ActivityTask.md#complete!-instance_method") or [fail!](../../../AWSRubySDK/latest/AWS/SimpleWorkflow/ActivityTask.md#fail!-instance_method "../../../AWSRubySDK/latest/AWS/SimpleWorkflow/ActivityTask.md#fail!-instance_method") on the task based on the
return code.

###### Note

This code exits from the poller once the final activity has been launched, because it has completed
its mission and has launched all of the activities. In your own Amazon SWF code, if your activities might be run again,
you may want to keep the activity poller running indefinitely.

That's the end of the code for our **ActivitiesPoller** class, but we'll add a
little more code at the end of the file to allow the user to run it from the command-line.

```
if __FILE__ == $0
  if ARGV.count < 1
    puts "You must supply a task-list name to use!"
    exit
  end
  poller = ActivitiesPoller.new(init_domain, ARGV[0])
  poller.poll_for_activities
  puts "All done!"
end
```

If the user runs the file from the command line (passing it an activity task list as the first argument), this
code will instantiate the poller class and start it polling for activities. Once the poller completes (after it has
launched the final activity), we just print a message and exit.

That's it for the activities poller. All that's left for you to do is to run the code and see how it works, in
[Subscription Workflow Tutorial: Running the Workflow](swf-sns-tutorial-running-the-workflow.md "swf-sns-tutorial-running-the-workflow.md").

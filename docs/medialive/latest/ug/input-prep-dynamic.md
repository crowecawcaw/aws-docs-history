# Input prepare and dynamic inputs

You can prepare for an input switch in a MediaLive channel when the associated input is a [dynamic input](dynamic-inputs.md "dynamic-inputs.md"). A dynamic input has a variable in its path. Each
time that you add the input to the schedule, you specify a _replacement
string_ to replace the variable with a file.

When you set up the prepare input action, you must specify this replacement string. The
string must exactly match the replacement string in the switch action. If the strings are not
identical, MediaLive won't prepare the input in advance.

You might use this dynamic input more than once in the channel, and the replacement string
might be different in each instance. Make sure that you change the string in each prepare
action.

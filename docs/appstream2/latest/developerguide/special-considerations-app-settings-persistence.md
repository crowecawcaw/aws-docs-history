# Special Considerations

for Application Settings Persistence

When you create a stack in the AppStream 2.0 console, in **Step 3: User
Settings**, if you use the same settings group under **Application
settings persistence** as another stack that uses different regional
settings, only one set of regional settings is used for both stacks. For each user, the
default regional settings for the stack that the user logs into first automatically
override the default regional settings of any other stacks in the same application
settings group. To avoid this problem, do not use the same application settings group
for two different stacks that have different regional settings.

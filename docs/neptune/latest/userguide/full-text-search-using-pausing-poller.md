# Disabling and re-enabling the stream poller process

###### Warning

Be careful when you disable the stream poller process! Data loss can
occur if the process is paused for longer than the stream expiry window.
The default window is 7 days, but starting with engine version [1.2.0.0](engine-releases-1.2.0.md "engine-releases-1.2.0.md"), you can set
a custom stream expiry window up to a maximum of 90 days.

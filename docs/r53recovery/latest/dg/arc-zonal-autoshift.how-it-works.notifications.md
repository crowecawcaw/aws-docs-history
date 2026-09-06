

# Notification for practice runs and autoshifts
<a name="arc-zonal-autoshift.how-it-works.notifications"></a>

You can choose to be notified about practice runs and autoshifts for your resource by setting up Amazon EventBridge notifications. You can set up EventBridge notifications even when you haven't enabled zonal autoshift for any resources, known as *autoshift observer notification*. With autoshift observer notification, you are notified about all autoshifts that ARC starts when an Availability Zone is potentially impaired. Note that you must configure this option in each AWS Region that you want to receive notifications about. 

To see the steps for enabling autoshift observer notification, see [Enabling or disabling autoshift observer notification](arc-zonal-autoshift.enable-autoshift-observer.md). To learn more about notification options and how to configure them in EventBridge, see [Using zonal autoshift with Amazon EventBridge](eventbridge-zonal-autoshift.md).
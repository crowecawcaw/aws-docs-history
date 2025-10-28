# Service notifications

AMS sends outbound service requests, or service notifications, when you
need to act on, or be aware of, something that might impact your account or resources, including:

- Infrastructure impact: AMS sends a service notification when there is an underlying AWS service
  impacting your infrastructure, and you need to take action before a certain date, or you may have an outage.
- EC2 Hardware issues: AMS sends service notifications out for EC2 hardware issues that require you
  to reboot an EC2 instance before a certain date, or letting you know that AMS will reboot the instance for
  you. This
  is an important notice because reboot can cause an outage and you must respond with an acceptable date, or
  create an RFC with ct-09qbhy7kvtxqw, to reboot the instance yourself. A service notification like this automatically
  closes in five days if you do not respond.

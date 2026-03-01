# Add triggers for a Lambda@Edge function

A Lambda@Edge trigger is one combination of a CloudFront distribution, cache behavior, and
event that causes a function to execute. For example, you can create a trigger that
causes the function to execute when CloudFront receives a request from a viewer for a specific
cache behavior you set up for your distribution. You can specify one or more CloudFront
triggers.

###### Tip

When you create a CloudFront distribution, you specify settings that tell CloudFront how to
respond when it receives different requests. The default settings are called the
_default cache behavior_ for the distribution. You can set up
additional cache behaviors that define how CloudFront responds under specific
circumstances, for example, when it receives a request for a specific file type. For
more information, see [Cache behavior settings](DownloadDistValuesCacheBehavior.md "DownloadDistValuesCacheBehavior.md").

When you first create a Lambda function, you can specify only _one_
trigger. You can add more triggers to the same function later by using the Lambda console
or by editing the distribution in the CloudFront console.

- The Lambda console works well if you want to add more triggers to a function
  for the same CloudFront distribution.
- The CloudFront console can be better if you want to add triggers for multiple
  distributions because it's easier to find the distribution that you want to
  update. You can also update other CloudFront settings at the same time.

###### Topics

- [CloudFront events that can trigger a Lambda@Edge function](lambda-cloudfront-trigger-events.md "lambda-cloudfront-trigger-events.md")
- [Choose the event to trigger the function](lambda-how-to-choose-event.md "lambda-how-to-choose-event.md")
- [Add triggers to a Lambda@Edge function](lambda-edge-add-triggers-console.md "lambda-edge-add-triggers-console.md")

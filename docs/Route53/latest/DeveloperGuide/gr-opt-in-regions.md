

# Opt-in Region considerations for Route 53 Global Resolver
<a name="gr-opt-in-regions"></a>

Some AWS Regions are active by default for your AWS account. Certain Regions are activated only when you manually select them. This document refers to those Regions as opt-in Regions. In contrast, Regions that are active by default, as soon as your AWS account is created, are referred to as commercial Regions, default Regions, or simply, Regions.

AWS Regions introduced after March 20, 2019 are deployed as opt-in Regions. In an opt-in Region, your account is not enabled within that Region. Your Route 53 Global Resolver data is not replicated to the Region unless you choose to opt into use of that Region. For more information about opt-in Regions, see [Managing AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html).

When using Route 53 Global Resolver in opt-in Regions, here are some considerations to keep in mind.
+ To select an opt-in Region for your Global Resolver deployment, your account must be opted-in to the Region.
+ You can select any set of default or opt-in Regions for your Global Resolver.
+ If you have selected an AWS opt-in Region for a Global Resolver, when you opt-out your account from that Region, the service will stop propagating your global resolver data to that Region. It will also trigger deletion of all your resources in that Region. This will cause impairment to your DNS traffic destined to that Region as resources get cleaned up, but traffic will eventually direct away to your other selected Regions.
+ Similarly, if you have selected only a set of opt-in Regions for your Global Resolver and you opt-out your account from all the Regions, it will effectively delete your Global Resolver.
+ You might also select any default or opt-in Region for your Observability Region where your DNS logs will be delivered. If you choose to opt-out your account, the service will stop sending DNS logs to your destinations in that Region. To prevent impairment of log delivery, we recommend setting up a new log delivery destination in a separate Region and update the observability Region in your Global Resolver accordingly.
+ Global Resolver does not support expanding and contracting Regions in your Global Resolver at this time. We recommend you plan ahead which Regions you intend to opt-in and select before creating a Global Resolver.
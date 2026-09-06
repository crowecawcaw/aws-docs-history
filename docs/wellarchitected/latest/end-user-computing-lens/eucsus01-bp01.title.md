

# EUCSUS01-BP01 Choose the appropriate fleet type
<a name="eucsus01-bp01.title"></a>

By selecting [Always-On instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/fleet-type.html) in WorkSpaces Applications, your instances are constantly kept running and ready to receive user connection. With [On-Demand](https://docs.aws.amazon.com/appstream2/latest/developerguide/fleet-type.html), your instances will be provisioned based on your scaling policies, but instances start only when users initiate the connection. [Elastic fleet](https://docs.aws.amazon.com/appstream2/latest/developerguide/fleet-type.html) is a fleet of instances managed by AWS directly, and you only pay when your user is launching a new session and there is no scaling management.

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-93a.title"></a>

Encourage the usage of On-Demand fleet type. With On-Demand, streaming instances run only when users are streaming and therefore have a lower carbon footprint in comparison to Always-On fleets. The number of streaming instances will still require auto scaling rules. Once the user disconnects, the instance is terminated. 

 

An additional option is to select a multi-session fleet according to the performance pillar to select the right instances type.

 

Elastic fleets offer a pool of streaming instances managed by WorkSpaces Applications service. When you use Elastic fleets, an app block (also known as a virtual hard disk) will be downloaded and mounted from Amazon S3. You do not have to configure scaling policies, so you will not consume and reserve unnecessary resources. Elastic fleets do not support domain join, for further details see: [Using Active Directory with WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory.html).
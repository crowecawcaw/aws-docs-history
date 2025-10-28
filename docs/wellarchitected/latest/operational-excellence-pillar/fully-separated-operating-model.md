# Fully separated operating model

In the following diagram, on the vertical axis we have
Applications and Platform. Applications refer to the
workload serving a business outcome and can be custom developed
or purchased software. Platform refers to the physical and
virtual infrastructure and other software that supports that
workload.

On the horizontal axis, we have Engineering and Operations.
Engineering refers to the development, building, and testing of
applications and infrastructure. Operations is the deployment,
update, and ongoing support of applications and infrastructure.

![Traditional model diagram](images/full-seperate.png)
_Traditional model_

Historically, organizations embraced frameworks such as ITIL or standards like ISO and shaped their operational activties around them, which often resulted in a fully-separated topology. In this model, activities in each quadrant are performed by a separate team. Work is passed between teams through mechanisms such as work requests, queues, tickets, or by using an IT service management (ITSM) system.

The transition of tasks to or between teams increases
complexity, and creates bottlenecks and delays. Requests may be
delayed until they are a priority. Defects identified late may
require significant rework and may have to pass through the same
teams and their functions once again. If there are incidents
that require action by engineering teams, their responses are
delayed by the hand off activity.

There is a higher risk of misalignment when business, development, and operations teams are organized around the activities or functions that are being performed. This can lead to teams focusing on their specific responsibilities instead of focusing on achieving business outcomes. Teams may be narrowly specialized, physically isolated, or logically isolated, hindering communication and collaboration.

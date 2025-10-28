# EUCPERF02-BP02 Scale your EUC environment to accommodate the required number of end

users

The number of users accessing the selected AWS EUC service should not affect the
performance of the service itself, as AWS provides both scale and resilience for the
components that affect authentication and streaming of user sessions. Many supporting
components, however, need to be scaled to support the user numbers you intend to deploy.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Understand the backend requirements for your deployment and scale them accordingly.
For example, a WorkSpaces compute instance with 2 vCPU and 4Gb of RAM may offer acceptable
performance to run a targeted application set, but if access to user data or an
application database backend is compromised by server performance or network constraints,
then the user may complain that WorkSpaces is performing badly. Ideally, perform end to end
testing for each application set using scalability testing tools to be sure that they will
deliver acceptable performance in production as the services scale.

# How failover works for unhealthy endpoints

If there are no healthy endpoints in an endpoint group that have a weight greater than zero, Global Accelerator
tries to fail over to a healthy endpoint with a weight greater than zero in another endpoint group.
Note that for this failover, Global Accelerator ignores the traffic dial setting. So if, for example, an endpoint group
has a traffic dial set to zero, Global Accelerator still includes that endpoint group in the failover attempt.

If Global Accelerator doesn't find a healthy endpoint with a weight greater than zero after trying
the three closest endpoint groups (that is, AWS Regions), it routes traffic to a random
endpoint in the endpoint group that is closest to the client. That is, it _fails open_.

Note the following:

- The endpoint group chosen for failover might be one that has a traffic dial
  set to zero.
- The nearest endpoint group might not be the original endpoint group. This is because
  Global Accelerator considers account traffic dial settings when it chooses the original endpoint group.
  For example, let's say your configuration has two endpoints, one healthy and one unhealthy, and
  you've set the weight for each of them to be greater than zero. In this case, Global Accelerator routes traffic
  to the healthy endpoint. However, now say you set the weight of the only healthy endpoint to zero.
  Global Accelerator then tries three additional endpoint groups to find a healthy endpoint with a weight
  greater than zero. If it doesn't find one, Global Accelerator routes traffic to a random endpoint in the
  endpoint group that is closest to the client.

When recovery occurs, that is, Regions are healthy again, Global Accelerator returns to regular routing
behavior. This means that, typically, routing will start back to healthy endpoints with traffic dials that aren't
set to zero in about 30 seconds or so. However, note that established active connections are not moved. They
continue to route to the zero weight Region until the connection is reset by the client or
the server, or until the client makes a new connection.

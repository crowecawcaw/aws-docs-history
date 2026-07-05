# How AMS accesses your account

AMS Accelerate operators can access your account console and instances, in certain circumstances.

![AMS Accelerate console access method.](images/acc-op-console-access-method2.png)
AMS operators use the internal AMS Accelerate access service to access your accounts in a secured and audited manner.
To access your instances, AMS operators use the same internal AMS access service as the broker and, after access is granted, AMS Accelerate
operators use SSM session manager to gain access by using session credentials. RDP access for Windows instances is provided by establishing
port forwarding to the instance and creating a local user using SSM. The local user credentials are used for RDP access and removed at the end of the session.

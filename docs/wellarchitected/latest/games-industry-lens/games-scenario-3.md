# Game production in the cloud –

Workstations

The game development process can be highly distributed with teams working on various
aspects of the game from many locations, and it is important that they have access to
workstations and shared storage in order to be productive. In a simple scenario, a game
can be developed by a single game development studio located in a specific office
location. However, in practice, it is more common for developers to contribute to a game
project from many geographic locations, such as a single game studio with many globally
distributed teams in different cities or countries, or work-for-hire studios, contractors,
and co-development studio partners who may support a project by bringing specific
expertise such as art development or game testing, QA, and localization specialization to
the project. Game development also must be able to support remote work so that developers
can be productive from home or other locations. An increasingly popular trend in the games
industry is for newly developed studios to be fully remote without the expectation of
working in an office environment.

The following reference architecture demonstrates how to use AWS for hosting remote
game development workstations using the NICE DCV protocol.

![Reference architecture diagram showing stream game development from anywhere with NICE DCV.](images/game-production-in-the-cloud-workstations.jpg)
_Stream game development from anywhere with NICE
DCV_

1. **NICE DCV** is a streaming protocol that supports
   4K, 60-FPS streaming. Developers using a browser connect via TCP connections whereas
   desktop clients can use QUIC UDP over port 8443 for increased performance.
2. Developers use **AWS Client VPN** for a secure
   connection to network interfaces in the workstation subnets with source network
   address translation (SNAT).
3. **Amazon Route 53** provides private DNS for the
   resources in the VPC as well as inbound and outbound DNS forwarding.
4. **AWS Directory Service** provides managed
   Microsoft Active Directory to enable local game project storage mapped to individual
   users.
5. Workstations are created using an **Amazon Machine Image (AMI)** built with **Image Builder**. Images include
   NICE DCV Server, developer software, registry changes, and drivers such as GPU gaming
   drivers or peripheral drivers. **AWS Marketplace**
   includes common AMIs used for workstations.
6. Fleets of workstations use graphics **Amazon EC2**
   instance types that provide GPUs and are scaled using EC2 Auto Scaling
   groups.
7. A Session Manager Broker enables management of NICE DCV sessions.
8. Local file storage of projects is hosted in **Amazon FSx for
   Windows File Server**. Developers commit to a separate CI/CD pipeline by
   pushing from local storage to source control.

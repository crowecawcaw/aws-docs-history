# Best Practice 1.5 – Implement user

activity monitoring

Configure your SAP applications to provide information about user activity, for
example, response time, number of active users, transaction abandonment rates, and order
processing time. Consider both inside-out approaches (monitoring SAP internal dialogue
response time) and outside-in approaches (deploying agents or robots at end-user locations
geographically) to understand how connectivity plays a role in the experience. Use this
information to help understand how the application is used, patterns of usage, and to
determine when a response is required due to poor performance.

**Suggestion 1.5.1 - Implement user experience monitoring from
end-user locations**

Consider outside-in monitoring approaches by deploying user agents or robots at
end-user locations geographically to understand how network and connectivity play a role
in SAP user experience. Often this type of end-user location-based monitoring can provide
insight and early warning of problems not detectable in the central infrastructure and
applications.

Implement Amazon CloudWatch RUM, SAP, or third-party tools which provide end-user experience
reporting to measure the responsiveness of your SAP application from end-user locations. For
example, SAP provides End-User Experience Monitoring in Solution Manager, and Amazon CloudWatch RUM
allows the deployment of monitoring scripts to measure front-end user experience.

- SAP on AWS Blog: [Monitor and Optimize SAP Fiori User Experience on AWS using CloudWatch RUM](https://aws.amazon.com/blogs/awsforsap/monitor-and-optimize-sap-fiori-user-experience-on-aws/ "https://aws.amazon.com/blogs/awsforsap/monitor-and-optimize-sap-fiori-user-experience-on-aws/")
- SAP Documentation: [SAP User Experience Monitoring](https://help.sap.com/viewer/82f6dd44db4e4518aad4dfce00116fcf/LATEST/en-US/1083786db5f1461c8cff8fbcc1666a4d.html "https://help.sap.com/viewer/82f6dd44db4e4518aad4dfce00116fcf/LATEST/en-US/1083786db5f1461c8cff8fbcc1666a4d.html")
- AWS Marketplace: [Products and Tools for SAP Monitoring](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2 "https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2")

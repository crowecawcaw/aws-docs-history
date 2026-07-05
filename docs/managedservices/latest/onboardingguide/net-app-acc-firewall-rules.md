End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# Firewall Rules for Application Access

You must open the following ports for traffic through your firewall:

- From your on-premise network to your new application VPC CIDRs in both the ingress
  and egress directions.
- From your new application VPC CIDRs to your on-premise network in both the ingress
  and egress directions (if your cloud applications need to reach out to your on-premise applications).

| **Port** | **Protocol** | **Service**      | **From/To**        | **To/From**         |
| -------- | ------------ | ---------------- | ------------------ | ------------------- |
| 80       | TCP          | HTTP Web Access  | On Premise Network | AMS Application VPC |
| 443      | TCP          | HTTPS Web Access | On Premise Network | AMS Application VPC |

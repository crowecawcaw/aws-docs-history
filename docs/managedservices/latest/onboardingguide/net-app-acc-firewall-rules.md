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

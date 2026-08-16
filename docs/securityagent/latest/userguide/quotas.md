# Service Quotas

AWS Security Agent has quotas that limit the number of resources you can create and the rate at which you can perform operations. Quotas marked as adjustable can be increased by submitting a request through AWS Support. For more information, see [Creating support cases and case management.](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md")

Quotas limit capacity but don’t limit spending. The monthly quotas on this page cap how many reviews you can run, and reaching one blocks additional reviews until the next month. They don’t cap what you spend, and a quota increase doesn’t change your rate. For more information, see [Pricing and billing](pricing.md "pricing.md").

## Operations Quotas

Operations quotas limit the monthly usage of security testing and review features to help manage service capacity.

| Resource        | Scope                            | Quota | Adjustable |
| --------------- | -------------------------------- | ----- | ---------- |
| Design reviews  | Per month per account per region | 200   | Yes        |
| PR code reviews | Per month per account per region | 1,000 | Yes        |

## Configuration Quotas

Configuration quotas limit the number of resources and settings you can configure in your AWS Security Agent environment.

| Resource                             | Scope                  | Quota | Adjustable |
| ------------------------------------ | ---------------------- | ----- | ---------- |
| Agent Spaces                         | Per account per region | 100   | Yes        |
| Integrations                         | Per account per region | 20    | No         |
| Integrated resources per integration | Per integration        | 50    | No         |
| Security requirement packs           | Per account per region | 20    | No         |
| Security requirements per pack       | Per pack               | 30    | No         |
| Enabled security requirements        | Per account per region | 150   | No         |
| Pentest projects                     | Per account per region | 1,000 | Yes        |
| Concurrent pentest runs              | Per account per region | 5     | Yes        |
| Code review projects                 | Per account per region | 1,000 | Yes        |
| Concurrent code review runs          | Per account per region | 5     | Yes        |

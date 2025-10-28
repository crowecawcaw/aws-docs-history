# Embedding security

Amazon Quick Sight provides a secure platform that allows you to distribute dashboards and insights to tens of thousands of users with multiple-region availability and built-in redundancy. Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

## Quick Sight manages who sees content

By default, Quick Sight only allows users who have access to content in the console see that same content in an embedded view. For anonymous (unregistered) users, content access can be governed with row level security (RLS) tags. Additionally, Quick Sight has the capability to share assets to anyone on the internet with [1-click public embedding](../user/embedded-analytics-1-click-public.md "../user/embedded-analytics-1-click-public.md").

## Quick Sight manages where you see content

Quick Sight offers a variety of solutions to control where embedding can take place. To ensure embedding is only done intentionally, Quick Sight will only embed on domains that are allow-listed. You can add static domains to your allow-list through the Quick Sight console, or you can dynamically add a domain at runtime. Additionally, you can limit access to your organization's Quick Sight account to a predefined list of Internet Protocol (IP) address ranges.

## Quick Sight manages what you see

Quick Sight allows you to restrict access to a dataset. You can do this before or after you have shared the dataset. When a dataset owner views the content, they can still see all the data. When you share the dataset with readers, they can only see the data applicable to them individually, as restricted by the permission dataset rules.

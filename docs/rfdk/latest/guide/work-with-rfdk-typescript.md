# Working with the RFDK in TypeScript

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

## Installing peer dependencies

The following command (requires [jq](https://stedolan.github.io/jq/ "https://stedolan.github.io/jq/")) installs all of the peer dependencies required by RFDK.
Run it from the root of your CDK application directory.

```
npm view --json aws-rfdk peerDependencies | jq '. | to_entries[] | .key + "@" + .value' | xargs npm i --save
```

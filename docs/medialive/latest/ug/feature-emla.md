

# Running channels in AWS Elemental MediaLive Anywhere
<a name="feature-emla"></a>

Your organization can deploy a AWS Elemental MediaLive Anywhere cluster of on-premises nodes, and run channels on those nodes. This means that you can run channels on your own hardware, as well as running channels in the regular way, in the AWS Cloud.

You decide where to run the channel when you create the channel. In this case the channel is a MediaLive Anywhere channel. Several new rules apply:

## Workflow design and available features
<a name="feature-emla-supported-features"></a>
+ The channel must be [single-pipeline channel](#feature-emla). The inputs can be a combination of single-class inputs (such as SMPTE 2110) and standard-class inputs. MediaLive ignores content from the second pipeline, if there is any. You can also instruct the upstream system to send content to just one of the pipelines. See [Choosing the channel class and input class](class-channel-input.md).
+ You can't run the channel on your Amazon VPC.
+ Some input types don't work in a MediaLive Anywhere channel. See [Input deployments: AWS Cloud and MediaLive Anywhere](inputs-emla.md).

## Quotas and charges
<a name="feature-emla-supported-quotas-charges"></a>
+ There is a new quota category: MediaLive Anywhere inputs. To view quotas, see the link in [Quotas in MediaLive](limits.md).
+ Charges for inputs, outputs, and channels in MediaLive Anywhere mode are different from charges for MediaLive in the AWS Cloud. See [https://aws.amazon.com/medialive/features/anywhere/](https://aws.amazon.com/medialive/features/anywhere/).

## Getting started
<a name="feature-emla-next-steps"></a>

For information about setting up the cluster of nodes in your organization's premises, see [Setting up AWS Elemental MediaLive Anywhere](setup-emla.md).
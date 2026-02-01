# Setting up a

single-pipeline channel with upgrade options

When you followed the [guidelines](pipeline-redundancy-guidelines.md "pipeline-redundancy-guidelines.md")
for implementing pipeline redundancy in a MediaLive channel, you might have decided that you
want to create the channel without pipeline redundancy. But you might want to allow for
easy upgrade to pipeline redundancy later.

In this case, follow these guidelines when you plan the workflow:

- When you [create
  inputs](medialive-inputs.md "medialive-inputs.md"), set up all the inputs as standard-class
  inputs.

Some inputs are always set up as standard-class inputs. For all other inputs,
set the **Input class** field to **Standard
input**.

- When you create the channel, do the following:
  - Set up the channel as a single-pipeline channel.
    See [Complete channel and input details](creating-a-channel-step1.md "creating-a-channel-step1.md").
  - At the step to [attach inputs
    to the channel](creating-a-channel-step2.md "creating-a-channel-step2.md"), double-check that the
    inputs you attach are standard-class inputs.

- Contact the upstream system and request that they provide
  _one_ content
  source.

## How a

single-pipeline channel works

When you set up a single-pipeline channel with the option to
easily upgrade, the channel is a single-pipeline channel but the
inputs are all standard-class inputs.

- The channel contains one pipeline—pipeline 0.
- Each standard-class input contains two pipelines.
  However, only one of the pipelines is connected to a
  content source. The other input pipeline is
  inactive.

As this diagram illustrates, the upstream system provides one
instance of the source content to the input, to the pipeline
that is indicated by the blue line. The input provides that one
instance to the one pipeline in the channel. The channel
produces one instance of the output for the downstream system.
The other pipeline in the input (the green pipeline) is always
inactive.

![Diagram showing single-pipeline channel with standard-class input connecting upstream and downstream systems.](images/pipeline-redundancy-single-channel-standard-input.png)

## Failure

handling

If there is a problem that causes a pipeline to stop
functioning, MediaLive stops producing output. The downstream system
stops receiving output.



# Choosing the channel class and input class
<a name="class-channel-input"></a>

One of the characteristics of a MediaLive channel is its class. One of the characteristics of a MediaLive input is its class. You set both the channel class and input class to implement or to omit pipeline redundancy.

Read this section for an overview of channel class and input class. Then for detailed information about implementing or omitting pipeline redundancy, see [Implementing pipeline redundancy](plan-redundancy-mode.md).

## About channel classes
<a name="about-channel-class"></a>

When you [plan the workflow](plan-redundancy.md), you must decide on the class for the channel. There are two channel classes:
+ Standard class

  A *standard channel *has two encoding pipelines. When there are two pipelines, both pipelines perform the encoding. If one pipeline fails, output to the downstream system can continue, from the other pipeline. For more information and diagrams about exactly how MediaLive handles the failure, see [Implementing pipeline redundancy](plan-redundancy-mode.md).
+ Single-pipeline class

  A *single-pipeline channel* has one encoding pipeline. If the single pipeline fails, output to the downstream system stops.

You set the channel class when you [create the channel](creating-a-channel-step1.md). You can [upgrade or downgrade](pipeline-redundancy-change.md) the class of an existing channel. 

## About input classes
<a name="pipeline-redundancy-input-class"></a>

As part of the steps for implementing or omitting pipeline redundancy in the channel, you must decide on the class for each input. There are two input classes:
+ Standard class

  A standard-class input has two pipelines.
+ A single-class input has one pipeline.

Most inputs can be standard-class or single-class. In this case, you set the channel class when you [create the input](medialive-inputs.md). Some inputs can only be standard-class, and some other inputs can only be single-class. For more information, see [Supported input class](inputs-single-standard-vpc.md).

## Combinations of channel and input class
<a name="combinations-channel-input-class"></a>

The following table summarizes the valid combinations of channel class and input class. 


| Channel | Inputs | 
| --- | --- | 
| Standard channel | All inputs must be standard-class inputs. In this case, you can implement pipeline redundancy or omit it. See [Deciding whether to implement pipeline redundancy](pipeline-redundancy-guidelines.md). | 
| Single-pipeline channel | These possibilities apply:+  The channel has only single-class inputs. <br />+  The channel has only standard-class inputs. <br />+  The channel has a mix of standard-class and single-class inputs. Typically, you set up with a mix because some of your inputs can only be standard-class and/or some can only be single-class. <br />The combination that applies to a channel determines if you can implement pipeline redundancy. See [Deciding whether to implement pipeline redundancy](pipeline-redundancy-guidelines.md). | 
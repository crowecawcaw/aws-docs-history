

# AWS Flow Framework for Java Packages
<a name="awsflow.packages"></a>

This section provides an overview of the packages included with the AWS Flow Framework for Java. For more information about each package, see the com.amazonaws.services.simpleworkflow.flow in the [AWS SDK for Java API Reference](https://docs.aws.amazon.com/sdk-for-java/latest/reference/).

[com.amazonaws.services.simpleworkflow.flow](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/package-summary.html)  
Contains components that integrate with Amazon SWF.

[com.amazonaws.services.simpleworkflow.flow.annotations](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/annotations/package-summary.html)  
Contains the annotations used by the AWS Flow Framework for Java programming model.

[com.amazonaws.services.simpleworkflow.flow.aspectj](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/aspectj/package-summary.html)  
Contains AWS Flow Framework for Java components required for features such as [@Asynchronous](annotations.md#annotations-asynchronous) and [@ExponentialRetry](annotations.md#annotations-exponentialretry).

[com.amazonaws.services.simpleworkflow.flow.common](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/common/package-summary.html)  
Contains common utilities such as framework-defined constants.

[com.amazonaws.services.simpleworkflow.flow.core](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/core/package-summary.html)  
Contains core features such as `Task` and `Promise`.

[com.amazonaws.services.simpleworkflow.flow.generic](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/generic/package-summary.html)  
Contains core components, such as generic clients, that other features build on.

[com.amazonaws.services.simpleworkflow.flow.interceptors](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/interceptors/package-summary.html)  
Contains implementations of framework provided decorators including `RetryDecorator`.

[com.amazonaws.services.simpleworkflow.flow.junit](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/junit/package-summary.html)  
Contains components that provide Junit integration.

[com.amazonaws.services.simpleworkflow.flow.pojo](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/pojo/package-summary.html)  
Contains classes that implement activity and workflow definitions for the annotation-based programming model.

[com.amazonaws.services.simpleworkflow.flow.spring](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/spring/package-summary.html)  
Contains components that provide Spring integration.

[com.amazonaws.services.simpleworkflow.flow.test](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/test/package-summary.html)  
Contains helper classes, such as `TestWorkflowClock`, for unit testing workflow implementations.

[com.amazonaws.services.simpleworkflow.flow.worker](https://docs.aws.amazon.com//AWSJavaSDK/latest/javadoc/com/amazonaws/services/simpleworkflow/flow/worker/package-summary.html)  
Contains implementations of activity and workflow workers.
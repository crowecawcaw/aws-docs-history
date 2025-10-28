# Child Workflow Executions

In the examples so far, we have started workflow execution directly from an application.
However, a workflow execution may be started from within a workflow by calling the workflow
entry point method on the generated client. When a workflow execution is started from the context of another workflow
execution, it is called a child workflow execution. This allows you to refactor complex
workflows into smaller units and potentially share them across different workflows. For
example, you can create a payment processing workflow and call it from an order processing
workflow.

Semantically, the child workflow execution behaves the same as a standalone workflow except
for the following differences:

1. When the parent workflow terminates due to an explicit action by the user—for example, by
   calling the `TerminateWorkflowExecution` Amazon SWF API, or it is terminated due to a timeout—then the
   fate of the child workflow execution will be determined by a child policy. You can set this
   child policy to terminate, cancel, or abandon (keep running) child workflow executions.
2. The output of the child workflow (return value of the entry point method) can be used by
   the parent workflow execution just like the `Promise<T>` returned by an asynchronous method.
   This is different from standalone executions where the application must get the output by using
   Amazon SWF APIs.
   In the following example, the `OrderProcessor` workflow creates a `PaymentProcessor` child
   workflow:

```
@Workflow
@WorkflowRegistrationOptions(defaultExecutionStartToCloseTimeoutSeconds = 60,
              defaultTaskStartToCloseTimeoutSeconds = 10)
public interface OrderProcessor {

    @Execute(version = "1.0")
    void processOrder(Order order);
}

public class OrderProcessorImpl implements OrderProcessor {
    PaymentProcessorClientFactory factory
         = new PaymentProcessorClientFactoryImpl();

    @Override
    public void processOrder(Order order) {
        float amount = order.getAmount();
        CardInfo cardInfo = order.getCardInfo();

        PaymentProcessorClient childWorkflowClient = factory.getClient();
        childWorkflowClient.processPayment(amount, cardInfo);
    }

}

@Workflow
@WorkflowRegistrationOptions(defaultExecutionStartToCloseTimeoutSeconds = 60,
                 defaultTaskStartToCloseTimeoutSeconds = 10)
public interface PaymentProcessor {

    @Execute(version = "1.0")
    void processPayment(float amount, CardInfo cardInfo);

}

public class PaymentProcessorImpl implements PaymentProcessor {
    PaymentActivitiesClient activitiesClient = new PaymentActivitiesClientImpl();

    @Override
    public void processPayment(float amount, CardInfo cardInfo) {
        Promise<PaymentType> payType = activitiesClient.getPaymentType(cardInfo);
        switch(payType.get()) {
        case Visa:
            activitiesClient.processVisa(amount, cardInfo);
            break;
        case Amex:
            activitiesClient.processAmex(amount, cardInfo);
            break;
      default:
         throw new UnSupportedPaymentTypeException();
        }
    }

}

@Activities(version = "1.0")
@ActivityRegistrationOptions(defaultTaskScheduleToStartTimeoutSeconds = 3600,
                             defaultTaskStartToCloseTimeoutSeconds = 3600)
public interface PaymentActivities {

    PaymentType getPaymentType(CardInfo cardInfo);

    void processVisa(float amount, CardInfo cardInfo);

    void processAmex(float amount, CardInfo cardInfo);

}
```

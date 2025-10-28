# Testability and Dependency Injection

###### Topics

- [Spring Integration](#test.spring "#test.spring")
- [JUnit Integration](#test.junit "#test.junit")
  The framework is designed to be Inversion of Control (IoC) friendly. Activity and workflow implementations as
  well as the framework supplied workers and context objects can be configured and instantiated using containers like
  Spring. Out of the box, the framework provides integration with the Spring Framework. In addition, integration with
  JUnit has been provided for unit testing workflow and activity implementations.

## Spring Integration

The com.amazonaws.services.simpleworkflow.flow.spring package contains classes that make it easy to use the
Spring framework in your applications. These include a custom Scope and Spring-aware activity and workflow
workers: `WorkflowScope`, `SpringWorkflowWorker` and `SpringActivityWorker`.
These classes allow you to configure your workflow and activity implementations as well as the workers entirely
through Spring.

### WorkflowScope

`WorkflowScope` is a custom Spring Scope implementation provided by the framework. This
scope allows you to create objects in the Spring container whose lifetime is scoped to
that of a decision task. The beans in this scope are instantiated every time a new
decision task is received by the worker. You should use this scope for workflow
implementation beans and any other beans it depends on. The Spring-provided singleton and
prototype scopes should not be used for workflow implementation beans because the
framework requires that a new bean be created for each decision task. Failure to do so
will result in unexpected behavior.

The following example shows a snippet of Spring configuration that registers the
`WorkflowScope` and then uses it for configuring a workflow implementation bean and an activity
client bean.

```
<!-- register AWS Flow Framework for Java WorkflowScope -->
   <bean class="org.springframework.beans.factory.config.CustomScopeConfigurer">
      <property name="scopes">
       <map>
         <entry key="workflow">
          <bean class="com.amazonaws.services.simpleworkflow.flow.spring.WorkflowScope" />
         </entry>
       </map>
      </property>
   </bean>

   <!-- activities client -->
   <bean id="activitiesClient" class="aws.flow.sample.MyActivitiesClientImpl" scope="workflow">
   </bean>

   <!-- workflow implementation -->
   <bean id="workflowImpl" class="aws.flow.sample.MyWorkflowImpl" scope="workflow">
      <property name="client" ref="activitiesClient"/>
      <aop:scoped-proxy proxy-target-class="false" />
   </bean>
```

The line of configuration: `<aop:scoped-proxy proxy-target-class="false" />`, used in the
configuration of the `workflowImpl` bean, is required because the `WorkflowScope` doesn't
support proxying using CGLIB. You should use this configuration for any bean in the `WorkflowScope` that
is wired to another bean in a different scope. In this case, the `workflowImpl` bean needs to be wired to
a workflow worker bean in singleton scope (see complete example below).

You can learn more about using custom scopes in the Spring Framework documentation.

### Spring-Aware Workers

When using Spring, you should use the Spring-aware worker classes provided by the framework:
`SpringWorkflowWorker` and `SpringActivityWorker`. These workers can be injected in your
application using Spring as shown in the next example. The Spring-aware workers implement Spring's
`SmartLifecycle` interface and, by default, automatically start polling for tasks when the Spring
context is initialized. You can turn off this functionality by setting the `disableAutoStartup`
property of the worker to `true`.

The following example shows how to configure a decider. This example uses `MyActivities` and
`MyWorkflow` interfaces (not shown here) and corresponding implementations,
`MyActivitiesImpl` and `MyWorkflowImpl`. The generated client interfaces and implementations
are `MyWorkflowClient`/`MyWorkflowClientImpl` and
`MyActivitiesClient`/`MyActivitiesClientImpl` (also not shown here).

The activities client is injected in the workflow implementation using Spring's auto wire feature:

```
public class MyWorkflowImpl implements MyWorkflow {
   @Autowired
   public MyActivitiesClient client;

   @Override
   public void start() {
      client.activity1();
   }
}
```

The Spring configuration for the decider is as follows:

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xmlns:aop="http://www.springframework.org/schema/aop"
   xmlns:context="http://www.springframework.org/schema/context"
   xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
   http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-2.5.xsd
   http://www.springframework.org/schema/context
    http://www.springframework.org/schema/context/spring-context-3.0.xsd">

   <!-- register custom workflow scope -->
   <bean class="org.springframework.beans.factory.config.CustomScopeConfigurer">
      <property name="scopes">
       <map>
         <entry key="workflow">
          <bean class="com.amazonaws.services.simpleworkflow.flow.spring.WorkflowScope" />
         </entry>
       </map>
      </property>
   </bean>
   <context:annotation-config/>

   <bean id="accesskeys" class="com.amazonaws.auth.BasicAWSCredentials">
      <constructor-arg value="{AWS.Access.ID}"/>
      <constructor-arg value="{AWS.Secret.Key}"/>
   </bean>

   <bean id="clientConfiguration" class="com.amazonaws.ClientConfiguration">
      <property name="socketTimeout" value="70000" />
   </bean>

   <!-- Amazon SWF client -->
   <bean id="swfClient"
      class="com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflowClient">
      <constructor-arg ref="accesskeys" />
      <constructor-arg ref="clientConfiguration" />
      <property name="endpoint" value="{service.url}" />
   </bean>

   <!-- activities client -->
   <bean id="activitiesClient" class="aws.flow.sample.MyActivitiesClientImpl" scope="workflow">
   </bean>

   <!-- workflow implementation -->
   <bean id="workflowImpl" class="aws.flow.sample.MyWorkflowImpl" scope="workflow">
      <property name="client" ref="activitiesClient"/>
      <aop:scoped-proxy proxy-target-class="false" />
   </bean>

   <!-- workflow worker -->
   <bean id="workflowWorker"
      class="com.amazonaws.services.simpleworkflow.flow.spring.SpringWorkflowWorker">
      <constructor-arg ref="swfClient" />
      <constructor-arg value="domain1" />
      <constructor-arg value="tasklist1" />
      <property name="registerDomain" value="true" />
      <property name="domainRetentionPeriodInDays" value="1" />
      <property name="workflowImplementations">
         <list>
            <ref bean="workflowImpl" />
         </list>
      </property>
   </bean>
</beans>
```

Because the `SpringWorkflowWorker` is fully configured in Spring and automatically starts
polling when the Spring context is initialized, the host process for the decider is
simple:

```
public class WorkflowHost {
   public static void main(String[] args){
      ApplicationContext context
          = new FileSystemXmlApplicationContext("resources/spring/WorkflowHostBean.xml");
      System.out.println("Workflow worker started");
   }
}
```

Similarly, the activity worker can be configured as follows:

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xmlns:aop="http://www.springframework.org/schema/aop"
   xmlns:context="http://www.springframework.org/schema/context"
   xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
   http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-2.5.xsd
   http://www.springframework.org/schema/context
    http://www.springframework.org/schema/context/spring-context-3.0.xsd">

   <!-- register custom scope -->
   <bean class="org.springframework.beans.factory.config.CustomScopeConfigurer">
      <property name="scopes">
         <map>
            <entry key="workflow">
               <bean
                  class="com.amazonaws.services.simpleworkflow.flow.spring.WorkflowScope" />
            </entry>
         </map>
      </property>
   </bean>

   <bean id="accesskeys" class="com.amazonaws.auth.BasicAWSCredentials">
      <constructor-arg value="{AWS.Access.ID}"/>
      <constructor-arg value="{AWS.Secret.Key}"/>
   </bean>

   <bean id="clientConfiguration" class="com.amazonaws.ClientConfiguration">
      <property name="socketTimeout" value="70000" />
   </bean>

   <!-- Amazon SWF client -->
   <bean id="swfClient"
      class="com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflowClient">
      <constructor-arg ref="accesskeys" />
      <constructor-arg ref="clientConfiguration" />
      <property name="endpoint" value="{service.url}" />
   </bean>

   <!-- activities impl -->
   <bean name="activitiesImpl" class="asadj.spring.test.MyActivitiesImpl">
   </bean>

   <!-- activity worker -->
   <bean id="activityWorker"
      class="com.amazonaws.services.simpleworkflow.flow.spring.SpringActivityWorker">
      <constructor-arg ref="swfClient" />
      <constructor-arg value="domain1" />
      <constructor-arg value="tasklist1" />
      <property name="registerDomain" value="true" />
      <property name="domainRetentionPeriodInDays" value="1" />
      <property name="activitiesImplementations">
         <list>
            <ref bean="activitiesImpl" />
         </list>
      </property>
   </bean>
</beans>
```

The activity worker host process is similar to the decider:

```
public class ActivityHost {
   public static void main(String[] args) {
      ApplicationContext context = new FileSystemXmlApplicationContext(
      "resources/spring/ActivityHostBean.xml");
      System.out.println("Activity worker started");
   }
}
```

### Injecting Decision Context

If your workflow implementation depends on the context objects, then you can easily inject
them through Spring as well. The framework automatically registers context-related beans
in the Spring container. For example, in the following snippet, the various context
objects have been auto wired. No other Spring configuration of the context objects is
required.

```
public class MyWorkflowImpl implements MyWorkflow {
   @Autowired
   public MyActivitiesClient client;
   @Autowired
   public WorkflowClock clock;
   @Autowired
   public DecisionContext dcContext;
   @Autowired
   public GenericActivityClient activityClient;
   @Autowired
   public GenericWorkflowClient workflowClient;
   @Autowired
   public WorkflowContext wfContext;
   @Override
   public void start() {
      client.activity1();
   }
}
```

If you want to configure the context objects in the workflow implementation through Spring
XML configuration, then use the bean names declared in the `WorkflowScopeBeanNames` class in the
com.amazonaws.services.simpleworkflow.flow.spring package. For example:

```
<!-- workflow implementation -->
<bean id="workflowImpl" class="asadj.spring.test.MyWorkflowImpl" scope="workflow">
   <property name="client" ref="activitiesClient"/>
   <property name="clock" ref="workflowClock"/>
   <property name="activityClient" ref="genericActivityClient"/>
   <property name="dcContext" ref="decisionContext"/>
   <property name="workflowClient" ref="genericWorkflowClient"/>
   <property name="wfContext" ref="workflowContext"/>
   <aop:scoped-proxy proxy-target-class="false" />
</bean>
```

Alternatively, you may inject a `DecisionContextProvider` in the workflow implementation
bean and use it to create the context. This can be useful if you want to provide custom
implementations of the provider and context.

### Injecting Resources in Activities

You can instantiate and configure activity implementations using an Inversion of Control (IoC) container and
easily inject resources like database connections by declaring them as properties of the
activity implementation class. Such resources will typically be scoped as singletons. Note
that activity implementations are called by the activity worker on multiple threads.
Therefore, access to shared resources must be synchronized.

## JUnit Integration

The framework provides JUnit extensions as well as test implementations of the context
objects, such as a test clock, that you can use to write and run unit tests with JUnit. With
these extensions, you can test your workflow implementation locally inline.

### Writing a Simple Unit Test

In order to write tests for your workflow, use the `WorkflowTest` class in the
com.amazonaws.services.simpleworkflow.flow.junit package. This class is a
framework-specific JUnit `MethodRule` implementation and runs your workflow code locally,
calling activities inline as opposed to going through Amazon SWF. This gives you the
flexibility to run your tests as frequently as you desire without incurring any
charges.

In order to use this class, simply declare a field of type `WorkflowTest` and
annotate it with the `@Rule` annotation. Before running your tests, create a
new `WorkflowTest` object and add your activity and workflow implementations to
it. You can then use the generated workflow client factory to create a client and start an
execution of the workflow. The framework also provides a custom JUnit runner,
`FlowBlockJUnit4ClassRunner`, that you must use for your workflow tests. For
example:

```
@RunWith(FlowBlockJUnit4ClassRunner.class)
public class BookingWorkflowTest {

    @Rule
    public WorkflowTest workflowTest = new WorkflowTest();

    List<String> trace;

    private BookingWorkflowClientFactory workflowFactory
         = new BookingWorkflowClientFactoryImpl();

    @Before
    public void setUp() throws Exception {
        trace = new ArrayList<String>();
        // Register activity implementation to be used during test run
        BookingActivities activities = new BookingActivitiesImpl(trace);
        workflowTest.addActivitiesImplementation(activities);
        workflowTest.addWorkflowImplementationType(BookingWorkflowImpl.class);
    }

    @After
    public void tearDown() throws Exception {
        trace = null;
    }

    @Test
    public void testReserveBoth() {
        BookingWorkflowClient workflow = workflowFactory.getClient();
        Promise<Void> booked = workflow.makeBooking(123, 345, true, true);
        List<String> expected = new ArrayList<String>();
        expected.add("reserveCar-123");
        expected.add("reserveAirline-123");
        expected.add("sendConfirmation-345");
        AsyncAssert.assertEqualsWaitFor("invalid booking", expected, trace, booked);
    }
}
```

You can also specify a separate task list for each activity implementation that you add
to `WorkflowTest`. For example, if you have a workflow implementation that schedules
activities in host-specific task lists, then you can register the activity in the task
list of each host:

```
for (int i = 0; i < 10; i++) {
    String hostname = "host" + i;
    workflowTest.addActivitiesImplementation(hostname,
                                             new ImageProcessingActivities(hostname));
}
```

Notice that the code in the `@Test` is asynchronous. Therefore, you should use the
asynchronous workflow client to start an execution. In order to verify the results of your
test, an `AsyncAssert` help class is also provided. This class allows you to wait for
promises to become ready before verifying results. In this example, we wait for the result
of the workflow execution to be ready before verifying the test output.

If you are using Spring, then the `SpringWorkflowTest` class can be used instead
of the `WorkflowTest` class. `SpringWorkflowTest` provides
properties that you can use to configure activity and workflow implementations easily
through Spring configuration. Just like the Spring-aware workers, you should use the
`WorkflowScope` to configure workflow implementation beans. This ensures that
a new workflow implementation bean is created for every decision task. Make sure to
configure these beans with the scoped-proxy proxy-target-class setting set to
`false`. See the Spring Integration section for more details. The example
Spring configuration shown in the Spring Integration section can be changed to test the
workflow using `SpringWorkflowTest`:

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:aop="http://www.springframework.org/schema/aop"
  xmlns:context="http://www.springframework.org/schema/context"
  xsi:schemaLocation="http://www.springframework.org/schema/beans ht
tp://www.springframework.org/schema/beans/spring-beans.xsd
http://www.springframework.org/schema/aop http://www.springframe
work.org/schema/aop/spring-aop-2.5.xsd
http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context-3.0.xsd">

  <!-- register custom workflow scope -->
  <bean class="org.springframework.beans.factory.config.CustomScopeConfigurer">
    <property name="scopes">
      <map>
        <entry key="workflow">
          <bean
            class="com.amazonaws.services.simpleworkflow.flow.spring.WorkflowScope" />
        </entry>
      </map>
    </property>
  </bean>
  <context:annotation-config />
  <bean id="accesskeys" class="com.amazonaws.auth.BasicAWSCredentials">
    <constructor-arg value="{AWS.Access.ID}" />
    <constructor-arg value="{AWS.Secret.Key}" />
  </bean>
  <bean id="clientConfiguration" class="com.amazonaws.ClientConfiguration">
    <property name="socketTimeout" value="70000" />
  </bean>

  <!-- Amazon SWF client -->
  <bean id="swfClient"
    class="com.amazonaws.services.simpleworkflow.AmazonSimpleWorkflowClient">
    <constructor-arg ref="accesskeys" />
    <constructor-arg ref="clientConfiguration" />
    <property name="endpoint" value="{service.url}" />
  </bean>

  <!-- activities client -->
  <bean id="activitiesClient" class="aws.flow.sample.MyActivitiesClientImpl"
    scope="workflow">
  </bean>

  <!-- workflow implementation -->
  <bean id="workflowImpl" class="aws.flow.sample.MyWorkflowImpl"
    scope="workflow">
    <property name="client" ref="activitiesClient" />
    <aop:scoped-proxy proxy-target-class="false" />
  </bean>

  <!-- WorkflowTest -->
  <bean id="workflowTest"
    class="com.amazonaws.services.simpleworkflow.flow.junit.spring.SpringWorkflowTest">
    <property name="workflowImplementations">
      <list>
        <ref bean="workflowImpl" />
      </list>
    </property>
    <property name="taskListActivitiesImplementationMap">
      <map>
        <entry>
          <key>
            <value>list1</value>
          </key>
          <ref bean="activitiesImplHost1" />
        </entry>
      </map>
    </property>
  </bean>
</beans>
```

#### Mocking Activity Implementations

You may use the real activity implementations during testing, but if you want to unit test
just the workflow logic, you should mock the activities. This can do this by providing a
mock implementation of the activities interface to the `WorkflowTest` class.
For example:

```
@RunWith(FlowBlockJUnit4ClassRunner.class)
public class BookingWorkflowTest {

    @Rule
    public WorkflowTest workflowTest = new WorkflowTest();

    List<String> trace;

    private BookingWorkflowClientFactory workflowFactory
         = new BookingWorkflowClientFactoryImpl();

    @Before
    public void setUp() throws Exception {
        trace = new ArrayList<String>();
        // Create and register mock activity implementation to be used during test run
        BookingActivities activities = new BookingActivities() {

            @Override
            public void sendConfirmationActivity(int customerId) {
                trace.add("sendConfirmation-" + customerId);
            }

            @Override
            public void reserveCar(int requestId) {
                trace.add("reserveCar-" + requestId);
            }

            @Override
            public void reserveAirline(int requestId) {
                trace.add("reserveAirline-" + requestId);
            }
        };
        workflowTest.addActivitiesImplementation(activities);
        workflowTest.addWorkflowImplementationType(BookingWorkflowImpl.class);
    }

    @After
    public void tearDown() throws Exception {
        trace = null;
    }

    @Test
    public void testReserveBoth() {
        BookingWorkflowClient workflow = workflowFactory.getClient();
        Promise<Void> booked = workflow.makeBooking(123, 345, true, true);
        List<String> expected = new ArrayList<String>();
        expected.add("reserveCar-123");
        expected.add("reserveAirline-123");
        expected.add("sendConfirmation-345");
        AsyncAssert.assertEqualsWaitFor("invalid booking", expected, trace, booked);
    }
}
```

Alternatively, you can provide a mock implementation of the activities client and inject
that into your workflow implementation.

### Test Context Objects

If your workflow implementation depends on the framework context objects—for example,
the `DecisionContext`—you don't have to do anything special to test such
workflows. When a test is run through `WorkflowTest`, it automatically injects
test context objects. When your workflow implementation accesses the context
objects—for example, using `DecisionContextProviderImpl`—it will
get the test implementation. You can manipulate these test context objects in your test
code (`@Test` method) to create interesting test cases. For example, if your
workflow creates a timer, you can make the timer fire by calling the
`clockAdvanceSeconds` method on the `WorkflowTest` class to move
the clock forward in time. You can also accelerate the clock to make timers fire earlier
than they normally would using the `ClockAccelerationCoefficient` property on
`WorkflowTest`. For example, if your workflow creates a timer for one hour,
you can set the `ClockAccelerationCoefficient` to 60 to make the timer fire in
one minute. By default, `ClockAccelerationCoefficient` is set to 1.

For more details about the com.amazonaws.services.simpleworkflow.flow.test and
com.amazonaws.services.simpleworkflow.flow.junit packages, see the AWS SDK for Java
documentation.

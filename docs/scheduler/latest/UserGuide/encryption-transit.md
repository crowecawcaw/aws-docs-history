# Encryption in transit in EventBridge Scheduler

EventBridge Scheduler encrypts your data in transit as it travels the network. Transport Layer Security (TLS) encrypts your data when you call any EventBridge Scheduler API operations, as well as when EventBridge Scheduler calls any target APIs when it invokes your schedule.
By default, EventBridge Scheduler uses TLS 1.2 when encrypting your data in transit. You do not need to configure encryption in transit, and you cannot choose a different TLS version when using EventBridge Scheduler.

**Using the EventBridge Scheduler API** – When you perform an API operation, such as `CreateSchedule`, EventBridge Scheduler encrypts the entire HTTP request, including the request body and headers.
EventBridge Scheduler also encrypts the entire response object that you receive from our APIs.

**Using target APIs** – When EventBridge Scheduler invokes your schedule, it calls the target API that you specified when you created the schedule. When delivering an event to a target, EventBridge Scheduler encrypts
the entire request, including the request body and all headers, as well as the response it receives from the target.

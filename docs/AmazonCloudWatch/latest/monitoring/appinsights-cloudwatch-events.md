# Application Insights CloudWatch Events for detected problems

For each application that is added to CloudWatch Application Insights, a CloudWatch event is published for the
 following events on a best effort basis:


* **Problem creation.** Emitted when CloudWatch Application Insights
 detects a new problem.




	+ Detail Type:  **"Application Insights Problem
	 Detected"**
	+ Detail:
	
	
	
	
		- `problemId`: The detected problem
		 ID.
		- `region`: The AWS Region where the
		 problem was created.
		- `resourceGroupName`: The Resource Group for
		 the registered application for which the problem was
		 detected.
		- `status`: The status of the problem. Possible status and definitions are as follows:
		
		
		
		
			* `In progress`: A new problem has
			 been identified. The problem is still receiving
			 observations.
			* `Recovering`: The problem is
			 stabilizing. You can manually resolve the problem
			 when it is in this state.
			* `Resolved`: The problem is
			 resolved. There are no new observations about this
			 problem.
			* `Recurring`: The problem was
			 resolved within the past 24 hours. It has reopened
			 as a result of additional observations.
		- `severity`: The severity of the
		 problem.
		- `problemUrl`: The console URL for the
		 problem.

* **Problem update.** Emitted when the
 problem is updated with a new observation or when an existing
 observation is updated and the problem is subsequently updated; updates
 include a resolution or closure of the problem.




	+ Detail Type:  **"Application Insights Problem
	 Updated"**
	+ Detail:
	
	
	
	
		- `problemId`: The created problem ID.
		- `region`: The AWS Region where the
		 problem was created.
		- `resourceGroupName`: The Resource Group for
		 the registered application for which the problem was
		 detected.
		- `status`: The status of the problem.
		- `severity`: The severity of the
		 problem.
		- `problemUrl`: The console URL for the
		 problem.

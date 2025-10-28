# Integrate a published dashboard into the

agent workspace

You can create a customized dashboard, and then surface it in the agent workspace. You
may want to do this if you don't want agents to have access to all the widgets or
metrics on the default **Agent workspace performance
dashboard**.

###### How often do embedded dashboards and widgets refresh?

- Dashboards and widgets embedded in the agent workspace refresh every 2
  minutes.
- Embedded timeseries widgets refresh every 15 minutes.
- There are some use cases where the embedded dashboard refreshes sooner than 2
  minutes. For example, when an agent manually refreshes the dashboard, or they
  receive a new contact.
  Following is a high-level overview of how you integrate a published dashboard in the
  agent workspace.

1. Publish your Amazon Connect dashboard. For instructions, see [Publish reports](publish-reports.md "publish-reports.md").
2. Integrate your published Amazon Connect dashboard into the agent workspace. For
   instructions, see [Integrate third-party applications (3p
   apps)](3p-apps.md "3p-apps.md").

###### Note

When you perform this step, ensure the access URL includes
`&_appLayoutMode=embedded` at the end. This ensures the
website navigation and header are hidden. 3. Assign permissions to the agent's security profile so they can access and view
the saved report and the dashboard.

    * Assign the following Analytics and Optimization permissions:




    	+ **Saved reports - View**: Grants permission
    	 to view the published dashboard.
    	+ **View my own data in dashboards - View**:
    	 Grants access to the Dashboards to view individual agent
    	 performance metrics and the metrics of queues in the agent's
    	 routing profile.

They don't need permission to **Agent Applications - Performance
metrics - Access** because instead you're giving them permissions
to your published report. 4. If supervisors or managers also want to view published dashboard in the agent
workspace, assign them the following Analytics and Optimization
permissions:

    * **Saved reports - View**: Grants permission to view
     the published dashboard.
    * Assign one of the following permissions:




    	+ **Dashboards - Access**: Grants access to only
    	 the **Dashboards** tab.
    	+ OR **Access metrics - Access**: Grants
    	 permission to all the tabs on the
    	 **Dashboards** page, such as Real-time
    	 metrics reports and Historical metrics reports.

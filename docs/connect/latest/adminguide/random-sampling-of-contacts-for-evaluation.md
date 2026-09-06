

# Random sampling of contacts for evaluation in Connect Customer
<a name="random-sampling-of-contacts-for-evaluation"></a>

 Connect Customer provides managers with a random sample of their agents' contacts for evaluation, removing manager bias and streamlining the evaluation process. On Contact Search, managers can specify the number of contacts that they need to evaluate for each agent, as per union agreements, regulation or internal guidelines. They then receive the required number of contacts, randomly selected from the specified timeframe, for example, 3 contacts per agent from the last week. In addition, managers can apply additional filters within Contact Search to make sure that the provided contacts are suitable for evaluation. For example, contacts must be longer than 180 seconds, have an associated audio or screen recording, transcripts, and have not yet been evaluated. After the sample is generated, you can select an evaluation form and create draft evaluations in bulk for each of the contacts within the sample. Evaluations created in this way will denote that the contact was selected through random sampling, and provide auditability to make sure that the filter criteria did not introduce any bias in selection. 

**Random sampling of contacts for evaluation**

1.  Login to Amazon Connect with a user, who has the following set of permissions on their security profile: 

   1.  Contact Search - View 

   1.  Sample contacts 

   1.  Evaluation forms – perform evaluations 

1. Select the timeframe of contacts for evaluation, such as trailing week. You can sample contacts from a maximum period of 5 weeks.  
![Select timeframe.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-time-range.png)

1. Select the agent or agent hierarchy that you need to evaluate.  
![Filter search - Agent.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-agent-filter.png)  
![Add filter - Agent.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-agent-filter-select.png)

1. Apply any additional filters to select only those contacts that are suitable for evaluation.
   + **Conversational analytics**: Ensures that the contact is analyzed by conversational analytics and has a transcript
   + **Recording**: Filter contacts with audio recording (voice) or screen recording (video)
   + **Interaction Duration**: You can choose contacts with a minimum and maximum agent-customer interaction
   + **Evaluation Status**: Only select contacts that have not yet been evaluated  
![Add additional filters.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-search-filters.png)

1. Specify the sampling criteria, such as 5 contacts per agent and choose **apply** to generate a sample.  
![Sampling criteria.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-criteria.png)

1. You can save the set of filters and sampling criteria within saved search.  
![Save filters and sampling criteria.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-save-search.png)![Save filters and sampling criteria.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-save-search-name.png)![Save filters and sampling criteria.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-save-search-banner.png)

1. After the sample is generated, you can create draft evaluations in bulk across all the contacts.
   + Select **Create Draft Evaluations**
   + Select the **Evaluation Form**  
![Create draft evaluations.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-create-draft-eval-empty.png)  
![Select evaluation form.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-create-draft-eval-form-select.png)

   This associates the draft evaluations with the sample name.
**Note**  
This step is required if you need to retrieve the contact sample in the future.  

![Creating draft evaluations.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-in-progress-banner.png)


![Draft evaluations successfully created.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-success-banner.png)


## Retrieving and viewing sampled contacts for evaluation
<a name="retrieve-and-view-sampled-contacts-for-evaluation"></a>

 To retrieve the contact sample in the future, navigate to Contact search and apply the filter Evaluation – contact samples. Contact samples are specific to the user that generated the sample. 

![Create draft evaluations.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-contact-samples-filter.png)


## Auditing sampling criteria
<a name="auditing-sampling-criteria"></a>

 If you open an evaluation, it will indicate if contact sampling was used to create the evaluation. You can choose **Yes** to audit the filter criteria used to generate the contact sample, making sure that filters did not introduce any bias (for example, negative customer sentiment) during the contact selection process. 

![Create draft evaluations - contact details.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-evals-list.png)


![Create draft evaluations - evaluation overview.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-sampled-eval.png)


![Create draft evaluations - contact sample details.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-randomsampling-sampled-eval-details.png)

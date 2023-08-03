## Deployment
Deployment is the process of using your new insights to make improvements within your organization. This can mean a formal integration such as the implementation of a model producing churn scores that are then read into a data warehouse. Alternatively, deployment can mean that you use the insights gained from data mining to elicit change in your organization. For example, perhaps you discovered alarming patterns in your data indicating a shift in behavior for customers over the age of 30. These results may not be formally integrated into your information systems, but they will undoubtedly be useful for planning and making marketing decisions.

In general, the deployment phase of CRISP-DM includes two types of activities:
1) Planning and monitoring the deployment of results
2) Completing wrap-up tasks such as producing a final report and conducting a project review
Depending on your organization's requirements, you may need to complete one or both of these steps.

### - Planning for Deployment ###

> Although you may be anxious to share the fruits of your data mining efforts, take time to plan for a smooth and comprehensive deployment of results.
 - The first step is to summarize your results--both models and findings. This helps you determine which models can be integrated within your database systems and which findings should be presented to your colleagues.
 - For each deployable model, create a step-by-step plan for deployment and integration with your systems. Note any technical details such as database requirements for model output. For example, perhaps your system requires that modeling output be deployed in a tab-delimited format.
 - For each conclusive finding, create a plan to disseminate this information to strategy makers.
 - Are there alternative deployment plans for both types of results that are worth mentioning?
 - Consider how the deployment will be monitored. For example, how will a model deployed using IBM® SPSS® Modeler Solution Publisher be updated? How will you decide when the model is no longer applicable?
 - Identify any deployment problems and plan for contingencies. For example, decision makers may want more information on modeling results and may require that you provide further technical details.


### - Planning Monitoring and Maintenance ###
> In a full-fledged deployment and integration of modeling results, your data mining work may be ongoing. For example, if a model is deployed to predict sequences of e-basket purchases, this model will likely need to be evaluated periodically to ensure its effectiveness and to make continuous improvements. Similarly, a model deployed to increase customer retention among high-value customers will likely need to be tweaked once a particular level of retention is reached. The model might then be modified and re-used to retain customers at a lower but still profitable level on the value pyramid. Take notes on the following issues and be sure to include them in the final report:

 - For each model or finding, which factors or influences (such as market value or seasonal variation) need to be tracked?
 - How can the validity and accuracy of each model be measured and monitored?
 - How will you determine when a model has "expired"? Give specifics on accuracy thresholds or expected changes in data, etc.
 - What will occur when a model expires? Can you simply rebuild the model with newer data or make slight adjustments? Or will changes be pervasive enough as to require a new data mining project?
 - Can this model be used for similar business issues once it has expired? This is where good documentation becomes critical for assessing the business purpose for each data mining project.

### - Producing a Final Report ###
> Writing a final report not only ties up loose ends in earlier documentation, it can also be used to communicate your results. While this may seem straightforward, it's important to present your results to the various people with a stake in the results. This can include both technical administrators who will be responsible for implementation of the modeling results as well as marketing and management sponsors who will make decisions based on your results.

> First, consider the audience of your report. Are they technical developers or market-focused managers? You may need to create separate reports for each audience if their needs are disparate. In either case, your report should include most of the following points:

 - A thorough description of the original business problem
 - The process used to conduct data mining
 - Costs of the project
 - Notes on any deviations from the original project plan
 - A summary of data mining results, both models and findings
 - An overview of the proposed plan for deployment
 - Recommendations for further data mining work, including interesting leads discovered during exploration and modeling
 - Preparing a Final Presentatio


### - Conducting a Final Project Review ###
> This is the final step of the CRISP-DM methodology, and it offers you a chance to formulate your final impressions and collate the lessons learned during the data mining process. You should conduct a brief interview with those significantly involved in the data mining process. Questions to consider during these interviews include the following:

 - What are your overall impressions of the project?
 - What did you learn during the process--both about data mining in general and the data available?
 - Which parts of the project went well? Where did difficulties arise? Was there information that might have helped ease the confusion?

> After the data mining results have been deployed, you might also interview those affected by the results such as customers or business partners. Your goal here should be to determine whether the project was worthwhile and offered the benefits it set out to create.

> The results of these interviews can be summarized along with your own impressions of the project in a final report that should focus on the lessons learned from the experience of mining your stores of data.

## Reference
 - IBM Docs. (2021, August 17). Ibm.com. https://www.ibm.com/docs/en/spss-modeler/SaaS?topic=guide-deployment‌


[Volver al inicio](../README.md)
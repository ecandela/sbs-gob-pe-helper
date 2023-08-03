## Modeling
Modeling is usually conducted in multiple iterations. Typically, data miners run several models using the default parameters and then fine-tune the parameters or revert to the data preparation phase for manipulations required by their model of choice. 

### - Selecting Modeling Techniques ###

> Although you may already have some idea about which types of modeling are most appropriate for your organization's needs, now is the time to make some firm decisions about which ones to use. Determining the most appropriate model will typically be based on the following considerations:
1) The data types available for mining. For example, are the fields of interest categorical (symbolic)?
2) Your data mining goals. Do you simply want to gain insight into transactional data stores and unearth interesting purchase patterns?
3) do you need to produce a score indicating, for example, propensity to default on a student loan?
4) Specific modeling requirements. Does the model require a particular data size or type? 
5) Do you need a model with easily presentable results?


### - Generating a Test Design ###
> As a final step before actually building the model, you should take a moment to consider again how the model's results will be tested. There are two parts to generating a comprehensive test design:
1) Describing the criteria for "goodness" of a model
2) Defining the data on which these criteria will be tested
> A model's goodness can be measured in several ways. For supervised models, such as C5.0 and C&R Tree, measurements of goodness typically estimate the error rate of a particular model. For unsupervised models, such as Kohonen cluster nets, measurements may include criteria such as ease of interpretation, deployment, or required processing time.
> Remember, model building is an iterative process. This means that you will typically test the results of several models before deciding on the ones to use and deploy.

### - Determining Data Mining Goals ###
> Now that the business goal is clear, it's time to translate it into a data mining reality. For example, the business objective to "reduce churn" can be translated into a data mining goal that includes:
1) Identifying high-value customers based on recent purchase data
2) Building a model using available customer data to predict the likelihood of churn for each customer
3) Assigning each customer a rank based on both churn propensity and customer value
> These data mining goals, if met, can then be used by the business to reduce churn among the most valuable customers. As you can see, business and technology must work hand-in-hand for effective data mining. 

### - Building the Models ###
> At this point, you should be well prepared to build the models you've spent so long considering. Give yourself time and room to experiment with a number of different models before making final conclusions. Most data miners typically build several models and compare the results before deploying or integrating them.
> In order to track your progress with a variety of models, be sure to keep notes on the settings and data used for each model. This will help you to discuss the results with others and retrace your steps if necessary. At the end of the model-building process, you'll have three pieces of information to use in data mining decisions:
> Parameter settings include the notes you take on parameters that produce the best results.
The actual models produced.
Descriptions of model results, including performance and data issues that occurred during the execution of the model and exploration of its results.

### - Assessing the Model ###
> Now that you have a set of initial models, take a closer look at them to determine which are accurate or effective enough to be final. Final can mean several things, such as "ready to deploy" or "illustrating interesting patterns.

## Reference
 - IBM Docs. (2021, August 17). Ibm.com. https://www.ibm.com/docs/en/spss-modeler/SaaS?topic=guide-modeling

[Volver al inicio](../README.md)
## Data Preparation
Data preparation is one of the most important and often time-consuming aspects of data mining. In fact, it is estimated that data preparation usually takes 50-70% of a project's time and effort. Devoting adequate energy to the earlier business understanding and data understanding phases can minimize this overhead, but you still need to expend a good amount of effort preparing and packaging the data for mining. Data preparation typically involves the following tasks:
1) Merging data sets and/or records
2) Selecting a sample subset of data
3) Aggregating records
4) Deriving new attributes
5) Sorting the data for modeling
6) Removing or replacing blank or missing values
7) Splitting into training and test data sets

### - Selecting Data ###
> Based upon the initial data collection conducted in the previous CRISP-DM phase, you are ready to begin selecting the data relevant to your data mining goals. Generally, there are two ways to select data:
1) Selecting items (rows) involves making decisions such as which accounts, products, or customers to include.
2) Selecting attributes or characteristics (columns) involves making decisions about the use of characteristics such as transaction amount or household income.

### - Cleaning Data ###
> Cleaning your data involves taking a closer look at the problems in the data that you've chosen to include for analysis. There are several ways to clean data using the Record and Field Operation.
1) Missing data: 	Exclude rows or characteristics. Or, fill blanks with an estimated value.
2) Data errors: Use logic to manually discover errors and replace. Or, exclude characteristics.
3) Coding inconsistencies: Decide upon a single coding scheme, then convert and replace values.
4) Missing or bad metadata: Manually examine suspect fields and track down correct meaning.

### - Constructing New Data ###
> It is frequently the case that you'll need to construct new data. For example, it may be useful to create a new column flagging the purchase of an extended warranty for each transaction. There are two ways to construct new data:
1) Deriving attributes (columns or characteristics)
2) Generating records (rows)

### - Integrating Data ###
> It is not uncommon to have multiple data sources for the same set of business questions. For example, you may have access to mortgage loan data as well as purchased demographic data for the same set of clients. If these data sets contain the same unique identifier (such as social security number), you can merge them  using this key field. There are two basic methods of integrating data:
1) Merging data involves merging two data sets with similar records but different attributes. The data is merged using the same key identifier for each record (such as customer ID). The resulting data increases in columns or characteristics.
2) Appending data involves integrating two or more data sets with similar attributes but different records. The data is integrated based upon a similar fields (such as product name or contract length).

### - Formatting Data ###
> As a final step before model building, it is helpful to check whether certain techniques require a particular format or order to the data. For example, it is not uncommon that a sequence algorithm requires the data to be presorted before running the model. Even if the model can perform the sorting for you, it may save processing time to use a Sort node prior to modeling. Consider the following questions when formatting data:
1) Which models do you plan to use?
2) Do these models require a particular data format or order?
3) If changes are recommended, the processing tools in IBM® SPSS® Modeler can help you apply the necessary data manipulation.

## Reference
 - IBM Docs. (2021, August 17). Ibm.com. https://www.ibm.com/docs/en/spss-modeler/SaaS?topic=guide-data-preparation


[Volver al inicio](../README.md)
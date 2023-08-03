## Data Understanding

The data understanding phase of CRISP-DM involves taking a closer look at the data available for mining. This step is critical in avoiding unexpected problems during the next phase--data preparation--which is typically the longest part of a project. Data understanding involves accessing the data and exploring it using tables and graphics that can be organized with a statistical software. This enables you to determine the quality of the data and describe the results of these steps in the project documentation.

### - Collecting Initial Data ###
> At this point in CRISP-DM, you're ready to access data and bring it into statistical software. Data come from a variety of sources, such as Existing data (such as transactional data, survey data, Web logs, etc), Purchased data ( supplemental data, such as demographics) or Additional data (you may need to conduct surveys or begin additional tracking to supplement the existing data stores). You may consider the following questions. Be sure to take notes on your findings:
1) Which attributes (columns) from the database seem most promising?
2) Which attributes seem irrelevant and can be excluded?
3) Is there enough data to draw generalizable conclusions or make accurate predictions?
4) Are there too many attributes for your modeling method of choice?
5) Are you merging various data sources? If so, are there areas that might pose a problem when merging?
6) Have you considered how missing values are handled in each of your data sources?

### - Describing Data ###
> There are many ways to describe data, but most descriptions focus on the quantity and quality of the data--how much data is available and the condition of the data. Listed below are some key characteristics to address when describing data:
1) Amount of data. For most modeling techniques, there are trade-offs associated with data size. Large data sets can produce more accurate models, but they can also lengthen the processing time. Consider whether using a subset of data is a possibility. When taking notes for the final report, be sure to include size statistics for all data sets, and remember to consider both the number of records as well as fields (attributes) when describing data.
2) Value types. Data can take a variety of formats, such as numeric, categorical (string), or Boolean (true/false). Paying attention to value type can head off problems during later modeling.
3) Coding schemes. Frequently, values in the database are representations of characteristics such as gender or product type. For example, one data set may use M and F to represent male and female, while another may use the numeric values 1 and 2. Note any conflicting schemes in the data report.

### - Verifying Data Quality ###
> Data are rarely perfect. In fact, most data contain coding errors, missing values, or other types of inconsistencies that make analysis tricky at times. One way to avoid potential pitfalls is to conduct a thorough quality analysis of available data before modeling. You can look for the following types of problems:
1) Missing data include values that are blank or coded as a non-response.
2) Data errors are usually typographical errors made in entering the data.
3) Measurement errors include data that are entered correctly but are based on an incorrect measurement scheme.
4) Coding inconsistencies typically involve nonstandard units of measurement or value inconsistencies, such as the use of both M and male for gender.
5) Bad metadata include mismatches between the apparent meaning of a field and the meaning stated in a field name or definition.


## Reference
 - IBM Docs. (2021, August 17). Ibm.com. https://www.ibm.com/docs/en/spss-modeler/SaaS?topic=guide-data-understanding -


[Volver al inicio](../README.md) &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;[Ir a siguiente](README03.md)
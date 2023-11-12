# data_engineer_portifolio
Welcome to my data engineer portfolio.
This is a project underdevelopment to demonstrate my skills as a data engineer.
This portfolio contains a PostgreSQL instance where the final Data Warehouse is built and an Airflow instance that creates certain pipelines to bring data into this Warehouse.
To run the above project please follow the steps:
- Clone this repository to your machine.
- Check that you have Docker and Docker-compose. If not download it [here](https://docs.docker.com/get-docker/).
- Run the docket container.
  ```
  docker-compose up -d 
  ```
- Connect to the data warehouse by localhost on port 5433, the admin and password are 'portfolio', and the database is portifolio_dwh. 
    >If you do not have an IDE to make this connection easier I may recomment the download of [DBeaver free version here](https://dbeaver.com/download/).
- Online you can access the Airflow GUI to run the pipelines by accessing http://localhost:8080/. With user and password 'airflow'.
- Run any pipeline and see the result data available in the Data Warehouse.

Refer to: https://www.youtube.com/watch?v=nr9ujxeCOfA
Ideas for data sets!
https://www.youtube.com/shorts/CUbN0m4-ZdM
projects ideas!
#### Data Architecture
#### Data Model


<details>
  <summary>Pipelines Details</summary>

## Pipeline Options:
<details>
  <summary>World Population</summary>
  
### World Population
Begins with an export task with pulls an Excel file out of the UN website with a worldwide report of important metrics for world population, such as total population, the population born and deceased during the years, and so forth. The result of this Excel can be found on schema world_population in their respective tables.

Refer to: https://www.youtube.com/watch?v=nr9ujxeCOfA
#### Data Architecture
#### Data Model


</details>

</details>

<details>
  <summary>Data interview Questions</summary>
  
## Data interview Questions
This is a mixture of questions I have received while interviewing for data engineering positions and questions that I found on the internet and the answers to them.
Firstly I attempt to answer common HR questions and then I dive into technical interview questions.

<details>
  <summary>Tell me about yourself</summary>

#### Tell me about yourself
I'm Timna Aversa, a Brazilian now living in Germany. I started my path in data engineering around 3 years ago with the support of 2 amazing mentors who guided me on what a data engineer does and what I need to know in the field. Around a year and a half ago I got my first job in data engineering and have loved it ever since.
</details>

<details>
  <summary>What is a data engineer’s role within a team or company?</summary>

#### What is a data engineer’s role within a team or company?
Data engineers are responsible for providing data to the company and making it easy to access and understand so the company can take value out of this data. That is done by creating an architecture where data can be moved and transformed, also creating the pipeline that performs such tasks. Within a team, the work of a data engineer can be encapsulated in performing all the movement and transformation of the data in the case of a small data team, or it can be specialized on certain pipelines or the development of infrastructure in more specialized teams.
</details>
<details>
  <summary>When did you face a challenge in dealing with unstructured data and how did you solve it?</summary>

#### When did you face a challenge in dealing with unstructured data and how did you solve it?
As of now I have not yet dealt with unstructured data in my career, that is something I really look forward to doing in new opportunities. Nonetheless, I frequently faced challenges in which I didn't have the answer or solutions for it right away. I usually search if this problem has happened before, Jira tickets can be very insightful in certain problems. If this problem is a novelty I will research possible solutions, often reading documentation on how to solve this issue can go a long way, and reading how other people have solved the same issue can help in the small details for specific errors, as of late, I have been also implementing the use of Bard as part of my search to get quick answers to problems.
</details>
<details>
  <summary>Walk me through a project you worked on from start to finish.</summary>

#### Walk me through a project you worked on from start to finish.
As of late, I worked on a project migrating some pipelines from a Postgres DWH running on cronjobs into a Snowflake DWH running on airflow.
- Situation: The company I work with has a variety of Data Warehouses some are in a Postgres Instance, some are on Redshift and the newest is in Snowflake. This is complicated in many ways beginning with the variety of tools and processes necessary for each system, the knowledge and personnel required to maintain so many different systems, the necessity to copy data across platforms, and the added complexity of creating reports in multiple platforms. To solve this issue we wanted to create a single destination having Snowflake as the only Data Warehouse.
- Task: The task to be performed in this project was to create the pipeline to bring the dimension tables from the Application databases into Snowflake DWH.
- Action: Creation of a pipeline on Airflow that would fetch that information from Application databases and store it into an S3 bucket, from there we used sternal tables to make the data available in Snowflake. We then utilized DBT models to deduplicate and perform the casting of the data. The final model available would be the dimention table available in the Warehouse.
- Result: Availability of the dimention tables into the Snowflake for transformation and for reporting. Makes easier to verify the performance of the apps accross different Aplications databases. Better query responses.

</details>

<details>
  <summary>What tools did you use on the project?</summary>

#### What tools did you use on the project?
Airflow was used as a orquestration tool. This was used not only because is a great orquestration tool but also because we already have an instance running to perform other jobs for Snowflake with given permissions.
Lambda used to fetch the data. We wanted something that was reliable, that could run asynchronous for multiple tables and that had a high performance and inbeded logs, and since our company already have all our projects in AWS, a Lambda seemed like the best option.
S3 to store data, due to the company already utilizing the tool.
Snowflake as the Data Warehouse.
DBT modeling tool to data transformations, this is the only new tool (for the company) utilized in this project, we wanted a tool that would give us flexibility to be able to reutilize the same queries with small changes for running the deduplicationg and casting accross the applications. Another features of the tool that made us interested was the cascading models visualization and  the inbedded documentation.

</details>
<details>
  <summary>What are big data’s four Vs?</summary>

#### What are big data’s four Vs?
My Thoughts:
I don't fully have an opnion about big data since is something I haven't touched much, but is definetly something I want to learn more in the future.

[website's response](https://www.coursera.org/articles/data-engineer-interview-questions):
The four Vs are volume, velocity, variety, and veracity. Chances are, the interviewer will ask you not just what they are, but why they matter. You might explain that big data is about compiling, storing, and exploiting huge amounts of data to be useful for businesses. The four Vs must create a fifth V, which is value. 

- Volume: Refers to the size of the data sets (terabytes or petabytes) that need to be processed—for example, all of the credit card transactions that occur in a day in Latin America. 

- Velocity: Refers to the speed at which the data is generated. Instagram posts have high velocity. 

- Variety: Refers to the many sources and files types of structured and unstructured data. 

- Veracity: Refers to the quality of the data being analyzed. Data engineers need to understand different tools, algorithms, and analytics in order to cultivate meaningful information.

</details>
<details>
  <summary></summary>

#### 


</details>


<details>
  <summary>What is a data vault?</summary>

#### What is a data vault?
My thoughts:
A data vault is a modeling structure in which you compartmentalize groups of data in the silver layer by hubs and create links between their hubs, you can have a hub for customers and another for purchases with a link in between them.

[Website's response](https://www.databricks.com/glossary/data-vault):
A data vault is a data modeling design pattern used to build a data warehouse for enterprise-scale analytics. The data vault has three types of entities: hubs, links, and satellites.

Hubs represent core business concepts, links represent relationships between hubs, and satellites store information about hubs and the relationships between them.

The data vault is a data model that is well-suited to organizations that are adopting the lakehouse paradigm.
##### Data vault modeling: Hubs, links, and satellites
Hubs - Each hub represents a core business concept, such as they represent Customer Id/Product Number/Vehicle identification number (VIN). Users will use a business key to get information about a Hub. The business key may have a combination of business concept ID and sequence ID, load date, and other metadata information.
Links - Links represent the relationship between Hub entities.
Satellites - Satellites fill the gap in answering the missing descriptive information on core business concepts. Satellites store information that belongs to Hub and the relationships between them.
A few additional things to keep in mind:

A satellite cannot have a direct connection to another satellite.
A hub or link may have one or more satellites.

##### Modeling techniques by lakehouse layer
With these concepts in mind, let's explore how Data Vault fits into our Bronze, Silver and Gold data layers where data goes from a raw to a refined state that is ready for analytics. In this multi-hop architecture, raw data gets stored in a Bronze layer with minimum transformation and data structure as close to the source system. The Data Vault methodology can be applied to the Silver layer where data is transformed into Hubs, links and satellites.

In the Gold layer, multiple data marts/data warehouses can be built as per dimensional modeling/Kimball methodology. As discussed earlier, the Gold layer is for reporting and uses more de-normalized and read-optimized data models with fewer joins. Sometimes tables in the Gold Layer can be completely denormalized, typically if the Data Scientists want it that way to feed their algorithms for feature engineering.

If a Data Vault model is used in the Silver layer it simplifies and significantly reduces the changes needed to perform ETL in the Data Marts and Data Warehouses, as Hubs make key management (surrogate key / natural keys) easier. Satellites make loading dimensions easier because they have all the attributes, and links make loading fact tables quite straightforward because they have all the relationships.
</details>
<details>
  <summary>What is the difference between a Data Model and Data architecture?</summary>

#### What is the difference between a Data Model and Data architecture?

My thoughts: Data architecture is the structure of tools utilized by the parts of the data process (Solutions and Tools), while data model is the structure of the tables in relation to each other and the schema organization (Entities and Rules).

Website's response:
Data Modeling vs Data Architecture: Key Differences 
While data modeling and data architecture share some similarities, there are also some key differences. The following are five key differences between data modeling and data architecture.

- Data modeling focuses on the representation of the data while data architecture is concerned with what tools and platforms to use for storing and analyzing it.
- Data modeling is all about the accuracy of data while data architecture is about the infrastructure housing that data.
- Data modeling is concerned with the reliability of the data, while data architecture is concerned with keeping the data safe.
- A data model is an attempted representation of reality, while data architecture is a framework of systems and logistics.
- A data model represents a limited set of business concepts and how they relate to one another. Data architecture covers the data infrastructure of the entire organization.

</details>
<details>
  <summary>Can you explain Iteration and generation?</summary>

#### Can you explain Iteration and generation?

My thoughts:
Iteration and Generation are different ways of processing data, while iteration performs processing row by row, which is amazing for loading and cleaning data, generation performs processing by batches which is useful for aggregating data and creating reports.

Bard's response:
Iteration and generation are important concepts in data engineering that refer to different ways of processing data.

Iteration is the process of processing data one row or record at a time. It is a common approach for processing large datasets, as it allows data engineers to break down the task into smaller, more manageable pieces.

Generation is the process of processing data in batches. It is a more efficient approach than iteration for certain types of data processing tasks, such as data aggregation and machine learning.

Here are some examples of how iteration and generation are used in data engineering:

Iteration:
Loading data from a database into a data warehouse
Cleaning and transforming data
Performing data quality checks
Generation:
Aggregating data to generate reports and dashboards
Training machine learning models
Generating synthetic data for testing and development
Data engineers often use a combination of iteration and generation to process data. For example, they may use iteration to load data from a database into a data warehouse, and then use generation to aggregate the data to generate reports and dashboards.

The best approach to use for a particular data processing task depends on the specific requirements of the task and the characteristics of the data. For example, if the data is small and needs to be processed quickly, then iteration may be the best approach. If the data is large and needs to be processed efficiently, then generation may be the best approach.

Data engineers should also consider the scalability and performance of their data processing pipelines when choosing between iteration and generation. Iteration can be more scalable than generation, as it can be easily parallelized. However, generation can be more performant for certain types of data processing tasks.

Overall, iteration and generation are important concepts in data engineering that can be used to efficiently process data and generate insights. Data engineers should choose the best approach for each task based on the specific requirements of the task and the characteristics of the data.
</details>
<details>
  <summary>What is data normalization?</summary>

#### What is data normalization?
My thoughts:
Table normalization is a process in which you structure the organization of the tables to decrease the redundancy of information by breaking down information with mappings tables and separating unrelated data. This is an important part of improving the quality and efficiency of the data.

[Website's response](https://www.simplilearn.com/automated-recruiting-in-companies-article#:~:text=Data%20normalization%20is%20the%20process,across%20all%20records%20and%20fields.):
Data normalization is the process of reorganizing data within a database so that users can utilize it for further queries and analysis. Simply put, it is the process of developing clean data. This includes eliminating redundant and unstructured data and making the data appear similar across all records and fields.

Data organization in a database is done by normalization. This entails building tables and linking those tables together in accordance with principles intended to safeguard the data and increase the database's adaptability by removing duplication and inconsistent reliance.

Disk space is wasted by redundant data, and maintenance issues result. If data that already exists in multiple locations needs to be modified, it must be updated in the same manner everywhere. If the information is kept solely in the Customers table and not elsewhere in the database, changing a customer's address is significantly simpler to do.

Whereas it makes perfect sense for a user to search in the Customers database for a specific customer's address, it might not sound right to do so for the worker who phones on that customer's behalf. The wage of the employee must be transferred to the Employees table because it is connected to or dependent upon the employee. Data might become difficult to access as a result of inconsistent dependencies because the path to finding the data may be incomplete or damaged.

</details>
<details>
  <summary>What is the difference between a star schema and a snowflake schema?</summary>

#### What is the difference between a star schema and a snowflake schema?
My thoughts:
In a star schema, you have multiple dimensions (base) tables feeding a fact table, while in a snowflake schema, you have multiple dimension tables that are normalized one or more times to create a fact table.

Bard's Response:
A star schema and a snowflake schema are both data warehouse designs that are used to store and analyze large amounts of data. However, there are some key differences between the two designs.

Star schema:

A star schema is a data warehouse design that is characterized by a central fact table and a number of dimension tables.
The fact table contains the core data of the data warehouse, such as sales transactions or customer orders.
The dimension tables contain descriptive data about the fact table data, such as product information, customer information, or time information.
The star schema is a simple and easy-to-understand design, which makes it a good choice for many data warehouse applications.
Snowflake schema:

A snowflake schema is a data warehouse design that is similar to a star schema, but with one key difference: the dimension tables are normalized into one or more additional levels of dimension tables. This process of normalizing the dimension tables is what gives the snowflake schema its name.
The snowflake schema is a more complex design than the star schema, but it can offer some performance benefits for certain types of queries.
Here is a table that summarizes the key differences between the star schema and the snowflake schema:

|Characteristic	|Star schema	|Snowflake schema|
|---|---|---|
|Dimension tables	|Normalized to a single level	|Normalized to one or more levels|
|Queries	|Performance is good for most queries	|Performance can be better than star schema for certain types of queries|
|Complexity	|Simple and easy to understand	|More complex than star schema|

Which design to choose:

The best data warehouse design for your needs depends on a number of factors, such as the size and complexity of your data set, the types of queries that you need to run, and your performance requirements.

If you are new to data warehouse design, or if you have a relatively simple data set, then a star schema is a good choice. If you have a large and complex data set, or if you need to run complex queries, then a snowflake schema may be a better choice.

It is also important to note that you can combine star and snowflake schema designs in a single data warehouse. For example, you could use a star schema for your core data and a snowflake schema for your more complex data.
</details>
<details>
  <summary>What are the pros and cons of saving a file in Parquet or Avro in place of CSV?</summary>

#### What are the pros and cons of saving a file in Parquet or Avro in place of CSV?
My thoughts:
CSV is a great file system for data that need to be used across teams, it is easier to understand and more widely supported but complicated to use for large data sets and slow to read. 
Parquet allows easy data access and storage, with efficient compression, it is a great file system to store data that is gonna be read by tools and frameworks but can be hard to troubleshoot and is slower to write.
Avro is an amazing file for big data coming with schema evolution and using efficient compression algorithms, but is also harder to troubleshoot and it is not as widely supported then the others.

Bard's response:
##### Parquet
Pros:

Efficient compression: Parquet uses columnar storage and efficient compression algorithms to reduce file size.
Fast data access: Parquet allows for fast data access, especially when reading subsets of columns.
Schema support: Parquet supports schema evolution, which makes it easy to add new columns or change the data types of existing columns without having to recreate the entire file.
Widely supported: Parquet is widely supported by big data processing tools and frameworks.
Cons:

Slower write performance: Writing data to Parquet can be slower than writing to CSV.
More complex to use: Parquet is a more complex file format than CSV, which can make it more difficult to use and troubleshoot.
##### Avro
Pros:

Efficient compression: Avro uses efficient compression algorithms to reduce file size.
Schema support: Avro supports schema evolution, which makes it easy to add new fields or change the data types of existing fields without having to recreate the entire file.
Widely supported: Avro is widely supported by big data processing tools and frameworks.
Cons:

Slower write performance: Writing data to Avro can be slower than writing to CSV.
More complex to use: Avro is a more complex file format than CSV, which can make it more difficult to use and troubleshoot.
Less widely supported than Parquet: Avro is less widely supported than Parquet, especially among big data processing tools and frameworks.
##### CSV
Pros:

Easy to use: CSV is a simple and easy-to-use file format.
Widely supported: CSV is widely supported by all types of software, including big data processing tools and frameworks.
Fast write performance: Writing data to CSV is fast.
Cons:

Inefficient compression: CSV does not compress data very efficiently, which can result in large file sizes.
Slow data access: CSV is not optimized for fast data access, especially when reading subsets of columns.
No schema support: CSV does not support schema evolution, which can make it difficult to add new columns or change the data types of existing columns.
Overall, Parquet and Avro are better choices than CSV for storing large datasets that need to be processed quickly. Parquet and Avro offer efficient compression and fast data access, which can make big data processing tasks more efficient. However, Parquet and Avro are more complex to use than CSV.

CSV is a good choice for storing small datasets or for datasets that do not need to be processed quickly. CSV is also a good choice for datasets that need to be shared with other users who may not have access to Parquet or Avro readers.

</details>

</details>
# data_engineer_portifolio
Welcome to my data engineer portifolio.
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


<details>
  <summary>Pipelines Details</summary>

## Pipeline Options:
<details>
  <summary>World Population</summary>
  
### World Population
Begins with an export task with pulls a CSV file out of the UN website with a worldwide report of important metrics for world population, such as total population, the population born and deceased during the years, and so forth. The result of this CSV can be fond on schema world_population in their respective tables.
  
</details>

</details>
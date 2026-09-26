![image alt](https://github.com/basheercodes/AUTOMATION-WITH-AIRFLOW/blob/cf4e1afe429b54843e72129a333b148e63cdad8b/AUTOMATION%20DATA%20PIPELINE%20WITH%20AIRFLOW%20.png)
Airflow × Snowflake × Docker Data Pipeline
📖 Project Overview
This project is a containerized, production‑ready data pipeline that integrates Apache Airflow with Snowflake Cloud Data Warehouse, orchestrated entirely through Docker. It automates incremental data loading into Snowflake, ensuring scalability, reproducibility, and maintainability.

The pipeline was designed, debugged, and deployed in a Linux WSL environment with VS Code for development and GitHub for version control. It represents a complete end‑to‑end workflow — from DAG authoring to containerized execution and cloud integration.

🧩 Architecture
1. Local Development
WSL (Linux on Windows): Provides a stable environment for Airflow and Docker.

VS Code: Authoring and debugging DAGs (snowflake_code.py).

GitHub Repository: Version control for DAGs, Docker Compose files, and documentation.

2. Containerized Deployment
Docker Compose spins up multiple containers:

Airflow Scheduler: Orchestrates DAG execution.

Airflow API Server: Provides REST endpoints for DAG control.

Airflow Web UI: Monitoring and visualization of DAG runs.

Metadata Database (Postgres): Stores DAG states and execution metadata.

Containers ensure portability, isolation, and easy scaling.

3. Airflow DAG
DAG: snowflake_increment_loading_dag scheduled @daily.

Tasks:

start → EmptyOperator

increment_load → SnowflakeOperator (executes SQL/stored procedure)

end → EmptyOperator

DAG execution is logged and monitored via Airflow Web UI.

4. Snowflake Integration
Connection: snowflake_conn configured in Airflow.

Database: AIRFLOW_DB

Schema: SILVER

Stored Procedure: increment_load() handles incremental data ingestion.

Results validated directly in Snowflake tables.

🔄 Workflow Steps
Develop DAG Code in VS Code under WSL.

Build & Run Containers using docker compose up.

Access Airflow Web UI at http://localhost:8080.

Trigger DAG Execution → incremental load runs daily.

Snowflake Operator executes stored procedure.

Validate Results in Snowflake database (AIRFLOW_DB.SILVER).

🌟 Key Achievements
Built a production‑style pipeline with Dockerized Airflow.

Automated incremental data loading into Snowflake.

Achieved seamless integration between local dev, containers, and cloud.

Debugged complex issues across Airflow, Docker, and Snowflake.

Delivered a professional workflow diagram for documentation.

🛠 Setup Instructions
Clone the repo and run:
# Build and start containers
docker compose up -d

# Access Airflow Web UI
http://localhost:8080

# Run scheduler and API server (inside containers)
airflow scheduler
airflow api-server
Deactivate and shut down:
docker compose down
wsl --shutdown

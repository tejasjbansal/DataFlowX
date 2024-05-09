# Project Name: DataFlowX

## Description
DataFlowX is an innovative end-to-end data engineering pipeline designed to handle real-time data acquisition, processing, and sentiment analysis. It uses a combination of TCP/IP Socket streaming, Apache Spark processing, OpenAI's ChatGPT for sentiment analysis, and cloud-based Kafka for data dissemination. The project utilizes the Yelp.com dataset to demonstrate a practical application of processing and analyzing customer reviews in real-time.

## Architecture
![Project Architecture](https://github.com/tejasjbansal/DataFlowX/assets/56173595/b6ca22fb-422c-4c6d-8c5d-9945ea57e7e6)

## Project Components

- **Data Source:** The Yelp.com dataset is utilized to simulate real-world data ingestion and processing scenarios.
- **TCP/IP Socket:** This component is responsible for streaming data over the network in manageable chunks, enabling real-time data processing.
- **Apache Spark:** Used for efficient data processing across its distributed master and worker nodes, Spark handles large-scale data with ease.
- **Confluent Kafka:** This serves as our messaging backbone, hosted in the cloud, facilitating robust data exchange and stream processing.
- **Control Center and Schema Registry:** These tools from Confluent help in monitoring Kafka streams and managing schemas effectively, ensuring data integrity and smooth operation.

## Technologies Used
- **Python:** The primary programming language for development.
- **TCP/IP:** Networking protocol used for data transmission.
- **Confluent Kafka:** Manages messaging services in the cloud.
- **Apache Spark:** Processes large datasets using distributed computing.
- **Docker:** Ensures consistent environments and ease of deployment across different stages of the pipeline.

## Getting Started

### Prerequisites
- Docker
- Python 3.8 or higher
- Access to a Confluent Cloud account
- Apache Spark setup

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/tejasjbansal/DataFlowX/
   cd DataFlowX
   ```

2. **Set Up Environment**
   Use Docker to set up your local development environment. Ensure Docker Desktop is installed and running.
   ```bash
   docker-compose up -d --build
   ```

3. **Run the TCP/IP Socket Server Job**
   Navigate to the TCP/IP server directory and start the server script:
   ```bash
   docker exec spark-master python streaming-socket.py
   ```

5. **Start Apache Spark Processing**
   Execute the Spark job to begin processing the streamed data:
   ```bash
   docker exec spark-master spark-submit\
   --master spark://spark-master:7077 \
   --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 spark_job.py \
    jobs/spark-streaming.py
   ```

### Usage
Once the setup is complete, the system will start ingesting data from the Yelp dataset via the TCP/IP socket, process it through Apache Spark, perform sentiment analysis using OpenAI's ChatGPT, and publish results to a Kafka topic in real-time. You can monitor the pipeline through Confluent's Control Center.

## Monitoring
Access the Confluent Control Center via:
```
http://<your-cloud-url>:9021/
```
Monitor the Kafka streams and ensure data integrity across your pipeline.

## Contributing
We welcome contributions from the community! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

# Microservices Project - Text summarizer

## Introduction
This project demonstrates the implementation of a microservices-based architecture. It includes services that communicate through defined interfaces, ensuring modularity and scalability. The application is containerized using Docker for ease of deployment.

## Features
- **Microservices Architecture**: Modular and independently deployable services.
- **Docker Support**: Simplified containerization and orchestration.
- **Python-based Implementation**: Core functionality implemented in Python.

## Prerequisites
- Python 3.8 or later
- Docker and Docker Compose installed
- Basic knowledge of microservices and Docker

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd EN2AR-master
   ```

2. **Install Dependencies**
   Install Python dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run with Docker Compose**
   Build and start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. **Run Locally**
   Execute the main Python script:
   ```bash
   python main.py
   ```

## Directory Structure
```
EN2AR-master/
├── Dockerfile             # Docker configuration for containerizing the app
├── docker-compose.yml     # Docker Compose configuration
├── main.py                # Main application entry point
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

## Usage
- Access the application through the service endpoint (e.g., `http://localhost:<port>`).
- Modify the services or extend functionality by editing the respective modules in the project.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature description'`
4. Push to your branch: `git push origin feature-name`
5. Submit a pull request.


## Contact
For questions or suggestions, feel free to reach out.

## About
This project implements a text summarization microservice, which processes long text and returns concise summaries. The project aims to simplify text processing tasks and can be extended to handle additional NLP tasks such as sentiment analysis or keyword extraction.
## Docker and Python Components
Dockerfile: Contains the configuration for containerizing the application to ensure that it works seamlessly across different environments.
Docker Compose: Manages the orchestration of the services and ensures they can communicate with each other.


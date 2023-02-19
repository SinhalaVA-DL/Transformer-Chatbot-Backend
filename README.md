# Transformer-based Conversational Chatbot Backend using FastAPI

This is a repository for a conversational chatbot backend that is built using the transformer architecture and FastAPI. The chatbot is designed to answer general questions and have conversations with the users.

## Requirements

To run the code in this repository, you need to have the following software installed on your system:

- Python 3.x
- TensorFlow 2.x
- FastAPI

You also need to have a GPU if you want to train the model yourself, as the training process can be quite slow on a CPU.

## Deployment

To deploy the chatbot backend, run the following command:


```
uvicorn app.main:app --reload
```

This will launch the FastAPI server and make the chatbot available through a REST API.

## Running the Docker Image

To run the Docker image, you will need to have Docker installed on your machine. If you don't have Docker installed, you can download it from the official website.

Once you have Docker installed, you can run the Docker image using the following command:

```
docker run -p 8080:80 <image-name>

```
If you want to customize the container configuration, you can pass additional options to the docker run command. Here are some common options:

- -d: runs the container in the background (detached mode)
- -e <ENV_VAR>=<VALUE>: sets environment variables inside the container
- -v <HOST_PATH>:<CONTAINER_PATH>: mounts a host directory inside the container
-  --name <CONTAINER_NAME>: gives a custom name to the container

## Contributing

If you want to contribute to this project, please feel free to open a pull request. We welcome all contributions, including bug fixes, improvements to the code, and new features.

## License

This repository is released under the MIT License. See the LICENSE file for more information.

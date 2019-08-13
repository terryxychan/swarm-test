# Template Python Server

This is a microservice template written in Python. It provides the following functionality to manage your bank account:
* [GET] Retrieve your bank balance
* [PUT] Deposit or withdraw money from your account

Microservice Name: template-python-server (should be same as GIT repository name)

Authors: Muthu Chandrasekaran, Terry Chan

This template follows the [coding and naming conventions](https://slb-swt.visualstudio.com/bit-inspection/_git/documentation?path=%2FServiceRequirements.md&version=GBmaster) described here.

# Directory Structure
```
.                                         // Root folder
+-- .swagger-codegen                      // All swagger codegen related files in this folder
|   +-- config.json                       // Swagger codegen configuration - do not delete/modify unless specified
|   +-- swagger-codegen-cli.jar           // Swagger codegen executable - do not delete/modify
|   +-- VERSION                           // Auto-generated - do not delete/modify
+-- api                                   // API specifications folder
|   +-- openapi.yaml                      // [MODIFY] This is where you modify your API before codegen
+-- server                                // Auto-generated - do not delete/modify
|   +-- controller                        // [MODIFY] Code stubs for all your methods will be auto-generated here. Update them here.
|   +-- models                            // Auto-generated object schemas from API secifications - do not delete/modify
|   +-- swagger                           // Auto-generated - do not delete/modify
|   |   +-- swagger.yaml                  // Auto-generated - do not delete/modify
|   +-- test                              // Auto-generated - do not delete/modify
|   |   +-- __init__.py                   // Auto-generated - do not delete/modify
|   |   +-- additional_requirements.txt   // [Modify] Any required packages/dependencies for your tests must be specified here. Docker will automatially install them.
|   |   +-- test.py                       // [MODIFY] Write your unit tests here
|   +-- __init__.py                       // Auto-generated - do not delete/modify
|   +-- __main__.py                       // Auto-generated - do not delete/modify
|   +-- encoder.py                        // Auto-generated - do not delete/modify
|   +-- requirements.txt                  // [Modify] Any required packages/dependencies for your microservice must be specified here. Docker will automatially install them.
|   +-- util.py                           // Auto-generated - do not delete/modify
+-- .dockerignore                         // Do not delete/modify
+-- .gitignore                            // Do not delete/modify
+-- .swagger-codegen-ignore               // [Modify] Update to prevent files from being overwritten by the code generator
+-- docker-compose.yaml                   // [Modify] Update to modify your microservice launch file
+-- Dockerfile                            // [Modify] Update to modify your microservice docker image (e.g. if some manual installation is needed)
+-- Jenkinsfile_dev                       // Required for CI - do not delete/modify
+-- Jenkinsfile_master                    // Required for CI - do not delete/modify
+-- README.md                             // [MODIFY] Update instructions to build and run your microservice
+-- version.yml                           // [MODIFY] Update version information for your microservice here
```

# Setup your development environment
Follow the [Getting Started Guide](https://slb-swt.visualstudio.com/bit-inspection/_git/documentation?path=%2FGettingStarted.md&version=GBmaster) to set up your development environment if you haven't already.

We recommend the use of the following tools to aid your development:
* [Java 8 or above](https://www.java.com/en/download/)
* [Docker CE](https://docs.docker.com/install/)
* [Docker compose](https://docs.docker.com/compose/install/)
* [Git](https://git-scm.com/downloads)
* [Swagger inspector](https://inspector.swagger.io/builder): Web-based client for exercising your microservice
* Swagger editor: [online](https://editor.swagger.io/) or follow the [instructions here](https://slb-swt.visualstudio.com/bit-inspection/_git/documentation?path=%2FGettingStarted.md&version=GBmaster) to set up a local docker installation.



# Prerequisites
This microservice has the following prerequisites:
* Python 3.5.2+

# Installation from Source
Clone this repository:
```
$ git clone slb-swt@vs-ssh.visualstudio.com:v3/slb-swt/bit-inspection/template-python-server
```

## Option 1: Build and Launch using Docker compose
```
$ cd template-python-server
$ docker-compose up
```

## Option 2: Build and Launch using Docker
```
$ cd template-python-server
$ docker build -t template-python-server .
$ docker run -p 20000:5000 --name template-python-server template-python-server
```

## Stopping your microservice
If you launched your microservice using docker-compose:
```
$ docker-compose down --rmi all
```
If you launched your microservice using docker:
```
$ docker container stop template-python-server
```

# Usage
Go to [Swagger Inspector](https://inspector.swagger.io/builder) and execute the following:

`GET` http://localhost:20000/api/v1/account

Expected Result:
```
{
    "balance": 100
}
```  

Try depositing $1000 to your bank account (by performing a `PUT`):

`PUT` http://localhost:20000/api/v1/account

With the following body:
```
{
  "amount": 1000
}
```
The expected result is as follows:
```
{
    "balance": 1100
}
```   

Now, try withdrawing $800 from your bank account (also by performing a `PUT`) with the following body:
```
{
  "amount": -800
}
```
The expected result is as follows:
```
{
    "balance": 300
}
```
# Supporting API spec
The codegen engine provided in this template supports both **OAS2** and **OAS3**.

# How to Modify

1. Start by updating your API here: `api/openapi.yaml`
2. Ensure that the files and folders you don't want regenerated are included in the `.swagger-codegen-ignore` file. For example, if you don't want `account_controller.py` to be overwritten, add the following line to the `.swagger-codegen-ignore` file:
```
server/controller/additional_controller.py
```
3. Autogenerate using codegen:
```
$ cd template-python-server
$ java -jar .swagger-codegen/swagger-codegen-cli.jar generate -i api/openapi.yaml -l python-flask -c .swagger-codegen/config.json
```
After this, you should see the following files generated or changed:
```
server/swagger/swagger.yaml
server/controller/*_controller.py
server/models/*.py
```

4. Delete the autogenrated tests from `test` folder

5. Ensure that the models and controllers are generated properly.

More information on swagger-codegen can be [found here](https://github.com/swagger-api/swagger-codegen).

# How to Set Version
You will modify the version number in the `release-config.yml` file. 
```
version: '1.0'                               // [MODIFY] This is the version of this development, MAJOR.MINOR
image_name: 'template-python-server'         // [MODIFY] This will be the name of the image when released to the docker container registry. Therefore, this has to be unique
docker_registry_url: '163.188.39.81:5000'    // This is the url of the Docker Registry - Do not delete/modify
```

Please refer to [this link](https://dev.azure.com/slb-swt/bit-inspection/_git/documentation?path=%2FSettingVersion.md&version=GBmaster) on how to set the version. 

# CI Integration
CI pipelines have been set up for the `dev` and `master` branches for this repository in our lab's Jenkins CI server:
- [DEV Branch]      http://163.188.39.81:8090/job/template-python-server-dev/
- [MASTER Branch]   http://163.188.39.81:8090/job/template-python-server-master/

Please refer to [this guide for more information on how to create a CI pipeline in Jenkins](https://slb-swt.visualstudio.com/bit-inspection/_git/documentation?path=%2FCIServerSetup.md&version=GBmaster).

# Troubleshooting
If you ran into a problem  similar to this:
```
connexion.exceptions.ResolverError: <ResolverError: Empty module name>
```
Go to `/server/swagger/swagger.yaml` and see if the autogenerated line:
`x-swagger-router-controller: "server.controller.account_controller"`
points to the correct controller. 
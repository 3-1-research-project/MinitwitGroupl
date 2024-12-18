###### Main branch
![Lint and Test - Main Branch](https://github.com/MinitwitGroupI/Minitwit/actions/workflows/lint-and-test.yml/badge.svg?branch=main)

![Deployed to Server - Main Branch](https://github.com/MinitwitGroupI/Minitwit/actions/workflows/deploy.yaml/badge.svg?branch=main)

# Energy Measurement
To run the application you must first spin up a posgres instance

```
cd src/db/
docker build -t group-l-posgres .
docker run --name group-l-posgres -p 5432:5432 -e POSTGRES_PASSWORD=1234 -e POSTGRES_HOST_AUTH_METHOD=trust -d group-l-posgres
```

Then the app can be run from the [src/backend/](./src/backend/) folder with the following command

```
gunicorn --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker main:app
```

# MiniTwit

MiniTwit is a messaging application which was converted from Flask to FastAPI framework.

You can find the deployed application [here](https://opsdev.gg) or https://opsdev.gg

![Landing Page](docs/images/landingpage.png?raw=true)

### All Url's: 
*  [Main page](https://opsdev.gg)
*  [Elastic](http://opsdev.gg:5601) (Username: helgeandmircea, password: sesame0uvr3toi)
*  [Grafana](http://opsdev.gg:3000/d/DVJQxp-4k/minitwit-responses?orgId=1)

## How to install and run the application

### Prerequisites: 
- Docker must be installed.
- Inside src/backend there is a file called [".env_sample"](src/backend/.env_sample). Input all necessary fields and rename the file to ".env".

### How to install and run the application:

Inside src/ there is a [docker-compose.yml file](src/docker-compose.yml).
Composing this file up will generate all necessary containers, volumes and files to run the application.

Once the containers have been deployed: navigate to http://localhost:8000 to access the main page.

## How to install required dependencies

All required dependencies will be installed once docker-compose file is executed.

However, in the rare case that there is no way to run docker containers. You can find the list of all dependencies [here](src/backend/requirements.txt) or inside src/backend/requirements.txt

## Contributing

Anyone is welcome to [contribute](docs/CONTRIBUTE.md),
however, if you decide to get involved, please take a moment to review
the [guidelines](docs/CONTRIBUTE.md).

## Logging

The team employs efficient logging infrastructure to track errors and other forms of data. Check out the teams [Postmortem](docs/Postmortems.md) report for a more detailed view on how the team tracks and manages errors.

## SLA

The team is commited to providing excelent service to their customers. Check out our commitments [here](docs/SLA.md).

## Security report

The team is proud to support our fellow students by evaluating [their applications security](docs/security%20report/Group%20I%20%20-%20Security%20Assessment%20Findings%20Report.pdf).

Additionally, the team would like to thank [Group d CI/CDont](https://github.com/kjaerb/DevOps-CI-CDont) for their [contributions to the security of the application](docs/group%20d%20security%20report/sec_report_group_i.md).

## License

The code is available under the [MIT license](LICENSE).
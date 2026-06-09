# global-product-lab-sandbox

GP&Ds home for product prototypes, Claude skills, and shared context/data. Central monorepo for Global Product & Design (GP&D) prototypes, experiments, and AI tooling — individual project builds, reusable Claude skills, shared context, and supporting data/assets..

`global-product-lab-sandbox` includes the following components:

## Creating additional components

To create additional components within an existing repository...

1. Create directory for `<new-component>` in `global-product-lab-sandbox`: `mkdir <new-component>`
1. Create and configure an `.omd/<new-component>/now.yaml` file. For additional assistance related to OMD, feel free to connect with the team on the Slack channel #wbd-omd-help.
1. Create a `<new-component>/sonar-project.properties` file configuring the [SonarCloud project](https://docs.sonarcloud.io/advanced-setup/ci-based-analysis/sonarscanner-cli/)
1. Create a `<new-component>/Makefile` with standard built targets (details TBD; stay tuned!)

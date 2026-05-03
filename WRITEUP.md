# WRITEUP.md

## Resource Choice Analysis: VM vs App Service

For deploying the CMS application, two main Azure options were considered: Virtual Machine (VM) and App Service.

### 1. Virtual Machine (VM)

* **Cost**: Requires continuous running resources, which increases cost over time.
* **Scalability**: Manual scaling is required, which makes it less flexible.
* **Availability**: Needs manual configuration for high availability and backups.
* **Workflow**: Requires full setup and maintenance of OS, dependencies, and server configuration.

### 2. Azure App Service

* **Cost**: More cost-effective, especially with the free or basic tiers.
* **Scalability**: Easily scalable with built-in auto-scaling features.
* **Availability**: Managed service with high availability provided by Azure.
* **Workflow**: Simple deployment using GitHub integration and minimal configuration.

### Final Decision

Azure App Service was chosen for deploying this project because it simplifies the deployment process and reduces the need for manual server management. It is ideal for web applications like this CMS, where quick setup, easy scaling, and minimal maintenance are important. The integration with GitHub also made continuous deployment straightforward.

---

## Changes That Could Affect This Decision

If the application becomes more complex in the future, such as requiring custom OS-level configurations, background services, or advanced networking setups, then a Virtual Machine might be a better choice. Additionally, if full control over the environment is needed or if the application requires specific system-level dependencies, switching to a VM would be more suitable.

For the current project scope, however, Azure App Service is the most efficient and practical option.

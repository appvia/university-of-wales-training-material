
# Azure Key Vault Overview

Azure Key Vault is a cloud service that provides a secure storage solution for secrets, keys, and certificates. Understanding what information to store in each part of the Key Vault - keys, secrets, and certificates - is essential for effectively utilising its capabilities.

## Keys

In the **Keys** section of Azure Key Vault, cryptographic keys are stored. These keys are used for various purposes, including encrypting and decrypting data, digital signing, and verification of signatures. Azure Key Vault supports multiple key types and algorithms, such as RSA and elliptic curve keys.

### Use Cases for Keys
- **Encrypting/Decrypting Data**: Keys can be used to encrypt data before storing it in a database or storage account and decrypt it when necessary.
- **Digital Signatures**: Utilise keys to digitally sign documents or tokens, allowing the recipient to verify the integrity and origin of the data.
- **Key Wrapping/Unwrapping**: Encrypt other keys or secrets for secure storage or transfer using keys.

## Secrets

The **Secrets** section of Azure Key Vault is designed for storing sensitive string data that does not require the cryptographic operations provided for keys. This includes passwords, connection strings, API keys, and other sensitive information that applications might need to access securely.

### Use Cases for Secrets
- **Database Connection Strings**: Securely store sensitive database connection details and access them dynamically from your applications.
- **API Keys**: Keep third-party API keys secure and manage them centrally.
- **Application Passwords**: Store passwords used by your applications to access other services or resources securely.
- **Certificates**: Although Azure Key Vault has a dedicated section for certificates, the private keys of certificates can be regarded as secrets. The "Certificates" section automates certain aspects of certificate management, but fundamentally, it's leveraging the capabilities of keys and secrets.

## Certificates

Though not initially asked for, it's worth mentioning that the **Certificates** section is for managing X.509 certificates. Azure Key Vault automates tasks like the renewal and deployment of certificates used for SSL/TLS on web servers or for other purposes requiring public key infrastructure (PKI).

## Summary

- **Keys** are used for cryptographic operations that require asymmetric key pairs or symmetric keys, crucial for operations like encryption, decryption, and digital signing.
- **Secrets** are used for storing sensitive information that does not require cryptographic operations, such as passwords, tokens, or connection strings.

By understanding these distinctions and use cases, you can more effectively leverage Azure Key Vault to secure your applications and services.


# 2. Using Azure Key Vault in the Azure Portal

This guide provides a simple walkthrough on how to create an Azure Key Vault, add a secret to it, and retrieve the secret, all directly through the Azure Portal. This process is ideal for securely storing and managing sensitive information like passwords, connection strings, and more.

## Step 1: Create an Azure Key Vault

1. **Sign In**: Go to the [Azure Portal](https://portal.azure.com) and sign in with your Azure account.

2. **Navigate to Key Vaults**: Use the search bar to find and select "Key Vaults".

3. **Create a Key Vault**:
    - Click on "+ Create" to initiate the creation process.
    - Fill out the "Basics" tab with the appropriate Subscription, Resource Group, Key Vault Name, and Region.
    - Adjust any other settings as necessary, then click "Review + create", followed by "Create" to deploy the Key Vault.

## Step 2: Add a Secret to Your Key Vault

1. **Access Your Key Vault**: Once created, open your Key Vault by selecting it from your resource group or the deployment confirmation page.

2. **Access Via IAM**:
    - Click on Access control (IAM)
    - Press the `Add` button
    - Select `Add Role Assignment`
    - In the search box type: `Key Vault Administrator`
    - Click `Next`
    - On the next page click `Select Members`
    - On the side panel select your username and click `Select`
    - Click `Review and Assign`
    - Click `Create` 

This will provide you access to create secrets 

3. **Add a Secret**:
    - Within the "Settings" section, navigate to "Secrets".
    - Click on "+ Generate/Import" to create a new secret.
    - Provide a Name for your secret and input the Value that you want to store.
    - Set any additional configurations as needed and click "Create".

## Step 3: Retrieve a Secret from Your Key Vault

1. **Find Your Secret**:
    - In the "Secrets" section of your Key Vault, click on the secret you wish to access.
    - Select the specific version of the secret.
    - To view the secret's value, click on "Show secret value". Note that you may need appropriate permissions to perform this action.


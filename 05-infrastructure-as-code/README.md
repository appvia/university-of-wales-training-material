# Infrastructure as Code

## 1. Installing Terraform on Windows

### Step 1: Download Terraform

    Download the terraform tool from [this link](https://releases.hashicorp.com/terraform/1.7.5/terraform_1.7.5_windows_386.zip)

### Step 2: Install Terraform

1. Extract the .zip file you downloaded. It contains a single executable file, terraform.exe.
1. Decide on a location to store the Terraform binary. A common choice is C:\Terraform\.
1. Move the terraform.exe file to your chosen location.

### Step 3: Set Up the Path Environment Variable

1. Open the Start Search, type in "env", and choose "Edit the system environment variables".
1. In the System Properties window, click the "Environment Variables…" button.
1. In the Environment Variables window, under the "System variables" section, find the Path variable and select it. Click "Edit…".
1. In the "Edit Environment Variable" window, click "New" and add the path to the folder where you placed your Terraform executable. For example, C:\Terraform\.
1. Click "OK" on all windows to close them.

### Step 4: Verify the Installation

1. Open a new Command Prompt window (cmd.exe) or PowerShell window.
1. Type `terraform` and press Enter.
1. If the installation was successful, you should see Terraform's help output.

## 2. Steps Required to Create Azure Resource Group

Before you begin: Make sure you have an Azure account. If you don’t have one, you can create a free account at Azure's website.

### Step 1: Install the Azure CLI

1. Download and install the Azure CLI from Azure CLI from [here](https://aka.ms/installazurecliwindowsx64)
1. Once installed, open a command prompt or PowerShell and log in to your Azure account by running: `az login`
1. Follow the prompts to complete the login process.

### Step 2: Create a Service Principal for Terraform

1. Open [portal.azure.com](https://portal.azure.com), in the search box, type subscription, you will see subscription in a table, get the subscriptionid from the table.
1. In your command-line interface, run the following command to create a service principal:
    `az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/YOUR_SUBSCRIPTION_ID"`
Replace YOUR_SUBSCRIPTION_ID with your Azure subscription ID with the Id from above.
This command will output several values. Note down the appId, password, tenant, and name. You'll use these in your Terraform configuration.

### Step 3: Configure Terraform to Use the Service Principal

1. Create a directory for your Terraform configuration files.
1. For example go to C drive and create a new folder called `terraform`.
1. Inside this directory, create a file named `main.tf`.
1. Edit `main.tf` to include the following configuration, replacing placeholders with the actual values from the previous step:

```shell
provider "azurerm" {
  features {}
  subscription_id = "SubscriptionId"
  client_id       = "AppId"
  client_secret   = "Password"
  tenant_id       = "Tennand"
}}

resource "azurerm_resource_group" "usw" {
  name     = "usw"
  location = "UK South"
}
```

### Step 4: Initialize Terraform

1. Open a command prompt or PowerShell window in the directory where your main.tf file is located.
1. Run: `C:\terraform> terraform init`
This command initializes Terraform and downloads the necessary providers.

### Step 5: Create the Resource Group

1.Run `C:\terraform>terraform plan`
This shows what actions Terraform will perform.

1. If everything looks correct, run: `C:\terraform>terraform apply`
When prompted, type `yes` to proceed with the creation of resources.
Terraform will now create the specified Azure Resource Group.

### Step 6: Verify the Resource Group

Login to `https://portal.azure.com` and type Resource Group in the search box, you will see the resource created

## 3. Create Virtual Machine

Now we will update the `main.tf` file and add a Virtual machine to the existing resource group. Add the following code to the bottom of existing `main.tf`

This creates a Virtual Network, Subnet, Public IP, and Network Interface for the VM.

### Step 1: Define the Network Components

```shell
resource "azurerm_virtual_network" "example_vnet" {
  name                = "exampleVNet"
  address_space       = ["10.0.0.0/16"]
  location            = "UK South"
  resource_group_name = "usw"
}

resource "azurerm_subnet" "example_subnet" {
  name                 = "exampleSubnet"
  resource_group_name  = "usw"
  virtual_network_name = azurerm_virtual_network.example_vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_public_ip" "example_public_ip" {
  name                = "examplePublicIP"
  location            = "UK South"
  resource_group_name = "usw"
  allocation_method   = "Dynamic"
}

resource "azurerm_network_interface" "example_nic" {
  name                = "exampleNIC"
  location            = "UK South"
  resource_group_name = "usw"

  ip_configuration {
    name                          = "exampleNicConfiguration"
    subnet_id                     = azurerm_subnet.example_subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.example_public_ip.id
  }
}
```

### Step 2: Create the Windows Virtual Machine

This configuration creates a basic Windows Server VM. Add the following code to the `main.tf` file

```shell
resource "azurerm_windows_virtual_machine" "example_vm" {
  name                = "exampleVM"
  resource_group_name = "usw"
  location            = "UK South"
  size                = "Standard_B1s"
  admin_username      = "vm-admin"
  admin_password      = "your-password-here12!"
  network_interface_ids = [
    azurerm_network_interface.example_nic.id,
  ]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "MicrosoftWindowsServer"
    offer     = "WindowsServer"
    sku       = "2022-Datacenter"
    version   = "latest"
  }
}
```

1. Run `C:\terraform>terraform plan` 
2. Apply the configuration to create the resources with `C:\terraform>terraform plan`. Confirm the action by typing yes when prompted.
3. Login to azure portal to see the created resources.

# 4. Delete everything

1. Run `C:\terraform>terraform destroy`
2. Confirm the action by typing `yes` when prompted
3. All created resources will be deleted.
# GitHub Actions

## Step 1: Create a Custom ARM Template
Copy  the Azure Resource Manager (ARM) template from the link. This  defines all the resources we will be using to deploy our banking application custom resources and their configurations.


## Step 2: Deploy the Custom Template
* Navigate to the "Deploy a custom template" option or from the left-hand navigation pane in the Azure Portal.
* Click on "Build your own template in the editor" or "Load file" to upload the custom ARM template you created in Step 1.
* Click on "Save" to save the template configuration.

## Step 3: Fill in the deployment details:
* Subscription: Choose the Azure subscription where the custom resources will be deployed.
* Resource group: select "Create new". Please name your resource group as "primary"  
* Region: Choose the Azure region where the resources will be deployed.
* Template parameters: Enter values for any parameters defined in your custom ARM template.

## Step 4: Validate and Deploy
* Click on "Review + create" to validate the deployment configuration.
* Review the summary to ensure accuracy.
* Click on "Create" to initiate the deployment.


## Step 5: Monitor Deployment
Azure will start the deployment process, which may take some time depending on the complexity of your custom template.
Monitor the deployment progress in the "Notifications" or "Deployments" section.

## Step 6: Verify Resources
* Once the deployment is complete, navigate to the resource group you created in Step 2.
* Verify that the custom resources defined in your ARM template are successfully deployed and functioning as expected.
* Click on the Primary-lbPublic IP address created
* Copy and past IP address on a new windows tab
* This will resolve to a simple hello world application

## Step 7: Validation
We simulate DR scenario by stopping two of our Virtual machines to see if our application is still available 
Firstly stop one of the VMs created by searching for Primary-vm1 and on the overview tab click stop.
Repeat the following steps for Primary-vm2


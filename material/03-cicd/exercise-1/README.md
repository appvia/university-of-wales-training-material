# GitHub Actions

We will be using GitHub Actions to push images to a Docker Container Registry. For this exercise we will be pushing the Docker image that you create locally into the Docker Hub Container Registry that you created in Docker exercises. For Azure you will be using a similar setup. If you have not completed Docker `exercise-01` please complete [this](https://github.com/bank-of-england-technology/developer-training/tree/main/material/02-docker/exercise-1#container-registry) before doing this exercise. 

Open the training repository that you created at the begining of your workshop in Visual Studio. You should have the following files

```
index.html
Dockerfile
README.md
```

We will be adding a GitHub Action CI file in the repo.

Create folder called `.github` 
Inside `.github` folder create another folder called `workflows` 
In the `workflows` folder create a new yaml file called `build-image.yaml` 

Copy and paste the following text in `build-iamge.yaml` file 

```yaml
name: ci

on:
  push:
    branches:
      - 'main'

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      -
        name: Set up QEMU
        uses: docker/setup-qemu-action@v1
      -
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1
      -
        name: Login to DockerHub
        uses: docker/login-action@v1 
        with:
          username: ${{ secrets.DOCKER_HUB_USERNAME }}
          password: ${{ secrets.DOCKER_HUB_PASSWORD }}
      -
        name: Build and push
        id: docker_build
        uses: docker/build-push-action@v2
        with:
          push: true
          tags: salmaniqbal/web-app:ci
      -
        name: Image digest
        run: echo ${{ steps.docker_build.outputs.digest }}
```

In the file where it says `tags: salmaniqbal/web-app:ci` replace `salmaniqbal` with your Docker Hub Repository name. 

We need to provide GitHub Actions Username and Password for your DockerHub registry:

1. Open your personal training repository and click on the `Settings` tab.  
2. From the menu on the left click on `Secrets`
3. On the right you will see a `New repository secret` button, click it
4. For `Name` insert `DOCKER_HUB_USERNAME`
5. For `Value` insert your Docker Hub Username
6. Click `Add secret` -> the secret is now stored in the repository, no one can see the value apart from the pipeline. Once the value is set even you cannot see the value.
7. Click `New repository secret` button again
8. For `Name` insert `DOCKER_HUB_PASSWORD`
9.  For `Value` insert your Docker Hub password
10. Click `Add Secret`

Now the secrets are saved in the repositor for the pipeline to be reused. 

If you see your `build-image.yaml` file, you will notice this section:

```yaml
        name: Login to DockerHub
        uses: docker/login-action@v1 
        with:
          username: ${{ secrets.DOCKER_HUB_USERNAME }}
          password: ${{ secrets.DOCKER_HUB_PASSWORD }}
```

This is using a pre-built action called `docker/login-action@v1` that allows the peipline to login to DockerHub using the secrets you just provided. We can use the same action to login to any container registry including Azure Container Registry, have a look at [this](https://github.com/marketplace/actions/azure-container-registry-login) to see how you can allow Github Actions to login to ACR. There are many actions available, for more details you can see the documentation [here](https://docs.github.com/en/actions).

The job that builds and pushes the image is:

```yaml
        name: Build and push
        id: docker_build
        uses: docker/build-push-action@v2
        with:
          push: true
          tags: salmaniqbal/web-app:ci
```

Just like the docker login action, this uses an existing action, which looks at the root directory of your repository, takes all the files, runs `docker build` and `docker push`! Sweet!

Now we are ready to check in the file. Run the following commands in git bash in root folder of your:

`git add .`  
`git commit -m "add ci file"`  
`git push`  

Open your training repo in the browser and click on the `Actions` tab. You should see a build running, open and look at the logs. Once completed, you should login to your DockerHub repo and see that a new tag called `ci` has been pushed to your Docker Hub `web-app` reporistory. Well done, you have created a pipeline that pushes an image everytime a changes has been pushed.

Pushing the same tag everytime for Docker image is not best practice, we did it in this exercise for simplicity. Usually, docker images have versions or Git Commit SHA's as the image tags, have a look at [this](https://www.lotharschulz.info/2020/07/23/github-packages-docker-image-tags-customization-with-github-actions/) for more details on customising docker tags. Or you can use [Semantic Versioning Action](https://github.com/marketplace/actions/docker-publish-semver-tags) to tag your images using Semantic Version such as `v1.2.3`

If you would like to learn about how to build and test dotnet applications, have a look at [this action](https://github.com/actions/setup-dotnet)

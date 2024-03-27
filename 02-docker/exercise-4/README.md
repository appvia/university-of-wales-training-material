

# Windows Containers

Follow the guide [here](https://learn.microsoft.com/en-us/virtualization/windowscontainers/quick-start/run-your-first-container#run-a-windows-container) to enable Windows containers on Docker Desktop.

### .NET Framework

Have a look at [this](https://github.com/Microsoft/dotnet-framework-docker) tutorial for ASP .NET and .NET Framework containers.

### Nano Server

`docker pull mcr.microsoft.com/windows/nanoserver:ltsc2022
`

`docker run -it mcr.microsoft.com/windows/nanoserver:ltsc2022`

This will allow you to run powershell in `nanoserver`. Have a look [here](https://hub.docker.com/_/microsoft-windows-nanoserver) for more information.

### IIS

[microsoft/iis](https://hub.docker.com/_/microsoft-windows-servercore-iis) image is based on Windows Server Core and is around 4GB when downloading (sad face).

In order to run default IIS page you can run the following command:

`docker run -d -p 8082:80 microsoft/iis ping -t localhost`

If you access localhost:8082 you will see the default IIS web page.

If you would like to create your own ASP.NET app, you can use following `Dockerfile`

```
FROM microsoft/iis

RUN ["powershell.exe", "Install-WindowsFeature NET-Framework-45-ASPNET"]  
RUN ["powershell.exe", "Install-WindowsFeature Web-Asp-Net45"]

COPY web/app/ c:\\web-app

EXPOSE 8081

RUN powershell New-Website -Name 'my-app' -Port 8081 -PhysicalPath 'c:\web-app' -ApplicationPool '.NET v4.5'

ENTRYPOINT powershell  
```

Have a look at [this](https://docs.microsoft.com/en-us/dotnet/core/docker/build-container?tabs=windows) tutorial for containerising .NET Core apps

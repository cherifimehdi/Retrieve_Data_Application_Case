# Efficient Network Devices Data Retrieving - Application case of Validate/Monitor access to network devices with the integration of Genie/pyATS, WebEx Messenger and Syslog server use case

This use case shows an efficent and optimized way to retrieve data from network devices with checking access process by leveraging the [Validate/Monitor access to network devices with the integration of Genie/pyATS, WebEx Messenger and Syslog server](https://developer.cisco.com/network-automation/detail/31f2a492-d5b7-11eb-95a0-c6918c6fb71b/) use case relating with the project [Check_Access](https://developer.cisco.com/codeexchange/github/repo/cherifimehdi/Check_Access).

Suppose we have 100 network devices and we have access only to 50 of them, the retriving data process is applied only to these 50 devices witch conduct to save the time with generating logs to Syslog server for maintenance purposes besides the report sent to WebEx Messenger Space.

In summary, this project aims to : 

- Check if there is an access to the network devices and generating notification for eeach of them to Syslog server and as report incorporated in text file to WebEx Messenger Space.
- Retrieve data only form devices on witch there is access and generate notifications to Syslog server for both case : Retrieving Success or Not 
      
# Remark
We focus here only on the result for the Syslog server notifications and the package installation and requirements, the others details like configuration files modification, topology and the WebEx Messenger result could be found at [Check_Access](https://developer.cisco.com/codeexchange/github/repo/cherifimehdi/Check_Access) repository related to [Validate/Monitor access to network devices with the integration of Genie/pyATS, WebEx Messenger and Syslog server](https://developer.cisco.com/network-automation/detail/31f2a492-d5b7-11eb-95a0-c6918c6fb71b/) use case as it is a part of this project.


## Related Sandbox

Cisco DevNet Sandbox [Cisco Modeling Labs](https://devnetsandbox.cisco.com/RM/Diagram/Index/45100600-b413-4471-b28e-b014eb824555?diagramType=Topology)

## Related Repository

[Check_Access](https://github.com/cherifimehdi/Check_Access)

## Solutions on Ecosystem Exchange
How pyATS can be used as an end-to-end DevOps automation ecosystem: [Accelerating your DevOps with pyATS](https://developer.cisco.com/pyats/)

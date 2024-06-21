# Author : Mehdi CHERIFI
# Note : Please make sure to apply your <YOUR_SYSLOG_SERVER> and <YOUR_ROOM_ID> in the required emplacement
# Please refer to https://github.com/cherifimehdi/Check_Access for more details about this project 

import os
from genie.testbed import load
from prettytable import PrettyTable
import logging.handlers
from logging import Formatter
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from dotenv import load_dotenv
from pprint import pprint


def Check_Access_Use(token, testbed):

   Table_Result = PrettyTable(["Device", "Status"])
   Table_Result.padding_width = 1
   Table_Result.title = 'Access Check'

   #Save the decision for further use
   Device_Decision={}

   #Try access to each device and generate logs to send to the Syslog server and to save the result as table

   for device in testbed.devices:
      try:
         testbed.devices[device].connect(log_stdout=False)

         MSG = f'No Access Issue with {device} device'
         my_logger.info(MSG)
         Table_Result.add_row([str(device),"Access Ok"])
         Device_Decision[str(device)]="Access Ok"
      
      except Exception as e:

         MSG = f'Access Issue with {device} device!!!, please proceed for a solution'
         my_logger.info(MSG)
         Table_Result.add_row([str(device),"No Access"])
         Device_Decision[str(device)]="No Access"

   print(Table_Result)

   #Send Table_Result as a text file to Webex Teams Space

   with open('Result.txt', 'w') as w:
       w.write(str(Table_Result))

   m = MultipartEncoder({'roomId': '<YOUR_ROOM_ID>',
                         'text': 'CHECK ACCESS RESULT  !!!',
                         'files': ('Result.txt', open('Result.txt', 'rb'),
                         'document/txt')})
   r = requests.post('https://webexapis.com/v1/messages', data=m,
                     headers={'Authorization': 'Bearer '+token,
                    'Content-Type': m.content_type})

   return Device_Decision


def Retrieve_Data(Device_Decision,testbed):
   for Device, Decision in Device_Decision.items():

      if Decision=="Access Ok":
         MSG = f'Retrieving Data Process for {Device} begin'
         my_logger.info(MSG)

         testbed.devices[Device].connect(log_stdout=False)
         result=testbed.devices[Device].parse("show ip interface brief")
         print(100*'0')
         print(f'Result for {Device}')
         print(100*'0')
         pprint(result)
         print(100*'0')

      else:
         MSG = f'NO Retrieving Data Process for {Device} : Refer to Result.txt for more infos'
         my_logger.info(MSG)
         print(f'NO Retrieving Data Process for {Device} : Refer to Result.txt for more infos')

if __name__ == "__main__":
   load_dotenv()
   token = os.getenv("Token")
   testbed=load('connex.yml')
   my_logger = logging.getLogger('MyLogger')
   my_logger.setLevel(logging.INFO)

   handler = logging.handlers.SysLogHandler(address = ('<YOUR_SYSLOG_SERVER>',514))
   my_logger.addHandler(handler)

   log_format = '[%(levelname)s] \"%(message)s\"'
   handler.setFormatter(Formatter(fmt=log_format))
   Retrieve_Data(Check_Access_Use(token,testbed), testbed)



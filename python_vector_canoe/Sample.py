# -*- coding: UTF-8 -*-
#.Data:2018/5/19

import CANoe
import time

app = CANoe.CANoe() #CANoe app

app.open_simulation("puru_ecu.cfg") #CANoe congif

app.start_Measurement() #CANoe

var_from_namespace = app.get_all_SysVar("mfl") #namespace

print(app.get_SysVar("mfl","vol_plus")) #environment variable 

app.set_SysVar("mfl","vol_plus",1)  #defined range to set the variable

app.stop_Measurement() #CANoe

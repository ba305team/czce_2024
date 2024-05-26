#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 13:45:31 2024

@author: zichengli
"""

#from fastapi import FastAPI  
  
# 创建一个FastAPI应用程序实例  
#app = FastAPI()  
  
# 定义路由（使用装饰器将函数绑定到特定的路径和HTTP方法）  
#@app.get("/")  
#async def root():  
    #return {"message": "Hello World"}  
  
#@app.get("/items/{item_id}")  
#def read_item(item_id: int, q: str = None):  
    #return {"item_id": item_id, "q": q} 

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  


class PortInfo(BaseModel):
    port: str
    cargo: int
    sd_ma: float
    query_string: Optional[bool] = None
    

@app.get('/')
async def hello_world():
    return {'hello': 'world'}


@app.get('/port/{port}')
async def result(port: str, 
                 cargo: int, 
                 sd_ma: float, 
                 query_string: Optional[str] = None):
    return {'port': port, 'cargo': cargo, 'sd_ma': sd_ma, 'query_string': query_string}


@app.put('/port/{port}')
async def result(port: str, port_info: PortInfo):
    return {'port': port, 'cargo': port_info.cargo, 'sd_ma': port_info.sd_ma}

# 启动命令：uvicorn fastapi_tryout:app --reload
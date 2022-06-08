# fastapi imports
from fastapi import FastAPI, Request, Response, status, Depends, BackgroundTasks, HTTPException
from fastapi.middleware import Middleware

# schema imports
from typing import Dict, List, Optional
from enum import Enum
from pydantic import BaseModel, Field, validator, ValidationError, BaseConfig, create_model, HttpUrl, EmailStr

#responses imports
from starlette.responses import JSONResponse, RedirectResponse, HTMLResponse, StreamingResponse, FileResponse, Response

# enviroment variables
from os import getenv
from dotenv import load_dotenv
load_dotenv()
FAUNA_SECRET = getenv('fauna_secret') 

# fauna imports
from faunadb import query as q
from faunadb.client import FaunaClient
from faunadb.objects import Ref, Query, FaunaTime, _Expr
from faunadb.errors import FaunaError
from faunadb.page import Page

# boto3 imports
from boto3 import ec2, dynamodb, s3, client, resource, session, exceptions

# here comes the fun part

main = FastAPI()

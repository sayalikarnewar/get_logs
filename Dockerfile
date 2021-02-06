FROM python:3.7

RUN pip3 install asyncio
RUN pip3 install motor
RUN pip3 install aiohttp
RUN pip3 install pymongo
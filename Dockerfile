FROM python:3
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV BOT_TOKEN OTkyNzc1OTQxMzA4ODI5Njk2.GqIRpV.OdNYMoMTMdKCPH6kI74hVOsItDkSutcL1q0kQ0
ENTRYPOINT ["python3"]
CMD ["bot.py"]

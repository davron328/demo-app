# Node Hello World

Simple node.js app that servers "hello world"

Great for testing simple deployments to the cloud

## Dockerfile example  [link](https://www.middlewareinventory.com/blog/docker-nodejs-example/)

```
FROM node:10.15-alpine
LABEL author=”rahymov”

WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY ["package.json", "package-lock.json*", "./"]

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .
CMD [ "npm", "start" ]
```

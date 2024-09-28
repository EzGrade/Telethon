### STAGE 1: Build ###
FROM node:lts-alpine AS build

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY frontend/frontend/package*.json ./

# Install Angular CLI
RUN npm install -g @angular/cli

# Install project dependencies
RUN npm install

# Copy the project files
COPY frontend/frontend .

# Run the build
CMD npx ng serve --host 0.0.0.0 --port 4200
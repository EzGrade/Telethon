FROM node:alpine

WORKDIR /frontend

COPY /frontend/frontend /frontend

RUN npm install -g @angular/cli

RUN npm install

# Set the appropriate permissions
RUN chown -R node:node /frontend

# Ensure cache folder has correct permissions for the node user
RUN mkdir -p /frontend/frontend/frontend/.angular/cache && \
    chown -R node:node /frontend/frontend/frontend/.angular/cache

USER node

EXPOSE 4200

WORKDIR /frontend/frontend/frontend

CMD ng serve --host 0.0.0.0 --port 4200

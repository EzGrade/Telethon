FROM node:alpine

WORKDIR /frontend

COPY /frontend/frontend /frontend

RUN npm install -g @angular/cli

RUN npm install

EXPOSE 4200

WORKDIR /frontend/frontend/frontend

CMD ["npx", "ng", "serve", "--host", "0.0.0.0", "--port", "4200"]
FROM node:18 as frontend-builder

RUN npm --yes init react-app front

WORKDIR /front

COPY *.js src

ARG CI=true
RUN npm run test

RUN npm --yes run build

FROM nginx as runtime

COPY --from=frontend-builder /front/build /var/www/

COPY nginx.conf /etc/nginx/conf.d/default.conf

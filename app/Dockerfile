FROM node:20-alpine
RUN corepack enable pnpm

WORKDIR /app
COPY ./strudel .

RUN apk add --no-cache dumb-init python3 build-base pango-dev
RUN pnpm i --frozen-lockfile

EXPOSE 4321
CMD ["dumb-init", "pnpm", "start"]

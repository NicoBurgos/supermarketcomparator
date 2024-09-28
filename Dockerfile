FROM node:22-alpine

WORKDIR /app

COPY package.json .
COPY pnpm-lock.yaml . 

RUN npm install -g pnpm 
RUN pnpm install 

# Copiar el resto de tu aplicación
COPY . .

RUN pnpm build

# Comando para iniciar la aplicación
CMD ["pnpm", "start"]

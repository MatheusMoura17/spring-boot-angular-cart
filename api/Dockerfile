FROM gradle:jdk17-alpine

VOLUME /temp

WORKDIR /app

COPY ./src src
COPY ./settings.gradle settings.gradle
COPY build.gradle build.gradle
COPY gradle/ gradle

RUN gradle build

EXPOSE 8080
ENTRYPOINT ["java","-jar","build/libs/api-0.0.1-SNAPSHOT.jar"]

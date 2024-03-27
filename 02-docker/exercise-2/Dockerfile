FROM openjdk:8-jdk-alpine
COPY PingPong.java /
RUN javac PingPong.java
EXPOSE 8080
ENTRYPOINT ["java"]
CMD ["PingPong"]
FROM openjdk:7-alpine
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN javac Findcosine.java
EXPOSE 8080
CMD ["java", "Findcosine"]

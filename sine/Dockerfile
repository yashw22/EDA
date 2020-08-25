FROM centos:latest

RUN yum update -y
# add gfortran, debugging tools and make
RUN yum install -y gcc-gfortran gdb make 

# build code
COPY . /fortran/
WORKDIR /fortran/

RUN make findsine
CMD ["./findsine"]

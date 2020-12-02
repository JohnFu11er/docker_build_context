# docker_build_context

This repo is used as the source for the build context for a practice docker image build that
can be sourced with the example command below:

docker image build -t your_image_name https://github.com/JohnFu11er/docker_build_context.git


after building it can be run with:

docker container run -it --name your_container_name your_image_name

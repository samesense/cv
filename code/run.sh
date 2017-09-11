#boot2docker up
#eval "$(boot2docker shellinit)"
docker run --rm -v `pwd`:/latex samesense/docker-latex autobuild cv.tex


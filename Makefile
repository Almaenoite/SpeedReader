NAME			=	speedreader

all:				${NAME}

${NAME}:
			sudo docker build -t ${NAME} .
			sudo docker run -it --rm --name ${NAME} -e DISPLAY=$$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix ${NAME}

clean:
			sudo docker rmi ${NAME}

re:				clean all

.PHONY: 		all clean fclean re